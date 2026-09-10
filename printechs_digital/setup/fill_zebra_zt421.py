# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.ZEB.3626 — Zebra ZT421 (203 dpi).

Official:
https://www.zebra.com/us/en/products/printers/industrial/zt400-series/zt421.html
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/zt400-series-spec-sheet-en-us.pdf
https://www.zebra.com/content/dam/zebra_dam/en/tech-specs/zt421-tech-specs-en-us.pdf

This page is the 203 dpi colour-display kit (USB, RS-232, Bluetooth, Ethernet).
Do not mix 300 dpi (RET.SYS.ZEB.4943), the cutter SKU (RET.SYS.ZEB.3628),
ZT411 4-inch / 600 dpi, or RFID-enabled ZT421 onto this item.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image

import frappe

NAME = "RET.SYS.ZEB.3626"
ITEM_300 = "RET.SYS.ZEB.4943"
SLUG = "zebra-zt421"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
TMP_DIR = Path("/tmp/zt421-imgs")

VIDEO_SETUP = "https://youtu.be/h-YhWqI2zUY"
VIDEO_LOAD = "https://youtu.be/rAOxqJ6o6gc"
VIDEO_CAL = "https://youtu.be/2hd-wDxfwuA"

FRONT = "zebra-zt421-front.png"
ANGLE = "zebra-zt421-angle.png"
WINDOW = "zebra-zt421-window.png"
CLOSED = "zebra-zt421-closed.png"
CARD = "zebra-zt421-card.jpg"

OFFICIAL_ANGLES = {
	FRONT: [
		"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4380/9139/zt421-rfid-printer-3__74499.1780395569.png?c=2",
	],
	ANGLE: [
		"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4380/9136/zt421-rfid-printer-2__78999.1780395569.png?c=2",
	],
	WINDOW: [
		"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4380/9137/zt421-rfid-printer__81491.1780395569.png?c=2",
	],
	CLOSED: [
		"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4380/9138/zt421-rfid-printer-1__01526.1780395569.png?c=2",
	],
}

TMP_FALLBACK = {
	FRONT: "p4.png",
	ANGLE: "p1.png",
	WINDOW: "p2.png",
	CLOSED: "p3.png",
}

LOCAL_SCENES = {
	"zebra-zt421-warehouse.png": "zt421 ware house.png",
	"zebra-zt421-retail.png": "zt421 retail.png",
	"zebra-zt421-packaging.png": "zt421 packaging.png",
	"zebra-zt421-manufacturing.png": "zt421 manufacturing.png",
}

HEADERS = {
	"User-Agent": (
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
		"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	)
}


def copy_local(dest_name: str, source_name: str) -> str:
	source = SITE_FILES / source_name
	target = SITE_FILES / dest_name
	if source.exists() and (not target.exists() or target.stat().st_size == 0):
		copy2(source, target)
	return f"/files/{dest_name}"


def download_file(filename: str, urls: list[str]) -> str:
	target = SITE_FILES / filename
	if target.exists() and target.stat().st_size > 20000:
		return f"/files/{filename}"
	last_error = None
	for url in urls:
		try:
			request = Request(url, headers=HEADERS)
			with urlopen(request, timeout=30) as response, target.open("wb") as handle:
				handle.write(response.read())
			if target.exists() and target.stat().st_size > 20000:
				return f"/files/{filename}"
		except Exception as exc:
			last_error = exc
	fallback = TMP_DIR / TMP_FALLBACK.get(filename, "")
	if fallback.exists() and fallback.stat().st_size > 20000:
		copy2(fallback, target)
		return f"/files/{filename}"
	legacy = SITE_FILES / "zt421-front-photography-website-3x2-3600x2400.jpg.imgw.1920.1920.jpg"
	if filename == FRONT and legacy.exists():
		copy2(legacy, target)
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


def fill_zebra_zt421():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	for filename, urls in OFFICIAL_ANGLES.items():
		download_file(filename, urls)
	card = catalog_card(FRONT, CARD)
	front = f"/files/{FRONT}"
	angle = f"/files/{ANGLE}"
	window = f"/files/{WINDOW}"
	closed = f"/files/{CLOSED}"
	warehouse = copy_local("zebra-zt421-warehouse.png", LOCAL_SCENES["zebra-zt421-warehouse.png"])
	retail = copy_local("zebra-zt421-retail.png", LOCAL_SCENES["zebra-zt421-retail.png"])
	packaging = copy_local("zebra-zt421-packaging.png", LOCAL_SCENES["zebra-zt421-packaging.png"])
	manufacturing = copy_local(
		"zebra-zt421-manufacturing.png", LOCAL_SCENES["zebra-zt421-manufacturing.png"]
	)

	doc = frappe.get_doc("Website Product", NAME)
	doc.display_name = "Zebra ZT421"
	doc.website_product_name = "Zebra ZT421"
	doc.slug = SLUG
	if frappe.db.exists("Brand", "Zebra"):
		doc.brand = "Zebra"
	doc.brand_name = "Zebra"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.page_mode = "Full"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Industrial Label Printers"
	doc.category_label = "INDUSTRIAL LABEL PRINTER"
	doc.tagline = "6.6-inch industrial printer — 203 dpi, 12 ips, colour touch"
	doc.short_description = (
		"Zebra ZT421 industrial label printer: 6.6-inch / 168 mm print width, 203 dpi on this "
		"SKU, 4.3-inch colour touch display, ZPL/EPL and USB, serial, Bluetooth and Ethernet. "
		"Thermal transfer or direct thermal for shipping, pallet and compliance labels."
	)
	doc.long_description = (
		"<p>The Zebra ZT421 is the 6-inch-class industrial printer in the ZT400 Series. "
		"Official print width is 6.6 inches (168 mm) at up to 12 ips (305 mm/s). This page "
		"is <strong>RET.SYS.ZEB.3626</strong> — 203 dpi (8 dots/mm), colour display, real-time "
		"clock, EPL / ZPL / ZPL II, USB, RS-232, Bluetooth and Ethernet. It is not the 300 dpi "
		"kit (RET.SYS.ZEB.4943), not the cutter SKU, and not an RFID-enabled ZT421.</p>"
		"<p>A 4.3-inch colour touchscreen and bi-fold metal door make media and ribbon loading "
		"straightforward. Dual transmissive/reflective sensors, a colour-coded path and Link-OS "
		"/ Zebra DNA cover warehouse, DC, packaging and manufacturing labels. Wi-Fi 5 or Wi-Fi 6, "
		"peeler, cutter and rewind are field or factory options — not on this item.</p>"
		"<p>ZT421 replaces ZM600 and ZT420. 600 dpi is a ZT411 option only. In the box: printer, "
		"power cord and quick-start guide (USB cable is not included). Printechs supplies ZT421 "
		"with Zebra media, ribbons and service in Riyadh, Jeddah and Dammam.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZT421 industrial label printer, front view with 4.3-inch colour touch display"
	doc.video_url = VIDEO_SETUP
	doc.hero_trust_chips = (
		"6.6 in / 168 mm print width\n"
		"203 dpi on this SKU · 12 ips\n"
		"4.3-inch colour touch\n"
		"USB · serial · BT · Ethernet"
	)
	doc.story_heading = "Wide industrial labels. Colour touch. Link-OS."
	doc.visual_story_heading = "ZT421 on the bench and on the line"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "ZT421"
	doc.card_brand_label = "Zebra"
	doc.card_summary = (
		"6.6-inch industrial printer, 203 dpi on this kit, 12 ips, 4.3-inch colour touch. "
		"ZPL/EPL, USB, serial, Bluetooth and Ethernet."
	)
	doc.card_image = card
	doc.show_item_code_on_website = 1
	doc.final_cta_heading = "Specify ZT421 for shipping and compliance labels"
	doc.final_cta_description = (
		"Printechs will confirm 203 vs 300 dpi, media width, ribbon and whether you need "
		"Wi-Fi, peel or cutter for Zebra ZT421 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Zebra ZT421 Industrial Label Printer 203 dpi | Printechs"
	doc.meta_description = (
		"Zebra ZT421 6.6-inch industrial printer, 203 dpi, 12 ips, 4.3-inch colour touch. "
		"ZPL/EPL, Ethernet. Supplied by Printechs in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "print",
				"title": "6.6-inch industrial width",
				"description": (
					"Official print width 168 mm — shipping, pallet and compliance labels "
					"wider than a 4-inch ZT411. 12 ips / 305 mm/s at 203 dpi on this SKU."
				),
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "4.3-inch colour touch",
				"description": (
					"Icon menu, status at a glance and a real-time clock. Colour-coded, "
					"lighted media path for ribbon and labels."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Ready to connect",
				"description": (
					"USB 2.0, dual USB Host, RS-232, Bluetooth 4.1 and 10/100 Ethernet "
					"on this kit. Wi-Fi 5 / Wi-Fi 6 is optional, not included."
				),
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "ZPL, EPL and Link-OS",
				"description": (
					"Move existing Zebra formats with ZPL / ZPL II and EPL. Link-OS and "
					"Zebra DNA for setup, security and fleet tools."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "ZT421 front",
				"image": front,
				"image_alt": "Front of a Zebra ZT421 with colour touchscreen and print path",
				"caption": "4.3-inch colour touch, Pause / Feed / Cancel, USB host on the front.",
				"sort_order": 1,
			},
			{
				"label": "Printing a label",
				"image": angle,
				"image_alt": "Zebra ZT421 at an angle printing a label",
				"caption": "Thermal transfer or direct thermal — this SKU does both.",
				"sort_order": 2,
			},
			{
				"label": "Media window",
				"image": window,
				"image_alt": "Zebra ZT421 side window showing the media roll",
				"caption": "Up to 8-inch OD rolls on a 3-inch core. Ribbon up to 450 m.",
				"sort_order": 3,
			},
			{
				"label": "Closed unit",
				"image": closed,
				"image_alt": "Zebra ZT421 closed metal bi-fold door",
				"caption": "Metal frame and bi-fold door — the ZT400 industrial chassis.",
				"sort_order": 4,
			},
			{
				"label": "Warehouse shipping",
				"image": warehouse,
				"image_alt": "ZT421 printing a shipping label in a warehouse",
				"caption": "Carton and shipper labels for outbound logistics.",
				"sort_order": 5,
			},
			{
				"label": "Case labelling",
				"image": packaging,
				"image_alt": "ZT421 printing case labels next to a packed carton",
				"caption": "Case and pallet IDs on packing lines.",
				"sort_order": 6,
			},
			{
				"label": "Manufacturing",
				"image": manufacturing,
				"image_alt": "ZT421 printing a work-in-progress label on a factory bench",
				"caption": "WIP, component and compliance labels on the shop floor.",
				"sort_order": 7,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 6.6 in / 168 mm · 12 ips", "sort_order": 1},
			{"icon": "display", "title": "4.3-inch HMI", "description": "Colour touch · real-time clock", "sort_order": 2},
			{"icon": "connectivity", "title": "On this kit", "description": "USB · RS-232 · BT 4.1 · Ethernet", "sort_order": 3},
			{"icon": "integration", "title": "Languages", "description": "EPL · ZPL · ZPL II · Link-OS", "sort_order": 4},
			{"icon": "durability", "title": "Industrial", "description": "Metal frame · 40 lb / 18.14 kg", "sort_order": 5},
			{"icon": "inventory", "title": "Typical jobs", "description": "Shipping · pallet · compliance · WIP", "sort_order": 6},
		],
	)

	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZT421 (ZT400 Series) — not ZT411, not ZT421 RFID"),
					("Item on this page", "RET.SYS.ZEB.3626 — 203 dpi, colour display, RTC, EPL/ZPL, USB, RS-232, BT, Ethernet"),
					("Also available", "RET.SYS.ZEB.4943 — 300 dpi ZT421 (Euro/UK cord). Ask if you need that kit."),
					("Not on this item", "Cutter, peeler, rewind, Wi-Fi 5/6, RFID encode — options, quoted separately"),
					("In the box", "Printer, power cord, quick-start guide. USB A-to-B cable is not included."),
					("Replaces", "ZM600 and ZT420 (Zebra official)"),
				],
			),
			(
				"Printing",
				[
					("Method", "Thermal transfer and direct thermal"),
					("Resolution (this SKU)", "203 dpi / 8 dots per mm. 300 dpi is a different item."),
					("Print width", "Up to 6.6 in / 168 mm (not 4.09 in ZT411)"),
					("Print speed", "Up to 12 ips / 305 mm per second"),
					("Print length (203 dpi)", "Up to 102 in / 2591 mm"),
					("Printhead", "Thin-film with E3 Element Energy Equalizer"),
					("Memory", "256 MB SDRAM, 512 MB linear Flash"),
				],
			),
			(
				"Media & ribbon",
				[
					("Media width", "2.00–7.0 in (51–178 mm) tear/cutter; 2.00–6.75 in peel/rewind"),
					("Media roll", "8.0 in / 203 mm OD on a 3 in / 76 mm ID core"),
					("Media types", "Continuous, die-cut, notch, black-mark"),
					("Sensors", "Adjustable dual sensors — transmissive and reflective"),
					("Ribbon", "Up to 450 m / 1476 ft; width 2.00–6.85 in (51–174 mm); 1 in core"),
					("Ribbon wind", "Coated-side-out on the standard spindle"),
				],
			),
			(
				"Control, I/O & environment",
				[
					("Display", "4.3-inch full-colour capacitive touch, real-time clock"),
					("Languages", "EPL, ZPL, ZPL II. Link-OS and Zebra DNA for Printers"),
					("Standard I/O", "USB 2.0, dual USB Host, RS-232, Bluetooth 4.1, 10/100 Ethernet"),
					("Optional I/O", "Wi-Fi 6 + BT 5.3, or Wi-Fi 5 + BT 4.2; applicator card"),
					("Size / weight", "19.5 × 13.25 × 12.75 in (495 × 336 × 324 mm); 40 lb / 18.14 kg"),
					("Power", "100–240 VAC, 50–60 Hz, ENERGY STAR, auto-detect PFC"),
					("Climate", "TT 5–40 °C; DT 0–40 °C; 20–85% RH non-condensing"),
				],
			),
		],
	)

	doc.set(
		"applications",
		[
			{
				"title": "Shipping and receiving",
				"description": "Carton, shipper and SSCC-style labels at DC speed.",
				"image": warehouse,
				"image_alt": "ZT421 printing a warehouse shipping label",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Packaging and pallet labels",
				"description": "Case and pallet IDs on packing lines — 6.6-inch width for large formats.",
				"image": packaging,
				"image_alt": "ZT421 case labelling next to a packed carton",
				"industry_link": "packaging",
				"sort_order": 2,
			},
			{
				"title": "Retail distribution",
				"description": "Store replenishment and compliance labels for retail DCs.",
				"image": retail,
				"image_alt": "ZT421 in a retail distribution setting",
				"industry_link": "retail",
				"sort_order": 3,
			},
			{
				"title": "Manufacturing identification",
				"description": "WIP, component and compliance labels on the shop floor.",
				"image": manufacturing,
				"image_alt": "ZT421 printing a manufacturing work-order label",
				"industry_link": "steel",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Unbox and basic setup (ZT400 Series)",
				"body": (
					"Official Zebra film is shot on a ZT411 — the same ZT400 chassis and "
					"load path as ZT421. Install Zebra Setup Utilities before USB, then "
					"power on. A USB A-to-B cable is not in the box."
				),
				"video_url": VIDEO_SETUP,
				"image": front,
				"image_alt": "Zebra ZT421 industrial printer front view",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Load media and ribbon",
				"body": (
					"ZT411 / ZT421 share the side-loading, colour-coded path. Ribbon is "
					"coated-side-out on the standard spindle and should be wider than the "
					"media to protect the printhead. This clip is a distributor how-to, "
					"not a Zebra HQ product film."
				),
				"video_url": VIDEO_LOAD,
				"image": window,
				"image_alt": "Zebra ZT421 with media roll visible in the side window",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Calibrate media and ribbon sensors",
				"body": (
					"Official Zebra ZT400 how-to: set gap/notch or black-mark, transmissive "
					"or reflective sensor, then run media/ribbon calibration after a media "
					"change. Auto-calibrate on power-up or when the head is closed is standard."
				),
				"video_url": VIDEO_CAL,
				"image": angle,
				"image_alt": "Zebra ZT421 ready for media calibration",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "203 dpi, 300 dpi, cutter or RFID",
				"body": (
					"This item is 203 dpi without cutter or RFID. Order RET.SYS.ZEB.4943 "
					"for 300 dpi. A cutter, peeler, rewind or Wi-Fi card is a separate "
					"option. RFID encode is a different ZT421 configuration — do not assume "
					"it on 3626. 600 dpi exists only on ZT411."
				),
				"image": closed,
				"image_alt": "Zebra ZT421 closed industrial chassis",
				"link_label": "Request a Quote",
				"link_href": f"/products/{SLUG}/quote",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Labels, ribbons and support in KSA",
				"body": (
					"Printechs matches Zebra Certified labels and 450 m ribbons to the "
					"pack, sets sensors and first formats, and services ZT421 in Riyadh, "
					"Jeddah and Dammam. Pair with a warehouse PDA such as Memor 12 when "
					"you need scan-and-print on the same dock."
				),
				"image": warehouse,
				"image_alt": "ZT421 shipping-label station in a warehouse",
				"link_label": "Talk to a specialist",
				"link_href": "/contact",
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Network or USB setup, first format, sensor position and calibration.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Labels & ribbons",
				"description": "Zebra-width media and 450 m coated-side-out ribbon for 6.6-inch jobs.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Service",
				"description": "Printheads, platen, OneCare plans and on-site support in KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Colour-touch menus, media/ribbon load and everyday calibration.",
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
			{"item_description": "ZT421 industrial printer (203 dpi, colour display, this SKU)", "sort_order": 1},
			{"item_description": "Power cord", "sort_order": 2},
			{"item_description": "Quick-start guide", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])

	related = [
		row
		for row in (
			related_by_slug("datalogic-memor-12", 1),
			related_by_slug("datalogic-memor-17", 2),
		)
		if row
	]
	doc.set("related_products", related)

	doc.set(
		"faq_items",
		[
			{
				"question": "Which ZT421 is on this page?",
				"answer": (
					"RET.SYS.ZEB.3626 — 203 dpi, colour display, RTC, EPL/ZPL/ZPL II, "
					"USB, RS-232, Bluetooth and Ethernet. The 300 dpi printer is "
					"RET.SYS.ZEB.4943."
				),
				"sort_order": 1,
			},
			{
				"question": "How wide and how fast does it print?",
				"answer": (
					"Zebra lists 6.6 inches / 168 mm print width and 12 ips / 305 mm/s. "
					"Media for tear/cutter is 2.00–7.0 inches wide. That is the 6-inch "
					"ZT421, not the 4-inch ZT411."
				),
				"sort_order": 2,
			},
			{
				"question": "Does it include Wi-Fi, a cutter or RFID?",
				"answer": (
					"No. This kit is wired Ethernet plus Bluetooth 4.1. Wi-Fi 5/6, peeler, "
					"cutter, rewind and RFID encode are options. Do not order 3626 if you "
					"need those built in."
				),
				"sort_order": 3,
			},
			{
				"question": "What is in the box?",
				"answer": (
					"Printer, power cord and quick-start guide. Zebra does not include a "
					"USB A-to-B cable. Install Zebra Setup Utilities before you connect USB."
				),
				"sort_order": 4,
			},
			{
				"question": "Do you supply labels and support in Saudi Arabia?",
				"answer": (
					"Yes. Printechs supplies ZT421, matched labels and ribbons, installation "
					"and after-sales service in Riyadh, Jeddah and Dammam."
				),
				"sort_order": 5,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()

	if frappe.db.exists("Item", NAME):
		item = frappe.get_doc("Item", NAME)
		if item.image != card:
			item.db_set("image", card, update_modified=False)

	frappe.db.commit()
	print(f"Filled and published {doc.name} → /products/{doc.slug}")
	return doc.name
