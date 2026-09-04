# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	if not frappe.db.exists("DocType", "Website Product"):
		return

	meta = frappe.get_doc("DocType", "Website Product")
	existing = {field.fieldname for field in meta.fields}
	changed = False

	if "configure_on_demo" not in existing:
		meta.append(
			"fields",
			{
				"fieldname": "configure_on_demo",
				"fieldtype": "Check",
				"label": "Configure on Demo",
				"default": "0",
				"description": "If checked, the Request Demo form asks the visitor to answer scoping questions.",
				"insert_after": "quote_options",
			},
		)
		changed = True

	if "demo_options" not in existing:
		meta.append(
			"fields",
			{
				"fieldname": "demo_options",
				"fieldtype": "Table",
				"label": "Demo Options",
				"options": "Website Product Quote Option",
				"depends_on": "eval:doc.configure_on_demo",
				"description": "Shown on the demo form only when Configure on Demo is enabled.",
				"insert_after": "configure_on_demo",
			},
		)
		changed = True

	if changed:
		meta.save()
		frappe.db.commit()
