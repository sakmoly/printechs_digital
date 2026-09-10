# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic Magellan 9900i (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail-gs1-digital-link/fixed-retail-scanners/magellan-9900i-pd-924.html
Datasheet: DS-MAGELLAN-9900i-EN Revision H.

AI cameras, TPU and PoE switch are optional / variant features — not standard
on every 9900i. Base QuadVision scanning is standard.
"""

from pathlib import Path
from urllib.request import Request, urlopen

import frappe

SLUG = "datalogic-magellan-9900i"
VIDEO_URL = "https://youtu.be/U156EEyY7Ng"
SCAN_VIDEO = "https://youtu.be/zdkRjyV8kEE"
GS1_VIDEO = "https://youtu.be/Hd0NZLkkA7M"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-magellan-9900i.png": "/upload/products/Magellan%209900i.png",
	"datalogic-magellan-9900i-ai.jpg": "/upload/prod_line2/Magellan9900/1.jpg",
	"datalogic-magellan-9900i-loss-prevention.jpg": "/upload/prod_line2/Magellan9900/2.jpg",
	"datalogic-magellan-9900i-poe.jpg": "/upload/prod_line2/Magellan9900/3.jpg",
	"datalogic-magellan-9900i-gs1.jpg": "/upload/prod_line2/Magellan9900/4.jpg",
}


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


def get_or_create():
	existing = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = SLUG
	doc.website_product_name = "Datalogic Magellan 9900i"
	doc.display_name = "Datalogic Magellan 9900i"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic Magellan 9900i in-counter multi-plane scanner."
	doc.long_description = "<p>Datalogic Magellan 9900i in-counter multi-plane scanner.</p>"
	doc.hero_image = official_image("datalogic-magellan-9900i.png")
	return doc


def fill_datalogic_magellan_9900i():
	doc = get_or_create()

	hero = official_image("datalogic-magellan-9900i.png")
	ai = official_image("datalogic-magellan-9900i-ai.jpg")
	lp = official_image("datalogic-magellan-9900i-loss-prevention.jpg")
	poe = official_image("datalogic-magellan-9900i-poe.jpg")
	gs1 = official_image("datalogic-magellan-9900i-gs1.jpg")

	# Intentionally no Item — link later under ERP Item Link when the Item exists.
	doc.item = None
	doc.website_product_name = "Datalogic Magellan 9900i"
	doc.display_name = "Datalogic Magellan 9900i Barcode Scanner"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Barcode Scanners"
	doc.category_label = "IN-COUNTER MULTI-PLANE SCANNER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Real-time AI, on-device by design — nothing else required"
	doc.short_description = (
		"The Datalogic Magellan 9900i is an in-counter multi-plane imaging scanner "
		"(scanner-only or scanner/scale) for high-throughput assisted and self-checkout. "
		"QuadVision™ four-camera imaging, a low 6.8 cm bonnet, optional Top-Down Reader "
		"for 6-sided reading, GS1 Digital Link and Digimarc keep checkout fast today and "
		"ready for AI loss-prevention variants."
	)
	doc.long_description = (
		"<p>The Magellan 9900i is Datalogic’s next-generation in-counter scanner for "
		"assisted lanes and self-checkout. Official series models are scanner-only "
		"(9910 / 9911 / 9912) and scanner/scale (9921 / 9922), in short, medium and long "
		"platters with shelf or flange mounts.</p>"
		"<p>QuadVision uses an IMX8 multi-core processor and four cameras (two horizontal, "
		"two vertical) for 5-sided capture and up to 50% faster 2D reading versus legacy "
		"Magellan models. An optional Top-Down Reader (7\", 9\" or 12.4\") adds a sixth "
		"view and about 20% more scan volume. A Customer-Facing Reader option lets shoppers "
		"scan loyalty cards and coupons themselves.</p>"
		"<p>Every 9900i is GS1 Digital Link and Digimarc ready. Traditional shrink tools "
		"— ScaleSentry, ScanSentry, All-Weighs platter and EAS interlock — are available "
		"on the base barcode-scanning configuration.</p>"
		"<p>AI-enabled variants add Edge loss prevention (produce recognition, mis-scan, "
		"label switching, multiple items) with optional color cameras, a TPU / neural "
		"processor and a PoE switch. Those are not standard on every 9900i — confirm the "
		"variant before specifying.</p>"
		"<p>Printechs supplies and supports Datalogic Magellan checkout scanners in Saudi "
		"Arabia, including Riyadh, Jeddah and Dammam — model selection, TDR/CFR, scale, "
		"POS interface, lane layout and after-sales service.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Magellan 9900i in-counter multi-plane barcode scanner"
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"QuadVision 5-sided imaging\n"
		"GS1 Digital Link + Digimarc\n"
		"Optional 6-sided TDR\n"
		"1-year factory warranty"
	)
	doc.story_heading = "In-counter scanning built for throughput and shrink control"
	doc.visual_story_heading = "Magellan 9900i at assisted and self-checkout"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "Magellan 9900i"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"In-counter multi-plane scanner/scale with QuadVision imaging, GS1 Digital Link, "
		"Digimarc and optional TDR, scale and Edge AI loss prevention for grocery POS and SCO."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify Magellan 9900i for your checkout lanes"
	doc.final_cta_description = (
		"Printechs can confirm platter length, TDR, scale, interface and whether you need "
		"the barcode-only or AI loss-prevention Magellan 9900i in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Magellan 9900i In-Counter Scanner Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Magellan 9900i in-counter multi-plane scanner/scale with QuadVision, "
		"GS1 Digital Link, optional TDR and Edge AI loss prevention. Available in Saudi Arabia from Printechs."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "speed",
				"title": "Faster 2D checkout",
				"description": (
					"QuadVision IMX8 processing and four cameras deliver up to 50% faster 2D "
					"reads than legacy Magellan models, including damaged and hard-to-read codes."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "5-sided, optional 6-sided",
				"description": (
					"Standard 5-sided capture; add a 7\", 9\" or 12.4\" Top-Down Reader for "
					"true 6-sided reading without turning the item."
				),
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Ready for modern codes",
				"description": "GS1 Digital Link, Digimarc, QR, Data Matrix and stacked GS1 codes on pack or phone.",
				"sort_order": 3,
			},
			{
				"icon": "shield",
				"title": "Shrink tools, optional AI",
				"description": (
					"ScaleSentry, ScanSentry and EAS on the base platform; Edge AI produce, "
					"mis-scan and label-switch detection on AI-enabled variants only."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Grocery checkout",
				"image": gs1,
				"image_alt": "Datalogic Magellan 9900i scanning GS1 and 2D codes at grocery POS",
				"caption": "Assisted lanes and self-checkout with GS1 Digital Link and Digimarc.",
				"sort_order": 1,
			},
			{
				"label": "Edge AI variants",
				"image": ai,
				"image_alt": "Datalogic Magellan 9900i AI-enabled checkout scanner",
				"caption": "Optional on-device neural processing — no extra server required.",
				"sort_order": 2,
			},
			{
				"label": "Loss prevention",
				"image": lp,
				"image_alt": "Datalogic Magellan 9900i label-switching and mis-scan detection",
				"caption": "AI variants detect mis-scans, label switches and stacked items.",
				"sort_order": 3,
			},
			{
				"label": "PoE camera hub",
				"image": poe,
				"image_alt": "Datalogic Magellan 9900i optional built-in PoE Ethernet switch",
				"caption": "Optional 7-port PoE switch for integrated and overhead cameras.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "scan",
				"title": "QuadVision",
				"description": "IMX8 · 4 cameras · 5-sided capture",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "TDR option",
				"description": "7\" / 9\" / 12.4\" for 6-sided reading",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "POS interfaces",
				"description": "OEM USB · RS-232 · Ethernet",
				"sort_order": 3,
			},
			{
				"icon": "store",
				"title": "6.8 cm bonnet",
				"description": "Low profile for ADA-friendly checkstands",
				"sort_order": 4,
			},
			{
				"icon": "battery",
				"title": "9.3 W",
				"description": "Nominal operating · 7.3 W sleep @ 12 VDC",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "1-year warranty",
				"description": "Standard factory warranty · EASEOFCARE options",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Scanner",
			[
				("Family", "Magellan 9900i in-counter multi-plane imager"),
				("Scanner-only models", "9910, 9911, 9912"),
				("Scanner/scale models", "9921, 9922"),
				("Imaging", "QuadVision IMX8 multi-core; 4 cameras (2 horizontal, 2 vertical)"),
				("Scan coverage", "5-sided standard; 6-sided with optional TDR"),
				("Illumination", "Multiple diffused LEDs optimized for eye comfort"),
				("Indicators", "Good-read LEDs all planes; 85 dB speaker, WAV files"),
				("OS on device", "Embedded Linux"),
				("Bonnet height", "6.8 cm / 2.7 in above counter"),
			],
		),
		(
			"Decoding",
			[
				("1D / retail", "EAN/JAN/UPC, Code 128, GS1 DataBar linear and stacked"),
				("Stacked / composite", "EAN/JAN, GS1 DataBar, UPC A/E composites; PDF417; MicroPDF417"),
				("2D codes", "Aztec, Data Matrix, QR, Micro QR"),
				("Digital watermarks", "Digimarc Barcode"),
				("Next-gen IDs", "GS1 Digital Link and future GS1 codes"),
			],
		),
		(
			"Interfaces & power",
			[
				("Host interfaces", "OEM (IBM) USB Plus Power; RS-232 scanner/scale; single-cable RS-232"),
				("POS software", "Windows 10, Linux, Android via OPOS / JavaPOS"),
				("Auxiliary ports", "2× powered USB-A; powered RS-232; remote scale display; EAS"),
				("Ethernet", "1× Ethernet standard; optional 7-port IEEE1588 switch (48 V brick)"),
				("Scanner power", "12 VDC; 9.3 W nominal; 7.3 W sleep"),
				("AC brick (optional)", "100–240 VAC, 50–60 Hz"),
				("Configuration", "Magellan Aladdin"),
				("Remote management", "WMI / MBeans; IBM Director; Wavelink Avalanche"),
			],
		),
		(
			"Scale, TDR & accessories",
			[
				("Single-interval scale", "0–15 kg / 0–30 lb; 0.005 kg / 0.010 lb increment"),
				("Dual-interval scale", "0–6 kg then 6–15 kg (0.002 / 0.005 kg increments)"),
				("Adaptive scale", "Supports Bizerba, Mettler Toledo and Digi"),
				("All-Weighs platter", "Horizontal plus vertical bonnet weighing surface"),
				("TDR 7 in", "90ACC0417 — 17.8 cm"),
				("TDR 9 in", "90ACC0418 — 22.8 cm"),
				("TDR 12.4 in", "90ACC0419 — 31.5 cm"),
				("CFR", "Optional Customer-Facing Reader on TDR for loyalty and coupons"),
			],
		),
		(
			"Loss prevention & AI variants",
			[
				("ScaleSentry", "Infrared beam detects produce hanging off the platter"),
				("ScanSentry", "Alerts POS if an item crosses the platter with no barcode read"),
				("EAS", "Checkpoint / Nedap antenna; Sensormatic via SmartSentry"),
				("AI suite (variant)", "Produce recognition, mis-scan, label switching, multiple items"),
				("AI hardware (variant)", "Color cameras, TPU / neural processor, optional PoE switch"),
				("Note", "AI cameras, TPU and PoE switch are not standard on every 9900i"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Width", "29.2 cm / 11.5 in"),
				("Below counter", "10.6 cm / 4.0 in"),
				("Platter length", "Short 35.2 cm · Medium 39.9 cm · Long 43.7 cm"),
				("Ambient light", "0–86,080 lux"),
				("ESD", "25 kV air discharge"),
				("Humidity", "5–95% non-condensing"),
				("Operating temperature", "10 to 40 °C"),
				("Storage / transport", "−40 to 70 °C"),
				("Compliance", "China RoHS, EU RoHS, REACH"),
				("Warranty", "1-year standard factory warranty"),
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
				"title": "Assisted grocery checkout",
				"description": "High-throughput cashier lanes with 5- or 6-sided reading and optional scale.",
				"image": gs1,
				"image_alt": "Datalogic Magellan 9900i at grocery POS",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Self-checkout",
				"description": "Low bonnet, large scan volume and ScanSentry for SCO lanes.",
				"image": lp,
				"image_alt": "Datalogic Magellan 9900i self-checkout scanning",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Loss-prevention lanes",
				"description": "ScaleSentry/EAS on the base unit; Edge AI variants for produce and mis-scan detection.",
				"image": ai,
				"image_alt": "Datalogic Magellan 9900i AI loss prevention",
				"industry_link": "retail",
				"sort_order": 3,
			},
			{
				"title": "Loyalty and mobile codes",
				"description": "Optional Customer-Facing Reader for coupons, loyalty and GS1 Digital Link on phones.",
				"image": gs1,
				"image_alt": "Datalogic Magellan 9900i GS1 Digital Link checkout",
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
				"heading": "Watch Magellan 9600i and 9900i",
				"body": (
					"Official Datalogic films cover the 9600i/9900i generation and scan performance. "
					"The 9900i is the in-counter multi-plane model with QuadVision, optional TDR and "
					"AI-ready variants."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic Magellan 9900i in-counter scanner",
				"link_label": "Scanning performance on YouTube",
				"link_href": SCAN_VIDEO,
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "QuadVision and the optional Top-Down Reader",
				"body": (
					"Four cameras and an IMX8 processor capture 5 sides as items cross the platter. "
					"Add a 7\", 9\" or 12.4\" TDR for a sixth view and about 20% more volume. "
					"A Customer-Facing Reader on the TDR lets shoppers scan phones and coupons."
				),
				"image": hero,
				"image_alt": "Datalogic Magellan 9900i with Top-Down Reader",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "GS1 Digital Link and Digimarc",
				"body": (
					"The 9900i is specified for GS1 Digital Link and Digimarc digital watermarks "
					"as well as QR, Data Matrix and stacked GS1 codes — printed or on a phone."
				),
				"video_url": GS1_VIDEO,
				"image": gs1,
				"image_alt": "Datalogic Magellan 9900i GS1 Digital Link scanning",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Base shrink tools vs AI-enabled variants",
				"body": (
					"Standard options include ScaleSentry infrared platter watch, ScanSentry no-read "
					"alerts, All-Weighs platter and Checkpoint/Nedap EAS.\n\n"
					"AI-enabled 9900i models add on-device produce recognition, mis-scan, label "
					"switching and stacked-item detection using optional color cameras, a TPU and "
					"a PoE switch. Confirm the variant — those extras are not on every 9900i."
				),
				"image": lp,
				"image_alt": "Datalogic Magellan 9900i loss-prevention scanning",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "POS integration and Saudi Arabia support",
				"body": (
					"Host links are OEM USB Plus Power, RS-232 and Ethernet. Configure with Magellan "
					"Aladdin; OPOS and JavaPOS cover Windows, Linux and Android POS.\n\n"
					"Printechs can specify platter length, TDR/CFR, scale interval and interface "
					"for grocery and SCO lanes in Riyadh, Jeddah and Dammam. An ERP Item can be "
					"linked later under ERP Item Link without changing this URL."
				),
				"image": poe,
				"image_alt": "Datalogic Magellan 9900i ports and optional PoE switch",
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "store",
				"title": "Lane & model selection",
				"description": "Confirm 991x scanner-only vs 992x scanner/scale, platter length and TDR height.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Checkstand fit",
				"description": "Shelf or flange mount, 6.8 cm bonnet, ScaleSentry produce rail and ADA layout.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "POS & AI options",
				"description": "USB / RS-232 / Ethernet, Aladdin, and whether the lane needs Edge AI hardware.",
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
			{"item_description": "Magellan 9900i scanner or scanner/scale (configuration dependent)", "sort_order": 1},
			{"item_description": "Optional TDR 90ACC0417 / 0418 / 0419 (7\" / 9\" / 12.4\")", "sort_order": 2},
			{"item_description": "Optional Customer-Facing Reader on TDR", "sort_order": 3},
			{"item_description": "Optional scale display 90ACC0340 / 90ACC0343", "sort_order": 4},
			{"item_description": "Power brick, USB or RS-232 cable per kit", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4981", 1),
			related_product_row("RET.SYS.DLG.4885", 2),
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
				"question": "What is the Datalogic Magellan 9900i?",
				"answer": (
					"An in-counter multi-plane imaging scanner or scanner/scale for high-throughput "
					"assisted and self-checkout, using QuadVision four-camera capture."
				),
				"sort_order": 1,
			},
			{
				"question": "Does every 9900i include AI loss prevention?",
				"answer": (
					"No. Produce recognition, mis-scan, label switching and stacked-item AI need "
					"the AI-enabled variant (color cameras, TPU, optional PoE switch). The base "
					"model is barcode scanning with ScaleSentry, ScanSentry and EAS options."
				),
				"sort_order": 2,
			},
			{
				"question": "Does it read GS1 Digital Link and Digimarc?",
				"answer": "Yes. Both are specified for the Magellan 9900i, along with QR, Data Matrix and stacked GS1 codes.",
				"sort_order": 3,
			},
			{
				"question": "What is the Top-Down Reader?",
				"answer": (
					"An optional tower (7\", 9\" or 12.4\") that adds a sixth scan view and about "
					"20% more volume. A Customer-Facing Reader can be combined for loyalty and coupons."
				),
				"sort_order": 4,
			},
			{
				"question": "Scanner only or with a scale?",
				"answer": "Scanner-only 9910/9911/9912 or scanner/scale 9921/9922, single- or dual-interval, plus adaptive scale partners.",
				"sort_order": 5,
			},
			{
				"question": "What interfaces does it support?",
				"answer": "OEM USB Plus Power, RS-232 (including single-cable scanner/scale) and Ethernet. Two powered USB-A ports are available.",
				"sort_order": 6,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page was published without an ERP Item. When the Item is created, link it "
					"on this Website Product under ERP Item Link. The URL stays /products/datalogic-magellan-9900i."
				),
				"sort_order": 7,
			},
			{
				"question": "What is the warranty?",
				"answer": "The official datasheet specifies a 1-year standard factory warranty. EASEOFCARE plans can extend coverage.",
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
