# Copyright (c) 2026, Printechs and contributors
"""Seed Website Industry records from the current Home industry grid."""

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image

INDUSTRIES = [
	{
		"industry_name": "Dairy",
		"slug": "dairy",
		"sort_order": 1,
		"image": "industries/industry-dairy.jpg",
		"image_alt": "Dairy production line with coded milk bottles on a conveyor",
		"summary": "Coding, traceability and packaging identification for dairy producers.",
		"related_product_slugs": "hitachi-ux-d161",
		"related_software_slugs": "erpnext\nwarehouse-management-system",
		"related_solution_slugs": "coding-marking\ntraceability",
		"meta_title": "Dairy Industry Solutions | Printechs",
		"meta_description": "Technology solutions for dairy producers from Printechs.",
	},
	{
		"industry_name": "Food & Beverage",
		"slug": "food-beverage",
		"sort_order": 2,
		"image": "industries/industry-food-beverage.jpg",
		"image_alt": "Food and beverage production line with coded meal containers and bottles",
		"summary": "Line coding, labelling and retail systems for F&B operations.",
		"related_solution_slugs": "coding-marking\nretail-automation",
		"meta_title": "Food & Beverage Solutions | Printechs",
		"meta_description": "Food and beverage technology solutions from Printechs.",
	},
	{
		"industry_name": "Bakery",
		"slug": "bakery",
		"sort_order": 3,
		"image": "industries/industry-bakery.jpg",
		"image_alt": "Bakery production line with coded bread packaging on a conveyor",
		"summary": "Weighing, coding and store technology for bakery brands.",
		"meta_title": "Bakery Solutions | Printechs",
		"meta_description": "Bakery industry solutions from Printechs.",
	},
	{
		"industry_name": "Egg / Poultry",
		"slug": "egg-poultry",
		"sort_order": 4,
		"image": "industries/industry-egg-poultry.jpg",
		"image_alt": "Egg packaging line with traceability coding on cartons and shells",
		"summary": "Marking and traceability systems for egg and poultry producers.",
		"meta_title": "Egg & Poultry Solutions | Printechs",
		"meta_description": "Egg and poultry technology solutions from Printechs.",
	},
	{
		"industry_name": "Pharmaceutical",
		"slug": "pharmaceutical",
		"sort_order": 5,
		"image": "industries/industry-pharmaceutical.jpg",
		"image_alt": "Pharmaceutical packaging line with batch-coded product boxes",
		"summary": "Compliant coding and identification for pharmaceutical packaging.",
		"related_solution_slugs": "coding-marking\ntraceability",
		"meta_title": "Pharmaceutical Solutions | Printechs",
		"meta_description": "Pharmaceutical coding and traceability with Printechs.",
	},
	{
		"industry_name": "Pipe",
		"slug": "pipe",
		"sort_order": 6,
		"image": "industries/industry-pipe.jpg",
		"image_alt": "Industrial pipe with batch number and size marking",
		"summary": "Large character and industrial coding for pipe manufacturers.",
		"meta_title": "Pipe Industry Solutions | Printechs",
		"meta_description": "Pipe industry coding solutions from Printechs.",
	},
	{
		"industry_name": "Plastic",
		"slug": "plastic",
		"sort_order": 7,
		"image": "industries/industry-plastic.jpg",
		"image_alt": "Plastic bottles on a production line with lot and expiry coding",
		"summary": "Durable coding systems for plastic manufacturing environments.",
		"meta_title": "Plastic Industry Solutions | Printechs",
		"meta_description": "Plastic industry technology from Printechs.",
	},
	{
		"industry_name": "Steel",
		"slug": "steel",
		"sort_order": 8,
		"image": "industries/industry-steel.jpg",
		"image_alt": "Steel coil with batch number, production date and QR code marking",
		"summary": "Rugged identification and marking for steel and metals.",
		"meta_title": "Steel Industry Solutions | Printechs",
		"meta_description": "Steel industry marking solutions from Printechs.",
	},
	{
		"industry_name": "Packaging",
		"slug": "packaging",
		"sort_order": 9,
		"image": "industries/industry-packaging.jpg",
		"image_alt": "Automated packaging line with cartons and pouches on a conveyor",
		"summary": "Coding, inspection readiness and packaging line technology.",
		"meta_title": "Packaging Solutions | Printechs",
		"meta_description": "Packaging industry solutions from Printechs.",
	},
	{
		"industry_name": "Retail",
		"slug": "retail",
		"sort_order": 10,
		"image": "industries/industry-retail.jpg",
		"image_alt": "Retail checkout scanning product with lot and expiry traceability data",
		"summary": "Store hardware, POS software and retail automation platforms.",
		"related_software_slugs": "modern-pos\nprintechs-loyalty-management-system",
		"related_solution_slugs": "retail-automation\npos-retail-software",
		"meta_title": "Retail Solutions | Printechs",
		"meta_description": "Retail technology and software from Printechs.",
	},
	{
		"industry_name": "Fashion",
		"slug": "fashion",
		"sort_order": 11,
		"image": "industries/industry-fashion.jpg",
		"image_alt": "Fashion retail checkout with modern POS terminal and store display",
		"summary": "Labelling, mobility and store systems for fashion retail.",
		"meta_title": "Fashion Retail Solutions | Printechs",
		"meta_description": "Fashion retail technology from Printechs.",
	},
	{
		"industry_name": "Warehouse & Logistics",
		"slug": "warehouse-logistics",
		"sort_order": 12,
		"image": "industries/industry-warehouse-logistics.jpg",
		"image_alt": "Warehouse logistics with conveyor, forklift and pallet racking",
		"summary": "Barcode mobility, WMS and automation for distribution centres.",
		"related_software_slugs": "warehouse-management-system",
		"related_solution_slugs": "warehouse-automation\nbarcode-mobility",
		"meta_title": "Warehouse & Logistics Solutions | Printechs",
		"meta_description": "Warehouse and logistics technology from Printechs.",
	},
]


def fill_website_industries():
	if not frappe.db.exists("DocType", "Website Industry"):
		frappe.throw("Website Industry doctype is missing")

	created = 0
	for row in INDUSTRIES:
		if frappe.db.exists("Website Industry", {"slug": row["slug"]}):
			continue
		doc = frappe.new_doc("Website Industry")
		doc.industry_name = row["industry_name"]
		doc.slug = row["slug"]
		doc.published = 1
		doc.show_on_home = 1
		doc.sort_order = row["sort_order"]
		doc.image = copy_public_image(row["image"])
		doc.image_alt = row["image_alt"]
		doc.summary = row["summary"]
		doc.related_product_slugs = row.get("related_product_slugs")
		doc.related_software_slugs = row.get("related_software_slugs")
		doc.related_solution_slugs = row.get("related_solution_slugs")
		doc.meta_title = row["meta_title"]
		doc.meta_description = row["meta_description"]
		doc.flags.ignore_permissions = True
		doc.insert()
		created += 1

	frappe.db.commit()
	return created
