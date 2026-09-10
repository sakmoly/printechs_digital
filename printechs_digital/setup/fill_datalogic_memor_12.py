# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.DLG.4648 — Datalogic Memor 12.

Official family page (Memor 12 and 17 share one Datalogic URL):
https://www.datalogic.com/eng/retail-transportation-logistics-healthcare-gs1-digital-link/mobile-computers/memor-12-17-pd-1102.html
Datasheet: DS-MEMOR12-17-EN Revision A 20252301.

This ERP Item is the Memor 12 6 GB / 64 GB Wi-Fi 6E full-touch PDA (no 5G).
Do not advertise Memor 17-only features: 5G, GNSS, eSIM, barometer, Safe Swap.
Memor 12 HC (white) is a different SKU.
"""

from pathlib import Path
from shutil import copy2
from urllib.parse import quote
from urllib.request import Request, urlopen

import frappe

NAME = "RET.SYS.DLG.4648"
SLUG = "datalogic-memor-12"
VIDEO_URL = "https://youtu.be/YTrq-KObWho"
CHANGE_VIDEO = "https://youtu.be/Sfx_y3peb6Y"
GS1_VIDEO = "https://youtu.be/Hd0NZLkkA7M"
STORE_VIDEO = "https://youtu.be/pjezQXMf1jo"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"
HERO = "/files/datalogic-memor-12-product.jpg"

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


def fill_datalogic_memor_12():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)

	hero = HERO
	combo = official_image("datalogic-memor-12-17-combo.png")
	slim = official_image("datalogic-memor-12-17-slim.jpg")
	gs1 = official_image("datalogic-memor-12-17-gs1.jpg")
	swap = official_image("datalogic-memor-12-17-swap.jpg")
	charging = official_image("datalogic-memor-12-17-charging.jpg")
	mobility = official_image("datalogic-memor-12-17-mobility.jpg")
	warehouse = copy_public_image("industry-warehouse-logistics.jpg")
	fashion = copy_public_image("industry-fashion.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")

	# Keep the existing ERP Item link.
	doc.website_product_name = "Datalogic Memor 12"
	doc.display_name = "Datalogic Memor 12"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "FULL-TOUCH MOBILE COMPUTER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Enterprise-grade power in a pocket-sized Wi-Fi PDA"
	doc.short_description = (
		"Datalogic Memor 12 is the Wi-Fi 6E full-touch PDA in the Memor 12-17 family — "
		"Datalogic’s thinnest enterprise device for the store floor. Same 6\" FHD+ Gorilla "
		"Glass 7 body, Green Spot scanning and GS1 Digital Link as Memor 17, without 5G. "
		"This Printechs item is 6 GB / 64 GB, Android 13 GMS, black."
	)
	doc.long_description = (
		"<p>Datalogic publishes Memor 12 and Memor 17 on one family page. Printechs keeps "
		"them as two products so you can specify Wi-Fi-only (12) or Wi-Fi + 5G (17). "
		"Memor 12 is the indoor, front-facing PDA for price check, assisted selling, shelf "
		"work and queue-busting.</p>"
		"<p>This item is the black Memor 12 full-touch PDA: Wi-Fi 6E, 6 GB RAM / 64 GB flash, "
		"standard-range 2D imager with Green Spot, Android 13 GMS and a 4,000 mAh wireless-"
		"charging battery. It does not include a handstrap. Memor 12 HC (white) and Memor 17 "
		"(5G / Safe Swap) are separate SKUs.</p>"
		"<p>The 6.0\" FHD+ (1080 × 2160) LTPS display is 450 nits with Gorilla Glass 7 in a "
		"13.5 mm, 245 g body. Halogen DE2121-DL plus DeepSight reads damaged or poorly lit "
		"codes. The family is GS1 Digital Link ready.</p>"
		"<p>Qualcomm QCx4490 (2.4 GHz) and optional Swap memory (+2 GB virtual RAM) keep "
		"apps moving. Charge by USB-C, wired cradle or Qi EPP 7 W wireless. Multi-side NFC "
		"supports contactless payments and Apple ECP. Enterprise Battery Saver can cut "
		"consumption by up to 20%.</p>"
		"<p>Memor 12 has no cellular modem — no 5G, eSIM, GNSS or Safe Swap. Choose "
		"<a href=\"/products/datalogic-memor-17\">Memor 17</a> for outdoor / last-mile 5G.</p>"
		"<p>Android 13 GMS on this SKU; the family also lists Android 15 options and a path "
		"to Android 19 with 4+4 years of support. Printechs stages Memor 12 in Riyadh, "
		"Jeddah and Dammam.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Memor 12 full-touch Wi-Fi 6E mobile computer, all sides"
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"6\" FHD+ · Gorilla Glass 7\n"
		"Wi-Fi 6E · no 5G\n"
		"GS1 Digital Link ready\n"
		"IP65 / IP68 · 4,000 mAh"
	)
	doc.story_heading = "Pocket-sized Android for the store floor — Wi-Fi 6E, no cellular"
	doc.visual_story_heading = "Memor 12 in retail operations"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.featured = 1
	doc.card_title = "Memor 12"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Thinnest Datalogic full-touch Wi-Fi 6E PDA for in-store work: Green Spot 2D, "
		"GS1 Digital Link and a 4,000 mAh wireless-charge battery. 5G is Memor 17."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify Memor 12 for Wi-Fi store teams"
	doc.final_cta_description = (
		"Need 5G or Safe Swap? That is Memor 17. Printechs can confirm docks, HC vs "
		"standard and MDM staging for Memor 12 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Memor 12 Full-Touch Wi-Fi 6E PDA Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Memor 12 pocket-sized full-touch PDA: 6\" FHD+, Wi-Fi 6E, Green Spot 2D "
		"and GS1 Digital Link. No 5G — that is Memor 17. From Printechs in Saudi Arabia."
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
					"13.5 mm and 245 g with a firm grip for all-day store work — enterprise "
					"scanning without a brick in the pocket."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Green Spot + DeepSight + GS1",
				"description": (
					"Halogen DE2121-DL with Green Spot and DeepSight reads dirty or poorly lit "
					"codes. The family is GS1 Digital Link ready."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E indoors — not 5G",
				"description": (
					"Wi-Fi 6E, Bluetooth 5.3 and multi-side NFC for the shop floor. Memor 12 "
					"has no cellular modem. Specify Memor 17 when you need 5G, GNSS or eSIM."
				),
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "Wireless charge, three ways",
				"description": (
					"4,000 mAh pack with USB-C, wired cradles or Qi EPP 7 W wireless. "
					"Enterprise Battery Saver can cut drain by up to 20%. Safe Swap is Memor 17 only."
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
				"image_alt": "Memor 12 slim full-touch PDA held in a retail aisle",
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
				"image_alt": "Memor wireless charging cradle and multi-side NFC tap-to-pay",
				"caption": "USB-C, wired or wireless dock — and multi-side NFC for tap-to-pay.",
				"sort_order": 3,
			},
			{
				"label": "Qualcomm + Swap memory",
				"image": swap,
				"image_alt": "Memor 12 Qualcomm QCM4490 processor and Swap memory",
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
				"title": "Wi-Fi 6E",
				"description": "Bluetooth 5.3 · NFC · no cellular",
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
				"description": "Qi EPP 7 W wireless · USB-C · cradles",
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
				("Printechs item", "RET.SYS.DLG.4648 — Memor 12 full-touch PDA"),
				("Memory / storage", "6 GB RAM / 64 GB UFS"),
				("Wireless", "Wi-Fi 6E, Bluetooth 5.3, NFC, PTT — no 5G"),
				("Imager", "Standard-range 2D with Green Spot"),
				("Cameras", "13 MP rear autofocus; 8 MP front"),
				("Battery", "4,000 mAh wireless-charging pack (not Safe Swap)"),
				("Colour", "Black (Memor 12 HC white is a different SKU)"),
				("In the box", "Device and battery — no handstrap on this item"),
			],
		),
		(
			"Computer",
			[
				("Family", "Memor 12-17 full-touch PDA; Memor 12 is the Wi-Fi-only model"),
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
				("Sensors", "Accelerometer, gyro, ambient light, proximity, magnetometer"),
				("Not on Memor 12", "Barometer / Z-location is Memor 17 only"),
			],
		),
		(
			"Wireless (Memor 12)",
			[
				("WLAN", "Wi-Fi 6E 802.11 a/b/g/n/ac/ax; 2.4 / 5 / 6 GHz; 2×2 MIMO"),
				("WLAN security", "WPA3 Enterprise 192-bit supported"),
				("Bluetooth", "5.3 Classic and BLE"),
				("NFC", "Tags 1–5; card emulator; contactless pay; Apple ECP"),
				("WWAN / 5G", "Not fitted — specify Memor 17 for LTE-A / 5G FR1"),
				("SIM / eSIM", "Not used on Memor 12"),
				("GNSS", "Not a Memor 12 feature — Memor 17 has dual-band GNSS"),
			],
		),
		(
			"Power, I/O & charging",
			[
				("Battery", "Swappable Li-Ion 3.87 V; 4,000 mAh typical (14.98 Wh)"),
				("Safe Swap", "Not on Memor 12 — Memor 17 only"),
				("Wireless charge", "WPC Qi EPP compliant, 7 W"),
				("Other charge", "USB-C fast top-up; wired enterprise cradles"),
				("Battery saver", "Enterprise Battery Saver — up to 20% less consumption"),
				("Interfaces", "USB 3.2 Gen1 host/client Type-C; SuperSpeed USB 2.0 bottom I/O"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Sealing", "IP65 and IP68 with battery (family datasheet / this catalog line)"),
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
					"queue-busting on Wi-Fi 6E — no SIM required."
				),
				"image": slim,
				"image_alt": "Memor 12 used for in-store retail operations",
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
				"title": "Wi-Fi warehouses and back-of-store",
				"description": (
					"Receiving, counts and put-away where coverage is WLAN. For yards and last "
					"mile, specify Memor 17 5G."
				),
				"image": warehouse,
				"image_alt": "Warehouse and back-of-store mobile scanning",
				"industry_link": "warehouse-logistics",
				"sort_order": 3,
			},
			{
				"title": "Healthcare (or Memor 12 HC)",
				"description": (
					"eMR and pharmacy ID on Wi-Fi. Specify Memor 12 HC (white) when you need "
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
				"heading": "Watch Memor 12-17 — then pick the Wi-Fi model",
				"body": (
					"Official Datalogic film covers the shared Memor 12-17 family. This page is "
					"Memor 12 only: same pocket-sized full-touch body as Memor 17, Wi-Fi 6E "
					"instead of 5G. Need cellular? Open the Memor 17 page."
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
					"drops (1.3 m without boot, 1.5 m with boot). Catalog sealing for Memor 12 "
					"is IP65/IP68 with battery."
				),
				"image": slim,
				"image_alt": "Slim Memor 12 PDA in a supermarket aisle",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "GS1 Digital Link, Green Spot and DeepSight",
				"body": (
					"Halogen DE2121-DL with Green Spot and DeepSight keeps reads reliable on "
					"damaged or poorly lit labels. Memor 12 is GS1 Digital Link ready with "
					"Magellan and Gryphon in Datalogic’s retail portfolio."
				),
				"video_url": GS1_VIDEO,
				"image": gs1,
				"image_alt": "Memor 12 GS1 Digital Link shelf scanning",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Qualcomm 4490 and Swap memory — on Wi-Fi 6E",
				"body": (
					"Qualcomm QCx4490 plus optional Swap memory (+2 GB virtual RAM) keep POS "
					"and WMS apps in play. Memor 12 stays on Wi-Fi 6E, Bluetooth 5.3 and NFC. "
					"Memor 17 is the model that adds 5G, GNSS, eSIM and a barometer."
				),
				"image": swap,
				"image_alt": "Memor 12 Qualcomm QCM4490 and Swap memory",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Charge three ways — or take payment",
				"body": (
					"USB-C for a quick top-up, wired cradles for data, or Qi EPP 7 W wireless "
					"docks with no pins to corrode. Multi-side NFC handles tap-to-pay and "
					"Apple ECP. Safe Swap (change the pack without killing the session) is "
					"Memor 17 only."
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
					"EASEOFCARE.\n\n"
					"Printechs stages MDM, docks and apps for retailers in Riyadh, Jeddah and "
					"Dammam. Watch Datalogic’s Intelligent Store film for the wider context."
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
				"title": "12 vs 17",
				"description": "Wi-Fi-only Memor 12, or Memor 17 when the site needs 5G, GNSS or Safe Swap.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Device staging",
				"description": "Scan2Deploy, OEMConfig, Zero-Touch and app load before devices hit the floor.",
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
			{"item_description": "Memor 12 full-touch PDA (this item: 6 GB / 64 GB, Wi-Fi 6E, black)", "sort_order": 1},
			{"item_description": "4,000 mAh wireless-charging battery", "sort_order": 2},
			{"item_description": "Google Mobile Services", "sort_order": 3},
			{"item_description": "No handstrap on this item", "sort_order": 4},
			{"item_description": "Optional wired or wireless docks, holster and trigger handle sold separately", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4708", 1),
			related_product_row("RET.SYS.DLG.5029", 2),
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
				"question": "What is the Datalogic Memor 12?",
				"answer": (
					"The Wi-Fi 6E full-touch model in the Memor 12-17 family — Datalogic’s "
					"thinnest enterprise PDA for in-store work. Datalogic shows 12 and 17 on "
					"one page; Printechs lists them separately."
				),
				"sort_order": 1,
			},
			{
				"question": "How is Memor 12 different from Memor 17?",
				"answer": (
					"Same slim 6\" body, scanner, GS1 Digital Link and Wi-Fi 6E. Memor 12 has "
					"no 5G, GNSS, eSIM, barometer or Safe Swap. Those are Memor 17. This page "
					"is Memor 12 (RET.SYS.DLG.4648)."
				),
				"sort_order": 2,
			},
			{
				"question": "Does Memor 12 have 5G?",
				"answer": "No. Specify Memor 17 when you need cellular, GPS or eSIM.",
				"sort_order": 3,
			},
			{
				"question": "Is this the healthcare Memor 12 HC?",
				"answer": (
					"No. This item is the black standard Memor 12. Memor 12 HC is a separate "
					"white healthcare SKU (for example 944950027)."
				),
				"sort_order": 4,
			},
			{
				"question": "Does it read GS1 Digital Link?",
				"answer": (
					"Yes. The Memor 12-17 family is specified GS1 Digital Link ready, with "
					"Halogen DE2121-DL, Green Spot and DeepSight."
				),
				"sort_order": 5,
			},
			{
				"question": "What memory and Android version ship on this item?",
				"answer": (
					"6 GB RAM / 64 GB flash and Android 13 GMS. Swap memory can add +2 GB "
					"virtual RAM. The published OS path is Android 19."
				),
				"sort_order": 6,
			},
			{
				"question": "Does it include a handstrap?",
				"answer": "Not on this Printechs item. Battery is included; holster and docks are optional.",
				"sort_order": 7,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"1-year factory warranty. Official page cites 4+4 years of hardware and "
					"software support; EASEOFCARE and Shield extend service and Android patches."
				),
				"sort_order": 8,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
