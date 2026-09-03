# Copyright (c) 2026, Printechs and contributors
"""Seed Website Solution records from the current Home and solutions list."""

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image

PLACEHOLDER = "placeholders/solution.svg"

SOLUTIONS = [
	{
		"solution_name": "Coding & Marking",
		"slug": "coding-marking",
		"sort_order": 1,
		"featured": 1,
		"show_on_list": 1,
		"card_title": "Production Coding & Marking",
		"card_summary": "Reliable coding and marking for products, packaging and production lines.",
		"href": "/solutions/coding-marking",
		"image": "solutions/featured-production-coding-marking.jpg",
		"image_alt": "Industrial coding and marking system operating on a production line",
		"summary": "Industrial coding systems that keep production lines compliant and readable.",
		"related_product_slugs": "hitachi-ux-d161\nhitachi-ux-d160\nrea-jet-coding-systems",
		"meta_title": "Coding & Marking Solutions | Printechs",
		"meta_description": "Industrial coding and marking solutions from Printechs.",
	},
	{
		"solution_name": "Traceability",
		"slug": "traceability",
		"sort_order": 2,
		"featured": 1,
		"show_on_list": 1,
		"card_title": "Product Traceability",
		"card_summary": "Connect products, batches and production data for greater visibility and control.",
		"href": "/solutions/traceability",
		"image": "solutions/featured-product-traceability.png",
		"image_alt": "Product barcode and traceability identification technology",
		"summary": "End-to-end identification strategies for product and batch visibility.",
		"meta_title": "Traceability Solutions | Printechs",
		"meta_description": "Traceability solutions from Printechs.",
	},
	{
		"solution_name": "Retail Automation",
		"slug": "retail-automation",
		"sort_order": 3,
		"featured": 1,
		"show_on_list": 1,
		"card_title": "Connected Retail Operations",
		"card_summary": "Integrate POS, weighing, mobility and store technology into a smarter retail environment.",
		"href": "/solutions/retail-automation",
		"image": "solutions/featured-connected-retail.png",
		"image_alt": "Connected retail POS and store automation technology",
		"summary": "Connected store technology that improves speed, accuracy and experience.",
		"meta_title": "Retail Automation | Printechs",
		"meta_description": "Retail automation solutions from Printechs.",
	},
	{
		"solution_name": "Enterprise & Warehouse Systems",
		"slug": "enterprise-warehouse",
		"sort_order": 4,
		"featured": 1,
		"show_on_list": 0,
		"card_title": "Enterprise & Warehouse Systems",
		"card_summary": "Connect ERP, warehouse, POS and compliance systems for better operational control.",
		"href": "/software",
		"image": "solutions/featured-enterprise-warehouse.png",
		"image_alt": "Enterprise ERP and warehouse management software systems",
		"summary": "Connect ERP, warehouse, POS and compliance systems for better operational control.",
		"related_software_slugs": "erpnext\nwarehouse-management-system",
		"meta_title": "Enterprise & Warehouse Systems | Printechs",
		"meta_description": "Enterprise ERP and warehouse systems from Printechs.",
	},
	{
		"solution_name": "Barcode & Mobility",
		"slug": "barcode-mobility",
		"sort_order": 5,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/barcode-mobility",
		"image": PLACEHOLDER,
		"image_alt": "Barcode and mobility solution",
		"summary": "Scanning, printing and mobile computing for accurate operations.",
		"related_product_slugs": "autoid-solutions\ndatalogic-barcode-solutions\nzebra-mobility",
		"meta_title": "Barcode & Mobility | Printechs",
		"meta_description": "Barcode and mobility solutions from Printechs.",
	},
	{
		"solution_name": "Warehouse Automation",
		"slug": "warehouse-automation",
		"sort_order": 6,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/warehouse-automation",
		"image": PLACEHOLDER,
		"image_alt": "Warehouse automation solution",
		"summary": "Hardware and software designed for efficient warehouse execution.",
		"related_software_slugs": "warehouse-management-system",
		"meta_title": "Warehouse Automation | Printechs",
		"meta_description": "Warehouse automation solutions from Printechs.",
	},
	{
		"solution_name": "POS & Retail Software",
		"slug": "pos-retail-software",
		"sort_order": 7,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/pos-retail-software",
		"image": PLACEHOLDER,
		"image_alt": "POS and retail software solution",
		"summary": "Software platforms that power modern retail selling and operations.",
		"related_software_slugs": "modern-pos\nprintechs-loyalty-management-system",
		"meta_title": "POS & Retail Software | Printechs",
		"meta_description": "POS and retail software solutions from Printechs.",
	},
	{
		"solution_name": "ERP & Business Automation",
		"slug": "erp-business-automation",
		"sort_order": 8,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/erp-business-automation",
		"image": PLACEHOLDER,
		"image_alt": "ERP and business automation solution",
		"summary": "Business systems that unify finance, inventory and service delivery.",
		"related_software_slugs": "erpnext\nzatca-integration",
		"meta_title": "ERP & Business Automation | Printechs",
		"meta_description": "ERP and business automation from Printechs.",
	},
	{
		"solution_name": "RFID",
		"slug": "rfid",
		"sort_order": 9,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/rfid",
		"image": PLACEHOLDER,
		"image_alt": "RFID solution",
		"summary": "RFID identification for inventory visibility and process control.",
		"meta_title": "RFID Solutions | Printechs",
		"meta_description": "RFID solutions from Printechs.",
	},
	{
		"solution_name": "Electronic Shelf Labels",
		"slug": "electronic-shelf-labels",
		"sort_order": 10,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/electronic-shelf-labels",
		"image": PLACEHOLDER,
		"image_alt": "Electronic shelf labels solution",
		"summary": "Dynamic pricing displays for accurate and efficient store operations.",
		"meta_title": "Electronic Shelf Labels | Printechs",
		"meta_description": "Electronic shelf label solutions from Printechs.",
	},
	{
		"solution_name": "System Integration",
		"slug": "system-integration",
		"sort_order": 11,
		"featured": 0,
		"show_on_list": 1,
		"href": "/solutions/system-integration",
		"image": PLACEHOLDER,
		"image_alt": "System integration solution",
		"summary": "Connecting hardware, software and operational processes into one stack.",
		"related_software_slugs": "api-integration",
		"meta_title": "System Integration | Printechs",
		"meta_description": "System integration services from Printechs.",
	},
]


def fill_website_solutions():
	if not frappe.db.exists("DocType", "Website Solution"):
		frappe.throw("Website Solution doctype is missing")

	created = 0
	for row in SOLUTIONS:
		if frappe.db.exists("Website Solution", {"slug": row["slug"]}):
			continue
		doc = frappe.new_doc("Website Solution")
		doc.solution_name = row["solution_name"]
		doc.slug = row["slug"]
		doc.published = 1
		doc.show_on_list = row["show_on_list"]
		doc.featured = row["featured"]
		doc.sort_order = row["sort_order"]
		doc.card_title = row.get("card_title")
		doc.card_summary = row.get("card_summary")
		doc.href = row["href"]
		doc.image = copy_public_image(row["image"])
		doc.image_alt = row["image_alt"]
		doc.summary = row["summary"]
		doc.related_product_slugs = row.get("related_product_slugs")
		doc.related_software_slugs = row.get("related_software_slugs")
		doc.meta_title = row["meta_title"]
		doc.meta_description = row["meta_description"]
		doc.flags.ignore_permissions = True
		doc.insert()
		created += 1

	frappe.db.commit()
	return created
