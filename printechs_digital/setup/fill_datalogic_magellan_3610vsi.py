# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product RET.SYS.DLG.4981 — Datalogic Magellan 3610VSi."""

from pathlib import Path
from shutil import copy2

import frappe

NAME = "RET.SYS.DLG.4981"
SLUG = "datalogic-magellan-3610vsi"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


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


def fill_datalogic_magellan_3610vsi():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero = doc.hero_image or "/files/Magellan3600-right-lights.jpg"

	doc.display_name = "Datalogic Magellan 3610VSi Barcode Scanner"
	doc.website_product_name = "Datalogic Magellan 3610VSi"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Barcode Scanners"
	doc.category_label = "VERTICAL 1D/2D POS SCANNER"
	doc.tagline = (
		"High-performance vertical single-plane scanner for fast-moving retail checkout"
	)
	doc.short_description = (
		"The Datalogic Magellan 3610VSi is a high-performance vertical single-plane barcode "
		"scanner designed for fast-moving retail checkout environments. Its advanced digital "
		"imaging technology delivers reliable reading of 1D, 2D, stacked, GS1 Digital Link and "
		"Digimarc digital watermark codes, including barcodes printed on products or displayed "
		"on mobile phones."
	)
	doc.long_description = (
		"<p>With a compact design, global-shutter imaging, low power consumption, multiple POS "
		"interfaces and support for modern retail software platforms, the Magellan 3610VSi is "
		"ideal for supermarkets, fashion stores, pharmacies, convenience stores, specialty retail, "
		"kiosks and self-checkout applications. It scans printed, mobile, damaged and hard-to-read "
		"barcodes with enhanced throughput and motion tolerance.</p>"
		"<p>The Magellan 3610VSi continues Datalogic’s Magellan retail scanning platform with a "
		"focus on speed, accuracy and reliability. Its advanced digital imaging system supports "
		"standard retail barcode formats as well as GS1 Digital Link, composite barcodes, OCR and "
		"Digimarc digital watermarks. Codes can be read on printed packaging or from customer "
		"mobile phones, so loyalty cards, coupons, tickets and QR-based applications stay in the "
		"same checkout motion.</p>"
		"<p>The scanner uses a 1360 × 1120 pixel global-shutter image sensor and multiple diffused "
		"LEDs optimized for user comfort. It is a solid-state imaging platform — quiet, with no "
		"moving scan engine — and is not specified with UHF RFID, colour image capture, a colour "
		"video camera, USB-C Power Delivery or a powered auxiliary USB port. Those capabilities "
		"belong to higher Magellan 3600VSi models (3650/3670).</p>"
		"<p>Printechs supplies and supports Datalogic retail barcode scanning in Saudi Arabia, "
		"including Riyadh, Jeddah and Dammam — product selection, POS configuration, USB and "
		"RS-232 setup, checkout deployment, multi-store rollout, mounting and after-sales service.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "Datalogic Magellan 3610VSi barcode scanner"
	doc.hero_trust_chips = (
		"1D + 2D advanced reading\n"
		"1360 × 1120 global shutter\n"
		"1.2 W nominal power\n"
		"3-year factory warranty"
	)
	doc.story_heading = "Retail scanning built for speed, accuracy and modern codes"
	doc.visual_story_heading = "Magellan 3610VSi in retail operations"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.card_title = "Magellan 3610VSi"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"High-performance vertical 1D/2D retail barcode scanner with GS1 Digital Link, "
		"Digimarc, mobile barcode reading, global-shutter imaging and multiple POS interfaces. "
		"Ideal for supermarkets, fashion retail, pharmacies, specialty stores and self-checkout."
	)
	if not doc.card_image:
		doc.card_image = hero
	doc.final_cta_heading = "Specify Magellan 3610VSi for your checkout"
	doc.final_cta_description = (
		"Printechs can confirm interface, mounting, POS integration and multi-store rollout "
		"for Datalogic Magellan 3610VSi in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Datalogic Magellan 3610VSi Barcode Scanner Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Magellan 3610VSi high-performance 1D/2D retail barcode scanner for POS, "
		"self-checkout and kiosks. Available in Saudi Arabia from Printechs with integration "
		"and support."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "speed",
				"title": "Faster checkout",
				"description": "Advanced imaging and motion tolerance reduce repeated scans when operators present products naturally.",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Ready for modern barcode standards",
				"description": "1D, 2D, GS1 Digital Link, composite and Digimarc codes — printed or on a phone.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Mobile-friendly",
				"description": "Read loyalty cards, digital coupons, QR promotions, tickets and membership IDs from smartphones.",
				"sort_order": 3,
			},
			{
				"icon": "store",
				"title": "Compact POS installation",
				"description": "13.7 × 15.2 × 8.4 cm vertical form factor for counters where space is limited.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Supermarket checkout",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Datalogic 3610VSi scanner for supermarket checkout",
				"caption": "Attended lanes and compact grocery counters.",
				"sort_order": 1,
			},
			{
				"label": "Fashion POS",
				"image": copy_public_image("industry-fashion.jpg"),
				"image_alt": "Datalogic Magellan 3610VSi retail POS barcode scanner",
				"caption": "Fast identification in modern fashion checkout.",
				"sort_order": 2,
			},
			{
				"label": "Pharmacy",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Datalogic Magellan 3610VSi in pharmacy retail",
				"caption": "1D and 2D codes for pharmacy and healthcare retail.",
				"sort_order": 3,
			},
			{
				"label": "Saudi retail",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Datalogic Magellan 3610VSi scanner Saudi Arabia",
				"caption": "Supplied and supported by Printechs in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "scan",
				"title": "1D + 2D",
				"description": "Advanced barcode reading including GS1 Digital Link and Digimarc",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "1360 × 1120",
				"description": "Global-shutter image sensor",
				"sort_order": 2,
			},
			{
				"icon": "battery",
				"title": "1.2 W",
				"description": "Nominal operating power (no auxiliary handheld)",
				"sort_order": 3,
			},
			{
				"icon": "shield",
				"title": "3-year warranty",
				"description": "Factory warranty from the official datasheet",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "POS interfaces",
				"description": "OEM / IBM USB · RS-232 · USB Keyboard · USB COM",
				"sort_order": 5,
			},
			{
				"icon": "durability",
				"title": "IP52",
				"description": "Particulate and water sealing · 0–40 °C",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Scanner",
			[
				("Scanner type", "Vertical single-plane digital imaging scanner"),
				("Imaging technology", "Advanced digital area imaging"),
				("Image sensor", "1360 × 1120 pixels"),
				("Shutter", "Global shutter"),
				("Image capture", "Grayscale; BMP, JPEG, TIFF, RAW"),
				("Maximum grayscale read rate", "60 million pixels/sec"),
				("Read height", "15.0 cm / 6.0 in"),
			],
		),
		(
			"Decoding",
			[
				("Barcode capability", "1D, 2D, stacked, composite, GS1 Digital Link, Digimarc"),
				("1D codes", "Standard 1D codes including GS1 DataBar"),
				("2D codes", "Aztec Code, Data Matrix ECC200, QR Code"),
				(
					"Stacked codes",
					"GS1 DataBar stacked/composites, MicroPDF417, PDF417",
				),
				(
					"Stacked GS1 variants",
					"Expanded Stacked, Stacked Omnidirectional, GS1 Digital Link",
				),
				("Digital watermarks", "Digimarc Barcodes / GS1 Digital Watermark Code"),
				("Minimum 1D resolution", "3 mil"),
				("Minimum 2D resolution", "6 mil"),
				("Minimum print contrast", "25%"),
				("Pitch", "±65°"),
				("Roll", "0–360°"),
				("Skew", "±65°"),
				("Reading indicators", "Adjustable audio speaker, Good Read LED, Good Transmission"),
			],
		),
		(
			"Typical reading ranges",
			[
				("Code 39 – 5 mil", "1 to 13 cm"),
				("Code 39 – 7.5 mil", "0 to 18 cm"),
				("EAN – 10 mil", "0 to 19 cm"),
				("EAN – 13 mil", "0 to 22 cm"),
				("Code 39 – 20 mil", "0 to 26 cm"),
				("PDF – 6.6 mil", "1 to 12 cm"),
				("PDF – 10 mil", "0 to 18 cm"),
				("Data Matrix – 10 mil", "1 to 9 cm"),
				("Data Matrix – 15 mil", "0 to 16 cm"),
				("QR – 15 mil", "0 to 16 cm"),
				("Data Matrix – 20 mil", "0 to 18 cm"),
				("QR – 20 mil", "0 to 18 cm"),
				(
					"Note",
					"Actual distance depends on print resolution, symbol length, scan angle, contrast and ambient light.",
				),
			],
		),
		(
			"Interfaces & power",
			[
				("Interfaces", "OEM (IBM) USB, RS-232, USB Keyboard, USB COM"),
				("Host software", "Windows, Linux and Android via OPOS, JavaPOS or Android SDK"),
				("Configuration", "Magellan Aladdin"),
				("Remote management", "IoT platform for diagnostics, software upgrades and configuration"),
				("AC input", "100–240 VAC, 50–60 Hz"),
				("DC input", "5–12 V"),
				("Nominal power", "1.2 W (no auxiliary handheld)"),
				("Maximum power", "3 W (no auxiliary handheld)"),
				("Sleep mode", "1.0 W (no auxiliary handheld)"),
			],
		),
		(
			"Environment & physical",
			[
				("Ambient light", "0–86,100 lux"),
				("ESD protection", "25 kV air discharge"),
				("Humidity", "5–95%, non-condensing"),
				("IP rating", "IP52"),
				("Operating temperature", "0 to 40 °C"),
				("Storage / transport", "−40 to 70 °C"),
				("Dimensions", "13.7 × 15.2 × 8.4 cm"),
				("Weight", "0.60 kg / 1.3 lb"),
				("Environmental compliance", "China RoHS, EU RoHS"),
				("LED classification", "EN62471 and IEC62471, Exempt Group"),
				("Warranty", "3-year factory warranty"),
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
				"title": "Supermarkets & grocery",
				"description": "Fast barcode scanning at attended checkout lanes and compact retail counters.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Datalogic 3610VSi scanner for supermarket checkout",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Fashion & apparel",
				"description": "Compact hardware for fashion POS where products need fast barcode identification.",
				"image": copy_public_image("industry-fashion.jpg"),
				"image_alt": "Datalogic Magellan 3610VSi retail POS barcode scanner",
				"industry_link": "fashion",
				"sort_order": 2,
			},
			{
				"title": "Pharmacy",
				"description": "1D and 2D codes for pharmaceutical and healthcare-related retail workflows.",
				"image": copy_public_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmacy retail barcode scanning",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Convenience, specialty & self-checkout",
				"description": "High-frequency convenience retail, specialty stores, kiosks, ticketing, access control and price verification.",
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Datalogic Magellan 3610VSi scanner Saudi Arabia",
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
				"heading": "GS1 Digital Link and Digimarc on the same scanner",
				"body": (
					"The Magellan 3610VSi supports GS1 Digital Link so retailers can work with newer "
					"product identification — expiry-date management, recalls and richer product "
					"information — without a second device.\n\n"
					"It also decodes Digimarc Barcodes and GS1 Digital Watermark Codes embedded in "
					"packaging. Combined with QR Code, Data Matrix, Aztec, PDF417, MicroPDF417, "
					"GS1 DataBar and GS1 Composite, printed and mobile codes stay in one checkout motion."
				),
				"image": hero,
				"image_alt": "Datalogic Magellan 3610VSi barcode scanner",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Scan printed labels and phones without extra alignment",
				"body": (
					"Checkout operators can present products naturally. The 3600VSi platform is designed "
					"for improved throughput and motion tolerance, with pitch ±65°, roll 0–360° and "
					"skew ±65°.\n\n"
					"The 1360 × 1120 global-shutter sensor captures moving barcodes with less distortion. "
					"The same imager reads loyalty cards, digital coupons, QR promotions, tickets and "
					"membership IDs from a smartphone screen."
				),
				"image": copy_public_image("industry-retail.jpg"),
				"image_alt": "Datalogic Magellan 3610VSi retail POS barcode scanner",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Accessories and mounting options",
				"body": (
					"The Magellan 3600VSi family datasheet lists these accessories for counter and "
					"service deployments: 90ACC0598 Wall / Counter Mount, 90ACC0599 Tilt / Riser Mount, "
					"and 90ACC0515 Customer Service Scanner with Omni Mount.\n\n"
					"Printechs can confirm the correct mount, OEM USB or RS-232 cable and POS setup "
					"for your lane. The 3610VSi does not include UHF RFID, colour image capture, a "
					"colour video camera, USB-C Power Delivery or a powered auxiliary USB port — those "
					"are specified for 3650/3670 models only."
				),
				"image": hero,
				"image_alt": "Datalogic Magellan 3610VSi barcode scanner",
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "store",
				"title": "Product selection",
				"description": "Confirm 3610VSi versus other Magellan models for attended POS, SCO and kiosks.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "POS configuration",
				"description": "USB, RS-232, USB Keyboard and USB COM setup with Magellan Aladdin.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "Retail integration",
				"description": "Windows, Linux and Android via OPOS, JavaPOS or the Android SDK.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Mounting, multi-store rollout and after-sales service in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "Magellan 3610VSi scanner main unit", "sort_order": 1},
			{"item_description": "90ACC0598 — Wall / Counter Mount (optional)", "sort_order": 2},
			{"item_description": "90ACC0599 — Tilt / Riser Mount (optional)", "sort_order": 3},
			{
				"item_description": "90ACC0515 — Customer Service Scanner with Omni Mount (optional)",
				"sort_order": 4,
			},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.4708", 1),
			related_product_row("RET.SYS.DLG.4648", 2),
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
				"question": "What is the Datalogic Magellan 3610VSi?",
				"answer": (
					"The Magellan 3610VSi is a vertical single-plane digital imaging scanner "
					"designed for high-performance retail barcode scanning."
				),
				"sort_order": 1,
			},
			{
				"question": "Does the Magellan 3610VSi read QR codes?",
				"answer": (
					"Yes. It supports QR Code, Data Matrix and Aztec Code along with standard 1D "
					"and stacked barcode formats."
				),
				"sort_order": 2,
			},
			{
				"question": "Does the Magellan 3610VSi support GS1 Digital Link?",
				"answer": "Yes. GS1 Digital Link is included in the scanner's decoding capability.",
				"sort_order": 3,
			},
			{
				"question": "Can it scan barcodes from mobile phones?",
				"answer": (
					"Yes. The official datasheet states that it can read barcodes displayed on "
					"mobile phones as well as printed barcodes."
				),
				"sort_order": 4,
			},
			{
				"question": "Does the 3610VSi support RFID?",
				"answer": (
					"No integrated RFID capability is specified for the 3610VSi. The datasheet "
					"identifies RFID as available for the 3650/3670 models."
				),
				"sort_order": 5,
			},
			{
				"question": "What interfaces does the 3610VSi support?",
				"answer": "It supports OEM/IBM USB, RS-232, USB Keyboard and USB COM.",
				"sort_order": 6,
			},
			{
				"question": "What is the power consumption?",
				"answer": (
					"Nominal operating consumption is 1.2 W, maximum operating consumption is 3 W, "
					"and sleep mode consumption is 1.0 W when no auxiliary handheld device is attached."
				),
				"sort_order": 7,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The scanner comes with a 3-year factory warranty according to the official datasheet."
				),
				"sort_order": 8,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
