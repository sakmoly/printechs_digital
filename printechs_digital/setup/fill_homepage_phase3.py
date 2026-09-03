# Copyright (c) 2026, Printechs and contributors
"""Add divisions / section headings to Homepage Settings without overwriting hero copy."""

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image


def fill_homepage_phase3():
	if not frappe.db.exists("DocType", "Website Homepage Settings"):
		frappe.throw("Website Homepage Settings doctype is missing")

	doc = frappe.get_single("Website Homepage Settings")

	if not doc.get("divisions_title"):
		doc.divisions_eyebrow = "Capabilities"
		doc.divisions_title = "Three divisions. One technology partner."
		doc.divisions_description = (
			"Industrial systems, retail technology and enterprise software — "
			"each with a clear focus and deep delivery expertise."
		)
	doc.show_divisions = 1

	if not doc.get("divisions"):
		doc.set(
			"divisions",
			[
				{
					"title": "Industrial Solutions",
					"summary": "Coding, marking, traceability and identification systems engineered for production environments.",
					"href": "/solutions/coding-marking",
					"image": copy_public_image("divisions/division-industrial.jpg"),
					"image_alt": "Hitachi industrial coding and marking system on a production line",
					"items": "Coding & Marking\nTraceability\nRFID\nSystem Integration",
					"sort_order": 1,
				},
				{
					"title": "Retail Solutions",
					"summary": "Store automation, barcode mobility and weighing technology for modern retail operations.",
					"href": "/solutions/retail-automation",
					"image": copy_public_image("divisions/division-retail.jpg"),
					"image_alt": "Retail POS, barcode scanner and weighing system in a grocery store",
					"items": "Barcode & Mobility\nElectronic Shelf Labels\nWeighing\nRetail Hardware",
					"sort_order": 2,
				},
				{
					"title": "Software Solutions",
					"summary": "Enterprise platforms that connect operations, compliance and growth across the business.",
					"href": "/software",
					"image": copy_public_image("divisions/division-software.jpg"),
					"image_alt": "Enterprise software dashboards across desktop, POS, mobile and tablet",
					"items": "Modern POS\nERPNext\nWarehouse Management\nZATCA Integration\nLoyalty",
					"sort_order": 3,
				},
			],
		)

	if not doc.get("featured_solutions_title"):
		doc.featured_solutions_eyebrow = "Featured solutions"
		doc.featured_solutions_title = "Technology built for real operations"
		doc.featured_solutions_description = (
			"From production floors to retail stores and enterprise systems, our solutions "
			"help businesses improve accuracy, visibility and operational control."
		)
		doc.featured_solutions_limit = 4
	doc.show_featured_solutions = 1

	if not doc.get("industries_title"):
		doc.industries_eyebrow = "Industries"
		doc.industries_title = "Industries we serve"
		doc.industries_description = (
			"From dairy and packaging to retail and logistics — technology mapped to the realities of each sector."
		)
		doc.industries_limit = 12
	doc.show_industries = 1

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
