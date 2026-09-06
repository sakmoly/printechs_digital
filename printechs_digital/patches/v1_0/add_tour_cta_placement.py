# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	if not frappe.db.exists("DocType", "Website Product Tour Section"):
		return

	frappe.reload_doc("Printechs Digital", "doctype", "website_product_tour_section")
	frappe.db.updatedb("Website Product Tour Section")
	frappe.db.commit()
