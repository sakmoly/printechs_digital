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
		"official_website": "https://www.hitachi-ies.co.jp/english/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "Reajet",
		"display_name": "REA JET",
		"slug": "rea-jet",
		"logo": "brand-rea-jet.png",
		"summary": "Industrial coding and marking systems for packaging and manufacturing.",
		"sort_order": 2,
		"official_website": "https://www.rea-jet.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "DATALOGIC",
		"display_name": "Datalogic",
		"slug": "datalogic",
		"logo": "brand-datalogic.png",
		"summary": "Barcode scanning and data capture for retail, warehouse and industry.",
		"sort_order": 3,
		"official_website": "https://www.datalogic.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "Zebra",
		"display_name": "Zebra",
		"slug": "zebra",
		"logo": "brand-zebra.png",
		"summary": "Enterprise mobility, printing and identification technology.",
		"sort_order": 4,
		"official_website": "https://www.zebra.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "AVERY BERKEL",
		"display_name": "Avery Berkel",
		"slug": "avery-berkel",
		"logo": "brand-avery-berkel.png",
		"summary": "Retail and food weighing systems built for accuracy and uptime.",
		"sort_order": 5,
		"official_website": "https://www.averyberkel.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "CAS",
		"display_name": "CAS",
		"slug": "cas",
		"logo": "brand-cas.png",
		"summary": "Weighing and retail scale technology for store and food operations.",
		"sort_order": 6,
		"official_website": "https://www.globalcas.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "Nedap",
		"display_name": "Nedap",
		"slug": "nedap",
		"logo": "brand-nedap.png",
		"summary": "Connected RF EAS gates, labels and iSenseOS for retail loss prevention.",
		"sort_order": 7,
		"official_website": "https://www.nedap-retail.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "SES-imagotag",
		"display_name": "Vusion",
		"slug": "vusion",
		"logo": "brand-vusion.png",
		"summary": "Electronic shelf labels, smart shelves and connected-store IoT for retail.",
		"sort_order": 8,
		"official_website": "https://www.vusion.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "UKCM",
		"display_name": "UKCM",
		"slug": "ukcm",
		"logo": "brand-ukcm.png",
		"summary": "UKCM laser marking and thermal inkjet for industrial coding and marking.",
		"sort_order": 9,
		"official_website": "https://uk-cm.uk/",
		"show_in_footer": 0,
	},
	{
		"erp_brand": "Hiweigh",
		"display_name": "HiWEIGH",
		"slug": "hiweigh",
		"logo": "brand-hiweigh.png",
		"summary": "Industrial weighing — waterproof benches, floor scales, truck pads and livestock systems.",
		"sort_order": 10,
		"official_website": "https://www.hiweigh.com/",
		"show_in_footer": 1,
	},
	{
		"erp_brand": "FEC",
		"display_name": "FEC",
		"slug": "fec",
		"logo": "brand-fec.png",
		"summary": "FEC POS Solutions from Printechs Saudi Arabia — terminals, panel PCs, kiosks, kitchen displays, box PCs, monitors and peripherals.",
		"sort_order": 13,
		"official_website": "https://www.fecpos.com/",
		"show_in_footer": 0,
	},
]

# Extra published brands not managed in the list above (keep their other fields).
EXTRA_BRANDS = [
	{"slug": "anser", "sort_order": 11, "official_website": "https://www.anser-ufa.com/", "show_in_footer": 0},
	{"slug": "erpnext", "sort_order": 12, "official_website": "https://frappe.io/erpnext", "show_in_footer": 0},
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
		doc.official_website = row.get("official_website")
		doc.show_in_footer = row.get("show_in_footer", 0)
		doc.published = 1
		if not doc.meta_title:
			doc.meta_title = f"{row['display_name']} | Printechs Brands"
		if not doc.meta_description:
			doc.meta_description = row["summary"]
		doc.flags.ignore_permissions = True
		if name:
			doc.save()
		else:
			doc.insert()
		created.append(doc.name)

	for extra in EXTRA_BRANDS:
		name = frappe.db.get_value("Website Brand", {"slug": extra["slug"]}, "name")
		if not name:
			continue
		extra_doc = frappe.get_doc("Website Brand", name)
		extra_doc.sort_order = extra["sort_order"]
		extra_doc.official_website = extra["official_website"]
		extra_doc.show_in_footer = extra.get("show_in_footer", 0)
		extra_doc.flags.ignore_permissions = True
		extra_doc.save()
		created.append(extra_doc.name)

	frappe.db.commit()
	return created
