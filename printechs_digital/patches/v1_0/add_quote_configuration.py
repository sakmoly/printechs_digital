# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	if not frappe.db.exists("DocType", "Website Product"):
		return

	meta = frappe.get_doc("DocType", "Website Product")
	existing = {field.fieldname for field in meta.fields}

	if "configure_on_quote" not in existing:
		meta.append(
			"fields",
			{
				"fieldname": "configure_on_quote",
				"fieldtype": "Check",
				"label": "Configure on Quote",
				"default": "0",
				"description": "If checked, the Request Quote form asks the visitor to choose configuration options.",
				"insert_after": "show_demo_cta",
			},
		)

	if "quote_options" not in existing:
		meta.append(
			"fields",
			{
				"fieldname": "quote_options",
				"fieldtype": "Table",
				"label": "Quote Options",
				"options": "Website Product Quote Option",
				"depends_on": "eval:doc.configure_on_quote",
				"description": "Shown on the quote form only when Configure on Quote is enabled.",
			},
		)

	if "configure_on_quote" not in existing or "quote_options" not in existing:
		meta.save()
		frappe.db.commit()
