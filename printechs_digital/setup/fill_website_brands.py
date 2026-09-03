# Copyright (c) 2026, Printechs and contributors
"""Create Website Brand records for the current marketing brand list."""

from pathlib import Path
from shutil import copy2

import frappe

BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")

BRANDS = [
	{
		"erp_brand": "Hitachi",
		"display_name": "Hitachi",
		"slug": "hitachi",
		"logo": "brand-hitachi.png",
		"summary": "Industrial continuous inkjet coding technology for high-speed production lines.",
		"sort_order": 1,
	},
	{
		"erp_brand": "Reajet",
		"display_name": "REA JET",
		"slug": "rea-jet",
		"logo": "brand-rea-jet.png",
		"summary": "Industrial coding and marking systems for packaging and manufacturing.",
		"sort_order": 2,
	},
	{
		"erp_brand": "DATALOGIC",
		"display_name": "Datalogic",
		"slug": "datalogic",
		"logo": "brand-datalogic.png",
		"summary": "Barcode scanning and data capture for retail, warehouse and industry.",
		"sort_order": 3,
	},
	{
		"erp_brand": "Zebra",
		"display_name": "Zebra",
		"slug": "zebra",
		"logo": "brand-zebra.png",
		"summary": "Enterprise mobility, printing and identification technology.",
		"sort_order": 4,
	},
	{
		"erp_brand": "AVERY BERKEL",
		"display_name": "Avery Berkel",
		"slug": "avery-berkel",
		"logo": "brand-avery-berkel.png",
		"summary": "Retail and food weighing systems built for accuracy and uptime.",
		"sort_order": 5,
	},
	{
		"erp_brand": "CAS",
		"display_name": "CAS",
		"slug": "cas",
		"logo": "brand-cas.png",
		"summary": "Weighing and retail scale technology for store and food operations.",
		"sort_order": 6,
	},
]


def copy_logo(filename: str) -> str:
	source = BRAND_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def fill_website_brands():
	created = []
	for row in BRANDS:
		if not frappe.db.exists("Brand", row["erp_brand"]):
			frappe.throw(f"ERP Brand {row['erp_brand']} was not found")

		name = frappe.db.get_value("Website Brand", {"slug": row["slug"]}, "name")
		doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
		doc.brand = row["erp_brand"]
		doc.display_name = row["display_name"]
		doc.slug = row["slug"]
		doc.logo = copy_logo(row["logo"])
		doc.summary = row["summary"]
		doc.sort_order = row["sort_order"]
		doc.published = 1
		doc.meta_title = f"{row['slug'].replace('-', ' ').title()} | Printechs Brands"
		doc.meta_description = row["summary"]
		doc.flags.ignore_permissions = True
		if name:
			doc.save()
		else:
			doc.insert()
		created.append(doc.name)

	frappe.db.commit()
	return created
