# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	if not frappe.db.exists("DocType", "Website Product"):
		return

	meta = frappe.get_doc("DocType", "Website Product")
	existing = {field.fieldname for field in meta.fields}

	new_fields = [
		{
			"fieldname": "product_tour_section",
			"fieldtype": "Section Break",
			"label": "Product Tour",
			"insert_after": "visual_story_heading",
		},
		{
			"fieldname": "enable_product_tour",
			"fieldtype": "Check",
			"label": "Enable Product Tour",
			"default": "0",
			"description": "Show the interactive screenshot tour on the website product page.",
			"insert_after": "product_tour_section",
		},
		{
			"fieldname": "product_tour_heading",
			"fieldtype": "Data",
			"label": "Product Tour Heading",
			"depends_on": "eval:doc.enable_product_tour",
			"insert_after": "enable_product_tour",
		},
		{
			"fieldname": "product_tour_subheading",
			"fieldtype": "Small Text",
			"label": "Product Tour Subheading",
			"depends_on": "eval:doc.enable_product_tour",
			"insert_after": "product_tour_heading",
		},
		{
			"fieldname": "tour_sections",
			"fieldtype": "Table",
			"label": "Tour Sections",
			"options": "Website Product Tour Section",
			"depends_on": "eval:doc.enable_product_tour",
			"insert_after": "product_tour_subheading",
		},
	]

	for field in new_fields:
		if field["fieldname"] not in existing:
			meta.append("fields", field)

	if new_fields:
		meta.save()
		frappe.db.commit()
