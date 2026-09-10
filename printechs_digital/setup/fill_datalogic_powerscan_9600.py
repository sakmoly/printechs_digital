# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic PowerScan 9600 Series (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail-manufacturing-transportation-logistics-healthcare-gs1-digital-link/handheld-scanners/powerscan-9600-series-pd-917.html
Datasheet: DS-POWERSCAN9600-EN Revision B.

Industrial / warehouse handheld — not a retail checkout scanner.
RFID series is North America / Europe only; do not sell as available in KSA.
Digimarc is specified on HP and DC models only.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

SLUG = "datalogic-powerscan-9600"
VIDEO_URL = "https://youtu.be/OHKoHXkGmVA"
GS1_VIDEO = "https://youtu.be/Hd0NZLkkA7M"
CONNECT_VIDEO = "https://youtu.be/XCIiJsDV8p0"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-powerscan-9600-series.png": "/upload/products/PowerScan%209600%20series.png",
	"datalogic-powerscan-9600-connectivity.jpg": "/upload/prod_line2/PowerScan9600/1.jpg",
	"datalogic-powerscan-9600-wlc.jpg": "/upload/prod_line2/PowerScan9600/2.jpg",
	"datalogic-powerscan-9600-star.jpg": "/upload/prod_line2/PowerScan9600/3.jpg",
	"datalogic-powerscan-9600-display.jpg": "/upload/prod_line2/PowerScan9600/4.jpg",
}


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


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
	return download_file(filename, DATALOGIC_HOST + OFFICIAL_IMAGES[filename])


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


def get_or_create():
	existing = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = SLUG
	doc.website_product_name = "Datalogic PowerScan 9600 Series"
	doc.display_name = "Datalogic PowerScan 9600 Series"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic PowerScan 9600 industrial handheld scanner."
	doc.long_description = "<p>Datalogic PowerScan 9600 industrial handheld scanner.</p>"
	doc.hero_image = official_image("datalogic-powerscan-9600-series.png")
	return doc


def fill_datalogic_powerscan_9600():
	doc = get_or_create()

	hero = official_image("datalogic-powerscan-9600-series.png")
	connect = official_image("datalogic-powerscan-9600-connectivity.jpg")
	wlc = official_image("datalogic-powerscan-9600-wlc.jpg")
	star = official_image("datalogic-powerscan-9600-star.jpg")
	display = official_image("datalogic-powerscan-9600-display.jpg")
	warehouse = copy_public_image("industry-warehouse-logistics.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")

	# Intentionally no Item — link later under ERP Item Link when the Item exists.
	doc.item = None
	doc.website_product_name = "Datalogic PowerScan 9600 Series"
	doc.display_name = "Datalogic PowerScan 9600 Series"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Barcode Scanners"
	doc.category_label = "INDUSTRIAL HANDHELD SCANNER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "When top flexibility meets extreme reliability"
	doc.short_description = (
		"The Datalogic PowerScan 9600 Series is a range-topping industrial handheld imager "
		"for warehouse, manufacturing and logistics. IP65/IP67 sealing, 2.5 m drop rating and "
		"a 10-million-hit trigger sit alongside inductive wireless charging, modular industrial "
		"I/O and GS1 Digital Link — so Datalogic is as strong on the shop floor as at checkout."
	)
	doc.long_description = (
		"<p>PowerScan 9600 is Datalogic’s flagship industrial handheld for traceability on the "
		"shop floor, in the warehouse and across transportation &amp; logistics. It is built for "
		"receiving, put-away, picking, sorting and WIP — not for the POS lane.</p>"
		"<p>The housing is IP65 and IP67, survives 50 drops from 2.5 m at 20 °C, and the trigger "
		"is tested to 10 million hits. Cordless models charge inductively in the cradle, so dirt "
		"and bent contacts no longer kill the fleet.</p>"
		"<p>Choose Standard Range (single camera), High Performance (dual camera, longer depth "
		"of field, 2.5 mil 1D) or Document Capture (colour images for QC and signatures). "
		"Connectivity is modular: RS-232, USB, USB-C, Ethernet, EtherNet/IP or PROFINET in the "
		"cradle or inline on corded units — swap the module when the line changes.</p>"
		"<p>PD9630 is corded. PM9600 uses Datalogic STAR Cordless System (433 / 910 MHz, up to "
		"150 m open air on 433 MHz). PBT9600 is Bluetooth 5.0 up to 100 m. PM9600-D/DK add a "
		"1.8\" OLED and 4- or 16-key keypad for host feedback at the point of work.</p>"
		"<p>Auto Range (AR) and DPX (direct part mark) variants extend the same platform for "
		"distance reading and DPM traceability. The RFID series is sold only in North America "
		"and Europe and is not offered as a standard Saudi Arabia configuration.</p>"
		"<p>Printechs specifies and supports PowerScan 9600 in Saudi Arabia — Riyadh, Jeddah "
		"and Dammam — including optic, radio, cradle protocol and EASEOFCARE.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = (
		"Datalogic PowerScan 9600 Series corded and cordless industrial handheld scanners"
	)
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"IP65 / IP67 industrial\n"
		"2.5 m drop · 10M trigger\n"
		"STAR / Bluetooth / corded\n"
		"3-year factory warranty"
	)
	doc.story_heading = "Industrial scanning for warehouse, shop floor and logistics"
	doc.visual_story_heading = "PowerScan 9600 on the warehouse floor"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "PowerScan 9600"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Ultra-rugged industrial handheld for warehouse and manufacturing: IP65/IP67, "
		"inductive charging, modular industrial I/O and GS1 Digital Link."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify PowerScan 9600 for your warehouse or line"
	doc.final_cta_description = (
		"Printechs can confirm SR, HP, DC, AR or DPX optics, corded vs STAR vs Bluetooth, "
		"and the cradle protocol for sites in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic PowerScan 9600 Industrial Scanner Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic PowerScan 9600 Series industrial handheld scanner: IP65/IP67, 2.5 m drop, "
		"STAR or Bluetooth, modular Ethernet/PROFINET and GS1 Digital Link. From Printechs in KSA."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "rugged",
				"title": "Built for the warehouse",
				"description": (
					"IP65 and IP67 sealing, 50 drops from 2.5 m and a trigger rated to 10 million "
					"hits — the yellow/black PowerScan that belongs on the shop floor, not the till."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "SR, HP or Document Capture",
				"description": (
					"Single-camera Standard Range, dual-camera High Performance (2.5 mil 1D) or "
					"colour Document Capture for QC photos and signatures — about 20% faster reads."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Industrial I/O, not a dongle",
				"description": (
					"Swap RS-232, USB, USB-C, Ethernet, EtherNet/IP or PROFINET in the cradle or "
					"inline. Talk to a PC, IPC, tablet or PLC without a third-party box."
				),
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "Inductive charge, fewer failures",
				"description": (
					"Wireless charging removes dirty contacts — the usual cordless failure. "
					"3350 mAh Li-Ion, about 80,000 reads, plus cradle health for planned maintenance."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Warehouse STAR radio",
				"image": star,
				"image_alt": "Datalogic PowerScan PM9600 STAR cordless scanner in a warehouse aisle",
				"caption": "STAR Cordless System keeps operators moving across receiving and pick faces.",
				"sort_order": 1,
			},
			{
				"label": "Industrial connectivity",
				"image": connect,
				"image_alt": "PowerScan 9600 corded scanner and modular industrial cradle interfaces",
				"caption": "Exchangeable modules: serial, USB, USB-C, Ethernet, EtherNet/IP, PROFINET.",
				"sort_order": 2,
			},
			{
				"label": "Wireless charging",
				"image": wlc,
				"image_alt": "Datalogic PowerScan 9600 inductive wireless charging in the cradle",
				"caption": "No pins to bend or corrode — inductive charge and a healthier fleet.",
				"sort_order": 3,
			},
			{
				"label": "OLED + keypad",
				"image": display,
				"image_alt": "PowerScan PM9600-DK with OLED display and 16-key keypad",
				"caption": "PM9600-D/DK: host messages on a 1.8\" OLED with 4 or 16 keys.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "rugged",
				"title": "IP65 / IP67",
				"description": "50× 2.5 m drops @ 20 °C · 10M trigger",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "1280 × 800",
				"description": "White LED · Green Spot / 3GL · vibration",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Industrial I/O",
				"description": "RS-232 · USB · Ethernet · PROFINET",
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "3350 mAh",
				"description": "~80,000 reads · inductive cradle charge",
				"sort_order": 4,
			},
			{
				"icon": "display",
				"title": "OLED + keys",
				"description": "PM9600-D 4 keys · DK 16 keys",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "3-year warranty",
				"description": "Factory warranty · EASEOFCARE options",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Scanner",
			[
				("Family", "PowerScan 9600 industrial handheld 2D imager"),
				("Corded", "PD9630"),
				("STAR cordless", "PM9600 — Datalogic STAR 433 / 910 MHz"),
				("Bluetooth cordless", "PBT9600 — Bluetooth 5.0, Class 1/2/3"),
				("Optics", "SR single camera; HP dual camera; DC colour document capture"),
				("Series variants", "Auto Range (AR); DPX for DPM. RFID is NA/Europe only"),
				("Imager", "1280 × 800 pixels"),
				("Illumination", "White LED reading light"),
				("Aiming", "630–680 nm VLD"),
				("Indicators", "3GL, Green Spot, dual LEDs, beeper, vibration"),
				("Field of view", "SR and HP: 38° H × 24° V"),
				("Print contrast", "15% minimum"),
				("Reading angle", "Pitch ±52°; roll 360°; skew ±52°"),
				("Resolution SR/DC", "1D 3 mil; 2D 6 mil"),
				("Resolution HP", "1D 2.5 mil; 2D 4 mil"),
				("Colours", "Yellow / black"),
			],
		),
		(
			"Decoding",
			[
				("1D / linear", "All standard 1D including GS1 DataBar linear"),
				("2D codes", "Aztec, Han Xin, Data Matrix, MaxiCode, QR, Micro QR, Dot Code"),
				("Stacked", "PDF417, MicroPDF417, MacroPDF, GS1 DataBar stacked/composites"),
				("Postal", "Australian, British, China, IMB, Japan, KIX, Planet, Postnet, RM4SCC"),
				("Digital watermarks", "Digimarc Barcodes on HP and DC models only"),
				("Next-gen IDs", "GS1 Digital Link ready with the Datalogic GS1 portfolio"),
			],
		),
		(
			"Wireless, battery & display",
			[
				("STAR range", "433 MHz: 150 m low / 100 m high. 910 MHz: 230 m / 180 m"),
				("STAR topology", "Point-to-point or multi-point; up to 16 readers per receiver"),
				("Bluetooth", "5.0; SPP and HID; up to 100 m open air to the base"),
				("Battery", "Li-Ion 3350 mAh; ~80,000 reads per charge"),
				("Charge time", "2.5 h to 95%, 3.2 h to 100% at 12 VDC external power"),
				("Charging", "Inductive wireless charging — no battery contacts"),
				("Display", "PM9600-D/DK: 1.8\" OLED, user-selectable fonts"),
				("Keyboard", "PM9600-D 4 keys; PM9600-DK 16 keys, configurable"),
			],
		),
		(
			"Interfaces & power",
			[
				("Host interfaces", "RS-232, USB, USB-C, Ethernet, EtherNet/IP, PROFINET"),
				("Architecture", "Exchangeable cradle modules; inline modules on corded"),
				("Corded current", "SR 200 mA @ 5 V; HP/DC 280 mA @ 5 V typical operating"),
				("Corded voltage", "5–30 VDC ±5%"),
				("Cordless power", "Host 5 V or 10–30 VDC; external supply 10–30 VDC"),
				("Configuration", "Datalogic Aladdin (free download)"),
				("POS utilities", "OPOS and JavaPOS utilities (free download)"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Corded size", "19.0 × 14.0 × 7.9 cm / 7.5 × 5.5 × 3.1 in"),
				("Cordless size", "19.7 × 14.9 × 7.9 cm / 7.8 × 5.9 × 3.1 in"),
				("Weight", "PD9630 318 g; PBT9600 415 g; PM9600 425 g; D 445 g; DK 455 g"),
				("Drop", "50 drops from 2.5 m @ 20 °C; 50 from 2.0 m @ −20 °C"),
				("Trigger life", "10 million hits"),
				("Sealing", "Scanner IP67 and IP65; cradle IP65 on specific models"),
				("Ambient light", "0–100,000 lux"),
				("ESD", "20 kV air discharge"),
				("Humidity", "0–95% non-condensing"),
				("Operating temp", "−20 to 50 °C"),
				("Storage / transport", "−40 to 70 °C"),
				("Charging temp", "0–40 °C nominal; 0–35 °C ideal"),
				("Compliance", "China RoHS, EU RoHS, REACH"),
				("Laser / LED", "CDRH Class II / IEC 60825 Class 2; IEC 62471 Exempt"),
				("Warranty", "3-year factory warranty"),
			],
		),
		(
			"Typical depth of field",
			[
				("SR Code 128 5 mil", "6.4–30.9 cm / 2.5–12.2 in"),
				("SR Code 128 40 mil", "5.5–175 cm / 2.2–68.9 in"),
				("SR EAN/UPC 13 mil", "4–67.5 cm / 1.5–26.5 in"),
				("HP Code 128 2.5 mil", "6.3–11.5 cm / 2.5–4.5 in"),
				("HP Code 128 40 mil", "5.5–242.9 cm / 2.1–95.6 in"),
				("HP EAN/UPC 13 mil", "4–120 cm / 1.5–40.2 in"),
				("Note", "DoF depends on symbol length, angle, print quality and light"),
			],
		),
	]

	sort = 1
	for group_title, items in groups:
		for label, value in items:
			if len(value) > 140:
				frappe.throw(f"Spec value too long ({len(value)}): {label}")
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
				"title": "Warehouse receiving, picking and sorting",
				"description": (
					"Rugged cordless scanning across docks, pick faces and sort lanes — STAR or "
					"Bluetooth range with host feedback on OLED models."
				),
				"image": warehouse,
				"image_alt": "Warehouse logistics aisle for PowerScan 9600 handheld scanning",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Manufacturing WIP and shop-floor traceability",
				"description": (
					"Read labels and (with DPX) direct part marks on the line. Modular PROFINET "
					"or EtherNet/IP talks to the PLC without extra gateways."
				),
				"image": packaging,
				"image_alt": "Packaging and manufacturing line barcode traceability",
				"industry_link": "packaging",
				"sort_order": 2,
			},
			{
				"title": "Healthcare device and pack tracking",
				"description": (
					"DPX models target DPM and label codes on instruments and packs. Document "
					"Capture adds colour images for QC."
				),
				"image": pharma,
				"image_alt": "Pharmaceutical and healthcare pack identification",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Retail distribution, not the checkout lane",
				"description": (
					"Back-of-store and DC work — receiving, inventory and outbound — alongside "
					"Magellan and Gryphon at the front end."
				),
				"image": star,
				"image_alt": "PowerScan 9600 cordless scanner used in a distribution warehouse",
				"industry_link": "retail",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Watch PowerScan 9600 — flexibility and reliability",
				"body": (
					"Official Datalogic film: When top flexibility meets extreme reliability. "
					"The 9600 is the range-topping industrial handheld in the PowerScan family — "
					"built for manufacturing, intralogistics and tough warehouse work."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic PowerScan 9600 Series industrial handheld scanners",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Future-proof industrial connectivity",
				"body": (
					"Communication modules sit in the cradle, or inline on the wired scanner. "
					"Configure RS-232, USB, USB-C, Ethernet, EtherNet/IP or PROFINET and change "
					"them in minutes when the network changes — no third-party converter on the line."
				),
				"video_url": CONNECT_VIDEO,
				"image": connect,
				"image_alt": "PowerScan 9600 modular industrial connectivity",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Three optics — plus AR and DPX",
				"body": (
					"Standard Range uses one camera for everyday 1D/2D at normal distances. "
					"High Performance adds a second camera for longer depth of field and 2.5 mil "
					"1D. Document Capture takes colour images for quality control and signatures.\n\n"
					"Auto Range (PD/PM/PBT 9600 AR) stretches distance reading. DPX models add DPM "
					"for automotive, aerospace, tyres, electronics and hospital device tracking."
				),
				"image": hero,
				"image_alt": "PowerScan 9600 SR, HP and Document Capture models",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "STAR, Bluetooth 5.0 and inductive charging",
				"body": (
					"PM9600 uses Datalogic STAR Cordless System with two-way radio and optional "
					"OLED so the host can confirm the scan before the operator walks on. PBT9600 "
					"pairs over Bluetooth 5.0 to a base or any Bluetooth host, up to 100 m.\n\n"
					"Inductive charging and smart-battery health cut the number-one cordless "
					"failure — dirty or bent contacts — and help plan maintenance before a shift fails."
				),
				"image": wlc,
				"image_alt": "PowerScan 9600 inductive wireless charging",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "GS1 Digital Link with the Datalogic portfolio",
				"body": (
					"PowerScan 9600 sits with Magellan, Gryphon and QuickScan as GS1 Digital Link "
					"ready. Digimarc digital watermarks are specified on High Performance and "
					"Document Capture models. White illumination and Green Spot / 3GL keep reads "
					"clear on damaged or dirty codes."
				),
				"video_url": GS1_VIDEO,
				"image": star,
				"image_alt": "PowerScan 9600 GS1-ready industrial scanning",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Saudi Arabia specification and support",
				"body": (
					"Printechs helps choose optic, radio (STAR 433 MHz for typical EMEA sites, or "
					"Bluetooth), keypad/display and cradle protocol for warehouses and plants in "
					"Riyadh, Jeddah and Dammam.\n\n"
					"The PowerScan 9600 RFID series is available only in North America and Europe "
					"— it is not a standard KSA offering. ERP Items can be linked later under "
					"ERP Item Link without changing this URL."
				),
				"image": display,
				"image_alt": "PowerScan PM9600 keypad model for warehouse data entry",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "rugged",
				"title": "Model & optic selection",
				"description": "Confirm PD9630, PM9600 or PBT9600 and SR, HP, DC, AR or DPX for the job.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "Cradle & PLC protocols",
				"description": "RS-232, USB, USB-C, Ethernet, EtherNet/IP or PROFINET — swap the module, keep the gun.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Fleet health",
				"description": "Inductive charge, smart battery and cradle health data for planned downtime.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Rollout, EASEOFCARE and after-sales support in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "PowerScan 9600 scanner (PD9630, PBT9600 or PM9600 — configuration dependent)", "sort_order": 1},
			{"item_description": "Optional BC96xx base / charger with chosen interface module", "sort_order": 2},
			{"item_description": "3350 mAh Li-Ion battery on cordless models", "sort_order": 3},
			{"item_description": "Host cable or industrial protocol module per kit", "sort_order": 4},
			{"item_description": "Optional OLED/keypad housing on PM9600-D and PM9600-DK", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4708", 1),
			related_product_row("datalogic-magellan-9900i", 2),
			related_product_row("RET.SYS.DLG.5031", 3),
		)
		if row
	]
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])

	doc.set(
		"faq_items",
		[
			{
				"question": "What is the Datalogic PowerScan 9600 Series?",
				"answer": (
					"Datalogic’s range-topping industrial handheld 2D imager for warehouse, "
					"manufacturing and logistics. It is IP65/IP67, drop-rated to 2.5 m, and offered "
					"corded (PD9630), STAR cordless (PM9600) or Bluetooth 5.0 (PBT9600)."
				),
				"sort_order": 1,
			},
			{
				"question": "Is this a retail checkout scanner?",
				"answer": (
					"No. PowerScan 9600 is the industrial / warehouse handheld. For POS and "
					"self-checkout use Magellan or Gryphon. PowerScan shares GS1 Digital Link "
					"readiness with that retail portfolio."
				),
				"sort_order": 2,
			},
			{
				"question": "What is the difference between SR, HP and DC?",
				"answer": (
					"Standard Range: one camera for normal-distance 1D/2D. High Performance: dual "
					"camera, longer depth of field, 2.5 mil 1D. Document Capture: colour images for "
					"QC and signatures. Digimarc is on HP and DC only."
				),
				"sort_order": 3,
			},
			{
				"question": "Does it read GS1 Digital Link?",
				"answer": (
					"Yes. PowerScan 9600 is positioned in Datalogic’s GS1 Digital Link portfolio. "
					"Digimarc watermarks are specified on High Performance and Document Capture models."
				),
				"sort_order": 4,
			},
			{
				"question": "STAR or Bluetooth?",
				"answer": (
					"PM9600 STAR is a dedicated two-way radio (433 MHz typical for EMEA, up to "
					"150 m; 910 MHz regional) with optional OLED feedback. PBT9600 is Bluetooth 5.0 "
					"to a base or any Bluetooth host, up to 100 m."
				),
				"sort_order": 5,
			},
			{
				"question": "Is the RFID PowerScan available in Saudi Arabia?",
				"answer": (
					"No. Datalogic lists the 9600 RFID series as available only in North America "
					"and Europe. Specify barcode-only PD, PM or PBT 9600 (including AR and DPX) for KSA."
				),
				"sort_order": 6,
			},
			{
				"question": "What industrial protocols are supported?",
				"answer": (
					"Exchangeable modules cover RS-232, USB, USB-C, Ethernet, EtherNet/IP and "
					"PROFINET — in the cradle or inline on corded scanners."
				),
				"sort_order": 7,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page was published without an ERP Item. When Items are created, link them "
					"on this Website Product under ERP Item Link. The URL stays "
					"/products/datalogic-powerscan-9600."
				),
				"sort_order": 8,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The official datasheet specifies a 3-year factory warranty. EASEOFCARE plans "
					"can extend coverage and service."
				),
				"sort_order": 9,
			},
		],
	)

	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	frappe.db.commit()
	return doc.name
