# Copyright (c) 2026, Printechs and contributors
"""Default copy for the Talk to a Specialist sidebar."""

SPECIALIST_DEFAULTS = {
	"specialist_eyebrow": "Printechs",
	"specialist_title": "Talk to a specialist",
	"specialist_description": (
		"Industrial coding, retail technology, and enterprise software across Saudi Arabia."
	),
	"specialist_email": "info@printechs.com",
	"specialist_phone": "+966 11 206 2828 | +966 11 206 2929",
	"specialist_location": "Riyadh, Jeddah & Dammam, Kingdom of Saudi Arabia",
	"specialist_office_hours": "Sunday – Thursday, 9:00 AM – 6:00 PM (AST)",
	"specialist_whatsapp_number": "+966550733441",
	"specialist_whatsapp_label": "Chat on WhatsApp",
	"specialist_pricing_title": "Looking for pricing?",
	"specialist_pricing_link_label": "Products",
	"specialist_pricing_link_href": "/products",
	"specialist_pricing_description": (
		"to open a product and request a quote with the correct item context."
	),
}


def fill_contact_specialist_fields():
	import frappe

	if not frappe.db.exists("DocType", "Website Contact Settings"):
		return

	doc = frappe.get_single("Website Contact Settings")
	changed = False

	for field, value in SPECIALIST_DEFAULTS.items():
		if not doc.get(field):
			doc.set(field, value)
			changed = True

	if not changed:
		return doc.name

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
