# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.DLG.5031 — Datalogic Gryphon I GD4690.

Reviewed against GD4690i.py and the official Gryphon 4600 Series page:
https://www.datalogic.com/eng/retail-manufacturing-transportation-logistics-healthcare-gs1-digital-link-other-applications/handheld-scanners/gryphon-4600-series-pd-1147.html

GD4690 is the corded High Performance model. Do not advertise wireless-only
family features (Li-Ion pack, SuperCap, inductive charging) as standard.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

import frappe

NAME = "RET.SYS.DLG.5031"
SLUG = "datalogic-gryphon-i-gd4690"
# Official product video embedded on the Datalogic Gryphon 4600 Series page.
VIDEO_URL = "https://youtu.be/aVovr29rStc"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-gryphon-4600-series-product.png": (
		"/upload/products/GeneralDutyHandheldScanners/Gryphon%204600%20series(2).png"
	),
	"datalogic-gryphon-4600-eco.jpg": "/upload/prod_line2/Gryphon4600/2.jpg",
	"datalogic-gryphon-4600-aimer.jpg": "/upload/prod_line2/Gryphon4600/3.jpg",
	"datalogic-gryphon-4600-retail-pos.jpg": "/upload/prod_line2/Gryphon4600/4.jpg",
	"datalogic-gryphon-4600-applications.jpg": "/upload/prod_line2/Gryphon4600/5.jpg",
	"datalogic-gryphon-4600-accessories.jpg": "/upload/prod_line2/Gryphon4600/6.jpg",
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


def fill_datalogic_gryphon_i_gd4690():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)

	eco = official_image("datalogic-gryphon-4600-eco.jpg")
	aimer = official_image("datalogic-gryphon-4600-aimer.jpg")
	retail = official_image("datalogic-gryphon-4600-retail-pos.jpg")
	applications = official_image("datalogic-gryphon-4600-applications.jpg")
	accessories = official_image("datalogic-gryphon-4600-accessories.jpg")
	family = official_image("datalogic-gryphon-4600-series-product.png")

	# Prefer the corded presentation packshot already on this SKU.
	hero = doc.hero_image or "/files/Gryphon4600_presentation.jpg"

	doc.display_name = "Datalogic Gryphon I GD4690 2D Barcode Scanner"
	doc.website_product_name = "Datalogic Gryphon I GD4690"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Barcode Scanners"
	doc.category_label = "CORDED 2D HANDHELD SCANNER"
	doc.tagline = (
		"Premium high-performance 2D handheld scanner with dual-sensor optics, "
		"AI-enhanced decoding and USB / RS-232 connectivity"
	)
	doc.short_description = (
		"The Datalogic Gryphon I GD4690 is the corded High Performance model in the "
		"Gryphon 4600 Series. It combines dual-sensor 1.5 MP + VGA imaging, a high-speed "
		"dual-core processor, AI-enhanced decoding, GS1 Digital Link support, Digimarc "
		"digital watermark reading and Datalogic Green Spot good-read feedback for fast, "
		"accurate scanning at retail POS and other professional applications."
	)
	doc.long_description = (
		"<p>The Gryphon I GD4690 is designed for demanding corded scanning where operators "
		"need fast first-pass reads across standard 1D and 2D barcodes, dense symbols, "
		"damaged or poorly printed labels, codes on curved or reflective surfaces and "
		"barcodes displayed on mobile devices.</p>"
		"<p>Its High Performance dual-sensor optical system combines a 1.5 megapixel "
		"1360 × 1120 imager with a VGA 640 × 600 sensor to deliver an extended depth of "
		"field from near to far. A bright green central-cross LED aimer supports precise "
		"targeting, while warm-white and Hyper Red dual-color illumination can adapt to "
		"different scanning conditions.</p>"
		"<p>The Gryphon 4600 platform is Datalogic’s first handheld scanner line designed "
		"around eco-design: up to 25% lower power consumption and over 70% recycled "
		"materials, with lighter packaging and product weight to reduce environmental "
		"impact. Combined with Green Spot good-read feedback, operators get fast, reliable "
		"scanning in quiet or noisy environments.</p>"
		"<p>The corded GD4690 supports USB Type-C, USB and RS-232 multi-interface connectivity, "
		"operates from 4.5 to 14 VDC, withstands repeated 1.8 m drops, is rated IP52 and carries "
		"a 5-year factory warranty for corded models. Li-Ion packs, SuperCapacitor power and "
		"inductive charging apply to wireless Gryphon 4600 models, not this corded scanner.</p>"
		"<p>Printechs supplies and supports Datalogic Gryphon barcode scanners in Saudi Arabia, "
		"including Riyadh, Jeddah and Dammam, with product selection, POS integration, "
		"interface configuration, mounting, rollout and after-sales support.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Gryphon I GD4690 high-performance 2D barcode scanner"
	doc.video_url = VIDEO_URL

	doc.hero_trust_chips = (
		"Dual-sensor 1.5 MP + VGA optics\n"
		"AI-enhanced 1D / 2D decoding\n"
		"USB Type-C / USB / RS-232\n"
		"5-year factory warranty"
	)
	doc.story_heading = "Premium corded scanning from near to far"
	doc.visual_story_heading = "Gryphon I GD4690 across professional applications"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "Gryphon I GD4690"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Premium corded 2D handheld scanner with High Performance dual-sensor optics, "
		"AI-enhanced decoding, GS1 Digital Link, Digimarc, Green Spot feedback and "
		"USB Type-C / USB / RS-232 multi-interface connectivity."
	)
	if not doc.card_image:
		doc.card_image = hero

	doc.final_cta_heading = "Specify Gryphon I GD4690 for your scanning workflow"
	doc.final_cta_description = (
		"Printechs can confirm the correct interface, cable, stand, POS integration and deployment "
		"for Datalogic Gryphon I GD4690 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Gryphon I GD4690 Barcode Scanner Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Gryphon I GD4690 premium corded 2D barcode scanner with dual-sensor optics, "
		"AI-enhanced decoding, GS1 Digital Link, USB Type-C, USB and RS-232. Available in Saudi Arabia from Printechs."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "speed",
				"title": "Faster first-pass decoding",
				"description": (
					"Dual-core processing, AI-driven algorithms and advanced neural decoding improve reads of damaged, "
					"poorly printed, distorted, shiny, reflective and curved barcode labels."
				),
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Near-to-far High Performance optics",
				"description": (
					"Dual 1.5 MP + VGA sensors provide a wide depth of field for dense codes nearby and larger codes at distance."
				),
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Modern barcode standards",
				"description": (
					"Reads 1D, 2D, stacked, GS1 Digital Link, Digimarc digital watermarks and OCR, including codes on mobile screens."
				),
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Flexible corded connectivity",
				"description": "USB Type-C, USB and RS-232 multi-interface support for POS and professional systems.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Retail POS",
				"image": retail,
				"image_alt": "Datalogic Gryphon I GD4690 scanner at retail point of sale",
				"caption": "Premium 1D/2D scanning for attended checkout and customer service counters.",
				"sort_order": 1,
			},
			{
				"label": "Green Spot targeting",
				"image": aimer,
				"image_alt": "Datalogic Gryphon I GD4690 green central-cross LED aimer",
				"caption": "Bright green crosshair aimer and on-code Green Spot good-read feedback.",
				"sort_order": 2,
			},
			{
				"label": "Healthcare & industry",
				"image": applications,
				"image_alt": "Datalogic Gryphon I GD4690 across healthcare, manufacturing and logistics",
				"caption": "One scanner family for pharmacy, light manufacturing and commercial services.",
				"sort_order": 3,
			},
			{
				"label": "Eco-designed platform",
				"image": eco,
				"image_alt": "Datalogic Gryphon 4600 eco-designed handheld scanner",
				"caption": "Up to 25% lower power use and over 70% recycled materials on the Gryphon 4600 platform.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "scan",
				"title": "1D + 2D + GS1",
				"description": "Omnidirectional reading including GS1 Digital Link, Digimarc and OCR",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Dual sensor",
				"description": "1.5 MP 1360 × 1120 + VGA 640 × 600 High Performance optics",
				"sort_order": 2,
			},
			{
				"icon": "speed",
				"title": "70 IPS",
				"description": "Motion tolerance for moving barcode reading",
				"sort_order": 3,
			},
			{
				"icon": "shield",
				"title": "1.8 m drops",
				"description": "IP52 sealing · 2,000 tumbles · 10 million trigger hits",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "Multi-interface",
				"description": "USB Type-C · USB · RS-232",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "5-year warranty",
				"description": "Factory warranty for corded Gryphon 4600 models",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Scanner & imaging",
			[
				("Model", "Gryphon I GD4690 — High Performance corded model"),
				("Scanner type", "Premium corded omnidirectional 1D/2D area imager"),
				("Processor", "High-speed dual-core processor with AI-enhanced decoding"),
				("Optical system", "High Performance dual-sensor optics"),
				("Primary imager", "1.5 megapixel — 1360 × 1120 pixels"),
				("Secondary imager", "VGA — 640 × 600 pixels"),
				("Aimer", "Highly visible green central-cross LED"),
				("Illumination", "Dual-color Warm White and Hyper Red LED"),
				("Image capture", "BMP, JPEG, TIFF; greyscale 256, 16, 2"),
				("Motion tolerance", "70 IPS"),
				("Minimum print contrast", "15%"),
				("Pitch / roll / skew", "Pitch ±65° · Roll 360° · Skew ±65°"),
			],
		),
		(
			"Decoding",
			[
				("1D / linear codes", "Auto-discriminates all standard 1D codes including GS1 DataBar"),
				("2D codes", "Aztec, China Han Xin, Data Matrix, MaxiCode, Micro QR, QR, DotCode, GS1 Digital Link"),
				("Stacked codes", "EAN/JAN Composites, GS1 DataBar Composites, MacroPDF, MicroPDF417, PDF417"),
				("Stacked UPC composites", "UPC A/E Composites"),
				("Digital watermarking", "Digimarc Barcodes"),
				("OCR", "OCR-A, OCR-B, MICR"),
				("Postal codes", "Australian Post, British Post, China Post, IMB, Japanese Post, KIX, Planet, Postnet, Royal Mail"),
				("Maximum 1D resolution", "0.077 mm / 3 mil"),
				("Maximum PDF417 resolution", "0.077 mm / 3 mil"),
				("Maximum Data Matrix resolution", "0.102 mm / 4 mil"),
				("Good-read feedback", "Beeper, Datalogic Green Spot on code and Good Read LED"),
			],
		),
		(
			"Typical reading ranges — High Performance",
			[
				("Code 39 — 3 mil", "2.5 to 20.0 cm"),
				("Code 39 — 5 mil", "0.5 to 35.0 cm"),
				("Code 39 — 10 mil", "0 to 60.0 cm*"),
				("Code 39 — 20 mil", "0 to 125.0 cm*"),
				("Code 128 — 3 mil", "3.5 to 14.5 cm"),
				("Code 128 — 5 mil", "1.5 to 30.0 cm"),
				("EAN / UPC — 13 mil", "0 to 100.0 cm*"),
				("PDF417 — 5 mil", "2.5 to 17.0 cm"),
				("PDF417 — 10 mil", "0.5 to 38.5 cm*"),
				("Data Matrix — 5 mil", "3.5 to 10.0 cm"),
				("Data Matrix — 10 mil", "0.5 to 29.5 cm*"),
				("QR Code — 10 mil", "0.5 to 25.0 cm*"),
				(
					"Note",
					"Depth of field depends on label size, print resolution, contrast, ambient light and scan angle.",
				),
			],
		),
		(
			"Interfaces & electrical",
			[
				("Interfaces", "USB Type-C / USB / RS-232 multi-interface"),
				("Input voltage", "4.5–14.0 VDC ±5%"),
				("Operating current", "<300 mA @ 5 V; <150 mA @ 12 V"),
				("Standby / idle current", "<70 mA @ 5 V; <40 mA @ 12 V"),
				("Configuration utility", "Datalogic Aladdin"),
				("Device management", "Datalogic Connect IoT cloud platform"),
				("Software support", "JavaPOS, OPOS and SDK for Android utilities"),
				("Remote host download", "Supported to lower service costs and simplify operations"),
			],
		),
		(
			"Environment & durability",
			[
				("Ambient light", "0–110,000 lux"),
				("Drop resistance", "Repeated drops from 1.8 m / 6 ft onto concrete"),
				("Tumble specification", "2,000 tumbles from 0.5 m / 1.5 ft"),
				("Trigger resistance", "10 million hits"),
				("ESD protection", "16 kV air discharge"),
				("Humidity", "0–95%, non-condensing"),
				("IP rating", "IP52"),
				("Operating temperature", "0 to 50 °C"),
				("Storage / transport", "−40 to 70 °C"),
			],
		),
		(
			"Physical, eco-design & warranty",
			[
				("Colors available", "Black, White"),
				("Dimensions — scanner", "18 × 6.5 × 7.9 cm"),
				("Weight — corded scanner", "144 g"),
				("Dimensions with presentation base", "21 × 7.5 × 10.9 cm"),
				("Weight with presentation base", "426 g"),
				("Eco-design", "Up to 25% lower power; over 70% recycled materials"),
				("Environmental compliance", "China RoHS, EU RoHS"),
				("Warranty", "5-year factory warranty — corded models"),
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
				"description": "Fast handheld 1D/2D scanning for checkout, customer service and mobile-code workflows.",
				"image": retail,
				"image_alt": "Datalogic Gryphon I GD4690 at retail POS",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Light manufacturing",
				"description": "Work-in-progress, order processing and barcode identification in light industrial environments.",
				"image": applications,
				"image_alt": "Datalogic Gryphon I GD4690 in manufacturing",
				"industry_link": "manufacturing",
				"sort_order": 2,
			},
			{
				"title": "Healthcare, laboratory & pharmacy",
				"description": "Reliable barcode capture for laboratory, pharmacy and patient-related identification workflows.",
				"image": applications,
				"image_alt": "Datalogic Gryphon I GD4690 for healthcare and pharmacy scanning",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Commercial services & access control",
				"description": "Suitable for post offices, banking, public administration, utilities, access control, transport and entertainment.",
				"image": aimer,
				"image_alt": "Datalogic Gryphon I GD4690 for commercial services",
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
				"heading": "See the Gryphon 4600 in action",
				"body": (
					"Watch Datalogic’s official Gryphon 4600 overview: eco-design, dual-sensor imaging, "
					"AI-enhanced decoding and Green Spot feedback. The GD4690 is the corded High Performance "
					"model from this series — USB Type-C / USB / RS-232, without wireless battery options."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic Gryphon I GD4690 barcode scanner",
				"link_label": "Talk to Our Retail Team",
				"link_href": "/contact",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "AI-enhanced decoding for difficult barcodes",
				"body": (
					"The Gryphon 4600 platform combines a high-speed dual-core processor with AI-driven algorithms "
					"and neural network-based decoding. This improves first-pass reading of damaged, poorly printed "
					"or distorted symbols and helps on shiny, reflective and curved surfaces.\n\n"
					"For operators, the result is less repeated scanning and more consistent capture during normal workflows."
				),
				"image": aimer,
				"image_alt": "Datalogic Gryphon I GD4690 AI-enhanced barcode decoding",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Dual-sensor optics from near to far",
				"body": (
					"The GD4690 High Performance model uses dual optics: a 1.5 MP 1360 × 1120 sensor plus a VGA "
					"640 × 600 sensor. This gives the scanner strong depth-of-field performance for small high-density "
					"codes at close range as well as larger symbols at longer distances.\n\n"
					"The official High Performance reading table reaches up to 100 cm for 13 mil EAN/UPC and up to "
					"125 cm for 20 mil Code 39 under suitable conditions."
				),
				"image": retail,
				"image_alt": "Datalogic Gryphon I GD4690 dual-sensor High Performance optics",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Green Spot, central-cross aimer and adaptive illumination",
				"body": (
					"A bright green central-cross LED aimer helps operators target the intended barcode quickly. "
					"Datalogic Green Spot projects good-read feedback directly on the code, while the adjustable beeper "
					"and Good Read LED provide additional confirmation.\n\n"
					"Dual-color illumination uses Warm White and Hyper Red LEDs so the scanner can adapt to different "
					"barcode materials and application conditions."
				),
				"image": aimer,
				"image_alt": "Datalogic Gryphon Green Spot and LED aimer",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Designed for sustainability",
				"body": (
					"The official Gryphon 4600 Series page describes this as Datalogic’s first handheld scanner line "
					"built with eco-design: up to 25% lower power consumption, over 70% recycled materials, and "
					"lighter product and packaging weight to reduce environmental impact.\n\n"
					"Those platform values apply to the corded GD4690. Wireless Li-Ion, SuperCapacitor and inductive "
					"charging options belong to GBT4600 / GM4600 models, not this corded scanner."
				),
				"image": eco,
				"image_alt": "Datalogic Gryphon 4600 eco-designed handheld scanner",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "USB Type-C, USB and RS-232 for professional integration",
				"body": (
					"The corded Gryphon I GD4690 is the multi-interface High Performance model with USB Type-C, USB "
					"and RS-232 connectivity and a 4.5–14 VDC input range.\n\n"
					"Datalogic Aladdin is available for configuration, while JavaPOS, OPOS and Android SDK utilities "
					"support software integration. Datalogic Connect can be used for remote device management."
				),
				"image": family,
				"image_alt": "Datalogic Gryphon I GD4690 USB and RS-232 integration",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Stands and presentation accessories",
				"body": (
					"Corded GD4690 kits can include the PM-BASE-GD46-BK presentation mode base, STD-G041 stand or "
					"HLD-G041 holder, plus USB cable 90A052258 (black) or 90A052278 (white HC).\n\n"
					"Wireless charging bases (WLC4690) are for cordless Gryphon 4600 models. Printechs can confirm "
					"the correct cable, stand and POS interface for your checkout or counter."
				),
				"image": accessories,
				"image_alt": "Datalogic Gryphon 4600 presentation base and stand options",
				"sort_order": 7,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "store",
				"title": "Model & interface selection",
				"description": "Confirm GD4690 High Performance versus GD4620 High Density and select USB or RS-232 connectivity.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Scanner configuration",
				"description": "Barcode symbology, interface and operating settings using Datalogic Aladdin.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "POS & software integration",
				"description": "Support for USB, RS-232, OPOS, JavaPOS and Android SDK based deployments.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Deployment, stands, cables, rollout and after-sales support in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])

	doc.set(
		"package_contents",
		[
			{"item_description": "Gryphon I GD4690 High Performance corded scanner", "sort_order": 1},
			{"item_description": "USB / RS-232 cable according to selected kit or installation (optional / kit dependent)", "sort_order": 2},
			{"item_description": "PM-BASE-GD46-BK presentation mode base (optional / kit dependent)", "sort_order": 3},
			{"item_description": "STD-G041 stand or HLD-G041 holder (optional)", "sort_order": 4},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4981", 1),
			related_product_row("RET.SYS.DLG.4708", 2),
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
				"question": "What is the Datalogic Gryphon I GD4690?",
				"answer": (
					"The Gryphon I GD4690 is the corded High Performance model in Datalogic's Gryphon 4600 Series, "
					"using dual-sensor optics and multi-interface USB / RS-232 connectivity."
				),
				"sort_order": 1,
			},
			{
				"question": "Does the GD4690 read QR codes and GS1 Digital Link?",
				"answer": "Yes. It reads QR Code, Data Matrix, Aztec, GS1 Digital Link and other standard 1D/2D and stacked symbologies.",
				"sort_order": 2,
			},
			{
				"question": "Can the GD4690 read damaged or difficult barcodes?",
				"answer": (
					"Yes. The Gryphon 4600 platform uses AI-enhanced and neural network-based decoding to improve "
					"reading of damaged, poorly printed, distorted, shiny, reflective and curved codes."
				),
				"sort_order": 3,
			},
			{
				"question": "Can the GD4690 scan barcodes from mobile phones?",
				"answer": "Yes. The Gryphon 4600 Series is designed to read common barcodes displayed on mobile devices.",
				"sort_order": 4,
			},
			{
				"question": "What interfaces does the Gryphon I GD4690 support?",
				"answer": "The GD4690 supports USB Type-C, USB and RS-232 multi-interface connectivity.",
				"sort_order": 5,
			},
			{
				"question": "What is the scanning range of the GD4690?",
				"answer": (
					"It varies by barcode type and size. For the High Performance model, the datasheet lists up to "
					"100 cm for 13 mil EAN/UPC and up to 125 cm for 20 mil Code 39 under suitable conditions."
				),
				"sort_order": 6,
			},
			{
				"question": "How durable is the GD4690?",
				"answer": (
					"It is rated IP52, withstands repeated 1.8 m drops onto concrete, is designed for 2,000 tumbles "
					"from 0.5 m and has a trigger rated for 10 million hits."
				),
				"sort_order": 7,
			},
			{
				"question": "Is the GD4690 wireless or battery powered?",
				"answer": (
					"No. The GD4690 is the corded High Performance model. Li-Ion battery packs, SuperCapacitor power "
					"and inductive charging are specified for wireless GBT4600 and GM4600 models."
				),
				"sort_order": 8,
			},
			{
				"question": "What is the warranty for the GD4690?",
				"answer": "The official Gryphon 4600 Series datasheet specifies a 5-year factory warranty for corded models.",
				"sort_order": 9,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
