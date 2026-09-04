# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	if not frappe.db.exists("DocType", "Website Product"):
		return

	meta = frappe.get_doc("DocType", "Website Product")
	existing = {field.fieldname for field in meta.fields}

	if "generate_lead" not in existing:
		meta.append(
			"fields",
			{
				"fieldname": "generate_lead",
				"fieldtype": "Check",
				"label": "Generate Lead",
				"default": "0",
				"description": "If checked, website quote and demo submissions create CRM Lead and Opportunity records. If unchecked, only email notifications are sent.",
				"insert_after": "demo_options",
			},
		)
		meta.save()
		frappe.db.commit()

	# Hardware products linked to an Item should keep CRM lead creation enabled.
	frappe.db.sql(
		"""
		UPDATE `tabWebsite Product`
		SET generate_lead = 1
		WHERE IFNULL(item, '') != '' OR IFNULL(item_code, '') != ''
		"""
	)
	frappe.db.commit()
