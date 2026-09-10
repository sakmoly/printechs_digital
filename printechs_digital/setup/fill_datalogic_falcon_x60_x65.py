# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic Falcon X60/X65 (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail-manufacturing-transportation-logistics-healthcare-gs1-digital-link/mobile-computers/falcon-x60-65-pd-1163.html
Datasheet: DS-FALCONX60-X65-EN Rev A 20260421.

Higher-end ultra-rugged warehouse / logistics computer vs Skorpio X40/X45.
X60 is Wi-Fi 6/6E. X65 adds 5G, GPS/GNSS, Nano SIM + eSIM and barometer.
Do not advertise 5G as standard on every Falcon X60.
XLR / 20 m scan and TrueAim are model options — not on every SKU.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

SLUG = "datalogic-falcon-x60-x65"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-falcon-x60-x65.png": "/upload/products/Falcon_700x700.png",
	"datalogic-falcon-x60-x65-1.jpg": "/upload/prod_line2/Falcon/1_2.jpg",
	"datalogic-falcon-x60-x65-2.jpg": "/upload/prod_line2/Falcon/2.jpg",
	"datalogic-falcon-x60-x65-3.jpg": "/upload/prod_line2/Falcon/3.jpg",
	"datalogic-falcon-x60-x65-4.jpg": "/upload/prod_line2/Falcon/4.jpg",
	"datalogic-falcon-x60-x65-5.jpg": "/upload/prod_line2/Falcon/5.jpg",
	"datalogic-falcon-x60-x65-6.jpg": "/upload/prod_line2/Falcon/6.jpg",
	"datalogic-falcon-x60-x65-7.jpg": "/upload/prod_line2/Falcon/7.jpg",
	"datalogic-falcon-x60-x65-8.jpg": "/upload/prod_line2/Falcon/8.jpg",
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
	doc.website_product_name = "Datalogic Falcon X60/X65"
	doc.display_name = "Datalogic Falcon X60/X65"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic Falcon X60/X65 ultra-rugged warehouse mobile computer."
	doc.long_description = "<p>Datalogic Falcon X60/X65 ultra-rugged warehouse mobile computer.</p>"
	doc.hero_image = official_image("datalogic-falcon-x60-x65.png")
	return doc


def fill_datalogic_falcon_x60_x65():
	doc = get_or_create()

	hero = official_image("datalogic-falcon-x60-x65.png")
	yard = official_image("datalogic-falcon-x60-x65-1.jpg")
	xlr = official_image("datalogic-falcon-x60-x65-2.jpg")
	greenspot = official_image("datalogic-falcon-x60-x65-3.jpg")
	outdoor = official_image("datalogic-falcon-x60-x65-4.jpg")
	wireless = official_image("datalogic-falcon-x60-x65-5.jpg")
	connect = official_image("datalogic-falcon-x60-x65-6.jpg")
	platform = official_image("datalogic-falcon-x60-x65-7.jpg")
	warehouse = official_image("datalogic-falcon-x60-x65-8.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")

	# Intentionally no Item — link later under ERP Item Link when the Item exists.
	doc.item = None
	doc.website_product_name = "Datalogic Falcon X60/X65"
	doc.display_name = "Datalogic Falcon X60/X65"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "ULTRA-RUGGED MOBILE COMPUTER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Built for hard work, heavy input and the highest shelves"
	doc.short_description = (
		"Datalogic Falcon X60/X65 is Datalogic’s latest ultra-rugged Android computer for "
		"demanding warehouse and logistics work. A 4.3\" 600-nit display, up to 53 backlit "
		"keys, TrueAim two-stage trigger and optional XLR reading to 20 m sit on an IP65/IP68 "
		"body with 2.8 m drop rating — a step up from compact key-based models."
	)
	doc.long_description = (
		"<p>Falcon X60/X65 is Datalogic’s current ultra-rugged mobile-computing family for "
		"scan-heavy warehouses, yards, ports and transportation hubs. It is built for "
		"continuous data capture and heavy keying — not for the checkout lane.</p>"
		"<p>Compared with compact devices such as Skorpio X40/X45, Falcon adds a brighter "
		"4.3\" WVGA display (600 nits, Gorilla Glass Victus), 8 GB RAM / 128 GB UFS, "
		"IP65/IP68 sealing, 2.8 m ambient drops, 4,000 tumbles and optional extra-long-range "
		"imaging to 20 m with Green Spot visible to 10 m on XLR.</p>"
		"<p>TrueAim™ is a professional two-stage trigger for precise long-distance aiming. "
		"Standard (DE2121-DL), extended-range (DE2121-ER) and XLR (DE2172) engines are "
		"offered — confirm the optic; 20 m is the XLR class, not every SKU.</p>"
		"<p>Three backlit keyboards (31 numeric, 41 functional numeric, 53 alphanumeric) "
		"and a field-detachable handle cover glove work on the floor or from a truck. "
		"Cameras are 13 MP rear plus 8 MP front.</p>"
		"<p>Qualcomm Dragonwing™ 4490 octa-core 2.4 GHz runs Android 15 (GMS / AOSP), "
		"Android Enterprise Recommended, with a published path to Android 19. Datalogic "
		"cites up to 10 years of OS support on the official product page.</p>"
		"<p>X60 is Wi-Fi 6/6E, Bluetooth 5.3 and NFC. X65 adds 5G FR1, dual-band GNSS, "
		"Nano SIM + eSIM and a barometer. Listed X65 configurations are pistol-grip XLR. "
		"The 7,000 mAh pack hot-swaps and charges by contacts or Qi EPP 10 W. Docks are "
		"shared with Skorpio X40/X45 and remain compatible with Skorpio X5 singles.</p>"
		"<p>Printechs specifies and supports Falcon X60/X65 in Saudi Arabia — Riyadh, "
		"Jeddah and Dammam — including optic, keyboard, Wi-Fi vs 5G, docks and EASEOFCARE.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = (
		"Datalogic Falcon X60/X65 handheld and pistol-grip ultra-rugged mobile computers"
	)
	doc.video_url = ""
	doc.hero_trust_chips = (
		"IP65 / IP68 · 2.8 m drop\n"
		"XLR scanning up to 20 m\n"
		"8 GB / 128 GB · Android 15\n"
		"Wi-Fi 6E · 5G on X65"
	)
	doc.story_heading = "Ultra-rugged computing for the highest shelves and hardest shifts"
	doc.visual_story_heading = "Falcon X60/X65 in warehouse and yard work"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "Falcon X60/X65"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Ultra-rugged warehouse computer: 4.3\" 600-nit display, up to 53 keys, TrueAim, "
		"optional XLR to 20 m, IP65/IP68 and 5G on X65."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify Falcon X60/X65 for demanding warehouse fleets"
	doc.final_cta_description = (
		"Printechs can confirm X60 Wi-Fi or X65 5G, standard / long-range / XLR optics, "
		"keyboard and docks for high-intensity sites in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Falcon X60/X65 Rugged Warehouse Computer | Printechs"
	doc.meta_description = (
		"Datalogic Falcon X60/X65 ultra-rugged Android computer for warehouse and logistics: "
		"XLR to 20 m, TrueAim, IP65/IP68, 53-key options, Wi-Fi 6E and 5G on X65. From Printechs in KSA."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "rugged",
				"title": "Ultra-rugged, not compact-duty",
				"description": (
					"IP65/IP68 with battery, 2.8 m ambient drops, 2.4 m across −20 to 50 °C "
					"and 4,000 one-metre tumbles — built for docks, yards and high bays."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "From the floor to 20 metres",
				"description": (
					"Choose standard, long-range or XLR (Halogen DE2172). XLR reads to about "
					"20 m with Green Spot visible to 10 m. TrueAim two-stage trigger cuts misreads."
				),
				"sort_order": 2,
			},
			{
				"icon": "inventory",
				"title": "Heavy input, glove-ready keys",
				"description": (
					"31, 41 or 53 backlit keys with large spacing — faster than a touchscreen "
					"for scan-and-key work on receiving, picking and truck loading."
				),
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Indoor Wi-Fi 6E, outdoor 5G",
				"description": (
					"X60 stays on Wi-Fi 6/6E, Bluetooth 5.3 and NFC. Specify X65 when the "
					"yard or campus needs 5G, GNSS and eSIM."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Yard and port range",
				"image": yard,
				"image_alt": "Falcon X60/X65 extra-long-range scanning in a container yard",
				"caption": "XLR optics and TrueAim for labels on the highest shelves and across the yard.",
				"sort_order": 1,
			},
			{
				"label": "High-bay warehouse",
				"image": xlr,
				"image_alt": "Falcon X60/X65 long-range scan up warehouse racking",
				"caption": "Barcode capture up to 20 m on XLR models — less travel, more throughput.",
				"sort_order": 2,
			},
			{
				"label": "Green Spot confirmation",
				"image": greenspot,
				"image_alt": "Falcon X60/X65 Green Spot good-read on a parcel label",
				"caption": "Green Spot on the label, visible up to 10 m on extra-long-range engines.",
				"sort_order": 3,
			},
			{
				"label": "Connect and Mobility Suite",
				"image": connect,
				"image_alt": "Falcon X60/X65 with Datalogic Connect and Mobility Suite",
				"caption": "Stage, lock down and watch the fleet with Mobility Suite and Datalogic Connect.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "rugged",
				"title": "IP65 / IP68",
				"description": "2.8 m ambient drop · 4,000 tumbles",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "XLR to 20 m",
				"description": "DE2121-DL / ER / DE2172 · TrueAim",
				"sort_order": 2,
			},
			{
				"icon": "display",
				"title": "4.3\" 600 nits",
				"description": "WVGA · Gorilla Glass Victus",
				"sort_order": 3,
			},
			{
				"icon": "android",
				"title": "Android 15",
				"description": "8 GB / 128 GB · path to Android 19",
				"sort_order": 4,
			},
			{
				"icon": "battery",
				"title": "7,000 mAh",
				"description": "Hot-swap · Qi EPP 10 W wireless",
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
				("Family", "Falcon X60/X65 ultra-rugged industrial handheld computer"),
				("X60", "Wi-Fi 6/6E handheld or pistol grip (listed SKUs 946600xxx)"),
				("X65", "Wi-Fi 6E + 5G pistol-grip XLR models (listed SKUs 946650xxx)"),
				("Processor", "Qualcomm Dragonwing 4490 octa-core 2.4 GHz"),
				("Memory", "8 GB RAM; 128 GB UFS flash"),
				("Expansion", "MicroSD up to 2 TB"),
				("OS", "Android 15 GMS and AOSP; platform upgradeable to Android 19"),
				("OS lifecycle", "Official page: up to 10 years of operating-system updates"),
				("Enterprise", "Android Enterprise Recommended; GMS certified"),
				("Display", "4.3\" LCD A-Si IPS WVGA 480 × 800; 600 nits typical"),
				("Touch", "5-point capacitive; Gorilla Glass Victus; gloves and stylus"),
				("Keyboards", "31-key numeric; 41-key functional numeric; 53-key alphanumeric; backlight"),
				("Other keys", "2 side scan keys; power; 3 Android soft keys"),
				("Trigger", "TrueAim professional two-stage trigger"),
				("Handle", "Field-detachable pistol grip (94ACC0446)"),
				("Cameras", "13 MP rear autofocus + torch; 8 MP front fixed focus"),
				("Audio", "Dual mics with noise cancellation; hands-free speaker"),
			],
		),
		(
			"Scanning & sensors",
			[
				("Standard", "Halogen DE2121-DL 1D/2D"),
				("Long range", "Halogen DE2121-ER extended-range 1D/2D"),
				("XLR", "Halogen DE2172 extra-long-range 1D/2D; typical reads to 20 m"),
				("Good-read", "Green Spot on all engines; visible up to 10 m on XLR"),
				("Note", "20 m / 10 m Green Spot apply to XLR configurations, not every SKU"),
				("Accelerometer", "3-axis orientation"),
				("Other sensors", "Gyroscope, ambient light, proximity, magnetometer"),
				("Barometer", "Atmospheric / Z-location on Falcon X65 only"),
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
				("WWAN", "X65 only: 3G / LTE-A / 5G FR1, data only, private network / CBRS"),
				("SIM", "X65 only: 1 Nano SIM + 1 eSIM"),
				("GNSS", "X65 only: GPS, Galileo, GLONASS, BeiDou; L1 + L5; A-GPS"),
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
				("Shared docks", "4-slot charge 94A150143; 4-slot Ethernet 94A150144 (with Skorpio X40/X45)"),
				("Single dock", "94A150151 contacts; backward-compatible with Skorpio X5 docks"),
				("Battery pack P/N", "94ACC0440 (shared with Skorpio X40/X45)"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Handheld size", "232 × 80 × 42 mm / 9.13 × 3.15 × 1.65 in"),
				("Pistol size", "232 × 80 × 165 mm / 9.13 × 3.15 × 6.50 in"),
				("Weight", "Handheld 550 g; pistol grip XLR 700 g, with battery"),
				("Drop ambient", "Multiple 2.8 m / 9.2 ft to concrete, MIL-STD-810H"),
				("Drop operating", "Multiple 2.4 m / 7.9 ft, −20 to 50 °C, MIL-STD-810H"),
				("Tumble", "4,000 × 1.0 m at room temperature, IEC 60068-2-32"),
				("Sealing", "IP65 and IP68 with battery, IEC 60529"),
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
				"title": "High-bay warehouse and forklift work",
				"description": (
					"XLR and long-range optics cut travel in tall racking. TrueAim steadies "
					"reads from a truck or the floor."
				),
				"image": xlr,
				"image_alt": "Falcon X60/X65 scanning high warehouse racking",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Yards, ports and outdoor docks",
				"description": (
					"IP68, 600-nit display and X65 5G/GNSS keep the device online between "
					"the shed and the container row."
				),
				"image": yard,
				"image_alt": "Falcon X60/X65 used in a container terminal yard",
				"industry_link": "warehouse-logistics",
				"sort_order": 2,
			},
			{
				"title": "Manufacturing intralogistics and kitting",
				"description": (
					"Heavy-input keys and rugged sealing for receiving, put-away, work orders "
					"and traceability on the shop floor."
				),
				"image": packaging,
				"image_alt": "Manufacturing and packaging line mobile data capture",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Healthcare warehouse and batch tracking",
				"description": (
					"Receiving, quality check, fulfilment and returns where batch accuracy matters."
				),
				"image": pharma,
				"image_alt": "Pharmaceutical warehouse inventory identification",
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
				"heading": "Datalogic’s latest ultra-rugged warehouse computer",
				"body": (
					"Falcon X60/X65 is the current flagship key-based family for hard work, "
					"heavy input and the highest shelves. It sits above compact models such as "
					"Skorpio when you need more drop, more sealing, a brighter 4.3\" display, "
					"8 GB RAM and extra-long-range scanning."
				),
				"image": hero,
				"image_alt": "Datalogic Falcon X60/X65 handheld and pistol-grip models",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Confident scanning at every distance",
				"body": (
					"Standard, long-range and XLR Halogen engines all include Green Spot. "
					"On XLR, confirmation stays visible out to about 10 m and codes can be "
					"taken from around 20 m.\n\n"
					"TrueAim is a two-stage trigger: aim, then fire — fewer wasted walks back "
					"to the pallet. Specify the optic; not every Falcon ships XLR."
				),
				"image": greenspot,
				"image_alt": "Falcon Green Spot good-read feedback on a shipping label",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "X60 Wi-Fi 6E or X65 with 5G",
				"body": (
					"Every Falcon has Wi-Fi 6/6E (2×2 MU-MIMO, WPA3 Enterprise), Bluetooth 5.3 "
					"and NFC.\n\n"
					"Falcon X65 adds 5G FR1, dual-band GNSS (L1+L5), Nano SIM + eSIM and a "
					"barometer for yard, campus and outdoor-adjacent work. Listed X65 SKUs "
					"are pistol-grip XLR. Do not specify 5G unless you need the X65."
				),
				"image": wireless,
				"image_alt": "Falcon X65 Wi-Fi 6E and 5G connectivity",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "All-day power and shared docks",
				"body": (
					"The 7,000 mAh pack hot-swaps for 24/7. Charge on contacts or Qi EPP 10 W "
					"wireless to avoid pin wear.\n\n"
					"New 4-slot charge and Ethernet docks (94A150143 / 94A150144) are shared "
					"with Skorpio X40/X45. Skorpio X5 single docks still fit — upgrading the "
					"gun does not force a full cradle rip-out."
				),
				"image": warehouse,
				"image_alt": "Falcon X60/X65 handheld and pistol-grip units in warehouse use",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Android 15, Mobility Suite and Datalogic Connect",
				"body": (
					"Android 15 with GMS ships Android Enterprise Recommended and is specified "
					"as upgradeable to Android 19. The official page cites up to 10 years of "
					"OS updates. Mobility Suite covers Shield, kiosk Launcher, staging and "
					"OEMConfig for SOTI, Intune, Workspace ONE and Ivanti.\n\n"
					"Datalogic Connect is the cloud IoT layer. Falcon sits with Skorpio, Memor "
					"and PowerScan in Datalogic’s current GS1-ready warehouse portfolio."
				),
				"image": connect,
				"image_alt": "Falcon X60/X65 Datalogic Connect and Mobility Suite",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Saudi Arabia specification and support",
				"body": (
					"Printechs helps choose X60 vs X65, keyboard, standard vs long-range vs "
					"XLR, handheld vs pistol and dock type for warehouses, plants and yards "
					"in Riyadh, Jeddah and Dammam.\n\n"
					"ERP Items can be linked later under ERP Item Link without changing this URL. "
					"EASEOFCARE and Datalogic Shield cover Android security patches and OS."
				),
				"image": outdoor,
				"image_alt": "Falcon X60/X65 outdoor logistics scanning",
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
				"description": "Confirm X60 Wi-Fi vs X65 5G, 31/41/53 keys, DL / ER / XLR optic, handheld vs pistol.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Docks & accessories",
				"description": "Shared Skorpio/Falcon 4-slot docks, X5 single-dock reuse, holster 94ACC0444 and boot.",
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
			{"item_description": "Falcon X60 or X65 (keyboard, optic and grip per configuration)", "sort_order": 1},
			{"item_description": "7,000 mAh battery 94ACC0440", "sort_order": 2},
			{"item_description": "Hand-strap (handheld) or lanyard (pistol grip)", "sort_order": 3},
			{"item_description": "Keyboard overlays", "sort_order": 4},
			{"item_description": "Google Mobile Services on GMS models", "sort_order": 5},
			{"item_description": "Optional dock, holster 94ACC0444, rubber boot and handle 94ACC0446 sold separately", "sort_order": 6},
		],
	)

	related = [
		row
		for row in (
			related_product_row("datalogic-skorpio-x40-x45", 1),
			related_product_row("datalogic-powerscan-9600", 2),
			related_product_row("RET.SYS.DLG.4708", 3),
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
				"question": "What is the Datalogic Falcon X60/X65?",
				"answer": (
					"Datalogic’s latest ultra-rugged key-based Android 15 computer for demanding "
					"warehouse and logistics work — high bays, docks, yards and heavy scan-and-key "
					"shifts. It is the higher-end family above compact models such as Skorpio X40/X45."
				),
				"sort_order": 1,
			},
			{
				"question": "How is Falcon different from Skorpio X40/X45?",
				"answer": (
					"Falcon is larger and tougher: 4.3\" 600-nit display, 8 GB RAM, IP65/IP68, "
					"2.8 m ambient drops, 4,000 tumbles, optional XLR to 20 m, TrueAim two-stage "
					"trigger, 53-key backlight and a front camera. Skorpio is the compact all-day key-based option."
				),
				"sort_order": 2,
			},
			{
				"question": "What is the difference between X60 and X65?",
				"answer": (
					"X60 is Wi-Fi 6/6E, Bluetooth 5.3 and NFC (handheld or pistol). X65 adds 5G, "
					"dual-band GNSS, Nano SIM + eSIM and a barometer. Listed X65 SKUs are pistol-grip XLR."
				),
				"sort_order": 3,
			},
			{
				"question": "Does every Falcon read 20 metres?",
				"answer": (
					"No. About 20 m and Green Spot to 10 m are specified for the XLR (DE2172) "
					"engine. Standard and long-range imagers are shorter. Confirm the optic on the SKU."
				),
				"sort_order": 4,
			},
			{
				"question": "Does every unit include 5G?",
				"answer": "No. Specify Falcon X65 when you need cellular, GPS or eSIM. X60 is WLAN only.",
				"sort_order": 5,
			},
			{
				"question": "Can we reuse Skorpio docks?",
				"answer": (
					"Yes. 4-slot charge/Ethernet docks are shared with Skorpio X40/X45. "
					"Skorpio X5 single docks with contacts remain compatible."
				),
				"sort_order": 6,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page was published without an ERP Item. When Items are created, link them "
					"on this Website Product under ERP Item Link. The URL stays "
					"/products/datalogic-falcon-x60-x65."
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
