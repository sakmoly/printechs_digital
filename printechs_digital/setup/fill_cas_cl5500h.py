# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.CAS.3036 — CAS CL-5500H hanging label printing scale."""

from pathlib import Path
from shutil import copy2

import frappe

NAME = "RET.SYS.CAS.3036"
RELATED_POLE = "RET.SYS.CAS.3035"
RELATED_CN1 = "RET.SYS.CAS.3677"
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


def fill_cas_cl5500h():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = doc.hero_image or site_file("CL5500H-60.jpg")
	secondary = site_file("CAS-5500H.png") if (SITE_FILES / "CAS-5500H.png").exists() else hero
	brochure = doc.primary_download_file or site_file("brochure-cl-5500d.pdf")

	doc.display_name = "CAS CL-5500H"
	doc.website_product_name = "CAS CL-5500H Label Printing Scale"
	doc.category = "Retail Systems"
	doc.subcategory = "Label Printing Scales"
	doc.category_label = "HANGING LABEL PRINTING SCALE"
	doc.tagline = "Overhead hanging label printing for busy fresh-food counters"
	doc.short_description = (
		"CAS CL-5500H hanging label printing scale with dual LCD displays, "
		"144 speed keys, dual-range 15/30 kg weighing, high-speed thermal "
		"label printer, and CL-Works Pro software for supermarkets and deli operations."
	)
	doc.long_description = (
		"<p>The CAS CL-5500H is a legal-for-trade label printing scale in a "
		"<strong>hanging overhead configuration</strong> — ideal for butcher shops, "
		"seafood counters, deli departments, and fresh-food retail areas where "
		"bench space is limited and operators need the weighing platter suspended "
		"for easy product handling.</p>"
		"<p>Two high-quality LCD displays show tare weight, unit weight, unit price, "
		"and total price on the operator side, with PLU names, scrolling messages, "
		"and programming menus on the customer-facing display. The double-click speed "
		"key function allows fast PLU recall without using the shift key.</p>"
		"<p>Print barcode labels at up to 100 mm/s with 202 dpi resolution using "
		"quick-change label cartridges. Store 4,000 PLUs with direct ingredient "
		"messages, use 50 preset label formats, and add up to 20 custom formats "
		"through CAS CL-Works Pro. Supports UPC, EAN, Code 128, and other barcode "
		"symbologies on die-cut or continuous labels from 40–60 mm wide.</p>"
		"<p>This 60 lb / 30 kg dual-range model (15 kg × 5 g / 30 kg × 10 g) "
		"connects via RS-232C, USB, and built-in 100 Base-T Ethernet, with optional "
		"wireless networking available. Printechs supplies, installs, and supports "
		"CAS CL-5500 scales across Saudi Arabia.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "CAS CL-5500H hanging label printing scale"
	doc.hero_trust_chips = "Hanging overhead design\n15/30 kg dual range\n144 speed keys"
	doc.story_heading = "Label printing where counter space is tight"
	doc.visual_story_heading = "Built for hanging fresh-food service"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "CL-5500H"
	doc.card_brand_label = "CAS"
	doc.card_summary = (
		"Hanging label printing scale with dual LCD displays, 144 speed keys, "
		"and dual-range 15/30 kg weighing."
	)
	doc.card_image = hero
	doc.primary_download_label = "Download Brochure"
	doc.primary_download_file = brochure
	doc.final_cta_heading = "Specify CL-5500H for your fresh-food counter"
	doc.final_cta_description = (
		"Printechs can confirm hanging-scale mounting, networking, label formats, "
		"CL-Works Pro setup, and supplies for CAS CL-5500H in Saudi Arabia."
	)
	doc.meta_title = "CAS CL-5500H Hanging Label Printing Scale | Printechs"
	doc.meta_description = (
		"CAS CL-5500H hanging label printing scale from Printechs. "
		"Dual-range 15/30 kg overhead scale with barcode labels and CL-Works Pro."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "store",
				"title": "Hanging overhead design",
				"description": "Frees counter space in butcher, seafood, and deli departments while keeping the platter at a comfortable working height.",
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "Dual LCD displays",
				"description": "Operator and customer displays show weight, price, PLU names, and scrolling messages clearly.",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "High-speed label printing",
				"description": "Thermal printer up to 100 mm/s at 202 dpi with quick-change label cartridges.",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Store networking",
				"description": "Built-in Ethernet plus RS-232C and USB; optional wireless kit for multi-scale management.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Hanging scale layout",
				"image": hero,
				"image_alt": "CAS CL-5500H hanging label printing scale",
				"caption": "Overhead hanging configuration for fresh-food counters with limited bench space.",
				"sort_order": 1,
			},
			{
				"label": "Operator display",
				"image": secondary,
				"image_alt": "CAS CL-5500H display and keyboard",
				"caption": "Dual LCD displays and 144 speed keys with double-click PLU recall.",
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
				"description": "144 keys (72 × 2) with double-click recall",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "Printer",
				"description": "100 mm/s thermal · 202 dpi · quick-change cartridge",
				"sort_order": 3,
			},
			{
				"icon": "inventory",
				"title": "PLU memory",
				"description": "4,000 PLUs with direct ingredient messages",
				"sort_order": 4,
			},
			{
				"icon": "lines",
				"title": "Label formats",
				"description": "50 preset formats · up to 20 custom via CL-Works Pro",
				"sort_order": 5,
			},
			{
				"icon": "connectivity",
				"title": "Interfaces",
				"description": "RS-232C · USB · 100 Base-T Ethernet · optional WiFi",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Model configuration",
			[
				("Model", "CAS CL-5500H"),
				("Form factor", "Hanging overhead"),
				("Capacity (dual range)", "15/30 kg (30/60 lb)"),
				("Readability", "5/10 g (0.01/0.02 lb)"),
				("Speed keys", "144 (72 × 2)"),
				("Display", "Dual LCD — operator and customer"),
				("Weight units", "kg or lb"),
			],
		),
		(
			"Printing",
			[
				("Print technology", "High-speed thermal"),
				("Print speed", "Up to 100 mm/s"),
				("Resolution", "202 dpi"),
				("Label width", "40–60 mm"),
				("Label length", "30–200 mm"),
				("Label formats", "50 standard · up to 20 custom"),
				("Barcodes", "UPC-A, EAN-13, Code 128, Code 93, Codabar, and more"),
			],
		),
		(
			"Data & software",
			[
				("PLU capacity", "4,000 PLUs"),
				("Ingredient messages", "Direct ingredient text supported"),
				("Software", "CAS CL-Works Pro (PLU, label, and keypad editor)"),
				("Compatibility", "Same menu system as CL-5000 / CL series"),
				("Firmware", "Flash ROM for upgrades"),
				("Languages", "English or Spanish characters"),
			],
		),
		(
			"Connectivity",
			[
				("Ethernet", "100 Base-T TCP/IP (built-in)"),
				("RS-232C", "Yes"),
				("USB", "Yes"),
				("Keyboard", "PS/2 interface"),
				("Wireless", "Optional IEEE 802.11 kit"),
			],
		),
		(
			"Physical",
			[
				("Dimensions (W×D×H)", "420 × 281 × 706 mm"),
				("Product weight", "14.2 kg (31.3 lb)"),
				("Operating temperature", "−10 °C to 40 °C"),
				("Power", "AC 100–240 V, 50/60 Hz"),
				("Measurement", "Load cell"),
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
				"title": "Butcher & meat counters",
				"description": "Overhead hanging platter keeps the work area clear while printing weight, price, and barcode labels.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Fresh meat counter weighing",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Seafood departments",
				"description": "Dual-range weighing for fillets and whole product with high-speed label output at wet counters.",
				"image": copy_public_image("industry-dairy.jpg"),
				"image_alt": "Seafood and fresh food counter",
				"industry_link": "dairy",
				"sort_order": 2,
			},
			{
				"title": "Deli & prepared foods",
				"description": "144 speed keys and scrolling messages for fast service in busy deli operations.",
				"image": copy_public_image("industry-bakery.jpg"),
				"image_alt": "Deli counter service",
				"industry_link": "bakery",
				"sort_order": 3,
			},
			{
				"title": "Supermarkets",
				"description": "Networked label printing across fresh-food departments with CL-Works Pro management.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Supermarket fresh-food section",
				"industry_link": "retail",
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
				"description": "Overhead mounting, networking, label format setup, and trade-verified commissioning.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Labels & cartridges",
				"description": "Thermal label rolls and replacement cartridges matched to CL-5500 media specifications.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Service & options",
				"description": "Fish pan, protective cover, wireless kit, and on-site support through Printechs.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "CL-Works Pro training",
				"description": "PLU programming, custom label design, and sales data export for store teams.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"downloads",
		[
			{
				"label": "CL-5500 Brochure",
				"file": brochure,
				"download_type": "Brochure",
				"sort_order": 1,
			},
		],
	)

	doc.set(
		"package_contents",
		[
			{"item_description": "CAS CL-5500H hanging label printing scale", "sort_order": 1},
			{"item_description": "Built-in high-speed thermal label printer", "sort_order": 2},
			{"item_description": "Dual LCD operator and customer displays", "sort_order": 3},
			{"item_description": "Power and interface cabling as supplied by manufacturer", "sort_order": 4},
		],
	)

	related = []
	for idx, product_name in enumerate([RELATED_POLE, RELATED_CN1], start=1):
		row = related_product_row(product_name, idx)
		if row:
			related.append(row)
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "Hanging scale for space-constrained counters",
				"body": (
					"The CL-5500H keeps the weighing platter overhead so operators have more "
					"room to prepare and pack product. It delivers the same CL-series label "
					"printing, PLU management, and networking capability as bench and pole models."
				),
				"image": hero,
				"image_alt": "CAS CL-5500H hanging scale",
				"link_label": "Retail automation solutions",
				"link_href": "/solutions/retail-automation",
				"sort_order": 1,
			},
			{
				"heading": "CL-Works Pro for labels and PLU control",
				"body": (
					"Manage PLUs, design custom labels, edit speed keys, and analyze sales "
					"data from one PC application. CL-Works Pro supports all recent CAS CL "
					"series label printing scales on the store network."
				),
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail store scale management",
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
				"question": "When should I choose the hanging CL-5500H?",
				"answer": (
					"Choose the CL-5500H when you need an overhead weighing platter — "
					"common in butcher, seafood, and deli areas where bench space is limited "
					"or operators prefer a suspended scale pan."
				),
				"sort_order": 1,
			},
			{
				"question": "How is CL-5500H different from the pole CL-5500D?",
				"answer": (
					"The CL-5500H uses a hanging overhead form factor. The CL-5500D pole model "
					"is floor-standing with a vertical column. Both support label printing, "
					"but mounting and counter layout differ."
				),
				"sort_order": 2,
			},
			{
				"question": "Which configuration is this item?",
				"answer": (
					f"This website product ({NAME}) is the CL-5500H hanging model with "
					"dual-range 15/30 kg (30/60 lb) capacity. Bench and pole CL-5500 variants "
					"are available on request."
				),
				"sort_order": 3,
			},
			{
				"question": "Can Printechs supply labels and install the scale?",
				"answer": (
					"Yes. Printechs supplies CAS CL-5500H scales, compatible thermal labels, "
					"optional accessories, installation, CL-Works Pro setup, and service across "
					"Saudi Arabia."
				),
				"sort_order": 4,
			},
		],
	)

	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(f"Filled Website Product {doc.name} ({doc.slug})")
