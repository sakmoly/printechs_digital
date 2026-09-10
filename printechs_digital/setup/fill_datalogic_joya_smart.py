# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic Joya Smart & Smart+ (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail/mobile-computers/joya-smart-smart+-pd-1148.html
Datasheet: DS-JOYASMARTANDSMART+-EN Revision A 20251027.

Joya Smart (911450001) is the current AI self-shopping PDA.
Joya Smart+ (911450002) is listed by Datalogic as coming soon — smartphone-like,
front-facing scan. Do not sell Smart+ as shipping today.
Android path is to 18 (not 19). Warranty is 1 year.
Shop Guard AI needs the rear camera + Shop Guard software — not a standalone claim.
"""

from pathlib import Path
from shutil import copy2
from urllib.parse import quote
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SLUG = "datalogic-joya-smart"
VIDEO_URL = "https://youtu.be/uEkF4k59gSY"
AI_VIDEO = "https://youtu.be/kSG8zCZ2gf4"
STORE_VIDEO = "https://youtu.be/pjezQXMf1jo"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-joya-smart-cutout.png": "/upload/products/MobileComputers/JoyaSmart-min.png",
	"datalogic-joya-smart-3.jpg": "/upload/prod_line/JoyaSmart/3_2.jpg",
	"datalogic-joya-smart-4.jpg": "/upload/prod_line/JoyaSmart/4_2.jpg",
	"datalogic-joya-smart-5.jpg": "/upload/prod_line/JoyaSmart/5_2.jpg",
	"datalogic-joya-smart-6.jpg": "/upload/prod_line/JoyaSmart/6.jpg",
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
	doc.website_product_name = "Datalogic Joya Smart & Smart+"
	doc.display_name = "Datalogic Joya Smart & Smart+"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic Joya Smart AI self-shopping mobile computer."
	doc.long_description = "<p>Datalogic Joya Smart AI self-shopping mobile computer.</p>"
	doc.hero_image = official_image("datalogic-joya-smart-cutout.png")
	return doc


def fill_datalogic_joya_smart():
	doc = get_or_create()

	hero = catalog_card_from_cutout(
		"datalogic-joya-smart-cutout.png", "datalogic-joya-smart-product.jpg"
	)
	img3 = official_image("datalogic-joya-smart-3.jpg")
	img4 = official_image("datalogic-joya-smart-4.jpg")
	img5 = official_image("datalogic-joya-smart-5.jpg")
	img6 = official_image("datalogic-joya-smart-6.jpg")
	retail = copy_public_image("industry-retail.jpg")
	fashion = copy_public_image("industry-fashion.jpg")
	food = copy_public_image("industry-food-beverage.jpg")

	# Intentionally no Item — ERP currently has Joya Touch A6, not Joya Smart.
	doc.item = None
	doc.website_product_name = "Datalogic Joya Smart & Smart+"
	doc.display_name = "Datalogic Joya Smart & Smart+"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Mobile Computers"
	doc.category_label = "SELF-SHOPPING MOBILE COMPUTER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Re-shaping the future of self-shopping"
	doc.short_description = (
		"Datalogic Joya Smart is an AI-enabled personal shopping PDA for grocery and "
		"hypermarket self-scan: 5\" HD display, Green Spot 2D, rear 13 MP Shop Guard camera, "
		"Wi-Fi 6E and wireless charging. Joya Smart+ (front-facing scan) is listed as coming soon."
	)
	doc.long_description = (
		"<p>Joya Smart is Datalogic’s next self-shopping handset for grocery, hypermarkets, "
		"DIY and cash-and-carry. Shoppers pick a device at the entrance, scan as they walk "
		"and tap-to-pay on the unit — or hand it back at a Smart Portal / checkout.</p>"
		"<p>This SKU (911450001) is 6 GB / 64 GB, Qualcomm QCS4490 octa-core 2.4 GHz, "
		"Android 15 GMS (path to Android 18), Wi-Fi 6E, Bluetooth 5.3, NFC and IP54. The "
		"5\" HD (1280 × 720, 450 nits) panel uses Gorilla Glass 3. The imager is Halogen "
		"DE2121-DL with Green Spot; a 13 MP rear camera feeds Shop Guard AI when that app "
		"is deployed.</p>"
		"<p>Shop Guard watches the cart through the rear camera, flags missed scans and "
		"shows associates the image of items to re-check. Auto-scan and GS1 Digital Link "
		"put product facts, nutrition and promotions on screen from a QR. Bluetooth headsets "
		"are supported for visually impaired shoppers.</p>"
		"<p>Wireless Qi EPP 10 W charging (same speed as pin cradles) keeps contacts off "
		"the device. One PSU can feed up to nine docks; fast or eco charge modes are listed. "
		"Wall brackets are specified to reuse existing Joya Touch positions.</p>"
		"<p>Joya Smart+ (911450002) is on the same electronics list but Datalogic still "
		"marks it <strong>coming soon</strong> — smartphone-like body and front-facing scan. "
		"Do not quote Smart+ as available stock until Datalogic ships it.</p>"
		"<p>The family won a Red Dot Design Award 2026. Printechs specifies Joya Smart with "
		"Shopevolution / Smart Portal for Saudi grocery and hypermarket projects. Create the "
		"ERP Item and link it here when you buy; the URL stays /products/datalogic-joya-smart.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = (
		"Datalogic Joya Smart AI-enabled self-shopping mobile computer, front and scan window"
	)
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"5\" HD · Android 15 → 18\n"
		"Shop Guard AI · 13 MP rear\n"
		"Wi-Fi 6E · Green Spot 2D\n"
		"IP54 · Qi 10 W · 1-year"
	)
	doc.story_heading = "AI self-shopping for grocery, hypermarkets and DIY"
	doc.visual_story_heading = "Joya Smart in the store"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.card_title = "Joya Smart"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"AI self-shopping PDA: 5\" HD, Green Spot 2D, 13 MP Shop Guard camera, Wi-Fi 6E "
		"and wireless charging. Smart+ front-scan model is coming soon."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify Joya Smart for your self-scan fleet"
	doc.final_cta_description = (
		"Printechs can confirm Smart vs upcoming Smart+, docks, Shop Guard, Shopevolution "
		"and Smart Portal entry for grocery and hypermarkets in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Retail Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Joya Smart Self-Shopping PDA Saudi Arabia | Printechs"
	doc.meta_description = (
		"Datalogic Joya Smart AI self-shopping device: 5\" HD, Green Spot 2D, Shop Guard "
		"13 MP camera, Wi-Fi 6E and wireless charging. From Printechs in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "Green Spot 2D, then shop",
				"description": (
					"Halogen DE2121-DL reads damaged or poorly printed labels. Green Spot and "
					"a smiley LED under the display confirm the read before the item hits the cart."
				),
				"sort_order": 1,
			},
			{
				"icon": "loyalty",
				"title": "Shop Guard on the rear camera",
				"description": (
					"The 13 MP rear camera plus Shop Guard AI watches the basket for missed "
					"scans and shows associates the image of items to re-check — not a claim "
					"without that software."
				),
				"sort_order": 2,
			},
			{
				"icon": "checkout",
				"title": "Tap-to-pay on the device",
				"description": (
					"NFC (ISO 14443/15693, Mifare, FeliCa) supports contactless cards, wallets "
					"and Apple ECP. EMVCo RR PCD Level 1 is listed. Unlock from the cradle by "
					"loyalty scan or NFC tap."
				),
				"sort_order": 3,
			},
			{
				"icon": "battery",
				"title": "Wireless charge, fewer contacts",
				"description": (
					"Qi EPP 10 W on the device and listed docks. One PSU can feed up to nine "
					"units. Fast or eco charge. Compatible wall kits reuse Joya Touch holes."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Self-scan on the shop floor",
				"image": img3,
				"image_alt": "Shopper using Datalogic Joya Smart for in-store self-scanning",
				"caption": "5\" HD, GS1 Digital Link product facts and auto-scan mode.",
				"sort_order": 1,
			},
			{
				"label": "AI cart check",
				"image": img4,
				"image_alt": "Joya Smart rear camera Shop Guard checking a shopping cart",
				"caption": "Shop Guard flags missed scans and speeds associate re-checks.",
				"sort_order": 2,
			},
			{
				"label": "Wireless docks",
				"image": img5,
				"image_alt": "Joya Smart multi-slot wireless charging cradles on a store wall",
				"caption": "3-slot wall or single-slot lock docks; pin-free Qi charge.",
				"sort_order": 3,
			},
			{
				"label": "Two form factors",
				"image": img6,
				"image_alt": "Joya Smart and upcoming Joya Smart+ self-shopping devices",
				"caption": "Smart now. Smart+ (front-facing scan) is still coming soon.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "display",
				"title": "5\" HD 450 nits",
				"description": "1280 × 720 · Gorilla Glass 3 · glove/stylus",
				"sort_order": 1,
			},
			{
				"icon": "android",
				"title": "Android 15",
				"description": "Path to Android 18 · GMS · QCS4490",
				"sort_order": 2,
			},
			{
				"icon": "scan",
				"title": "DE2121-DL",
				"description": "Green Spot 2D · 13 MP rear AI camera",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "Wi-Fi 6E",
				"description": "BT 5.3 · NFC pay · 2×2 MIMO",
				"sort_order": 4,
			},
			{
				"icon": "battery",
				"title": "3,500 mAh",
				"description": "Qi EPP 10 W · listed 12+ hour shift",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "1-year warranty",
				"description": "Factory · EASEOFCARE and Shield",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Models & platform",
			[
				("Family", "Joya Smart & Smart+ personal shopping / associate PDA"),
				("Joya Smart", "911450001 — current shipping self-shopping form"),
				("Joya Smart+", "911450002 — coming soon; smartphone-like, front-facing scan"),
				("Processor", "Qualcomm QCS4490 Kryo octa-core 2.4 GHz"),
				("Memory", "6 GB RAM / 64 GB flash"),
				("OS", "Android 15 GMS, upgradeable to Android 18 (not 19)"),
				("Colours", "Light grey / dark grey (customisable colours listed)"),
			],
		),
		(
			"Display, scan & camera",
			[
				("Display", "5\" HD 1280 × 720, 450 nits, optically bonded"),
				("Touch", "5-point capacitive, Gorilla Glass 3, gloves, stylus, water-drop reject"),
				("Keys", "1 physical scan trigger"),
				("Imager", "Halogen DE2121-DL 1D/2D with Green Spot"),
				("Rear camera", "13 MP autofocus, LED torch — Shop Guard / Snap OCR / auto-scan"),
				("Smart+", "Front-facing scan on the coming-soon body — not on Joya Smart"),
				("Feedback", "Green Spot plus smiley LED under the display"),
				("GS1", "GS1 Digital Link for on-screen product, nutrition and promotions"),
			],
		),
		(
			"Wireless, sensors & pay",
			[
				("WLAN", "Wi-Fi 6E 802.11 a/b/g/n/ac/ax; 2.4 / 5 / 6 GHz typical; 2×2 MIMO"),
				("Security", "WPA3 Enterprise 192-bit supported"),
				("Bluetooth", "5.3 Classic and BLE (headsets for accessibility listed)"),
				("NFC", "Tags 2/3/4/5; ISO14443-4 A/B; ISO15693; Mifare; FeliCa; card emulator"),
				("Payments", "Contactless + Apple ECP; EMVCo RR PCD Level 1; Strongbox SE"),
				("Indoor location", "IMU + third-party software; no extra RTLS infrastructure claimed"),
				("Sensors", "Accel, gyro, magnetometer, barometer (Z), ToF"),
				("USB", "USB 2.0 Type-C for maintenance"),
			],
		),
		(
			"Battery, docks & audio",
			[
				("Battery", "Replaceable Li-Ion 3,500 mAh (94ACC0433)"),
				("Wireless charge", "WPC Qi EPP, 10 W — on device and listed WLC docks"),
				("Shift claim", "Datasheet graphic lists 12+ hours (settings dependent)"),
				("3-slot dock", "94A150138 pin / 94A150148 WLC — wall; needs 94ACC0380 + cord"),
				("Single dock", "Locking 94A150140 / 94A150150; unlock 94A150139 / 94A150149"),
				("PSU share", "94ACC0380 also used on Memor 12-17 / 30-35 docks; daisy-chain 91ACC0049"),
				("Nine-up", "One power supply can charge up to nine devices; fast or eco mode"),
				("Audio", "1 mic; 0.8 W speaker (1 W short), 92 dBA"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("Size", "214 × 77.8 × 104 mm / 8.42 × 3.06 × 4.09 in"),
				("Weight", "303 g / 10.68 oz with battery"),
				("Sealing", "IP54"),
				("Drop no boot", "Multiple 1.3 m / 4 ft to concrete, MIL-STD-810H"),
				("Drop with boot", "Multiple 1.5 m / 6 ft, −10 to 50 °C, MIL-STD-810H (94ACC0431)"),
				("Tumble no boot", "1,000 × 0.5 m at room temp (IEC 60068-2-32)"),
				("Tumble with boot", "500 × 1.0 m at room temp"),
				("Operating", "−10 to 50 °C / 14 to 122 °F"),
				("Storage", "−40 to 70 °C / −40 to 158 °F"),
				("ESD", "15 kV air / 8 kV contact"),
				("Hygiene", "Chemical-resistant plastics; listed IPA, bleach and peroxide cleaners"),
				("Warranty", "1-year factory warranty; EASEOFCARE and Datalogic Shield optional"),
			],
		),
		(
			"Software ecosystem",
			[
				("Self-shopping", "Shopevolution, EasyShop and major retailer / ISV apps"),
				("Shop Guard", "AI cart validation via rear camera — specify the app with the device"),
				("Mobility Suite", "Launcher kiosk, Enterprise Browser, Integrity KIT, SoftSpot, Wedge"),
				("Staging", "Scan2Deploy, OEMConfig, Android Zero-Touch / QR / NFC bump"),
				("Shield", "Android security patches and OS upgrades with EASEOFCARE"),
				("UEM", "SOTI, Workspace ONE, Intune, 42Gears, Ivanti, OEMConfig-compliant EMM"),
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
				"title": "Grocery and hypermarket self-scan",
				"description": (
					"Shoppers scan as they walk, see GS1 facts on the 5\" display and tap-to-pay "
					"or finish at a Smart Portal / SCO lane."
				),
				"image": retail,
				"image_alt": "Grocery retail aisle for Joya Smart self-shopping",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Click & collect and associate picking",
				"description": (
					"Datasheet associate uses: online-order picking, replenishment, inventory, "
					"markdowns, stock lookup and queue-busting mPOS."
				),
				"image": food,
				"image_alt": "Food retail click-and-collect picking with a shopping PDA",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Fashion, DIY and department stores",
				"description": (
					"Product information, availability and loyalty lookup on a customer-facing "
					"device — same Wi-Fi 6E platform as grocery."
				),
				"image": fashion,
				"image_alt": "Fashion and department-store assisted shopping PDA",
				"industry_link": "fashion",
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Joya Smart & Smart+ — official family film",
				"body": (
					"Datalogic’s product film for the Joya Smart family. Joya Smart is the "
					"AI self-shopping handset shipping today. Smart+ (front-facing scan, "
					"smartphone-like body) is still marked coming soon on the official page."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic Joya Smart self-shopping mobile computer",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Shop Guard AI and the 13 MP rear camera",
				"body": (
					"Joya Smart is positioned as the first self-shopping device with integrated "
					"AI. The rear camera plus Shop Guard watches the cart, flags missed scans "
					"and shows associates which items to re-check.\n\n"
					"Specify Shop Guard (and Shopevolution if you use Datalogic’s stack) with "
					"the hardware. The camera alone is not a shrink system."
				),
				"video_url": AI_VIDEO,
				"image": img4,
				"image_alt": "Joya Smart Shop Guard AI cart monitoring",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Wireless docks and Joya Touch upgrade",
				"body": (
					"Qi EPP 10 W charging is on the device and on the WLC docks. Pin-style "
					"3-slot wall cradles remain on the list. Datalogic says wireless charge "
					"matches conventional pin speed and that wall kits can reuse existing "
					"Joya Touch positions.\n\n"
					"One 94ACC0380 PSU can feed up to nine devices (fast or eco). Locking "
					"single-slot docks and trolley holders (94ACC0427) complete a fleet."
				),
				"image": img5,
				"image_alt": "Joya Smart wireless charging docks and wall brackets",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Intelligent Store with Smart Portal",
				"body": (
					"Entrance unlock is a loyalty scan or NFC tap. Pair Joya Smart with "
					"Datalogic Smart Portal at the door, Magellan or Gryphon at SCO, and "
					"Shopevolution 8.x in the back office.\n\n"
					"Watch Empowering the Intelligent Store for the wider Datalogic retail "
					"context. Printechs stages MDM, kiosk lock and Shop Guard for KSA grocers."
				),
				"video_url": STORE_VIDEO,
				"image": img3,
				"image_alt": "Joya Smart in a Datalogic Intelligent Store self-shopping journey",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Saudi Arabia specification and support",
				"body": (
					"Quote Joya Smart 911450001 today. Treat 911450002 Smart+ as coming soon "
					"until Datalogic confirms shipment. Confirm dock type (pin vs WLC), rubber "
					"boot, Shop Guard and whether you keep Joya Touch wall geometry.\n\n"
					"Factory warranty is 1 year. EASEOFCARE and Datalogic Shield cover hardware "
					"and Android patches. ERP still has Joya Touch A6 only — create a Joya Smart "
					"Item and link it on this page; the URL does not change."
				),
				"image": retail,
				"image_alt": "Joya Smart self-shopping rollout support in Saudi retail",
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "device",
				"title": "Smart vs Smart+",
				"description": "Quote Joya Smart now. Smart+ front-scan is coming soon — do not promise stock dates.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Docks & walls",
				"description": "3-slot or locking single, pin or Qi, plus brackets that reuse Joya Touch holes.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "Shopevolution & Shop Guard",
				"description": "Self-scan app, AI cart check, Smart Portal unlock and UEM/kiosk lock.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Pilot, staging, EASEOFCARE and Shield for grocery and hypermarkets in KSA.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "Joya Smart PDA 911450001 (6 GB / 64 GB, Android 15, Wi-Fi 6E) — or Smart+ when shipped", "sort_order": 1},
			{"item_description": "3,500 mAh replaceable battery (94ACC0433 typically ordered with the fleet)", "sort_order": 2},
			{"item_description": "Dock, PSU and line cord sold separately (3-slot, single lock or USB single)", "sort_order": 3},
			{"item_description": "Optional rubber boot, belt holster, trolley holder and screen protectors", "sort_order": 4},
			{"item_description": "Shop Guard, Shopevolution and Mobility Suite licensed / staged as required", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("RET.SYS.DLG.5029", 1),
			related_product_row("RET.SYS.DLG.4648", 2),
			related_product_row("RET.SYS.DLG.4981", 3),
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
				"question": "What is Datalogic Joya Smart?",
				"answer": (
					"An AI-enabled personal shopping PDA for grocery and hypermarket self-scan: "
					"5\" HD, Green Spot 2D, 13 MP rear camera for Shop Guard, Wi-Fi 6E and "
					"wireless charging. It replaces the older Joya Touch generation."
				),
				"sort_order": 1,
			},
			{
				"question": "Is Joya Smart+ available now?",
				"answer": (
					"Datalogic still lists Smart+ as coming soon. It shares the 6/64, Android 15, "
					"Wi-Fi 6E spec but adds a smartphone-like body and front-facing scan. Quote "
					"Joya Smart (911450001) unless shipment of 911450002 is confirmed."
				),
				"sort_order": 2,
			},
			{
				"question": "Does Shop Guard work without extra software?",
				"answer": (
					"No. The 13 MP camera is in the hardware. Cart validation, missed-scan "
					"alerts and associate re-check images need Shop Guard (and your self-scan "
					"application) to be deployed."
				),
				"sort_order": 3,
			},
			{
				"question": "Android 18 or 19?",
				"answer": (
					"The Joya Smart datasheet specifies Android 15 with a path to Android 18. "
					"Do not copy Smart Portal’s Android 19 path onto this device."
				),
				"sort_order": 4,
			},
			{
				"question": "Can we reuse Joya Touch cradles and walls?",
				"answer": (
					"Datalogic lists compatibility with existing cradle positions and wall "
					"brackets to replace JT installations (94ACC0428 / 0429 / 0430). Confirm "
					"pin vs wireless-charge dock for each site."
				),
				"sort_order": 5,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page is published without an Item link. ERP currently has Joya Touch "
					"A6 (RET.SYS.DLG.3658), not Joya Smart. Create the Smart Item and link it "
					"under ERP Item Link; the URL stays /products/datalogic-joya-smart."
				),
				"sort_order": 6,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The official datasheet specifies a 1-year factory warranty. EASEOFCARE "
					"and Datalogic Shield extend hardware cover and Android security updates."
				),
				"sort_order": 7,
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
