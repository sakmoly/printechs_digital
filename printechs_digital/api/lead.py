# Copyright (c) 2026, Printechs and contributors

import json

import frappe
from frappe.utils import cstr, get_defaults, strip_html

from printechs_digital.api.email_templates import (
	contact_customer_confirmation_html,
	contact_sales_notification_html,
	demo_customer_confirmation_html,
	demo_sales_notification_html,
)


WEBSITE_QUOTE_SOURCE = "Website Quote"
WEBSITE_DEMO_SOURCE = "Website Demo"
WEBSITE_SOURCE = "Website"

PRODUCT_ENQUIRY_EMAIL = "sakeer@printechs.com"
PRODUCT_ENQUIRY_EMAIL_ONLY_CC = ("marketing@printechs.com",)
GENERAL_ENQUIRY_EMAILS = ("info@printechs.com", "marketing@printechs.com")
CONTACT_NOTIFICATION_EMAILS = ("sakeer@printechs.com", "marketing@printechs.com")

INQUIRY_TYPE_LABELS = {
	"general": "General enquiry",
	"sales": "Sales & products",
	"support": "Support & service",
	"software": "Software & integration",
	"partnership": "Partnership",
}


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


def _attribution_dict(context: dict) -> dict:
	return _as_dict(context.get("attribution"))


def _attribution_block(context: dict) -> str:
	attribution = _attribution_dict(context)
	if not attribution:
		return ""

	lines = []
	for key, label in (
		("utm_source", "UTM Source"),
		("utm_medium", "UTM Medium"),
		("utm_campaign", "UTM Campaign"),
		("utm_content", "UTM Content"),
		("utm_term", "UTM Term"),
		("landing_page", "Landing Page"),
		("referrer", "Referrer"),
		("first_visit_at", "First Visit"),
	):
		value = _text(attribution.get(key))
		if value:
			lines.append(f"{label}: {value}")
	return "\n".join(lines)


def _apply_lead_attribution(lead, context: dict) -> bool:
	attribution = _attribution_dict(context)
	if not attribution and not _text(context.get("productSlug")) and not _text(context.get("sourceUrl")):
		return False

	changed = False
	field_map = {
		"web_utm_source": _text(attribution.get("utm_source")),
		"web_utm_medium": _text(attribution.get("utm_medium")),
		"web_utm_campaign": _text(attribution.get("utm_campaign")),
		"web_utm_content": _text(attribution.get("utm_content")),
		"web_utm_term": _text(attribution.get("utm_term")),
		"web_landing_page": _text(attribution.get("landing_page")),
		"web_referrer": _text(attribution.get("referrer")),
		"web_product_slug": _text(context.get("productSlug")),
		"web_source_url": _text(context.get("sourceUrl")),
	}
	first_visit = _text(attribution.get("first_visit_at"))
	if first_visit:
		field_map["web_first_visit_at"] = first_visit

	for fieldname, value in field_map.items():
		if not value:
			continue
		if not lead.meta.get_field(fieldname):
			continue
		if not lead.get(fieldname):
			lead.set(fieldname, value)
			changed = True

	return changed


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
		("inquiryType", "Enquiry type"),
	):
		value = _text(context.get(key))
		if key == "inquiryType" and value:
			value = INQUIRY_TYPE_LABELS.get(value.lower(), value)
		if value:
			lines.append(f"{label}: {value}")

	attribution_text = _attribution_block(context)
	if attribution_text:
		if lines:
			lines.append("")
		lines.append("Acquisition")
		lines.extend(attribution_text.splitlines())

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
	context: dict | None = None,
	whatsapp_no: str | None = None,
):
	context = context or {}
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
		if _apply_lead_attribution(lead, context):
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
	_apply_lead_attribution(lead, context)
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


def _resolve_generate_lead(context: dict) -> bool:
	if "generateLead" in context:
		return bool(context.get("generateLead"))
	slug = _text(context.get("productSlug"))
	if not slug:
		return False
	return bool(
		frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "generate_lead")
	)


def _contact_details(name: str, email: str, phone: str, company: str, lead_name: str | None = None):
	return frappe._dict(
		{
			"lead_name": name,
			"email_id": email,
			"mobile_no": phone,
			"company_name": company,
			"name": lead_name,
		}
	)


def _create_opportunity(lead, context: dict, notes: str, source: str | None, kind: str = "quote"):
	company = _default_company()
	if not company:
		frappe.throw("Company is not set. Cannot create Opportunity.")

	product = _text(context.get("product")) or lead.lead_name
	label = "Demo" if kind == "demo" else "Quote"
	title = f"Website {label} — {product}"[:140]
	item = _opportunity_item(context, notes)
	sales_stage = None
	if kind == "demo":
		sales_stage = (
			"Qualification"
			if frappe.db.exists("Sales Stage", "Qualification")
			else None
		)
	else:
		sales_stage = (
			"Proposal/Price Quote"
			if frappe.db.exists("Sales Stage", "Proposal/Price Quote")
			else None
		)

	opportunity = frappe.get_doc(
		{
			"doctype": "Opportunity",
			"naming_series": "OPTY-" if "OPTY-" in (frappe.get_meta("Opportunity").get_field("naming_series").options or "") else "CRM-OPP-.YYYY.-",
			"opportunity_from": "Lead",
			"party_name": lead.name,
			"opportunity_type": "Sales" if frappe.db.exists("Opportunity Type", "Sales") else None,
			"status": "Open",
			"sales_stage": sales_stage,
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


def _unique_recipients(*groups) -> list[str]:
	seen: set[str] = set()
	recipients: list[str] = []
	for group in groups:
		for email in group:
			normalized = _text(email).lower()
			if normalized and normalized not in seen:
				seen.add(normalized)
				recipients.append(normalized)
	return recipients


def _product_enquiry_recipients(generate_lead: bool) -> list[str]:
	recipients = [PRODUCT_ENQUIRY_EMAIL]
	if not generate_lead:
		recipients = _unique_recipients(recipients, PRODUCT_ENQUIRY_EMAIL_ONLY_CC)
	return recipients


def _general_enquiry_recipients() -> list[str]:
	return _unique_recipients(GENERAL_ENQUIRY_EMAILS, CONTACT_NOTIFICATION_EMAILS)


def _inquiry_type_label(value: str) -> str:
	key = _text(value).lower()
	return INQUIRY_TYPE_LABELS.get(key, value or "General enquiry")


def _send_quote_emails(
	contact,
	opportunity_name: str | None,
	notes: str,
	preferred_contact: str,
	generate_lead: bool,
):
	lead_line = f"Lead: {contact.name}\n" if contact.name else ""
	opportunity_line = f"Opportunity: {opportunity_name or '-'}\n" if opportunity_name else ""
	try:
		frappe.sendmail(
			recipients=_product_enquiry_recipients(generate_lead),
			subject=f"New website quote — {contact.lead_name}",
			message=(
				f"New quote request from the website.\n\n"
				f"Name: {contact.lead_name}\n"
				f"Company: {contact.company_name or '-'}\n"
				f"Email: {contact.email_id}\n"
				f"Phone: {contact.mobile_no or '-'}\n"
				f"Preferred contact: {preferred_contact or 'email'}\n"
				f"{lead_line}"
				f"{opportunity_line}\n"
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
			recipients=[contact.email_id],
			subject="Quote request received — Printechs",
			message=(
				f"Dear {contact.lead_name},\n\n"
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


def _send_demo_emails(contact, message: str, context: dict, generate_lead: bool):
	product = _text(context.get("product")) or "Software demo"
	sales_html = demo_sales_notification_html(contact, context, message)
	try:
		frappe.sendmail(
			recipients=_product_enquiry_recipients(generate_lead),
			subject=f"New website demo request — {product}",
			message=sales_html,
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website demo sales notification failed")

	try:
		frappe.sendmail(
			recipients=[contact.email_id],
			subject="Demo request received — Printechs",
			message=demo_customer_confirmation_html(contact, product),
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website demo customer confirmation failed")


def _send_contact_emails(contact, message: str, context: dict):
	inquiry_type = _inquiry_type_label(_text(context.get("inquiryType")))
	sales_html = contact_sales_notification_html(contact, context, message, inquiry_type)
	try:
		frappe.sendmail(
			recipients=_general_enquiry_recipients(),
			subject=f"New website enquiry — {contact.lead_name}",
			message=sales_html,
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website contact sales notification failed")

	try:
		frappe.sendmail(
			recipients=[contact.email_id],
			subject="Message received — Printechs",
			message=contact_customer_confirmation_html(contact, inquiry_type),
			now=True,
		)
	except Exception:
		frappe.log_error(title="Website contact customer confirmation failed")


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
	generate_lead = lead_type in ("quote", "demo") and _resolve_generate_lead(context)
	contact = _contact_details(name, email, phone, company)

	lead = None
	lead_name = None
	if generate_lead or lead_type == "contact":
		lead = _get_or_create_lead(name, email, phone, company, source, context, whatsapp_no)
		lead_name = lead.name
		contact.name = lead_name

	subject = f"{source_name}: {name}"
	lead_notes = demo_notes if lead_type == "demo" else notes
	if lead:
		_add_communication("Lead", lead.name, subject, lead_notes, email)

	opportunity_name = None
	if lead_type == "quote":
		if generate_lead and lead:
			opportunity = _create_opportunity(lead, context, notes, source, kind="quote")
			opportunity_name = opportunity.name
			_add_communication("Opportunity", opportunity.name, subject, notes, email)
		_send_quote_emails(contact, opportunity_name, notes, preferred_contact, generate_lead)
	elif lead_type == "demo":
		if generate_lead and lead:
			opportunity = _create_opportunity(lead, context, demo_notes, source, kind="demo")
			opportunity_name = opportunity.name
			_add_communication("Opportunity", opportunity.name, subject, demo_notes, email)
		_send_demo_emails(contact, demo_message, context, generate_lead)
	elif lead_type == "contact":
		_send_contact_emails(contact, message, context)

	return {
		"ok": True,
		"reference": lead_name or opportunity_name or "WEB-LEAD",
		"message": "Thank you. Your request has been received.",
		"lead": lead_name,
		"opportunity": opportunity_name,
		"generateLead": generate_lead,
	}
