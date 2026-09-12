# Copyright (c) 2026, Printechs and contributors
"""Create Website Products for Hitachi UX2-D160W and UX2-D150W.

Official sources:
https://hitachi-industrial.eu/products/continuous-inkjet-printer/ux2-series/
https://mc.hitachi-iesa.com/industrial-continuous-inkjet-printer/ux2-dynamic
https://mc.hitachi-iesa.com/industrial-continuous-inkjet-printer/ux-high-speed
https://visy-tech.com/product/hitachi-ux2-safe-clean-station/
Datasheet: Hitachi UX2-D150W (55 μm high-speed), July 2025.
US Dynamic ordering/specs apply to UX2-D160W (65 μm, up to 6 lines).

Do not mix models:
- D160W: 65 μm, up to 6 lines, 1,538 cps (optional 3,076), messages 300 (opt. 2,000)
- D150W: 55 μm, up to 4 lines, 3,173 cps, 2,000 messages
Safe-Clean-Station is optional on both.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")

VIDEO_UX2 = "https://youtu.be/2hVqni_pMMs"
VIDEO_ANIM = "https://youtu.be/KcHESzxBRyE"
VIDEO_HEAD = "https://youtu.be/9NcoKlOHQ2o"
VIDEO_CLEAN = "https://youtu.be/P5zv7qJ_r_k"
VIDEO_STARTUP = "https://youtu.be/8ZTN7LBzEco"
VIDEO_SAFER = "https://youtu.be/bxRy-XdaRWo"
VIDEO_DAIRY = "https://youtu.be/UrlwpJ-P5pQ"
VIDEO_HSPEED = "https://youtu.be/gIQBZ5vzhS4"
VIDEO_NOZZLES = "https://youtu.be/jOOo-R96yUE"

OFFICIAL_IMAGES = {
	"hitachi-ux2-028.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/HITACHI_UX2_028-1.webp",
	"hitachi-ux2-048.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/HITACHI_UX2_048.webp",
	"hitachi-ux2-068.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/HITACHI_UX2_068.webp",
	"hitachi-ux2-085.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/HITACHI_UX2_085.webp",
	"hitachi-ux2-121.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/HITACHI_UX2_121.webp",
	"hitachi-ux2-cabinet.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Hitachi_UX2_016-023webp.webp",
	"hitachi-ux2-print-tea.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Tea_print_sample.webp",
	"hitachi-ux2-print-oil.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Body_oil_print_sample.webp",
	"hitachi-ux2-print-margarine.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Margarine_print_sample.webp",
	"hitachi-ux2-print-tictac.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/TicTac_s_print_sample.webp",
	"hitachi-ux2-industry-dairy.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Dairy_Industry_Hoover.webp",
	"hitachi-ux2-industry-packaging.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Packaging_Hoover.webp",
	"hitachi-ux2-industry-cosmetics.webp": "https://hitachi-industrial.eu/wp-content/uploads/2025/05/Cosmetics-Pharmaceuticals_Hoover.webp",
}


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def cover_square(source: Path, dest_name: str) -> str:
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGB")
	side = min(im.size)
	left = (im.width - side) // 2
	top = (im.height - side) // 2
	im = im.crop((left, top, left + side, top + side)).resize((1200, 1200), Image.Resampling.LANCZOS)
	im.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"})
		with urlopen(request, timeout=30) as response, target.open("wb") as handle:
			handle.write(response.read())
	return f"/files/{filename}"


def official_image(filename: str) -> str:
	target = SITE_FILES / filename
	if target.exists():
		return f"/files/{filename}"
	return download_file(filename, OFFICIAL_IMAGES[filename])


def catalog_card(source_name: str, dest_name: str) -> str:
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	official_image(source_name)
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


def related_by_slug(slug: str, sort_order: int) -> dict | None:
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	return related_product_row(name, sort_order) if name else None


def get_or_create(slug: str, display_name: str, item: str | None):
	existing = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = slug
	if item and frappe.db.exists("Item", item):
		# Only link if no other Website Product already owns this Item.
		other = frappe.db.get_value("Website Product", {"item": item}, "name")
		if not other:
			doc.item = item
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.short_description = f"{display_name} continuous inkjet printer."
	doc.long_description = f"<p>{display_name} continuous inkjet printer.</p>"
	doc.hero_image = official_image("hitachi-ux2-028.webp")
	return doc


def shared_media():
	copy_public_image("industry-food-beverage.jpg")
	copy_public_image("industry-dairy.jpg")
	copy_public_image("industry-pipe.jpg")
	return {
		"hero_d160": catalog_card("hitachi-ux2-028.webp", "hitachi-ux2-product.jpg"),
		"hero_d150": catalog_card("hitachi-ux2-048.webp", "hitachi-ux2-d150-product.jpg"),
		"cab": official_image("hitachi-ux2-cabinet.webp"),
		"img048": official_image("hitachi-ux2-048.webp"),
		"img068": official_image("hitachi-ux2-068.webp"),
		"img085": official_image("hitachi-ux2-085.webp"),
		"img121": official_image("hitachi-ux2-121.webp"),
		"print_tea": official_image("hitachi-ux2-print-tea.webp"),
		"print_oil": official_image("hitachi-ux2-print-oil.webp"),
		"print_margarine": official_image("hitachi-ux2-print-margarine.webp"),
		"print_tictac": official_image("hitachi-ux2-print-tictac.webp"),
		"dairy": official_image("hitachi-ux2-industry-dairy.webp"),
		"packaging": official_image("hitachi-ux2-industry-packaging.webp"),
		"pharma": official_image("hitachi-ux2-industry-cosmetics.webp"),
		"food": official_image("hitachi-ux2-print-tea.webp"),
		"food_line": copy_public_image("industry-food-beverage.jpg"),
		"milk": copy_public_image("industry-dairy.jpg"),
		"pipe": copy_public_image("industry-pipe.jpg"),
	}


def apply_common(doc, media):
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.subcategory = "Continuous Inkjet"
	doc.category_label = "CONTINUOUS INKJET PRINTER"
	if frappe.db.exists("Brand", "Hitachi"):
		doc.brand = "Hitachi"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.featured = 0
	doc.card_brand_label = "Hitachi"
	doc.index_page = 1
	doc.published = 1
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.hero_image = media["hero"]
	doc.card_image = media["hero"]


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


def fill_hitachi_ux2_d160():
	slug = "hitachi-ux2-d160"
	doc = get_or_create(slug, "Hitachi UX2-D160W", "IND.SYS.HIJ.3892")
	media = shared_media()
	media["hero"] = media["hero_d160"]
	apply_common(doc, media)

	doc.website_product_name = "Hitachi UX2-D160W"
	doc.display_name = "Hitachi UX2-D160W"
	doc.slug = slug
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.tagline = "UX2 Dynamic — six-line CIJ with Ink Guard and optional Safe-Clean"
	doc.short_description = (
		"Hitachi UX2-D160W is the UX2 Dynamic continuous inkjet: 65 μm nozzle, up to 6 print "
		"lines, patented Ink Guard (up to 3× longer between cleanings) and optional Safe-Clean-"
		"Station. Dates, lots, barcodes and Data Matrix on food, dairy, pharma and packaging lines."
	)
	doc.long_description = (
		"<p>UX2-D160W is Hitachi’s flagship UX2 Dynamic CIJ for Saudi production lines. "
		"It is the 65 μm, up-to-6-line model — not the high-speed D150 (55 μm / 4 lines) "
		"and not the older UX-D161W generation.</p>"
		"<p>Patented Ink Guard traps mist and splashback so the head can run up to three "
		"times longer between quality faults. Enhanced Dot Control keeps codes readable at "
		"speed. Pulse Recovery reduces makeup evaporation.</p>"
		"<p>The 10.1\" WSVGA touch panel has on-board maintenance videos. Smart Bottle "
		"cartridges gravity-drain so fluid is used, not left in the bottle. Filters change "
		"without tools. Individual parts are replaced only when needed — no forced time-based "
		"shutdown.</p>"
		"<p>Safe-Clean-Station is <strong>optional</strong>: sealed Eco / Standard / Deep "
		"clean, nozzle diagnosis, scheduled recirculation and a docking park. Preconfigured "
		"I/O connectors speed line-to-line moves. 4 m umbilical is standard; 6 m and 90° "
		"heads are options (UX2-D160W-6M, UX2-D160W-L).</p>"
		"<p>Printechs specifies, installs and services UX2-D160W in Riyadh, Jeddah and "
		"Dammam — including ink, Safe-Clean and encoder integration. ERP Item "
		"IND.SYS.HIJ.3892 can sit on this page; E-suffix and 6 m kits remain separate SKUs.</p>"
	)
	doc.hero_image_alt = "Hitachi UX2-D160W Dynamic continuous inkjet printer cabinet and printhead"
	doc.video_url = VIDEO_UX2
	doc.hero_trust_chips = (
		"65 μm · up to 6 lines\n"
		"Ink Guard · 3× longer runs\n"
		"IP65 console · 10.1\" HMI\n"
		"OPC-UA · EtherNet/IP"
	)
	doc.story_heading = "Dynamic CIJ for dates, lots, barcodes and Data Matrix"
	doc.visual_story_heading = "Official UX2 print samples and line shots"
	doc.card_title = "UX2-D160W"
	doc.card_summary = (
		"UX2 Dynamic CIJ: 65 μm nozzle, up to 6 lines, Ink Guard and optional Safe-Clean-"
		"Station for food, dairy, pharma and packaging."
	)
	doc.final_cta_heading = "Specify UX2-D160W for your coding line"
	doc.final_cta_description = (
		"Printechs can confirm 4 m vs 6 m umbilical, 90° head, Safe-Clean-Station, short "
		"head and ink for sites in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.meta_title = "Hitachi UX2-D160W Continuous Inkjet Saudi Arabia | Printechs"
	doc.meta_description = (
		"Hitachi UX2-D160W Dynamic CIJ: 65 μm, up to 6 lines, Ink Guard and optional "
		"Safe-Clean-Station. Supplied and supported by Printechs in KSA."
	)
	doc.canonical_path = f"/products/{slug}"

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "Up to 6 lines, 65 μm",
				"description": (
					"Standard Dynamic nozzle for logos, best-before, lots, barcodes and Data "
					"Matrix. Character height 2–10 mm (short head 2.0–6.5 mm)."
				),
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Ink Guard + Enhanced Dot Control",
				"description": (
					"The redesigned head traps splashback for up to 3× longer clean runs. "
					"Dot algorithms keep codes readable as line speed rises."
				),
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Optional Safe-Clean-Station",
				"description": (
					"Sealed Eco / Standard / Deep clean, self-diagnosis and scheduled "
					"recirculation — not included in the printer carton."
				),
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Line-ready industrial I/O",
				"description": (
					"OPC-UA, Modbus, EtherNet/IP and serial, plus quick-change I/O so the "
					"cabinet can move between lines without rewiring from scratch."
				),
				"sort_order": 4,
			},
		],
	)
	_set_d160_story_and_apps(doc, media)
	doc.set(
		"icon_specifications",
		[
			{"icon": "scan", "title": "65 μm nozzle", "description": "Up to 6 lines · 2–10 mm height", "sort_order": 1},
			{"icon": "speed", "title": "1,538 cps", "description": "Optional 3,076 characters/s", "sort_order": 2},
			{"icon": "display", "title": "10.1\" WSVGA", "description": "On-board maintenance videos", "sort_order": 3},
			{"icon": "rugged", "title": "IP65 console", "description": "Stainless cabinet · 27 kg", "sort_order": 4},
			{"icon": "connectivity", "title": "OPC-UA / EIP", "description": "Modbus · EtherNet/IP · serial", "sort_order": 5},
			{"icon": "maintenance", "title": "Safe-Clean", "description": "Optional sealed head station", "sort_order": 6},
		],
	)
	set_specs(doc, _d160_spec_groups())
	_set_d160_sections(doc, media, slug)
	_set_support_and_faq_d160(doc)
	_set_related(doc, exclude_slug=slug)
	_save(doc)
	return doc.name


def fill_hitachi_ux2_d150():
	slug = "hitachi-ux2-d150"
	doc = get_or_create(slug, "Hitachi UX2-D150W", "IND.SYS.HIJ.4369")
	media = shared_media()
	media["hero"] = media["hero_d150"]
	apply_common(doc, media)

	doc.website_product_name = "Hitachi UX2-D150W"
	doc.display_name = "Hitachi UX2-D150W"
	doc.slug = slug
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.tagline = "UX2 High-Speed — 55 μm nozzle, up to 3,173 characters per second"
	doc.short_description = (
		"Hitachi UX2-D150W is the UX2 high-speed CIJ: 55 μm nozzle, up to 4 print lines "
		"and 3,173 characters/s. Same Ink Guard, Smart Bottle and optional Safe-Clean-Station "
		"as D160 — specified for fast beverage, can and food lines."
	)
	doc.long_description = (
		"<p>UX2-D150W is Hitachi’s high-speed UX2 model (55 μm). It is not the six-line "
		"Dynamic D160W (65 μm) and not the older UX-D150W / UX-D151W generation.</p>"
		"<p>Hitachi rates it at up to 3,173 characters per second and 1–4 lines, with "
		"character height 1.5–10 mm (optional short head 1–6.5 mm). Message storage is "
		"2,000. The same Ink Guard head, Enhanced Dot Control, 10.1\" HMI and Smart Bottle "
		"system as the rest of UX2.</p>"
		"<p>US and EU material position D150 for PET bottles, cans and other fast primary "
		"packs — batch, expiry and lot at beverage and canning speeds. Safe-Clean-Station "
		"is optional (station envelope 197 × 145 × 295 mm, about 3 kg).</p>"
		"<p>Console is IP65 (circulatory area IP55 on the D150 datasheet). Power is "
		"100–120 / 200–240 VAC ±10%, 120 VA. Umbilical 4 m or 6 m, 0° or 90°.</p>"
		"<p>Printechs specifies D150 vs D160 from line speed and line-count, then installs "
		"and services in Riyadh, Jeddah and Dammam. ERP Item IND.SYS.HIJ.4369 can sit on "
		"this page.</p>"
	)
	doc.hero_image_alt = "Hitachi UX2-D150W high-speed continuous inkjet printer cabinet and printhead"
	doc.video_url = ""
	doc.hero_trust_chips = (
		"55 μm · up to 4 lines\n"
		"3,173 characters/s\n"
		"IP65 console · 10.1\" HMI\n"
		"OPC-UA · EtherNet/IP"
	)
	doc.story_heading = "High-speed CIJ for beverage, cans and fast food lines"
	doc.visual_story_heading = "Food, milk and pipe coding at high speed"
	doc.card_title = "UX2-D150W"
	doc.card_summary = (
		"UX2 high-speed CIJ: 55 μm nozzle, up to 4 lines and 3,173 cps, with optional "
		"Safe-Clean-Station for beverage and canning lines."
	)
	doc.final_cta_heading = "Specify UX2-D150W for high-speed coding"
	doc.final_cta_description = (
		"Printechs can confirm 55 μm D150 vs 65 μm D160, short head, Safe-Clean and ink "
		"for fast lines in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.meta_title = "Hitachi UX2-D150W High-Speed CIJ Saudi Arabia | Printechs"
	doc.meta_description = (
		"Hitachi UX2-D150W high-speed CIJ: 55 μm, 4 lines, 3,173 cps and optional "
		"Safe-Clean-Station. From Printechs in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{slug}"

	doc.set(
		"benefits",
		[
			{
				"icon": "speed",
				"title": "3,173 characters per second",
				"description": (
					"55 μm high-speed nozzle for 1–4 line codes on fast PET, can and film "
					"lines — Hitachi’s UX2 high-speed rating, not the D160 optional 3,076 cps."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Four lines, 1.5–10 mm",
				"description": (
					"Enough for expiry + lot + extra line on beverage and can packs. Short "
					"head option: 1–6.5 mm for 1–2 line high-speed work."
				),
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Same UX2 uptime kit",
				"description": (
					"Ink Guard, Smart Bottle, tool-less filters and optional Safe-Clean-"
					"Station — shared UX2 design, 55 μm jet."
				),
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Same industrial Ethernet",
				"description": (
					"OPC-UA, Modbus, EtherNet/IP and serial on the 10.1\" cabinet — match "
					"the PLC the same way as D160."
				),
				"sort_order": 4,
			},
		],
	)
	_set_d150_story_and_apps(doc, media)
	doc.set(
		"icon_specifications",
		[
			{"icon": "scan", "title": "55 μm nozzle", "description": "Up to 4 lines · 1.5–10 mm height", "sort_order": 1},
			{"icon": "speed", "title": "3,173 cps", "description": "High-speed UX2 rating", "sort_order": 2},
			{"icon": "display", "title": "10.1\" WSVGA", "description": "On-board maintenance videos", "sort_order": 3},
			{"icon": "rugged", "title": "IP65 / IP55", "description": "Console IP65 · circulatory IP55", "sort_order": 4},
			{"icon": "connectivity", "title": "OPC-UA / EIP", "description": "Modbus · EtherNet/IP · serial", "sort_order": 5},
			{"icon": "maintenance", "title": "Safe-Clean", "description": "Optional sealed head station", "sort_order": 6},
		],
	)
	set_specs(doc, _d150_spec_groups())
	_set_d150_sections(doc, media, slug)
	_set_support_and_faq_d150(doc)
	_set_related(doc, exclude_slug=slug)
	_save(doc)
	return doc.name


def _set_d160_story_and_apps(doc, media):
	doc.set(
		"visual_story_items",
		[
			{
				"label": "Tea pouch codes",
				"image": media["print_tea"],
				"image_alt": "Official Hitachi UX2 print sample markings on tea packaging",
				"caption": "EU UX2 print sample: best-before, lot and extra lines on a tea pouch.",
				"sort_order": 1,
			},
			{
				"label": "Confectionery pack",
				"image": media["print_tictac"],
				"image_alt": "Official Hitachi UX2 print sample markings on TicTac packaging",
				"caption": "EU UX2 print sample: lot and date codes on confectionery primary pack.",
				"sort_order": 2,
			},
			{
				"label": "Dairy tub codes",
				"image": media["print_margarine"],
				"image_alt": "Official Hitachi UX2 print sample markings on margarine packaging",
				"caption": "EU UX2 print sample: codes on a dairy tub — cold, wet hall work.",
				"sort_order": 3,
			},
			{
				"label": "Cosmetics bottle",
				"image": media["print_oil"],
				"image_alt": "Official Hitachi UX2 print sample marking on body oil packaging",
				"caption": "EU UX2 print sample: lot / date on a cosmetics bottle.",
				"sort_order": 4,
			},
			{
				"label": "UX2 cabinet and 10.1\" HMI",
				"image": media["cab"],
				"image_alt": "Hitachi UX2-D160W stainless CIJ cabinet and touch panel",
				"caption": "Same UX2 console: 460 × 425 × 534 mm, about 27 kg.",
				"sort_order": 5,
			},
			{
				"label": "Printhead and Ink Guard",
				"image": media["img068"],
				"image_alt": "Hitachi UX2 printhead with Ink Guard mist control",
				"caption": "Redesigned head traps splashback for longer clean runs.",
				"sort_order": 6,
			},
			{
				"label": "Safe-Clean-Station (optional)",
				"image": media["img085"],
				"image_alt": "Hitachi UX2 optional Safe-Clean-Station for the printhead",
				"caption": "Sealed Eco / Standard / Deep clean — ordered separately.",
				"sort_order": 7,
			},
		],
	)
	doc.set(
		"applications",
		[
			{
				"title": "Food and beverage primary packs",
				"description": "Best-before, lot and barcode on pouches, bottles and cartons at line speed.",
				"image": media["print_tea"],
				"image_alt": "Official Hitachi UX2 print sample on tea packaging",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Dairy and cold, wet halls",
				"description": "IP65 console for wash-down areas. Optional pressurised head kit for moisture.",
				"image": media["dairy"],
				"image_alt": "Official Hitachi UX2 dairy industry coding scene",
				"industry_link": "dairy",
				"sort_order": 2,
			},
			{
				"title": "Packaging and secondary cases",
				"description": "Lot and shipping IDs on film, foil, board and mixed substrates.",
				"image": media["packaging"],
				"image_alt": "Official Hitachi UX2 packaging industry coding scene",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Pharma and cosmetics packs",
				"description": "Lot, expiry and 2D codes on cartons and bottles. Confirm ink and height per SKU.",
				"image": media["pharma"],
				"image_alt": "Official Hitachi UX2 cosmetics and pharmaceutical coding scene",
				"industry_link": "pharmaceutical",
				"sort_order": 4,
			},
		],
	)


def _set_d150_story_and_apps(doc, media):
	doc.set(
		"visual_story_items",
		[
			{
				"label": "Food packs",
				"image": media["food_line"],
				"image_alt": "Ready-meal trays and juice bottles with date and lot codes on a food line",
				"caption": "High-speed expiry and lot on food trays and beverage bottles — D150’s 55 μm job.",
				"sort_order": 1,
			},
			{
				"label": "Milk bottles",
				"image": media["milk"],
				"image_alt": "Milk bottles on a dairy filling line with manufacture, expiry and lot codes",
				"caption": "Milk and dairy: manufacture, expiry and lot at filling-line speed.",
				"sort_order": 2,
			},
			{
				"label": "Pipe and extrusion",
				"image": media["pipe"],
				"image_alt": "HDPE pipe marked with batch number and size for extrusion coding",
				"caption": "Batch and size on pipe, tube and extrusion — confirm pigment ink for dark PE.",
				"sort_order": 3,
			},
			{
				"label": "Dairy tub sample",
				"image": media["print_margarine"],
				"image_alt": "Official Hitachi UX2 print sample markings on margarine packaging",
				"caption": "Official EU dairy-tub print sample — same UX2 family, high-speed D150 jet.",
				"sort_order": 4,
			},
			{
				"label": "UX2 cabinet (head down)",
				"image": media["img048"],
				"image_alt": "Hitachi UX2-D150W cabinet with printhead parked beside the stainless body",
				"caption": "Different official angle from D160 — same UX2 cabinet, 55 μm high-speed head.",
				"sort_order": 5,
			},
			{
				"label": "Printhead and Ink Guard",
				"image": media["img068"],
				"image_alt": "Hitachi UX2 printhead with Ink Guard mist control",
				"caption": "Ink Guard matters more at D150 line speeds.",
				"sort_order": 6,
			},
			{
				"label": "Safe-Clean-Station (optional)",
				"image": media["img085"],
				"image_alt": "Hitachi UX2 optional Safe-Clean-Station for the printhead",
				"caption": "Sealed Eco / Standard / Deep clean — ordered separately.",
				"sort_order": 7,
			},
		],
	)
	doc.set(
		"applications",
		[
			{
				"title": "Food and beverage lines",
				"description": "Expiry, lot and barcode on trays, PET and cans at up to 3,173 characters/s.",
				"image": media["food_line"],
				"image_alt": "Food trays and juice bottles coded on a high-speed line",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Milk and dairy filling",
				"description": "Manufacture, expiry and lot on milk bottles in cold, wet halls (IP65 console).",
				"image": media["milk"],
				"image_alt": "Milk bottles with inkjet date and lot codes",
				"industry_link": "dairy",
				"sort_order": 2,
			},
			{
				"title": "Pipe, tube and extrusion",
				"description": "Batch, size and shift marks on PE/PP pipe. Confirm pigment or dye ink on the substrate.",
				"image": media["pipe"],
				"image_alt": "Extruded pipe marked with batch and size",
				"industry_link": "pipe",
				"sort_order": 3,
			},
			{
				"title": "Cans and primary packs",
				"description": "1–4 line codes on fast can and film lines — D150’s 55 μm jet, not the six-line D160.",
				"image": media["print_margarine"],
				"image_alt": "Official Hitachi UX2 dairy tub print sample",
				"industry_link": "packaging",
				"sort_order": 4,
			},
		],
	)


def _d160_spec_groups():
	return [
		(
			"Model",
			[
				("Model", "UX2-D160W — UX2 Dynamic (not D150 high-speed, not UX-D161W)"),
				("Nozzle", "65 μm"),
				("Print lines", "Up to 6 (short head option: typically 1–2 lines)"),
				("Character height", "2–10 mm; optional short head 2.0–6.5 mm"),
				("Print rate", "1,538 characters/s; optional 3,076 characters/s"),
				("Message storage", "300 standard; optional 2,000"),
				("Ink base", "Dye and soft pigment (MEK-free options in the Hitachi portfolio)"),
				("Kits", "UX2-D160W; UX2-D160W-6M (6 m); UX2-D160W-L (90° head)"),
			],
		),
		(
			"Head, fluids & options",
			[
				("Ink Guard", "Patented mist/splashback trap — up to 3× longer between cleanings"),
				("Dot control", "Enhanced Dot Control Algorithm vs previous UX generation"),
				("Pulse Recovery", "Pulsating ink recovery to cut makeup evaporation"),
				("Smart Bottle", "RFID gravity-drain cartridges; empty bottle is drained"),
				("Filters", "Tool-less ink filter change"),
				("Safe-Clean-Station", "Optional SF-CLEAN-STATION — Eco / Standard / Deep + diagnosis"),
				("Short head", "Optional SHORT-HEAD-KIT for high-speed 1–2 line work"),
				("Pressurised head", "Optional kit for wet / dusty halls"),
				("Umbilical", "4 m standard; optional 6 m; 0° or 90°"),
			],
		),
		(
			"HMI, I/O & environment",
			[
				("Display", "10.1\" colour TFT, WSVGA 1024 × 600, on-board videos"),
				("Communications", "OPC-UA, Modbus, EtherNet/IP, serial"),
				("Connectors", "Preconfigured quick-change I/O for line moves"),
				("Cabinet", "460 × 425 × 534 mm; stainless hairline; about 27 kg"),
				("Protection", "IP65 (US Dynamic specification)"),
				("Barcode input", "Compatible with a handheld barcode scanner (Hitachi list)"),
			],
		),
	]


def _d150_spec_groups():
	return [
		(
			"Model",
			[
				("Model", "UX2-D150W — UX2 high-speed (not D160 Dynamic, not older UX-D150W)"),
				("Nozzle", "55 μm"),
				("Type", "High-speed printing model, 1 printhead"),
				("Print lines", "Up to 4"),
				("Character height", "1.5–10 mm; optional short head 1–6.5 mm"),
				("Print rate", "3,173 characters/s (Hitachi high-speed rating)"),
				("Message storage", "2,000 messages"),
				("Ink base", "Dye and soft pigment; MEK-free inks in the portfolio"),
			],
		),
		(
			"Head, fluids & options",
			[
				("Ink Guard", "Same UX2 splashback trap — up to 3× longer clean runs"),
				("Dot control", "Enhanced Dot Control Algorithm"),
				("Smart Bottle", "RFID gravity-drain cartridges"),
				("Safe-Clean-Station", "Optional; 197 × 145 × 295 mm; about 3.0 kg"),
				("Short head", "Optional; 40 × 40 × 230 mm vs standard 40 × 40 × 235 mm"),
				("Umbilical", "4 m or 6 m; 0° or 90°"),
			],
		),
		(
			"HMI, power & environment",
			[
				("Display", "10.1\" colour TFT, WSVGA, on-board videos"),
				("Communications", "OPC-UA, Modbus, EtherNet/IP, serial"),
				("Supply", "AC 100–120 / 200–240 V ±10%, 50/60 Hz, 120 VA max"),
				("Cabinet", "460 × 425 × 534 mm; stainless; about 27 kg (body ~24.5 + head ~2.5)"),
				("Protection", "IP65 console; circulatory area IP55 (D150 datasheet)"),
				("Climate", "Ink-dependent; example 0–45 °C / 30–90 % RH (4148K), non-condensing"),
				("Vibration", "Approx. 1.96 m/s² or less; no corrosive gas"),
			],
		),
	]


def _set_d160_sections(doc, media, slug):
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Meet Hitachi UX2",
				"body": (
					"Official UX2 film from Hitachi. UX2-D160W is the Dynamic 65 μm / 6-line "
					"cabinet in that family — Ink Guard, 10.1\" HMI and industrial Ethernet."
				),
				"video_url": VIDEO_UX2,
				"image": media["hero"],
				"image_alt": "Hitachi UX2-D160W Dynamic continuous inkjet printer",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Introducing UX2 (animation)",
				"body": (
					"The US Dynamic product page animation: how UX2 codes dates, lots and "
					"barcodes with Ink Guard, Smart Bottle and optional Safe-Clean-Station. "
					"D160W is the 65 μm Dynamic model in that story."
				),
				"video_url": VIDEO_ANIM,
				"image": media["img048"],
				"image_alt": "Hitachi UX2 Dynamic continuous inkjet printer animation still",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Ink Guard printhead — run cleaner, longer",
				"body": (
					"Hitachi’s UX2 head film: the new geometry catches ink build-up so the "
					"printer can run up to three times longer with fewer quality stops and "
					"electronics faults. That claim is for the UX2 head design — it is on "
					"D160 and D150."
				),
				"video_url": VIDEO_HEAD,
				"image": media["img068"],
				"image_alt": "Hitachi UX2 Ink Guard printhead",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Safer, cleaner, smarter printing",
				"body": (
					"Official Hitachi IESA UX2 film: sealed cleaning, less open solvent and "
					"the same cabinet operators use for on-board maintenance videos."
				),
				"video_url": VIDEO_SAFER,
				"image": media["img085"],
				"image_alt": "Hitachi UX2 Safe-Clean and cabinet",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Optional Safe-Clean-Station",
				"body": (
					"Most CIJ stops are dirty nozzles. Safe-Clean seals the head, runs Eco / "
					"Standard / Deep clean, dries with an internal air pump and captures "
					"solvent in a closed reservoir — no open solvent on the floor.\n\n"
					"Self-diagnosis can reverse solvent on start-up. Schedule recirculation "
					"before a long weekend. Order SF-CLEAN-STATION (ERP IND.SPA.HIJ.3893) "
					"with the printer; it is not in the D160 carton."
				),
				"video_url": VIDEO_CLEAN,
				"image": media["img085"],
				"image_alt": "Hitachi UX2 Safe-Clean-Station",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Ready after downtime",
				"body": (
					"Hitachi’s “Avoid long startup” UX2 film. Ink Guard plus optional "
					"Safe-Clean is how the cabinet is meant to come back after a weekend "
					"or changeover without a long purge."
				),
				"video_url": VIDEO_STARTUP,
				"image": media["img121"],
				"image_alt": "Hitachi UX2 printhead ready after a cleaning cycle",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Official print samples",
				"body": (
					"The EU UX2 Series gallery shows logos, best-before dates, barcodes, "
					"lot numbers and Data Matrix on real packs: tea pouch, confectionery, "
					"dairy tub and cosmetics bottle. Those four official samples are in "
					"the visual story above — this is the tea pouch close-up.\n\n"
					"Printechs can mark your own substrate in Riyadh, Jeddah or Dammam "
					"before you lock ink and head length."
				),
				"image": media["print_tea"],
				"image_alt": "Official Hitachi UX2 print sample on tea packaging",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Confectionery and dairy samples",
				"body": (
					"Same EU print-sample set: lot and date on confectionery primary pack, "
					"and codes on a margarine tub for cold, wet dairy halls. D160’s 65 μm "
					"jet and up to six lines cover logo + expiry + lot on these packs."
				),
				"image": media["print_tictac"],
				"image_alt": "Official Hitachi UX2 print sample on confectionery packaging",
				"sort_order": 8,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Cosmetics bottle sample",
				"body": (
					"Official EU body-oil / cosmetics print sample. Confirm ink and "
					"character height per SKU — D160 height is 2–10 mm (short head 2.0–6.5 mm)."
				),
				"image": media["print_oil"],
				"image_alt": "Official Hitachi UX2 print sample on body oil packaging",
				"sort_order": 9,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Built for dairy halls",
				"body": (
					"Hitachi IESA dairy film: coding that holds up in cold, wet rooms. "
					"UX2-D160W adds an IP65 console and an optional pressurised head kit."
				),
				"video_url": VIDEO_DAIRY,
				"image": media["dairy"],
				"image_alt": "Official Hitachi UX2 dairy industry coding scene",
				"sort_order": 10,
			},
			{
				"section_type": "Industry Solution",
				"heading": "D160 vs D150 and Saudi Arabia support",
				"body": (
					"Choose D160 when you need up to six lines or a 65 μm Dynamic jet. "
					"Choose UX2-D150W for 55 μm and 3,173 cps on 1–4 line high-speed packs.\n\n"
					"Printechs installs UX2 in Riyadh, Jeddah and Dammam with genuine ink, "
					"encoders and training. Older UX-D161W remains a separate page."
				),
				"image": media["print_margarine"],
				"image_alt": "Official Hitachi UX2 print sample on margarine packaging",
				"link_label": "Open UX2-D150W",
				"link_href": "/products/hitachi-ux2-d150",
				"sort_order": 11,
			},
		],
	)


def _set_d150_sections(doc, media, slug):
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "UX2 platform — high-speed 55 μm jet",
				"body": (
					"Same UX2 cabinet and films as D160. UX2-D150W is the high-speed 55 μm "
					"member: up to 4 lines and 3,173 characters/s for beverage and can lines."
				),
				"video_url": VIDEO_UX2,
				"image": media["food_line"],
				"image_alt": "Food and beverage packs coded at high speed with Hitachi UX2-D150W",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Introducing UX2 (animation)",
				"body": (
					"The US Dynamic / UX2 family animation. D150W keeps that cabinet and "
					"changes the jet: 55 μm, 4 lines, 3,173 characters/s."
				),
				"video_url": VIDEO_ANIM,
				"image": media["img048"],
				"image_alt": "Hitachi UX2 continuous inkjet printer animation still",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Ink Guard at speed",
				"body": (
					"High line speed makes splashback worse. Ink Guard plus Enhanced Dot "
					"Control is why Hitachi added the 55 μm UX2 instead of only pushing the "
					"65 μm Dynamic faster."
				),
				"video_url": VIDEO_HEAD,
				"image": media["img121"],
				"image_alt": "Hitachi UX2 printhead coding at line speed",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Precision coding on high-speed lines",
				"body": (
					"Official Hitachi Europe film for high-speed coding. D150 is the UX2 "
					"model specified for fast PET, can and film — 3,173 cps, not the D160 "
					"optional 3,076 cps on a 65 μm jet."
				),
				"video_url": VIDEO_HSPEED,
				"image": media["food_line"],
				"image_alt": "High-speed food and beverage coding with Hitachi UX2-D150W",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Optional Safe-Clean-Station",
				"body": (
					"The D150 datasheet lists the station as optional parts (197 × 145 × "
					"295 mm, ~3 kg). Same sealed Eco / Standard / Deep modes as D160. "
					"Specify it when operators should not handle open solvent."
				),
				"video_url": VIDEO_CLEAN,
				"image": media["img085"],
				"image_alt": "Hitachi UX2 Safe-Clean-Station",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Clean nozzles, shorter restarts",
				"body": (
					"Hitachi Europe “clean nozzles” film plus the US “Avoid long startup” "
					"clip. Optional Safe-Clean plus Ink Guard is how D150 is meant to "
					"return after a stop without a long purge."
				),
				"video_url": VIDEO_NOZZLES,
				"image": media["img085"],
				"image_alt": "Hitachi UX2 printhead cleaning",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Food packs at line speed",
				"body": (
					"D150 is specified for fast food and beverage: ready meals, juice, PET "
					"and cans. Up to 4 lines and 3,173 characters/s — expiry + lot without "
					"slowing the belt."
				),
				"image": media["food_line"],
				"image_alt": "Ready-meal trays and juice bottles with inkjet date and lot codes",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Milk and dairy filling",
				"body": (
					"Milk bottles and dairy tubs in cold, wet halls. Console is IP65 "
					"(circulatory IP55). Optional pressurised head if the room is wet. "
					"Character height 1.5–10 mm (short head 1–6.5 mm)."
				),
				"image": media["milk"],
				"image_alt": "Milk bottles on a filling line with manufacture, expiry and lot codes",
				"sort_order": 8,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Pipe, tube and extrusion",
				"body": (
					"Batch, size and shift on PE/PP pipe and tube. Dark pipe usually needs "
					"a pigment ink from the Hitachi list — confirm before you lock the SKU. "
					"D150’s 55 μm jet is for 1–4 line marks, not a six-line Dynamic message."
				),
				"image": media["pipe"],
				"image_alt": "HDPE pipe coded with batch number and size",
				"sort_order": 9,
			},
			{
				"section_type": "Industry Solution",
				"heading": "When to choose D150 over D160",
				"body": (
					"D150: 55 μm, 4 lines, 3,173 cps, 2,000 messages. D160: 65 μm, 6 lines, "
					"1,538 cps (optional 3,076). Need more than four lines or a wider 65 μm "
					"jet? Open UX2-D160W.\n\n"
					"Printechs sizes nozzle, head length and ink for KSA food, milk, pipe "
					"and beverage plants."
				),
				"image": media["print_margarine"],
				"image_alt": "Official Hitachi UX2 dairy tub print sample",
				"link_label": "Open UX2-D160W",
				"link_href": "/products/hitachi-ux2-d160",
				"sort_order": 10,
			},
		],
	)


def _set_support_and_faq_d160(doc):
	doc.set(
		"support_items",
		[
			{"icon": "scan", "title": "D160 vs D150", "description": "6-line / 65 μm Dynamic, or 4-line / 55 μm high-speed — we size from the pack and belt.", "sort_order": 1},
			{"icon": "install", "title": "Head & station", "description": "4 m or 6 m, 0° or 90°, short head and optional Safe-Clean-Station.", "sort_order": 2},
			{"icon": "consumables", "title": "Ink & makeup", "description": "Dye, soft pigment and MEK-free options matched to substrate and wash.", "sort_order": 3},
			{"icon": "training", "title": "Saudi Arabia support", "description": "Install, encoder, training and genuine parts in Riyadh, Jeddah and Dammam.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "UX2-D160W printer cabinet and 65 μm printhead (4 m standard)", "sort_order": 1},
			{"item_description": "Smart Bottle ink/makeup system (fluids ordered to substrate)", "sort_order": 2},
			{"item_description": "Optional 6 m umbilical, 90° head, short-head kit", "sort_order": 3},
			{"item_description": "Optional Safe-Clean-Station and mount bracket", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set(
		"faq_items",
		[
			{"question": "What is the Hitachi UX2-D160W?", "answer": "The UX2 Dynamic CIJ: 65 μm nozzle, up to 6 print lines, Ink Guard and a 10.1\" HMI. It is the standard six-line UX2, not the high-speed D150.", "sort_order": 1},
			{"question": "How is it different from UX2-D150W?", "answer": "D160 is 65 μm / 6 lines / 1,538 cps (optional 3,076). D150 is 55 μm / 4 lines / 3,173 cps. Same cabinet family, different jet.", "sort_order": 2},
			{"question": "Is Safe-Clean-Station included?", "answer": "No. Hitachi lists it as an option (SF-CLEAN-STATION). ERP spare IND.SPA.HIJ.3893.", "sort_order": 3},
			{"question": "Is this the same as UX-D161W?", "answer": "No. UX-D161W is the previous UX generation on a separate page. UX2-D160W is the current Dynamic UX2.", "sort_order": 4},
			{"question": "Which ERP Item is this?", "answer": "Primary Item IND.SYS.HIJ.3892 (UX2-D160W). UX2-D160W-E and 6 m kits are separate Items — link the one you sell on this page.", "sort_order": 5},
		],
	)


def _set_support_and_faq_d150(doc):
	doc.set(
		"support_items",
		[
			{"icon": "speed", "title": "High-speed sizing", "description": "Confirm 3,173 cps / 4 lines is enough, or step up to D160 for six-line codes.", "sort_order": 1},
			{"icon": "install", "title": "Head & station", "description": "4 m or 6 m, 0°/90°, short head and optional Safe-Clean-Station.", "sort_order": 2},
			{"icon": "consumables", "title": "Ink & makeup", "description": "Dye, soft pigment and MEK-free options for PET, can and film.", "sort_order": 3},
			{"icon": "training", "title": "Saudi Arabia support", "description": "Install, encoder, training and genuine parts in Riyadh, Jeddah and Dammam.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "UX2-D150W printer cabinet and 55 μm printhead", "sort_order": 1},
			{"item_description": "Smart Bottle ink/makeup system (fluids ordered to substrate)", "sort_order": 2},
			{"item_description": "Optional 6 m / 90° umbilical and short-head kit", "sort_order": 3},
			{"item_description": "Optional Safe-Clean-Station (~3 kg)", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set(
		"faq_items",
		[
			{"question": "What is the Hitachi UX2-D150W?", "answer": "The UX2 high-speed CIJ: 55 μm nozzle, up to 4 lines and 3,173 characters/s. It is not the six-line D160 and not the older UX-D150W.", "sort_order": 1},
			{"question": "Why not just use D160 faster?", "answer": "D160’s optional 3,076 cps is still a 65 μm / 6-line Dynamic jet. D150 is a 55 μm high-speed nozzle with 2,000 messages as standard.", "sort_order": 2},
			{"question": "Is Safe-Clean-Station included?", "answer": "No. The D150 datasheet lists it under optional parts.", "sort_order": 3},
			{"question": "Which ERP Item is this?", "answer": "IND.SYS.HIJ.4369 — Hitachi Ink Jet Printer, UX2-D150W. Older UX-D150W Items are a different generation.", "sort_order": 4},
		],
	)


def _set_related(doc, exclude_slug: str):
	related = [
		row
		for row in (
			related_by_slug("hitachi-ux2-d160", 1) if exclude_slug != "hitachi-ux2-d160" else None,
			related_by_slug("hitachi-ux2-d150", 1 if exclude_slug == "hitachi-ux2-d160" else 2) if exclude_slug != "hitachi-ux2-d150" else None,
			related_by_slug("hitachi-ux-d161", 2),
			related_by_slug("hitachi-ux-d151", 3),
		)
		if row
	]
	# fix sort
	for idx, row in enumerate(related, start=1):
		row["sort_order"] = idx
	doc.set("related_products", related)


def _save(doc):
	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	frappe.db.commit()


def fill_hitachi_ux2():
	d160 = fill_hitachi_ux2_d160()
	d150 = fill_hitachi_ux2_d150()
	# Refresh related now that both exist.
	fill_hitachi_ux2_d160()
	fill_hitachi_ux2_d150()
	name = frappe.db.get_value("Website Solution", {"slug": "coding-marking"}, "name")
	if name:
		sol = frappe.get_doc("Website Solution", name)
		sol.related_product_slugs = "hitachi-ux2-d160\nhitachi-ux2-d150\nhitachi-ux-d161\nrea-jet-coding-systems"
		sol.flags.ignore_permissions = True
		sol.save()
		frappe.db.commit()
	return {"d160": d160, "d150": d150}
