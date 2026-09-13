# Copyright (c) 2026, Printechs and contributors
"""Authoritative product list for the Coding & Marking solution page.

Hitachi CIJ, REA JET / REA LASER, UKCM laser, ANSER and UKCM TIJ.
Does not change featured flags on individual products.
"""

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image

PRODUCT_SLUGS = [
	"hitachi-ux-d161",
	"hitachi-ux-d160",
	"hitachi-ux2-d160",
	"hitachi-ux2-d150",
	"hitachi-ux-d151",
	"rea-jet-coding-systems",
	"rea-jet-dod-2",
	"rea-jet-hr-2",
	"rea-jet-gk-2",
	"rea-jet-up",
	"rea-jet-spray-mark",
	"rea-jet-code-verification",
	"rea-jet-cl",
	"rea-jet-fl",
	"ukcm-laser",
	"ukcm-fiber-laser",
	"ukcm-co2-laser",
	"ukcm-uv-laser",
	"anser-a1",
	"anser-sph-smart-printhead",
	"ukcm-kt7",
	"ukcm-kt10",
	"ukcm-hand-coder",
]


def fill_coding_marking_solution() -> dict:
	name = frappe.db.get_value("Website Solution", {"slug": "coding-marking"}, "name")
	if not name:
		frappe.throw("Website Solution coding-marking is missing")

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
	doc.solution_name = "Coding & Marking"
	doc.card_title = "Production Coding & Marking"
	doc.card_summary = (
		"Hitachi CIJ, REA JET inkjet, REA LASER, UKCM laser and thermal inkjet "
		"for production lines in Saudi Arabia."
	)
	doc.summary = (
		"Industrial coding and marking — continuous inkjet, large-character, "
		"laser and TIJ — specified and supported by Printechs."
	)
	doc.href = "/solutions/coding-marking"
	doc.image = copy_public_image("solutions/featured-production-coding-marking.jpg")
	doc.image_alt = "Industrial coding and marking system operating on a production line"
	doc.related_product_slugs = "\n".join(slugs)
	doc.related_software_slugs = ""
	doc.meta_title = "Coding & Marking Solutions | Printechs"
	doc.meta_description = (
		"Hitachi CIJ, REA JET, REA LASER and UKCM laser marking systems for "
		"production lines in Saudi Arabia. Specified and supported by Printechs."
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": "coding-marking", "products": slugs}
