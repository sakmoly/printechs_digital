# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.CAS.1246 — CAS CL-5200B bench label printing scale."""

from pathlib import Path
from shutil import copy2

import frappe

NAME = "RET.SYS.CAS.1246"
RELATED_POLE = "RET.SYS.CAS.1247"
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


def fill_cas_cl5200b():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = site_file("CAS-CL5200B.png") if (SITE_FILES / "CAS-CL5200B.png").exists() else (
		doc.hero_image or site_file("CL5000B.jpg")
	)
	pole_image = site_file("CL5200.jpg")
	brochure = doc.primary_download_file or site_file("CL5200-en.pdf")

	doc.display_name = "CAS CL-5200B"
	doc.website_product_name = "CAS CL-5200B Label Printing Scale"
	doc.category = "Retail Systems"
	doc.subcategory = "Label Printing Scales"
	doc.category_label = "LABEL PRINTING SCALE"
	doc.tagline = "Compact bench-type label printing for retail counters"
	doc.short_description = (
		"CAS CL-5200B bench label printing scale with large LCD display, 54 speed keys, "
		"dual-range 15/30 kg weighing, easy-change label cartridge, wired/wireless "
		"networking, and CL-Works Pro software."
	)
	doc.long_description = (
		"<p>The CAS CL-5200B is the <strong>bench-type</strong> version of CAS's popular "
		"CL-5200 label printing scale — ideal for grocery stores, butcher shops, deli "
		"counters, and specialty retail where a compact footprint on the service counter "
		"matters.</p>"
		"<p>Features include a large customer-readable LCD display, 54 programmable speed "
		"keys with optional double-click recall, dual-range 15/30 kg capacity with 5/10 g "
		"readability, and a stainless steel weighing tray. Store up to 10,000 PLUs and "
		"1,000 ingredient records, print barcode labels with nutritional information, "
		"and design custom formats with free CAS CL-Works Pro software.</p>"
		"<p>The built-in thermal printer uses an easy-loading label cartridge. Connect "
		"over Ethernet with master and slave support, with USB, LAN, RJ11, and RS-232C "
		"interfaces. Flexible wired and wireless network options help multi-scale store "
		"deployments. A scrolling message bar keeps product and promotional information "
		"visible at the counter.</p>"
		"<p>Printechs supplies, installs, and supports CAS CL-5200 scales across "
		"Saudi Arabia, including labels, networking, training, and service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "CAS CL-5200B bench-type label printing scale"
	doc.hero_trust_chips = "Bench-type design\n15/30 kg dual range\n54 speed keys"
	doc.story_heading = "Compact label printing for the service counter"
	doc.visual_story_heading = "Proven CL-5200 performance in bench format"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "CL-5200B"
	doc.card_brand_label = "CAS"
	doc.card_summary = (
		"Bench-type label printing scale with large LCD display, "
		"54 speed keys, and dual-range 15/30 kg weighing."
	)
	doc.card_image = hero
	doc.primary_download_label = "Download Brochure"
	doc.primary_download_file = brochure
	doc.final_cta_heading = "Get CL-5200B pricing and label supplies"
	doc.final_cta_description = (
		"Printechs can confirm bench or pole configurations, label formats, "
		"CL-Works Pro setup, and networking for CAS CL-5200 scales in Saudi Arabia."
	)
	doc.meta_title = "CAS CL-5200B Label Printing Scale | Printechs"
	doc.meta_description = (
		"CAS CL-5200B bench label printing scale from Printechs. "
		"Compact counter scale with 54 speed keys, dual-range 15/30 kg, and barcode labels."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "checkout",
				"title": "Compact bench design",
				"description": "Fits directly on the service counter — ideal where pole-type scales are not required.",
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "Large LCD display",
				"description": "Combined wide LCD keeps weight, price, and PLU information clear for staff and customers.",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "Easy label cartridge",
				"description": "Quick-loading thermal label cartridge with free-format label design through CL-Works Pro.",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Flexible networking",
				"description": "Wired Ethernet with optional wireless — master/slave support for multi-scale stores.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Bench counter scale",
				"image": hero,
				"image_alt": "CAS CL-5200B bench label printing scale",
				"caption": "Compact bench layout for delis, butcher counters, and specialty retail.",
				"sort_order": 1,
			},
			{
				"label": "Pole model also available",
				"image": pole_image,
				"image_alt": "CAS CL-5200P pole label printing scale",
				"caption": "Need a pole-type layout? The CL-5200P offers 72 speed keys for high-volume service.",
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
				"description": "54 keys on bench model · 72 on pole model",
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
				"description": "Built-in thermal label printer · easy-change cartridge",
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
				("Model", "CAS CL-5200B"),
				("Form factor", "Bench type"),
				("Capacity (dual range)", "15/30 kg"),
				("Readability", "5/10 g"),
				("Speed keys", "54"),
				("Display", "Large combined wide LCD"),
				("Message bar", "Scrolling message bar"),
			],
		),
		(
			"Printing",
			[
				("Printer", "Built-in thermal label printer"),
				("Media", "Easy-loading label cartridge"),
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
				("Wireless", "Optional wireless network support"),
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
				("Also available", "Pole model CL-5200P with 72 speed keys"),
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
				"description": "Compact bench label printing for deli, fresh-food, and service counters.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail grocery counter",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Butcher shops",
				"description": "Barcode labels with weight, price, and ingredient data on a space-efficient bench scale.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Butcher counter weighing",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Deli & bakery",
				"description": "54 speed keys and readable display for prepared-food departments with limited counter depth.",
				"image": copy_public_image("industry-bakery.jpg"),
				"image_alt": "Deli counter",
				"industry_link": "bakery",
				"sort_order": 3,
			},
			{
				"title": "Specialty retail",
				"description": "General-purpose bench weighing and label printing for specialty and industrial retail.",
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
				"description": "Bench placement, networking, label format setup, and commissioning.",
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
				"description": "PLU programming, label design, and CL-Works Pro for store teams.",
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
			{"item_description": "CAS CL-5200B bench-type label printing scale", "sort_order": 1},
			{"item_description": "Stainless steel weighing tray", "sort_order": 2},
			{"item_description": "Built-in thermal label printer with cartridge system", "sort_order": 3},
			{"item_description": "Power and interface cabling as supplied by manufacturer", "sort_order": 4},
		],
	)

	related = []
	for idx, product_name in enumerate([RELATED_POLE, RELATED_CN1, RELATED_CL5500], start=1):
		row = related_product_row(product_name, idx)
		if row:
			related.append(row)
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "Bench format when space is tight",
				"body": (
					"The CL-5200B sits directly on the counter — the same proven CL-5200 label "
					"printing platform as the pole model, in a compact bench layout with "
					"54 speed keys for everyday fresh-food retail."
				),
				"image": hero,
				"image_alt": "CAS CL-5200B bench scale",
				"link_label": "Retail automation solutions",
				"link_href": "/solutions/retail-automation",
				"sort_order": 1,
			},
			{
				"heading": "CL-Works Pro and flexible networking",
				"body": (
					"Program PLUs, design labels, and connect multiple scales over wired or "
					"wireless networks. CL-Works Pro makes it straightforward to manage "
					"label formats across departments."
				),
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Retail store operations",
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
				"question": "What is the difference between CL-5200B and CL-5200P?",
				"answer": (
					"CL-5200B is the bench-type model with 54 speed keys that sits on the counter. "
					"CL-5200P is the pole-type model with 72 speed keys for taller, floor-standing "
					"layouts. Both share the same label printing and networking capability."
				),
				"sort_order": 1,
			},
			{
				"question": "Which configuration is this item?",
				"answer": (
					f"This website product ({NAME}) is the bench-type CL-5200B with "
					"dual-range 15/30 kg capacity and 54 speed keys."
				),
				"sort_order": 2,
			},
			{
				"question": "Does it support wireless networking?",
				"answer": (
					"CL-5200 scales support flexible wired and wireless network configurations. "
					"Ask Printechs about wireless options for your store layout."
				),
				"sort_order": 3,
			},
			{
				"question": "Can Printechs supply labels and install the scale?",
				"answer": (
					"Yes. Printechs supplies CAS CL-5200B scales, compatible thermal labels, "
					"installation, CL-Works Pro setup, training, and service across Saudi Arabia."
				),
				"sort_order": 4,
			},
		],
	)

	doc.save(ignore_permissions=True)
	frappe.db.commit()
	print(f"Filled Website Product {doc.name} ({doc.slug})")
