# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.DLG.4708 — Datalogic Memor 17.

Official family page:
https://www.datalogic.com/eng/retail-transportation-logistics-healthcare-gs1-digital-link/mobile-computers/memor-12-17-pd-1102.html
Datasheet: DS-MEMOR12-17-EN Revision A 20252301.

This ERP Item is the Memor 17 6 GB / 64 GB Wi-Fi 6E + 5G full-touch PDA.
Do not advertise Memor 12-only (no 5G) or Memor 17 HC-only features as standard.
128 GB flash and Android 15 are family options — this SKU is 64 GB / Android 13.
Safe Swap and barometer are Memor 17 features.
"""

from pathlib import Path
from shutil import copy2
from urllib.parse import quote
from urllib.request import Request, urlopen

import frappe

NAME = "RET.SYS.DLG.4708"
SLUG = "datalogic-memor-17"
VIDEO_URL = "https://youtu.be/YTrq-KObWho"
CHANGE_VIDEO = "https://youtu.be/Sfx_y3peb6Y"
GS1_VIDEO = "https://youtu.be/Hd0NZLkkA7M"
STORE_VIDEO = "https://youtu.be/pjezQXMf1jo"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-memor-12-17-combo.png": "/upload/products/Memor12-17_combo.png",
	"datalogic-memor-12-17-slim.jpg": "/upload/prod_line/memor 12-17/slim-and-robust-2.jpg",
	"datalogic-memor-12-17-gs1.jpg": "/upload/prod_line/memor 12-17/GS1.jpg",
	"datalogic-memor-12-17-swap.jpg": "/upload/prod_line/memor 12-17/wualcomm-+-swap.jpg",
	"datalogic-memor-12-17-charging.jpg": "/upload/prod_line/memor 12-17/charging-+-nfc.jpg",
	"datalogic-memor-12-17-mobility.jpg": "/upload/prod_line/memor 12-17/mobility-+-sostenibilità-+-eoc.jpg",
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
	path = OFFICIAL_IMAGES[filename]
	return download_file(filename, DATALOGIC_HOST + quote(path, safe="/:+"))


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


def fill_datalogic_memor_17():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)

	hero = doc.hero_image or "/files/Memor17_front.jpg"
	card = doc.card_image or hero
	combo = official_image("datalogic-memor-12-17-combo.png")
	slim = official_image("datalogic-memor-12-17-slim.jpg")
	gs1 = official_image("datalogic-memor-12-17-gs1.jpg")
	swap = official_image("datalogic-memor-12-17-swap.jpg")
	charging = official_image("datalogic-memor-12-17-charging.jpg")
	mobility = official_image("datalogic-memor-12-17-mobility.jpg")
	warehouse = copy_public_image("industry-warehouse-logistics.jpg")
	fashion = copy_public_image("industry-fashion.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")

	doc.display_name = "Datalogic Memor 17"
	doc.website_product_name = "Datalogic Memor 17"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "FULL-TOUCH MOBILE COMPUTER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Enterprise-grade power in a pocket-sized design"
	doc.short_description = (
		"Datalogic Memor 17 is the 5G full-touch PDA in the Memor 12-17 family — Datalogic’s "
		"thinnest enterprise device for store floor, last-mile and light warehouse work. "
		"A 6\" FHD+ Gorilla Glass 7 display, Halogen Green Spot scanning, GS1 Digital Link, "
		"Wi-Fi 6E + 5G and a Safe Swap 4,000 mAh pack fit a 13.5 mm, 245 g body."
	)
	doc.long_description = (
		"<p>Memor 17 is the cellular model in Datalogic’s Memor 12-17 full-touch family. "
		"It is built for front-facing retail, transportation &amp; logistics and healthcare "
		"tasks — price check, assisted selling, shelf work, proof of delivery — not for "
		"high-bay industrial scanning (use Falcon or Skorpio there).</p>"
		"<p>This Printechs item is the black Memor 17 full-touch PDA with standard-range "
		"2D imager, Green Spot, 13 MP rear / 8 MP front cameras, Wi-Fi 6E + 5G, "
		"6 GB RAM / 64 GB flash and a 4,000 mAh Safe Swap battery. The family also offers "
		"128 GB flash and Memor 17 HC (white, healthcare) as separate configurations.</p>"
		"<p>The 6.0\" FHD+ (1080 × 2160) LTPS display is 450 nits with Gorilla Glass 7. "
		"Halogen DE2121-DL plus DeepSight reads damaged or poorly lit codes; the platform "
		"is GS1 Digital Link ready. Qualcomm QCx4490 (2.4 GHz) and optional Swap memory "
		"(+2 GB virtual RAM from flash) keep apps moving.</p>"
		"<p>Charge by USB-C, wired cradle or Qi EPP 7 W wireless. Multi-side NFC supports "
		"contactless payments and Apple ECP. Enterprise Battery Saver can cut consumption "
		"by up to 20%. Safe Swap (Memor 17 only) protects data while the pack is changed.</p>"
		"<p>Android 13 GMS on this SKU; the family also lists Android 15 GMS options and a "
		"published path to Android 19 with 4+4 years of hardware and software support. "
		"Printechs supplies and stages Memor 17 in Saudi Arabia — Riyadh, Jeddah and Dammam.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Memor 17 full-touch 5G mobile computer"
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"6\" FHD+ · Gorilla Glass 7\n"
		"Wi-Fi 6E + 5G\n"
		"GS1 Digital Link ready\n"
		"Safe Swap 4,000 mAh"
	)
	doc.story_heading = "Pocket-sized Android for the store floor and the last mile"
	doc.visual_story_heading = "Memor 17 in retail and on the move"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_title = "Memor 17"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Thinnest Datalogic full-touch PDA with 5G, Wi-Fi 6E, Green Spot 2D, "
		"GS1 Digital Link and a Safe Swap 4,000 mAh battery."
	)
	doc.card_image = card

	doc.final_cta_heading = "Specify Memor 17 for store and field teams"
	doc.final_cta_description = (
		"Printechs can confirm 64 GB vs 128 GB, standard vs HC, docks (wired or wireless) "
		"and MDM staging for Memor 17 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Memor 17 Full-Touch 5G PDA Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Memor 17 pocket-sized full-touch PDA: 6\" FHD+, Wi-Fi 6E + 5G, Green Spot "
		"2D, GS1 Digital Link and Safe Swap battery. Supplied by Printechs in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "device",
				"title": "Thinnest Datalogic PDA",
				"description": (
					"13.5 mm and 245 g with a firm grip for all-day store and delivery work — "
					"enterprise scanning without a brick in the pocket."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Green Spot + DeepSight + GS1",
				"description": (
					"Halogen DE2121-DL with Green Spot and DeepSight reads dirty or poorly lit "
					"codes. The family is GS1 Digital Link ready for the next pack codes."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E and 5G",
				"description": (
					"Memor 17 adds 5G FR1, dual-band GNSS, Nano SIM + eSIM and a barometer "
					"on top of Wi-Fi 6E, Bluetooth 5.3 and multi-side NFC."
				),
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "Safe Swap and wireless charge",
				"description": (
					"4,000 mAh pack changes without killing the session (Memor 17 Safe Swap). "
					"USB-C, wired cradles or Qi EPP 7 W wireless — plus up to 20% less drain "
					"with Enterprise Battery Saver."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Store-floor ergonomics",
				"image": slim,
				"image_alt": "Memor 12-17 slim full-touch PDA held in a retail aisle",
				"caption": "Ultra-thin body for price checks, assisted selling and shelf work.",
				"sort_order": 1,
			},
			{
				"label": "GS1 Digital Link",
				"image": gs1,
				"image_alt": "Memor scanning a grocery pack with GS1 Digital Link product data",
				"caption": "GS1 Digital Link ready — lot, expiry and product data on the shelf.",
				"sort_order": 2,
			},
			{
				"label": "Charge or take payment",
				"image": charging,
				"image_alt": "Memor 17 wireless charging cradle and multi-side NFC tap-to-pay",
				"caption": "USB-C, wired or wireless dock — and multi-side NFC for tap-to-pay.",
				"sort_order": 3,
			},
			{
				"label": "Qualcomm + Swap memory",
				"image": swap,
				"image_alt": "Memor 17 Qualcomm QCM4490 processor and Swap memory",
				"caption": "QCx4490 plus optional +2 GB Swap memory for faster multitasking.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "display",
				"title": "6.0\" FHD+",
				"description": "1080 × 2160 · 450 nits · Gorilla Glass 7",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Halogen DE2121-DL",
				"description": "Green Spot · DeepSight · GS1 Digital Link",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E + 5G",
				"description": "Bluetooth 5.3 · NFC · eSIM",
				"sort_order": 3,
			},
			{
				"icon": "android",
				"title": "Android 13 GMS",
				"description": "Path to 19 · 6 GB / 64 GB this SKU",
				"sort_order": 4,
			},
			{
				"icon": "battery",
				"title": "4,000 mAh",
				"description": "Safe Swap · Qi EPP 7 W wireless",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "1-year warranty",
				"description": "4+4 year support path · EASEOFCARE",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"This configuration",
			[
				("Printechs item", "RET.SYS.DLG.4708 — Memor 17 full-touch PDA"),
				("Memory / storage", "6 GB RAM / 64 GB UFS (128 GB is a separate family SKU)"),
				("Wireless", "Wi-Fi 6E + 5G, NFC, PTT"),
				("Imager", "Standard-range 2D with Green Spot"),
				("Cameras", "13 MP rear autofocus; 8 MP front"),
				("Battery", "4,000 mAh Safe Swap"),
				("Colour", "Black (Memor 17 HC white is a different SKU)"),
			],
		),
		(
			"Computer",
			[
				("Family", "Memor 12-17 full-touch PDA; Memor 17 is the 5G model"),
				("Processor", "Qualcomm QCx4490 octa-core 2.4 GHz"),
				("Swap memory", "Optional +2 GB virtual RAM from flash (setting)"),
				("Expansion", "MicroSD up to 2 TB"),
				("OS (this SKU)", "Android 13 GMS"),
				("OS (family)", "Android 13 or 15 GMS options; upgradeable to Android 19"),
				("Support window", "Official page: 4+4 years hardware and software support"),
				("Display", "6.0\" LTPS 18:9 FHD+ 1080 × 2160; 450 nits"),
				("Touch", "5-point capacitive; Gorilla Glass 7; gloves and stylus"),
				("Keys", "2 side scan keys; PTT; power; volume; 3 Android soft keys"),
				("Size", "165 × 76.7 × 13.5 mm / 6.49 × 3.0 × 0.53 in"),
				("Weight", "245 g / 8.6 oz with battery"),
			],
		),
		(
			"Scanning & sensors",
			[
				("Scan engine", "Halogen DE2121-DL 1D/2D; Green Spot good-read"),
				("Decoding", "DeepSight for damaged, dirty or poorly lit codes"),
				("Next-gen IDs", "GS1 Digital Link ready"),
				("Typical scan", "About 1 m class standard-range (family graphic)"),
				("Memor 17 sensors", "Barometer / Z-location (Memor 17 only)"),
				("Other sensors", "Accelerometer, gyro, ambient light, proximity, magnetometer"),
			],
		),
		(
			"Wireless (Memor 17)",
			[
				("WLAN", "Wi-Fi 6E 802.11 a/b/g/n/ac/ax; 2.4 / 5 / 6 GHz; 2×2 MIMO"),
				("WLAN security", "WPA3 Enterprise 192-bit supported"),
				("Bluetooth", "5.3 Classic and BLE"),
				("NFC", "Tags 1–5; card emulator; contactless pay; Apple ECP"),
				("WWAN", "LTE-A / 5G FR1, 3GPP Rel.16; VoLTE, VoNR, Wi-Fi calling"),
				("SIM", "1 Nano SIM + 1 eSIM"),
				("GNSS", "Dual-band GPS, Galileo, BeiDou; A-GPS"),
			],
		),
		(
			"Power, I/O & charging",
			[
				("Battery", "Swappable Li-Ion 3.87 V; 4,000 mAh typical (14.98 Wh)"),
				("Safe Swap", "Memor 17 only — keeps application data during battery change"),
				("Wireless charge", "WPC Qi EPP compliant, 7 W"),
				("Other charge", "USB-C fast top-up; wired enterprise cradles"),
				("Battery saver", "Enterprise Battery Saver — up to 20% less consumption"),
				("Interfaces", "USB 3.2 Gen1 host/client Type-C; SuperSpeed USB 2.0 bottom I/O"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Family sealing", "IP65 and IP68 with battery (latest family datasheet)"),
				("SKU note", "Some catalog lines list IP65/IP67; confirm the exact unit"),
				("Drop without boot", "Multiple 1.3 m to concrete, operating temp, MIL-STD-810H"),
				("Drop with boot", "Multiple 1.5 m, −10 to 50 °C, MIL-STD-810H"),
				("Tumble", "500 × 0.5 m without boot; 500 × 1.0 m with boot"),
				("Operating temp", "−10 to 50 °C"),
				("Storage / transport", "−40 to 70 °C"),
				("ESD", "15 kV air / 8 kV contact"),
				("Compliance", "EU RoHS"),
				("Warranty", "1-year factory warranty"),
			],
		),
		(
			"Software & management",
			[
				("Mobility Suite", "Shield, Launcher, Enterprise Browser, Integrity KIT"),
				("Staging", "Scan2Deploy Studio, OEMConfig, AE QR enrollment"),
				("SDKs", "Java, Kotlin, Xamarin, .NET MAUI, JavaScript"),
				("UEM / EMM", "SOTI, Workspace ONE, Intune, 42Gears, Ivanti, OEMConfig"),
				("TE / PTT", "Ivanti Velocity, StayLinked Smart TE, Zello PTT"),
				("Extras", "SoftSpot, Snap OCR, QuickBoard, Wi-Fi Guard, Battery Manager"),
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
				"title": "In-store retail",
				"description": (
					"Price check, assisted selling, shelf replenishment, loyalty lookup and "
					"queue-busting on a pocket-sized 5G PDA."
				),
				"image": slim,
				"image_alt": "Memor 17 used for in-store retail operations",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Fashion and click-and-collect",
				"description": "Stock lookup, endless-aisle selling and order fulfilment on the shop floor.",
				"image": fashion,
				"image_alt": "Fashion retail inventory with a mobile computer",
				"industry_link": "fashion",
				"sort_order": 2,
			},
			{
				"title": "Last-mile and T&L",
				"description": (
					"Proof of delivery, ticketing, baggage and postal work with 5G, GNSS and PTT."
				),
				"image": warehouse,
				"image_alt": "Transportation and logistics mobile scanning",
				"industry_link": "warehouse-logistics",
				"sort_order": 3,
			},
			{
				"title": "Healthcare (standard or HC)",
				"description": (
					"eMR, bed-side ID and lab tasks. Specify Memor 17 HC (white) when you need "
					"the healthcare-certified housing — it is a different SKU."
				),
				"image": pharma,
				"image_alt": "Healthcare and pharmacy mobile identification",
				"industry_link": "pharmaceutical",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Watch Memor 12-17 — enterprise power, pocket size",
				"body": (
					"Official Datalogic film: Enterprise-Grade Power in a Pocket-Sized Design. "
					"Memor 17 is the 5G model in that family — same slim full-touch body as "
					"Memor 12, with cellular, GNSS and Safe Swap for store and field teams."
				),
				"video_url": VIDEO_URL,
				"image": combo,
				"image_alt": "Datalogic Memor 12 and Memor 17 full-touch PDAs",
				"link_label": "Change is Here on YouTube",
				"link_href": CHANGE_VIDEO,
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Ultra-thin, still enterprise-rugged",
				"body": (
					"Datalogic’s thinnest device: 13.5 mm, 245 g, Gorilla Glass 7 and MIL-STD-810H "
					"drops (1.3 m without boot, 1.5 m with boot). Family sealing is IP65/IP68 "
					"with battery; some catalog SKUs list IP65/IP67 — we confirm the unit at order."
				),
				"image": slim,
				"image_alt": "Slim Memor 12-17 PDA in a supermarket aisle",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "GS1 Digital Link, Green Spot and DeepSight",
				"body": (
					"Halogen DE2121-DL with Green Spot and DeepSight keeps reads reliable on "
					"damaged or poorly lit labels. Memor 12-17 is GS1 Digital Link ready — "
					"the same Datalogic retail portfolio as Magellan and Gryphon."
				),
				"video_url": GS1_VIDEO,
				"image": gs1,
				"image_alt": "Memor 17 GS1 Digital Link shelf scanning",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "5G, Swap memory and Qualcomm 4490",
				"body": (
					"Qualcomm QCx4490 plus optional Swap memory (+2 GB virtual RAM) keep "
					"POS, WMS and browser apps in play. Memor 17 adds 5G, dual-band GNSS, "
					"eSIM and a barometer; Memor 12 stays Wi-Fi 6E only."
				),
				"image": swap,
				"image_alt": "Memor 17 Qualcomm QCM4490 and Swap memory",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Charge three ways — or take payment",
				"body": (
					"USB-C for a quick top-up, wired cradles for data, or Qi EPP 7 W wireless "
					"docks that have no pins to corrode. Multi-side NFC handles tap-to-pay "
					"and Apple ECP. Safe Swap keeps the session alive while you change the pack."
				),
				"image": charging,
				"image_alt": "Memor wireless charging dock and multi-side NFC payment",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Android path to 19 and Saudi Arabia support",
				"body": (
					"This SKU ships Android 13 GMS. The family lists Android 15 options and a "
					"path to Android 19 with 4+4 years of support, Mobility Suite, Shield and "
					"EASEOFCARE. Eco-friendly accessories and packaging are part of the official story.\n\n"
					"Printechs stages MDM, docks and apps for retailers and 3PLs in Riyadh, "
					"Jeddah and Dammam. Watch Datalogic’s Intelligent Store film for the wider context."
				),
				"video_url": STORE_VIDEO,
				"image": mobility,
				"image_alt": "Memor 12-17 Android support, EASEOFCARE and sustainable accessories",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "device",
				"title": "SKU & accessory selection",
				"description": "Confirm 64 vs 128 GB, standard vs HC, trigger handle, holster and wired or wireless docks.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Device staging",
				"description": "Scan2Deploy, OEMConfig, Zero-Touch and app load before the devices hit the floor.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "POS, WMS and ERP",
				"description": "Connect to Modern POS, WMS, ERPNext and terminal emulation as required.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Rollout, EASEOFCARE, Shield and after-sales support in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "Memor 17 full-touch PDA (this item: 6 GB / 64 GB, Wi-Fi 6E + 5G)", "sort_order": 1},
			{"item_description": "4,000 mAh Safe Swap wireless-charging battery", "sort_order": 2},
			{"item_description": "Handstrap (as supplied on this configuration)", "sort_order": 3},
			{"item_description": "Google Mobile Services", "sort_order": 4},
			{"item_description": "Optional wired or wireless single / 4-slot docks, holster and trigger handle", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4648", 1),
			related_product_row("RET.SYS.DLG.5029", 2),
			related_product_row("datalogic-skorpio-x40-x45", 3),
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
				"question": "What is the Datalogic Memor 17?",
				"answer": (
					"The 5G full-touch model in the Memor 12-17 family — Datalogic’s thinnest "
					"enterprise PDA for store, last-mile and light warehouse work."
				),
				"sort_order": 1,
			},
			{
				"question": "How is Memor 17 different from Memor 12?",
				"answer": (
					"Same slim 6\" body and Wi-Fi 6E. Memor 17 adds 5G, GNSS, eSIM, barometer "
					"and Safe Swap. Memor 12 is Wi-Fi only. This page is Memor 17 (RET.SYS.DLG.4708)."
				),
				"sort_order": 2,
			},
			{
				"question": "Is this the healthcare Memor 17 HC?",
				"answer": (
					"No. This item is the black standard Memor 17. Memor 17 HC is a separate "
					"white healthcare-certified SKU (for example 944950006 / 944950023)."
				),
				"sort_order": 3,
			},
			{
				"question": "Does it read GS1 Digital Link?",
				"answer": (
					"Yes. The Memor 12-17 family is specified GS1 Digital Link ready, with "
					"Halogen DE2121-DL, Green Spot and DeepSight."
				),
				"sort_order": 4,
			},
			{
				"question": "What memory and Android version ship on this item?",
				"answer": (
					"6 GB RAM / 64 GB flash and Android 13 GMS. 128 GB and Android 15 are "
					"family options on other SKUs. Swap memory can add +2 GB virtual RAM. "
					"The published OS path is Android 19."
				),
				"sort_order": 5,
			},
			{
				"question": "What is the IP rating?",
				"answer": (
					"The latest family datasheet is IP65 and IP68 with battery. Some catalog "
					"SKUs list IP65/IP67. We confirm sealing on the exact unit at quote."
				),
				"sort_order": 6,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"1-year factory warranty. Official page cites 4+4 years of hardware and "
					"software support; EASEOFCARE and Shield extend service and Android patches."
				),
				"sort_order": 7,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
