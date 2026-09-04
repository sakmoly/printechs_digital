# Copyright (c) 2026, Printechs and contributors

import frappe

from printechs_digital.constants.product_page_sections import (
	DEFAULT_PAGE_SECTION_ORDER,
	default_page_section_order_rows,
)


def execute():
	if not frappe.db.exists("DocType", "Website Product"):
		return

	meta = frappe.get_doc("DocType", "Website Product")
	existing = {field.fieldname for field in meta.fields}

	new_fields = [
		{
			"fieldname": "page_layout_section",
			"fieldtype": "Section Break",
			"label": "Page Layout",
			"insert_after": "collapsible_full_specs",
		},
		{
			"fieldname": "page_section_order",
			"fieldtype": "Table",
			"label": "Page Section Order",
			"options": "Website Product Page Section Order",
			"description": (
				"Controls the order of sections on the website product page. "
				"Hero and final CTA stay fixed. Empty sections are skipped automatically."
			),
			"insert_after": "page_layout_section",
		},
	]

	for field in new_fields:
		if field["fieldname"] not in existing:
			meta.append("fields", field)

	if new_fields:
		meta.save()
		frappe.db.commit()

	seed_page_section_order()


def seed_page_section_order():
	default_rows = default_page_section_order_rows()
	products = frappe.get_all("Website Product", pluck="name")
	for name in products:
		doc = frappe.get_doc("Website Product", name)
		if doc.get("page_section_order"):
			continue
		doc.set("page_section_order", default_rows)
		doc.flags.ignore_permissions = True
		doc.save()

	frappe.db.commit()
