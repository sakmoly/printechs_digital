# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic Skorpio X40/X45 (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail-manufacturing-transportation-logistics-healthcare-gs1-digital-link/mobile-computers/skorpio-x40-45-pd-1164.html
Datasheet: DS-SKORPIOX40-X45-EN Rev A 20260421.

X40 is Wi-Fi 6/6E. X45 adds 5G, GPS/GNSS, Nano SIM + eSIM and barometer.
Do not advertise 5G as standard on every Skorpio X40.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

SLUG = "datalogic-skorpio-x40-x45"
VIDEO_URL = "https://youtu.be/-EYF6b0JoC4"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-skorpio-x40-x45.png": "/upload/products/Skorpio_700x700.png",
	"datalogic-skorpio-x40-x45-1.jpg": "/upload/prod_line2/Skorpio/1_2.jpg",
	"datalogic-skorpio-x40-x45-2.jpg": "/upload/prod_line2/Skorpio/2.jpg",
	"datalogic-skorpio-x40-x45-3.jpg": "/upload/prod_line2/Skorpio/3.jpg",
	"datalogic-skorpio-x40-x45-4.jpg": "/upload/prod_line2/Skorpio/4.jpg",
	"datalogic-skorpio-x40-x45-5.jpg": "/upload/prod_line2/Skorpio/5.jpg",
	"datalogic-skorpio-x40-x45-6.jpg": "/upload/prod_line2/Skorpio/6.jpg",
	"datalogic-skorpio-x40-x45-7.jpg": "/upload/prod_line2/Skorpio/7.jpg",
	"datalogic-skorpio-x40-x45-8.jpg": "/upload/prod_line2/Skorpio/8.jpg",
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
	doc.website_product_name = "Datalogic Skorpio X40/X45"
	doc.display_name = "Datalogic Skorpio X40/X45"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic Skorpio X40/X45 key-based warehouse mobile computer."
	doc.long_description = "<p>Datalogic Skorpio X40/X45 key-based warehouse mobile computer.</p>"
	doc.hero_image = official_image("datalogic-skorpio-x40-x45.png")
	return doc


def fill_datalogic_skorpio_x40_x45():
	doc = get_or_create()

	hero = official_image("datalogic-skorpio-x40-x45.png")
	scan = official_image("datalogic-skorpio-x40-x45-1.jpg")
	android = official_image("datalogic-skorpio-x40-x45-2.jpg")
	dock = official_image("datalogic-skorpio-x40-x45-3.jpg")
	workflows = official_image("datalogic-skorpio-x40-x45-4.jpg")
	rugged = official_image("datalogic-skorpio-x40-x45-5.jpg")
	connect = official_image("datalogic-skorpio-x40-x45-6.jpg")
	wireless = official_image("datalogic-skorpio-x40-x45-7.jpg")
	warehouse = official_image("datalogic-skorpio-x40-x45-8.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")

	# Intentionally no Item — link later under ERP Item Link when the Item exists.
	doc.item = None
	doc.website_product_name = "Datalogic Skorpio X40/X45"
	doc.display_name = "Datalogic Skorpio X40/X45"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "KEY-BASED MOBILE COMPUTER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "The next-generation key-based mobile computer for all-day operations"
	doc.short_description = (
		"Datalogic Skorpio X40/X45 is a compact, key-based Android mobile computer for "
		"warehouse picking, replenishment, stock count and goods movement. A 4\" display, "
		"up to 48 physical keys, detachable pistol grip, Green Spot 2D imaging and a "
		"7,000 mAh hot-swap battery keep operators accurate through a full shift."
	)
	doc.long_description = (
		"<p>Skorpio X40/X45 is Datalogic’s next-generation key-based handheld for frontline "
		"warehouse work — retail distribution, manufacturing and transportation &amp; "
		"logistics. It is built for high-frequency scan-and-key tasks, not for the POS lane.</p>"
		"<p>The compact, balanced body supports one-handed use. Three keyboards (29 numeric, "
		"39 functional numeric, 48 alphanumeric) have large, well-spaced keys that work with "
		"gloves. A field-detachable handle switches the same unit between handheld and pistol "
		"grip without slowing the shift.</p>"
		"<p>Qualcomm Dragonwing™ 4490 octa-core 2.4 GHz, 6 GB RAM and 128 GB UFS run Android "
		"15 (GMS / AOSP), Android Enterprise Recommended, with a published path to Android 19. "
		"The 4.0\" WVGA IPS display (480 × 800, 450 nits) uses Corning Gorilla Glass Victus.</p>"
		"<p>X40 is Wi-Fi 6/6E, Bluetooth 5.3 and NFC. X45 adds 5G (Sub-6), dual-band GNSS, "
		"Nano SIM + eSIM and a barometer. Both read 1D/2D with Halogen DE2121-DL or "
		"extended-range DE2121-ER and Green Spot confirmation, plus a 13 MP rear camera.</p>"
		"<p>The 7,000 mAh pack is hot-swappable and charges by contacts or Qi EPP 10 W "
		"wireless. Sealing is IP65/IP67; drops are 2.4 m at ambient and 1.8 m across "
		"−20 to 50 °C (MIL-STD-810H). New 4-slot docks are shared with Falcon X60/X65; "
		"single docks remain backward-compatible with Skorpio X5.</p>"
		"<p>Printechs specifies and supports Skorpio X40/X45 in Saudi Arabia — Riyadh, "
		"Jeddah and Dammam — including keyboard, optic, Wi-Fi vs 5G, docks and EASEOFCARE.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = (
		"Datalogic Skorpio X40/X45 handheld and pistol-grip key-based mobile computers"
	)
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"Android 15 · path to 19\n"
		"29 / 39 / 48 physical keys\n"
		"Wi-Fi 6E · 5G on X45\n"
		"IP65/IP67 · 7,000 mAh"
	)
	doc.story_heading = "Key-based computing for fast-moving warehouse shifts"
	doc.visual_story_heading = "Skorpio X40/X45 on the warehouse floor"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "Skorpio X40/X45"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Compact key-based Android warehouse computer: 4\" display, up to 48 keys, "
		"detachable pistol grip, Green Spot 2D, Wi-Fi 6E and 5G on X45."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify Skorpio X40/X45 for your warehouse fleet"
	doc.final_cta_description = (
		"Printechs can confirm X40 Wi-Fi or X45 5G, keyboard, standard or long-range imager, "
		"handheld or pistol grip, and docks for sites in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Skorpio X40/X45 Warehouse Computer Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Skorpio X40/X45 key-based Android mobile computer for warehouse picking "
		"and inventory. Wi-Fi 6E, 5G on X45, 48-key options, Green Spot 2D. From Printechs in KSA."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "inventory",
				"title": "Built for warehouse keying",
				"description": (
					"29, 39 or 48 well-spaced keys keep scan-and-key work fast when a "
					"touchscreen is the wrong tool — picking, replenishment, counts and goods movement."
				),
				"sort_order": 1,
			},
			{
				"icon": "rugged",
				"title": "All-day comfort, industrial hide",
				"description": (
					"Compact one-handed balance, detachable pistol grip, IP65/IP67 and MIL-STD-810H "
					"drops (2.4 m ambient / 1.8 m over the full operating range)."
				),
				"sort_order": 2,
			},
			{
				"icon": "scan",
				"title": "Green Spot you can trust",
				"description": (
					"Halogen DE2121 standard or extended-range 1D/2D engines project Green Spot "
					"on the label so operators keep their eyes on the work."
				),
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "Hot-swap and wireless charge",
				"description": (
					"7,000 mAh Li-Ion, hot-swap for 24/7, plus contact or Qi EPP 10 W wireless "
					"charging — and new docks shared with Falcon X60/X65."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Warehouse scanning",
				"image": scan,
				"image_alt": "Skorpio X40/X45 long-range scanning from a warehouse vehicle",
				"caption": "Standard or extended-range Halogen imaging with Green Spot confirmation.",
				"sort_order": 1,
			},
			{
				"label": "Handheld or pistol",
				"image": workflows,
				"image_alt": "Skorpio X40/X45 in warehouse, manufacturing and parcel workflows",
				"caption": "Field-detachable handle: switch grip to match the task.",
				"sort_order": 2,
			},
			{
				"label": "Docks and Green Spot",
				"image": dock,
				"image_alt": "Skorpio X40/X45 handheld and pistol-grip units in charging docks",
				"caption": "Contact or wireless charge; backward-compatible with Skorpio X5 single docks.",
				"sort_order": 3,
			},
			{
				"label": "Connect and Mobility Suite",
				"image": connect,
				"image_alt": "Skorpio X40/X45 with Datalogic Connect and Mobility Suite",
				"caption": "Stage, lock down and watch the fleet with Mobility Suite and Datalogic Connect.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "android",
				"title": "Android 15",
				"description": "GMS · Enterprise Recommended · path to 19",
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "4.0\" WVGA",
				"description": "480 × 800 · 450 nits · Gorilla Glass Victus",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E / 5G",
				"description": "X40 WLAN · X45 adds 5G + GNSS",
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "7,000 mAh",
				"description": "Hot-swap · Qi EPP 10 W wireless",
				"sort_order": 4,
			},
			{
				"icon": "rugged",
				"title": "IP65 / IP67",
				"description": "2.4 m ambient drop · 3,000 tumbles",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "1-year warranty",
				"description": "Factory warranty · EASEOFCARE + Shield",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Computer",
			[
				("Family", "Skorpio X40/X45 key-based industrial handheld computer"),
				("X40", "Wi-Fi 6/6E handheld or pistol grip (listed SKUs 946400xxx)"),
				("X45", "Wi-Fi 6E + 5G pistol-grip models (listed SKUs 946450xxx)"),
				("Processor", "Qualcomm Dragonwing 4490 octa-core 2.4 GHz"),
				("Memory", "6 GB RAM; 128 GB UFS flash"),
				("Expansion", "MicroSD up to 2 TB"),
				("OS", "Android 15 GMS and AOSP; platform upgradeable to Android 19"),
				("Enterprise", "Android Enterprise Recommended; GMS certified"),
				("Display", "4.0\" LCD A-Si IPS WVGA 480 × 800; 450 nits typical"),
				("Touch", "5-point capacitive; Gorilla Glass Victus; gloves and stylus"),
				("Keyboards", "29-key numeric; 39-key functional numeric; 48-key alphanumeric"),
				("Other keys", "2 side scan keys; power; 3 Android soft keys"),
				("Handle", "Field-detachable pistol grip (94ACC0445 / conversion 94ACC0447)"),
				("Camera", "13 MP rear, autofocus, LED torch"),
				("Audio", "Dual mics with noise cancellation; hands-free speaker"),
			],
		),
		(
			"Scanning & sensors",
			[
				("Scan engines", "Halogen DE2121-DL 1D/2D or DE2121-ER extended range"),
				("Good-read", "Datalogic Green Spot on all scan engines"),
				("Long range", "Extended-range option for distance reads (up to ~10 m class)"),
				("Accelerometer", "3-axis orientation"),
				("Other sensors", "Gyroscope, ambient light, proximity, magnetometer"),
				("Barometer", "Atmospheric / Z-location on Skorpio X45 only"),
				("Vibration", "Software-programmable duration and intensity"),
			],
		),
		(
			"Wireless",
			[
				("WLAN (all)", "Wi-Fi 6/6E 802.11 a/b/g/n/ac/ax; 2.4 / 5 / 6 GHz; 2×2 MU-MIMO"),
				("WLAN security", "WPA3 Enterprise 192-bit supported"),
				("Bluetooth", "5.3 Classic and BLE"),
				("NFC", "Tag types 2/3/4/5; reader and card emulator"),
				("WWAN", "X45 only: 3G / LTE-A / 5G FR1, data only, private network / CBRS"),
				("SIM", "X45 only: 1 Nano SIM + 1 eSIM"),
				("GNSS", "X45 only: GPS, Galileo, GLONASS, BeiDou; L1 + L5; A-GPS"),
			],
		),
		(
			"Power, I/O & docks",
			[
				("Battery", "Removable Li-Ion 3.63 V; 7,000 mAh typical (25.445 Wh)"),
				("Hot-swap", "Supported for application data protection / 24/7 use"),
				("Wireless charge", "WPC Qi EPP compatible, 10 W"),
				("USB charge", "USB-C for fast battery charging"),
				("Interfaces", "USB 3.2 Gen1 host/client Type-C; SuperSpeed USB 2.0 bottom I/O"),
				("Ethernet", "Gigabit via multi-slot dock"),
				("Shared docks", "4-slot charge 94A150143; 4-slot Ethernet 94A150144 (with Falcon X60/X65)"),
				("Single dock", "94A150151 contacts; backward-compatible with Skorpio X5 docks"),
				("Battery pack P/N", "94ACC0440 (shared with Falcon X60/X65)"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Handheld size", "210 × 75 × 27 mm / 8.27 × 2.95 × 1.06 in"),
				("Pistol size", "210 × 75 × 155 mm / 8.27 × 2.95 × 6.10 in"),
				("Weight", "Handheld 445 g; pistol grip 575 g, with battery"),
				("Drop ambient", "Multiple 2.4 m / 8 ft to concrete, MIL-STD-810H"),
				("Drop operating", "Multiple 1.8 m / 6 ft, −20 to 50 °C, MIL-STD-810H"),
				("Tumble", "3,000 × 1.0 m at room temperature, IEC 60068-2-32"),
				("Sealing", "IP65 and IP67 with battery, IEC 60529"),
				("Operating temp", "−20 to 50 °C"),
				("Storage / transport", "−30 to 70 °C"),
				("ESD", "15 kV air / 8 kV contact"),
				("Chemicals", "Selected bleach, ammonia glass, IPA 70%, H2O2 3%, industrial oils"),
				("Laser / LED", "VLD Class 2 IEC/EN 60825-1; LED Exempt IEC/EN 62471"),
				("Compliance", "EU RoHS"),
				("Warranty", "1-year factory warranty"),
			],
		),
		(
			"Software & management",
			[
				("Mobility Suite", "Shield, Launcher, Enterprise Browser, Integrity KIT"),
				("Staging", "Scan2Deploy, OEMConfig, AE / Wi-Fi QR enrollment"),
				("SDKs", "Java, Kotlin, Xamarin, .NET MAUI, JavaScript"),
				("UEM / EMM", "SOTI, Workspace ONE, Intune, 42Gears, Ivanti, OEMConfig"),
				("TE / PTT", "Ivanti Velocity, StayLinked Smart TE, Zello PTT"),
				("Datalogic Connect", "Cloud IoT for remote control and fleet insights"),
				("Battery tools", "Battery Manager, Enterprise Battery Saver, Smart Charge"),
				("Extras", "Snap OCR, Pocket Mode, SoftSpot, QuickBoard, Wi-Fi Guard, Logger"),
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
				"title": "Warehouse picking, put-away and counts",
				"description": (
					"One-handed keying and Green Spot reads for receiving, replenishment, "
					"cycle count and outbound in retail DCs and 3PLs."
				),
				"image": warehouse,
				"image_alt": "Skorpio X40/X45 in a warehouse aisle",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Manufacturing WIP and kitting",
				"description": (
					"Track materials, work orders and kits on the shop floor with a glove-friendly "
					"keypad and detachable pistol grip."
				),
				"image": packaging,
				"image_alt": "Manufacturing and packaging line mobile data capture",
				"industry_link": "packaging",
				"sort_order": 2,
			},
			{
				"title": "Healthcare warehouse and batch tracking",
				"description": (
					"Receiving, quality check, fulfilment and returns where batch accuracy matters."
				),
				"image": pharma,
				"image_alt": "Pharmaceutical warehouse inventory identification",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Retail distribution — not the checkout lane",
				"description": (
					"Back-of-store and DC work alongside Memor full-touch devices and Magellan at POS."
				),
				"image": workflows,
				"image_alt": "Skorpio used for warehouse, shop-floor and parcel scanning",
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
				"heading": "Watch Datalogic Skorpio X40/X45",
				"body": (
					"Official Datalogic film for the next-generation key-based mobile computer "
					"built for all-day warehouse operations — compact, ergonomic and ready for "
					"picking, replenishment and goods movement."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic Skorpio X40/X45 handheld and pistol-grip models",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Ergonomic keys and a detachable handle",
				"body": (
					"Three layouts — 29, 39 or 48 keys — are spaced for gloves and high-frequency "
					"data entry when a touchscreen slows the line. The handle comes off in the "
					"field so the same device works as a handheld or a pistol grip."
				),
				"image": workflows,
				"image_alt": "Skorpio X40/X45 handheld and pistol-grip use",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "X40 Wi-Fi 6E or X45 with 5G",
				"body": (
					"Every Skorpio X40/X45 has Wi-Fi 6/6E (2×2 MU-MIMO, WPA3 Enterprise), "
					"Bluetooth 5.3 and NFC.\n\n"
					"Skorpio X45 adds 5G FR1, dual-band GNSS (L1+L5), Nano SIM + eSIM and a "
					"barometer for yard, campus and outdoor-adjacent work. Do not specify 5G "
					"unless you need the X45."
				),
				"image": wireless,
				"image_alt": "Skorpio X45 5G and Wi-Fi 6E certified Android platform",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Green Spot scanning and all-day power",
				"body": (
					"Halogen DE2121-DL or extended-range DE2121-ER read 1D and 2D codes with "
					"Green Spot on the label. A 13 MP camera covers exceptions.\n\n"
					"The 7,000 mAh pack hot-swaps. Charge on contacts or Qi EPP 10 W wireless "
					"to avoid pin wear. New 4-slot docks are shared with Falcon X60/X65; "
					"Skorpio X5 single docks still fit."
				),
				"image": dock,
				"image_alt": "Skorpio X40/X45 in docks with Green Spot scan confirmation",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Android 15, Mobility Suite and Datalogic Connect",
				"body": (
					"Android 15 with GMS ships Android Enterprise Recommended and is specified "
					"as upgradeable to Android 19. Mobility Suite covers Shield security, kiosk "
					"Launcher, staging and OEMConfig for SOTI, Intune, Workspace ONE and Ivanti.\n\n"
					"Datalogic Connect is the cloud IoT layer for fleet visibility. The platform "
					"sits with Memor, Smart Portal and PowerScan in Datalogic’s current GS1-ready "
					"warehouse and retail portfolio."
				),
				"image": connect,
				"image_alt": "Skorpio X40/X45 Datalogic Connect and Mobility Suite",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Saudi Arabia specification and support",
				"body": (
					"Printechs helps choose X40 vs X45, keyboard, standard vs long-range imager, "
					"handheld vs pistol and dock type for warehouses and plants in Riyadh, "
					"Jeddah and Dammam.\n\n"
					"ERP Items can be linked later under ERP Item Link without changing this URL. "
					"EASEOFCARE and Datalogic Shield cover Android security patches and OS."
				),
				"image": rugged,
				"image_alt": "Skorpio X40/X45 rugged construction for industrial temperatures",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "device",
				"title": "Model selection",
				"description": "Confirm X40 Wi-Fi vs X45 5G, 29/39/48 keys, SR vs ER imager, handheld vs pistol.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Docks & accessories",
				"description": "Single or 4-slot charge/Ethernet docks, holster, rubber boot and X5 dock reuse.",
				"sort_order": 2,
			},
			{
				"icon": "cloud",
				"title": "MDM & WMS",
				"description": "Mobility Suite, Datalogic Connect, OEMConfig and terminal emulation for your WMS.",
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
			{"item_description": "Skorpio X40 or X45 (keyboard, optic and grip per configuration)", "sort_order": 1},
			{"item_description": "7,000 mAh battery 94ACC0440", "sort_order": 2},
			{"item_description": "Hand-strap (handheld) or lanyard (pistol grip)", "sort_order": 3},
			{"item_description": "Keyboard overlays", "sort_order": 4},
			{"item_description": "Google Mobile Services on GMS models", "sort_order": 5},
			{"item_description": "Optional dock, holster, rubber boot and handle sold separately", "sort_order": 6},
		],
	)

	related = [
		row
		for row in (
			related_product_row("datalogic-powerscan-9600", 1),
			related_product_row("RET.SYS.DLG.4708", 2),
			related_product_row("RET.SYS.DLG.5029", 3),
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
				"question": "What is the Datalogic Skorpio X40/X45?",
				"answer": (
					"A compact, key-based Android 15 mobile computer for all-day warehouse "
					"operations — picking, replenishment, stock count and goods movement — with "
					"optional detachable pistol grip."
				),
				"sort_order": 1,
			},
			{
				"question": "What is the difference between X40 and X45?",
				"answer": (
					"X40 is Wi-Fi 6/6E, Bluetooth 5.3 and NFC (handheld or pistol). X45 adds 5G, "
					"dual-band GNSS, Nano SIM + eSIM and a barometer. Listed X45 SKUs are pistol grip."
				),
				"sort_order": 2,
			},
			{
				"question": "Which keyboards are available?",
				"answer": (
					"29-key numeric, 39-key functional numeric and 48-key full alphanumeric, "
					"plus two side scan keys. Overlays are included; spare overlay packs are accessories."
				),
				"sort_order": 3,
			},
			{
				"question": "Does every unit include 5G?",
				"answer": "No. Specify Skorpio X45 when you need cellular, GPS or eSIM. X40 is WLAN only.",
				"sort_order": 4,
			},
			{
				"question": "What Android version does it ship with?",
				"answer": (
					"Android 15 with GMS (and AOSP options), Android Enterprise Recommended, "
					"specified as upgradeable to Android 19. Shield covers security patches."
				),
				"sort_order": 5,
			},
			{
				"question": "Can we reuse Skorpio X5 docks?",
				"answer": (
					"Yes for single docks with contacts. New 4-slot charge and Ethernet docks "
					"(94A150143 / 94A150144) are shared with Falcon X60/X65."
				),
				"sort_order": 6,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page was published without an ERP Item. When Items are created, link them "
					"on this Website Product under ERP Item Link. The URL stays "
					"/products/datalogic-skorpio-x40-x45."
				),
				"sort_order": 7,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The official datasheet specifies a 1-year factory warranty. EASEOFCARE and "
					"Datalogic Shield extend service and Android security updates."
				),
				"sort_order": 8,
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
