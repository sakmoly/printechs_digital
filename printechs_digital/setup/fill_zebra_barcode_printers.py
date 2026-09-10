# Copyright (c) 2026, Printechs and contributors
"""Create and fill the Printechs Zebra barcode-printer lineup.

ZD421 (entry) → ZD621 (flagship desktop) → ZD621R (RFID desktop)
→ ZT411 (industrial) → ZT610/ZT620 (premium industrial)

ZT421 already exists and stays the 6-inch ZT400 page.
Images and YouTube IDs are unique per page — do not reuse ZT421 assets here.

Official:
https://www.zebra.com/us/en/products/printers/desktop/zd421.html
https://www.zebra.com/us/en/products/printers/desktop/zd621.html
https://www.zebra.com/us/en/products/printers/desktop/zd621r.html
https://www.zebra.com/us/en/products/printers/industrial/zt400-series/zt411.html
https://www.zebra.com/us/en/products/printers/industrial/zt600-series.html
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
	wipe_reseller_badge,
)

# Unique videos — each ID is used on one page only.
VIDEO_ZD421_LOAD = "https://youtu.be/eUw4jhHZaeg"
VIDEO_ZD621_WIFI = "https://youtu.be/QGrMF2xSsuE"
VIDEO_ZD621R = "https://youtu.be/BRnWeQHH96U"
VIDEO_ZT411_OOB = "https://youtu.be/h-YhWqI2zUY"
VIDEO_ZT411_RFID = "https://youtu.be/8toFG166e38"
VIDEO_ZT600_OPTIONS = "https://youtu.be/sfx5VA17xm4"
# ZT421 keeps rAOxqJ6o6gc + 2hd-wDxfwuA (see update_zt421_related).

IMAGES = {
	"zebra-zd421-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4301/10457/1000x1000_13__25960.1780396360.jpg",
		],
		"zd421-a.jpg",
	),
	"zebra-zd621-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4255/10536/cq5dam.web.1280.1280_43__47472.1782819574.jpg",
		],
		"maybe-zd621.jpg",
	),
	"zebra-zd621r-product.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4038/10147/Product_-_Zebra_printers_ZD621R_01__52030.1788787353.png",
		],
		"zd621r.png",
	),
	"zebra-zd621r-open.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4038/9592/cq5dam.web.1280.1280_24__58323.1788787353.jpg",
		],
		"zd621r-cq.jpg",
	),
	"zebra-zd621r-retail.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4038/8015/zd621r-photography-application-retail-clothing-close-up__58242.1788787353.png",
		],
		"zd621r-retail.png",
	),
	"zebra-zt411-front.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4379/10677/zt411-front-photography-website-3x2-3600x2400__67720.1787662604.jpg",
		],
		"zt411-front.jpg",
	),
	"zebra-zt610-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4302/8770/ZT6101__26009.1768479939.jpg",
		],
		"zt610-b.jpg",
	),
	"zebra-zt620-product.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/3519/10162/Product_-_Zebra_printers_Zebra_ZT620__01138.1749127618.png",
		],
		"zt620.png",
	),
	"zebra-zt620-angle.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4312/8824/zt620-angled-left_1__17595.1686750975.png",
		],
		"zt620-angle.png",
	),
}

LINEUP_RELATED = {
	"zebra-zd421": ["zebra-zd621", "zebra-zd621r", "zebra-zt411"],
	"zebra-zd621": ["zebra-zd421", "zebra-zd621r", "zebra-zt411"],
	"zebra-zd621r": ["zebra-zd621", "zebra-zq630-rfid-plus", "zebra-zt411"],
	"zebra-zt411": ["zebra-zd621", "zebra-zt421", "zebra-zt610-zt620"],
	"zebra-zt421": ["zebra-zt411", "zebra-zt610-zt620", "zebra-zd621"],
	"zebra-zt610-zt620": ["zebra-zt411", "zebra-zt421", "zebra-zd621r"],
}


def _media():
	paths = {}
	for filename, (urls, tmp_name) in IMAGES.items():
		paths[filename] = download_file(filename, urls, tmp_name)
	for badged in (
		"zebra-zd421-product.jpg",
		"zebra-zd621r-product.png",
		"zebra-zt620-product.png",
	):
		wipe_reseller_badge(badged)
	paths["warehouse"] = copy_public_image("industry-warehouse-logistics.jpg")
	paths["retail"] = copy_public_image("industry-retail.jpg")
	paths["packaging"] = copy_public_image("industry-packaging.jpg")
	paths["fashion"] = copy_public_image("industry-fashion.jpg")
	paths["pharma"] = copy_public_image("industry-pharmaceutical.jpg")
	return paths


def fill_zd421(media):
	slug = "zebra-zd421"
	item = "RET.SYS.ZEB.3985"
	card = catalog_card("zebra-zd421-product.jpg", "zebra-zd421-card.jpg")
	photo = media["zebra-zd421-product.jpg"]
	doc = get_or_create(slug, "Zebra ZD421", item, card, "Desktop Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZD421",
		item=item,
		subcategory="Desktop Label Printers",
		category_label="DESKTOP LABEL PRINTER",
	)
	doc.tagline = "Entry 4-inch desktop — 203 dpi, 6 ips, Ethernet"
	doc.short_description = (
		"Zebra ZD421 thermal-transfer desktop printer. This kit is 203 dpi with USB, USB Host, "
		"Bluetooth LE and Ethernet. Direct thermal and 300 dpi are other ZD421 configurations."
	)
	doc.long_description = (
		"<p>ZD421 is Printechs’ entry Zebra desktop for shipping, shelf and workbench labels. "
		"OpenACCESS loading, Link-OS and Print Touch keep a 4-inch station simple. Official "
		"speed is 6 ips at 203 dpi or 4 ips at 300 dpi. Print width is 4.09 in / 104 mm at 203 dpi.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.3985</strong> — ZD421t, 203 dpi, RTC, USB, USB Host, "
		"BLE and Ethernet. RET.SYS.ZEB.4114 is the same 203 dpi printer without Ethernet. "
		"RET.SYS.ZEB.4947 is the 300 dpi Ethernet kit. Wi-Fi 6 / Bluetooth 5.3 is a field module, "
		"not on 3985.</p>"
		"<p>The 3-button interface is not the ZD621 colour touch. Step up to ZD621 when you want "
		"8 ips, serial and a 4.3-inch screen, or ZD621R for RFID encode.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZD421 4-inch desktop label printer with three-button interface"
	doc.video_url = VIDEO_ZD421_LOAD
	doc.hero_trust_chips = "203 dpi on this SKU\n6 ips · 4.09 in width\nUSB · BLE · Ethernet\nLink-OS · OpenACCESS"
	doc.story_heading = "The 4-inch desktop that starts the Zebra line"
	doc.visual_story_heading = "ZD421 desktop"
	doc.card_title = "ZD421"
	doc.card_summary = (
		"Entry Zebra desktop: 203 dpi, 6 ips, USB, BLE and Ethernet. Step up to ZD621 for "
		"colour touch and 8 ips."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZD421 for the workbench"
	doc.final_cta_description = (
		"Printechs will confirm 203 vs 300 dpi, Ethernet vs BLE-only, and whether you need "
		"the optional Wi-Fi module."
	)
	doc.meta_title = "Zebra ZD421 Desktop Label Printer | Printechs"
	doc.meta_description = (
		"Zebra ZD421 4-inch desktop, 203 dpi, 6 ips, USB, BLE and Ethernet. Entry Zebra "
		"printer from Printechs in Saudi Arabia."
	)
	doc.set(
		"benefits",
		[
			{"icon": "print", "title": "4-inch desktop TT", "description": "203 dpi and 6 ips on this SKU. 300 dpi / 4 ips is RET.SYS.ZEB.4947.", "sort_order": 1},
			{"icon": "install", "title": "OpenACCESS loading", "description": "Yellow latch, 5-inch OD rolls and a fan-fold slot for simple media changes.", "sort_order": 2},
			{"icon": "connectivity", "title": "Ethernet on this kit", "description": "USB, USB Host, BLE and 10/100 Ethernet. Wi-Fi 6 is an optional card.", "sort_order": 3},
			{"icon": "integration", "title": "ZPL and EPL", "description": "ZPL II, EPL2, PDF Direct and Link-OS. Move formats from older GX desktops.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZD421", "image": photo, "image_alt": "Zebra ZD421 three-button desktop printer", "caption": "3-button ZD421t — not the ZD621 colour-touch chassis.", "sort_order": 1},
			{"label": "Warehouse bench", "image": media["warehouse"], "image_alt": "Warehouse shipping station", "caption": "Shipping and tote labels at a pack bench.", "sort_order": 2},
			{"label": "Retail", "image": media["retail"], "image_alt": "Retail counter labelling", "caption": "Shelf, price and back-office labels.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 6 ips · 4.09 in", "sort_order": 1},
			{"icon": "display", "title": "Interface", "description": "3-button · Print Touch · RTC", "sort_order": 2},
			{"icon": "connectivity", "title": "On 3985", "description": "USB · Host · BLE · Ethernet", "sort_order": 3},
			{"icon": "integration", "title": "Languages", "description": "ZPL II · EPL2 · PDF Direct", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZD421t thermal transfer (not ZD421d, not ZD621, not ZD411)"),
					("Item on this page", "RET.SYS.ZEB.3985 — 203 dpi, RTC, USB, USB Host, BLE, Ethernet"),
					("Also available", "4114 = 203 dpi without Ethernet. 4947 = 300 dpi with Ethernet + BTLE5"),
					("Not on this item", "Colour touch (ZD621), RFID (ZD621R), Wi-Fi 6 module"),
				],
			),
			(
				"Printing",
				[
					("Method", "Thermal transfer on this SKU; direct-thermal ZD421d is a different model"),
					("Resolution", "203 dpi / 8 dots/mm. 300 dpi is RET.SYS.ZEB.4947"),
					("Print speed", "Up to 6 ips / 152 mm/s at 203 dpi; 4 ips / 102 mm/s at 300 dpi"),
					("Print width", "4.09 in / 104 mm at 203 dpi (4.27 in / 108 mm at 300 dpi)"),
					("Print length", "Up to 39 in / 991 mm"),
					("Memory", "256 MB SDRAM, 512 MB Flash"),
				],
			),
			(
				"Media, I/O & environment",
				[
					("Media", "0.585–4.41 in TT; 5 in OD roll; 0.5 / 1.0 / 1.5 / 3 in cores"),
					("Ribbon", "TT ribbon roll (cartridge ZD421c is a different model)"),
					("I/O on 3985", "USB 2.0, USB Host, Bluetooth LE, 10/100 Ethernet"),
					("Optional I/O", "Wi-Fi 5 + BT 4.1 or Wi-Fi 6 + BT 5.3 dual-radio card"),
					("Size / weight", "10.5 × 8.0 × 7.44 in (267 × 202 × 189 mm); about 4.52 lb / 2.05 kg"),
					("Power / warranty", "ENERGY STAR. Zebra standard 2-year limited warranty"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Shipping bench", "description": "4-inch shippers and tote labels at the pack station.", "image": media["warehouse"], "image_alt": "Warehouse packing bench", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Retail back office", "description": "Price, shelf and return labels without an industrial chassis.", "image": media["retail"], "image_alt": "Retail labelling", "industry_link": "retail", "sort_order": 2},
			{"title": "Light packaging", "description": "Short-run carton IDs where 6 ips is enough.", "image": media["packaging"], "image_alt": "Packaging labels", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Load media on a Zebra desktop",
				"body": (
					"Official Zebra film covers ZD421 (and other desktops) media load and "
					"gap calibration. This page is the 203 dpi Ethernet ZD421t — not ZD621."
				),
				"video_url": VIDEO_ZD421_LOAD,
				"image": photo,
				"image_alt": "Zebra ZD421 desktop printer",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "When to step up from ZD421",
				"body": (
					"Stay on ZD421 for 6 ips and a 3-button interface. Choose ZD621 for "
					"8 ips, serial and a 4.3-inch colour touch. Choose ZD621R to print and "
					"encode RAIN RFID. Industrial volume belongs on ZT411."
				),
				"image": media["warehouse"],
				"image_alt": "Warehouse labelling station",
				"link_label": "See ZD621",
				"link_href": "/products/zebra-zd621",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Driver, Ethernet or USB, first format and calibration.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels & ribbons", "description": "4-inch TT media and ribbons matched to ZD421t.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Printheads, platens and OneCare in Saudi Arabia.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "OpenACCESS load, 3-button status and everyday calibration.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZD421t printer (203 dpi, Ethernet kit)", "sort_order": 1},
			{"item_description": "Power supply and cord", "sort_order": 2},
			{"item_description": "USB cable (desktop kits typically include USB)", "sort_order": 3},
			{"item_description": "Quick-start documentation", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which ZD421 is this?", "answer": "RET.SYS.ZEB.3985 — 203 dpi TT with USB, USB Host, BLE and Ethernet. 4114 drops Ethernet. 4947 is 300 dpi.", "sort_order": 1},
			{"question": "Does it include Wi-Fi or a colour screen?", "answer": "No. Wi-Fi 6 is an optional module. Colour touch is ZD621 / ZD621R.", "sort_order": 2},
			{"question": "How fast and how wide?", "answer": "6 ips at 203 dpi, 4.09-inch print width. 300 dpi kits print at 4 ips.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zd621(media):
	slug = "zebra-zd621"
	item = "RET.SYS.ZEB.4948"
	card = catalog_card("zebra-zd621-product.jpg", "zebra-zd621-card.jpg")
	photo = media["zebra-zd621-product.jpg"]
	doc = get_or_create(slug, "Zebra ZD621", item, card, "Desktop Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZD621",
		item=item,
		subcategory="Desktop Label Printers",
		category_label="DESKTOP LABEL PRINTER",
	)
	doc.tagline = "Flagship 4-inch desktop — colour touch, 8 ips, 203/300 dpi"
	doc.short_description = (
		"Zebra ZD621 is Printechs’ flagship Zebra desktop: colour touch LCD, 8 ips at 203 dpi, "
		"USB, USB Host, Ethernet, serial and BTLE5. Optional Wi-Fi 6 / Bluetooth 5.3. RFID is ZD621R."
	)
	doc.long_description = (
		"<p>ZD621 is the premium 4-inch desktop — faster and smarter than ZD421. Official "
		"speed is 8 ips at 203 dpi or 6 ips at 300 dpi. A media dancer, 4.3-inch colour touch "
		"(on this kit) and full wired I/O cover mid-volume shipping and compliance work.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4948</strong> — TT, colour touch LCD, 203 dpi, "
		"USB, USB Host, Ethernet, serial and BTLE5. RET.SYS.ZEB.4040 is 300 dpi with peeler. "
		"Wi-Fi 6 + Bluetooth 5.3 is the optional dual-radio card (official ZD621 option), not "
		"bundled on 4948. Factory RFID encode is the ZD621R page, not this SKU.</p>"
		"<p>Link-OS and Zebra DNA match the industrial printers. Step down to ZD421 for a "
		"3-button 6 ips station, or up to ZT411 when the line needs 14 ips metal.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZD621 premium desktop printer with colour touch display"
	doc.video_url = VIDEO_ZD621_WIFI
	doc.hero_trust_chips = "Colour touch LCD\n8 ips at 203 dpi\nUSB · serial · Ethernet · BTLE5\nOptional Wi-Fi 6"
	doc.story_heading = "The Zebra desktop we specify first"
	doc.visual_story_heading = "ZD621 flagship desktop"
	doc.card_title = "ZD621"
	doc.card_summary = (
		"Flagship Zebra desktop: colour touch, 8 ips, 203 dpi on this kit, full wired I/O. "
		"Optional Wi-Fi 6. RFID is ZD621R."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZD621 as your desktop standard"
	doc.final_cta_description = (
		"Printechs will confirm 203 vs 300 dpi, peeler, and whether to add Wi-Fi 6 / BT 5.3."
	)
	doc.meta_title = "Zebra ZD621 Desktop Label Printer | Printechs"
	doc.meta_description = (
		"Zebra ZD621 flagship desktop: colour touch, 8 ips, 203 dpi, Ethernet and serial. "
		"Optional Wi-Fi 6. From Printechs in Saudi Arabia."
	)
	doc.set(
		"benefits",
		[
			{"icon": "display", "title": "Colour touch LCD", "description": "4.3-inch icon menu on this SKU — not the ZD421 three-button panel.", "sort_order": 1},
			{"icon": "speed", "title": "8 ips at 203 dpi", "description": "Faster than ZD421’s 6 ips. 300 dpi kits (4040) run at 6 ips with a peeler.", "sort_order": 2},
			{"icon": "connectivity", "title": "Full wired I/O", "description": "USB, USB Host, Ethernet, serial and BTLE5. Wi-Fi 6 / BT 5.3 is optional.", "sort_order": 3},
			{"icon": "print", "title": "Media dancer", "description": "Industrial-style dancer for consistent 4-inch print quality at speed.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZD621", "image": photo, "image_alt": "Zebra ZD621 with colour touchscreen", "caption": "Colour-touch ZD621 — not ZD421 and not ZD621R.", "sort_order": 1},
			{"label": "Packaging", "image": media["packaging"], "image_alt": "Packaging line labels", "caption": "Mid-volume case and shipper labels.", "sort_order": 2},
			{"label": "Warehouse", "image": media["warehouse"], "image_alt": "Warehouse desktop printing", "caption": "Dock-office 4-inch printing before you need ZT411.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 8 ips · 4.09 in", "sort_order": 1},
			{"icon": "display", "title": "HMI", "description": "Colour touch LCD · RTC", "sort_order": 2},
			{"icon": "connectivity", "title": "On 4948", "description": "USB · serial · Ethernet · BTLE5", "sort_order": 3},
			{"icon": "speed", "title": "Optional", "description": "Wi-Fi 6 + BT 5.3 card", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZD621t premium desktop (not ZD421, not ZD621R RFID)"),
					("Item on this page", "RET.SYS.ZEB.4948 — colour touch, 203 dpi, USB, Host, Ethernet, serial, BTLE5"),
					("Also available", "RET.SYS.ZEB.4040 — 300 dpi ZD621t with peeler"),
					("RFID", "Factory RFID encode is ZD621R (RET.SYS.ZEB.4042), not this item"),
					("Wireless", "Wi-Fi 6 + Bluetooth 5.3 or Wi-Fi 5 + BT 4.1 — optional dual-radio card"),
				],
			),
			(
				"Printing",
				[
					("Method", "Thermal transfer on this SKU; direct-thermal ZD621d is a different model"),
					("Resolution", "203 dpi on 4948. 300 dpi is 4040"),
					("Print speed", "Up to 8 ips / 203 mm/s at 203 dpi; 6 ips / 152 mm/s at 300 dpi"),
					("Print width", "4.09 in / 104 mm at 203 dpi"),
					("Print length", "Up to 39 in / 991 mm"),
					("Memory", "256 MB SDRAM, 512 MB Flash"),
				],
			),
			(
				"Control, I/O & body",
				[
					("Display", "Colour touch LCD with icon menu (this SKU)"),
					("I/O on 4948", "USB 2.0, USB Host, 10/100 Ethernet, RS-232, BTLE5"),
					("Media", "5 in OD; dancer; OpenACCESS; fan-fold slot"),
					("Size / weight", "10.5 × 8.0 × 7.5 in (267 × 202 × 192 mm); about 5.5 lb / 2.5 kg"),
					("Power / warranty", "ENERGY STAR. Zebra standard 2-year limited warranty"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Shipping office", "description": "4-inch shippers at 8 ips with a colour-touch operator panel.", "image": media["warehouse"], "image_alt": "Warehouse shipping labels", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Retail DC", "description": "Compliance and store labels with Ethernet and serial to the WMS.", "image": media["retail"], "image_alt": "Retail distribution labels", "industry_link": "retail", "sort_order": 2},
			{"title": "Packaging", "description": "Short-to-mid carton runs before an industrial ZT411 is justified.", "image": media["packaging"], "image_alt": "Packaging labels", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Add Wi-Fi 6 or Bluetooth to ZD621",
				"body": (
					"Official Zebra film: install the dual-radio card and join Wi-Fi from the "
					"ZD621 colour-touch menu or Setup Utilities. 4948 ships wired — the card "
					"is optional. The same module family also fits ZD421; we show it here "
					"because ZD621 is the flagship desktop."
				),
				"video_url": VIDEO_ZD621_WIFI,
				"image": photo,
				"image_alt": "Zebra ZD621 colour-touch desktop",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "ZD421 vs ZD621 vs ZD621R",
				"body": (
					"ZD421 is 6 ips and three buttons. ZD621 is 8 ips, colour touch and "
					"serial. ZD621R adds RAIN RFID encode. Need 14 ips or 600 dpi? That is "
					"ZT411, not a desktop."
				),
				"image": media["packaging"],
				"image_alt": "Packaging labels",
				"link_label": "See ZD621R RFID",
				"link_href": "/products/zebra-zd621r",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Ethernet/serial, colour-touch menus and first formats.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels & ribbons", "description": "4-inch TT media; peeler kit if you order 4040.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Printheads, dancer parts and OneCare in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Touch menus, optional Wi-Fi card and calibration.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZD621t printer with colour touch LCD (203 dpi kit)", "sort_order": 1},
			{"item_description": "Power supply and cord (Euro/UK as supplied)", "sort_order": 2},
			{"item_description": "Quick-start documentation", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Why is ZD621 the flagship desktop?", "answer": "Colour touch, 8 ips, serial plus Ethernet, and a media dancer. ZD421 is the 6 ips entry unit. RFID is ZD621R.", "sort_order": 1},
			{"question": "Does 4948 include Wi-Fi 6?", "answer": "No. Wi-Fi 6 / Bluetooth 5.3 is the optional dual-radio card shown in Zebra’s setup film.", "sort_order": 2},
			{"question": "What about 300 dpi or a peeler?", "answer": "Order RET.SYS.ZEB.4040 for 300 dpi with peeler. Do not assume those on 4948.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zd621r(media):
	slug = "zebra-zd621r"
	item = "RET.SYS.ZEB.4042"
	card = catalog_card("zebra-zd621r-product.png", "zebra-zd621r-card.jpg")
	photo = media["zebra-zd621r-product.png"]
	opened = media["zebra-zd621r-open.jpg"]
	retail = media["zebra-zd621r-retail.png"]
	doc = get_or_create(slug, "Zebra ZD621R", item, card, "Desktop Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZD621R",
		item=item,
		subcategory="Desktop Label Printers",
		category_label="RFID DESKTOP PRINTER",
	)
	doc.tagline = "Premium desktop that prints and encodes RAIN RFID"
	doc.short_description = (
		"Zebra ZD621R is the RFID ZD621: 4.3-inch colour touch, 203 dpi on this kit, USB, "
		"USB Host, RS-232, BLE and Ethernet, plus factory UHF RFID encode."
	)
	doc.long_description = (
		"<p>ZD621R is the desktop RFID printer in the Printechs Zebra line. It is a ZD621 "
		"with a factory RE40 UHF encoder — RAIN RFID, EPC Gen 2 V2.1 / ISO/IEC 18000-63. "
		"Adaptive Encoding handles tags down to 0.6 in / 16 mm pitch. Official speed matches "
		"ZD621: 8 ips at 203 dpi, 6 ips at 300 dpi.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4042</strong> — 203 dpi, colour display, RTC, "
		"RFID, USB, USB Host, RS-232, BLE and Ethernet, grey. It is not the non-RFID ZD621 "
		"(4948) and not an industrial RFID ZT411 (4566). Wi-Fi remains optional.</p>"
		"<p>Use it for apparel, asset and returnable-transport tags at a packing table. "
		"Industrial RFID volume belongs on ZT411 RFID or ZT600.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZD621R RFID desktop printer with colour touch display"
	doc.video_url = VIDEO_ZD621R
	doc.hero_trust_chips = "RAIN RFID encode\n4.3-inch colour touch\n203 dpi on this SKU\nUSB · serial · Ethernet"
	doc.story_heading = "Print the label. Encode the tag."
	doc.visual_story_heading = "ZD621R RFID desktop"
	doc.card_title = "ZD621R"
	doc.card_summary = (
		"ZD621 with factory UHF RFID encode. Colour touch, 203 dpi, Ethernet and serial. "
		"For apparel, assets and RTI tags."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZD621R for desktop RFID"
	doc.final_cta_description = (
		"Printechs will match inlays, pitch and whether you need industrial RFID on ZT411 instead."
	)
	doc.meta_title = "Zebra ZD621R RFID Desktop Printer | Printechs"
	doc.meta_description = (
		"Zebra ZD621R RAIN RFID desktop: colour touch, 203 dpi, encode tags from 0.6 inch. "
		"From Printechs in Saudi Arabia."
	)
	doc.set(
		"benefits",
		[
			{"icon": "scan", "title": "Factory RFID encode", "description": "RE40 UHF module, RAIN / EPC Gen 2 / ISO 18000-63. Adaptive Encoding from 16 mm pitch.", "sort_order": 1},
			{"icon": "display", "title": "4.3-inch colour touch", "description": "Same premium HMI as ZD621, with RFID status and calibration on the screen.", "sort_order": 2},
			{"icon": "print", "title": "ZD621 print quality", "description": "8 ips at 203 dpi, media dancer, 4.09-inch width — plus encode in one pass.", "sort_order": 3},
			{"icon": "connectivity", "title": "Wired I/O on 4042", "description": "USB, USB Host, RS-232, BLE and Ethernet. Wi-Fi 6 is still an option.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZD621R", "image": photo, "image_alt": "Zebra ZD621R RFID desktop printer", "caption": "Colour-touch ZD621R — factory RFID, not a field kit on ZD621.", "sort_order": 1},
			{"label": "OpenACCESS + RFID path", "image": opened, "image_alt": "ZD621R open showing colour touch and media path", "caption": "Antenna sits between the platen and the media sensor.", "sort_order": 2},
			{"label": "Apparel tagging", "image": retail, "image_alt": "ZD621R on a retail packing table with garments", "caption": "Official Zebra retail/apparel application still.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "scan", "title": "RFID", "description": "UHF RAIN · EPC Gen 2 · 16 mm pitch", "sort_order": 1},
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 8 ips · 4.09 in", "sort_order": 2},
			{"icon": "display", "title": "HMI", "description": "4.3-inch colour touch", "sort_order": 3},
			{"icon": "connectivity", "title": "On 4042", "description": "USB · RS-232 · BLE · Ethernet", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZD621R RFID desktop (not ZD621, not ZD611R, not ZT411 RFID)"),
					("Item on this page", "RET.SYS.ZEB.4042 — 203 dpi, colour display, RTC, RFID, USB, Host, RS-232, BLE, Ethernet"),
					("Non-RFID sibling", "ZD621 RET.SYS.ZEB.4948 — same desktop class without encode"),
				],
			),
			(
				"RFID & printing",
				[
					("RFID", "UHF RAIN, EPC Gen 2 V2.1, ISO/IEC 18000-63; Adaptive Encoding"),
					("Tag pitch", "Minimum 0.6 in / 16 mm (Zebra official)"),
					("Resolution", "203 dpi on 4042. 300 dpi is a ZD621R family option, not this item"),
					("Print speed", "8 ips at 203 dpi; 6 ips at 300 dpi (family)"),
					("Print width", "4.09 in / 104 mm at 203 dpi"),
				],
			),
			(
				"I/O & body",
				[
					("I/O on 4042", "USB 2.0, USB Host, RS-232, BLE, 10/100 Ethernet"),
					("Size / weight", "10.5 × 8.0 × 7.5 in (267 × 202 × 192 mm); about 5.5 lb / 2.5 kg"),
					("Warranty", "Zebra standard 2-year limited warranty"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Apparel and retail tags", "description": "Print and encode hang tags and item labels at the packing table.", "image": retail, "image_alt": "ZD621R with folded garments", "industry_link": "fashion", "sort_order": 1},
			{"title": "Asset labels", "description": "Desktop RFID for IT, tools and returnable assets.", "image": media["retail"], "image_alt": "Retail asset labelling", "industry_link": "retail", "sort_order": 2},
			{"title": "Pharma / healthcare packs", "description": "Small RFID labels where a desktop encoder is enough.", "image": media["pharma"], "image_alt": "Healthcare packaging", "industry_link": "pharmaceutical", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "ZD621R RFID overview",
				"body": (
					"Distributor film (RFID4U) of the ZD621 RFID desktop — not a Zebra HQ "
					"clip and not reused on ZD621. We still qualify inlays and pitch on site."
				),
				"video_url": VIDEO_ZD621R,
				"image": photo,
				"image_alt": "Zebra ZD621R",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Desktop RFID vs industrial RFID",
				"body": (
					"ZD621R is the packing-table encoder. Field-install RFID on ZT411 "
					"(RET.SYS.ZEB.4566) or a ZT600 RFID kit is for line-side volume. Do not "
					"order 4042 if you need 4- or 6-inch industrial RFID."
				),
				"image": opened,
				"image_alt": "ZD621R colour touch and media path",
				"link_label": "See ZT411",
				"link_href": "/products/zebra-zt411",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "RFID setup", "description": "Inlay pitch, RFID calibrate and first encode test.", "sort_order": 1},
			{"icon": "consumables", "title": "RFID media", "description": "RAIN inlays and 4-inch TT ribbons qualified on ZD621R.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Printhead, encoder path and OneCare in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Touch RFID menus, Adaptive Encoding and void handling.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZD621R RFID printer (203 dpi, colour display)", "sort_order": 1},
			{"item_description": "Power supply and cord", "sort_order": 2},
			{"item_description": "Quick-start documentation", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Is this the same as ZD621?", "answer": "Same desktop family, factory RFID encode. Non-RFID ZD621 is RET.SYS.ZEB.4948.", "sort_order": 1},
			{"question": "What RFID standard?", "answer": "UHF RAIN, EPC Gen 2 V2.1 and ISO/IEC 18000-63. Minimum tag pitch 0.6 inch.", "sort_order": 2},
			{"question": "When do I need ZT411 RFID instead?", "answer": "When you need 4-inch industrial duty, 14 ips or line-side RFID. That item is RET.SYS.ZEB.4566.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zt411(media):
	slug = "zebra-zt411"
	item = "RET.SYS.ZEB.3717"
	card = catalog_card("zebra-zt411-front.jpg", "zebra-zt411-card.jpg")
	photo = media["zebra-zt411-front.jpg"]
	doc = get_or_create(slug, "Zebra ZT411", item, card, "Industrial Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZT411",
		item=item,
		subcategory="Industrial Label Printers",
		category_label="INDUSTRIAL LABEL PRINTER",
	)
	doc.tagline = "4-inch industrial — 14 ips, 203/300/600 dpi, optional RFID"
	doc.short_description = (
		"Zebra ZT411 is the 4-inch industrial printer we put on the website first: 14 ips, "
		"203 dpi on this kit, colour touch, USB, serial, Ethernet and Bluetooth 4.1. 300 dpi, "
		"600 dpi and RFID are other ZT411 items."
	)
	doc.long_description = (
		"<p>ZT411 is the 4-inch ZT400 industrial printer — shipping, inventory, manufacturing "
		"and asset labels in a metal chassis. Official speed is 14 ips (faster than 6-inch "
		"ZT421). Resolution on the family is 203, 300 or 600 dpi. Print width is 4.09 in / 104 mm.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.3717</strong> — 4-inch, 203 dpi, Euro/UK cord, "
		"serial, USB, Ethernet, BT 4.1/MFi, USB Host, EZPL. RET.SYS.ZEB.4624 is 300 dpi. "
		"RET.SYS.ZEB.4566 is 203 dpi with RFID UHF. RET.SYS.ZEB.4228 is peel with full rewind. "
		"600 dpi is a ZT411 family option (no 600 dpi ZT411 item in this catalog today).</p>"
		"<p>6-inch ZT400 work stays on ZT421. 24/7 premium metal and micro-labels are ZT610 / "
		"ZT620. Desktop work stays on ZD621.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZT411 4-inch industrial label printer with colour touch display"
	doc.video_url = VIDEO_ZT411_OOB
	doc.hero_trust_chips = "14 ips · 4.09 in\n203 dpi on this SKU\n300 / 600 dpi family\nOptional RFID UHF"
	doc.story_heading = "The industrial 4-inch we specify first"
	doc.visual_story_heading = "ZT411 industrial"
	doc.card_title = "ZT411"
	doc.card_summary = (
		"4-inch industrial ZT400: 14 ips, 203 dpi on this kit, colour touch. 300 dpi, 600 dpi "
		"and RFID are separate items."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZT411 for the line"
	doc.final_cta_description = (
		"Printechs will confirm 203/300/600 dpi, peel/rewind and whether you need RFID UHF (4566)."
	)
	doc.meta_title = "Zebra ZT411 Industrial Label Printer | Printechs"
	doc.meta_description = (
		"Zebra ZT411 4-inch industrial printer, 14 ips, 203 dpi, colour touch. Optional 300/600 "
		"dpi and RFID. From Printechs in Saudi Arabia."
	)
	doc.set(
		"benefits",
		[
			{"icon": "speed", "title": "14 ips industrial", "description": "Faster than ZT421’s 12 ips. Built for shipping, WIP and asset labels.", "sort_order": 1},
			{"icon": "print", "title": "203, 300 or 600 dpi", "description": "This SKU is 203 dpi. 300 dpi is 4624. 600 dpi is a ZT411-only family option.", "sort_order": 2},
			{"icon": "scan", "title": "RFID when you need it", "description": "Field or factory UHF (4566). Official install film is on this page only.", "sort_order": 3},
			{"icon": "display", "title": "Colour touch ZT400", "description": "4.3-inch HMI, Link-OS, USB, serial, Ethernet and Bluetooth 4.1/MFi.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZT411", "image": photo, "image_alt": "Zebra ZT411 industrial printer front", "caption": "4-inch ZT400 — not the 6-inch ZT421 and not ZT610.", "sort_order": 1},
			{"label": "Shipping", "image": media["warehouse"], "image_alt": "Warehouse shipping labels", "caption": "4-inch shippers and inventory labels at 14 ips.", "sort_order": 2},
			{"label": "Manufacturing", "image": media["packaging"], "image_alt": "Production identification labels", "caption": "WIP and asset labels on the line.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 4.09 in · 14 ips", "sort_order": 1},
			{"icon": "display", "title": "HMI", "description": "Colour touch · Link-OS", "sort_order": 2},
			{"icon": "connectivity", "title": "On 3717", "description": "USB · serial · Ethernet · BT 4.1", "sort_order": 3},
			{"icon": "scan", "title": "RFID", "description": "Optional — item 4566", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZT411 4-inch ZT400 (not ZT421 6-inch, not ZT610)"),
					("Item on this page", "RET.SYS.ZEB.3717 — 203 dpi, Euro/UK, serial, USB, Ethernet, BT 4.1/MFi, USB Host"),
					("Also available", "4624 = 300 dpi. 4566 = 203 dpi RFID UHF. 4228 = peel + full rewind"),
					("600 dpi", "ZT411 family option (Zebra official). No 600 dpi ZT411 item in this catalog yet"),
				],
			),
			(
				"Printing",
				[
					("Method", "Thermal transfer and direct thermal"),
					("Resolution", "203 dpi on 3717; 300 dpi on 4624; 600 dpi family option"),
					("Print speed", "Up to 14 ips / 356 mm/s"),
					("Print width", "4.09 in / 104 mm"),
					("Memory", "256 MB SDRAM, 512 MB Flash"),
				],
			),
			(
				"I/O & body",
				[
					("I/O on 3717", "USB 2.0, USB Host, RS-232, 10/100 Ethernet, Bluetooth 4.1 / MFi"),
					("Optional I/O", "Wi-Fi 5/6 dual radio, applicator card, parallel"),
					("Size / weight", "19.5 × 10.6 × 12.75 in (495 × 269 × 324 mm); 36 lb / 16.33 kg"),
					("Power", "100–240 VAC, 50–60 Hz, ENERGY STAR"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Shipping labels", "description": "4-inch shippers and cartons at 14 ips.", "image": media["warehouse"], "image_alt": "Warehouse shipping", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Inventory and assets", "description": "Bin, tote and asset labels. Add RFID (4566) when tags must encode.", "image": media["retail"], "image_alt": "Inventory labels", "industry_link": "retail", "sort_order": 2},
			{"title": "Manufacturing", "description": "WIP and compliance marks on the line.", "image": media["packaging"], "image_alt": "Production labels", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "ZT411 out of box and basic setup",
				"body": (
					"Official Zebra ZT411 unbox and first media load. This film is the ZT411 "
					"page only — it is not reused on ZT421."
				),
				"video_url": VIDEO_ZT411_OOB,
				"image": photo,
				"image_alt": "Zebra ZT411",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Optional RFID on ZT411",
				"body": (
					"Official Zebra install for the ZT411/ZT421 RFID option. Order "
					"RET.SYS.ZEB.4566 if you need UHF encode on this chassis. 3717 on this "
					"page does not include the RFID kit."
				),
				"video_url": VIDEO_ZT411_RFID,
				"image": media["warehouse"],
				"image_alt": "Industrial labelling",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "ZT411 vs ZT421 vs ZT610",
				"body": (
					"ZT411 is 4-inch / 14 ips / optional 600 dpi. ZT421 is 6-inch / 12 ips. "
					"ZT610/ZT620 is the heavier 24/7 Xi-class platform with Gigabit Ethernet."
				),
				"image": media["packaging"],
				"image_alt": "Production labelling",
				"link_label": "See ZT610 / ZT620",
				"link_href": "/products/zebra-zt610-zt620",
				"sort_order": 3,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Stand, Ethernet, first formats and sensor calibration.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels & ribbons", "description": "4-inch industrial media and 450 m coated-side-out ribbon.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "203/300/600 printheads, platens and OneCare.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Colour-touch menus, RFID option and everyday load.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZT411 industrial printer (203 dpi kit)", "sort_order": 1},
			{"item_description": "Euro and UK power cord", "sort_order": 2},
			{"item_description": "Quick-start documentation", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which ZT411 is this?", "answer": "RET.SYS.ZEB.3717 — 203 dpi with serial, USB, Ethernet and BT 4.1. 300 dpi is 4624. RFID is 4566.", "sort_order": 1},
			{"question": "How is it different from ZT421?", "answer": "ZT411 is 4.09-inch / 14 ips. ZT421 is 6.6-inch / 12 ips. 600 dpi is a ZT411 family option, not ZT421.", "sort_order": 2},
			{"question": "Does 3717 include RFID?", "answer": "No. RFID UHF is RET.SYS.ZEB.4566. The official install film on this page is for that option.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zt600(media):
	slug = "zebra-zt610-zt620"
	item = "RET.SYS.ZEB.4792"
	card = catalog_card("zebra-zt610-product.jpg", "zebra-zt610-card.jpg")
	zt610 = media["zebra-zt610-product.jpg"]
	zt620 = media["zebra-zt620-product.png"]
	zt620_angle = media["zebra-zt620-angle.png"]
	doc = get_or_create(slug, "Zebra ZT610 / ZT620", item, card, "Industrial Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZT610 / ZT620",
		item=item,
		subcategory="Industrial Label Printers",
		category_label="PREMIUM INDUSTRIAL PRINTER",
	)
	doc.tagline = "ZT600 Series — 24/7 metal, Gigabit, 4-inch or 6-inch"
	doc.short_description = (
		"Zebra ZT610 (4-inch) and ZT620 (6-inch) are the premium industrial pair. This page "
		"is linked to the ZT610 203 dpi tear kit. ZT620 300 dpi and ZT610 600 dpi are other items."
	)
	doc.long_description = (
		"<p>ZT610 and ZT620 succeed the Xi Series: full-metal 24/7 printers with a 4.3-inch "
		"colour touch, Gigabit Ethernet and Link-OS. ZT610 is the 4-inch machine (up to 14 ips, "
		"203/300/600 dpi, down to 3 mm labels at 600 dpi). ZT620 is the 6-inch machine (up to "
		"12 ips, 203/300 dpi, media to 7.1 in).</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4792</strong> — ZT610, 4-inch, 203 dpi, tear, "
		"colour touch, serial, USB, Gigabit Ethernet, BT 4.1, USB Host, ZPL. "
		"<strong>RET.SYS.ZEB.4944</strong> is ZT610 600 dpi. <strong>RET.SYS.ZEB.4945</strong> "
		"is ZT620 6-inch 300 dpi tear. <strong>RET.SYS.ZEB.4294</strong> is ZT620 300 dpi peel "
		"with full rewind.</p>"
		"<p>Stay on ZT411 when 4-inch ZT400 is enough. Use this series when you need Xi-class "
		"duty, Gigabit, micro-labels (600 dpi ZT610) or a 6-inch premium chassis (ZT620).</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZT610 4-inch premium industrial label printer"
	doc.video_url = VIDEO_ZT600_OPTIONS
	doc.hero_trust_chips = "ZT610 4 in · 14 ips\nZT620 6 in · 12 ips\nGigabit Ethernet\n203 / 300 / 600 dpi"
	doc.story_heading = "Xi-class duty. Two widths."
	doc.visual_story_heading = "ZT610 and ZT620"
	doc.card_title = "ZT610 / ZT620"
	doc.card_summary = (
		"Premium ZT600 pair: ZT610 4-inch (this kit 203 dpi) and ZT620 6-inch. Gigabit, "
		"colour touch, 24/7 metal."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZT610 or ZT620"
	doc.final_cta_description = (
		"Printechs will confirm 4-inch vs 6-inch, 203/300/600 dpi, tear vs peel/rewind."
	)
	doc.meta_title = "Zebra ZT610 and ZT620 Industrial Printers | Printechs"
	doc.meta_description = (
		"Zebra ZT610 4-inch and ZT620 6-inch premium industrial printers. Gigabit, colour "
		"touch, 203/300/600 dpi. From Printechs in Saudi Arabia."
	)
	doc.set(
		"benefits",
		[
			{"icon": "durability", "title": "24/7 metal chassis", "description": "Xi-class duty cycle — heavier than ZT400. ZT610 50 lb; ZT620 57.4 lb.", "sort_order": 1},
			{"icon": "lines", "title": "Two widths", "description": "ZT610: 4.5 in media, 14 ips. ZT620: 7.1 in media, 12 ips.", "sort_order": 2},
			{"icon": "print", "title": "600 dpi micro-labels", "description": "ZT610 600 dpi (4944) prints labels as short as 3 mm. Not available on ZT620.", "sort_order": 3},
			{"icon": "connectivity", "title": "Gigabit Ethernet", "description": "Standard Gigabit, USB, serial, BT 4.1 and USB Host on the 4792 kit.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZT610 4-inch", "image": zt610, "image_alt": "Zebra ZT610 premium industrial printer", "caption": "This page’s linked SKU — ZT610 203 dpi tear (4792).", "sort_order": 1},
			{"label": "ZT620 6-inch", "image": zt620, "image_alt": "Zebra ZT620 6-inch industrial printer", "caption": "6-inch sibling — 300 dpi tear is RET.SYS.ZEB.4945.", "sort_order": 2},
			{"label": "ZT620 angle", "image": zt620_angle, "image_alt": "Zebra ZT620 at an angle", "caption": "Same ZT600 platform, wider media path.", "sort_order": 3},
			{"label": "Line-side", "image": media["warehouse"], "image_alt": "Industrial warehouse labelling", "caption": "24/7 shipping and WIP identification.", "sort_order": 4},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "ZT610 (this SKU)", "description": "4 in · 203 dpi · 14 ips · tear", "sort_order": 1},
			{"icon": "lines", "title": "ZT620", "description": "6 in · 300 dpi item 4945 · 12 ips", "sort_order": 2},
			{"icon": "connectivity", "title": "Network", "description": "Gigabit Ethernet · BT 4.1", "sort_order": 3},
			{"icon": "display", "title": "HMI", "description": "4.3-inch colour touch", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Series", "Zebra ZT600 — ZT610 (4-inch) and ZT620 (6-inch), not ZT411/ZT421"),
					("Item on this page", "RET.SYS.ZEB.4792 — ZT610 4-inch 203 dpi, tear, colour touch, Gigabit, BT 4.1"),
					("ZT610 600 dpi", "RET.SYS.ZEB.4944 — micro-labels; cutter/RFID not supported on 600 dpi"),
					("ZT620 300 dpi tear", "RET.SYS.ZEB.4945 — 6-inch, colour touch, Gigabit"),
					("ZT620 peel/rewind", "RET.SYS.ZEB.4294 — 6-inch 300 dpi peel with full rewind"),
				],
			),
			(
				"ZT610 printing",
				[
					("Width / speed", "Media 0.79–4.5 in; up to 14 ips (203/300 dpi family)"),
					("Resolution", "203 dpi on 4792; 300 dpi family; 600 dpi on 4944"),
					("Size / weight", "19.88 × 10.56 × 15.58 in (505 × 268 × 396 mm); 50 lb / 22.7 kg"),
				],
			),
			(
				"ZT620 printing",
				[
					("Width / speed", "Media 2.0–7.1 in; up to 12 ips"),
					("Resolution", "203 or 300 dpi (4945 is 300 dpi tear)"),
					("Size / weight", "19.88 × 13.44 × 15.58 in (505 × 341 × 396 mm); 57.4 lb / 26 kg"),
				],
			),
			(
				"Shared ZT600",
				[
					("I/O", "Gigabit Ethernet, USB 2.0, USB Host, RS-232, Bluetooth 4.1"),
					("Optional", "Wi-Fi, parallel, applicator, peel, cutter, rewind, RFID"),
					("Ribbon", "Up to 450 m, coated-side out, 1 in core"),
					("Media roll", "8 in OD on a 3 in core"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "High-volume shipping", "description": "24/7 shippers — 4-inch on ZT610, 6-inch on ZT620.", "image": media["warehouse"], "image_alt": "Warehouse industrial printing", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Manufacturing / micro-labels", "description": "ZT610 600 dpi (4944) for PCB and small-component marks.", "image": media["pharma"], "image_alt": "Precision labelling", "industry_link": "pharmaceutical", "sort_order": 2},
			{"title": "Wide case labels", "description": "ZT620 takes media to 7.1 inches for large compliance panels.", "image": media["packaging"], "image_alt": "Wide case labels", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "ZT600 media-handling options",
				"body": (
					"Official Zebra ZT600 film: tear, peel, cutter and rewind on the same "
					"platform. 4792 is tear. Peel/rewind on ZT620 is 4294. This clip is not "
					"used on ZT411 or ZT421."
				),
				"video_url": VIDEO_ZT600_OPTIONS,
				"image": zt610,
				"image_alt": "Zebra ZT610",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Pick ZT610 or ZT620",
				"body": (
					"ZT610 if you need 4-inch width, 14 ips or 600 dpi micro-labels. ZT620 "
					"if you need 6-inch / 7.1-inch media at 12 ips. Both share Gigabit and "
					"the 4.3-inch colour touch."
				),
				"image": zt620,
				"image_alt": "Zebra ZT620",
				"link_label": "Request a Quote",
				"link_href": "/products/zebra-zt610-zt620/quote",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Gigabit, first formats and 24/7 line placement.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels & ribbons", "description": "4-inch (ZT610) or wide (ZT620) industrial media and 450 m ribbon.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "ZT61/ZT62 OneCare, printheads and platens in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Colour-touch menus, tear vs peel/rewind and 600 dpi media.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZT610 printer (203 dpi tear kit on this page)", "sort_order": 1},
			{"item_description": "Euro and UK power cord", "sort_order": 2},
			{"item_description": "Quick-start documentation", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which item is linked?", "answer": "RET.SYS.ZEB.4792 — ZT610 4-inch 203 dpi tear. ZT620 300 dpi tear is 4945. ZT610 600 dpi is 4944.", "sort_order": 1},
			{"question": "ZT610 or ZT620?", "answer": "ZT610 is 4-inch / 14 ips / optional 600 dpi. ZT620 is 6-inch / 12 ips / media to 7.1 inches.", "sort_order": 2},
			{"question": "When is ZT411 enough?", "answer": "When you do not need Xi-class duty, Gigabit or 600 dpi micro-labels. Start with ZT411 (3717).", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def update_zt421_related():
	"""Keep ZT421 videos unique and point related products at the new lineup."""
	name = "RET.SYS.ZEB.3626"
	if not frappe.db.exists("Website Product", name):
		return
	from printechs_digital.setup.fill_zebra_zt421 import VIDEO_LOAD

	doc = frappe.get_doc("Website Product", name)
	doc.video_url = VIDEO_LOAD
	for row in doc.content_sections or []:
		if "h-YhWqI2zUY" in (row.video_url or ""):
			row.video_url = VIDEO_LOAD
			row.heading = "Load media and ribbon on ZT421"
			row.body = (
				"ZT411/ZT421 side-loading path. Official ZT411 unbox now lives on the "
				"ZT411 page so the films are not duplicated."
			)
	set_related(doc, LINEUP_RELATED["zebra-zt421"])
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	print("Updated ZT421 related products and videos")


def wire_related():
	for slug, related in LINEUP_RELATED.items():
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		set_related(doc, related)
		doc.flags.ignore_permissions = True
		doc.save()
	frappe.db.commit()
	print("Wired printer-lineup related products")


def fill_zebra_barcode_printers():
	media = _media()
	fill_zd421(media)
	fill_zd621(media)
	fill_zd621r(media)
	fill_zt411(media)
	fill_zt600(media)
	update_zt421_related()
	wire_related()
	return "ok"
