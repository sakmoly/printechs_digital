# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic CODiScan (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail-manufacturing-transportation-logistics-healthcare-other-applications/mobile-computers/codiscan-pd-1084.html
Datasheet: DS-CODISCAN-EN Rev D 20240214.

Wearable Bluetooth scanner (HS7600). Hand trigger and lanyard are sold separately.
Wi-Fi is on Gateway Connect only — not on the wearable itself.
Warranty is 1 year (covers the battery), not 3 years.
"""

from pathlib import Path
from shutil import copy2
from urllib.parse import quote
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SLUG = "datalogic-codiscan"
VIDEO_URL = "https://youtu.be/FC0RMAj4DGU"
CONNECT_VIDEO = "https://youtu.be/9lDy3QuVahU"
CHARGE_VIDEO = "https://youtu.be/LGuFSIULuVU"
MOUNT_VIDEO = "https://youtu.be/KDEcWjuK6uk"
INTRA_VIDEO = "https://youtu.be/64M5axPhF7o"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-codiscan-product.png": "/upload/products/GeneralDutyHandheldScanners/CODiScan_web.png",
	"datalogic-codiscan-1.jpg": "/upload/prod_line/CODiScan/Image1.jpg",
	"datalogic-codiscan-2.jpg": "/upload/prod_line/CODiScan/Image2.jpg",
	"datalogic-codiscan-3.jpg": "/upload/prod_line/CODiScan/Image3.jpg",
	"datalogic-codiscan-4.jpg": "/upload/prod_line/CODiScan/Image4.jpg",
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
	return download_file(filename, DATALOGIC_HOST + quote(OFFICIAL_IMAGES[filename], safe="/:+"))


def catalog_card_from_cutout(source_name: str, dest_name: str) -> str:
	"""Official web cutout is 288 px; pad/scale to a 1200×1200 catalog card."""
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	official_image(source_name)
	im = Image.open(source).convert("RGBA")
	scale = 900 / max(im.size)
	new = im.resize((int(im.width * scale), int(im.height * scale)), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


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
	doc.website_product_name = "Datalogic CODiScan"
	doc.display_name = "Datalogic CODiScan"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic CODiScan wearable Bluetooth scanner."
	doc.long_description = "<p>Datalogic CODiScan wearable Bluetooth scanner.</p>"
	doc.hero_image = official_image("datalogic-codiscan-product.png")
	return doc


def fill_datalogic_codiscan():
	doc = get_or_create()

	hero = catalog_card_from_cutout("datalogic-codiscan-product.png", "datalogic-codiscan-product.jpg")
	img1 = official_image("datalogic-codiscan-1.jpg")
	img2 = official_image("datalogic-codiscan-2.jpg")
	img3 = official_image("datalogic-codiscan-3.jpg")
	img4 = official_image("datalogic-codiscan-4.jpg")
	warehouse = copy_public_image("industry-warehouse-logistics.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	retail = copy_public_image("industry-retail.jpg")
	fashion = copy_public_image("industry-fashion.jpg")

	# Intentionally no Item — link later under ERP Item Link when the Item exists.
	doc.item = None
	doc.website_product_name = "Datalogic CODiScan"
	doc.display_name = "Datalogic CODiScan"
	doc.slug = SLUG
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Wearable Scanners"
	doc.category_label = "WEARABLE SCANNER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Lightweight size, heavyweight performance"
	doc.short_description = (
		"Datalogic CODiScan is a 44 g Bluetooth wearable 2D scanner for warehouse picking, "
		"e-commerce fulfilment, packing and sorting. Hands stay free — wear it on the hand, "
		"neck, belt or pocket — with Green Spot confirmation and up to 12,000 scans per charge."
	)
	doc.long_description = (
		"<p>CODiScan is Datalogic’s Bluetooth wearable scanner for transportation &amp; "
		"logistics, retail distribution and manufacturing. At 44 g / 1.5 oz it sits on the "
		"hand, neck, belt or pocket so both hands stay free for pick, pack and sort work.</p>"
		"<p>Datalogic’s comparison versus a traditional handheld is a weight saving of up to "
		"1.5 tons per shift, about 4 seconds saved per scan and up to 33% fewer errors — "
		"because the operator never puts the scanner down.</p>"
		"<p>The Smart Scanning System aims up to 1.5 m / 4.9 ft. Good-read feedback is Green "
		"Spot on the label, two lateral LED blades plus a rear spot (visible to 180°), "
		"adjustable 85 dBA audio and optional vibration.</p>"
		"<p>One 640 mAh charge runs up to 16 hours or 12,000 scans (about two shifts) and "
		"recharges in 2.15 hours. Chargers are 1-slot USB, modular 2-slot (stack to 6) or "
		"12-slot. The HS7600SR, HS7600MR and HS7600RT imagers ship without a trigger or "
		"lanyard — order those separately.</p>"
		"<p>Pair to Android with the Aladdin app, or use Gateway Connect for up to seven "
		"scanners on a PC, vehicle mount or Wi-Fi/cloud link. The wearable itself is "
		"Bluetooth 5.2 only — Wi-Fi sits on the gateway.</p>"
		"<p>Printechs specifies CODiScan for Saudi Arabia warehouses and e-commerce sites in "
		"Riyadh, Jeddah and Dammam. Link the ERP Item on this page when it is created; the "
		"URL stays /products/datalogic-codiscan.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = (
		"Datalogic CODiScan HS7600 wearable Bluetooth scanner on a hand trigger"
	)
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"44 g wearable · both hands free\n"
		"Bluetooth 5.2 · up to 100 m\n"
		"12,000 scans · 16-hour shift\n"
		"Green Spot · IP54 · 1.8 m drop"
	)
	doc.story_heading = "Hands-free scanning for pick, pack, sort and e-commerce"
	doc.visual_story_heading = "CODiScan in warehouse and fulfilment"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.card_title = "CODiScan"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"44 g Bluetooth wearable 2D scanner for picking and sorting: Green Spot, "
		"12,000 scans per charge, Aladdin pairing and Gateway Connect for up to 7 devices."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify CODiScan for hands-free warehouse teams"
	doc.final_cta_description = (
		"Printechs can confirm SR, mid-range or high-density optics, hand trigger vs "
		"lanyard, chargers and Gateway Connect for sites in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic CODiScan Wearable Scanner Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic CODiScan 44 g Bluetooth wearable scanner for warehouse picking, "
		"e-commerce, packing and sorting. Green Spot, 12,000 scans/charge. From Printechs."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "Both hands stay on the work",
				"description": (
					"At 44 g, CODiScan wears on the hand, neck, belt or pocket. Operators pick "
					"and scan without putting a gun down — Datalogic cites up to 4 seconds saved "
					"per scan versus a handheld."
				),
				"sort_order": 1,
			},
			{
				"icon": "inventory",
				"title": "Smart aim and Green Spot",
				"description": (
					"Intelligent aiming up to 1.5 m frames the right code first. Green Spot, "
					"180° LED blades, beep and vibration confirm the read on the label — not "
					"only on the device."
				),
				"sort_order": 2,
			},
			{
				"icon": "battery",
				"title": "Two shifts, one charge",
				"description": (
					"Up to 16 hours or 12,000 scans from the 640 mAh pack, 2.15-hour recharge, "
					"and 1-, 2-to-6- or 12-slot chargers so the fleet is ready for the next wave."
				),
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Aladdin and Gateway Connect",
				"description": (
					"Pair to Android with the Aladdin app. Gateway Connect links up to seven "
					"CODiScans to a PC, vehicle computer or Wi-Fi/cloud — the wearable itself "
					"is Bluetooth 5.2."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Wear it how the job needs",
				"image": img1,
				"image_alt": "Datalogic CODiScan wearable scanner mounting on hand, neck or belt",
				"caption": "Hand trigger, lanyard or pocket — one scanner, several wear styles.",
				"sort_order": 1,
			},
			{
				"label": "Pick, pack and sort",
				"image": img2,
				"image_alt": "CODiScan used hands-free in warehouse picking and sorting",
				"caption": "Built for distribution, e-commerce fulfilment and put-away.",
				"sort_order": 2,
			},
			{
				"label": "Charge the fleet",
				"image": img3,
				"image_alt": "Datalogic CODiScan multi-slot charging options",
				"caption": "1-slot USB, modular 2-slot (stack to 6) or 12-slot charging.",
				"sort_order": 3,
			},
			{
				"label": "Connect seven at a station",
				"image": img4,
				"image_alt": "CODiScan Gateway Connect pairing for fixed or vehicle hosts",
				"caption": "Gateway Connect: up to 7 wearables to a PC, Rhino or Wi-Fi.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "device",
				"title": "44 g / 1.5 oz",
				"description": "53 × 44 × 19 mm wearable body",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "1280 × 960",
				"description": "1D/2D · Green Spot · aim to 1.5 m",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Bluetooth 5.2",
				"description": "Up to 100 m · Wi-Fi on Gateway only",
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "640 mAh",
				"description": "16 h / 12,000 scans · 2.15 h charge",
				"sort_order": 4,
			},
			{
				"icon": "rugged",
				"title": "IP54",
				"description": "1.8 m drop · 1,000 tumbles @ 0.5 m",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "1-year warranty",
				"description": "Covers battery · EASEOFCARE 3/5 yr",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Scanner",
			[
				("Family", "CODiScan HS7600 Bluetooth wearable 2D imager"),
				("Standard Range", "HS7600SR — everyday 1D/2D at typical pick distances"),
				("Mid Range", "HS7600MR — longer 1D reach (Code 39 20 mil up to 160 cm)"),
				("High Density", "HS7600RT — short-range high-density codes"),
				("Trigger / lanyard", "Not in the box — order hand trigger or lanyard separately"),
				("Imager", "1280 × 960 pixels"),
				("Aiming", "650 nm, 1 mW plus Datalogic Green Spot on the code"),
				("Smart aiming", "Frames the barcode before the trigger; up to 1.5 m / 4.9 ft"),
				("Field of view SR", "42° horizontal × 32° vertical"),
				("Field of view MR", "30° horizontal × 23° vertical"),
				("Reading angle", "Skew ±60°; pitch ±60°; roll ±180°"),
				("Ambient light", "0–100,000 lux"),
				("Print / images", "Captures 1D/2D barcodes and images"),
			],
		),
		(
			"Feedback & trigger",
			[
				("Green Spot", "Good-read projected onto the scanned label"),
				("LEDs", "2 lateral blades + rear spot; good-read, battery, Bluetooth pairing"),
				("LED visibility", "Feedback visible from any angle up to 180°"),
				("Audio", "85 dBA, adjustable"),
				("Haptic", "Vibration option for quiet areas"),
				("On-device key", "Multifunction key: trigger, battery, connectivity, custom"),
				("Hand trigger", "Adjustable L/R, one size; 5 million hits; sold separately"),
				("Glove fabric", "Electronics separate from fabric; wash fabric at 30 °C"),
			],
		),
		(
			"Decoding",
			[
				("1D / linear", "All standard 1D including GS1 DataBar linear"),
				("2D codes", "PDF417, MicroPDF417, Data Matrix, QR, Micro QR, Aztec, MaxiCode"),
				("Postal", "US PostNet, US Planet, UK, Australia, Japan, Dutch KIX"),
			],
		),
		(
			"Wireless & gateway",
			[
				("On the wearable", "Bluetooth 5.2 Classic / BLE, Class 1/2/3 — no onboard Wi-Fi"),
				("Bluetooth stack", "BLE 4.0, 4.1, 4.2, 5.0, 5.1 and 5.2"),
				("BT range", "Up to 100 m / 328 ft to host (Gateway range depends on host)"),
				("Gateway Wi-Fi", "IEEE 802.11 b/g/n, 1×1, 20 MHz, 2.4 GHz — on GWU-HS7600 only"),
				("Gateway security", "WPA2/WPA3 Personal; WPA2 Enterprise PEAP, TLS, TTLS"),
				("Gateway protocols", "MQTT 3.1 / 3.1.1 and WebSocket client"),
				("Gateway capacity", "1 gateway manages up to 7 CODiScan units"),
				("Android pairing", "Aladdin app — pairing, firmware, symbologies, settings"),
				("Recommended hosts", "Memor 10/11, Skorpio X5, Rhino II (see product manual)"),
			],
		),
		(
			"Battery & charging",
			[
				("Battery", "Li-Polymer 640 mAh, rechargeable (covered by factory warranty)"),
				("Run time", "Up to 16 hours (1 scan / 5 s) or 12,000 scans, settings dependent"),
				("Charge time", "2.15 hours in a Datalogic charging station"),
				("1-slot", "SC-HS7600 USB cap charger (USB-A to USB-C cable in kit)"),
				("2-slot modular", "MC-HS7600 — stack to 6 slots on one power supply"),
				("12-slot", "MC-12HS7600 — fleet charging (needs 90ACC0350 PSU + cord)"),
				("Lanyard charge", "LH-HS7600 lanyard has a USB charge port; cable ordered separately"),
				("Charger power", "5 VDC, 1.2 A via the listed power supplies"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Dimensions", "53 × 44 × 19 mm / 2.0 × 1.7 × 0.7 in"),
				("Weight", "44 g / 1.5 oz"),
				("Sealing", "IP54 (EN 60529)"),
				("Drop", "Multiple drops from 1.8 m / 5.9 ft onto concrete (IEC 60068-2-31)"),
				("Tumble", "1,000 cycles at 0.5 m / 1.6 ft"),
				("Impact", "> IK06 (1 J) IEC 60068-2-75"),
				("Operating temp", "−20 to 50 °C / −4 to 122 °F"),
				("Charging temp", "0 to 40 °C / 32 to 104 °F"),
				("Storage temp", "−20 to 60 °C / −4 to 140 °F"),
				("Compliance", "China RoHS, EU RoHS, REACH"),
				("Warranty", "1-year factory warranty (covers the battery)"),
				("EASEOFCARE", "3- or 5-year plans (cover battery); also for chargers and Gateway"),
			],
		),
		(
			"Typical depth of field (SR / MR)",
			[
				("SR Code 39 3 mil", "13–22 cm / 5.1–8.6 in"),
				("SR Code 128 5 mil", "10–30 cm / 3.9–11.8 in"),
				("SR PDF417 5 mil", "12–19 cm / 4.7–7.5 in"),
				("SR Data Matrix 10 mil", "10–28 cm / 3.9–11.0 in"),
				("SR EAN/UPC 13 mil", "4.5–74 cm / 1.7–29.1 in"),
				("SR QR 15 mil", "4–37 cm / 1.5–14.5 in"),
				("SR Code 39 20 mil", "40–110 cm / 15.7–43.3 in"),
				("MR Code 128 5 mil", "21–52 cm / 8.2–20.4 in"),
				("MR PDF417 5 mil", "22–30 cm / 8.6–11.8 in"),
				("MR Data Matrix 10 mil", "20–45 cm / 7.8–17.7 in"),
				("MR UPC-A 13 mil", "8–100 cm / 3.1–39.3 in"),
				("MR Code 39 20 mil", "Up to 160 cm / 62.9 in"),
				("MR Code 39 100 mil", "Up to 500 cm / 196.8 in"),
				("Note", "DoF depends on symbol, angle, print quality and light. HD DoF not listed"),
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
				"title": "Warehouse picking, packing, put-away and sorting",
				"description": (
					"Hands-free 1D/2D on the pick face, pack bench and sort lane. Wear the "
					"imager and keep both hands on cartons."
				),
				"image": warehouse,
				"image_alt": "Warehouse aisle for CODiScan wearable picking and sorting",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "E-commerce fulfilment and click & collect",
				"description": (
					"Scan each unit without holstering a gun. Datasheet use cases include "
					"click and collect, order fulfilment and outbound."
				),
				"image": fashion,
				"image_alt": "E-commerce and fashion fulfilment scanning with a wearable",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Manufacturing WIP and finished-goods check",
				"description": (
					"Trace parts and assemblies, verify finished goods and count inventory "
					"on the line without occupying a hand."
				),
				"image": packaging,
				"image_alt": "Manufacturing and packaging line wearable barcode traceability",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Retail back-of-store inventory",
				"description": (
					"Receiving, replenishment and stock work behind the shop — not a POS "
					"lane scanner. Pair with Memor or Skorpio on Android."
				),
				"image": retail,
				"image_alt": "Retail back-of-store inventory with a wearable scanner",
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
				"heading": "Handle more with Datalogic CODiScan",
				"body": (
					"Official Datalogic film: lightweight size, heavyweight performance. "
					"CODiScan is the wearable Bluetooth scanner for warehouse, e-commerce "
					"and manufacturing teams that need both hands on the goods."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic CODiScan wearable Bluetooth scanner",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Mounting — hand, neck, belt or pocket",
				"body": (
					"One scanner, several wear styles. The adjustable left or right hand "
					"trigger is one-size and works bare-handed or over a work glove. The "
					"electronics unclip from the fabric so you can wash the glove at 30 °C "
					"and reuse the trigger.\n\n"
					"The extensible lanyard holds the unit at the neck, belt or pocket and "
					"adds a USB charge port. Hand trigger and lanyard are ordered separately "
					"from HS7600SR / MR / RT."
				),
				"video_url": MOUNT_VIDEO,
				"image": img1,
				"image_alt": "CODiScan hand trigger and lanyard mounting options",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Charging — 1, 2-to-6 or 12 slots",
				"body": (
					"A 2.15-hour charge returns up to 16 hours or 12,000 scans. Choose the "
					"USB cap charger for a single unit, stack modular 2-slot docks to six "
					"positions on one PSU, or park a fleet in the 12-slot station.\n\n"
					"Modules can sit on a bench or mount vertically. Less part-number clutter, "
					"fewer devices sitting idle between waves."
				),
				"video_url": CHARGE_VIDEO,
				"image": img3,
				"image_alt": "Datalogic CODiScan 1-slot, modular and 12-slot chargers",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Connectivity — Aladdin and Gateway Connect",
				"body": (
					"The wearable is Bluetooth 5.2 only. Pair it to an Android mobile computer "
					"with the Aladdin app (pre-installed on Memor 11; also via Scan2Deploy) "
					"for pairing, firmware and symbology settings.\n\n"
					"Gateway Connect (GWU-HS7600) takes up to seven CODiScans to a PC or "
					"vehicle mount over USB, or to the cloud over Wi-Fi. Do not specify "
					"onboard Wi-Fi on the scanner itself."
				),
				"video_url": CONNECT_VIDEO,
				"image": img4,
				"image_alt": "CODiScan Aladdin app and Gateway Connect",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Intralogistics — pick, pack, sort",
				"body": (
					"Datalogic positions CODiScan in the wider intralogistics stack: "
					"distribution centres, warehouses, e-commerce and in-plant logistics. "
					"Watch the Complete Intralogistics film for how wearable scanning sits "
					"next to handhelds, mobile computers and fixed readers."
				),
				"video_url": INTRA_VIDEO,
				"image": img2,
				"image_alt": "CODiScan in a Datalogic intralogistics warehouse workflow",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Saudi Arabia specification and support",
				"body": (
					"Printechs helps choose HS7600SR, HS7600MR or HS7600RT, left or right "
					"trigger versus lanyard, charger density and whether you need Gateway "
					"Connect or Aladdin-to-Android (Memor / Skorpio) for Riyadh, Jeddah and "
					"Dammam sites.\n\n"
					"Factory warranty is 1 year and covers the battery. EASEOFCARE 3- or "
					"5-year plans extend coverage for the scanner, chargers and gateway. "
					"Create the ERP Item when ready and link it on this Website Product — "
					"the public URL does not change."
				),
				"image": warehouse,
				"image_alt": "CODiScan wearable scanning support in Saudi Arabia warehouses",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "scan",
				"title": "Optic selection",
				"description": "HS7600SR standard, HS7600MR mid-range or HS7600RT high-density for the codes you scan.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Wear style & chargers",
				"description": "Left/right trigger or lanyard, plus 1-, 2-to-6- or 12-slot charging for the shift pattern.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "Host pairing",
				"description": "Aladdin to Android (Memor, Skorpio) or Gateway Connect for up to 7 units on a PC or Wi-Fi.",
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
			{"item_description": "CODiScan HS7600 wearable scanner (SR, MR or RT — configuration dependent)", "sort_order": 1},
			{"item_description": "Built-in 640 mAh Li-Polymer battery", "sort_order": 2},
			{"item_description": "Hand trigger or lanyard sold separately — not in the scanner carton", "sort_order": 3},
			{"item_description": "Optional 1-slot, modular 2-slot or 12-slot charger", "sort_order": 4},
			{"item_description": "Optional Gateway Connect (up to 7 scanners) and Aladdin software", "sort_order": 5},
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
				"question": "What is the Datalogic CODiScan?",
				"answer": (
					"A 44 g Bluetooth wearable 2D scanner (HS7600) for warehouse picking, "
					"e-commerce fulfilment, packing, sorting and shop-floor traceability. "
					"It is not a POS checkout scanner."
				),
				"sort_order": 1,
			},
			{
				"question": "What is the difference between HS7600SR, MR and RT?",
				"answer": (
					"SR is Standard Range for everyday 1D/2D. MR is Mid Range (longer 1D; "
					"Code 39 20 mil up to 160 cm, 100 mil up to 5 m). RT is Short Range High "
					"Density for tight, high-resolution codes."
				),
				"sort_order": 2,
			},
			{
				"question": "Does the scanner include a hand trigger?",
				"answer": (
					"No. Datalogic sells HS7600SR / MR / RT without a trigger or lanyard. "
					"Order the adjustable left or right hand trigger, or the extensible "
					"lanyard, as separate accessories."
				),
				"sort_order": 3,
			},
			{
				"question": "Does CODiScan have Wi-Fi or 5G?",
				"answer": (
					"The wearable is Bluetooth 5.2 only. Wi-Fi (2.4 GHz 802.11 b/g/n) is on "
					"Gateway Connect, not on the scanner. There is no cellular / 5G modem."
				),
				"sort_order": 4,
			},
			{
				"question": "How do I connect it to a phone, PDA or PC?",
				"answer": (
					"Use the Aladdin app to pair with Android mobile computers (officially "
					"listed: Memor 10/11, Skorpio X5; also used with later Memor / Skorpio). "
					"Gateway Connect joins up to seven scanners to a PC, vehicle mount or "
					"Wi-Fi/cloud."
				),
				"sort_order": 5,
			},
			{
				"question": "How long does the battery last?",
				"answer": (
					"Up to 16 hours (one scan every 5 seconds) or 12,000 scans per charge, "
					"depending on settings and environment. A Datalogic station recharges "
					"the 640 mAh pack in 2.15 hours."
				),
				"sort_order": 6,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page is published without an Item link. ERP already has Mid Range "
					"(RET.SYS.DLG.4349) and Standard Range (RET.SYS.DLG.4574). Link the SKU "
					"you sell under ERP Item Link; the URL stays /products/datalogic-codiscan."
				),
				"sort_order": 7,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The official datasheet specifies a 1-year factory warranty and it covers "
					"the battery. EASEOFCARE 3- or 5-year plans extend cover for the scanner, "
					"chargers and Gateway."
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
