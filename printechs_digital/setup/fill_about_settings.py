# Copyright (c) 2026, Printechs and contributors
"""Seed Website About Settings with approved About Printechs copy."""

import frappe

PARAGRAPHS = [
	"Since 2002, Printechs has been helping businesses across Saudi Arabia improve productivity, visibility and operational control through reliable technology solutions.",
	"We provide integrated solutions across three core areas: Industrial Automation, Retail Technology and Business Software.",
	"From industrial coding and marking systems, labeling and production identification to POS systems, Auto-ID, mobile computing, barcode solutions, electronic shelf labels and weighing systems, we support the technology requirements of manufacturing, distribution and retail operations.",
	"Our Software Solutions division extends these capabilities with ERPNext, retail POS, warehouse management systems, van sales, mobile applications, business intelligence, dashboards, system integration and custom software development.",
	"What makes Printechs different is our ability to connect these technologies into one complete operational environment. A product can be coded on the production line, identified and tracked through the warehouse, managed through ERP, sold through a retail system and monitored through management dashboards.",
	"We work with businesses across industries including food and beverage, manufacturing, retail, distribution, pharmaceuticals, cosmetics, bakery, meat and seafood, pipe and cable, and other industrial sectors.",
	"Our role does not end with supplying technology. Printechs provides application consultation, installation, commissioning, integration, training, preventive maintenance, technical support, consumables and spare parts to support customers throughout the lifecycle of their investment.",
	"With operations supporting customers from Riyadh, Jeddah and Dammam, we combine established international technologies with local knowledge, implementation expertise and after-sales support.",
]


def fill_about_settings():
	if not frappe.db.exists("DocType", "Website About Settings"):
		frappe.throw("Website About Settings doctype is missing")

	doc = frappe.get_single("Website About Settings")
	if doc.get("tagline") and doc.get("paragraphs"):
		return doc.name

	doc.published = 1
	doc.eyebrow = "Printechs"
	doc.tagline = "Industrial Automation. Retail Technology. Business Software."
	doc.closing_line = "Technology that connects your business."
	doc.company_profile_file = "/files/Company_Profile.pdf"
	doc.company_profile_label = "Download Profile"
	doc.meta_title = "About Printechs | Industrial, Retail & Software Solutions Saudi Arabia"
	doc.meta_description = PARAGRAPHS[0]
	doc.set(
		"paragraphs",
		[{"body": paragraph, "sort_order": index + 1} for index, paragraph in enumerate(PARAGRAPHS)],
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
