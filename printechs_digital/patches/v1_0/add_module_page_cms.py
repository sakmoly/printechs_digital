# Copyright (c) 2026, Printechs and contributors

import frappe

from printechs_digital.setup.fill_erpnext_finance import fill_erpnext_finance


def execute():
	for doctype, filename in (
		("Website Product Key Feature", "website_product_key_feature"),
		("Website Product Process Step", "website_product_process_step"),
		("Website Product Connection Item", "website_product_connection_item"),
		("Website Product Report Item", "website_product_report_item"),
		("Website Product Audience Item", "website_product_audience_item"),
		("Website Product Page Section Order", "website_product_page_section_order"),
		("Website Product", "website_product"),
	):
		if filename == "website_product" or frappe.db.exists("DocType", doctype) or filename.startswith("website_product"):
			frappe.reload_doc("Printechs Digital", "doctype", filename)

	for doctype in (
		"Website Product Key Feature",
		"Website Product Process Step",
		"Website Product Connection Item",
		"Website Product Report Item",
		"Website Product Audience Item",
		"Website Product",
	):
		if frappe.db.exists("DocType", doctype):
			frappe.db.updatedb(doctype)

	fill_erpnext_finance()
	frappe.db.commit()
