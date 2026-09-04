# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.CAS.1247 — CAS CL-5200P pole label printing scale."""

from pathlib import Path
from shutil import copy2

import frappe

NAME = "RET.SYS.CAS.1247"
RELATED_CN1 = "RET.SYS.CAS.3677"
RELATED_CL5500 = "RET.SYS.CAS.3035"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")


def site_file(path: str) -> str:
	return path if path.startswith("/files/") else f"/files/{path}"


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def related_product_row(name: str, sort_order: int) -> dict | None:
	if not frappe.db.exists("Website Product", name):
		return None
	related = frappe.get_doc("Website Product", name)
	return {
		"related_website_product": name,
		"display_name_override": related.display_name or related.website_product_name,
		"summary_override": related.card_summary or related.short_description,
		"href": f"/products/{related.slug}",
		"image": related.card_image or related.hero_image,
		"sort_order": sort_order,
	}


def fill_cas_cl5200():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = doc.hero_image or site_file("CL5200.jpg")
	secondary = site_file("CAS-CL5200B.png") if (SITE_FILES / "CAS-CL5200B.png").exists() else hero
	brochure = doc.primary_download_file or site_file("CL5200-en.pdf")

	doc.display_name = "CAS CL-5200P"
	doc.website_product_name = "CAS CL-5200P Label Printing Scale"
	doc.category = "Retail Systems"
	doc.subcategory = "Label Printing Scales"
	doc.category_label = "LABEL PRINTING SCALE"
	doc.tagline = "Popular pole-type label printing for grocery and fresh-food retail"
	doc.short_description = (
		"CAS CL-5200P pole label printing scale with large LCD display, 72 speed keys, "
		"dual-range 15/30 kg weighing, built-in thermal printer, and CL-Works Pro "
		"software for supermarkets, butcher shops, and deli counters."
	)
	doc.long_description = (
		"<p>The CAS CL-5200 is one of CAS's most popular retail label printing scales — "
		"a dependable, easy-to-use platform for grocery stores, butcher shops, deli "
		"counters, and general fresh-food retail. This pole-type model combines a large "
		"customer-readable LCD display with fast label printing and straightforward "
		"day-to-day operation.</p>"
		"<p>The CL-5200P includes 72 programmable speed keys with optional double-click "
		"recall, dual-range 15/30 kg capacity with 5/10 g readability, and a stainless "
		"steel weighing tray. Store up to 10,000 PLUs and 1,000 ingredient records, "
		"print barcode labels with nutritional and ingredient data, and manage formats "
		"through free CAS CL-Works Pro software.</p>"
		"<p>Built-in thermal label printing uses an easy-change printer cartridge. "
		"Multiple CL-5200 scales connect over Ethernet with master and slave "
		"relationships, with USB, LAN, RJ11, and RS-232C interfaces for store "
		"integration. A scrolling message bar keeps promotions and product information "
		"visible at the counter.</p>"
		"<p>Printechs supplies, installs, and supports CAS CL-5200 scales across "
		"Saudi Arabia, including labels, networking setup, training, and service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "CAS CL-5200P pole-type label printing scale"
	doc.hero_trust_chips = "15/30 kg dual range\n72 speed keys\n10,000 PLUs"
	doc.story_heading = "Proven label printing for everyday retail"
	doc.visual_story_heading = "Clear display, fast labels"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "CL-5200P"
	doc.card_brand_label = "CAS"
	doc.card_summary = (
		"Popular pole-type label printing scale with large LCD display, "
		"72 speed keys, and dual-range 15/30 kg weighing."
	)
	doc.card_image = hero
	doc.primary_download_label = "Download Brochure"
	doc.primary_download_file = brochure
	doc.final_cta_heading = "Get CL-5200P pricing and label supplies"
	doc.final_cta_description = (
		"Printechs can confirm pole or bench configurations, label formats, "
		"CL-Works Pro setup, and networking for CAS CL-5200 scales in Saudi Arabia."
	)
	doc.meta_title = "CAS CL-5200P Label Printing Scale | Printechs"
	doc.meta_description = (
		"CAS CL-5200P label printing scale from Printechs. "
		"Large LCD display, 72 speed keys, dual-range 15/30 kg pole scale with barcode labels."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "display",
				"title": "Large LCD display",
				"description": "Combined wide LCD is easy for customers and operators to read at busy fresh-food counters.",
				"sort_order": 1,
			},
			{
				"icon": "store",
				"title": "72 speed keys",
				"description": "Pole-type layout with fast PLU recall and optional double-click function for high-volume service.",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "Built-in label printer",
				"description": "Thermal barcode labels with easy-change printer cartridge and scrolling message bar.",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Ethernet networking",
				"description": "Connect multiple scales with master/slave support and manage PLUs through CL-Works Pro.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Pole-type retail scale",
				"image": hero,
				"image_alt": "CAS CL-5200P label printing scale",
				"caption": "Popular CL-5200 pole design with large display and built-in label printer.",
				"sort_order": 1,
			},
			{
				"label": "Bench model also available",
				"image": secondary,
				"image_alt": "CAS CL-5200 bench label printing scale",
				"caption": "CL-5200 is also available in bench format with 54 speed keys for compact counters.",
				"sort_order": 2,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "display",
				"title": "Capacity",
				"description": "15/30 kg dual range · 5/10 g readability",
				"sort_order": 1,
			},
			{
				"icon": "store",
				"title": "Speed keys",
				"description": "72 keys on pole model · 54 on bench model",
				"sort_order": 2,
			},
			{
				"icon": "inventory",
				"title": "PLU memory",
				"description": "Up to 10,000 PLUs · 1,000 ingredient records",
				"sort_order": 3,
			},
			{
				"icon": "print",
				"title": "Printing",
				"description": "Built-in thermal label printer · barcode formats",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "Interfaces",
				"description": "USB · LAN · RJ11 · RS-232C · Ethernet TCP/IP",
				"sort_order": 5,
			},
			{
				"icon": "cloud",
				"title": "Software",
				"description": "Free CAS CL-Works Pro for PLU and label design",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Model configuration",
			[
				("Model", "CAS CL-5200P"),
				("Form factor", "Pole type"),
				("Capacity (dual range)", "15/30 kg"),
				("Readability", "5/10 g"),
				("Speed keys", "72"),
				("Display", "Large combined wide LCD"),
				("Message bar", "Scrolling message bar"),
			],
		),
		(
			"Printing",
			[
				("Printer", "Built-in thermal label printer"),
				("Media", "Easy-to-use printer cartridge"),
				("Barcodes", "Multiple barcode formats supported"),
				("Label data", "Ingredients and nutritional information"),
				("Tray", "Stainless steel weighing tray"),
			],
		),
		(
			"Data & networking",
			[
				("PLU capacity", "Up to 10,000 PLUs"),
				("Ingredients", "Up to 1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP with master/slave support"),
				("Software", "CAS CL-Works Pro (free download)"),
			],
		),
		(
			"Connectivity",
			[
				("USB", "Yes"),
				("LAN", "Yes"),
				("RJ11", "Yes"),
				("RS-232C", "Yes"),
				("Ethernet", "Wired network (TCP/IP)"),
			],
		),
		(
			"Physical",
			[
				("Intended use", "Commercial retail weighing"),
				("Also available", "Bench model with 54 speed keys"),
				("Item code", NAME),
			],
		),
	]
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			spec_rows.append(
				{
					"group_title": group_title,
					"label": label,
					"value": value,
					"sort_order": sort,
				}
			)
			sort += 1
	doc.set("full_specifications", spec_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Grocery & supermarkets",
				"description": "Everyday label printing for fresh-food, deli, and service counters with networked PLU management.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail grocery weighing counter",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Butcher shops",
				"description": "Weight, price, and barcode labels with ingredient data for counter-packed meat products.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Butcher counter weighing",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Deli & bakery",
				"description": "Fast speed-key operation and readable display for high-volume prepared-food departments.",
				"image": copy_public_image("industry-bakery.jpg"),
				"image_alt": "Deli and bakery counter",
				"industry_link": "bakery",
				"sort_order": 3,
			},
			{
				"title": "Specialty retail",
				"description": "General-purpose label printing for industrial and specialty retail weighing applications.",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Specialty retail counter",
				"industry_link": "packaging",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Counter setup, networking, label format loading, and commissioning.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Labels & cartridges",
				"description": "Thermal label rolls and replacement cartridges for CL-5200 media.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Service & spares",
				"description": "On-site support and spare parts through Printechs in Saudi Arabia.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "PLU recall, label formats, and CL-Works Pro basics for store staff.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"downloads",
		[
			{
				"label": "CL-5200 Brochure",
				"file": brochure,
				"download_type": "Brochure",
				"sort_order": 1,
			},
		],
	)

	doc.set(
		"package_contents",
		[
			{"item_description": "CAS CL-5200P pole-type label printing scale", "sort_order": 1},
			{"item_description": "Stainless steel weighing tray", "sort_order": 2},
			{"item_description": "Built-in thermal label printer with cartridge system", "sort_order": 3},
			{"item_description": "Power and interface cabling as supplied by manufacturer", "sort_order": 4},
		],
	)

	related = []
	for idx, product_name in enumerate([RELATED_CN1, RELATED_CL5500], start=1):
		row = related_product_row(product_name, idx)
		if row:
			related.append(row)
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "A proven CL-series workhorse",
				"body": (
					"The CL-5200 is widely used in retail because it balances capability and "
					"simplicity: large readable display, dependable label printing, and "
					"straightforward PLU management through CL-Works Pro."
				),
				"image": hero,
				"image_alt": "CAS CL-5200P label printing scale",
				"link_label": "Retail automation solutions",
				"link_href": "/solutions/retail-automation",
				"sort_order": 1,
			},
			{
				"heading": "Pole or bench to suit your counter",
				"body": (
					"This item is the pole-type CL-5200P with 72 speed keys. Bench models "
					"with 54 speed keys are also available for compact service areas — "
					"ask Printechs which form factor fits your layout."
				),
				"image": secondary,
				"image_alt": "CAS CL-5200 bench scale",
				"link_label": "Talk to a specialist",
				"link_href": "/contact",
				"sort_order": 2,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "How is CL-5200 different from CL-5500 or CN1?",
				"answer": (
					"CL-5200 is CAS's popular mid-tier label printing scale with a large LCD "
					"display. CL-5500 adds label/receipt flexibility and more advanced printer "
					"features. CN1 is the newer CAS Network series with a 7-inch colour display."
				),
				"sort_order": 1,
			},
			{
				"question": "Which CL-5200 configuration is this item?",
				"answer": (
					f"This website product ({NAME}) is the pole-type CL-5200P with "
					"dual-range 15/30 kg capacity and 72 speed keys. Bench models with "
					"54 speed keys are available on request."
				),
				"sort_order": 2,
			},
			{
				"question": "Can multiple scales share PLU data?",
				"answer": (
					"Yes. CL-5200 scales connect over Ethernet with master and slave "
					"relationships, and PLU data can be managed centrally with CL-Works Pro."
				),
				"sort_order": 3,
			},
			{
				"question": "Do you supply labels and installation?",
				"answer": (
					"Printechs supplies CAS CL-5200 scales, compatible thermal labels, "
					"installation, CL-Works Pro setup, training, and service across "
					"Saudi Arabia."
				),
				"sort_order": 4,
			},
		],
	)

	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(f"Filled Website Product {doc.name} ({doc.slug})")
