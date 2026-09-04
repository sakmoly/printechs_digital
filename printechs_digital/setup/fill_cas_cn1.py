# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.CAS.3677 — CAS CN1 pole label printing scale."""

from pathlib import Path
from shutil import copy2

import frappe

NAME = "RET.SYS.CAS.3677"
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


def fill_cas_cn1():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = doc.hero_image or site_file("CN.jpg")
	secondary = site_file("CAS-CN.png") if (SITE_FILES / "CAS-CN.png").exists() else hero
	brochure = doc.primary_download_file or site_file(
		"bXin04WDlsflm1FL8s8FgIe7RS1Ul2o8FufRxuuT.pdf"
	)

	doc.display_name = "CAS CN1"
	doc.website_product_name = "CAS CN1 Label Printing Scale"
	doc.category = "Retail Systems"
	doc.subcategory = "Label Printing Scales"
	doc.category_label = "LABEL PRINTING SCALE"
	doc.tagline = "Network-ready label printing with a 7-inch colour display"
	doc.short_description = (
		"CAS CN series label printing scale with 7-inch colour customer display, "
		"72 speed keys, dual-range 15/30 kg weighing, enhanced Ethernet networking, "
		"and CL-Works Pro compatibility for modern grocery and fresh-food counters."
	)
	doc.long_description = (
		"<p>The CAS CN1 is the first model in CAS's CN network printer-scale series — "
		"CN stands for <strong>CAS Network</strong>. It combines robust remote and "
		"store-network functionality with a bright 7-inch colour display that is easy "
		"for both operators and customers to read.</p>"
		"<p>Designed for grocery stores, butcher shops, deli counters, and fresh-food "
		"departments, the CN1 prints barcode labels with weight, price, packed-on date, "
		"ingredient, and nutritional information. Store up to 10,000 PLUs and 1,000 "
		"ingredient records, with free CAS CL-Works Pro software for programming and "
		"custom label design.</p>"
		"<p>This pole-type configuration includes 72 programmable speed keys with "
		"optional double-click function, dual-range 15/30 kg capacity with 5/10 g "
		"readability, and a stainless steel weighing tray. Multiple CN1 scales connect "
		"over wired Ethernet with master and slave relationships. CN1 is compatible "
		"with the existing CAS CL series ecosystem and succeeds the popular LP1 family.</p>"
		"<p>Printechs supplies, installs, and supports CAS weighing systems across "
		"Saudi Arabia, including labels, networking setup, training, and service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "CAS CN1 pole-type label printing scale with colour display"
	doc.hero_trust_chips = "7″ colour display\n15/30 kg dual range\n72 speed keys"
	doc.story_heading = "The connected label scale for modern retail"
	doc.visual_story_heading = "Designed for visible, fast fresh-food service"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "CN1"
	doc.card_brand_label = "CAS"
	doc.card_summary = (
		"Network-ready label printing scale with 7-inch colour display, "
		"72 speed keys, and dual-range 15/30 kg weighing."
	)
	doc.card_image = hero
	doc.primary_download_label = "Download Brochure"
	doc.primary_download_file = brochure
	doc.final_cta_heading = "Plan your CN1 deployment with Printechs"
	doc.final_cta_description = (
		"Printechs can confirm pole configuration, networking, label formats, "
		"CL-Works Pro setup, and supplies for CAS CN1 scales in Saudi Arabia."
	)
	doc.meta_title = "CAS CN1 Label Printing Scale | Printechs"
	doc.meta_description = (
		"CAS CN1 label printing scale from Printechs. 7-inch colour display, "
		"dual-range 15/30 kg pole scale with barcode labels and Ethernet networking."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "display",
				"title": "7-inch colour display",
				"description": "Bright customer-facing screen makes pricing and product information easy to read at the counter.",
				"sort_order": 1,
			},
			{
				"icon": "connectivity",
				"title": "CAS Network ready",
				"description": "Enhanced Ethernet networking with master/slave support for multi-scale store environments.",
				"sort_order": 2,
			},
			{
				"icon": "store",
				"title": "72 speed keys",
				"description": "Fast PLU recall for high-volume deli, butcher, and grocery departments with optional double-click.",
				"sort_order": 3,
			},
			{
				"icon": "inventory",
				"title": "Rich PLU data",
				"description": "Up to 10,000 PLUs with ingredient and nutritional tables for compliant fresh-food labelling.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "CN series pole scale",
				"image": hero,
				"image_alt": "CAS CN1 label printing scale",
				"caption": "Stylish pole design with built-in thermal label printer and colour display.",
				"sort_order": 1,
			},
			{
				"label": "Customer-facing display",
				"image": secondary,
				"image_alt": "CAS CN1 colour display and keyboard",
				"caption": "7-inch vivid display improves menu navigation and customer visibility at fresh-food counters.",
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
				"icon": "display",
				"title": "Display",
				"description": "7-inch vivid colour customer display",
				"sort_order": 2,
			},
			{
				"icon": "store",
				"title": "Speed keys",
				"description": "72 programmable keys · pole type only",
				"sort_order": 3,
			},
			{
				"icon": "print",
				"title": "Printing",
				"description": "Built-in thermal label printer with barcode support",
				"sort_order": 4,
			},
			{
				"icon": "inventory",
				"title": "PLU memory",
				"description": "Up to 10,000 PLUs · 1,000 ingredient records",
				"sort_order": 5,
			},
			{
				"icon": "connectivity",
				"title": "Interfaces",
				"description": "USB · LAN · RJ11 · RS-232C · Ethernet TCP/IP",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Model configuration",
			[
				("Model", "CAS CN1"),
				("Series", "CN — CAS Network"),
				("Form factor", "Pole type"),
				("Capacity (dual range)", "15/30 kg"),
				("Readability", "5/10 g"),
				("Speed keys", "72"),
				("Display", "7-inch colour display"),
			],
		),
		(
			"Printing",
			[
				("Printer", "Built-in thermal label printer"),
				("Barcodes", "Multiple barcode formats supported"),
				("Label data", "Ingredients and nutritional information"),
				("Message bar", "Scrolling message bar"),
				("Tray", "Stainless steel weighing tray"),
			],
		),
		(
			"Data & networking",
			[
				("PLU capacity", "Up to 10,000 PLUs"),
				("Ingredients", "Up to 1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP with master/slave support"),
				("Compatibility", "Compatible with CAS CL series ecosystem"),
				("Software", "CAS CL-Works Pro (free download)"),
				("Predecessor", "Successor to LP1 series scales"),
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
				("Body", "Dark grey retail housing"),
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
				"description": "Fresh-food labelling with barcode PLUs, pricing, and ingredient information at service counters.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail grocery weighing counter",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Butcher & fresh meat",
				"description": "Packed-on dates, weight, price, and barcode labels for counter-packed meat products.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Fresh food counter weighing",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Deli & bakery",
				"description": "Fast PLU recall and clear customer display for high-volume fresh-food departments.",
				"image": copy_public_image("industry-bakery.jpg"),
				"image_alt": "Bakery and deli counter",
				"industry_link": "bakery",
				"sort_order": 3,
			},
			{
				"title": "Seafood counters",
				"description": "Dual-range weighing for light fillets and heavier whole products with compliant label data.",
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
				"description": "Counter placement, IP/network setup, label format loading, and commissioning.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Labels",
				"description": "Thermal label rolls matched to CN1 media and label design requirements.",
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
				"description": "PLU recall, label formats, and CL-Works Pro basics for store teams.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"downloads",
		[
			{
				"label": "CN1 Brochure",
				"file": brochure,
				"download_type": "Brochure",
				"sort_order": 1,
			},
		],
	)

	doc.set(
		"package_contents",
		[
			{"item_description": "CAS CN1 pole-type label printing scale", "sort_order": 1},
			{"item_description": "Stainless steel weighing tray", "sort_order": 2},
			{"item_description": "Built-in thermal label printer", "sort_order": 3},
			{"item_description": "Power and interface cabling as supplied by manufacturer", "sort_order": 4},
		],
	)

	related = []
	if frappe.db.exists("Website Product", RELATED_CL5500):
		cl5500 = frappe.get_doc("Website Product", RELATED_CL5500)
		related.append(
			{
				"related_website_product": RELATED_CL5500,
				"display_name_override": cl5500.display_name or "CAS CL-5500D",
				"summary_override": (
					cl5500.card_summary
					or "Label and receipt printing scale with cartridge-based media change."
				),
				"href": f"/products/{cl5500.slug}",
				"image": cl5500.card_image or cl5500.hero_image,
				"sort_order": 1,
			}
		)
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "CAS Network for connected stores",
				"body": (
					"The CN series was built for retailers who need more than a standalone scale. "
					"CN1 adds stronger network capability, remote management potential, and a "
					"colour display while remaining compatible with CAS CL series workflows and "
					"CL-Works Pro programming."
				),
				"image": hero,
				"image_alt": "CAS CN1 label printing scale",
				"link_label": "Retail automation solutions",
				"link_href": "/solutions/retail-automation",
				"sort_order": 1,
			},
			{
				"heading": "Clear labelling for fresh-food counters",
				"body": (
					"Print barcode labels with weight, price, dates, ingredients, and nutritional "
					"tables from one pole-type station. Dual-range weighing keeps lighter and "
					"heavier items accurate without changing scales."
				),
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail fresh-food counter",
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
				"question": "What does CN stand for in the CN1 model?",
				"answer": (
					"CN stands for CAS Network. CN1 is the first model in CAS's network-focused "
					"printer-scale series, designed for enhanced Ethernet connectivity and "
					"multi-scale store operation."
				),
				"sort_order": 1,
			},
			{
				"question": "Does the CN1 print receipts as well as labels?",
				"answer": (
					"The CN1 is a label printing scale. If you need both label and receipt/ticket "
					"printing from one station, consider the CAS CL-5500 family instead."
				),
				"sort_order": 2,
			},
			{
				"question": "Which configuration is this item?",
				"answer": (
					f"This website product ({NAME}) is the pole-type CN1 with dual-range "
					"15/30 kg capacity. CN1 is available in pole version only."
				),
				"sort_order": 3,
			},
			{
				"question": "Can Printechs help with networking and labels?",
				"answer": (
					"Yes. Printechs supplies CAS CN1 scales, configures Ethernet networking, "
					"provides compatible thermal labels, and offers installation, training, "
					"and service across Saudi Arabia."
				),
				"sort_order": 4,
			},
		],
	)

	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(f"Filled Website Product {doc.name} ({doc.slug})")
