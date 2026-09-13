# Copyright (c) 2026, Printechs and contributors
"""Authoritative hardware list for the Retail Automation solution page.

ESL, POS, weighing, scanning and RF EAS. Does not set software slugs
or change featured flags on individual products.
"""

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image

PRODUCT_SLUGS = [
	"vusion-esl",
	"vusion-v300",
	"vusion-v300-waterproof",
	"vusion-v300-freezer",
	"vusion-edgesense",
	"vusion-vusioncloud",
	"vusion-retail-media",
	"fec-pos-systems",
	"fec-xp-4765w",
	"fec-xelf-ii",
	"fec-st-1130w",
	"datalogic-smart-portal",
	"fec-tp-100",
	"avery-berkel",
	"avery-berkel-xti400",
	"cas-cl-5500d",
	"cas-cl-5500h",
	"cas-cl-5200p",
	"cas-cn1",
	"datalogic-magellan-9900i",
	"datalogic-magellan-3610vsi",
	"datalogic-gryphon-i-gd4690",
	"datalogic-joya-smart",
	"nedap-rf-eas",
	"nedap-i45",
	"nedap-i37",
	"nedap-i15-go",
	"nedap-checkout-antenna",
	"nedap-rf-eas-labels",
]


def fill_retail_automation_solution() -> dict:
	name = frappe.db.get_value("Website Solution", {"slug": "retail-automation"}, "name")
	if not name:
		frappe.throw("Website Solution retail-automation is missing")

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
	doc.featured = 1
	doc.show_on_list = 1
	doc.solution_name = "Retail Automation"
	doc.card_title = "Connected Retail Operations"
	doc.card_summary = (
		"Electronic shelf labels, POS, weighing, scanning and loss prevention "
		"for stores in Saudi Arabia."
	)
	doc.summary = (
		"Store technology that keeps price, scan and stock in step — from the "
		"shelf to the till."
	)
	doc.href = "/solutions/retail-automation"
	doc.image = copy_public_image("solutions/featured-connected-retail.png")
	if not doc.image or doc.image.startswith("/images/"):
		doc.image = "/files/featured-connected-retail.png"
	doc.image_alt = "Connected retail POS and store automation technology"
	doc.related_product_slugs = "\n".join(slugs)
	doc.related_software_slugs = ""
	doc.meta_title = "Retail Automation Solutions | Printechs"
	doc.meta_description = (
		"ESL, POS, weighing, barcode scanning and RF EAS for retailers in "
		"Saudi Arabia. Specified and supported by Printechs."
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": "retail-automation", "products": slugs}
