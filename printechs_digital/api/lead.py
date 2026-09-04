# Copyright (c) 2026, Printechs and contributors

import json

import frappe
from frappe.utils import cstr, get_defaults, strip_html

from printechs_digital.api.email_templates import (
	demo_customer_confirmation_html,
	demo_sales_notification_html,
)


WEBSITE_QUOTE_SOURCE = "Website Quote"
WEBSITE_DEMO_SOURCE = "Website Demo"
WEBSITE_SOURCE = "Website"


def _text(value) -> str:
	return strip_html(cstr(value)).strip()


def _as_dict(value):
	if not value:
		return {}
	if isinstance(value, dict):
		return value
	if isinstance(value, str):
		try:
			parsed = json.loads(value)
		except Exception:
			return {}
		return parsed if isinstance(parsed, dict) else {}
	return {}


def _context_block(context: dict) -> str:
	lines = []
	for key, label in (
		("product", "Product"),
		("code", "Item Code"),
		("brand", "Brand"),
		("category", "Category"),
		("sourceUrl", "Page"),
		("configuration", "Configuration"),
		("preferredTime", "Preferred demo time"),
		("preferredContactMethod", "Preferred contact"),
	):
		value = _text(context.get(key))
		if value:
			lines.append(f"{label}: {value}")
	return "\n".join(lines)


def _ensure_lead_source(name: str) -> str | None:
	if frappe.db.exists("Lead Source", name):
		return name
	try:
		frappe.get_doc({"doctype": "Lead Source", "source_name": name}).insert(ignore_permissions=True)
		return name
	except Exception:
		if frappe.db.exists("Lead Source", WEBSITE_SOURCE):
			return WEBSITE_SOURCE
		return None


def _default_company() -> str | None:
	company = get_defaults().get("company")
	if company:
		return company
	return frappe.db.get_single_value("Global Defaults", "default_company") or frappe.db.get_value(
		"Company", {}, "name"
	)


def _get_or_create_lead(
	name: str,
	email: str,
	phone: str,
	company: str,
	source: str | None,
	whatsapp_no: str | None = None,
):
	existing = frappe.db.get_value("Lead", {"email_id": email}, "name")
	if existing:
		lead = frappe.get_doc("Lead", existing)
		changed = False
		if phone and not lead.mobile_no:
			lead.mobile_no = phone
			changed = True
		if whatsapp_no and not lead.whatsapp_no:
			lead.whatsapp_no = whatsapp_no
			changed = True
		if company and not lead.company_name:
			lead.company_name = company
			changed = True
		if changed:
			lead.flags.ignore_permissions = True
			lead.save(ignore_permissions=True)
		return lead

	lead = frappe.get_doc(
		{
			"doctype": "Lead",
			"lead_name": name,
			"email_id": email,
			"mobile_no": phone,
			"whatsapp_no": whatsapp_no or phone,
			"company_name": company,
			"status": "Lead",
		}
	)
	if source:
		lead.source = source
	lead.flags.ignore_permissions = True
	lead.insert(ignore_permissions=True)
	return lead


def _add_communication(doctype: str, name: str, subject: str, notes: str, sender: str):
	if not notes:
		return
	frappe.get_doc(
		{
			"doctype": "Communication",
			"communication_type": "Communication",
			"communication_medium": "Email",
			"sent_or_received": "Received",
			"subject": subject,
			"content": frappe.utils.escape_html(notes).replace("\n", "<br>"),
			"reference_doctype": doctype,
			"reference_name": name,
			"sender": sender,
		}
	).insert(ignore_permissions=True)


def _opportunity_item(context: dict, notes: str) -> dict | None:
	item_code = _text(context.get("code"))
	if not item_code or not frappe.db.exists("Item", item_code):
		return None

	item = frappe.db.get_value(
		"Item",
		item_code,
		["item_name", "description", "stock_uom", "item_group", "brand"],
		as_dict=True,
	)
	description = _text(item.description) or item.item_name
	configuration = _text(context.get("configuration"))
	if configuration:
		description = f"{description}\n\n{configuration}" if description else configuration
	elif notes:
		description = f"{description}\n\n{notes}" if description else notes

	return {
		"item_code": item_code,
		"item_name": item.item_name,
		"uom": item.stock_uom,
		"qty": 1,
		"rate": 0,
		"amount": 0,
		"base_rate": 0,
		"base_amount": 0,
		"description": description,
		"item_group": item.item_group,
		"brand": item.brand,
	}


def _create_opportunity(lead, context: dict, notes: str, source: str | None):
	company = _default_company()
	if not company:
		frappe.throw("Company is not set. Cannot create Opportunity.")

	product = _text(context.get("product")) or lead.lead_name
	title = f"Website Quote — {product}"[:140]
	item = _opportunity_item(context, notes)

	opportunity = frappe.get_doc(
		{
			"doctype": "Opportunity",
			"naming_series": "OPTY-" if "OPTY-" in (frappe.get_meta("Opportunity").get_field("naming_series").options or "") else "CRM-OPP-.YYYY.-",
			"opportunity_from": "Lead",
			"party_name": lead.name,
			"opportunity_type": "Sales" if frappe.db.exists("Opportunity Type", "Sales") else None,
			"status": "Open",
			"sales_stage": (
				"Proposal/Price Quote"
				if frappe.db.exists("Sales Stage", "Proposal/Price Quote")
				else None
			),
			"company": company,
			"contact_email": lead.email_id,
			"contact_mobile": lead.mobile_no,
			"title": title,
		}
	)
	if source:
		opportunity.source = source
	if item:
		opportunity.append("items", item)

	opportunity.flags.ignore_permissions = True
	opportunity.insert(ignore_permissions=True)
	return opportunity


def _sales_inbox() -> str:
	if frappe.db.exists("DocType", "Website Contact Settings"):
		try:
			doc = frappe.get_single("Website Contact Settings")
			if doc.specialist_email:
				return _text(doc.specialist_email)
		except Exception:
			pass
	return "info@printechs.com"


def _send_quote_emails(lead, opportunity_name: str | None, notes: str, preferred_contact: str):
	try:
		frappe.sendmail(
			recipients=[_sales_inbox()],
			subject=f"New website quote — {lead.lead_name}",
			message=(
				f"New quote request from the website.\n\n"
				f"Name: {lead.lead_name}\n"
				f"Company: {lead.company_name or '-'}\n"
				f"Email: {lead.email_id}\n"
				f"Phone: {lead.mobile_no or '-'}\n"
				f"Preferred contact: {preferred_contact or 'email'}\n"
				f"Lead: {lead.name}\n"
				f"Opportunity: {opportunity_name or '-'}\n\n"
				f"{notes}"
			),
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website quote sales notification failed")

	if preferred_contact != "email":
		return

	try:
		frappe.sendmail(
			recipients=[lead.email_id],
			subject="Quote request received — Printechs",
			message=(
				f"Dear {lead.lead_name},\n\n"
				"Thank you for contacting Printechs. We have received your quote request "
				"and our team will respond by email during business hours "
				"(Sunday–Thursday, 9:00 AM – 6:00 PM AST).\n\n"
				"For urgent enquiries, visit printechs.com/contact or message us on WhatsApp.\n\n"
				"Regards,\nPrintechs Team\ninfo@printechs.com"
			),
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website quote customer confirmation failed")


def _format_configuration(configuration: str) -> str:
	text = _text(configuration)
	if text.startswith("Configuration\n"):
		return text[len("Configuration\n") :]
	return text


def _send_demo_emails(lead, message: str, context: dict):
	product = _text(context.get("product")) or "Software demo"
	sales_html = demo_sales_notification_html(lead, context, message)
	try:
		frappe.sendmail(
			recipients=[_sales_inbox()],
			subject=f"New website demo request — {product}",
			message=sales_html,
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website demo sales notification failed")

	try:
		frappe.sendmail(
			recipients=[lead.email_id],
			subject="Demo request received — Printechs",
			message=demo_customer_confirmation_html(lead, product),
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website demo customer confirmation failed")


@frappe.whitelist(allow_guest=True)
def submit_lead():
	"""Create a CRM Lead, and for website quotes also an Opportunity."""
	data = frappe.local.form_dict or {}
	if isinstance(data, dict) and data.get("cmd"):
		payload = {key: value for key, value in data.items() if key != "cmd"}
	else:
		payload = data

	name = _text(payload.get("name"))
	email = _text(payload.get("email"))
	if not name or not email:
		frappe.throw("Name and email are required")

	company = _text(payload.get("company"))
	phone = _text(payload.get("phone"))
	message = _text(payload.get("message"))
	lead_type = _text(payload.get("type") or "quote")
	context = _as_dict(payload.get("context"))
	context_text = _context_block(context)
	notes = "\n\n".join(part for part in (message, context_text) if part)
	demo_message = message
	demo_notes = "\n\n".join(
		part
		for part in (
			f"Preferred demo time: {_text(context.get('preferredTime'))}"
			if _text(context.get("preferredTime"))
			else "",
			message,
			_format_configuration(context.get("configuration")),
		)
		if part
	)

	source_name = (
		WEBSITE_QUOTE_SOURCE
		if lead_type == "quote"
		else WEBSITE_DEMO_SOURCE
		if lead_type == "demo"
		else WEBSITE_SOURCE
	)
	source = _ensure_lead_source(source_name)
	preferred_contact = _text(context.get("preferredContactMethod")).lower()
	whatsapp_no = phone if preferred_contact == "whatsapp" else None

	lead = _get_or_create_lead(name, email, phone, company, source, whatsapp_no)
	subject = f"{source_name}: {name}"
	lead_notes = demo_notes if lead_type == "demo" else notes
	_add_communication("Lead", lead.name, subject, lead_notes, email)

	opportunity_name = None
	if lead_type == "quote":
		opportunity = _create_opportunity(lead, context, notes, source)
		opportunity_name = opportunity.name
		_add_communication("Opportunity", opportunity.name, subject, notes, email)
		_send_quote_emails(lead, opportunity_name, notes, preferred_contact)
	elif lead_type == "demo":
		_send_demo_emails(lead, demo_message, context)

	return {
		"ok": True,
		"lead": lead.name,
		"opportunity": opportunity_name,
	}
