# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for ANSER A1 (Industrial TIJ carton coder).

Official product page:
https://www.anser-coding.com/product_thermal-detail/ANSER_A1_All_in_one_inkjet_printer/

This page is the A1 family. The linked ERP Item is the 1-inch single-head UK
anti-shock kit (IND.SYS.ANS.4211). The 0.5-inch single-head kit is
IND.SYS.ANS.4214. About 2 inches / 48.7–50 mm is a stitch of two 1-inch heads
— an official A1 capability, not a third ERP Item, and not included on 4211.

Do not mix SPH, X1, U2, Sojet or Kezojet KT10 ratings onto this page.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image

import frappe

ITEM = "IND.SYS.ANS.4211"
ITEM_HALF = "IND.SYS.ANS.4214"
SLUG = "anser-a1"

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
TMP_DIR = Path("/tmp/anser-a1-imgs")

VIDEO_A1 = "https://youtu.be/w512l49FLys"
VIDEO_SYNC = "https://youtu.be/6_wkciZOsqk"
VIDEO_IJ = "https://youtu.be/YrQWSdleiXY"
VIDEO_BATCH = "https://youtu.be/AmezcbmjzNE"

CUTOUT = "anser-a1-product.jpg"
CARD = "anser-a1-card.jpg"

# Official A1 product-page assets only (not SPH / X1 / U2 / application stock).
OFFICIAL = {
	"anser-a1-carton.png": [
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23E03_2w7pthp2g9.png",
	],
	"anser-a1-carton-close.jpg": [
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23E03_dnz4aayswh.jpg",
	],
	"anser-a1-carton-dpi.jpg": [
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23E03_psdhdjg5qs.jpg",
	],
	CUTOUT: [
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23G25_cwwtqw5jsq.jpg",
	],
	"anser-a1-hmi.jpg": [
		"https://www.anser-coding.com/upload/catalog_product_thermal_list_pic2/"
		"enL_catalog_product_thermal_23E17_fkp74cphg8.jpg",
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23E17_fkp74cphg8.jpg",
	],
	"anser-a1-setup.png": [
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23G25_3iznv28w6f.png",
	],
	"anser-a1-stand.png": [
		"https://www.anser-coding.com/upload/catalog_product_thermal_b/"
		"enL_catalog_product_thermal_23E03_aaa7y2kw7x.png",
	],
}

TMP_FALLBACK = {
	"anser-a1-carton.png": "01_enL_catalog_product_thermal_23E03_2w7pthp2g9.png",
	"anser-a1-carton-close.jpg": "03_enL_catalog_product_thermal_23E03_dnz4aayswh.jpg",
	"anser-a1-carton-dpi.jpg": "04_enL_catalog_product_thermal_23E03_psdhdjg5qs.jpg",
	CUTOUT: "09_enL_catalog_product_thermal_23G25_cwwtqw5jsq.jpg",
	"anser-a1-hmi.jpg": "10_enL_catalog_product_thermal_23E17_fkp74cphg8.jpg",
	"anser-a1-setup.png": "08_enL_catalog_product_thermal_23G25_3iznv28w6f.png",
	"anser-a1-stand.png": "02_enL_catalog_product_thermal_23E03_aaa7y2kw7x.png",
}

HEADERS = {
	"User-Agent": (
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
		"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	)
}


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
	last_error = None
	for url in urls:
		try:
			request = Request(url, headers=HEADERS)
			with urlopen(request, timeout=30) as response, target.open("wb") as handle:
				handle.write(response.read())
			if target.exists() and target.stat().st_size > 0:
				return f"/files/{filename}"
		except Exception as exc:
			last_error = exc
	fallback = TMP_DIR / TMP_FALLBACK.get(filename, "")
	if fallback.exists() and fallback.stat().st_size > 0:
		copy2(fallback, target)
		return f"/files/{filename}"
	if last_error:
		raise last_error
	frappe.throw(f"Could not download {filename}")


def catalog_card(source_name: str, dest_name: str) -> str:
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGBA")
	scale = min(1040 / im.width, 1040 / im.height)
	new = im.resize((int(im.width * scale), int(im.height * scale)), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


def related_by_slug(slug: str, sort_order: int) -> dict | None:
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if not name:
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


def get_or_create(hero: str):
	existing = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = SLUG
	if frappe.db.exists("Item", ITEM):
		other = frappe.db.get_value("Website Product", {"item": ITEM}, "name")
		if not other:
			doc.item = ITEM
	doc.website_product_name = "Anser A1"
	doc.display_name = "Anser A1"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.short_description = "ANSER A1 all-in-one thermal inkjet printer for carton and case coding."
	doc.long_description = "<p>ANSER A1 all-in-one thermal inkjet printer for carton and case coding.</p>"
	doc.hero_image = hero
	return doc


def append_related_slugs(doctype: str, slug: str, extras: list[str], prepend: bool = False):
	name = frappe.db.get_value(doctype, {"slug": slug}, "name")
	if not name:
		return
	doc = frappe.get_doc(doctype, name)
	current = [s.strip() for s in (doc.related_product_slugs or "").splitlines() if s.strip()]
	for extra in extras:
		if extra in current:
			continue
		if prepend:
			current.insert(0, extra)
		else:
			current.append(extra)
	doc.related_product_slugs = "\n".join(current)
	doc.flags.ignore_permissions = True
	doc.save()


def fill_anser_a1():
	for filename, urls in OFFICIAL.items():
		download_file(filename, urls)
	card = catalog_card(CUTOUT, CARD)
	carton = f"/files/anser-a1-carton.png"
	carton_close = f"/files/anser-a1-carton-close.jpg"
	carton_dpi = f"/files/anser-a1-carton-dpi.jpg"
	cutout = f"/files/{CUTOUT}"
	hmi = f"/files/anser-a1-hmi.jpg"
	setup = f"/files/anser-a1-setup.png"
	stand = f"/files/anser-a1-stand.png"
	food = copy_public_image("industry-food-beverage.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	warehouse = copy_public_image("industry-warehouse-logistics.jpg")

	doc = get_or_create(card)
	if frappe.db.exists("Item", ITEM) and not doc.item:
		other = frappe.db.get_value("Website Product", {"item": ITEM}, "name")
		if not other or other == doc.name:
			doc.item = ITEM

	doc.display_name = "Anser A1"
	doc.website_product_name = "Anser A1"
	doc.slug = SLUG
	if frappe.db.exists("Brand", "ANSER"):
		doc.brand = "ANSER"
	doc.brand_name = "ANSER"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.page_mode = "Full"
	doc.category = "Coding & Marking"
	doc.subcategory = "Thermal Inkjet"
	doc.category_label = "THERMAL INKJET PRINTER"
	doc.tagline = "2-inch all-in-one TIJ for carton and case coding"
	doc.short_description = (
		"ANSER A1 is a 2-inch all-in-one thermal inkjet coder for boxes, cases and "
		"cartons. This page is linked to the 1-inch single-head UK anti-shock kit "
		"(IND.SYS.ANS.4211). A 0.5-inch single-head kit is IND.SYS.ANS.4214."
	)
	doc.long_description = (
		"<p>ANSER A1 is ANSER Coding’s first 2-inch all-in-one thermal inkjet (TIJ) "
		"printer for box, case and carton coding in food and beverage, pharmaceutical "
		"and electronics plants. Controller, 5-inch capacitive touchscreen and "
		"cartridge heads sit in one 2 kg unit — no separate cabinet.</p>"
		"<p>Official print height is 12.7 mm (0.5 inch) or 25.4 mm (1.0 inch) on a "
		"single head. Two heads stitch to 24.75 mm or about 50 mm / 1.97 inch. This "
		"website product is the 1-inch single-head UK anti-shock item "
		"<strong>IND.SYS.ANS.4211</strong>. The 0.5-inch single-head kit is "
		"<strong>IND.SYS.ANS.4214</strong>. A ~2-inch stitch uses two 1-inch heads; "
		"it is not a third ERP item and is not included on 4211.</p>"
		"<p>HP or IUT cartridges print static text and logos plus dynamic string, "
		"shift, counter, production and expiry dates and barcodes at up to 600 DPI. "
		"Line speed is 60.96 m/min at 300 DPI or 121 m/min at 150 DPI. Multi-DPI can "
		"put a 300 DPI QR next to 150 DPI text on the same carton. A 3-step setup "
		"assistant aims to get the station printing in about three minutes.</p>"
		"<p>Direct-to-box coding reduces labels and pre-printed cartons. Printechs "
		"supplies, installs and supports ANSER A1 in Riyadh, Jeddah and Dammam with "
		"genuine cartridges and operator training.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "ANSER A1 all-in-one thermal inkjet printer, 5-inch touchscreen and dual cartridge ports"
	doc.video_url = VIDEO_A1
	doc.hero_trust_chips = (
		"2-inch all-in-one TIJ\n"
		"5-inch capacitive HMI\n"
		"Up to 600 DPI\n"
		"Carton & case coding"
	)
	doc.story_heading = "Print the case. Skip the label."
	doc.visual_story_heading = "A1 carton coding"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "A1"
	doc.card_brand_label = "ANSER"
	doc.card_summary = (
		"2-inch all-in-one TIJ for boxes and cases. 5-inch HMI, up to 600 DPI. "
		"This kit is the 1-inch single head with anti-shock."
	)
	doc.card_image = card
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.final_cta_heading = "Specify A1 for your carton line"
	doc.final_cta_description = (
		"Printechs will confirm 0.5-inch or 1-inch heads, stitch height, HP or IUT "
		"ink and mounting for ANSER A1 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "ANSER A1 Thermal Inkjet Carton Coder | Printechs"
	doc.meta_description = (
		"ANSER A1 all-in-one TIJ for carton and case coding. 5-inch HMI, up to "
		"600 DPI. 1-inch UK anti-shock kit from Printechs in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "print",
				"title": "Direct-to-carton TIJ",
				"description": (
					"First 2-inch all-in-one ANSER printer for box and case codes — QR, "
					"lot, date and handling text without a label or pre-printed panel."
				),
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "5-inch glove-ready HMI",
				"description": (
					"Colour capacitive 480×800 portrait touchscreen. Arabic and 23 other "
					"operator languages. One unit, no remote cabinet."
				),
				"sort_order": 2,
			},
			{
				"icon": "speed",
				"title": "Multi-DPI, line speed",
				"description": (
					"Up to 600 DPI. 60.96 m/min at 300 DPI or 121 m/min at 150 DPI. "
					"Print a sharp QR at 300 DPI next to faster 150 DPI text."
				),
				"sort_order": 3,
			},
			{
				"icon": "install",
				"title": "Three-minute setup",
				"description": (
					"Official Smart Setup Assistant: line settings, print station, then "
					"message — typically running in three minutes with no daily flush."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Carton coding",
				"image": carton,
				"image_alt": "ANSER A1 printing a QR code, lot, date and handling text on a brown carton",
				"caption": "Official A1 carton shot: QR plus product, MFD, lot and handling text on the box.",
				"sort_order": 1,
			},
			{
				"label": "Case mark close-up",
				"image": carton_close,
				"image_alt": "Close-up of ANSER A1 coding a shipping carton with QR and variable text",
				"caption": "Same official case-coding view — the job A1 is built for.",
				"sort_order": 2,
			},
			{
				"label": "Multi-DPI on the box",
				"image": carton_dpi,
				"image_alt": "ANSER A1 carton print with 300 DPI QR and 150 DPI text on one message",
				"caption": "Official Multi-DPI: 300 DPI QR beside 150 DPI text on one carton pass.",
				"sort_order": 3,
			},
			{
				"label": "A1 all-in-one",
				"image": cutout,
				"image_alt": "ANSER A1 all-in-one TIJ printer cutout with dual cartridge ports and 5-inch screen",
				"caption": "Controller, 5-inch HMI and two cartridge ports in one 2 kg unit.",
				"sort_order": 4,
			},
			{
				"label": "5-inch HMI",
				"image": hmi,
				"image_alt": "Front of ANSER A1 showing 5-inch touchscreen, Ethernet, encoder and USB ports",
				"caption": "Portrait 480×800 capacitive screen with Ethernet, encoder, sensor and USB.",
				"sort_order": 5,
			},
			{
				"label": "3-step setup",
				"image": setup,
				"image_alt": "ANSER A1 Smart Setup Assistant: line, station and print message in three steps",
				"caption": "Official assistant: production line, print station, assign message — about 3 minutes.",
				"sort_order": 6,
			},
			{
				"label": "Line mount",
				"image": stand,
				"image_alt": "ANSER A1 mounted on a production-line stand above the conveyor path",
				"caption": "Compact all-in-one on a line stand — no remote ink cabinet.",
				"sort_order": 7,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "Thermal inkjet", "description": "HP / IUT cartridges · water or solvent", "sort_order": 1},
			{"icon": "lines", "title": "This SKU: 25.4 mm", "description": "1-inch single head · 4211 with anti-shock", "sort_order": 2},
			{"icon": "display", "title": "5-inch HMI", "description": "480×800 portrait · glove capacitive", "sort_order": 3},
			{"icon": "speed", "title": "60.96 / 121 m/min", "description": "300 DPI / 150 DPI · max 600 DPI", "sort_order": 4},
			{"icon": "connectivity", "title": "USB · RS-232/485", "description": "Encoder + sensor (NPN) · Ethernet", "sort_order": 5},
			{"icon": "install", "title": "All-in-one", "description": "161.5 × 125 × 136 mm · 2 kg · 90 W", "sort_order": 6},
		],
	)

	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "ANSER A1 all-in-one TIJ (not SPH printhead, not X1, not U2)"),
					("Item on this page", "IND.SYS.ANS.4211 — 1-inch single printhead, UK, anti-shock"),
					("Also available", "IND.SYS.ANS.4214 — 0.5-inch single printhead, UK, anti-shock"),
					("Stitch ~2 inch", "Two 1-inch heads @ about 50 mm / 1.97 in (ANSER). Not a third item; not on 4211."),
					("Included on 4211", "A1 unit, 1-inch single-head kit, UK, anti-shock"),
				],
			),
			(
				"Printing performance",
				[
					("Technology", "Thermal inkjet (TIJ), HP and IUT cartridges"),
					("Print height (single)", "12.7 mm (0.5 in) or 25.4 mm (1.0 in) — this SKU is 25.4 mm"),
					("Print height (stitch)", "12.7 mm × 2 @ 24.75 mm, or 25.4 mm × 2 @ ~50 mm / 1.97 in"),
					("Resolution", "Up to 600 DPI. Multi-DPI example: 300 DPI QR with 150 DPI text"),
					("Print speed", "60.96 m/min at 300 DPI; 121 m/min at 150 DPI (ANSER official)"),
					("Throw distance", "Typically 6 mm (ANSER A1 brochure)"),
					("Static data", "Text, logo, shape and image"),
					("Dynamic data", "String, shift, counter, production date, expiration date"),
					("1D barcodes", "EAN-8/13/14/128, UPC-A/E, Code 39/128, ITF-14, Inter 2 of 5, Codabar, DUN-14"),
					("2D / GS1", "QR, Data Matrix, PDF417, Aztec, GS1 DataMatrix/DataBar/QR, NVE-18 / SSCC-18"),
				],
			),
			(
				"Inks & cartridges",
				[
					("Cartridges", "HP and IUT 0.5-inch or 1-inch TIJ cartridges (match to this SKU’s head)"),
					("Ink bases", "Water-based and solvent-based (ANSER ink range; confirm per substrate)"),
					("Typical job", "Corrugated case, paperboard carton, shipper — direct coding, fewer labels"),
				],
			),
			(
				"Controller, I/O & environment",
				[
					("Display", "5-inch colour capacitive touch, 480×800 portrait, glove-compatible"),
					("Languages", "24 languages including Arabic, English and both Chinese scripts"),
					("Fonts", "TrueType including Noto CJK, Amiri, Open Sans, OCR-B (ANSER official list)"),
					("I/O (ANSER)", "USB 2.0 ×1, RS-232 & RS-485 ×1, encoder NPN, sensor NPN"),
					("Network", "Ethernet on the unit. Modbus TCP/UDP and RTU 485 (Masterprint listing)"),
					("Power", "AC 100–240 V, 50/60 Hz, 90 W"),
					("Size / weight", "161.5 × 125 × 136 mm (L×H×W), 2 kg (ANSER official)"),
					("Climate", "0–40 °C (32–104 °F); 0–90% RH, non-condensing"),
				],
			),
		],
	)

	doc.set(
		"applications",
		[
			{
				"title": "Carton and case coding",
				"description": "QR, lot, date and handling text printed on the shipper — official A1 box job.",
				"image": carton,
				"image_alt": "ANSER A1 printing a QR code and variable text on a carton",
				"industry_link": "packaging",
				"sort_order": 1,
			},
			{
				"title": "Food and beverage cases",
				"description": "Direct codes on outer cases instead of labels or pre-printed carton panels.",
				"image": food,
				"image_alt": "Food and beverage packaging ready for case coding",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Pharmaceutical cartons",
				"description": "Batch, expiry and 2D codes on healthcare packs at up to 600 DPI.",
				"image": pharma,
				"image_alt": "Pharmaceutical carton coding on a packaging line",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Warehouse shippers",
				"description": "Readable case marks for outbound boxes — SSCC / NVE-18 and QR on brown board.",
				"image": warehouse,
				"image_alt": "Warehouse cartons ready for outbound case coding",
				"industry_link": "warehouse-logistics",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "ANSER A1 — cost-effective carton coding",
				"body": (
					"Official ANSER Coding film: A1 as a 2-inch all-in-one TIJ for box "
					"printing. Watch the 5-inch HMI and the case mark, then we size "
					"1-inch (4211) or 0.5-inch (4214) heads for your line."
				),
				"video_url": VIDEO_A1,
				"image": carton,
				"image_alt": "ANSER A1 printing QR and text on a shipping carton",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Print the shipper, not a label",
				"body": (
					"A1 is built for corrugated cases: QR, product ID, manufacture date, "
					"lot and handling text in one pass. Direct coding cuts label stock "
					"and pre-printed carton waste — ANSER’s eco-friendly case message."
				),
				"image": carton_close,
				"image_alt": "Close-up of an ANSER A1 carton code on brown board",
				"link_label": "Packaging industry",
				"link_href": "/industries/packaging",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Multi-DPI and QuickSync",
				"body": (
					"Official Multi-DPI keeps a 300 DPI QR sharp while text can run at "
					"150 DPI on the same carton. QuickSync is ANSER’s own A1 clip for "
					"message and line setup — not an SPH or X1 video."
				),
				"video_url": VIDEO_SYNC,
				"image": carton_dpi,
				"image_alt": "ANSER A1 Multi-DPI carton print, 300 DPI QR and 150 DPI text",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Three steps, about three minutes",
				"body": (
					"Smart Setup Assistant: production-line settings, print-station "
					"settings, assign the message. ANSER rates a first print in three "
					"minutes or less. No makeup fluid and no daily CIJ flush."
				),
				"image": setup,
				"image_alt": "ANSER A1 three-step setup assistant on the 5-inch screen",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "0.5 inch, 1 inch, or stitch ~2 inches",
				"body": (
					"IND.SYS.ANS.4211 on this page is the 1-inch single head with "
					"anti-shock (UK). Order IND.SYS.ANS.4214 for the 0.5-inch single "
					"head. A ~2-inch / 48.7–50 mm band is two 1-inch heads stitched — "
					"ask us to quote that kit; it is not bundled on 4211."
				),
				"image": cutout,
				"image_alt": "ANSER A1 dual cartridge ports for 0.5-inch or 1-inch TIJ cartridges",
				"link_label": "Request a Quote",
				"link_href": f"/products/{SLUG}/quote",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "A1 on a carton line (distributor films)",
				"body": (
					"These clips are from ANSER distributors (InkJet Inc. and a batch-"
					"coding partner), not ANSER HQ. They show A1 TIJ on cartons. We "
					"still confirm throw (about 6 mm), ink and photocell on your case "
					"sealer in Riyadh, Jeddah or Dammam."
				),
				"video_url": VIDEO_IJ,
				"image": packaging,
				"image_alt": "Packaging line cartons for thermal inkjet case coding",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Batch codes on cases, supported in KSA",
				"body": (
					"A second distributor film of A1 batch coding on cartons. Printechs "
					"installs the stand, photocell and first messages, and stocks HP / "
					"IUT cartridges. Need a compact printhead only? See ANSER SPH. "
					"Need a 10.1-inch twin-head station? See Kezojet KT10."
				),
				"video_url": VIDEO_BATCH,
				"image": food,
				"image_alt": "Food-line cases ready for batch and date coding",
				"link_label": "Talk to a specialist",
				"link_href": "/contact",
				"sort_order": 7,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Stand, photocell, ~6 mm throw, encoder and first carton messages.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Cartridges",
				"description": "HP / IUT 0.5-inch or 1-inch — water or solvent, matched to the board.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Spares & service",
				"description": "Anti-shock parts, cables and on-site support in Saudi Arabia.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "5-inch HMI, 3-step assistant, cartridge change and Multi-DPI messages.",
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
			{"item_description": "ANSER A1 all-in-one TIJ with 5-inch colour touchscreen", "sort_order": 1},
			{"item_description": "1-inch single printhead configuration (this SKU)", "sort_order": 2},
			{"item_description": "UK specification", "sort_order": 3},
			{"item_description": "Anti-shock", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])

	related = [
		row
		for row in (
			related_by_slug("anser-sph-smart-printhead", 1),
			related_by_slug("kezojet-kt10", 2),
		)
		if row
	]
	doc.set("related_products", related)

	doc.set(
		"faq_items",
		[
			{
				"question": "Which Item is on this page?",
				"answer": (
					"IND.SYS.ANS.4211 — ANSER A1 with a 1-inch single printhead, UK, "
					"anti-shock. The 0.5-inch single-head kit is IND.SYS.ANS.4214. "
					"A ~2-inch stitch is two 1-inch heads, quoted separately."
				),
				"sort_order": 1,
			},
			{
				"question": "Is A1 a carton / case coder?",
				"answer": (
					"Yes. ANSER positions A1 as a 2-inch all-in-one TIJ for box printing "
					"— food, pharma and electronics shippers. Official photos show QR, "
					"lot, date and handling text on brown board."
				),
				"sort_order": 2,
			},
			{
				"question": "How fast and how tall does it print?",
				"answer": (
					"ANSER lists 60.96 m/min at 300 DPI and 121 m/min at 150 DPI, up to "
					"600 DPI. This SKU prints 25.4 mm. Stitch of two 1-inch heads is "
					"about 50 mm / 1.97 inch. Throw is typically 6 mm."
				),
				"sort_order": 3,
			},
			{
				"question": "What can it print?",
				"answer": (
					"Text, logos, dates, shift, counter and a wide barcode set: EAN, "
					"UPC, Code 39/128, ITF-14, QR, Data Matrix, PDF417, Aztec and GS1 "
					"codes including SSCC-18 / NVE-18."
				),
				"sort_order": 4,
			},
			{
				"question": "Do you install A1 in Saudi Arabia?",
				"answer": (
					"Yes. Printechs supplies A1, HP/IUT cartridges, mounting and "
					"commissioning, and after-sales service in Riyadh, Jeddah and Dammam."
				),
				"sort_order": 5,
			},
		],
	)

	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()

	if frappe.db.exists("Item", ITEM):
		item = frappe.get_doc("Item", ITEM)
		if item.image != card:
			item.db_set("image", card, update_modified=False)
	if frappe.db.exists("Item", ITEM_HALF):
		half = frappe.get_doc("Item", ITEM_HALF)
		if not half.image:
			half.db_set("image", card, update_modified=False)

	# Cross-link SPH if that page has no related products yet.
	sph_name = frappe.db.get_value("Website Product", {"slug": "anser-sph-smart-printhead"}, "name")
	if sph_name:
		sph = frappe.get_doc("Website Product", sph_name)
		if not sph.related_products:
			row = related_by_slug(SLUG, 1)
			if row:
				sph.set("related_products", [row])
				sph.flags.ignore_permissions = True
				sph.save()

	append_related_slugs(
		"Website Solution",
		"coding-marking",
		["anser-a1", "anser-sph-smart-printhead", "kezojet-kt10"],
		prepend=True,
	)
	for industry_slug in ("packaging", "food-beverage", "pharmaceutical"):
		append_related_slugs("Website Industry", industry_slug, ["anser-a1"])

	frappe.db.commit()
	print(f"Filled and published {doc.name} → /products/{doc.slug} (item={doc.item})")
	return doc.name
