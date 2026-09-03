# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product IND.SYS.KZT.4982 — Kezojet KT10."""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

NAME = "IND.SYS.KZT.4982"
SLUG = "kezojet-kt10"
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")

# Supplier site (uk-cm.uk) blocks this host with 403. Use the distributor
# product photo, then industry images for other sections.
HERO_URLS = [
	"https://3sink.com/wp-content/uploads/2024/11/kt10.png",
]
HERO_FILES = ("kezojet-kt10-hero.png", "kezojet-kt10-hero.jpg")


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def download_file(filename: str, urls: list[str]) -> str:
	target = SITE_FILES / filename
	if target.exists() and target.stat().st_size > 0:
		return f"/files/{filename}"
	headers = {
		"User-Agent": (
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
		)
	}
	last_error = None
	for url in urls:
		try:
			request = Request(url, headers=headers)
			with urlopen(request, timeout=30) as response, target.open("wb") as handle:
				handle.write(response.read())
			if target.exists() and target.stat().st_size > 0:
				return f"/files/{filename}"
		except Exception as exc:
			last_error = exc
	if last_error:
		raise last_error
	frappe.throw(f"Could not download {filename}")


def resolve_hero() -> str:
	for filename in HERO_FILES:
		path = SITE_FILES / filename
		if path.exists() and path.stat().st_size > 0:
			return f"/files/{filename}"
	return download_file(HERO_FILES[0], HERO_URLS)


def fill_kezojet_kt10():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = resolve_hero()
	story = copy_public_image("industry-packaging.jpg")

	doc.display_name = "Kezojet KT10"
	doc.website_product_name = "Kezojet KT10"
	doc.slug = SLUG
	doc.brand = "Kezojet"
	doc.brand_name = "Kezojet"
	doc.category = "Coding & Marking"
	doc.subcategory = "Thermal Inkjet"
	doc.category_label = "THERMAL INKJET PRINTER"
	doc.tagline = "10.1-inch touchscreen TIJ with a 1-inch twin head"
	doc.short_description = (
		"Industrial thermal inkjet coder with a 10.1-inch colour touchscreen and a "
		"one-inch twin printhead — supplied with mounting, anti-shock and a cable "
		"cut to the line."
	)
	doc.long_description = (
		"<p>The Kezojet KT10 is a thermal inkjet (TIJ) coding station for date, "
		"batch, barcode and logo marking on packaging lines. This configuration "
		"pairs a 10.1-inch colour capacitive touchscreen with a one-inch twin "
		"printhead, so operators set messages on a large display while the heads "
		"cover a 25.4 mm print band for multi-line codes and graphics.</p>"
		"<p>TIJ uses a sealed cartridge. There is no makeup fluid and no long ink "
		"circuit. The KT series is built for food, beverage, pharmaceutical, "
		"cosmetics, medical devices and general packaging — paper, carton, film "
		"and many plastics — with plug-and-play mounting on conveyors and "
		"cartoners.</p>"
		"<p>The controller runs embedded Linux, supports about 20 operator "
		"languages, and can drive up to ten nozzles. IND.SYS.KZT.4982 ships as "
		"the twin-head package with complete mounting accessories, anti-shock and "
		"a cable length specified for the line. Printechs supplies, installs and "
		"supports Kezojet / UKCM TIJ systems across Saudi Arabia, including "
		"cartridges and service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "Kezojet KT10 10.1-inch thermal inkjet printer with twin head"
	doc.hero_trust_chips = "10.1-inch touchscreen\n1-inch twin head\nAnti-shock included"
	doc.story_heading = "Large controller. Twin-head print band."
	doc.visual_story_heading = "See the KT10"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.page_mode = "Full"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.card_title = "KT10"
	doc.card_brand_label = "Kezojet"
	doc.card_summary = (
		"10.1-inch TIJ controller with a one-inch twin head, mounting and anti-shock."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Specify KT10 for your packaging line"
	doc.final_cta_description = (
		"Printechs will confirm head count, ink type, mounting and cable length "
		"for Kezojet KT10 in Saudi Arabia."
	)
	doc.meta_title = "Kezojet KT10 Thermal Inkjet Printer | Printechs"
	doc.meta_description = (
		"Kezojet KT10 thermal inkjet coder for packaging lines in Saudi Arabia. "
		"10.1-inch touchscreen, 1-inch twin head, date, batch and barcode printing. "
		"Mounting and anti-shock included."
	)
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "display",
				"title": "10-inch colour touchscreen",
				"description": "Capacitive 10.1-inch controller with a clear operator interface and about 20 languages.",
				"sort_order": 1,
			},
			{
				"icon": "print",
				"title": "One-inch twin head",
				"description": "Dual TIJ heads for a 25.4 mm print band — dates, barcodes, QR codes and logos in one pass.",
				"sort_order": 2,
			},
			{
				"icon": "speed",
				"title": "Line-speed coding",
				"description": "High-resolution thermal inkjet for date, batch and variable data on moving packaging.",
				"sort_order": 3,
			},
			{
				"icon": "install",
				"title": "Ready to mount",
				"description": "This SKU includes mounting accessories, anti-shock and a cable length cut for the line.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Controller",
				"image": hero,
				"image_alt": "Kezojet KT10 10-inch TIJ controller",
				"caption": "10.1-inch colour touchscreen for message setup, print status and ink monitoring.",
				"sort_order": 1,
			},
			{
				"label": "Station",
				"image": story,
				"image_alt": "Kezojet KT10 thermal inkjet coding station",
				"caption": "Twin-head TIJ station for cartons, film and packaged goods on the conveyor.",
				"sort_order": 2,
			},
			{
				"label": "Line fit",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage packaging line",
				"caption": "Mount on cartoners, flow wrappers and case tapers with anti-shock hardware.",
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "print",
				"title": "Print technology",
				"description": "Thermal inkjet · HP / Funai cartridges",
				"sort_order": 1,
			},
			{
				"icon": "lines",
				"title": "Print height",
				"description": "25.4 mm (1 inch) twin-head band",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "Controller",
				"description": "10.1-inch colour capacitive touchscreen",
				"sort_order": 3,
			},
			{
				"icon": "speed",
				"title": "Line speed",
				"description": "Up to 120 m/min at 300 dpi",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "Connectivity",
				"description": "Ethernet · USB · wireless options",
				"sort_order": 5,
			},
			{
				"icon": "rugged",
				"title": "This SKU",
				"description": "Mounting + anti-shock + tailored cable",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"This configuration",
			[
				("Model", "Kezojet KT10 (UKCM KT series / UK 10)"),
				("Item code", NAME),
				("Controller", "10.1-inch colour capacitive touchscreen"),
				("Printheads", "One-inch twin head (25.4 mm print band)"),
				("Included", "Mounting accessories, anti-shock, tailored cable length"),
			],
		),
		(
			"Printing performance",
			[
				("Technology", "Thermal inkjet (TIJ)"),
				("Cartridge family", "HP45 / HP45si / Funai"),
				("Resolution", "300 dpi typical · up to 600 dpi depending on cartridge"),
				("Print height", "25.4 mm with twin 12.7 mm heads"),
				("Print speed", "Up to 120 m/min at 300 dpi"),
				("Variable data", "Text, logos, barcodes, QR, serial, date, batch, expiry"),
				("Substrates", "Paper, carton, film, many plastics and coated packs"),
			],
		),
		(
			"Controller & software",
			[
				("Display", "10.1-inch colour capacitive touchscreen"),
				("Operating system", "Embedded Linux"),
				("Languages", "About 20 operator languages"),
				("Head capacity", "Up to 10 nozzles on the controller; this SKU is twin-head"),
				("Ink handling", "Cartridge recognition and ink-level monitoring"),
				("Integration", "Line I/O and software/MES connection options"),
			],
		),
		(
			"Installation",
			[
				("Mounting", "Complete mounting kit included"),
				("Anti-shock", "Included on this SKU"),
				("Cable", "Length specified for the line"),
				("Typical lines", "Conveyors, cartoners, flow wrappers, case sealers"),
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
				"description": "Expiry, lot and batch codes on cartons, film and secondary packs.",
				"image": copy_public_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage packaging line",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Pharmaceutical",
				"description": "Batch and 2D codes on cartons and healthcare packs.",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical packaging line",
				"industry_link": "pharmaceutical",
				"sort_order": 2,
			},
			{
				"title": "Packaging",
				"description": "High-resolution text, logos and barcodes on cases and flexible film.",
				"image": copy_public_image("industry-packaging.jpg"),
				"image_alt": "Packaging line coding",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Cosmetics",
				"description": "Lot and date marking on cartons, tubes and labelled packs.",
				"image": copy_public_image("industry-plastic.jpg"),
				"image_alt": "Cosmetic and plastic pack coding",
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
				"description": "Mounting, photocell setup, cable routing and line commissioning.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Cartridges",
				"description": "HP / Funai ink matched to carton, film or plastic.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Spares & service",
				"description": "Heads, cables, anti-shock parts and on-site support in KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Touchscreen messages, cartridge change and daily checks.",
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
			{"item_description": "KT10 controller with 10.1-inch colour touchscreen", "sort_order": 1},
			{"item_description": "One-inch twin TIJ printhead", "sort_order": 2},
			{"item_description": "Complete mounting accessories", "sort_order": 3},
			{"item_description": "Anti-shock system", "sort_order": 4},
			{"item_description": "Cable length specified for the line", "sort_order": 5},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set(
		"related_products",
		[
			{
				"related_website_product": "IND.SPA.ANS.4742",
				"display_name_override": "Anser SPH Smart Printhead",
				"summary_override": "Compact TIJ printhead when the line needs a smaller stand-alone station.",
				"href": "/products/anser-sph-smart-printhead",
				"sort_order": 1,
			}
		]
		if frappe.db.exists("Website Product", "IND.SPA.ANS.4742")
		else [],
	)
	doc.set("quote_options", [])

	doc.set(
		"content_sections",
		[
			{
				"heading": "KT series controller, twin-head print band",
				"body": (
					"UKCM lists the KT series as UK MINI, UK 7 and UK 10. This SKU is the "
					"KT10 / UK 10 class: a large 10.1-inch operator screen and a one-inch "
					"twin head for wider codes. Ask Printechs if the line later needs "
					"more heads on the same controller."
				),
				"image": story,
				"image_alt": "Kezojet KT10 TIJ station",
				"link_label": "Talk to a specialist",
				"link_href": "/contact",
				"sort_order": 1,
			},
			{
				"heading": "When plants choose TIJ for packaging",
				"body": (
					"Thermal inkjet is a sealed cartridge system. For many carton and "
					"film jobs it avoids CIJ makeup fluid and daily flush. The KT10 is "
					"aimed at date, batch, barcode and logo work on food, beverage, "
					"pharma and cosmetics packaging — with a screen large enough for "
					"shift operators."
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
				"question": "What is included with IND.SYS.KZT.4982?",
				"answer": (
					"This item is the Kezojet KT10 with a 10.1-inch screen, a one-inch twin "
					"printhead, complete mounting accessories, anti-shock, and a cable "
					"length specified for the line."
				),
				"sort_order": 1,
			},
			{
				"question": "Is KT10 the same as UKCM UK 10?",
				"answer": (
					"Yes. KT10 is the Kezojet / UKCM KT-series controller with the 10.1-inch "
					"touchscreen (listed by the supplier as UK 10). Printechs quotes the "
					"exact SKU you need for the line."
				),
				"sort_order": 2,
			},
			{
				"question": "What can it print?",
				"answer": (
					"Text, logos, 1D/2D barcodes, QR codes, serial numbers, dates, batch "
					"and expiry — on paper, carton, film and many plastics, depending on "
					"the cartridge."
				),
				"sort_order": 3,
			},
			{
				"question": "Do you supply ink and installation in Saudi Arabia?",
				"answer": (
					"Yes. Printechs supplies the printer, HP/Funai cartridges, mounting "
					"and commissioning, and after-sales service in KSA."
				),
				"sort_order": 4,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()

	item = frappe.get_doc("Item", NAME)
	if item.image != hero:
		item.db_set("image", hero, update_modified=False)

	frappe.db.commit()
	print(f"Filled and published {doc.name} → /products/{doc.slug}")
	return doc.name
