# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product IND.SPA.ANS.4742 — Anser SPH Smart Printhead."""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

NAME = "IND.SPA.ANS.4742"
SLUG = "anser-sph-smart-printhead"
VIDEO_URL = "https://youtu.be/kh28jj6I_60"
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")

HERO_URL = (
	"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
	"enL_catalog_product_thermal_24C29_ezsr74krke.png"
)
STORY_URLS = [
	(
		"anser-sph-angle.png",
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_24C29_i5by8y72xq.png",
	),
	(
		"anser-sph-ports.png",
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_24C29_rh67e6hqpr.png",
	),
	(
		"anser-sph-status.png",
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_24C29_stxzrmi4wp.png",
	),
]


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(
			url,
			headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"},
		)
		with urlopen(request, timeout=30) as response, target.open("wb") as handle:
			handle.write(response.read())
	return f"/files/{filename}"


def fill_anser_sph():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = download_file("anser-sph-smart-printhead.png", HERO_URL)
	story_images = [download_file(filename, url) for filename, url in STORY_URLS]

	doc.display_name = "Anser SPH Smart Printhead"
	doc.website_product_name = "Anser SPH Smart Printhead"
	doc.slug = SLUG
	doc.category = "Coding & Marking"
	doc.subcategory = "Thermal Inkjet"
	doc.category_label = "THERMAL INKJET PRINTHEAD"
	doc.tagline = "Compact TIJ printhead for scalable line coding"
	doc.short_description = (
		"High-resolution thermal inkjet printhead for date, batch, barcode and logo "
		"coding — from a single station to a multi-head factory network."
	)
	doc.long_description = (
		"<p>The ANSER SPH Smart Printhead is a compact thermal inkjet (TIJ) coder for "
		"production-line marking. It prints dates, batch codes, barcodes and graphics "
		"on cartons, film, plastic, glass and foil without the fluid maintenance of "
		"continuous inkjet.</p>"
		"<p>One printhead works as a stand-alone station. The same platform expands to "
		"4-inch print height or more than 32 printheads on a hub, with Modbus and "
		"ANSER Xonnect for remote monitoring. This UK HP/IUT configuration is supplied "
		"without mounting bracket and without anti-shock — specify those options if "
		"the line needs them.</p>"
		"<p>Printechs supplies, installs and supports ANSER coding systems across "
		"Saudi Arabia, including spare printheads, ink and service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "ANSER SPH Smart Printhead thermal inkjet coder"
	doc.hero_trust_chips = "Up to 600 dpi\nHP / IUT cartridges\n5-year warranty"
	doc.story_heading = "Built for simple stations and smart factories"
	doc.visual_story_heading = "See the Smart Printhead"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "SPH Smart Printhead"
	doc.card_brand_label = "ANSER"
	doc.card_summary = (
		"Compact thermal inkjet printhead for date, batch and barcode coding on "
		"production lines."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Specify this printhead for your line"
	doc.final_cta_description = (
		"Printechs can confirm HP or IUT cartridges, mounting, and spare-part "
		"availability for ANSER SPH in Saudi Arabia."
	)
	doc.meta_title = "ANSER SPH Smart Printhead | Thermal Inkjet | Printechs"
	doc.meta_description = (
		"ANSER SPH Smart Printhead thermal inkjet coder from Printechs. "
		"High-resolution date, batch and barcode printing with HP or IUT cartridges."
	)
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "print",
				"title": "High-resolution TIJ",
				"description": "HP up to 600 × 600 dpi or IUT 300 × 600 dpi for sharp text, logos and barcodes.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "One head to a factory network",
				"description": "Start stand-alone, then expand to 4-inch print height or 32+ heads on a hub.",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "One-button operation",
				"description": "Power, message select and print/stop on a single control — less training and fewer errors.",
				"sort_order": 3,
			},
			{
				"icon": "cloud",
				"title": "Remote monitoring",
				"description": "ANSER Xonnect and Modbus for status, alerts and control from phone, tablet or laptop.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Compact head",
				"image": hero,
				"image_alt": "ANSER SPH Smart Printhead",
				"caption": "73 × 39 × 205 mm printhead with built-in photocell and status LED bar.",
				"sort_order": 1,
			},
			{
				"label": "Integration",
				"image": story_images[0],
				"image_alt": "ANSER SPH Smart Printhead side view",
				"caption": "Mount on conveyors, cartoners, flow wrappers and form-fill-seal lines.",
				"sort_order": 2,
			},
			{
				"label": "I/O",
				"image": story_images[1],
				"image_alt": "ANSER SPH ports and connections",
				"caption": "RJ45, USB, power lock and Mini-DP to DB9 for message import and control.",
				"sort_order": 3,
			},
			{
				"label": "Status",
				"image": story_images[2],
				"image_alt": "ANSER SPH status indicator",
				"caption": "Five-colour LED bar for print status and alarms.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "print",
				"title": "Print technology",
				"description": "Thermal inkjet · HP 600 dpi or IUT 300 × 600 dpi",
				"sort_order": 1,
			},
			{
				"icon": "lines",
				"title": "Print height",
				"description": "12.7 mm or 25.4 mm per head · expandable to 4 inches",
				"sort_order": 2,
			},
			{
				"icon": "speed",
				"title": "Line speed",
				"description": "60 m/min at 300 dpi · 300 m/min at 60 dpi",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Connectivity",
				"description": "Ethernet · USB · Modbus · ANSER Xonnect",
				"sort_order": 4,
			},
			{
				"icon": "durability",
				"title": "Throw distance",
				"description": "Up to 6 mm from the substrate",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "Warranty",
				"description": "5-year ANSER NexGen warranty",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Printing performance",
			[
				("Technology", "High-resolution thermal inkjet"),
				("Cartridge", "HP or IUT"),
				("Resolution (HP)", "600 × 600 dpi"),
				("Resolution (IUT)", "300 × 600 dpi"),
				("Print height", "12.7 mm (0.5 in) or 25.4 mm (1.0 in) per head"),
				("Print speed", "60 m/min at 300 dpi · 300 m/min at 60 dpi"),
				("Print distance", "Up to 6 mm"),
				("Photocell", "Built-in"),
			],
		),
		(
			"Data & codes",
			[
				("Static data", "Text, shapes, images"),
				("Dynamic data", "Variables, shift, counter, date/time, barcodes"),
				("Barcodes", "EAN, Code 128/39, Data Matrix, QR, GS1, PDF417, Aztec"),
				("Fonts", "TrueType including Arabic and CJK"),
			],
		),
		(
			"Connectivity",
			[
				("Network", "RJ45 Ethernet"),
				("USB", "Message import and firmware"),
				("Serial", "Mini-DP to DB9"),
				("Protocols", "Modbus TCP/IP, UDP, Modbus RTU 485"),
				("Software", "ANSER Xonnect and Loftware NiceLabel"),
			],
		),
		(
			"Physical",
			[
				("Dimensions", "73.3 × 38.5 × 204.5 mm"),
				("Weight", "320 g"),
				("Operating temperature", "0–40 °C"),
				("Humidity", "0–90% RH, non-condensing"),
				("This configuration", "UK · no bracket · no anti-shock"),
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
				"title": "Food & Beverage",
				"description": "Date, expiry and lot codes on cartons, film and bottles.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage packaging line",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Pharmaceutical",
				"description": "Batch and 2D codes on cartons and secondary packs.",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical packaging line",
				"industry_link": "pharmaceutical",
				"sort_order": 2,
			},
			{
				"title": "Packaging",
				"description": "High-resolution text and barcodes on cases and flexible film.",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Packaging line coding",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Plastic",
				"description": "Lot and logo marking on plastic packs and containers.",
				"image": copy_public_image("industry-plastic.jpg"),
				"image_alt": "Plastic packaging coding",
				"industry_link": "plastic",
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
				"description": "Mounting advice, photocell setup, and line commissioning.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Cartridges",
				"description": "HP and IUT ink supply matched to the substrate.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Spares & service",
				"description": "Printheads, cables and on-site support across KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Message setup, cartridge change and Xonnect basics.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set(
		"package_contents",
		[
			{"item_description": "SPH Smart Printhead (HP/IUT, UK)", "sort_order": 1},
			{"item_description": "Supplied without mounting bracket", "sort_order": 2},
			{"item_description": "Supplied without anti-shock", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("related_products", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "See the Smart Printhead in action",
				"body": (
					"ANSER NexGen Smart Printhead is built for automated lines: compact "
					"integration, one-button control, and room to add more heads as the "
					"factory grows. Watch the overview, then talk to Printechs about the "
					"HP/IUT configuration for your line."
				),
				"video_url": VIDEO_URL,
				"link_label": "Talk to a specialist",
				"link_href": "/contact",
				"sort_order": 1,
			},
			{
				"heading": "Why plants choose TIJ over CIJ for this job",
				"body": (
					"Thermal inkjet uses a sealed cartridge. There is no makeup fluid, "
					"no long ink circuit, and no daily flush for many date-and-batch jobs "
					"on cartons and film. When the line needs more print height or more "
					"lanes, add heads to the same hub instead of buying another full CIJ."
				),
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Carton coding on a packaging line",
				"link_label": "Coding and marking solutions",
				"link_href": "/solutions/coding-marking",
				"sort_order": 2,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "What does HP/IUT mean on this printhead?",
				"answer": (
					"The head accepts HP or IUT thermal inkjet cartridges. HP prints up to "
					"600 × 600 dpi. IUT prints 300 × 600 dpi. Printechs will match the "
					"cartridge to your substrate and code type."
				),
				"sort_order": 1,
			},
			{
				"question": "Does this item include a bracket or anti-shock?",
				"answer": (
					"No. IND.SPA.ANS.4742 is the UK printhead without mounting bracket and "
					"without anti-shock. Ask Printechs if the line needs those options."
				),
				"sort_order": 2,
			},
			{
				"question": "Can I run more than one printhead?",
				"answer": (
					"Yes. A single SPH works stand-alone. The same platform can expand to "
					"4-inch print height or more than 32 printheads on a hub for multi-lane "
					"or multi-side coding."
				),
				"sort_order": 3,
			},
			{
				"question": "How do operators change the print message?",
				"answer": (
					"The head has a one-button control for power, message select and "
					"print/stop. Messages can also be imported over USB or managed through "
					"ANSER Xonnect."
				),
				"sort_order": 4,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	print(f"Filled and published {doc.name} → /products/{doc.slug}")
	return doc.name
