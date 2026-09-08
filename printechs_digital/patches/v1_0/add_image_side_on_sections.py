# Copyright (c) 2026, Printechs and contributors

import frappe


def execute():
	for doctype, module_name in (
		("Website Product Content Section", "website_product_content_section"),
		("Website Product Tour Section", "website_product_tour_section"),
	):
		if not frappe.db.exists("DocType", doctype):
			continue
		frappe.reload_doc("Printechs Digital", "doctype", module_name)
		frappe.db.updatedb(doctype)
	frappe.db.commit()
