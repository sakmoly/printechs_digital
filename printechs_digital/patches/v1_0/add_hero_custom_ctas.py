# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	if not frappe.db.exists("DocType", "Website Product"):
		return

	frappe.reload_doc("Printechs Digital", "doctype", "website_product")
	frappe.db.updatedb("Website Product")
	frappe.db.commit()
