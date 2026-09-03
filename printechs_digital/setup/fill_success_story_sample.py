# Copyright (c) 2026, Printechs and contributors
"""Publish one sample Hitachi success story so the product button can be checked."""

import frappe

SLUG = "hitachi-dairy-line-riyadh"


def fill_success_story_sample():
	product = frappe.db.get_value(
		"Website Product",
		{"slug": "hitachi-ux-d161", "published": 1},
		["name", "brand", "display_name"],
		as_dict=True,
	)
	if not product:
		print("Skip: Website Product hitachi-ux-d161 is not published")
		return

	hero = "/files/UX-D161W.jpg" if frappe.db.exists("File", {"file_url": "/files/UX-D161W.jpg"}) else None
	if not hero:
		hero = frappe.db.get_value("Website Product", product.name, "hero_image")

	if frappe.db.exists("Website Success Story", {"slug": SLUG}):
		doc = frappe.get_doc("Website Success Story", {"slug": SLUG})
	else:
		doc = frappe.new_doc("Website Success Story")
		doc.slug = SLUG

	doc.title = "Dairy line coding upgrade in Riyadh"
	doc.published = 1
	doc.featured = 1
	doc.sort_order = 1
	doc.website_product = product.name
	doc.brand = product.brand
	doc.industry = "Dairy"
	doc.customer_name = "Regional dairy producer"
	doc.location = "Riyadh, Saudi Arabia"
	doc.summary = (
		"Hitachi UX-D161 installed on a high-speed dairy filling line for date, "
		"batch and expiry coding with cleaner print quality and less downtime."
	)
	doc.story = """
		<p>A Riyadh dairy producer needed reliable date and batch coding on high-speed filling lines without stopping production for frequent printhead cleaning.</p>
		<p>Printechs specified and installed a Hitachi UX-D161 continuous inkjet printer, mounted at the filler discharge, with operator training and a consumables plan.</p>
		<p>The line now prints date, batch and expiry codes consistently on bottles and cartons. The customer has a single support contact for hardware, ink and service across Saudi Arabia.</p>
	"""
	doc.hero_image = hero
	doc.hero_image_alt = "Hitachi UX-D161 on a dairy packaging line"
	doc.meta_title = "Dairy Line Coding Upgrade | Hitachi Success Story | Printechs"
	doc.meta_description = (
		"See how Printechs installed Hitachi UX-D161 coding on a Riyadh dairy line."
	)

	if not doc.gallery:
		if hero:
			doc.append(
				"gallery",
				{
					"image": hero,
					"image_alt": "Hitachi UX-D161 continuous inkjet printer",
					"caption": "UX-D161 installed for dairy coding",
					"sort_order": 1,
				},
			)

	doc.save()
	frappe.db.commit()
	print(f"Published success story {doc.name}")
