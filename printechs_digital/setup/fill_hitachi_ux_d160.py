# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product hitachi-ux-d160 (Hitachi UX-D160W).

Official sources (UX Series Standard — not UX2):
https://www.hitachi.asia/ice/en/coding-and-marking/ux.html
https://www.hitachi-ies.com/products/ijp/ux/size01.htm
https://hitachi-industrial.eu/products/continuous-inkjet-printer/ux-series/
https://hitachi-industrial.eu/blog/2025/06/25/fast-flexible-reliable-how-keeplastics-future-proofed-its-packaging-line-with-hitachi-ux-inkjet-printers/
Datasheet: UX-D Standard (UX-D160W 65 μm).

Do not reuse UX2 photos or YouTube IDs already on hitachi-ux2-d160 / hitachi-ux2-d150.
Do not mix UX2-D160W or UX-D161W extras onto this SKU.
"""

from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SLUG = "hitachi-ux-d160"
ITEM = "IND.SYS.HIJ.1995"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")

OFFICIAL_IMAGES = {
	"hitachi-ux-d160-main.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/UX_main-web-1.webp",
	"hitachi-ux-d160-model.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/UX_D-web.webp",
	"hitachi-ux-d160-cabinet.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/UX-gespiegelt.webp",
	"hitachi-ux-d160-beer.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Beer_can_print_sample-1.webp",
	"hitachi-ux-d160-carton.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Cardboard-Box-72dpi.webp",
	"hitachi-ux-d160-tealight.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Teelichter-1.webp",
	"hitachi-ux-d160-beverage.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Beverage_Industry_Hoover.webp",
	"hitachi-ux-d160-auto.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Automotive_Industry_Hoover.webp",
	"hitachi-ux-d160-keep-1.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/06/KeeplasticsPicture1.webp",
	"hitachi-ux-d160-keep-4.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/06/KeeplasticsPicture4.webp",
	"hitachi-ux-d160-keep-5.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/06/KeeplasticsPicture5.webp",
	"hitachi-ux-d160-keep-line.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/06/Keeplasticsslideshow-1200x460-2.webp",
}


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"})
		with urlopen(request, timeout=40) as response, target.open("wb") as handle:
			handle.write(response.read())
	return f"/files/{filename}"


def official_image(filename: str) -> str:
	target = SITE_FILES / filename
	if target.exists():
		return f"/files/{filename}"
	return download_file(filename, OFFICIAL_IMAGES[filename])


def catalog_card(source_name: str, dest_name: str) -> str:
	official_image(source_name)
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGBA")
	scale = 900 / max(im.size)
	new = im.resize((int(im.width * scale), int(im.height * scale)), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


def related_product_row(name: str, sort_order: int) -> dict | None:
	if not name or not frappe.db.exists("Website Product", name):
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


def related_by_slug(slug: str, sort_order: int) -> dict | None:
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	return related_product_row(name, sort_order) if name else None


def get_or_create():
	existing = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = SLUG
	if frappe.db.exists("Item", ITEM):
		other = frappe.db.get_value("Website Product", {"item": ITEM}, "name")
		if not other:
			doc.item = ITEM
	doc.website_product_name = "Hitachi UX-D160W"
	doc.display_name = "Hitachi UX-D160W"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.short_description = "Hitachi UX-D160W continuous inkjet printer."
	doc.long_description = "<p>Hitachi UX-D160W continuous inkjet printer.</p>"
	doc.hero_image = official_image("hitachi-ux-d160-model.webp")
	return doc


def set_specs(doc, groups):
	rows = []
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			if len(value) > 140:
				frappe.throw(f"Spec value too long ({len(value)}): {label}")
			rows.append(
				{
					"group_title": group_title,
					"label": label,
					"value": value,
					"sort_order": sort,
				}
			)
			sort += 1
	doc.set("full_specifications", rows)


def fill_hitachi_ux_d160():
	doc = get_or_create()
	hero = catalog_card("hitachi-ux-d160-model.webp", "hitachi-ux-d160-product.jpg")
	main = official_image("hitachi-ux-d160-main.webp")
	cabinet = official_image("hitachi-ux-d160-cabinet.webp")
	beer = official_image("hitachi-ux-d160-beer.webp")
	carton = official_image("hitachi-ux-d160-carton.webp")
	tealight = official_image("hitachi-ux-d160-tealight.webp")
	beverage = official_image("hitachi-ux-d160-beverage.webp")
	auto = official_image("hitachi-ux-d160-auto.webp")
	keep1 = official_image("hitachi-ux-d160-keep-1.webp")
	keep4 = official_image("hitachi-ux-d160-keep-4.webp")
	keep5 = official_image("hitachi-ux-d160-keep-5.webp")
	keepline = official_image("hitachi-ux-d160-keep-line.webp")

	doc.website_product_name = "Hitachi UX-D160W"
	doc.display_name = "Hitachi UX-D160W"
	doc.slug = SLUG
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.subcategory = "Continuous Inkjet"
	doc.category_label = "CONTINUOUS INKJET PRINTER"
	if frappe.db.exists("Brand", "Hitachi"):
		doc.brand = "Hitachi"
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.featured = 0
	doc.index_page = 1
	doc.published = 1
	doc.card_brand_label = "Hitachi"
	doc.card_title = "UX-D160W"
	doc.video_url = ""
	doc.hero_image = hero
	doc.card_image = hero
	doc.hero_image_alt = "Hitachi UX-D160W Standard continuous inkjet printer"
	doc.tagline = "UX Series Standard — 65 μm, six-line CIJ with clean cartridge fluids"
	doc.short_description = (
		"Hitachi UX-D160W is the UX Series Standard continuous inkjet: 65 μm nozzle, up to "
		"6 print lines, 1,148 characters/s (option 2,563), IP65 stainless cabinet and 10.4\" "
		"touch screen. Dates, lots, barcodes and Data Matrix on food, beverage and packaging lines."
	)
	doc.long_description = (
		"<p>UX-D160W is Hitachi’s UX Series Standard CIJ — the well-equipped 65 μm model "
		"for Saudi production lines that need up to six lines of code from one printhead. "
		"It is not the Basic UX-B160W (3 lines, IP55), not the Premium UX-E160W, and not "
		"the later UX2-D160W Dynamic cabinet.</p>"
		"<p>Hitachi rates UX-D160W at up to 240 print characters on 6 lines (option 1,000), "
		"1,148 characters per second on a 5×5 font (option 2,563), and 300 stored messages "
		"(option 2,000). Character height is 2–10 mm. Ethernet (IEEE 802.3, 100BASE-T) is "
		"standard. The 10.4\" colour TFT is a WYSIWYG touch panel with icon graphics.</p>"
		"<p>Cartridge-type ink and makeup bottles change without splashes; empty cartridges "
		"drain so no liquid remains. Hitachi’s makeup-consumption reduction system cuts "
		"volatilisation to about 30% versus earlier UX designs. RFID on the cartridge can "
		"block the wrong fluid once country radio approval is in place.</p>"
		"<p>The stainless cabinet is IP65, 400 × 320 × 527 mm, about 27 kg. Printhead cable "
		"is 4 m, in-line or 90°. Ambient range with 1067K ink is 0–50 °C. Power is "
		"100–120 / 220–240 VAC ±10%, 50/60 Hz, 120 VA.</p>"
		"<p>Printechs specifies, installs and services UX-D160W in Riyadh, Jeddah and "
		"Dammam with genuine Hitachi ink and encoder integration. ERP Item IND.SYS.HIJ.1995 "
		"can sit on this page; spare-part Items stay off it.</p>"
	)
	doc.hero_trust_chips = (
		"65 μm · up to 6 lines\n"
		"1,148 cps · option 2,563\n"
		"IP65 · 10.4\" touch HMI\n"
		"Clean cartridge fluids"
	)
	doc.story_heading = "Standard UX CIJ for dates, lots, barcodes and Data Matrix"
	doc.visual_story_heading = "Official UX Series print samples and UX-D160W line shots"
	doc.card_summary = (
		"UX Series Standard CIJ: 65 μm nozzle, up to 6 lines, IP65 cabinet and clean "
		"cartridge ink for food, beverage and packaging."
	)
	doc.final_cta_heading = "Specify UX-D160W for your coding line"
	doc.final_cta_description = (
		"Printechs can confirm nozzle, 4 m head, ink and whether UX-D160W or UX2-D160W "
		"is the right cabinet for sites in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Hitachi UX-D160W Continuous Inkjet Saudi Arabia | Printechs"
	doc.meta_description = (
		"Hitachi UX-D160W Standard CIJ: 65 μm, up to 6 lines, 1,148 cps and IP65 cabinet. "
		"Supplied and supported by Printechs in KSA."
	)
	doc.canonical_path = f"/products/{SLUG}"

	doc.set(
		"benefits",
		[
			{
				"icon": "lines",
				"title": "Up to 6 lines, 65 μm",
				"description": (
					"Standard UX-D nozzle for logos, best-before, lots, barcodes and Data "
					"Matrix. Character height 2–10 mm from a single printhead."
				),
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "1,148 characters per second",
				"description": (
					"Hitachi rates 1,148 cps on a 5×5 font, one line; optional high-speed "
					"print to 2,563 cps. Not the UX2-D150 3,173 cps jet."
				),
				"sort_order": 2,
			},
			{
				"icon": "consumables",
				"title": "Clean cartridge fluids",
				"description": (
					"Ink and makeup cartridges change without splash. Makeup volatilisation "
					"is reduced to about 30% on UX-D versus earlier designs."
				),
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Ethernet as standard",
				"description": (
					"IEEE 802.3 100BASE-T on the Standard model, USB for message storage, "
					"and a 10.4\" WYSIWYG touch panel for line operators."
				),
				"sort_order": 4,
			},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{
				"label": "UX-D Standard cabinet",
				"image": main,
				"image_alt": "Official Hitachi UX Series Standard continuous inkjet printer",
				"caption": "Official EU UX Series cabinet — the Standard UX-D platform used by UX-D160W.",
				"sort_order": 1,
			},
			{
				"label": "UX-D model view",
				"image": official_image("hitachi-ux-d160-model.webp"),
				"image_alt": "Official Hitachi UX-D continuous inkjet printer",
				"caption": "UX-D Standard: 65 μm, six-line printing, IP65 stainless console.",
				"sort_order": 2,
			},
			{
				"label": "Printhead and console",
				"image": cabinet,
				"image_alt": "Hitachi UX Series cabinet and printhead",
				"caption": "4 m umbilical, in-line or 90° head. Cabinet 400 × 320 × 527 mm, about 27 kg.",
				"sort_order": 3,
			},
			{
				"label": "Beer-can print sample",
				"image": beer,
				"image_alt": "Official Hitachi UX Series print sample on a beverage can",
				"caption": "Official EU UX print sample: date and lot on a beverage can.",
				"sort_order": 4,
			},
			{
				"label": "Carton print sample",
				"image": carton,
				"image_alt": "Official Hitachi UX Series print sample on a cardboard box",
				"caption": "Official EU UX print sample: codes on secondary carton packaging.",
				"sort_order": 5,
			},
			{
				"label": "Keeplastics UX-D160W line",
				"image": keepline,
				"image_alt": "Keeplastics packaging line using Hitachi UX-D160W",
				"caption": "Official Hitachi case: Keeplastics coded four SKUs on one line with UX-D160W.",
				"sort_order": 6,
			},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "scan", "title": "65 μm nozzle", "description": "Up to 6 lines · 2–10 mm height", "sort_order": 1},
			{"icon": "speed", "title": "1,148 cps", "description": "Optional 2,563 characters/s", "sort_order": 2},
			{"icon": "display", "title": "10.4\" TFT", "description": "WYSIWYG colour touch panel", "sort_order": 3},
			{"icon": "rugged", "title": "IP65 console", "description": "Stainless cabinet · 27 kg", "sort_order": 4},
			{"icon": "connectivity", "title": "Ethernet", "description": "IEEE 802.3 · 100BASE-T", "sort_order": 5},
			{"icon": "consumables", "title": "Cartridges", "description": "Ink + makeup, ~30% less makeup", "sort_order": 6},
		],
	)
	set_specs(
		doc,
		[
			(
				"Printing performance",
				[
					("Model", "UX-D160W (UX Series Standard)"),
					("Nozzle size", "65 μm"),
					("Print lines", "Up to 6 lines"),
					("Print characters", "Up to 240 (option 1,000)"),
					("Print rate", "1,148 cps; option 2,563 (5×5, space 1, 1 line)"),
					("Character height", "2–10 mm"),
					("Message storage", "300 messages (option 2,000)"),
					("Fonts", "4×5 through 36×48 including 24×32, 30×40, 36×48"),
					("Barcodes", "Code 39, ITF, NW-7, EAN-13/8, UPC-A/E, Code 128 / EAN-128, GS1 DataBar"),
					("2D codes", "Data Matrix, QR Code, Micro QR"),
				],
			),
			(
				"Operator interface",
				[
					("Display", "10.4\" colour TFT LCD, backlight, WYSIWYG"),
					("Input", "Touch panel with input sound"),
					("Languages", "English, Arabic and 25+ operator languages"),
				],
			),
			(
				"Ink system",
				[
					("Ink / makeup", "Cartridge-type bottles, splash-free change"),
					("Makeup use", "Reduced to about 30% vs earlier UX designs"),
					("RFID cartridge", "Optional; requires country radio approval"),
					("Ink example", "1067K rated 0–50 °C ambient"),
				],
			),
			(
				"Connectivity",
				[
					("Ethernet", "IEEE 802.3, 100BASE-T (standard on UX-D)"),
					("USB", "External memory for user data"),
					("I/O", "Print ready, fault, warning, print complete, online"),
				],
			),
			(
				"Cabinet and environment",
				[
					("Protection", "IP65"),
					("Dimensions", "400 × 320 × 527 mm (W × D × H)"),
					("Weight", "Approximately 27 kg"),
					("Head cable", "4 m, in-line or 90°"),
					("Temperature", "0–50 °C (1067K ink)"),
					("Humidity", "30–90% RH, no condensation"),
					("Power", "AC 100–120 / 220–240 V ±10%, 50/60 Hz, 120 VA"),
					("Approvals", "CE, UL, cUL, C-Tick, FCC, ICES"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{
				"title": "Beverage cans and bottles",
				"description": "Best-before, lot and plant codes on cans and PET at line speed.",
				"image": beer,
				"image_alt": "Official Hitachi UX Series beverage-can print sample",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Food packaging halls",
				"description": "Export codes and date changes without stopping the carton line.",
				"image": carton,
				"image_alt": "Official Hitachi UX Series carton print sample",
				"industry_link": "packaging",
				"sort_order": 2,
			},
			{
				"title": "Beverage filling",
				"description": "UX Series beverage coding for wet halls — IP65 stainless console.",
				"image": beverage,
				"image_alt": "Official Hitachi UX Series beverage industry coding scene",
				"industry_link": "food-beverage",
				"sort_order": 3,
			},
			{
				"title": "Automotive and industrial parts",
				"description": "Lot and traceability marks on components and dark parts (pigment ink on request).",
				"image": auto,
				"image_alt": "Official Hitachi UX Series automotive industry coding scene",
				"industry_link": "plastic",
				"sort_order": 4,
			},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Core Module",
				"heading": "UX Series Standard — not UX2",
				"body": (
					"UX-D160W is the current-generation name Hitachi Asia and Hitachi IES "
					"use for the UX Series Standard 65 μm printer. Europe’s brochure often "
					"lists the same platform as UX-D161W. This page is the D160W SKU "
					"(ERP IND.SYS.HIJ.1995), not UX2-D160W and not UX-D151W (55 μm)."
				),
				"image": main,
				"image_alt": "Official Hitachi UX Series Standard continuous inkjet printer",
				"sort_order": 1,
			},
			{
				"section_type": "Core Module",
				"heading": "Clean & Easy cartridge fluids",
				"body": (
					"Ink and makeup sit in cartridge bottles. Operators change them without "
					"splashes or leftover liquid in the empty pack. Hitachi’s makeup-reduction "
					"system cuts volatilisation to about 30% on UX-D versus earlier UX printers."
				),
				"image": official_image("hitachi-ux-d160-model.webp"),
				"image_alt": "Hitachi UX-D Standard printer with cartridge fluid system",
				"sort_order": 2,
			},
			{
				"section_type": "Core Module",
				"heading": "Six-line print from one 65 μm head",
				"body": (
					"Up to 240 characters across six lines (option 1,000). Fonts run from "
					"4×5 to 36×48. Barcodes include EAN, UPC, Code 128 and GS1 DataBar; "
					"2D includes Data Matrix, QR and Micro QR."
				),
				"image": tealight,
				"image_alt": "Official Hitachi UX Series small-character print sample",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Keeplastics: four products, one UX-D160W line",
				"body": (
					"Hitachi’s official Keeplastics case (Norrköping, Sweden) used UX-D160W "
					"to code four SKUs on one food-packaging line for 80+ export countries. "
					"Operators change label data without stopping the belt. RFID-secured "
					"cartridges stop the wrong ink going on the line."
				),
				"image": keep1,
				"image_alt": "Keeplastics production using Hitachi UX-D160W continuous inkjet",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Instant code changes on a live carton line",
				"body": (
					"The same official case shows UX-D160W sitting on the carton conveyor. "
					"Message storage is 300 as standard (option 2,000) so export variants "
					"stay in the printer instead of a stack of saved files on a USB stick."
				),
				"image": keep4,
				"image_alt": "Hitachi UX-D160W coding cartons on the Keeplastics line",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Food-safe hall, IP65 cabinet",
				"body": (
					"Keeplastics run UX-D160W in a food environment. The Standard cabinet "
					"is IP65 stainless — wash-down rated — 400 × 320 × 527 mm and about 27 kg. "
					"Ambient with 1067K ink is 0–50 °C."
				),
				"image": keep5,
				"image_alt": "Hitachi UX-D160W installed in a food packaging hall",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Beverage cans and wet filling",
				"body": (
					"Official EU UX Series beverage-can sample and beverage-hall still. "
					"UX-D160W’s 65 μm jet and 2–10 mm height cover date + lot + plant on "
					"cans and PET without stepping up to UX2."
				),
				"image": beer,
				"image_alt": "Official Hitachi UX Series print sample on a beer can",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Cartons, export codes and Saudi support",
				"body": (
					"Secondary cartons take the same six-line message as the primary pack. "
					"Need Ink Guard and optional Safe-Clean-Station? That is UX2-D160W, "
					"a different page.\n\n"
					"Printechs installs UX-D160W in Riyadh, Jeddah and Dammam with genuine "
					"ink, encoders and operator training."
				),
				"image": carton,
				"image_alt": "Official Hitachi UX Series print sample on a cardboard box",
				"link_label": "Open UX2-D160W",
				"link_href": "/products/hitachi-ux2-d160",
				"sort_order": 8,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{
				"icon": "scan",
				"title": "D160W vs UX2 / D161W",
				"description": "We size UX-D160W against UX2-D160W and UX-D161W from pack, lines and hall.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Head and encoder",
				"description": "4 m umbilical, 0° or 90° head, photocell and encoder set-up on your line.",
				"sort_order": 2,
			},
			{
				"icon": "consumables",
				"title": "Ink and makeup",
				"description": "Cartridge fluids matched to substrate, wash and 0–50 °C halls.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Install, training and genuine parts in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "UX-D160W printer cabinet and 65 μm printhead (4 m standard)", "sort_order": 1},
			{"item_description": "Cartridge ink and makeup system (fluids ordered to substrate)", "sort_order": 2},
			{"item_description": "10.4\" touch panel and Ethernet interface", "sort_order": 3},
			{"item_description": "Optional 90° head and message-memory upgrade (2,000)", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set(
		"faq_items",
		[
			{
				"question": "What is the Hitachi UX-D160W?",
				"answer": "The UX Series Standard CIJ: 65 μm nozzle, up to 6 print lines, 1,148 cps (option 2,563), IP65 cabinet and 10.4\" touch screen. It is not UX2-D160W.",
				"sort_order": 1,
			},
			{
				"question": "How is it different from UX2-D160W?",
				"answer": "UX-D160W is the previous UX Series Standard cabinet (10.4\" HMI, cartridge fluids). UX2-D160W is the later Dynamic cabinet with Ink Guard, 10.1\" HMI and optional Safe-Clean-Station.",
				"sort_order": 2,
			},
			{
				"question": "Is this the same as UX-D161W?",
				"answer": "Same UX-D Standard family. Asia and Hitachi IES list UX-D160W; Europe’s brochure often shows UX-D161W. This page is the D160W Item IND.SYS.HIJ.1995.",
				"sort_order": 3,
			},
			{
				"question": "What nozzle and speed does it have?",
				"answer": "65 μm, up to 6 lines, 1,148 characters/s standard and 2,563 optional. Character height 2–10 mm. UX-D151W is the 55 μm / 4-line sibling.",
				"sort_order": 4,
			},
			{
				"question": "Which ERP Item is this?",
				"answer": "IND.SYS.HIJ.1995 — Hitachi Ink Jet Printer, UX-D160W. Spare-part Items are not linked here.",
				"sort_order": 5,
			},
		],
	)
	related = [
		row
		for row in (
			related_by_slug("hitachi-ux2-d160", 1),
			related_by_slug("hitachi-ux-d161", 2),
			related_by_slug("hitachi-ux-d151", 3),
		)
		if row
	]
	doc.set("related_products", related)

	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	frappe.db.commit()
	return doc.name


def move_datalogic_warehouse_to_retail():
	"""Move the warehouse AutoID family onto the Retail catalogue."""
	slugs = (
		"datalogic-matrix-320",
		"datalogic-codiscan",
		"datalogic-falcon-x60-x65",
		"datalogic-skorpio-x40-x45",
		"datalogic-powerscan-9600",
	)
	updated = []
	for slug in slugs:
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		doc.product_type = "Retail Hardware"
		doc.division = "Retail"
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(slug)
	frappe.db.commit()
	return updated
