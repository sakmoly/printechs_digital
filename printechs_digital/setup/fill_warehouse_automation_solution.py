# Copyright (c) 2026, Printechs and contributors
"""Authoritative hardware list for the Warehouse Automation solution page.

Mobility, fixed scanning, label printing and Zebra RFID inventory.
Does not change featured flags. WMS stays a copy mention, not a product card.
"""

import frappe

PRODUCT_SLUGS = [
	"datalogic-memor-12",
	"datalogic-memor-17",
	"datalogic-skorpio-x40-x45",
	"datalogic-falcon-x60-x65",
	"datalogic-codiscan",
	"zebra-tc53e-tc58e",
	"zebra-tc73-tc78",
	"zebra-ws501",
	"datalogic-matrix-320",
	"datalogic-powerscan-9600",
	"zebra-ds3600-series",
	"zebra-zt421",
	"zebra-zt411",
	"zebra-zt610-zt620",
	"zebra-zd621",
	"zebra-zq630-plus",
	"zebra-zq521",
	"zebra-rfd90",
	"zebra-fxr90",
	"zebra-zd621r",
	"zebra-zq630-rfid-plus",
	"zebra-ws50-rfid",
	"zebra-rfd40",
]


def fill_warehouse_automation_solution() -> dict:
	name = frappe.db.get_value("Website Solution", {"slug": "warehouse-automation"}, "name")
	if not name:
		frappe.throw("Website Solution warehouse-automation is missing")

	existing = {
		row.slug
		for row in frappe.get_all(
			"Website Product",
			filters={"slug": ["in", PRODUCT_SLUGS], "published": 1},
			fields=["slug"],
		)
	}
	slugs = [slug for slug in PRODUCT_SLUGS if slug in existing]

	doc = frappe.get_doc("Website Solution", name)
	doc.published = 1
	doc.show_on_list = 1
	doc.solution_name = "Warehouse Automation"
	doc.card_title = "Warehouse Automation"
	doc.card_summary = (
		"Mobile computers, fixed scanners, label printers and RFID inventory "
		"for distribution centres in Saudi Arabia."
	)
	doc.summary = (
		"Aisle mobility, dock-door scans, ship-station labels and RFID inventory "
		"counts — specified and supported by Printechs."
	)
	doc.href = "/solutions/warehouse-automation"
	doc.image = "/files/featured-warehouse-automation.jpg"
	doc.image_alt = "High-bay warehouse aisle with a roller conveyor between pallet racks"
	doc.related_product_slugs = "\n".join(slugs)
	# Keep existing WMS link on the Desk record; do not add software product cards.
	if not (doc.related_software_slugs or "").strip():
		doc.related_software_slugs = "warehouse-management-system"
	doc.meta_title = "Warehouse Automation Solutions | Printechs"
	doc.meta_description = (
		"Warehouse mobility, industrial scanning, label printing and Zebra RFID "
		"inventory systems for DCs in Saudi Arabia."
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": "warehouse-automation", "products": slugs}
