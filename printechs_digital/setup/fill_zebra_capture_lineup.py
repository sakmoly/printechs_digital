# Copyright (c) 2026, Printechs and contributors
"""Zebra interactive retail, scanners, RFID, wearables and tablets.

PS30 · DS8100 · DS9308 · DS3600 · RFD40 · RFD90 · FXR90 · WS501 · WS50 RFID · ET6x

Images and YouTube IDs are unique to these pages — do not reuse printer/handheld assets.
"""

import frappe

from printechs_digital.setup.zebra_common import (
	apply_identity,
	catalog_card,
	copy_public_image,
	download_file,
	get_or_create,
	save_product,
	set_related,
	set_specs,
)

VIDEO_PS30 = "https://youtu.be/XsWqwGWeQJ8"  # Official: exceptional shopping experience
VIDEO_PS30_B = "https://youtu.be/z1jZ3u_jw8c"  # Official: discover the future of retail
VIDEO_DS8100 = "https://youtu.be/IKQ0OXKI8Xs"  # Official: DS8100 1-minute overview
VIDEO_DS8100_B = "https://youtu.be/0RzV1Fhl6q4"  # Official: document capture setup
VIDEO_DS9308 = "https://youtu.be/2fOmHoLLueU"  # Official: DS9300 15s overview
VIDEO_DS3600 = "https://youtu.be/OKgTyQ684lE"  # Official: 3600 1-minute overview
VIDEO_RFD40 = "https://youtu.be/Dlg61IPq9Bk"  # All Barcode Systems: RFD40 overview
VIDEO_RFD90 = "https://youtu.be/wD-fQdXNVyM"  # Logiscenter: RFD90 ultra-rugged
VIDEO_FXR90 = "https://youtu.be/4FqE5P06D2k"  # LogiQ-On: FXR90 fixed readers
VIDEO_WS50R = "https://youtu.be/IBKMH1gox2Y"  # Official: WS50 RFID introduction
VIDEO_WS50R_B = "https://youtu.be/V25XPSjkrS8"  # Official: WS50 RFID demo
VIDEO_WS501 = "https://youtu.be/w-iu-_PKtzs"  # POSGuys: WS501
VIDEO_ET6X = "https://youtu.be/JHNVMAD9cVQ"  # PeacockBros: ET60/ET65

IMAGES = {
	"zebra-ps30-front.jpg": (
		["https://cdn11.bigcommerce.com/s-ps5mmp8f7h/images/stencil/1280x1280/products/56058/202162/ps30-front__33391.1739245247.jpg"],
		"ps30-front.jpg",
	),
	"zebra-ds8178.jpg": (
		["https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4363/9073/ds8100-series-ds8178-sr-right-down-black-3x2-3600__17350.1690460119.jpg"],
		"ds8178.jpg",
	),
	"zebra-ds9308.png": ([], "ds9308-y780.png"),
	"zebra-ds3600.jpg": (
		["https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4362/9057/ds3600-series-cradle-right-down-3x2-3600__61054.1748282398.jpg"],
		"ds3600.jpg",
	),
	"zebra-rfd40.jpg": (
		["https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4030/7984/rfid40-photography-product-right-facing-top__07494.1626376048.jpg"],
		"rfd40.jpg",
	),
	"zebra-rfd40-pp.png": (
		["https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4052/8289/RFD40_PP__17624.1788971643.png"],
		"rfd40-pp.png",
	),
	"zebra-rfd90.png": (
		["https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4075/9784/RFD90-01__23925.1728906564.png"],
		"rfd90.png",
	),
	"zebra-fxr90.png": ([], "fxr90-hero.png"),
	"zebra-ws501.jpg": (
		["https://cdn11.bigcommerce.com/s-ps5mmp8f7h/images/stencil/1280x1280/products/57314/208156/WS5012-0F3J1020ENA_image1__32871.1788735762.jpg"],
		"ws501.jpg",
	),
	"zebra-ws50-rfid.jpg": (
		["https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4345/9990/1000x1000_5__66304.1738673713.jpg"],
		"ws50-rfid.jpg",
	),
	"zebra-et6x.png": ([], "et60-hero.png"),
}

RELATED = {
	"zebra-ps30": ["zebra-ds8100-series", "zebra-ds9308", "zebra-tc53e-tc58e"],
	"zebra-ds8100-series": ["zebra-ds9308", "zebra-ps30", "zebra-tc53e-tc58e"],
	"zebra-ds9308": ["zebra-ds8100-series", "zebra-ps30", "zebra-zd421"],
	"zebra-ds3600-series": ["zebra-tc73-tc78", "zebra-mc3400-mc3450", "zebra-rfd90"],
	"zebra-rfd40": ["zebra-rfd90", "zebra-tc53e-tc58e", "zebra-zd621r"],
	"zebra-rfd90": ["zebra-rfd40", "zebra-fxr90", "zebra-tc73-tc78"],
	"zebra-fxr90": ["zebra-rfd90", "zebra-rfd40", "zebra-zt411"],
	"zebra-ws501": ["zebra-ws50-rfid", "zebra-mc3400-mc3450", "zebra-tc73-tc78"],
	"zebra-ws50-rfid": ["zebra-ws501", "zebra-rfd40", "zebra-tc73-tc78"],
	"zebra-et6x": ["zebra-tc73-tc78", "zebra-rfd90", "zebra-mc3400-mc3450"],
}


def _media():
	paths = {}
	for filename, (urls, tmp_name) in IMAGES.items():
		paths[filename] = download_file(filename, urls, tmp_name)
	paths["retail"] = copy_public_image("industry-retail.jpg")
	paths["warehouse"] = copy_public_image("industry-warehouse-logistics.jpg")
	paths["fashion"] = copy_public_image("industry-fashion.jpg")
	paths["packaging"] = copy_public_image("industry-packaging.jpg")
	return paths


def _support(install, device, maintenance, training):
	return [
		{"icon": "install", "title": "Deployment", "description": install, "sort_order": 1},
		{"icon": "device", "title": "Accessories", "description": device, "sort_order": 2},
		{"icon": "maintenance", "title": "Service", "description": maintenance, "sort_order": 3},
		{"icon": "training", "title": "Training", "description": training, "sort_order": 4},
	]


def fill_ps30(media):
	slug = "zebra-ps30"
	card = catalog_card("zebra-ps30-front.jpg", "zebra-ps30-card.jpg")
	front = media["zebra-ps30-front.jpg"]
	doc = get_or_create(slug, "Zebra PS30 Personal Shopper", "", card, "Interactive Retail")
	apply_identity(doc, slug=slug, display_name="Zebra PS30 Personal Shopper", item="", subcategory="Interactive Retail", category_label="INTERACTIVE RETAIL & PERSONAL SHOPPING")
	doc.tagline = "2025 iF Design Award — self-scan, promotions and tap-to-pay, not a wall price checker"
	doc.short_description = (
		"Zebra PS30 is Printechs’ flagship personal-shopping device: 4.7-inch HD, Qualcomm 4490, "
		"Wi-Fi 6E, SE4710 + Digimarc. Scan, see price and promotion, add to basket, checkout — "
		"a Smart Retail loop with Modern POS / ERPNext, not a wall-mounted price checker."
	)
	doc.long_description = (
		"<p>PS30 is Zebra’s current personal-shopping platform (2025 iF Design Award). Official "
		"display is 4.7 in HD 1280 × 720 (540 nits), CPU is Qualcomm QCS4490 at 2.4 GHz, memory "
		"is 6 GB / 64 GB, and the battery is 3500 mAh PowerPrecision+. Scan engine is SE4710 with "
		"hands-free and Digimarc. Wireless is Wi-Fi 6E and Bluetooth 5.3. Weight is 9.95 oz / 282 g "
		"(Plus 10.26 oz / 291 g).</p>"
		"<p><strong>PS30 Base</strong> is WLAN. <strong>PS30 Plus</strong> adds sensors and NFC "
		"tap-to-pay (Apple VAS / Google Smart Tap). This is not a wall price checker. Printechs "
		"positions it as Interactive Retail: customer takes PS30 → scans → sees price/promotion → "
		"adds to basket → checkout on Modern POS / ERPNext.</p>"
		"<p>No PS30 Item is listed yet — quote Base vs Plus, cradle count and cart mount. Do not "
		"treat TC53e or a Magellan as a personal shopper.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra PS30 Personal Shopper, front handle view"
	doc.video_url = VIDEO_PS30
	doc.hero_trust_chips = "2025 iF Design Award\n4.7 in HD · 540 nits\nWi-Fi 6E · SE4710 + Digimarc\nPlus = NFC tap-to-pay"
	doc.story_heading = "Personal shopping, not a wall checker"
	doc.visual_story_heading = "PS30"
	doc.card_title = "PS30 Personal Shopper"
	doc.card_summary = "Award-winning self-scan shopper. Scan, promote, bag and tap-to-pay. Quote Base vs Plus."
	doc.card_image = card
	doc.final_cta_heading = "Specify PS30 for interactive retail"
	doc.final_cta_description = "Confirm Base vs Plus (NFC), cradle count and how it should land on Modern POS."
	doc.meta_title = "Zebra PS30 Personal Shopper | Printechs"
	doc.meta_description = "Zebra PS30 personal shopper: 4.7-inch, Wi-Fi 6E, Digimarc, optional tap-to-pay. Interactive retail with Modern POS from Printechs."
	doc.set("benefits", [
		{"icon": "loyalty", "title": "Not a price checker", "description": "Self-scan, lists, location offers and skip-the-line checkout — 2025 iF Design Award.", "sort_order": 1},
		{"icon": "scan", "title": "SE4710 + Digimarc", "description": "Hands-free scan and Digimarc. Shoppers point; the engine does the rest.", "sort_order": 2},
		{"icon": "checkout", "title": "Smart Retail loop", "description": "Scan → price/promo → basket → Modern POS / ERPNext. Hardware plus software.", "sort_order": 3},
		{"icon": "connectivity", "title": "Wi-Fi 6E / Plus NFC", "description": "Base is WLAN + BT 5.3. Plus adds sensors and NFC tap-to-pay.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "PS30", "image": front, "image_alt": "Zebra PS30 Personal Shopper", "caption": "Handle + 4.7-inch screen. Not TC53e, not a wall kiosk.", "sort_order": 1},
		{"label": "In the aisle", "image": media["retail"], "image_alt": "Retail aisle", "caption": "Price, promotion and basket on the device the shopper carries.", "sort_order": 2},
		{"label": "Fashion / specialty", "image": media["fashion"], "image_alt": "Fashion retail", "caption": "Scan-as-you-shop for grocery, club and specialty retail.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "display", "title": "Display", "description": "4.7 in HD · 540 nits · Gorilla", "sort_order": 1},
		{"icon": "scan", "title": "Scan", "description": "SE4710 · Digimarc · hands-free", "sort_order": 2},
		{"icon": "connectivity", "title": "Wireless", "description": "Wi-Fi 6E · BT 5.3 · Plus NFC", "sort_order": 3},
		{"icon": "battery", "title": "Battery", "description": "3500 mAh PowerPrecision+", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "PS30 Base (WLAN) and PS30 Plus (sensors + NFC tap-to-pay)"),
			("Item on this page", "No PS30 Item yet — quote Base vs Plus and cradle count"),
			("Not this page", "Wall price checker, TC53e, Magellan, PS20"),
		]),
		("Compute, display & capture", [
			("CPU / OS", "Qualcomm QCS4490 octa-core 2.4 GHz. Android (upgradeable to 17)"),
			("Memory / battery", "6 GB / 64 GB. 3500 mAh PowerPrecision+"),
			("Display", "4.7 in HD 1280 × 720, 540 nits, Gorilla Glass, multi-touch"),
			("Scanning", "SE4710 1D/2D, hands-free, Digimarc"),
			("Size / weight", "0.76 × 8.52 × 2.83 in; 9.95 oz / 282 g (Plus 10.26 oz / 291 g)"),
		]),
		("Wireless & environment", [
			("WLAN / BT", "Wi-Fi 6E 2×2 MU-MIMO; Bluetooth 5.3"),
			("NFC / pay", "Plus only: contactless pay, Apple VAS, Google Smart Tap"),
			("Drop / tumble", "4 ft / 1.2 m to concrete; 1000 × 0.5 m tumbles"),
			("Sealing", "PSS casual spill; disinfectant-ready plastics"),
			("Warranty", "Zebra 1-year limited. OneCare available"),
		]),
	])
	doc.set("applications", [
		{"title": "Scan-as-you-shop", "description": "Customer takes PS30, scans, bags and sees the running total.", "image": media["retail"], "image_alt": "Self-scan shopping", "industry_link": "retail", "sort_order": 1},
		{"title": "Price + promotion", "description": "Location offers and loyalty on the same device — not a wall checker.", "image": media["fashion"], "image_alt": "Retail promotion", "industry_link": "retail", "sort_order": 2},
		{"title": "Checkout on Modern POS", "description": "Basket lands on Printechs Modern POS / ERPNext. Tap-to-pay on Plus.", "image": media["retail"], "image_alt": "Retail checkout", "industry_link": "retail", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "PS30 personal shopping", "body": "Official Zebra film. This page is PS30 — Interactive Retail, not a wall-mounted price checker.", "video_url": VIDEO_PS30, "image": front, "image_alt": "Zebra PS30", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Smart Retail with Modern POS", "body": "Scan → basket → checkout. Pair PS30 with Printechs Modern POS / ERPNext so hardware is a solution, not a gadget.", "video_url": VIDEO_PS30_B, "image": media["retail"], "image_alt": "Retail", "link_label": "See Modern POS", "link_href": "/software/modern-pos", "sort_order": 2},
	])
	doc.set("support_items", _support("StageNow, Wi-Fi 6E and first self-scan walk.", "Locking cradles, cart mounts, Plus NFC checkout points.", "3500 mAh packs and OneCare in KSA.", "Shopper start, tap-to-pay (Plus) and associate assist."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "PS30 Base or Plus as quoted", "sort_order": 1}, {"item_description": "3500 mAh battery", "sort_order": 2}, {"item_description": "Quick-start (cradles quoted separately)", "sort_order": 3}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Is this a price checker?", "answer": "No. PS30 is a personal shopper the customer carries. Wall checkers are a different class. This page is Interactive Retail.", "sort_order": 1},
		{"question": "Base or Plus?", "answer": "Base is WLAN self-scan. Plus adds sensors and NFC tap-to-pay. Quote Plus when checkout should finish on the device.", "sort_order": 2},
		{"question": "How does it work with Modern POS?", "answer": "Shopper scans into a basket; Printechs lands that basket on Modern POS / ERPNext for pay, stock and receipt. Ask for the Smart Retail quote.", "sort_order": 3},
	])
	return save_product(doc, card)


def fill_ds8100(media):
	slug = "zebra-ds8100-series"
	card = catalog_card("zebra-ds8178.jpg", "zebra-ds8100-series-card.jpg")
	photo = media["zebra-ds8178.jpg"]
	doc = get_or_create(slug, "Zebra DS8100 Series", "", card, "Barcode Scanners")
	apply_identity(doc, slug=slug, display_name="Zebra DS8100 Series", item="", subcategory="Barcode Scanners", category_label="RETAIL HANDHELD SCANNER")
	doc.tagline = "Premium POS imager — DS8108 corded, DS8178 cordless, 1D/2D/Digimarc"
	doc.short_description = (
		"Zebra DS8100 Series is Printechs’ premium retail handheld: 800 MHz + PRZM, 1D/2D/Digimarc, "
		"up to 24 in / 61 cm. DS8108 is corded. DS8178 is cordless with PowerPrecision+ / PowerCap."
	)
	doc.long_description = (
		"<p>One DS8100 Series page covers both checkout guns. Official scan uses an 800 MHz CPU, "
		"1280 × 960 sensor and PRZM. Range is typically to 24 in / 61 cm. Digimarc is supported. "
		"<strong>DS8108 is corded</strong> (5.4 oz / 154 g, 5-year warranty). "
		"<strong>DS8178 is cordless</strong> (8.3 oz / 235 g, Bluetooth, 2500 mAh PP+ or PowerCap, "
		"3-year warranty on scanner/cradle).</p>"
		"<p>Drop is 6 ft / 1.8 m. IP52. Host: USB, RS232, KBW, IBM 46XX. No DS8108/DS8178 Item is "
		"listed yet — quote corded vs cordless, black vs white, and cradle. This is not DS9308 "
		"(presentation) and not DS3600 (industrial green).</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra DS8178 cordless retail scanner in presentation cradle"
	doc.video_url = VIDEO_DS8100
	doc.hero_trust_chips = "DS8108 corded · DS8178 cordless\n1D / 2D / Digimarc\nTo 24 in / 61 cm\nPRZM · 800 MHz"
	doc.story_heading = "Premium handheld POS"
	doc.visual_story_heading = "DS8100 Series"
	doc.card_title = "DS8100 Series"
	doc.card_summary = "Premium retail handheld. DS8108 corded, DS8178 cordless. 1D/2D/Digimarc."
	doc.card_image = card
	doc.final_cta_heading = "Specify DS8108 or DS8178"
	doc.final_cta_description = "Confirm corded vs cordless, battery vs PowerCap, and USB vs serial."
	doc.meta_title = "Zebra DS8108 / DS8178 Scanner | Printechs"
	doc.meta_description = "Zebra DS8100 Series retail scanners: DS8108 corded and DS8178 cordless. 1D/2D/Digimarc checkout from Printechs."
	doc.set("benefits", [
		{"icon": "checkout", "title": "Checkout first-time", "description": "PRZM + megapixel sensor on faded, wrinkled and phone-screen codes.", "sort_order": 1},
		{"icon": "scan", "title": "1D / 2D / Digimarc", "description": "Printed and electronic barcodes plus Digimarc at the lane.", "sort_order": 2},
		{"icon": "battery", "title": "Corded or cordless", "description": "DS8108 is the cable. DS8178 is Bluetooth with PP+ 2500 mAh or PowerCap.", "sort_order": 3},
		{"icon": "store", "title": "Retail scanners", "description": "Manned POS, SCO and click-and-collect. DS9308 is the counter presentation sibling.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "DS8178", "image": photo, "image_alt": "DS8178 in cradle", "caption": "Cordless DS8178 in the presentation cradle. DS8108 is the same head, corded.", "sort_order": 1},
		{"label": "Lane", "image": media["retail"], "image_alt": "Retail checkout", "caption": "Premium handheld POS — not the industrial green DS3600.", "sort_order": 2},
		{"label": "Fashion / pharmacy", "image": media["fashion"], "image_alt": "Specialty retail", "caption": "Use DS9308 when the job is hands-free on the counter.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "scan", "title": "Decode", "description": "1D / 2D / Digimarc · PRZM", "sort_order": 1},
		{"icon": "device", "title": "Models", "description": "DS8108 corded · DS8178 BT", "sort_order": 2},
		{"icon": "battery", "title": "DS8178 power", "description": "2500 mAh PP+ or PowerCap", "sort_order": 3},
		{"icon": "rugged", "title": "Duty", "description": "6 ft drop · IP52", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "DS8108 corded and DS8178 cordless. One series page"),
			("Item on this page", "No DS8108/DS8178 Item yet — quote cable vs Bluetooth and cradle"),
			("Not this page", "DS8100-HC healthcare, DS9308 presentation, DS3600 industrial"),
		]),
		("Scan & physical", [
			("Decode", "1D, 2D, Digimarc, OCR (family). 1280 × 960, 48° × 37° FOV"),
			("Range", "Typically to 24 in / 61 cm on UPC-class labels"),
			("Size / weight", "6.6 × 2.6 × 4.2 in. DS8108 154 g; DS8178 235 g"),
			("Host", "USB, RS232, keyboard wedge, IBM 46XX over RS485"),
		]),
		("Power & environment", [
			("DS8178 battery", "PP+ 2500 mAh (~65,000 scans) or PowerCap capacitor"),
			("Drop / IP", "6 ft / 1.8 m to concrete; IP52"),
			("Warranty", "DS8108 5-year; DS8178 + cradle 3-year"),
		]),
	])
	doc.set("applications", [
		{"title": "Manned POS", "description": "First-time decode on damaged and phone barcodes.", "image": media["retail"], "image_alt": "POS scan", "industry_link": "retail", "sort_order": 1},
		{"title": "Self-checkout", "description": "Cordless DS8178 at SCO; corded DS8108 on a fixed lane.", "image": media["retail"], "image_alt": "Self checkout", "industry_link": "retail", "sort_order": 2},
		{"title": "Click & collect", "description": "Scan the tote and the receipt at the counter.", "image": media["fashion"], "image_alt": "Collect desk", "industry_link": "retail", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "DS8100 Series overview", "body": "Official 1-minute film. This page is retail DS8108/DS8178 — not DS8100-HC and not DS3600.", "video_url": VIDEO_DS8100, "image": photo, "image_alt": "DS8178", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Document capture", "body": "Official setup film for DS8100 document capture. Pair with DS9308 when the counter should stay hands-free.", "video_url": VIDEO_DS8100_B, "image": media["retail"], "image_alt": "Retail", "link_label": "See DS9308", "link_href": "/products/zebra-ds9308", "sort_order": 2},
	])
	doc.set("support_items", _support("123Scan and first POS/SCO tune.", "Cradles, stands, PowerCap vs PP+.", "Cables, batteries and OneCare in KSA.", "Aim spot, multi-code and Digimarc."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "DS8108 or DS8178 as quoted", "sort_order": 1}, {"item_description": "Interface cable and/or cradle (as quoted)", "sort_order": 2}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "DS8108 or DS8178?", "answer": "DS8108 is corded. DS8178 is Bluetooth cordless. Same decode class. Quote the power style, not two marketing pages.", "sort_order": 1},
		{"question": "Is this healthcare DS8100-HC?", "answer": "No. HC is a different housing and night-mode kit. This page is retail twilight-black / nova-white.", "sort_order": 2},
		{"question": "When do I pick DS9308?", "answer": "When the cashier should present the item to a counter scanner. DS8100 is the handheld.", "sort_order": 3},
	])
	return save_product(doc, card)


def fill_ds9308(media):
	slug = "zebra-ds9308"
	item = "RET.SYS.ZEB.4000"
	card = catalog_card("zebra-ds9308.png", "zebra-ds9308-card.jpg")
	photo = media["zebra-ds9308.png"]
	doc = get_or_create(slug, "Zebra DS9308", item, card, "Barcode Scanners")
	apply_identity(doc, slug=slug, display_name="Zebra DS9308", item=item, subcategory="Barcode Scanners", category_label="PRESENTATION SCANNER")
	doc.tagline = "All-day counter imager — 1D, 2D, Digimarc and OCR in a near-zero footprint"
	doc.short_description = (
		"Zebra DS9308 is the compact presentation scanner for fashion, pharmacy, supermarket and "
		"convenience. This page is the USB black SR kit. Hands-free on the counter; pick up when needed."
	)
	doc.long_description = (
		"<p>DS9308 is the DS9300 Series presentation imager: 5.7 × 3.4 × 3.3 in, 11.2 oz / 318 g, "
		"IP52, 5 ft / 1.5 m drop, 1000 tumbles. Swipe to 120 in/s on 13 mil UPC. 1280 × 800 sensor, "
		"1D/2D, Digimarc and OCR. Amber LED aimer, Hyper Red illumination.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4000</strong> — DS9308-SR, multi-interface, USB kit, "
		"black (DS9308-SR00004ZZWW + USB). Alpine White and DL (driver-licence) are other SKUs. "
		"Not DS8100 (handheld) and not Magellan (bi-optic).</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra DS9308 presentation scanners in black and alpine white"
	doc.video_url = VIDEO_DS9308
	doc.hero_trust_chips = "Presentation + handheld\n1D / 2D / Digimarc / OCR\nIP52 · 5 ft drop\nUSB kit 4000"
	doc.story_heading = "The counter scanner that fits anywhere"
	doc.visual_story_heading = "DS9308"
	doc.card_title = "DS9308"
	doc.card_summary = "Compact counter presentation imager. This SKU is black USB SR kit RET.SYS.ZEB.4000."
	doc.card_image = card
	doc.final_cta_heading = "Specify DS9308 for the counter"
	doc.final_cta_description = "Confirm black vs white, USB vs serial, and SR vs DL parsing."
	doc.meta_title = "Zebra DS9308 Presentation Scanner | Printechs"
	doc.meta_description = "Zebra DS9308 counter scanner: 1D/2D/Digimarc/OCR. USB black kit RET.SYS.ZEB.4000. From Printechs."
	doc.set("benefits", [
		{"icon": "store", "title": "Near-zero footprint", "description": "Fits fashion, pharmacy, C-store and specialty counters.", "sort_order": 1},
		{"icon": "scan", "title": "1D / 2D / Digimarc / OCR", "description": "Swipe to 120 in/s. Documents and IDs on DL configurations.", "sort_order": 2},
		{"icon": "checkout", "title": "All-day presentation", "description": "Hands-free on the stand; lift for awkward items.", "sort_order": 3},
		{"icon": "rugged", "title": "Counter-proof", "description": "IP52, 5 ft drop, 1000 tumbles. Spill-ready plastics.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "DS9308", "image": photo, "image_alt": "DS9308 black and white", "caption": "This kit is black USB SR (4000). White is a colour option.", "sort_order": 1},
		{"label": "Fashion / pharmacy", "image": media["fashion"], "image_alt": "Fashion counter", "caption": "Small footprint for specialty and pharmacy POS.", "sort_order": 2},
		{"label": "Supermarket", "image": media["retail"], "image_alt": "Supermarket", "caption": "Use DS8100 when the cashier should walk the gun.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "scan", "title": "This SKU", "description": "SR · USB · midnight black", "sort_order": 1},
		{"icon": "display", "title": "Size", "description": "5.7 × 3.4 × 3.3 in · 318 g", "sort_order": 2},
		{"icon": "speed", "title": "Swipe", "description": "To 120 in/s on 13 mil UPC", "sort_order": 3},
		{"icon": "rugged", "title": "Duty", "description": "IP52 · 5 ft · 1000 tumbles", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "DS9308 presentation imager (DS9300 Series)"),
			("Item on this page", "RET.SYS.ZEB.4000 — SR, multi-IF, USB kit, black"),
			("Also available", "Alpine White; DL parsing; Checkpoint EAS. Not on 4000"),
		]),
		("Scan & physical", [
			("Decode", "1D, 2D, Digimarc, OCR. 1280 × 800, 52° × 33° FOV"),
			("Aimer / light", "617 nm amber circular LED; 660 nm Hyper Red"),
			("Size / weight", "5.7 × 3.4 × 3.3 in (145 × 86 × 83 mm); 11.2 oz / 318 g"),
			("Host", "USB, RS232, KBW, IBM 46XX. This kit is USB"),
		]),
		("Environment", [
			("Drop / tumble / IP", "5 ft / 1.5 m; 1000 × 0.5 m; IP52"),
			("Temp", "0–50 °C operating"),
			("Warranty", "Zebra limited (see zebra.com/warranty). OneCare available"),
		]),
	])
	doc.set("applications", [
		{"title": "Fashion & specialty", "description": "Small counter, large decode — QR, hang tags, phone wallets.", "image": media["fashion"], "image_alt": "Fashion POS", "industry_link": "retail", "sort_order": 1},
		{"title": "Pharmacy / C-store", "description": "OCR and 2D on packs that never sit still.", "image": media["retail"], "image_alt": "Pharmacy", "industry_link": "retail", "sort_order": 2},
		{"title": "Supermarket lane", "description": "Presentation first; lift for produce and awkward packs.", "image": media["retail"], "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "DS9300 in 15 seconds", "body": "Official Zebra overview. This page is RET.SYS.ZEB.4000 (black USB SR). Handheld POS is DS8100.", "video_url": VIDEO_DS9308, "image": photo, "image_alt": "DS9308", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Counter vs handheld", "body": "Stay on DS9308 for presentation. Step to DS8108/DS8178 when the cashier needs a gun.", "image": media["fashion"], "image_alt": "Retail counter", "link_label": "See DS8100 Series", "link_href": "/products/zebra-ds8100-series", "sort_order": 2},
	])
	doc.set("support_items", _support("123Scan and first POS tune.", "USB already on 4000; stands and EAS quoted extra.", "Windows and cables in KSA.", "Presentation vs trigger and Digimarc."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "DS9308-SR black scanner (4000)", "sort_order": 1}, {"item_description": "USB cable (kit)", "sort_order": 2}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Which DS9308 is this?", "answer": "RET.SYS.ZEB.4000 — SR, USB kit, black. White and DL are other quotes.", "sort_order": 1},
		{"question": "Handheld or presentation?", "answer": "DS9308 sits on the counter. DS8100 is the premium handheld. Magellan is bi-optic grocery.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_ds3600(media):
	slug = "zebra-ds3600-series"
	item = "RET.SYS.ZEB.4949"
	card = catalog_card("zebra-ds3600.jpg", "zebra-ds3600-series-card.jpg")
	photo = media["zebra-ds3600.jpg"]
	doc = get_or_create(slug, "Zebra DS3600 Series", item, card, "Barcode Scanners")
	apply_identity(doc, slug=slug, display_name="Zebra DS3600 Series", item=item, subcategory="Barcode Scanners", category_label="INDUSTRIAL SCANNER")
	doc.tagline = "Ultra-rugged 1D/2D — DS3608 corded, DS3678 cordless, IP65/IP68, 10 ft drop"
	doc.short_description = (
		"Zebra DS3600 is the industrial scanner for receiving, pick, pack, manufacturing, cold "
		"storage and logistics. This page is the DS3678-SR cordless kit. DS3608 is the corded twin."
	)
	doc.long_description = (
		"<p>DS3608 (corded) and DS3678 (cordless) are the ultra-rugged 3600 imagers: industrial "
		"green, dual IP65/IP68, 10 ft / 3.0 m drop at room temp, 7500 tumbles. Cordless drop across "
		"temp is 8 ft / 2.4 m. PRZM 1D/2D. Host USB, RS232, KBW, industrial Ethernet on family.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4949</strong> — DS3678-SR cordless kit (scanner, "
		"shielded USB, STB3678 cradle, PSU). <strong>RET.SYS.ZEB.4950 is DS3678-DP</strong> (direct "
		"part mark) — do not ship 4949 as DPM. DS3608 corded has no Item yet. ER/HP/HD/KD are "
		"other engines. Photo shows the industrial-green family (ER marking may appear on some "
		"cuts); this SKU is SR.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra DS3678 ultra-rugged industrial scanner in charging cradle"
	doc.video_url = VIDEO_DS3600
	doc.hero_trust_chips = "DS3608 corded · DS3678 cordless\nIP65 + IP68 · 10 ft drop\nThis SKU = DS3678-SR\nReceiving → logistics"
	doc.story_heading = "Industrial scanners, not retail black"
	doc.visual_story_heading = "DS3600 Series"
	doc.card_title = "DS3600 Series"
	doc.card_summary = "Ultra-rugged industrial imager. This SKU is DS3678-SR cordless (4949). DPM is 4950."
	doc.card_image = card
	doc.final_cta_heading = "Specify DS3608 or DS3678"
	doc.final_cta_description = "Confirm SR vs DP vs ER, corded vs cordless, and cradle power."
	doc.meta_title = "Zebra DS3608 / DS3678 Industrial Scanner | Printechs"
	doc.meta_description = "Zebra DS3600 ultra-rugged scanners: DS3608 corded, DS3678 cordless. Kit RET.SYS.ZEB.4949. From Printechs."
	doc.set("benefits", [
		{"icon": "rugged", "title": "Ultra-rugged", "description": "IP65/IP68, 10 ft to concrete, freezer-capable with the heated holder.", "sort_order": 1},
		{"icon": "scan", "title": "SR on this kit", "description": "4949 is DS3678-SR. 4950 is DPM. ER/HP/HD/KD are other quotes.", "sort_order": 2},
		{"icon": "inventory", "title": "Warehouse flow", "description": "Receiving → picking → packing → manufacturing → cold storage → logistics.", "sort_order": 3},
		{"icon": "battery", "title": "Corded or BT", "description": "DS3608 is the cable. DS3678 is Bluetooth with PP+ ~3100 mAh.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "DS3678", "image": photo, "image_alt": "DS3678 in cradle", "caption": "Industrial green + cradle. This kit is SR 4949, not retail DS8100.", "sort_order": 1},
		{"label": "Warehouse", "image": media["warehouse"], "image_alt": "Warehouse", "caption": "Dock, pick face and pack — where 10 ft drop matters.", "sort_order": 2},
		{"label": "Pack", "image": media["packaging"], "image_alt": "Packing", "caption": "Pair with ZT411 or ZQ630 when the same cart prints.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "rugged", "title": "Rugged", "description": "IP65/68 · 10 ft · 7500 tumbles", "sort_order": 1},
		{"icon": "scan", "title": "This SKU", "description": "DS3678-SR · cordless kit", "sort_order": 2},
		{"icon": "battery", "title": "Power", "description": "PP+ ~3100 mAh on cordless", "sort_order": 3},
		{"icon": "connectivity", "title": "Host", "description": "USB on 4949 · BT Class 1", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "DS3608 corded and DS3678 cordless. Family includes SR/HP/HD/DP/ER/KD"),
			("Item on this page", "RET.SYS.ZEB.4949 — DS3678-SR cordless USB cradle kit"),
			("Also available", "4950 = DS3678-DP DPM kit. DS3608 corded has no Item yet"),
		]),
		("Scan & physical", [
			("Decode", "1D/2D PRZM. SR on 4949. DPM is 4950. ER is another engine"),
			("Size / weight", "Corded ~7.3 × 3.0 × 5.2 in, ~334 g. Cordless deeper, ~436 g class"),
			("Host", "USB, RS232, KBW. 4949 kit is shielded USB + STB3678 cradle"),
		]),
		("Environment", [
			("Drop", "10 ft / 3.0 m room temp. 8 ft across operating temp (model-specific)"),
			("IP / tumble", "IP65 and IP68. 7500 tumbles class"),
			("Temp", "Corded −30 to 50 °C; cordless −20 to 50 °C"),
			("Warranty", "Scanner/cradle 36 months; battery 12 months"),
		]),
	])
	doc.set("applications", [
		{"title": "Receiving & pick", "description": "Shrink-wrap, damaged labels, dock concrete.", "image": media["warehouse"], "image_alt": "Receiving", "industry_link": "warehouse-logistics", "sort_order": 1},
		{"title": "Pack & ship", "description": "Confirm every carton code before it leaves.", "image": media["packaging"], "image_alt": "Packing", "industry_link": "packaging", "sort_order": 2},
		{"title": "Manufacturing / cold", "description": "DPM is 4950. Heated holder for freezer. Do not mix engines.", "image": media["warehouse"], "image_alt": "Manufacturing", "industry_link": "manufacturing", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "3600 ultra-rugged overview", "body": "Official 1-minute film. This page is RET.SYS.ZEB.4949 (DS3678-SR). DPM is 4950.", "video_url": VIDEO_DS3600, "image": photo, "image_alt": "DS3678", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Industrial vs retail scanners", "body": "DS3600 is warehouse green. DS8100/DS9308 stay in the store. Add RFD90 when the job is RFID.", "image": media["warehouse"], "image_alt": "Warehouse", "link_label": "See RFD90", "link_href": "/products/zebra-rfd90", "sort_order": 2},
	])
	doc.set("support_items", _support("123Scan, cradle pair and first WMS tune.", "STB3678 on 4949; extra cups and freezer holder quoted.", "Batteries, windows and DS3678 OneCare 4964.", "SR vs DP vs ER — do not mix kits."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "DS3678-SR scanner (4949)", "sort_order": 1}, {"item_description": "STB3678 cradle, USB cable, PSU (kit)", "sort_order": 2}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Which DS3678 is this?", "answer": "RET.SYS.ZEB.4949 — SR cordless kit. 4950 is DPM. Do not ship 4949 for DPM marks.", "sort_order": 1},
		{"question": "Where is DS3608?", "answer": "DS3608 is the corded twin. No corded Item is listed yet — ask for a cable quote.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_rfd40(media):
	slug = "zebra-rfd40"
	item = "RET.SYS.ZEB.3791"
	card = catalog_card("zebra-rfd40.jpg", "zebra-rfd40-card.jpg")
	std = media["zebra-rfd40.jpg"]
	plus = media["zebra-rfd40-pp.png"]
	doc = get_or_create(slug, "Zebra RFD40", item, card, "RFID")
	apply_identity(doc, slug=slug, display_name="Zebra RFD40", item=item, subcategory="RFID", category_label="RETAIL RFID SLED")
	doc.tagline = "UHF sled — 1,300+ tags/s, ~6 m, IP54; Premium Plus adds SE4100"
	doc.short_description = (
		"Zebra RFD40 is the retail RFID sled for inventory, cycle count, apparel and item-find. "
		"This page is the stocked UHF sled. Premium / Premium Plus (Wi-Fi 6, SE4100) are family options."
	)
	doc.long_description = (
		"<p>RFD40 reads 1,300+ tags/s with a nominal range ~19.7 ft / ~6 m, 7000 mAh PP+, IP54, "
		"5 ft / 1.5 m drop. Standard / Premium / Premium Plus share the sled body. Premium adds "
		"Wi-Fi 6 + BT 5.3 for OTA. <strong>Premium Plus adds SE4100 1D/2D</strong>.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.3791</strong> — RFD40 UHF, 865–868 MHz, IP54, 1300 "
		"tags/s, 7000 mAh. Do not treat 3791 as Premium Plus (no SE4100 claimed on this Item). "
		"eConnex adaptors (TC21/26, TC53/58) are spare parts, not this SKU. Step to RFD90 for "
		"IP65/67 warehouse range.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra RFD40 UHF RFID sled, top view"
	doc.video_url = VIDEO_RFD40
	doc.hero_trust_chips = "1,300+ tags/s · ~6 m\nIP54 · 7000 mAh\nPremium Plus = SE4100\nRetail inventory"
	doc.story_heading = "Retail RFID in the hand"
	doc.visual_story_heading = "RFD40"
	doc.card_title = "RFD40"
	doc.card_summary = "Retail UHF sled. This SKU is RFD40 UHF 3791. Premium Plus SE4100 is a family option."
	doc.card_image = card
	doc.final_cta_heading = "Specify RFD40 for retail RFID"
	doc.final_cta_description = "Confirm Standard vs Premium vs Premium Plus, region (865–868) and TC5/TC2 adaptor."
	doc.meta_title = "Zebra RFD40 RFID Sled | Printechs"
	doc.meta_description = "Zebra RFD40 UHF RFID sled: 1,300+ tags/s, retail inventory. Item RET.SYS.ZEB.3791. From Printechs."
	doc.set("benefits", [
		{"icon": "inventory", "title": "Retail inventory", "description": "Cycle count, apparel, stock lookup and item-find — 1,300+ tags/s.", "sort_order": 1},
		{"icon": "scan", "title": "Plus is optional", "description": "SE4100 imager is Premium Plus only. 3791 is UHF sled — do not assume a barcode engine.", "sort_order": 2},
		{"icon": "battery", "title": "7000 mAh", "description": "Quick-release PP+ on Standard, Premium and Plus.", "sort_order": 3},
		{"icon": "device", "title": "Sled + host", "description": "eConnex to TC21/26, TC53/58 and others. Host computer is separate.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "RFD40", "image": std, "image_alt": "RFD40 sled", "caption": "Stocked 3791 sled. Pair with TC53e — do not mix RFD90 photos.", "sort_order": 1},
		{"label": "Premium Plus class", "image": plus, "image_alt": "RFD40 Premium Plus", "caption": "Plus adds SE4100. Only quote Plus when the Item says so.", "sort_order": 2},
		{"label": "Apparel count", "image": media["fashion"], "image_alt": "Apparel inventory", "caption": "Walk the rail, count the floor, find the missing unit.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "inventory", "title": "RFID", "description": "1,300+ tags/s · ~6 m", "sort_order": 1},
		{"icon": "battery", "title": "Battery", "description": "7000 mAh PP+ quick-release", "sort_order": 2},
		{"icon": "rugged", "title": "Duty", "description": "IP54 · 5 ft · 500 tumbles", "sort_order": 3},
		{"icon": "connectivity", "title": "On Plus", "description": "Wi-Fi 6 · BT 5.3 · SE4100", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "RFD40 Standard, Premium, Premium Plus. RFD40-M is a longer-range sibling"),
			("Item on this page", "RET.SYS.ZEB.3791 — RFD40 UHF 865–868 MHz, 7000 mAh, IP54"),
			("Not on 3791", "SE4100 imager, Wi-Fi 6 claim, RFD90 IP67, FXR90 fixed"),
		]),
		("RFID & physical", [
			("Air", "EPC Gen2 / Gen2v2. Fastest 1,300+ tags/s. Nominal ~6+ m"),
			("Size / weight", "5.94 × 3.3 × 6.5 in; ~541 g Standard / ~556 g Plus with battery"),
			("Host", "eConnex 8-pin, USB, Bluetooth on Premium/Plus. Host MC sold separately"),
		]),
		("Environment", [
			("Drop / IP", "5 ft / 1.5 m to concrete; IP54"),
			("Temp", "−10 to 50 °C operating"),
			("Warranty", "Zebra 1-year limited on 3791"),
		]),
	])
	doc.set("applications", [
		{"title": "Cycle count", "description": "Walk the department; 1,300+ tags/s vs piece-scan.", "image": media["fashion"], "image_alt": "Apparel count", "industry_link": "retail", "sort_order": 1},
		{"title": "Item find", "description": "Geiger mode for the missing size on the rail.", "image": media["retail"], "image_alt": "Stock lookup", "industry_link": "retail", "sort_order": 2},
		{"title": "Receiving", "description": "Confirm the carton without opening every polybag.", "image": media["warehouse"], "image_alt": "Receiving", "industry_link": "warehouse-logistics", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "RFD40 sled overview", "body": "RFD40 Standard / Premium / Plus. This page is RET.SYS.ZEB.3791 (UHF sled). Plus SE4100 is a different quote.", "video_url": VIDEO_RFD40, "image": std, "image_alt": "RFD40", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "When to step to RFD90", "body": "Stay on RFD40 for store inventory. Choose RFD90 (IP65/67, 6.7–22.9 m class) for warehouse and yard.", "image": plus, "image_alt": "RFD40 Plus", "link_label": "See RFD90", "link_href": "/products/zebra-rfd90", "sort_order": 2},
	])
	doc.set("support_items", _support("eConnex adaptor, 123RFID and first count walk.", "TC21/26 and TC53/58 snap-ons already in ERP (3792/3793).", "7000 mAh packs and OneCare in KSA.", "Trigger modes: RFID / barcode (Plus) / find."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "RFD40 UHF sled (3791)", "sort_order": 1}, {"item_description": "7000 mAh battery", "sort_order": 2}, {"item_description": "Host computer and adaptor quoted separately", "sort_order": 3}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Is 3791 Premium Plus?", "answer": "The Item is RFD40 UHF. It does not name SE4100. Quote Premium Plus only when you need the imager and Wi-Fi 6 sled.", "sort_order": 1},
		{"question": "Does it include a handheld?", "answer": "No. RFD40 is a sled. Pair with TC53e/TC58e or another eConnex host.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_rfd90(media):
	slug = "zebra-rfd90"
	card = catalog_card("zebra-rfd90.png", "zebra-rfd90-card.jpg")
	photo = media["zebra-rfd90.png"]
	doc = get_or_create(slug, "Zebra RFD90", "", card, "RFID")
	apply_identity(doc, slug=slug, display_name="Zebra RFD90", item="", subcategory="RFID", category_label="RUGGED RFID SLED")
	doc.tagline = "Ultra-rugged UHF — RFD9030 ~6.7 m, RFD9090 ~22.9 m, IP65/IP67, 1,300 tags/s"
	doc.short_description = (
		"Zebra RFD90 is the premium industrial RFID handheld sled for WMS: IP65/IP67, 6 ft drop, "
		"1,300 tags/s. RFD9030 is standard range. RFD9090 is long range. No RFD90 Item is listed yet."
	)
	doc.long_description = (
		"<p>RFD90 is the ultra-rugged sled above RFD40. Dual IP65/IP67, 6 ft / 1.8 m to concrete, "
		"7000 mAh, Wi-Fi 6, Bluetooth 5.3, 1,300+ tags/s. Zebra specifies a nominal "
		"<strong>RFD9030 ~22 ft / ~6.7 m</strong> and <strong>RFD9090 ~75 ft / ~22.9 m</strong> "
		"(later sheets also list 12 m / 29 m class — confirm on the quote).</p>"
		"<p>No RFD90 Item is in ERP. Do not ship RFD40 3791 as RFD90. Optional SE4750MR / SE4850 "
		"imagers are family options. Host TC73/TC78 via eConnex. Pair with Printechs WMS for "
		"dock, yard and WIP.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra RFD90 ultra-rugged UHF RFID sled with scan window"
	doc.video_url = VIDEO_RFD90
	doc.hero_trust_chips = "RFD9030 ~6.7 m · RFD9090 ~22.9 m\n1,300+ tags/s\nIP65 + IP67 · 6 ft\nWMS / yard"
	doc.story_heading = "Industrial RFID above RFD40"
	doc.visual_story_heading = "RFD90"
	doc.card_title = "RFD90"
	doc.card_summary = "Ultra-rugged RFID sled. RFD9030 standard range, RFD9090 long range. No Item yet."
	doc.card_image = card
	doc.final_cta_heading = "Specify RFD9030 or RFD9090"
	doc.final_cta_description = "Confirm standard vs long range, imager option and TC73 adaptor."
	doc.meta_title = "Zebra RFD90 RFID Sled | Printechs"
	doc.meta_description = "Zebra RFD90 ultra-rugged RFID: RFD9030 ~6.7 m, RFD9090 ~22.9 m, IP67. WMS RFID from Printechs."
	doc.set("benefits", [
		{"icon": "rugged", "title": "Above RFD40", "description": "IP65/IP67 and 6 ft drop for dock, yard and wash-down — not store IP54.", "sort_order": 1},
		{"icon": "inventory", "title": "Two ranges", "description": "RFD9030 ~6.7 m standard. RFD9090 ~22.9 m long-range yagi class.", "sort_order": 2},
		{"icon": "scan", "title": "1,300 tags/s", "description": "Same class rate as RFD40, built for WMS volume and item-find.", "sort_order": 3},
		{"icon": "connectivity", "title": "Wi-Fi 6 / BT 5.3", "description": "OTA even without a host attached. eConnex to TC73/TC78.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "RFD90", "image": photo, "image_alt": "RFD90 sled", "caption": "Green ultra-rugged sled. Not the black RFD40.", "sort_order": 1},
		{"label": "Warehouse", "image": media["warehouse"], "image_alt": "Warehouse RFID", "caption": "Dock door counts and yard finds for WMS customers.", "sort_order": 2},
		{"label": "Pack / WIP", "image": media["packaging"], "image_alt": "WIP", "caption": "Fixed gates are FXR90. This page is the handheld sled.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "rugged", "title": "Rugged", "description": "IP65/67 · 6 ft · 1000 drops", "sort_order": 1},
		{"icon": "inventory", "title": "9030 / 9090", "description": "~6.7 m or ~22.9 m class", "sort_order": 2},
		{"icon": "battery", "title": "Battery", "description": "7000 mAh PP+ quick-release", "sort_order": 3},
		{"icon": "connectivity", "title": "Wireless", "description": "Wi-Fi 6 · BT 5.3 · NFC pair", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "RFD9030 standard range and RFD9090 long range"),
			("Item on this page", "No RFD90 Item yet — quote 9030 vs 9090 and imager"),
			("Not this page", "RFD40 3791 (IP54 retail), FXR90 fixed, WS50 RFID wearable"),
		]),
		("RFID & physical", [
			("Air", "EPC Gen2v2. 1,300+ tags/s. 9030 ~6.7 m; 9090 ~22.9 m nominal"),
			("Size", "9030 7.4 × 3.2 × 6.8 in; 9090 9.8 × 3.8 × 6.8 in"),
			("Weight class", "714–799 g with battery and optional imager"),
			("Imager", "Optional SE4750MR or SE4850 — not assumed on an unlisted Item"),
		]),
		("Environment", [
			("Drop / IP", "6 ft / 1.8 m to concrete; IP65 and IP67"),
			("Temp", "−20 to 55 °C"),
			("Warranty", "Zebra 1-year limited. OneCare available"),
		]),
	])
	doc.set("applications", [
		{"title": "WMS inventory", "description": "Pallet and location counts that barcode guns cannot finish in time.", "image": media["warehouse"], "image_alt": "WMS", "industry_link": "warehouse-logistics", "sort_order": 1},
		{"title": "Yard / dock", "description": "RFD9090 long range for trailer and cage finds.", "image": media["warehouse"], "image_alt": "Yard", "industry_link": "warehouse-logistics", "sort_order": 2},
		{"title": "WIP", "description": "Handheld RFID on the line; FXR90 for the fixed gate.", "image": media["packaging"], "image_alt": "WIP", "industry_link": "manufacturing", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "RFD90 ultra-rugged sled", "body": "RFD9030 vs RFD9090. No RFD90 Item yet. Do not treat 3791 as this page.", "video_url": VIDEO_RFD90, "image": photo, "image_alt": "RFD90", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Handheld plus WMS", "body": "Pair RFD90 with Printechs WMS. Fixed dock/gate automation is FXR90.", "image": media["warehouse"], "image_alt": "Warehouse", "link_label": "See FXR90", "link_href": "/products/zebra-fxr90", "sort_order": 2},
	])
	doc.set("support_items", _support("eConnex, 123RFID and first WMS count.", "TC73/TC78 cups and holsters quoted with the sled.", "7000 mAh packs in KSA.", "9030 vs 9090 range walk."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "RFD9030 or RFD9090 as quoted", "sort_order": 1}, {"item_description": "7000 mAh battery", "sort_order": 2}, {"item_description": "Host computer quoted separately", "sort_order": 3}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "RFD9030 or RFD9090?", "answer": "9030 is standard range (~6.7 m). 9090 is long range (~22.9 m). Same IP65/67 sled class.", "sort_order": 1},
		{"question": "Is this RFD40?", "answer": "No. RFD40 3791 is IP54 retail. RFD90 is the ultra-rugged WMS sled.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_fxr90(media):
	slug = "zebra-fxr90"
	card = catalog_card("zebra-fxr90.png", "zebra-fxr90-card.jpg")
	photo = media["zebra-fxr90.png"]
	doc = get_or_create(slug, "Zebra FXR90", "", card, "RFID")
	apply_identity(doc, slug=slug, display_name="Zebra FXR90", item="", subcategory="RFID", category_label="FIXED RFID READER")
	doc.tagline = "Ultra-rugged fixed UHF — IP65/IP67, Wi-Fi 6, optional 5G/GPS, integrated antenna"
	doc.short_description = (
		"Zebra FXR90 is the fixed RFID reader for dock doors, receiving/dispatch gates, WIP, "
		"yard and automatic warehouse movement. Not a handheld sled. No FXR90 Item is listed yet."
	)
	doc.long_description = (
		"<p>FXR90 is Zebra’s ultra-rugged fixed reader: die-cast aluminium, IP65/IP67, −40 to 65 °C, "
		"NXP i.MX8 Mini, Linux, 2 GB / 16 GB, 1,300+ tags/s. Integrated-antenna models list up to "
		"~100 ft / 30.5 m (tag/setup dependent). Ports: 4, 8, or integrated antenna + 4. Power is "
		"24 VDC or PoE+.</p>"
		"<p>Wireless options are Wi-Fi 6, Bluetooth 5.3, and optional 5G / GPS / CBRS — factory "
		"configurations, not field cards. No FXR90 Item is in ERP. Do not sell FX9600 photos as "
		"FXR90. Printechs quotes this as a solution: dock door, receiving gate, dispatch gate, "
		"asset track, WIP, yard, automatic warehouse movement.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra FXR90 ultra-rugged fixed RFID readers, integrated and ported models"
	doc.video_url = VIDEO_FXR90
	doc.hero_trust_chips = "IP65 + IP67 · −40 to 65 °C\n1,300+ tags/s\nWi-Fi 6 · optional 5G/GPS\n4 / 8 / integrated antenna"
	doc.story_heading = "Fixed RFID as a Printechs solution"
	doc.visual_story_heading = "FXR90"
	doc.card_title = "FXR90"
	doc.card_summary = "Ultra-rugged fixed RFID reader. Dock door, gate, WIP and yard — not a handheld."
	doc.card_image = card
	doc.final_cta_heading = "Specify FXR90 for the gate"
	doc.final_cta_description = "Confirm 4- vs 8-port vs integrated antenna, Wi-Fi vs 5G, and the door/gate design."
	doc.meta_title = "Zebra FXR90 Fixed RFID Reader | Printechs"
	doc.meta_description = "Zebra FXR90 ultra-rugged fixed RFID: IP67, Wi-Fi 6, optional 5G. Dock door and gate solutions from Printechs."
	doc.set("benefits", [
		{"icon": "rugged", "title": "Outdoor-capable", "description": "IP65/IP67, −40 to 65 °C, salt-fog and solar-rated housing.", "sort_order": 1},
		{"icon": "connectivity", "title": "Wi-Fi 6 / 5G", "description": "Cable-free backhaul where fibre is late. 5G/GPS/CBRS are options.", "sort_order": 2},
		{"icon": "integration", "title": "Solution, not a box", "description": "Dock door, receiving/dispatch gate, WIP, yard, automatic warehouse movement.", "sort_order": 3},
		{"icon": "cloud", "title": "Edge Linux", "description": "IoT Connector, Network Connect, MotionWorks — integrators, not a sled.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "FXR90", "image": photo, "image_alt": "FXR90 readers", "caption": "Integrated-antenna and ported bodies. Not FX9600, not RFD90.", "sort_order": 1},
		{"label": "Dock / yard", "image": media["warehouse"], "image_alt": "Dock door", "caption": "RFID dock door and dispatch gate — design the zone, then pick ports.", "sort_order": 2},
		{"label": "WIP", "image": media["packaging"], "image_alt": "Manufacturing WIP", "caption": "Line-side reads without a handheld in every hand.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "rugged", "title": "Rugged", "description": "IP65/67 · −40 to 65 °C", "sort_order": 1},
		{"icon": "inventory", "title": "RFID", "description": "1,300+ tags/s · to ~30 m*", "sort_order": 2},
		{"icon": "connectivity", "title": "Backhaul", "description": "GbE · PoE+ · Wi-Fi 6 · 5G*", "sort_order": 3},
		{"icon": "device", "title": "Ports", "description": "4 / 8 / integrated + 4", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "FXR90 4-port, 8-port, or integrated antenna + 4 ports"),
			("Item on this page", "No FXR90 Item yet — quote ports, Wi-Fi/5G and the gate design"),
			("Not this page", "FX9600, RFD40/RFD90 sleds, handheld computers"),
		]),
		("RFID & compute", [
			("Engine", "Zebra radio. 1,300+ tags/s. Integrated antenna to ~30.5 m (setup-dependent)"),
			("CPU / OS", "NXP i.MX8 Mini Quad. Linux. 2 GB LPDDR4 / 16 GB eMMC"),
			("Size / weight", "From 11.5 × 10.0 × 2.0 in, ~2.5 kg (no integrated antenna, no brackets)"),
		]),
		("Power, wireless & environment", [
			("Power", "24 VDC or PoE+ (802.3at). PoE af is not sufficient"),
			("Wireless", "Wi-Fi 6 and BT 5.3. 5G/GPS/CBRS on WAN SKUs only"),
			("IP / temp", "IP65 and IP67. −40 to 65 °C. MIL vibration / salt fog"),
			("Connectors", "Industrial M12, RP-TNC antenna ports"),
		]),
	])
	doc.set("applications", [
		{"title": "RFID dock door", "description": "In/out visibility without a handheld at every truck.", "image": media["warehouse"], "image_alt": "Dock", "industry_link": "warehouse-logistics", "sort_order": 1},
		{"title": "Receiving / dispatch gate", "description": "Confirm the ASN or the load as it crosses the portal.", "image": media["warehouse"], "image_alt": "Gate", "industry_link": "warehouse-logistics", "sort_order": 2},
		{"title": "WIP / yard / assets", "description": "Line, vehicle and tool tracking outside the four walls.", "image": media["packaging"], "image_alt": "WIP", "industry_link": "manufacturing", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "FXR90 fixed reader", "body": "Ultra-rugged fixed RFID. This is a gate/door solution quote — not RFD90 in a cradle.", "video_url": VIDEO_FXR90, "image": photo, "image_alt": "FXR90", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Handheld plus fixed", "body": "FXR90 for the portal. RFD90 for the exception walk. WMS ties both together.", "image": media["warehouse"], "image_alt": "Warehouse", "link_label": "See WMS", "link_href": "/software/warehouse-management-system", "sort_order": 2},
	])
	doc.set("support_items", _support("Site survey, antenna plan and first portal test.", "M12 Ethernet, PoE+ injectors, extra antennas.", "OneCare and spare readers in KSA.", "Web UI, IoT Connector and alarm walk."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "FXR90 reader (ports and radio as quoted)", "sort_order": 1}, {"item_description": "Mount brackets as quoted", "sort_order": 2}, {"item_description": "Antennas and PoE+ quoted for the gate design", "sort_order": 3}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Is this a handheld?", "answer": "No. FXR90 is a fixed reader for doors and gates. Handheld RFID is RFD40/RFD90.", "sort_order": 1},
		{"question": "Does every unit include 5G?", "answer": "No. Wi-Fi 6/BT are common. 5G/GPS/CBRS are WAN SKUs — confirm on the quote.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_ws501(media):
	slug = "zebra-ws501"
	card = catalog_card("zebra-ws501.jpg", "zebra-ws501-card.jpg")
	photo = media["zebra-ws501.jpg"]
	doc = get_or_create(slug, "Zebra WS501", "", card, "Wearable Scanners")
	apply_identity(doc, slug=slug, display_name="Zebra WS501", item="", subcategory="Wearable Scanners", category_label="WEARABLE COMPUTER")
	doc.tagline = "All-in-one wearable — Qualcomm 2290, 3/32, Wi-Fi 6, Bluetooth 5.3, SE4770"
	doc.short_description = (
		"Zebra WS501 is the current WS5x all-in-one wearable for warehouse pick: more CPU, 3 GB / "
		"32 GB, Wi-Fi 6 and BT 5.3 versus WS50. Finger, back-of-hand or wrist. No WS501 Item yet."
	)
	doc.long_description = (
		"<p>WS501 is the new all-in-one wearable (not WS50, not WS50 RFID). Official step-up vs "
		"WS50: Qualcomm QC2290 vs SDW4100, 3 GB / 32 GB vs 1/8, Wi-Fi 6 2×2 vs Wi-Fi 5 1×1, "
		"Bluetooth 5.3. 2 in AMOLED 460 × 460. Scan SKU uses SE4770 and ~1300 mAh. Finger, "
		"back-of-hand or wrist mounts.</p>"
		"<p>No WS501 Item is listed. Do not treat this page as WS50 RFID (that is the UHF wearable). "
		"WS501-R (RFID) is a newer RFID wearable — mention only as a follow-on quote. Demo with "
		"WMS: wear it, pick the line, update the location hands-free.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra WS501 finger-mount wearable computer with SE4770 imager"
	doc.video_url = VIDEO_WS501
	doc.hero_trust_chips = "3 GB / 32 GB · QC2290\nWi-Fi 6 · BT 5.3\nSE4770 · 2 in AMOLED\nFinger / BoH / wrist"
	doc.story_heading = "Hands-free pick without a sled"
	doc.visual_story_heading = "WS501"
	doc.card_title = "WS501"
	doc.card_summary = "Next-gen all-in-one wearable. Wi-Fi 6, 3/32, SE4770. Not WS50 RFID."
	doc.card_image = card
	doc.final_cta_heading = "Specify WS501 for wearable pick"
	doc.final_cta_description = "Confirm finger vs back-of-hand vs wrist and whether you need WS50 RFID instead."
	doc.meta_title = "Zebra WS501 Wearable Computer | Printechs"
	doc.meta_description = "Zebra WS501 wearable: Wi-Fi 6, 3 GB/32 GB, SE4770. Hands-free warehouse pick from Printechs."
	doc.set("benefits", [
		{"icon": "android", "title": "Above WS50", "description": "QC2290, triple RAM, quadruple flash, Wi-Fi 6 and BT 5.3.", "sort_order": 1},
		{"icon": "scan", "title": "SE4770 on-device", "description": "No separate ring scanner or host handheld for barcode pick.", "sort_order": 2},
		{"icon": "inventory", "title": "Pick demo", "description": "Wear it, scan the slot, WMS updates — both hands on the carton.", "sort_order": 3},
		{"icon": "battery", "title": "Hot-swap class", "description": "Scan SKU ~1300 mAh. RFID battery class is a different model.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "WS501", "image": photo, "image_alt": "WS501 finger mount", "caption": "Finger-mount barcode wearable. Not the BoH RFID strap on WS50 RFID.", "sort_order": 1},
		{"label": "Pick", "image": media["warehouse"], "image_alt": "Warehouse pick", "caption": "Two free hands on the case. Keypad cousins stay on MC3400.", "sort_order": 2},
		{"label": "Pack", "image": media["packaging"], "image_alt": "Pack", "caption": "Need RFID verify on the wrist? That is WS50 RFID.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "android", "title": "Compute", "description": "QC2290 · 3 GB / 32 GB", "sort_order": 1},
		{"icon": "connectivity", "title": "Wireless", "description": "Wi-Fi 6 2×2 · BT 5.3", "sort_order": 2},
		{"icon": "scan", "title": "Scan", "description": "SE4770 · 2 in AMOLED", "sort_order": 3},
		{"icon": "battery", "title": "Power", "description": "~1300 mAh scan SKU", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "WS501 all-in-one wearable (barcode). Not WS50, not WS50 RFID"),
			("Item on this page", "No WS501 Item yet — quote mount and whether RFID is required"),
			("Not this page", "WS50 RFID (~1.5 m UHF), WS501-R, RS6100 ring + host"),
		]),
		("Compute & capture", [
			("CPU / memory", "Qualcomm QC2290. 3 GB RAM / 32 GB flash. Android AOSP class"),
			("Display", "2 in AMOLED 460 × 460, Gorilla, glove touch"),
			("Scanning", "SE4770 1D/2D on scan SKUs"),
			("Mounts", "Two-finger, back-of-hand, wrist"),
		]),
		("Wireless & environment", [
			("WLAN / BT", "Wi-Fi 6 2×2 MU-MIMO; Bluetooth 5.3; NFC tap-to-pair"),
			("Battery", "High-capacity ~1300 mAh on scan SKU; hot-swap class"),
			("Sealing", "IP65 class wearable"),
			("Warranty", "Zebra 1-year limited"),
		]),
	])
	doc.set("applications", [
		{"title": "Picking", "description": "Hands-free line walk — both hands on the carton.", "image": media["warehouse"], "image_alt": "Picking", "industry_link": "warehouse-logistics", "sort_order": 1},
		{"title": "Put-away", "description": "Scan the licence plate without holstering a brick.", "image": media["warehouse"], "image_alt": "Put-away", "industry_link": "warehouse-logistics", "sort_order": 2},
		{"title": "Load / unload", "description": "Confirm the pallet at the door with a glanceable 2-inch screen.", "image": media["packaging"], "image_alt": "Loading", "industry_link": "warehouse-logistics", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "WS501 wearable", "body": "Current WS5x all-in-one. This page is barcode WS501 — not WS50 RFID.", "video_url": VIDEO_WS501, "image": photo, "image_alt": "WS501", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "When you need RFID on the wrist", "body": "WS50 RFID (and WS501-R) add UHF ~1.5 m. Use that page when pick must verify the tag.", "image": media["warehouse"], "image_alt": "Warehouse", "link_label": "See WS50 RFID", "link_href": "/products/zebra-ws50-rfid", "sort_order": 2},
	])
	doc.set("support_items", _support("Mount fit, StageNow and first pick walk.", "Cradles and spare 1300 mAh packs.", "OneCare in KSA.", "Soft keys, auto-trigger and WMS."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "WS501 wearable (mount as quoted)", "sort_order": 1}, {"item_description": "Battery (scan SKU typical)", "sort_order": 2}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "WS501 or WS50 RFID?", "answer": "WS501 is the new barcode wearable (Wi-Fi 6, 3/32). WS50 RFID adds UHF ~1.5 m and is a different page.", "sort_order": 1},
		{"question": "Does it need a TC73?", "answer": "No. WS501 is host-free. TC73 is the handheld when the job is a 6-inch screen.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_ws50_rfid(media):
	slug = "zebra-ws50-rfid"
	card = catalog_card("zebra-ws50-rfid.jpg", "zebra-ws50-rfid-card.jpg")
	photo = media["zebra-ws50-rfid.jpg"]
	doc = get_or_create(slug, "Zebra WS50 RFID", "", card, "Wearable Scanners")
	apply_identity(doc, slug=slug, display_name="Zebra WS50 RFID", item="", subcategory="Wearable Scanners", category_label="WEARABLE RFID")
	doc.tagline = "Android + barcode + UHF RFID wearable — no host handheld, RFID to ~1.5 m"
	doc.short_description = (
		"Zebra WS50 RFID combines Android, SE4770 and UHF RFID in a wearable — no separate sled "
		"or host. Zebra specifies RFID to about 1.5 m. Wear, pick, RFID-verify, WMS updates."
	)
	doc.long_description = (
		"<p>WS50 RFID is the host-free wearable with UHF: 2 in AMOLED, Snapdragon Wear 4100, "
		"1 GB / 8 GB, SE4770, Wi-Fi 5, IP65. RFID engine reads to <strong>~5 ft / ~1.5 m</strong> "
		"(EPC Gen2). Finger or back-of-hand mounts. RFID battery class ~2400 mAh on those SKUs.</p>"
		"<p>No WS50 RFID Item is listed. Do not mix WS501 (barcode, Wi-Fi 6, 3/32) onto this page. "
		"WS501-R is the next-gen RFID wearable — quote it when you want WS501 compute plus RFID. "
		"WMS demo: worker wears WS50 RFID → scans/picks carton → RFID verifies item → location "
		"updates.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra WS50 RFID back-of-hand wearable with UHF antenna"
	doc.video_url = VIDEO_WS50R
	doc.hero_trust_chips = "Android + scan + UHF\nRFID ~1.5 m\nSE4770 · no host handheld\nFinger or back-of-hand"
	doc.story_heading = "RFID on the wrist, not on a sled"
	doc.visual_story_heading = "WS50 RFID"
	doc.card_title = "WS50 RFID"
	doc.card_summary = "Host-free wearable RFID. Scan + UHF ~1.5 m. Not WS501 barcode-only."
	doc.card_image = card
	doc.final_cta_heading = "Specify WS50 RFID for wearable RFID"
	doc.final_cta_description = "Confirm finger vs back-of-hand and whether WS501-R (next-gen) is the better quote."
	doc.meta_title = "Zebra WS50 RFID Wearable | Printechs"
	doc.meta_description = "Zebra WS50 RFID wearable: Android, SE4770 and UHF to ~1.5 m. WMS pick-and-verify from Printechs."
	doc.set("benefits", [
		{"icon": "inventory", "title": "No host handheld", "description": "Computer + imager + UHF in one wearable. No RFD40 on the belt.", "sort_order": 1},
		{"icon": "scan", "title": "Barcode + RFID", "description": "SE4770 for the label; UHF to ~1.5 m for the tag on the same pick.", "sort_order": 2},
		{"icon": "integration", "title": "WMS demo", "description": "Wear → pick carton → RFID verify → WMS location update.", "sort_order": 3},
		{"icon": "android", "title": "WS50 class", "description": "1/8 and Wi-Fi 5. WS501 is the barcode upgrade; WS501-R is the RFID upgrade path.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "WS50 RFID", "image": photo, "image_alt": "WS50 RFID wearable", "caption": "Back-of-hand RFID mount. Not the finger-only WS501 barcode unit.", "sort_order": 1},
		{"label": "Pick + verify", "image": media["warehouse"], "image_alt": "Warehouse pick", "caption": "Scan the slot, RFID-confirm the each, both hands free.", "sort_order": 2},
		{"label": "Longer RFID", "image": media["warehouse"], "image_alt": "Inventory", "caption": "Need 6–22 m? That is RFD90, not a wearable.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "inventory", "title": "RFID", "description": "UHF · ~1.5 m · Gen2", "sort_order": 1},
		{"icon": "scan", "title": "Barcode", "description": "SE4770 1D/2D", "sort_order": 2},
		{"icon": "display", "title": "Display", "description": "2 in AMOLED 460 × 460", "sort_order": 3},
		{"icon": "battery", "title": "RFID SKU", "description": "~2400 mAh class", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "WS50 RFID host-free wearable (Android + SE4770 + UHF)"),
			("Item on this page", "No WS50 RFID Item yet — quote mount and region"),
			("Not this page", "WS501 barcode-only, RFD40 sled, WS501-R next-gen RFID"),
		]),
		("Compute, scan & RFID", [
			("CPU / memory", "Snapdragon Wear 4100 / SDW429w. 1 GB / 8 GB. Android 11 AOSP class"),
			("RFID", "EPC Gen2 / Gen2v2. Nominal ~5 ft / ~1.5 m. 0–24 dBm class"),
			("Scanning", "SE4770 1D/2D"),
			("Display", "2 in AMOLED 460 × 460, Gorilla, glove"),
		]),
		("Wireless & environment", [
			("WLAN", "Wi-Fi 5 1×1 SISO (not WS501 Wi-Fi 6)"),
			("Battery", "~2400 mAh on RFID SKUs; hot-swap class"),
			("Sealing", "IP65"),
			("Warranty", "Zebra 1-year limited"),
		]),
	])
	doc.set("applications", [
		{"title": "Pick and verify", "description": "Barcode the slot, RFID the each — fewer mis-picks.", "image": media["warehouse"], "image_alt": "Pick verify", "industry_link": "warehouse-logistics", "sort_order": 1},
		{"title": "Item finding", "description": "Short-range RFID on the wrist for the missing each.", "image": media["warehouse"], "image_alt": "Find", "industry_link": "warehouse-logistics", "sort_order": 2},
		{"title": "Retail back-of-house", "description": "Markdown and task work without a brick on the hip.", "image": media["retail"], "image_alt": "Back of store", "industry_link": "retail", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "WS50 RFID introduction", "body": "Official Zebra film. Host-free UHF wearable. This is not WS501 barcode-only.", "video_url": VIDEO_WS50R, "image": photo, "image_alt": "WS50 RFID", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "WMS pick-and-verify", "body": "Official demo. Worker wears WS50 RFID → picks → RFID verifies → WMS updates.", "video_url": VIDEO_WS50R_B, "image": media["warehouse"], "image_alt": "Warehouse", "link_label": "See WMS", "link_href": "/software/warehouse-management-system", "sort_order": 2},
	])
	doc.set("support_items", _support("Mount, 123RFID and first verify walk.", "Dual-slot wrist cradles and 2400 mAh packs.", "OneCare in KSA.", "RFID vs barcode trigger and WMS."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "WS50 RFID wearable (mount as quoted)", "sort_order": 1}, {"item_description": "RFID-class battery", "sort_order": 2}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Is this WS501?", "answer": "No. WS501 is the newer barcode wearable (Wi-Fi 6, 3/32). This page is WS50 RFID (UHF ~1.5 m).", "sort_order": 1},
		{"question": "Why not RFD40?", "answer": "RFD40 is a sled on a handheld. WS50 RFID is host-free on the hand — better for both-hands pick.", "sort_order": 2},
	])
	return save_product(doc, card)


def fill_et6x(media):
	slug = "zebra-et6x"
	item = "RET.SYS.ZEB.4951"
	card = catalog_card("zebra-et6x.png", "zebra-et6x-card.jpg")
	photo = media["zebra-et6x.png"]
	doc = get_or_create(slug, "Zebra ET6x Series", item, card, "Enterprise Tablets")
	apply_identity(doc, slug=slug, display_name="Zebra ET6x Series", item=item, subcategory="Enterprise Tablets", category_label="ENTERPRISE TABLET")
	doc.tagline = "Rugged 10.1-inch — Wi-Fi 6E, Qualcomm 6490, ET60 WLAN / ET65 5G, optional SE55"
	doc.short_description = (
		"Zebra ET6x is the enterprise tablet for supervisors, maintenance, delivery, manufacturing, "
		"vehicle mount and field service. This page is the ET60 10.1-inch 8/128 SE55 kit."
	)
	doc.long_description = (
		"<p>ET60 (WLAN) and ET65 (5G) share a 10.1 in WUXGA 1920 × 1200, 1000-nit display, "
		"Qualcomm 6490 at 2.7 GHz, 8 GB / 128 GB, Wi-Fi 6E, optional SE55 IntelliFocus. Size "
		"10.8 × 7.8 × 0.7 in; ~1108 g with standard battery. Vehicle dock turns it into a forklift "
		"computer. 3-year warranty class.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4951</strong> — ET60, standard 10.1, 8/128, Android "
		"GMS, standard battery, SE55, ROW. ET65 5G has no Item. ET40/ET45 (3996, 4016, 4101, 4504) "
		"are a different, lighter tablet family — do not mix onto this page. Accessories 4953–4962 "
		"are already in ERP.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ET60 10.1-inch rugged enterprise tablet"
	doc.video_url = VIDEO_ET6X
	doc.hero_trust_chips = "10.1 in · 1000 nits\nWi-Fi 6E · ET65 = 5G\n8/128 · SE55 on 4951\nVehicle-dock ready"
	doc.story_heading = "One tablet, many workflows"
	doc.visual_story_heading = "ET6x"
	doc.card_title = "ET6x Series"
	doc.card_summary = "Rugged 10.1-inch enterprise tablet. This SKU is ET60 8/128 SE55 (4951). ET65 is 5G."
	doc.card_image = card
	doc.final_cta_heading = "Specify ET60 or ET65"
	doc.final_cta_description = "Confirm WLAN vs 5G, SE55 vs no scanner, and vehicle dock / kickstand."
	doc.meta_title = "Zebra ET60 / ET65 Enterprise Tablet | Printechs"
	doc.meta_description = "Zebra ET6x rugged tablets: 10.1-inch, Wi-Fi 6E, optional 5G and SE55. Item RET.SYS.ZEB.4951. From Printechs."
	doc.set("benefits", [
		{"icon": "display", "title": "1000-nit 10.1", "description": "WUXGA you can read on the dock, in the yard and in the van.", "sort_order": 1},
		{"icon": "android", "title": "6490 class", "description": "Same compute family as TC73. 8/128 on 4951. Android GMS.", "sort_order": 2},
		{"icon": "scan", "title": "SE55 on this kit", "description": "4951 includes SE55 IntelliFocus. Other ET60 SKUs ship without a scanner.", "sort_order": 3},
		{"icon": "device", "title": "Dock it", "description": "Vehicle/forklift dock, kickstand, hand strap — supervisor to field service.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "ET60", "image": photo, "image_alt": "ET60 tablet", "caption": "10.1-inch ET6x. Not ET40/ET45 and not a TC73.", "sort_order": 1},
		{"label": "Warehouse floor", "image": media["warehouse"], "image_alt": "Supervisor", "caption": "Supervisors, maintenance and dock clerks on a real tablet.", "sort_order": 2},
		{"label": "Field / delivery", "image": media["packaging"], "image_alt": "Field service", "caption": "ET65 adds 5G when the van leaves the yard Wi-Fi.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "display", "title": "Display", "description": "10.1 in WUXGA · 1000 nits", "sort_order": 1},
		{"icon": "connectivity", "title": "On 4951", "description": "Wi-Fi 6E · BT · USB-C/A", "sort_order": 2},
		{"icon": "scan", "title": "Scanner", "description": "SE55 IntelliFocus on 4951", "sort_order": 3},
		{"icon": "battery", "title": "Battery", "description": "Standard pack · 9.3 Ah option", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Models", "ET60 (WLAN) and ET65 (5G). Windows SKUs exist — this page is Android"),
			("Item on this page", "RET.SYS.ZEB.4951 — ET60 10.1, 8/128, Android, std battery, SE55, ROW"),
			("Not this page", "ET40/ET45 (3996/4016/4101/4504), ET65 5G (no Item), Windows ET6x"),
		]),
		("Compute, display & capture", [
			("CPU / memory", "Qualcomm 6490 octa-core 2.7 GHz. 8 GB / 128 GB UFS. microSD to 2 TB"),
			("Display", "10.1 in WUXGA 1920 × 1200, 1000 nits, Gorilla, glove/wet/stylus"),
			("Cameras", "16 MP rear, 8 MP front with privacy shade"),
			("Scanning", "SE55 on 4951. Other kits omit the engine"),
			("Size / weight", "10.8 × 7.8 × 0.7 in; 2.44 lb / 1108 g standard battery"),
		]),
		("Wireless, power & environment", [
			("WLAN", "Wi-Fi 6E 2×2 MU-MIMO. ET65 adds 5G — not on 4951"),
			("I/O", "2× USB-A 3.1, 1× USB-C 3.1 with DisplayPort"),
			("Temp", "Std battery −20 to 55 °C; extended pack to −30 °C"),
			("Warranty", "3-year limited class. ET6XXX OneCare 4963 in ERP"),
		]),
	])
	doc.set("applications", [
		{"title": "Warehouse supervisor", "description": "WMS dashboard on 1000 nits, then dock it on the tugger.", "image": media["warehouse"], "image_alt": "Supervisor", "industry_link": "warehouse-logistics", "sort_order": 1},
		{"title": "Maintenance / manufacturing", "description": "Work orders, manuals and SE55 on the line.", "image": media["packaging"], "image_alt": "Maintenance", "industry_link": "manufacturing", "sort_order": 2},
		{"title": "Delivery / field", "description": "ET65 5G for the route. Vehicle dock for the cab.", "image": media["warehouse"], "image_alt": "Field", "industry_link": "warehouse-logistics", "sort_order": 3},
	])
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "ET60 / ET65 enterprise tablets", "body": "ET6x series film. This page is RET.SYS.ZEB.4951 (ET60 WLAN, SE55). ET65 is 5G. ET40 is a different family.", "video_url": VIDEO_ET6X, "image": photo, "image_alt": "ET60", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Tablet vs handheld", "body": "ET6x when the job is a document and a dock. TC73 when the job is one-hand scan. RFD90 when it is RFID.", "image": media["warehouse"], "image_alt": "Warehouse", "link_label": "See TC73 / TC78", "link_href": "/products/zebra-tc73-tc78", "sort_order": 2},
	])
	doc.set("support_items", _support("StageNow, WLAN/5G and first dock fit.", "Kickstand 4962, 9.3 Ah 4953, screen 4955 already in ERP.", "ET6XXX OneCare 4963 in KSA.", "SE55 aim, privacy shade and vehicle dock."))
	doc.set("downloads", [])
	doc.set("package_contents", [{"item_description": "ET60 tablet (4951 — 8/128, SE55, Android)", "sort_order": 1}, {"item_description": "Standard battery", "sort_order": 2}, {"item_description": "Dock and kickstand quoted separately", "sort_order": 3}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Which ET60 is this?", "answer": "RET.SYS.ZEB.4951 — 10.1-inch, 8/128, Android, standard battery, SE55. ET65 5G has no Item yet.", "sort_order": 1},
		{"question": "Is this ET40?", "answer": "No. ET40/ET45 are a lighter family already in ERP. This page is ET6x only.", "sort_order": 2},
	])
	return save_product(doc, card)


def wire_related():
	for slug, related in RELATED.items():
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		set_related(doc, related)
		doc.flags.ignore_permissions = True
		doc.save()
	frappe.db.commit()
	print("Wired capture-lineup related products")


def fill_zebra_capture_lineup():
	media = _media()
	fill_ps30(media)
	fill_ds8100(media)
	fill_ds9308(media)
	fill_ds3600(media)
	fill_rfd40(media)
	fill_rfd90(media)
	fill_fxr90(media)
	fill_ws501(media)
	fill_ws50_rfid(media)
	fill_et6x(media)
	wire_related()
	return "ok"
