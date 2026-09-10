# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.DLG.5029 — Datalogic Smart Portal.

Official page:
https://www.datalogic.com/eng/retail-transportation-logistics-healthcare-gs1-digital-link-other-applications/mobile-computers/smart-portal-pd-1162.html
Datasheet: DS-SMARTPORTAL-EN Revision A.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

NAME = "RET.SYS.DLG.5029"
SLUG = "datalogic-smart-portal"
VIDEO_URL = "https://youtu.be/CErma4Bbs30"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-smart-portal-product.png": "/upload/products/MobileComputers/smart-portal.png",
	"datalogic-smart-portal-retail.jpg": "/upload/prod_line2/SmartPortal/2.jpg",
	"datalogic-smart-portal-hospitality.jpg": "/upload/prod_line2/SmartPortal/3.jpg",
	"datalogic-smart-portal-healthcare.jpg": "/upload/prod_line2/SmartPortal/4.jpg",
	"datalogic-smart-portal-android.jpg": "/upload/prod_line2/SmartPortal/5.jpg",
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


def fill_datalogic_smart_portal():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)

	product = official_image("datalogic-smart-portal-product.png")
	retail = official_image("datalogic-smart-portal-retail.jpg")
	hospitality = official_image("datalogic-smart-portal-hospitality.jpg")
	healthcare = official_image("datalogic-smart-portal-healthcare.jpg")
	android = official_image("datalogic-smart-portal-android.jpg")

	hero = doc.hero_image or "/files/SmartPortal-front.jpg"

	doc.display_name = "Datalogic Smart Portal"
	doc.website_product_name = "Datalogic Smart Portal"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "WALL-MOUNT SELF-SERVICE HUB"
	doc.tagline = "The intelligent gateway to self-service"
	doc.short_description = (
		"Datalogic Smart Portal is a wall-mount interactive hub for self-service in retail, "
		"hospitality and healthcare. An 8.6\" HD display, Green Spot 2D scanning, Wi-Fi 6E, "
		"Bluetooth 5.3, NFC and PoE or standard power turn store entry, price checks, "
		"ticketing and check-in into one digital assistant."
	)
	doc.long_description = (
		"<p>Datalogic Smart Portal is a versatile interactive solution designed to transform "
		"self-service. Acting as a digital assistant, it enables faster, more autonomous and "
		"accessible interactions across retail, hospitality and healthcare.</p>"
		"<p>Built for intuitive use, it combines an 8.6\" HD display (1340 × 800, 450 nits), "
		"high-visibility status LEDs and front-facing audio. Datalogic’s Halogen DE2121-DL "
		"1D/2D engine with Green Spot and autoscan delivers rapid barcode capture from paper "
		"or a phone, with a typical 1 m scan range and Time-of-Flight sensing.</p>"
		"<p>Wi-Fi 6E (2×2 MIMO, WPA3 Enterprise), Bluetooth 5.3 and NFC keep the device "
		"online in busy sites. Power is PoE+ Type 2 or a standard DC supply. VESA 75 and "
		"universal wall brackets simplify mounting. The platform ships with Android 15, is "
		"upgradeable to Android 19, and works with Datalogic Mobility Suite, Connect and Shield.</p>"
		"<p>Official configurations are 6 GB RAM / 128 GB flash, Qualcomm QCx4490 octa-core "
		"2.4 GHz, 5 MP front camera, MicroSD up to 2 TB, USB-C OTG, USB-C, USB-A and Gigabit "
		"Ethernet. Colors: black (912000002) and light grey (912000001). Factory warranty is "
		"1 year, extendable with EASEOFCARE and Datalogic Shield.</p>"
		"<p>Printechs supplies and supports Datalogic self-service and mobility solutions in "
		"Saudi Arabia, including Riyadh, Jeddah and Dammam — selection, mounting, PoE, POS "
		"and Joya entry integration, rollout and after-sales service.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Smart Portal wall-mount self-service computer"
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"8.6\" HD · 1340 × 800\n"
		"Wi-Fi 6E · Bluetooth 5.3 · NFC\n"
		"2D imager + Green Spot\n"
		"Android 15, path to 19"
	)
	doc.story_heading = "One wall-mount hub for entry, price check and check-in"
	doc.visual_story_heading = "Smart Portal across retail, hospitality and healthcare"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "Smart Portal"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Wall-mount Android self-service hub with 8.6\" HD display, Green Spot 2D scanning, "
		"Wi-Fi 6E, NFC and PoE. For store entry, price verification, ticketing and check-in."
	)
	doc.card_image = doc.card_image or product

	doc.final_cta_heading = "Specify Smart Portal for your self-service touchpoints"
	doc.final_cta_description = (
		"Printechs can confirm color, PoE or DC power, wall bracket, Joya entry unlock and "
		"Android integration for Datalogic Smart Portal in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Smart Portal Self-Service Kiosk Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Smart Portal wall-mount self-service hub with 8.6\" HD display, Green Spot "
		"2D scanning, Wi-Fi 6E, NFC and PoE. For retail entry, price check and check-in in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "store",
				"title": "Frictionless in-store journeys",
				"description": (
					"Scan a loyalty card or mobile app to unlock a Joya device at the entrance, "
					"verify prices in real time, and validate tickets without a staffed counter."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Precision scanning with Green Spot",
				"description": (
					"Halogen DE2121-DL 1D/2D engine with autoscan and Green Spot reads paper and "
					"phone barcodes quickly, with visual and acoustic confirmation."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E, Bluetooth 5.3 and PoE",
				"description": (
					"Stable wireless in busy sites, NFC identification, Gigabit Ethernet and "
					"PoE+ Type 2 or a standard DC supply for flexible install."
				),
				"sort_order": 3,
			},
			{
				"icon": "android",
				"title": "Android 15 with a path to 19",
				"description": (
					"Future-ready OS, Datalogic Mobility Suite, Connect remote management and "
					"Shield security updates for a long self-service life."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Retail price check & entry",
				"image": retail,
				"image_alt": "Datalogic Smart Portal used for retail price verification and store entry",
				"caption": "Entrance unlock, price check and product information on the shop floor.",
				"sort_order": 1,
			},
			{
				"label": "Hospitality check-in",
				"image": hospitality,
				"image_alt": "Datalogic Smart Portal hotel and reception self check-in",
				"caption": "Self-service check-in, bookings and digital concierge at the front desk.",
				"sort_order": 2,
			},
			{
				"label": "Healthcare access",
				"image": healthcare,
				"image_alt": "Datalogic Smart Portal for healthcare patient check-in",
				"caption": "Patient self check-in and care information so staff can focus on care.",
				"sort_order": 3,
			},
			{
				"label": "Android self-service platform",
				"image": android,
				"image_alt": "Datalogic Smart Portal Android 15 self-service platform",
				"caption": "Android 15 today, upgradeable to Android 19, with Mobility Suite and Shield.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "display",
				"title": "8.6\" HD",
				"description": "1340 × 800 · 16:10 · 450 nits · glove-ready touch",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "2D + Green Spot",
				"description": "Halogen DE2121-DL · autoscan · ~1 m range",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E",
				"description": "Bluetooth 5.3 · NFC · Gigabit Ethernet · PoE+",
				"sort_order": 3,
			},
			{
				"icon": "android",
				"title": "Android 15",
				"description": "Upgradeable to Android 19 · GMS certified",
				"sort_order": 4,
			},
			{
				"icon": "device",
				"title": "6 / 128 GB",
				"description": "Qualcomm QCx4490 octa-core 2.4 GHz · MicroSD to 2 TB",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "1-year warranty",
				"description": "Factory warranty · EASEOFCARE and Shield options",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"System & display",
			[
				("Model", "Smart Portal — wall-mount entrance unit / price checker"),
				("Part numbers", "912000002 black · 912000001 light grey"),
				("Processor", "Qualcomm QCx4490 octa-core 2.4 GHz"),
				("Memory / storage", "6 GB RAM / 128 GB flash"),
				("Expansion", "MicroSD up to 2 TB"),
				("Operating system", "Android 15, upgradeable to Android 19"),
				("Display", "8.6\" color HD, 1340 × 800, 16:10, 450 nits"),
				("Touch", "5-point capacitive, optical bonding, gloves and stylus"),
				("Keys", "Power, volume up/down, reset"),
				("Front camera", "5 MP (badge verification)"),
				("Sensors", "Time of Flight"),
				("Audio", "2 microphones · 2 speakers 1.3 W (1.5 W short term), 90 dBA"),
			],
		),
		(
			"Scanning & identification",
			[
				("Scan engine", "Halogen DE2121-DL 1D/2D with Green Spot"),
				("Autoscan", "Supported (official model listing)"),
				("Typical scan range", "Up to 1 m (datasheet graphic)"),
				("NFC", "Tag types 2/3/4/5 — ISO14443-4 A/B, ISO15693, MIFARE, FeliCa"),
			],
		),
		(
			"Wireless, interfaces & power",
			[
				("WLAN", "Wi-Fi 6E IEEE 802.11 a/b/g/n/ac/ax; 2.4 / 5 / 6 GHz; 2×2 MIMO"),
				("WLAN security", "WPA3 Enterprise 192-bit mode supported"),
				("WPAN", "Bluetooth 5.3 Classic and BLE"),
				("USB", "USB-C host, USB-A host (USB 2.0), USB-C OTG"),
				("Ethernet", "Gigabit RJ45"),
				("Power", "PoE+ IEEE 802.3at Type 2, or DC port with power supply"),
			],
		),
		(
			"Physical & environment",
			[
				("Dimensions", "227 × 164.5 × 32 mm"),
				("Weight", "638 g"),
				("Mounting", "VESA 75; wall brackets 94ACC0464 / 94ACC0465"),
				("Operating temperature", "0 to 40 °C"),
				("Storage / transport", "−30 to 70 °C"),
				("Humidity", "5–95% non-condensing"),
				("ESD", "15 kV air / 8 kV contact"),
				("Chemical resistance", "IPA 70%, common glass cleaners, dilute bleach, H2O2 3%"),
				("LED feedback", "Light-guide LED around scan engine plus backlight status LEDs"),
				("Environmental compliance", "EU RoHS"),
				("GMS", "GMS certified"),
				("Warranty", "1-year factory warranty"),
				("Item code", NAME),
			],
		),
		(
			"Software & management",
			[
				("Mobility Suite", "Launcher kiosk lock, Enterprise Browser, Integrity KIT, Shield"),
				("Configuration", "Scan2Deploy, OEMConfig, AE / Wi-Fi QR enrollment"),
				("Development", "SDKs for Java, Kotlin, Xamarin, .NET, MAUI, JavaScript"),
				("Empower tools", "SoftSpot, QuickBoard, Snap OCR, Wedge, Visual Formatter"),
				("UEM / EMM", "SOTI, Workspace ONE, Intune, 42Gears, Ivanti, OEMConfig"),
				("Remote platform", "Datalogic Connect for visibility and device management"),
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
				"title": "Retail store entry & price check",
				"description": "Unlock Joya devices, verify prices, compare products and validate tickets on the shop floor.",
				"image": retail,
				"image_alt": "Datalogic Smart Portal retail price checker and entrance unit",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Hospitality reception",
				"description": "Self check-in, bookings, schedules and digital concierge to cut front-desk queues.",
				"image": hospitality,
				"image_alt": "Datalogic Smart Portal hospitality check-in",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Healthcare check-in",
				"description": "Patient self-registration and care information so clinical staff can focus on patients.",
				"image": healthcare,
				"image_alt": "Datalogic Smart Portal healthcare self check-in",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Assisted selling & digital signage",
				"description": "How-to video, product demonstration, loyalty and call-for-assistance on a single wall hub.",
				"image": android,
				"image_alt": "Datalogic Smart Portal Android digital assistant",
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
				"heading": "See Smart Portal — the intelligent gateway to self-service",
				"body": (
					"Watch Datalogic’s official film: store-entrance Joya unlock, price checks, "
					"ticketing, Green Spot confirmation, hospitality and healthcare check-in, "
					"Wi-Fi 6E and an Android 15 platform ready for Android 19."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic Smart Portal wall-mount self-service computer",
				"link_label": "Talk to Our Retail Team",
				"link_href": "/contact",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Retail: frictionless in-store journeys",
				"body": (
					"At the entrance, customers scan a loyalty card or mobile app to unlock a Joya "
					"device — a bright LED confirms access. On the floor, the same unit is a price "
					"checker tied to central product data. Ticket scanning speeds access control "
					"and reduces queues."
				),
				"image": retail,
				"image_alt": "Datalogic Smart Portal retail entrance and price verification",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Smart reception and healthcare check-in",
				"body": (
					"In hospitality the Smart Portal is a digital concierge: self check-in, bookings "
					"and service information without adding front-desk staff. In healthcare, patients "
					"register on arrival and reach care information while staff stay with patients."
				),
				"image": hospitality,
				"image_alt": "Datalogic Smart Portal reception and healthcare check-in",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Scan, identify and assist",
				"body": (
					"The Halogen DE2121-DL engine with Green Spot and autoscan reads 1D/2D codes "
					"from labels and phones. NFC handles cards and badges. A 5 MP front camera "
					"supports badge verification. Dual mics and speakers let users call a live or "
					"virtual assistant without leaving the hub."
				),
				"image": product,
				"image_alt": "Datalogic Smart Portal with Green Spot scan window",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Deploy anywhere — VESA, PoE and Mobility Suite",
				"body": (
					"VESA 75 plus brackets 94ACC0464 (cabinet / void wall) and 94ACC0465 (solid wall "
					"with PSU support) keep install simple. Power is PoE+ Type 2 or DC. Android 15 "
					"with a path to 19, Shield patches, Connect remote management and kiosk lock-down "
					"keep a fleet current. Factory warranty is 1 year."
				),
				"image": android,
				"image_alt": "Datalogic Smart Portal Android and Mobility Suite platform",
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "store",
				"title": "Use-case selection",
				"description": "Confirm entrance/Joya unlock, price checker, ticketing, hospitality or healthcare check-in.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Mounting & power",
				"description": "VESA 75, 94ACC0464/0465 brackets, PoE cable 94ACC0468 or DC PSU 94ACC0197.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "Android & POS integration",
				"description": "Aladdin/Scan2Deploy, Mobility Suite kiosk lock, Connect, EMM/UEM and Joya entry flows.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Rollout, Shield/EASEOFCARE options and after-sales support in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "Smart Portal entrance unit / price checker (black 912000002 or light grey 912000001)", "sort_order": 1},
			{"item_description": "94ACC0464 wall bracket for cabinets with void space (optional)", "sort_order": 2},
			{"item_description": "94ACC0465 wall bracket with power-supply support (optional)", "sort_order": 3},
			{"item_description": "94ACC0468 PoE Ethernet cable or 94ACC0197 DC power supply (optional)", "sort_order": 4},
			{"item_description": "94ACC0466 USB-A–C or 94ACC0467 USB-C–C 1 m cable (optional)", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4708", 1),
			related_product_row("RET.SYS.DLG.4648", 2),
			related_product_row("RET.SYS.DLG.4885", 3),
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
				"question": "What is the Datalogic Smart Portal?",
				"answer": (
					"A wall-mount Android self-service hub used as an entrance unit, price checker, "
					"ticketing kiosk and digital concierge in retail, hospitality and healthcare."
				),
				"sort_order": 1,
			},
			{
				"question": "What display and computer does it use?",
				"answer": (
					"An 8.6\" HD 1340 × 800 panel at 450 nits, Qualcomm QCx4490 octa-core 2.4 GHz, "
					"6 GB RAM and 128 GB flash, running Android 15 with an upgrade path to Android 19."
				),
				"sort_order": 2,
			},
			{
				"question": "How does store entry with Joya work?",
				"answer": (
					"Customers scan a loyalty card or mobile app at the portal to unlock a Joya "
					"device. A bright LED confirms access so shopping can start without a staffed gate."
				),
				"sort_order": 3,
			},
			{
				"question": "What scanner and wireless radios are included?",
				"answer": (
					"Halogen DE2121-DL 1D/2D with Green Spot and autoscan, plus Wi-Fi 6E, "
					"Bluetooth 5.3 and NFC. A 5 MP front camera supports badge checks."
				),
				"sort_order": 4,
			},
			{
				"question": "Can it run on PoE?",
				"answer": (
					"Yes. Official models support PoE+ Type 2 (IEEE 802.3at) or a DC power supply. "
					"Gigabit Ethernet is on an RJ45 port."
				),
				"sort_order": 5,
			},
			{
				"question": "What colors and part numbers are available?",
				"answer": "Black 912000002 and light grey 912000001 — same Wi-Fi 6E / 6+128 GB / Android 15 specification.",
				"sort_order": 6,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The official datasheet specifies a 1-year factory warranty. EASEOFCARE and "
					"Datalogic Shield plans can extend hardware and Android security coverage."
				),
				"sort_order": 7,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
