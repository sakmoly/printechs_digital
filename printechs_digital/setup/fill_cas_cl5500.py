# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.CAS.3035 — CAS CL-5500D pole label printing scale."""

from pathlib import Path
from shutil import copy2

import frappe

NAME = "RET.SYS.CAS.3035"
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


def fill_cas_cl5500():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = doc.hero_image or site_file("CL5500P.jpg")
	bench_image = site_file("CL5500H-60.jpg")
	brochure = doc.primary_download_file or site_file("brochure-cl-5500d.pdf")

	doc.display_name = "CAS CL-5500D"
	doc.website_product_name = "CAS CL-5500D Label & Receipt Printing Scale"
	doc.category = "Retail Systems"
	doc.subcategory = "Label Printing Scales"
	doc.category_label = "LABEL & RECEIPT PRINTING SCALE"
	doc.tagline = "Label and receipt printing for grocery and fresh-food counters"
	doc.short_description = (
		"Trade-capable CAS retail scale with built-in thermal label and receipt printer, "
		"72 speed keys, dual-range 15/30 kg weighing, and Ethernet networking for "
		"multi-scale store environments."
	)
	doc.long_description = (
		"<p>The CAS CL-5500D is a label and receipt printing scale designed for "
		"grocery stores, butcher shops, deli counters, and fresh-food departments that "
		"need accurate weighing, barcode labels, and customer receipts from one compact "
		"station.</p>"
		"<p>This pole-type configuration offers 72 programmable speed keys and a dual-range "
		"capacity of 15/30 kg with 5/10 g readability, giving accurate readings for both "
		"light and heavier items. Operators can switch between label and ticket modes using "
		"a quick-change printer cartridge system, while the LCD display and scrolling "
		"message bar keep pricing and product information visible at the counter.</p>"
		"<p>Store up to 10,000 PLUs with ingredient and nutritional data, print multiple "
		"barcode formats, and manage programming through free CAS CL-Works Pro software. "
		"Multiple CL-5500 scales can be connected over Ethernet with master and slave "
		"relationships, floating clerk function, and interfaces for USB, LAN, RJ11, and "
		"RS-232C integration.</p>"
		"<p>Printechs supplies, installs, and supports CAS weighing systems across Saudi "
		"Arabia, including label rolls, spare parts, training, and service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "CAS CL-5500D pole-type label and receipt printing scale"
	doc.hero_trust_chips = "15/30 kg dual range\n72 speed keys\nLabel & receipt modes"
	doc.story_heading = "Weigh, label, and receipt from one counter"
	doc.visual_story_heading = "Built for busy retail departments"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "CL-5500D"
	doc.card_brand_label = "CAS"
	doc.card_summary = (
		"Pole-type label and receipt printing scale with dual-range weighing, "
		"72 speed keys, and Ethernet networking."
	)
	doc.card_image = hero
	doc.primary_download_label = "Download Brochure"
	doc.primary_download_file = brochure
	doc.final_cta_heading = "Get pricing, labels, and installation support"
	doc.final_cta_description = (
		"Printechs can confirm pole or bench configurations, capacity options, "
		"label supplies, and CL-Works Pro setup for CAS CL-5500 scales in Saudi Arabia."
	)
	doc.meta_title = "CAS CL-5500D Label & Receipt Printing Scale | Printechs"
	doc.meta_description = (
		"CAS CL-5500D label and receipt printing scale from Printechs. "
		"Dual-range 15/30 kg pole scale with barcode labels, receipts, and Ethernet networking."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "checkout",
				"title": "Label or receipt mode",
				"description": "Switch between thermal label and customer receipt printing with a quick-change printer cartridge.",
				"sort_order": 1,
			},
			{
				"icon": "store",
				"title": "72 speed keys",
				"description": "Pole-type layout with fast PLU recall for high-volume deli, butcher, and grocery counters.",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "Dual-range accuracy",
				"description": "15/30 kg capacity with 5/10 g increments for precise weighing of light and heavier items.",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Networked store operation",
				"description": "Ethernet master/slave support, floating clerk function, and CL-Works Pro PLU programming.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Pole-type counter scale",
				"image": hero,
				"image_alt": "CAS CL-5500D pole-type label printing scale",
				"caption": "Compact pole design with LCD display, speed keys, and built-in thermal printer.",
				"sort_order": 1,
			},
			{
				"label": "Fresh-food service",
				"image": bench_image,
				"image_alt": "CAS CL-5500 scale at a fresh-food counter",
				"caption": "Ideal for grocery, butcher, deli, and seafood departments that print labels and receipts.",
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
				"description": "72 programmable keys on pole-type model",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "Printing",
				"description": "Built-in thermal label and receipt printer",
				"sort_order": 3,
			},
			{
				"icon": "inventory",
				"title": "PLU memory",
				"description": "Up to 10,000 PLUs with ingredient and nutrition data",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "Interfaces",
				"description": "USB · LAN · RJ11 · RS-232C · Ethernet network",
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
				("Model", "CAS CL-5500D"),
				("Form factor", "Pole type"),
				("Capacity (dual range)", "15/30 kg"),
				("Readability", "5/10 g"),
				("Speed keys", "72"),
				("Display", "LCD with scrolling message bar"),
			],
		),
		(
			"Printing",
			[
				("Printer", "Built-in thermal label and receipt printer"),
				("Modes", "Label or ticket/receipt"),
				("Media change", "Quick-change printer cartridge system"),
				("Barcodes", "Multiple barcode formats supported"),
				("Label data", "Ingredients and nutritional information"),
			],
		),
		(
			"Data & networking",
			[
				("PLU capacity", "Up to 10,000 PLUs"),
				("Ingredients", "Up to 1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP with master/slave support"),
				("Clerk function", "Floating clerk supported"),
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
				("Weighing pan", "Stainless steel tray"),
				("Intended use", "Commercial retail weighing"),
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
				"description": "Pre-packed fresh items, deli counters, and weighed product labelling with barcode PLUs.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail grocery weighing counter",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Butcher & fresh meat",
				"description": "Label packed-on dates, weight, price, and barcode data at the service counter.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Fresh food counter weighing",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Bakery & deli",
				"description": "Fast PLU recall and receipt printing for high-volume fresh-food departments.",
				"image": copy_public_image("industry-bakery.jpg"),
				"image_alt": "Bakery and deli counter",
				"industry_link": "bakery",
				"sort_order": 3,
			},
			{
				"title": "Seafood & specialty counters",
				"description": "Dual-range weighing for light fillets and heavier whole products on one scale.",
				"image": copy_public_image("industry-dairy.jpg"),
				"image_alt": "Fresh food service counter",
				"industry_link": "dairy",
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
				"description": "Counter placement, network setup, label format loading, and commissioning.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Labels & ribbons",
				"description": "Thermal label rolls and receipt rolls matched to CL-5500 media specifications.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Service & spares",
				"description": "On-site support, printer cartridges, and spare parts through Printechs in KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "PLU recall, label/receipt mode change, and CL-Works Pro basics for store teams.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"downloads",
		[
			{
				"label": "CL-5500D Brochure",
				"file": brochure,
				"download_type": "Brochure",
				"sort_order": 1,
			},
		],
	)

	doc.set(
		"package_contents",
		[
			{"item_description": "CAS CL-5500D pole-type label printing scale", "sort_order": 1},
			{"item_description": "Stainless steel weighing tray", "sort_order": 2},
			{"item_description": "Built-in thermal printer cartridge system", "sort_order": 3},
			{"item_description": "Power and interface cabling as supplied by manufacturer", "sort_order": 4},
		],
	)

	doc.set("ecosystem_items", [])
	doc.set("related_products", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "One scale for labels and customer receipts",
				"body": (
					"The CL-5500 family is designed for fresh-food retail where staff need to "
					"weigh quickly, print a barcode label, and hand the customer a receipt — "
					"without changing hardware. The printer cartridge system makes it practical "
					"to switch media at the counter."
				),
				"image": hero,
				"image_alt": "CAS CL-5500D label printing scale",
				"link_label": "Retail automation solutions",
				"link_href": "/solutions/retail-automation",
				"sort_order": 1,
			},
			{
				"heading": "Program once, operate across the store",
				"body": (
					"CL-Works Pro software simplifies PLU creation, custom label design, and "
					"network deployment. Connect multiple scales over Ethernet for consistent "
					"pricing and product data across departments."
				),
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail store technology",
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
				"question": "What is the difference between label mode and receipt mode?",
				"answer": (
					"In label mode the scale prints adhesive barcode/price labels for packaged "
					"product. In receipt/ticket mode it prints a customer receipt. The CL-5500 "
					"uses a quick-change printer cartridge so staff can swap media for the task."
				),
				"sort_order": 1,
			},
			{
				"question": "Which CL-5500 configuration is this item?",
				"answer": (
					f"This website product ({NAME}) is the pole-type CL-5500D with dual-range "
					"15/30 kg capacity and 5/10 g readability. Bench-type models with 48 speed "
					"keys and other capacities are available on request."
				),
				"sort_order": 2,
			},
			{
				"question": "Can multiple scales share the same PLU database?",
				"answer": (
					"Yes. CL-5500 scales can be connected over Ethernet with master and slave "
					"relationships, and PLU data can be managed through CL-Works Pro."
				),
				"sort_order": 3,
			},
			{
				"question": "Do you supply labels and provide installation?",
				"answer": (
					"Printechs supplies CAS scales, compatible thermal labels and receipt rolls, "
					"installation, training, and local service across Saudi Arabia."
				),
				"sort_order": 4,
			},
		],
	)

	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(f"Filled Website Product {doc.name} ({doc.slug})")
