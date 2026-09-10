# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.DLG.4885 — Datalogic QuickScan QW2520.

Source: official QuickScan 2500 Series page and datasheet DS-QUICKSCAN-2500-SERIES-EN Rev B.
https://www.datalogic.com/eng/retail-manufacturing-healthcare-gs1-digital-link/handheld-scanners/quickscan-2500-series-pd-898.html

QW2520 is the corded VGA / USB-only model. Do not advertise 1 MP optics,
Digimarc, two-triangle aimer, RS-232, STAR/Bluetooth or wireless charging.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

NAME = "RET.SYS.DLG.4885"
SLUG = "datalogic-quickscan-qw2520"
# Official QW2500 video from the Datalogic QuickScan 2500 Series media gallery.
VIDEO_URL = "https://youtu.be/52IjcvkoxcY"
SERIES_INTRO_VIDEO = "https://youtu.be/bdmsgZrx-s0"
GREEN_SPOT_VIDEO = "https://youtu.be/8G7pIjNbZhM"
ALADDIN_VIDEO = "https://youtu.be/yURudelqU54"
TRIGGER_VIDEO = "https://youtu.be/Uf20I88GBAQ"

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-quickscan-2500-series.png": "/upload/products/generaldutyhandheldscanners/QS2500Series.png",
	"datalogic-quickscan-2500-improve.jpg": "/upload/prod_line/qs2500%20series/IMPROVE.jpg",
	"datalogic-quickscan-2500-connect.jpg": "/upload/prod_line/qs2500%20series/CONNECT.jpg",
	"datalogic-quickscan-2500-perform.jpg": "/upload/prod_line/qs2500%20series/PERFORM.jpg",
	"datalogic-quickscan-2500-versatility.jpg": "/upload/prod_line/qs2500%20series/VERSATILITY.jpg",
	"datalogic-quickscan-qw2500-overview.jpg": (
		"/upload/prod_line/General%20Duty%20Handheld%20Scanners/QuickScan/QW2500_overview.jpg"
	),
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


def fill_datalogic_quickscan_qw2520():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)

	series = official_image("datalogic-quickscan-2500-series.png")
	improve = official_image("datalogic-quickscan-2500-improve.jpg")
	connect = official_image("datalogic-quickscan-2500-connect.jpg")
	perform = official_image("datalogic-quickscan-2500-perform.jpg")
	versatility = official_image("datalogic-quickscan-2500-versatility.jpg")
	overview = official_image("datalogic-quickscan-qw2500-overview.jpg")

	hero = doc.hero_image or "/files/PLP-QUICKSCAN-QW2500-RIGHT-FACING-2-HR.jpg"

	doc.display_name = "Datalogic QuickScan QW2520 Barcode Scanner"
	doc.website_product_name = "Datalogic QuickScan QW2520"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Barcode Scanners"
	doc.category_label = "CORDED VGA 2D HANDHELD"
	doc.tagline = (
		"Affordable corded 2D handheld scanner with VGA imaging, Green Spot feedback "
		"and USB Type-C / USB connectivity"
	)
	doc.short_description = (
		"The Datalogic QuickScan QW2520 is the simplest corded model in the QuickScan "
		"2500 Series. It uses a VGA 640 × 480 imager, USB Type-C / USB connectivity and "
		"the same IP52 housing as the rest of the series — with a trigger rated for 10 "
		"million hits — to deliver reliable 1D and 2D reading at retail POS and other "
		"everyday professional applications."
	)
	doc.long_description = (
		"<p>The QuickScan QW2520 is Datalogic’s extra-affordable entry-level 2D handheld "
		"for checkout and general-purpose scanning. Official model listings describe it as "
		"a 2D VGA imager with USB interface. It reads standard 1D and 2D barcodes, including "
		"codes that are damaged, poorly printed or shown on a smartphone, and the series is "
		"specified to read through plexiglass barriers at POS.</p>"
		"<p>Aiming on the QW model uses an intuitive blue LED / blue-dot aimer. Datalogic "
		"Green Spot confirms a good read on the code, with an adjustable beeper and Good Read "
		"LED. Soft red illumination and Motionix motion-sensing help operators pick up the "
		"scanner and start reading without extra setup.</p>"
		"<p>Do not confuse the QW2520 with higher QuickScan 2500 models. 1 megapixel optics, "
		"the two-triangle aimer, Digimarc digital watermarks, RS-232 / keyboard-wedge "
		"multi-interface, STAR radio and Bluetooth wireless charging bases belong to QD, QM "
		"or QBT models — not this VGA USB scanner.</p>"
		"<p>Printechs supplies and supports Datalogic QuickScan scanners in Saudi Arabia, "
		"including Riyadh, Jeddah and Dammam — product selection, USB setup, stands, POS "
		"integration, rollout and after-sales service.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic QuickScan QW2520 corded 2D barcode scanner"
	doc.video_url = VIDEO_URL

	doc.hero_trust_chips = (
		"VGA 640 × 480 2D imager\n"
		"USB Type-C / USB\n"
		"IP52 · 1.5 m drops\n"
		"5-year factory warranty"
	)
	doc.story_heading = "Entry-level 2D scanning with reliable everyday performance"
	doc.visual_story_heading = "QuickScan QW2520 in retail and professional use"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "QuickScan QW2520"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Affordable corded 2D VGA handheld scanner with USB Type-C / USB, Green Spot "
		"feedback, IP52 housing and a 10-million-hit trigger. Ideal for retail POS, "
		"hospitality, healthcare counters and light commercial scanning."
	)
	if not doc.card_image:
		doc.card_image = hero

	doc.final_cta_heading = "Specify QuickScan QW2520 for your checkout"
	doc.final_cta_description = (
		"Printechs can confirm cable, stand, USB setup and POS integration for "
		"Datalogic QuickScan QW2520 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic QuickScan QW2520 Barcode Scanner Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic QuickScan QW2520 affordable corded 2D VGA barcode scanner with USB "
		"Type-C, Green Spot and IP52 housing. Available in Saudi Arabia from Printechs."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "Reliable everyday 1D / 2D reading",
				"description": (
					"VGA imaging reads standard barcodes, damaged or poorly printed labels, "
					"and codes on smartphone screens at an affordable price."
				),
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Easy to aim, easy to confirm",
				"description": (
					"Blue-dot LED aiming plus Green Spot on-code feedback, adjustable beeper "
					"and Good Read LED for a clear result on every scan."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Simple USB Type-C / USB setup",
				"description": (
					"QW2520 and QD2520 are USB Type-C / USB only. Configure with Datalogic "
					"Aladdin; OPOS and JavaPOS utilities are available."
				),
				"sort_order": 3,
			},
			{
				"icon": "shield",
				"title": "Built for long retail shifts",
				"description": (
					"IP52 housing, 1.5 m / 5 ft drops to concrete, 10 million trigger hits "
					"and a 5-year factory warranty on corded models."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Retail POS",
				"image": improve,
				"image_alt": "Datalogic QuickScan QW2520 reading a barcode from a smartphone at POS",
				"caption": "Scan printed labels and mobile coupons, including through plexiglass at checkout.",
				"sort_order": 1,
			},
			{
				"label": "Blue-dot aiming",
				"image": overview,
				"image_alt": "Datalogic QuickScan QW2520 blue-dot LED aimer",
				"caption": "The QW model uses an intuitive blue-dot aimer — not the two-triangle aimer on QD/QM/QBT.",
				"sort_order": 2,
			},
			{
				"label": "USB hosts & stands",
				"image": connect,
				"image_alt": "Datalogic QuickScan QW2520 USB connection to POS, laptop and tablet",
				"caption": "USB Type-C / USB to POS terminals, PCs and tablets, with optional STD-QW25 stand.",
				"sort_order": 3,
			},
			{
				"label": "Healthcare & retail",
				"image": versatility,
				"image_alt": "Datalogic QuickScan 2500 in healthcare, fashion and counter applications",
				"caption": "Retail, hospitality, government, pharmacy and light commercial counters.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "scan",
				"title": "1D + 2D VGA",
				"description": "640 × 480 imager for extra-affordable 2D reading",
				"sort_order": 1,
			},
			{
				"icon": "connectivity",
				"title": "USB-C / USB",
				"description": "Corded USB Type-C and USB only — no RS-232 on QW2520",
				"sort_order": 2,
			},
			{
				"icon": "speed",
				"title": "30 IPS",
				"description": "Motion tolerance for handheld checkout scanning",
				"sort_order": 3,
			},
			{
				"icon": "durability",
				"title": "IP52",
				"description": "1.5 m drops · 10 million trigger hits",
				"sort_order": 4,
			},
			{
				"icon": "device",
				"title": "Green Spot",
				"description": "On-code good-read plus blue-dot LED aimer",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "5-year warranty",
				"description": "Factory warranty from the official datasheet",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Scanner & imaging",
			[
				("Model", "QuickScan QW2520 — corded VGA model in the 2500 Series"),
				("Scanner type", "Entry-level corded omnidirectional 1D/2D area imager"),
				("Image sensor", "VGA — 640 × 480 pixels"),
				("Aimer", "Blue LED, 468 nm — intuitive blue-dot aiming (QW)"),
				("Illumination", "Red LED, 624 nm"),
				("Image capture", "BMP, JPEG, TIFF; greyscale 256, 16, 2"),
				("Motion tolerance", "30 IPS"),
				("Minimum print contrast", "15% with specific configuration"),
				("Pitch / roll / skew", "Pitch ±65° · Roll 360° · Skew ±65°"),
				("Reading indicators", "Beeper, Green Spot on code, Good Read LED"),
			],
		),
		(
			"Decoding",
			[
				("1D / linear codes", "All standard 1D codes including GS1 DataBar"),
				("2D codes", "Aztec, China Han Xin, Data Matrix, MaxiCode, Micro QR, QR, DotCode"),
				("Stacked codes", "EAN/JAN Composites, GS1 DataBar composites, MacroPDF, MicroPDF417, PDF417"),
				("Stacked UPC composites", "UPC A/E Composites"),
				("Postal codes", "Australian, British, China, IMB, Japanese, KIX, Planet, Postnet, RM4SCC"),
				("Digital watermarks", "Not specified for QW2500 — Digimarc is QD/QM/QBT only"),
				("Maximum 1D resolution", "0.077 mm / 3 mil"),
				("Maximum PDF417 resolution", "0.127 mm / 5 mil"),
				("Maximum Data Matrix resolution", "0.152 mm / 6 mil"),
				("Maximum QR resolution", "0.17 mm / 6.7 mil"),
			],
		),
		(
			"Typical reading ranges — QW2500",
			[
				("Code 39 — 5 mil", "0.5 to 23.0 cm"),
				("Code 39 — 10 mil", "0.5 to 37.0 cm"),
				("Data Matrix — 10 mil", "1.0 to 15.5 cm"),
				("EAN / UPCA — 13 mil", "1.0 to 40.0 cm"),
				("PDF417 — 6.7 mil", "0.5 to 13.5 cm"),
				("QR Code — 20 mil", "1.0 to 33.0 cm"),
				(
					"Note",
					"Distance depends on symbol length, scan angle, print resolution, contrast and light.",
				),
			],
		),
		(
			"Interfaces & electrical",
			[
				("Interfaces", "USB Type-C / USB only"),
				("Input voltage", "5 VDC"),
				("Operating current", "< 400 mA @ 5 V"),
				("Standby / idle current", "< 90 mA @ 5 V"),
				("Configuration", "Datalogic Aladdin"),
				("Software support", "JavaPOS and OPOS utilities"),
				("Remote host download", "Supported to lower service costs"),
			],
		),
		(
			"Environment, physical & warranty",
			[
				("Ambient light", "0–110,000 lux"),
				("Drop resistance", "Repeated drops from 1.5 m / 5 ft onto concrete"),
				("Trigger resistance", "10 million hits"),
				("ESD protection", "16 kV air discharge"),
				("Humidity", "0–95%, non-condensing"),
				("IP rating", "IP52"),
				("Operating temperature", "0 to 50 °C"),
				("Storage / transport", "−40 to 70 °C"),
				("Color", "Black (QW2500)"),
				("Dimensions", "14.8 × 6.8 × 12.6 cm"),
				("Weight", "145 g"),
				("LED classification", "Illuminator Exempt; aiming Risk Group 1, IEC 62471"),
				("Environmental compliance", "China RoHS, EU RoHS"),
				("Warranty", "5-year factory warranty"),
				("Item code", NAME),
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
				"title": "Retail point of sale",
				"description": "Checkout, loyalty cards and electronic coupons from phones, including through plexiglass.",
				"image": improve,
				"image_alt": "Datalogic QuickScan QW2520 at retail POS",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Fashion & specialty retail",
				"description": "Handheld 1D/2D reading of hang tags and packed goods at attended counters.",
				"image": perform,
				"image_alt": "Datalogic QuickScan QW2520 scanning a fashion hang tag",
				"industry_link": "fashion",
				"sort_order": 2,
			},
			{
				"title": "Healthcare, pharmacy & lab",
				"description": "Everyday barcode capture for pharmacies, laboratories and in-room identification.",
				"image": versatility,
				"image_alt": "Datalogic QuickScan 2500 in healthcare and pharmacy",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Hospitality, government & light manufacturing",
				"description": "Ticketing, lottery, postal/banking counters and work-in-progress identification.",
				"image": connect,
				"image_alt": "Datalogic QuickScan QW2520 for commercial services",
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
				"heading": "Watch the official QuickScan QW2500 video",
				"body": (
					"Datalogic’s official QW2500 film — “The 2500 series is now Ultra-Affordable” — "
					"shows the corded VGA model this page covers. The series introduction video is "
					"also on the official product page."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic QuickScan QW2520 barcode scanner",
				"link_label": "Series introduction on YouTube",
				"link_href": SERIES_INTRO_VIDEO,
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Green Spot good-read feedback",
				"body": (
					"Green Spot projects confirmation onto the barcode after a successful read. "
					"On the QW2520 this sits with the blue-dot LED aimer, adjustable beeper and "
					"Good Read LED — not the two sharply defined blue triangles used on QD/QM/QBT."
				),
				"video_url": GREEN_SPOT_VIDEO,
				"image": perform,
				"image_alt": "Datalogic Green Spot good-read on a QuickScan 2500",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "VGA optics built for affordable 2D checkout",
				"body": (
					"The official datasheet gives the QW2500 a VGA 640 × 480 sensor for extra "
					"affordability. 1 MP (1280 × 800) optics are specified for QD, QM and QBT only.\n\n"
					"Typical QW reading ranges include 0.5–23 cm for 5 mil Code 39 and 1.0–40 cm "
					"for 13 mil EAN/UPCA, depending on print quality and angle."
				),
				"image": overview,
				"image_alt": "Datalogic QuickScan QW2520 VGA imager and blue-dot aimer",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Motionix, mobile codes and plexiglass POS",
				"body": (
					"Motionix motion-sensing switches the imager ready as soon as it is picked up. "
					"The series is specified to read damaged or poorly printed labels, codes on "
					"smartphone screens, and barcodes through plexiglass checkout barriers."
				),
				"image": improve,
				"image_alt": "Datalogic QuickScan QW2520 scanning a mobile barcode through plexiglass",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Configure with Aladdin 3.0",
				"body": (
					"Datalogic Aladdin is the free configurator for QuickScan 2500. Aladdin 3.0 "
					"adds a modern GUI, search and an online option that can generate programming "
					"barcodes to scan from a smartphone. OPOS and JavaPOS utilities are also listed."
				),
				"video_url": ALADDIN_VIDEO,
				"image": connect,
				"image_alt": "Datalogic QuickScan QW2520 USB host connectivity",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Trigger life and everyday durability",
				"body": (
					"The only moving part on the QW2520 is the trigger, specified for 10 million "
					"hits. The housing is IP52 and withstands repeated 1.5 m / 5 ft drops onto "
					"concrete. Official trigger-testing footage is on the QuickScan 2500 media gallery."
				),
				"video_url": TRIGGER_VIDEO,
				"image": series,
				"image_alt": "Datalogic QuickScan 2500 series handheld scanners and stands",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Kits, cables and the STD-QW25 stand",
				"body": (
					"Official QW2520 kits include QW2520-BK (scanner only), QW2520-BKK1 (USB cable "
					"90A052258), QW2520-BKK1S (cable plus STD-QW25-BK stand), plus coiled-cable "
					"kits with 90A052285.\n\n"
					"BC2090 bases and wireless charging belong to QM/QBT cordless models. "
					"The QW2520 is corded USB only."
				),
				"image": connect,
				"image_alt": "Datalogic QuickScan QW2520 with stand and USB host options",
				"sort_order": 7,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "store",
				"title": "Model selection",
				"description": "Confirm QW2520 VGA/USB versus QD2590 1 MP multi-interface or cordless QM/QBT.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "USB setup & Aladdin",
				"description": "Interface, symbology and tone settings with Datalogic Aladdin 3.0.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "POS integration",
				"description": "USB Type-C / USB to retail POS, with OPOS and JavaPOS utilities when required.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Cables, STD-QW25 stands, rollout and after-sales support in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "QuickScan QW2520 VGA corded scanner (black)", "sort_order": 1},
			{"item_description": "USB cable 90A052258 or coiled 90A052285 (kit dependent)", "sort_order": 2},
			{"item_description": "STD-QW25-BK collapsible stand (kit dependent)", "sort_order": 3},
			{"item_description": "HLD-Q040-BK holder (optional)", "sort_order": 4},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.5031", 1),
			related_product_row("RET.SYS.DLG.4981", 2),
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
				"question": "What is the Datalogic QuickScan QW2520?",
				"answer": (
					"It is the simplest corded model in the QuickScan 2500 Series: a VGA 2D imager "
					"with USB Type-C / USB, IP52 housing and a 10-million-hit trigger."
				),
				"sort_order": 1,
			},
			{
				"question": "Does the QW2520 read QR codes and phone screens?",
				"answer": (
					"Yes. It reads QR, Data Matrix, Aztec and other listed 2D codes, including "
					"barcodes displayed on smartphones for promotions and coupons."
				),
				"sort_order": 2,
			},
			{
				"question": "Does the QW2520 have a 1 MP sensor or Digimarc?",
				"answer": (
					"No. The datasheet specifies VGA 640 × 480 for QW2500. 1 MP optics and Digimarc "
					"digital watermarks are listed for QD, QM and QBT models only."
				),
				"sort_order": 3,
			},
			{
				"question": "What interface does the QW2520 use?",
				"answer": "USB Type-C / USB only. RS-232 and keyboard wedge are specified for QD2590 and cordless bases.",
				"sort_order": 4,
			},
			{
				"question": "Is the QW2520 wireless?",
				"answer": (
					"No. It is a corded scanner. STAR radio (QM2500) and Bluetooth (QBT2500) are "
					"separate cordless models with BC2090 bases."
				),
				"sort_order": 5,
			},
			{
				"question": "What is the reading range?",
				"answer": (
					"For the QW2500 table: about 0.5–23 cm for 5 mil Code 39 and 1.0–40 cm for "
					"13 mil EAN/UPCA, depending on print quality, angle and light."
				),
				"sort_order": 6,
			},
			{
				"question": "How durable is the QW2520?",
				"answer": (
					"IP52 sealing, repeated 1.5 m / 5 ft drops to concrete, and a trigger specified "
					"for 10 million hits."
				),
				"sort_order": 7,
			},
			{
				"question": "What is the warranty?",
				"answer": "The official QuickScan 2500 Series datasheet specifies a 5-year factory warranty.",
				"sort_order": 8,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
