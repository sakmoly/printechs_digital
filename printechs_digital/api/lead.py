# Copyright (c) 2026, Printechs and contributors

import json

import frappe
from frappe.utils import cstr, get_defaults, strip_html


WEBSITE_QUOTE_SOURCE = "Website Quote"
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


def _get_or_create_lead(name: str, email: str, phone: str, company: str, source: str | None):
	existing = frappe.db.get_value("Lead", {"email_id": email}, "name")
	if existing:
		lead = frappe.get_doc("Lead", existing)
		changed = False
		if phone and not lead.mobile_no:
			lead.mobile_no = phone
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

	source_name = WEBSITE_QUOTE_SOURCE if lead_type == "quote" else WEBSITE_SOURCE
	source = _ensure_lead_source(source_name)

	lead = _get_or_create_lead(name, email, phone, company, source)
	subject = f"{source_name}: {name}"
	_add_communication("Lead", lead.name, subject, notes, email)

	opportunity_name = None
	if lead_type == "quote":
		opportunity = _create_opportunity(lead, context, notes, source)
		opportunity_name = opportunity.name
		_add_communication("Opportunity", opportunity.name, subject, notes, email)

	return {
		"ok": True,
		"lead": lead.name,
		"opportunity": opportunity_name,
	}
