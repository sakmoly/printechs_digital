# Copyright (c) 2026, Printechs and contributors
"""Create and fill the Printechs Zebra mobile-printer lineup.

ZQ620 Plus (3-inch) → ZQ630 Plus (4-inch) → ZQ630 RFID Plus → ZQ521 (rugged)

Official:
https://www.zebra.com/us/en/products/printers/mobile/zq600-plus-series.html
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/zq600-series-spec-sheet-en-us.pdf
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/zq600-series-rfid-spec-sheet-en-us.pdf
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/zq511-zq521-spec-sheet-en-us.pdf

Images and YouTube IDs are unique to these pages — do not reuse desktop/industrial assets.
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

# Unique videos — none of these IDs are on desktop/industrial pages.
VIDEO_ZQ620_VS = "https://youtu.be/v8I_vP4CBCw"  # Official: ZQ300 Plus vs ZQ600 Plus
VIDEO_ZQ620_LOAD = "https://youtu.be/hDCCSYvHyHo"  # Barcode Bonanza: ZQ600 media load
VIDEO_ZQ630_WH = "https://youtu.be/0EbabO90KzI"  # Official: ZQ600 Plus warehouse
VIDEO_ZQ630_CMP = "https://youtu.be/Vym8MqatOok"  # Official: ZQ630 Plus vs SATO PW4NX
VIDEO_ZQ630R = "https://youtu.be/6ms4FajsSQw"  # Michael RFID: mobile RFID overview
VIDEO_ZQ521_LOAD = "https://youtu.be/jJRKAyeO7X8"  # Barcode Bonanza: ZQ500 media load

IMAGES = {
	"zebra-zq620-plus-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4325/8911/zq620-plus-photography-product-front-right-3x2-3600_1__30179.1770391593.jpg",
		],
		"zq620-front.jpg",
	),
	"zebra-zq620-plus-open.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4325/8912/zq600-series-right-open-3x2-3600__66114.1770391593.jpg",
		],
		"zq620-open.jpg",
	),
	"zebra-zq630-plus-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4326/8921/zq630-plus-photography-product-front-left-3x2-3600_1__32062.1770637938.jpg",
		],
		"zq630-front.jpg",
	),
	"zebra-zq630-plus-print.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4326/8920/zq630-plus-photography-product-headon-media-3x2-3600_1__14489.1770637938.jpg",
		],
		"zq630-headon.jpg",
	),
	"zebra-zq630-rfid-plus-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/3747/10461/1000x1000_17__46706.1770826081.jpg",
		],
		"zq630r-plusr.jpg",
	),
	"zebra-zq630-rfid-plus-front.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/3747/6995/zebra-zq630-rfid-printer__88460.1770826080.png",
		],
		"zq630r-1.png",
	),
	"zebra-zq630-rfid-plus-print.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/3747/7000/zebra-zq630-rfid-printer-3__72165.1770826080.png",
		],
		"zq630r-3.png",
	),
	"zebra-zq521-product.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4330/8941/zq500-series-right-facing-3x2-3600__03489.1687802602.jpg",
		],
		"zq521-right.jpg",
	),
	"zebra-zq521-open.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4330/8942/zq500-series-steel-hinge-closeup-3x2-3600_1__22008.1687802605.jpg",
		],
		"zq521-hinge.jpg",
	),
}

LINEUP_RELATED = {
	"zebra-zq620-plus": ["zebra-zq630-plus", "zebra-zq521", "zebra-zd621"],
	"zebra-zq630-plus": ["zebra-zq620-plus", "zebra-zq630-rfid-plus", "zebra-zt411"],
	"zebra-zq630-rfid-plus": ["zebra-zq630-plus", "zebra-zd621r", "zebra-zt411"],
	"zebra-zq521": ["zebra-zq630-plus", "zebra-zq620-plus", "zebra-zt411"],
}


def _media():
	paths = {}
	for filename, (urls, tmp_name) in IMAGES.items():
		paths[filename] = download_file(filename, urls, tmp_name)
	wipe_reseller_badge("zebra-zq630-rfid-plus-product.jpg")
	paths["retail"] = copy_public_image("industry-retail.jpg")
	paths["warehouse"] = copy_public_image("industry-warehouse-logistics.jpg")
	paths["packaging"] = copy_public_image("industry-packaging.jpg")
	paths["fashion"] = copy_public_image("industry-fashion.jpg")
	return paths


def fill_zq620_plus(media):
	slug = "zebra-zq620-plus"
	item = ""
	card = catalog_card("zebra-zq620-plus-product.jpg", "zebra-zq620-plus-card.jpg")
	photo = media["zebra-zq620-plus-product.jpg"]
	opened = media["zebra-zq620-plus-open.jpg"]
	doc = get_or_create(slug, "Zebra ZQ620 Plus", item, card, "Mobile Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZQ620 Plus",
		item=item,
		subcategory="Mobile Label Printers",
		category_label="3-INCH MOBILE PRINTER",
	)
	doc.tagline = "Premium 3-inch mobile — colour LCD, instant wake-up, optional Wi-Fi 6"
	doc.short_description = (
		"Zebra ZQ620 Plus is the 3-inch ZQ600 Plus mobile printer for retail markdown, "
		"shelf labels and warehouse tote IDs. Colour LCD, PowerPrecision+ 3250 mAh and "
		"instant wake-up. Wi-Fi 6 / Bluetooth 5.3 is a factory radio option."
	)
	doc.long_description = (
		"<p>ZQ620 Plus is Printechs’ core 3-inch Zebra mobile printer. Official print width "
		"is 2.8 in / 72 mm, speed is 4.5 ips / 115 mm/s at 203 dpi, and the standard battery "
		"is a 3250 mAh PowerPrecision+ pack. Instant wake-up works over Wi-Fi or Bluetooth so "
		"the printer sleeps between jobs.</p>"
		"<p>Zebra positions ZQ600 Plus as the premium indoor mobile family: colour 288 × 240 "
		"display, Link-OS, QLn-compatible accessories, and a choice of Wi-Fi 6 (802.11ax + "
		"BT 5.3) or Wi-Fi 5 (802.11ac + BT 4.2). Radios are factory-installed, not field "
		"cards. This page is the <strong>ZQ620 Plus</strong> family — Printechs does not "
		"currently list a ZQ620 Plus Item. RET.SYS.ZEB.3452 is the older ZQ620 (not Plus).</p>"
		"<p>Stay on 3-inch for markdown and shelf work. Step up to ZQ630 Plus for 4-inch "
		"shipping labels, ZQ630 RFID Plus to encode RAIN tags on the floor, or ZQ521 when "
		"the job is MIL-STD field / cross-dock abuse rather than premium indoor HMI.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZQ620 Plus 3-inch mobile label printer with colour display"
	doc.video_url = VIDEO_ZQ620_VS
	doc.hero_trust_chips = "3-inch · 2.8 in / 72 mm\n4.5 ips · 203 dpi\n3250 mAh PowerPrecision+\nOptional Wi-Fi 6 / BT 5.3"
	doc.story_heading = "The 3-inch Plus printer for the sales floor"
	doc.visual_story_heading = "ZQ620 Plus"
	doc.card_title = "ZQ620 Plus"
	doc.card_summary = (
		"3-inch ZQ600 Plus mobile: colour LCD, 4.5 ips, 3250 mAh. Markdown, shelf and tote labels."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZQ620 Plus for mobile retail labels"
	doc.final_cta_description = (
		"Printechs will confirm Wi-Fi 6 vs Wi-Fi 5 vs Bluetooth-only, linered vs linerless, "
		"and whether you need the Ethernet cradle."
	)
	doc.meta_title = "Zebra ZQ620 Plus 3-inch Mobile Printer | Printechs"
	doc.meta_description = (
		"Zebra ZQ620 Plus 3-inch mobile printer: 203 dpi, 4.5 ips, colour LCD and optional "
		"Wi-Fi 6. Retail markdown and shelf labels from Printechs."
	)
	doc.set(
		"benefits",
		[
			{"icon": "print", "title": "3-inch Plus class", "description": "2.8 in / 72 mm at 203 dpi, 4.5 ips. Direct thermal — not ZQ630’s 4-inch path.", "sort_order": 1},
			{"icon": "display", "title": "Colour LCD", "description": "288 × 240 colour display, 5-way nav and Print Touch NFC. Not the ZQ521 mono LCD.", "sort_order": 2},
			{"icon": "battery", "title": "3250 mAh PP+", "description": "PowerPrecision+ metrics and instant wake-up. Extended pack adds 0.6 in height.", "sort_order": 3},
			{"icon": "connectivity", "title": "Wi-Fi 6 optional", "description": "Factory dual radio: 802.11ax + BT 5.3 or 802.11ac + BT 4.2. Not field-upgradeable.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZQ620 Plus", "image": photo, "image_alt": "Zebra ZQ620 Plus mobile printer", "caption": "3-inch ZQ620 Plus with colour LCD — not ZQ630, not ZQ521.", "sort_order": 1},
			{"label": "Clamshell load", "image": opened, "image_alt": "ZQ620 Plus open media path", "caption": "Center-loading 3-inch rolls, 2.6 in OD, 0.75 or 1.375 in core.", "sort_order": 2},
			{"label": "Retail floor", "image": media["retail"], "image_alt": "Retail shelf labelling", "caption": "Markdown, shelf-edge and replacement tags on the floor.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "Print", "description": "203 dpi · 4.5 ips · 2.8 in", "sort_order": 1},
			{"icon": "battery", "title": "Battery", "description": "3250 mAh PowerPrecision+", "sort_order": 2},
			{"icon": "display", "title": "HMI", "description": "Colour LCD · NFC · Link-OS", "sort_order": 3},
			{"icon": "rugged", "title": "Duty", "description": "IP54 · 5 ft / 1.52 m drop", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZQ620 Plus 3-inch mobile (not ZQ610 Plus, not ZQ630 Plus, not ZQ521)"),
					("Item on this page", "No ERP Item yet — quote the radio (Wi-Fi 6 / Wi-Fi 5 / BT) and platen"),
					("Predecessor", "RET.SYS.ZEB.3452 is older ZQ620 (not Plus). Do not treat 3452 as ZQ620 Plus"),
					("Not on this model", "4-inch media (ZQ630), RFID encode (ZQ630 RFID Plus), MIL-STD 810G (ZQ521)"),
				],
			),
			(
				"Printing & media",
				[
					("Method / resolution", "Direct thermal, 203 dpi / 8 dots/mm"),
					("Print speed / width", "Up to 4.5 ips / 115 mm/s; 2.8 in / 72 mm"),
					("Print length", "0.5–32 in / 12.7–813 mm"),
					("Media width / OD", "1.0–3.125 in / 25–79 mm; 2.6 in / 66 mm OD"),
					("Sensors", "Black mark, gap, label present (peeler)"),
					("Memory / OS", "256 MB RAM, 512 MB Flash. Link-OS, ZPL, CPCL, EPL"),
				],
			),
			(
				"Power, I/O & environment",
				[
					("Battery", "3250 mAh / 23.4 Wh PowerPrecision+ Li-Ion; extended pack optional"),
					("Wireless options", "Wi-Fi 6 + BT 5.3 or Wi-Fi 5 + BT 4.2 (factory). USB mini-B, 14-pin serial"),
					("Ethernet", "10/100 via optional charging cradle — not a built-in LAN port"),
					("Size / weight", "6.84 × 4.64 × 3.03 in (174 × 118 × 77 mm); 1.6 lb / 0.73 kg with battery"),
					("Environment", "IP54. 5 ft / 1.52 m to concrete. −20 to 50 °C"),
					("Warranty", "Zebra 1-year limited. OneCare available"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Retail markdown", "description": "Price and promotional labels at the bay, not back at a desk.", "image": media["retail"], "image_alt": "Retail markdown labels", "industry_link": "retail", "sort_order": 1},
			{"title": "Shelf labelling", "description": "3-inch shelf-edge and replacement tags during a reset.", "image": media["retail"], "image_alt": "Shelf-edge labelling", "industry_link": "retail", "sort_order": 2},
			{"title": "Warehouse totes", "description": "Short tote and pick labels where 3-inch is enough.", "image": media["warehouse"], "image_alt": "Warehouse tote labels", "industry_link": "warehouse-logistics", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Why Zebra puts ZQ600 Plus above ZQ300 Plus",
				"body": (
					"Official Zebra comparison: ZQ600 Plus is the premium indoor family — "
					"colour LCD, instant wake-up and optional Wi-Fi 6. This page is the "
					"3-inch ZQ620 Plus, not the 4-inch ZQ630 Plus."
				),
				"video_url": VIDEO_ZQ620_VS,
				"image": photo,
				"image_alt": "Zebra ZQ620 Plus",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Load 3-inch media on a ZQ600",
				"body": (
					"Distributor film shows ZQ600-series clamshell load and peel. Use 3-inch "
					"rolls on ZQ620 Plus. 4-inch shipping labels belong on ZQ630 Plus."
				),
				"video_url": VIDEO_ZQ620_LOAD,
				"image": opened,
				"image_alt": "ZQ620 Plus open for media load",
				"link_label": "See ZQ630 Plus",
				"link_href": "/products/zebra-zq630-plus",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Radio, Print Touch pairing and first 3-inch format.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels", "description": "3-inch DT rolls, linered or linerless, matched to ZQ620 Plus.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Batteries, platens, cradles and ZQ6X OneCare in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Clamshell load, peeler bail and colour-LCD alerts.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZQ620 Plus printer (radio per quoted configuration)", "sort_order": 1},
			{"item_description": "3250 mAh PowerPrecision+ battery", "sort_order": 2},
			{"item_description": "Belt clip (not with extended battery)", "sort_order": 3},
			{"item_description": "Quick-start documentation (AC adapter typically sold separately)", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which ZQ620 is this?", "answer": "The ZQ620 Plus family page. There is no Plus Item in ERP yet. RET.SYS.ZEB.3452 is the older ZQ620, not Plus.", "sort_order": 1},
			{"question": "Does every ZQ620 Plus include Wi-Fi 6?", "answer": "No. Wi-Fi 6 + BT 5.3 or Wi-Fi 5 + BT 4.2 is a factory dual-radio choice. Bluetooth-only kits also exist.", "sort_order": 2},
			{"question": "When should I order ZQ630 Plus instead?", "answer": "When you need 4.1-inch / 104 mm shipping or pallet labels and the 6600 mAh pack. RFID encode is ZQ630 RFID Plus only.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zq630_plus(media):
	slug = "zebra-zq630-plus"
	item = "RET.SYS.ZEB.4370"
	card = catalog_card("zebra-zq630-plus-product.jpg", "zebra-zq630-plus-card.jpg")
	photo = media["zebra-zq630-plus-product.jpg"]
	printing = media["zebra-zq630-plus-print.jpg"]
	doc = get_or_create(slug, "Zebra ZQ630 Plus", item, card, "Mobile Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZQ630 Plus",
		item=item,
		subcategory="Mobile Label Printers",
		category_label="4-INCH MOBILE PRINTER",
	)
	doc.tagline = "4-inch ZQ600 Plus — warehouse, shipping and receiving"
	doc.short_description = (
		"Zebra ZQ630 Plus is the 4-inch ZQ600 Plus mobile printer. This kit is Dual "
		"802.11ac / Bluetooth 4.x with linered platen, shoulder strap and belt clip. "
		"6600 mAh PowerPrecision+. RFID is ZQ630 RFID Plus, not this item."
	)
	doc.long_description = (
		"<p>ZQ630 Plus is the 4-inch workhorse of Zebra’s premium mobile family: 4.1 in / "
		"104 mm print width, 4.5 ips, colour LCD and a 6600 mAh / 47.5 Wh PowerPrecision+ "
		"battery for long warehouse shifts. Instant wake-up, 802.11r roaming and QLn-compatible "
		"cradles keep carts and forklifts online.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4370</strong> — English fonts, Dual 802.11ac / "
		"BT 4.x (Wi-Fi 5, not Wi-Fi 6), linered platen, 0.75 in core, Group E, shoulder strap "
		"and belt clip. Wi-Fi 6 + Bluetooth 5.3 is a different factory radio. Linerless is a "
		"different platen. RFID encode is the separate ZQ630 RFID Plus product.</p>"
		"<p>Use ZQ620 Plus for 3-inch retail markdown. Use ZQ521 when MIL-STD 810G / 6.6 ft "
		"field duty matters more than the colour LCD. Use ZT411 when the label should stay "
		"on an industrial bench.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZQ630 Plus 4-inch mobile label printer"
	doc.video_url = VIDEO_ZQ630_WH
	doc.hero_trust_chips = "4-inch · 4.1 in / 104 mm\n4.5 ips · 203 dpi\n6600 mAh PowerPrecision+\nWi-Fi 5 + BT 4.x on 4370"
	doc.story_heading = "4-inch mobile labels for the dock"
	doc.visual_story_heading = "ZQ630 Plus"
	doc.card_title = "ZQ630 Plus"
	doc.card_summary = (
		"4-inch ZQ600 Plus: 104 mm, 4.5 ips, 6600 mAh. This SKU is Wi-Fi 5 + BT 4.x."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZQ630 Plus for warehouse labels"
	doc.final_cta_description = (
		"Confirm Wi-Fi 5 vs Wi-Fi 6, linered vs linerless, and whether RFID encode "
		"belongs on ZQ630 RFID Plus instead."
	)
	doc.meta_title = "Zebra ZQ630 Plus 4-inch Mobile Printer | Printechs"
	doc.meta_description = (
		"Zebra ZQ630 Plus 4-inch mobile printer, 203 dpi, 4.5 ips, 6600 mAh. Warehouse "
		"and shipping labels from Printechs. Item RET.SYS.ZEB.4370."
	)
	doc.set(
		"benefits",
		[
			{"icon": "print", "title": "4-inch mobile", "description": "4.1 in / 104 mm at 4.5 ips. Shipping, receiving and pallet IDs on a belt or cart.", "sort_order": 1},
			{"icon": "battery", "title": "6600 mAh PP+", "description": "4-cell PowerPrecision+ — larger than the 3250 mAh ZQ620 Plus pack.", "sort_order": 2},
			{"icon": "connectivity", "title": "Wi-Fi 5 on 4370", "description": "This item is 802.11ac + BT 4.x. Wi-Fi 6 + BT 5.3 is another factory kit.", "sort_order": 3},
			{"icon": "inventory", "title": "Indoor premium", "description": "Colour LCD, instant wake-up, IP54, 6 ft drop. RFID is a different product.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZQ630 Plus", "image": photo, "image_alt": "Zebra ZQ630 Plus mobile printer", "caption": "4-inch ZQ630 Plus — not the 3-inch ZQ620, not the RFID SKU.", "sort_order": 1},
			{"label": "Printing", "image": printing, "image_alt": "ZQ630 Plus printing a 4-inch label", "caption": "4.1-inch path for shippers and receiving labels.", "sort_order": 2},
			{"label": "Warehouse", "image": media["warehouse"], "image_alt": "Warehouse shipping and receiving", "caption": "Cart, belt or optional vehicle / forklift cradle.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 4.5 ips · 4.1 in", "sort_order": 1},
			{"icon": "battery", "title": "Battery", "description": "6600 mAh / 47.5 Wh PP+", "sort_order": 2},
			{"icon": "connectivity", "title": "On 4370", "description": "802.11ac · BT 4.x · USB", "sort_order": 3},
			{"icon": "rugged", "title": "Duty", "description": "IP54 · 6 ft / 1.83 m drop", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZQ630 Plus 4-inch mobile (not ZQ620 Plus, not ZQ630 RFID Plus, not ZQ521)"),
					("Item on this page", "RET.SYS.ZEB.4370 — Dual 802.11ac / BT 4.x, linered, 0.75 in core, strap + clip"),
					("Also available", "Wi-Fi 6 + BT 5.3 factory radio; linerless platen; vehicle cradle"),
					("Not on this item", "RFID encode (ZQ630 RFID Plus), Wi-Fi 6, 3-inch-only media path"),
				],
			),
			(
				"Printing & media",
				[
					("Method / resolution", "Direct thermal, 203 dpi / 8 dots/mm"),
					("Print speed / width", "Up to 4.5 ips / 115 mm/s; 4.1 in / 104 mm"),
					("Media width", "2.0–4.4 in linered; 2.0–4.1 in linerless"),
					("Roll / cores", "2.6 in / 66 mm OD; 0.75 or 1.375 in core (this kit is 0.75 in)"),
					("Sensors", "Black mark, gap, label present"),
					("Memory / OS", "256 MB RAM, 512 MB Flash. Link-OS, ZPL, CPCL, EPL"),
				],
			),
			(
				"Power, I/O & environment",
				[
					("Battery", "6600 mAh / 47.5 Wh PowerPrecision+ Li-Ion"),
					("I/O on 4370", "Wi-Fi 5 (802.11ac), Bluetooth 4.x, USB mini-B, 14-pin serial"),
					("Optional I/O", "Wi-Fi 6 + BT 5.3 factory kit; 10/100 Ethernet via cradle"),
					("Size / weight", "7.35 × 6.5 × 3.25 in (187 × 165 × 83 mm); 2.45 lb / 1.1 kg with battery"),
					("Environment", "IP54. 6 ft / 1.83 m to concrete. −20 to 50 °C"),
					("Warranty", "Zebra 1-year limited. ZQ6X OneCare (4609 / 4618) available"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Shipping & receiving", "description": "4-inch shippers printed at the door, not walked back to a bench.", "image": media["warehouse"], "image_alt": "Shipping and receiving", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Put-away & staging", "description": "Cart-mounted labels for put-away and staging lanes.", "image": media["warehouse"], "image_alt": "Warehouse staging", "industry_link": "warehouse-logistics", "sort_order": 2},
			{"title": "Packing", "description": "Pack-bench overflow when the industrial printer is the other side of the DC.", "image": media["packaging"], "image_alt": "Packing labels", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "ZQ600 Plus in the warehouse",
				"body": (
					"Official Zebra warehouse film for the ZQ600 Plus family. This page is "
					"the 4-inch ZQ630 Plus on RET.SYS.ZEB.4370 — Wi-Fi 5, not the RFID model."
				),
				"video_url": VIDEO_ZQ630_WH,
				"image": printing,
				"image_alt": "ZQ630 Plus printing a warehouse label",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "ZQ630 Plus versus other 4-inch mobiles",
				"body": (
					"Official Zebra comparison against another 4-inch mobile. Choose ZQ630 "
					"Plus for colour LCD, 6600 mAh and indoor Plus features. Choose ZQ521 "
					"for MIL-STD field duty. Choose ZQ630 RFID Plus to encode tags."
				),
				"video_url": VIDEO_ZQ630_CMP,
				"image": photo,
				"image_alt": "Zebra ZQ630 Plus",
				"link_label": "See ZQ630 RFID Plus",
				"link_href": "/products/zebra-zq630-rfid-plus",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Wi-Fi 5 radio, cradle Ethernet and first 4-inch format.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels", "description": "4-inch DT linered rolls for 4370. Linerless is another platen.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "6600 mAh packs, platens and ZQ6X OneCare in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Clamshell load, peeler and colour-LCD status.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZQ630 Plus printer (4370 — Wi-Fi 5 / BT 4.x, linered)", "sort_order": 1},
			{"item_description": "6600 mAh PowerPrecision+ battery", "sort_order": 2},
			{"item_description": "Shoulder strap and belt clip", "sort_order": 3},
			{"item_description": "Quick-start documentation (AC adapter typically sold separately)", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which ZQ630 Plus is this?", "answer": "RET.SYS.ZEB.4370 — Dual 802.11ac / BT 4.x, linered platen, strap and clip. Wi-Fi 6 is a different factory radio.", "sort_order": 1},
			{"question": "Does 4370 encode RFID?", "answer": "No. RFID is ZQ630 RFID Plus only (factory encoder). Do not mix that onto 4370.", "sort_order": 2},
			{"question": "ZQ630 Plus or ZQ521?", "answer": "ZQ630 Plus is indoor premium (colour LCD, 6600 mAh). ZQ521 is MIL-STD 810G / 6.6 ft rugged field.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zq630_rfid_plus(media):
	slug = "zebra-zq630-rfid-plus"
	item = ""
	card = catalog_card("zebra-zq630-rfid-plus-product.jpg", "zebra-zq630-rfid-plus-card.jpg")
	photo = media["zebra-zq630-rfid-plus-front.png"]
	printing = media["zebra-zq630-rfid-plus-print.png"]
	doc = get_or_create(slug, "Zebra ZQ630 RFID Plus", item, card, "Mobile Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZQ630 RFID Plus",
		item=item,
		subcategory="Mobile Label Printers",
		category_label="4-INCH RFID MOBILE PRINTER",
	)
	doc.tagline = "Print and encode RAIN RFID on a 4-inch belt printer"
	doc.short_description = (
		"Zebra ZQ630 RFID Plus is the RFID ZQ630 Plus: 4.1-inch direct thermal, integrated "
		"UHF encoder, Adaptive Encoding, 6600 mAh and colour LCD. Factory RFID — not an "
		"add-on to RET.SYS.ZEB.4370."
	)
	doc.long_description = (
		"<p>ZQ630 RFID Plus is the mobile RFID printer in Printechs’ Zebra line. It prints "
		"and encodes UHF EPC Gen 2 V2 / ISO 18000-63 / RAIN tags on the spot, with Adaptive "
		"Encoding so you calibrate once per media type. Official minimum tag pitch is 16 mm. "
		"RFID media is black-mark only — this model does not support gap sensing.</p>"
		"<p>Print class matches ZQ630 Plus: 203 dpi, 4.1 in / 104 mm, 4.5 ips, 6600 mAh "
		"PowerPrecision+, colour LCD, IP54 and 6 ft drop. Wireless is a factory choice of "
		"Wi-Fi 6 + BT 5.3 or Wi-Fi 5 + BT 4.2. Printechs does not currently list a ZQ630 "
		"RFID Plus Item — request a quote. <strong>RET.SYS.ZEB.4370 is the non-RFID "
		"ZQ630 Plus</strong> and must not be ordered as an RFID printer.</p>"
		"<p>Desktop RFID is ZD621R. Industrial RFID is ZT411 (4566) or the ZT600 family. "
		"Use this page when associates encode case, pallet or apparel tags on a cart or belt.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZQ630 RFID Plus 4-inch mobile RFID printer"
	doc.video_url = VIDEO_ZQ630R
	doc.hero_trust_chips = "UHF RAIN / EPC Gen 2 V2\nAdaptive Encoding · 16 mm pitch\n4.1 in · 4.5 ips · 6600 mAh\nFactory RFID — not 4370"
	doc.story_heading = "RFID labels where the work happens"
	doc.visual_story_heading = "ZQ630 RFID Plus"
	doc.card_title = "ZQ630 RFID Plus"
	doc.card_summary = (
		"4-inch mobile that prints and encodes RAIN RFID. Separate product from ZQ630 Plus 4370."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZQ630 RFID Plus for mobile encode"
	doc.final_cta_description = (
		"Printechs will match inlays, black-mark media and the Wi-Fi 6 vs Wi-Fi 5 radio."
	)
	doc.meta_title = "Zebra ZQ630 RFID Plus Mobile RFID Printer | Printechs"
	doc.meta_description = (
		"Zebra ZQ630 RFID Plus 4-inch mobile printer: print and encode RAIN / EPC Gen 2 "
		"UHF tags. Adaptive Encoding, 6600 mAh. From Printechs."
	)
	doc.set(
		"benefits",
		[
			{"icon": "scan", "title": "Print + encode", "description": "Integrated UHF reader/encoder. RAIN, EPC Gen 2 V2, ISO 18000-63, Gen2X.", "sort_order": 1},
			{"icon": "integration", "title": "Adaptive Encoding", "description": "Calibrate once per media type. 16 mm minimum pitch. ZPL RFID commands.", "sort_order": 2},
			{"icon": "battery", "title": "6600 mAh shift", "description": "Same 4-cell PP+ pack as ZQ630 Plus. Instant wake-up over Wi-Fi or Bluetooth.", "sort_order": 3},
			{"icon": "inventory", "title": "RFID strategy", "description": "Mobile sibling to ZD621R (desktop) and ZT411 RFID (industrial).", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZQ630 RFID Plus", "image": photo, "image_alt": "Zebra ZQ630 RFID Plus printer", "caption": "Factory RFID chassis — not RET.SYS.ZEB.4370.", "sort_order": 1},
			{"label": "On-the-spot labels", "image": printing, "image_alt": "ZQ630 RFID Plus printing RFID labels", "caption": "Black-mark RFID media; gap sensing is not supported.", "sort_order": 2},
			{"label": "Apparel & assets", "image": media["fashion"], "image_alt": "Apparel RFID labelling", "caption": "Item, case and return tags on the floor.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "scan", "title": "RFID", "description": "UHF · RAIN · 16 mm pitch", "sort_order": 1},
			{"icon": "print", "title": "Print", "description": "203 dpi · 4.5 ips · 4.1 in", "sort_order": 2},
			{"icon": "battery", "title": "Battery", "description": "6600 mAh PowerPrecision+", "sort_order": 3},
			{"icon": "connectivity", "title": "Radio", "description": "Wi-Fi 6 or Wi-Fi 5 factory", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZQ630 RFID Plus (factory UHF — not 4370, not ZD621R, not ZT411 4566)"),
					("Item on this page", "No ERP Item yet — quote radio, media and inlay. Do not ship 4370 as RFID"),
					("RFID protocols", "UHF EPC Gen 2 V2, ISO/IEC 18000-63, RAIN, Gen2X"),
					("Not on this model", "Gap sensing, field-install RFID, 3-inch ZQ620 path"),
				],
			),
			(
				"RFID, print & media",
				[
					("Encoder", "Integrated UHF reader/encoder in the printhead assembly"),
					("Setup", "Adaptive Encoding; RFID calibrate once per media type; ZPL ^HR / SGD"),
					("Tag pitch", "Minimum 16 mm. MCS and common EPC schemes (SGTIN-96, GS1 TDS)"),
					("Print", "Direct thermal, 203 dpi, 4.1 in / 104 mm, up to 4.5 ips"),
					("Media", "Black-mark RFID labels/tags only. 2.0–4.4 in linered; 2.6 in OD"),
					("Memory / OS", "256 MB RAM, 512 MB Flash. Link-OS, ZPL, CPCL, EPL"),
				],
			),
			(
				"Power, I/O & environment",
				[
					("Battery", "6600 mAh / 47.5 Wh PowerPrecision+ Li-Ion"),
					("Wireless", "Factory Wi-Fi 6 + BT 5.3 or Wi-Fi 5 + BT 4.2; USB; serial; cradle Ethernet"),
					("Size / weight", "7.35 × 6.5 × 3.25 in (187 × 165 × 83 mm); 2.45 lb / 1.1 kg"),
					("Environment", "IP54. 6 ft / 1.83 m to concrete. −20 to 50 °C"),
					("Warranty", "Zebra 1-year limited. OneCare available"),
					("Siblings", "Desktop RFID: ZD621R. Industrial RFID: ZT411 4566"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "RFID case / pallet", "description": "Encode and apply at receiving or staging instead of walking to a bench encoder.", "image": media["warehouse"], "image_alt": "RFID case labels", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Apparel & returns", "description": "Item-level tags on the floor during markdown or reverse logistics.", "image": media["fashion"], "image_alt": "Apparel RFID", "industry_link": "fashion-apparel", "sort_order": 2},
			{"title": "Asset tags", "description": "Mobile encode for assets that never visit a desktop RFID station.", "image": media["packaging"], "image_alt": "Asset RFID tags", "industry_link": "warehouse-logistics", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Mobile RFID printer overview",
				"body": (
					"Distributor overview of Zebra mobile RFID printing. This page is ZQ630 "
					"RFID Plus — factory UHF, black-mark media, Adaptive Encoding. The film "
					"is not the ZD621R desktop encode path."
				),
				"video_url": VIDEO_ZQ630R,
				"image": photo,
				"image_alt": "Zebra ZQ630 RFID Plus",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "When to stay on non-RFID ZQ630 Plus",
				"body": (
					"If you only need 4-inch barcodes, order RET.SYS.ZEB.4370. RFID is a "
					"separate factory printer. Desktop encode is ZD621R; industrial encode "
					"is ZT411 RFID."
				),
				"image": printing,
				"image_alt": "ZQ630 RFID Plus printing",
				"link_label": "See ZQ630 Plus",
				"link_href": "/products/zebra-zq630-plus",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "RFID calibrate, inlay map and first ZPL encode format.", "sort_order": 1},
			{"icon": "consumables", "title": "RFID media", "description": "Black-mark RAIN labels matched to ZQ630 RFID Plus.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Encoder, printhead and OneCare in Saudi Arabia.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "RFID menu, void-label behaviour and media changes.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZQ630 RFID Plus printer (factory UHF encoder)", "sort_order": 1},
			{"item_description": "6600 mAh PowerPrecision+ battery", "sort_order": 2},
			{"item_description": "Belt clip", "sort_order": 3},
			{"item_description": "Quick-start documentation", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Can I add RFID to 4370?", "answer": "No. RFID is factory-only on ZQ630 RFID Plus. Order the RFID product; do not convert RET.SYS.ZEB.4370.", "sort_order": 1},
			{"question": "Gap or black-mark media?", "answer": "Black-mark RFID media only. Official spec: ZQ630 RFID Plus does not support gap sensing.", "sort_order": 2},
			{"question": "Desktop or industrial RFID instead?", "answer": "ZD621R for a 4-inch desk. ZT411 RFID (4566) for industrial volume. This page is belt/cart encode.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_zq521(media):
	slug = "zebra-zq521"
	item = "RET.SYS.ZEB.3762"
	card = catalog_card("zebra-zq521-product.jpg", "zebra-zq521-card.jpg")
	photo = media["zebra-zq521-product.jpg"]
	opened = media["zebra-zq521-open.jpg"]
	doc = get_or_create(slug, "Zebra ZQ521", item, card, "Mobile Label Printers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra ZQ521",
		item=item,
		subcategory="Mobile Label Printers",
		category_label="RUGGED 4-INCH MOBILE PRINTER",
	)
	doc.tagline = "MIL-STD 4-inch mobile — field, warehouse, packing and cross-dock"
	doc.short_description = (
		"Zebra ZQ521 is the rugged 4-inch ZQ500-series mobile printer. This kit is 203 dpi, "
		"Bluetooth, LCD and 3250 mAh. IP54 and MIL-STD 810G, 6.6 ft / 2 m to concrete. "
		"Wi-Fi is another ZQ521 configuration, not on 3762."
	)
	doc.long_description = (
		"<p>ZQ521 is a different selling story from ZQ600 Plus: military-grade durability "
		"for field work, warehouse, packing, staging and cross-dock. Official ratings are "
		"IP54 without a case, MIL-STD 810G drop/shock, 6.6 ft / 2 m to concrete and 1,300 "
		"tumbles from 3.3 ft. An optional exoskeleton raises drop to 10 ft and IP to IP65.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.3762</strong> — 203 dpi, Bluetooth, LCD, "
		"104 mm print width, 127 mm/s (5 ips in draft), 3250 mAh. Dual-radio Wi-Fi (802.11ac) "
		"is a different ZQ521 kit. RFID and linerless are separate ZQ511/ZQ521 options. "
		"The HMI is a simple LCD with large icons — not the ZQ630 Plus colour display.</p>"
		"<p>Choose ZQ630 Plus when you want colour LCD, 6600 mAh and indoor Plus features. "
		"Choose ZQ521 when the printer will be dropped, dusted and used with gloves.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra ZQ521 rugged 4-inch mobile printer"
	doc.video_url = VIDEO_ZQ521_LOAD
	doc.hero_trust_chips = "4.09 in / 104 mm · 5 ips draft\nIP54 · MIL-STD 810G\n6.6 ft / 2 m drop\nBluetooth on 3762"
	doc.story_heading = "The rugged 4-inch for the dock and the field"
	doc.visual_story_heading = "ZQ521"
	doc.card_title = "ZQ521"
	doc.card_summary = (
		"Rugged 4-inch ZQ500: MIL-STD 810G, IP54, 6.6 ft drop. This SKU is Bluetooth + LCD."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify ZQ521 for rugged mobile printing"
	doc.final_cta_description = (
		"Confirm Bluetooth vs dual-radio Wi-Fi, standard vs extended battery, and whether "
		"you need the exoskeleton."
	)
	doc.meta_title = "Zebra ZQ521 Rugged Mobile Printer | Printechs"
	doc.meta_description = (
		"Zebra ZQ521 4-inch rugged mobile printer: 203 dpi, Bluetooth, IP54, MIL-STD 810G. "
		"Field, packing and cross-dock from Printechs. Item RET.SYS.ZEB.3762."
	)
	doc.set(
		"benefits",
		[
			{"icon": "rugged", "title": "MIL-STD 810G", "description": "6.6 ft / 2 m to concrete, 1,300 tumbles, IP54. Exoskeleton option: 10 ft / IP65.", "sort_order": 1},
			{"icon": "print", "title": "4-inch draft speed", "description": "4.09 in / 104 mm, up to 5 ips in draft. Dual-sided tear bar.", "sort_order": 2},
			{"icon": "battery", "title": "3250 mAh PP+", "description": "PowerPrecision+ on 3762. Optional 6500 mAh extended pack.", "sort_order": 3},
			{"icon": "durability", "title": "Field HMI", "description": "Large-icon LCD and glove-friendly buttons — not the ZQ600 Plus colour screen.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "ZQ521", "image": photo, "image_alt": "Zebra ZQ521 rugged mobile printer", "caption": "ZQ521 chassis — not ZQ630 Plus, not ZQ511 (3-inch).", "sort_order": 1},
			{"label": "Steel hinge", "image": opened, "image_alt": "ZQ521 open media compartment", "caption": "Center-loading 4-inch path built for repeated open/close in the field.", "sort_order": 2},
			{"label": "Cross-dock", "image": media["packaging"], "image_alt": "Packing and staging", "caption": "Packing, staging and cross-dock labels with gloves on.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "This SKU", "description": "203 dpi · 5 ips draft · 4.09 in", "sort_order": 1},
			{"icon": "rugged", "title": "Rugged", "description": "IP54 · MIL-STD · 6.6 ft", "sort_order": 2},
			{"icon": "connectivity", "title": "On 3762", "description": "Bluetooth · USB OTG", "sort_order": 3},
			{"icon": "battery", "title": "Battery", "description": "3250 mAh PowerPrecision+", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Zebra ZQ521 4-inch rugged mobile (not ZQ511, not ZQ520, not ZQ630 Plus)"),
					("Item on this page", "RET.SYS.ZEB.3762 — 203 dpi, Bluetooth, LCD, 3250 mAh"),
					("Also available", "Dual-radio 802.11ac ZQ521; RFID / linerless ZQ511–ZQ521 options"),
					("Not on this item", "Wi-Fi, colour LCD (ZQ600 Plus), factory RFID encode"),
				],
			),
			(
				"Printing & media",
				[
					("Method / resolution", "Direct thermal, 203 dpi / 8 dots/mm"),
					("Print speed / width", "Up to 5 ips / 127 mm/s in draft; 4.09 in / 104 mm"),
					("Print length", "Up to 39 in"),
					("Media", "ZQ521 4-inch class; black mark and gap sensors (RFID SKUs drop gap)"),
					("Memory / OS", "256 MB RAM, 512 MB Flash typical. Link-OS, ZPL, CPCL"),
					("Tear bar", "Dual-sided tear (not on linerless SKUs)"),
				],
			),
			(
				"Power, I/O & environment",
				[
					("Battery", "3250 mAh PowerPrecision+ on 3762; optional extended pack"),
					("I/O on 3762", "Bluetooth 4.1 EDR + LE, USB On-The-Go"),
					("Optional I/O", "WLAN 802.11ac dual radio on other ZQ521 kits"),
					("Size / weight", "6.2 × 6.1 × 2.6 in (158 × 155 × 67 mm); 1.73 lb / 0.79 kg"),
					("Environment", "IP54. MIL-STD 810G. 6.6 ft / 2 m. 1,300 × 3.3 ft tumbles"),
					("Warranty", "Zebra typically 2-year on ZQ511/ZQ521. OneCare available"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Field & yard", "description": "Labels outside the four walls where IP54 and 6.6 ft drop matter.", "image": media["warehouse"], "image_alt": "Outdoor / yard labelling", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Packing & staging", "description": "Glove-friendly 4-inch labels at pack and staging.", "image": media["packaging"], "image_alt": "Packing station", "industry_link": "packaging", "sort_order": 2},
			{"title": "Cross-dock", "description": "Reprint and exception labels on the dock without a desktop.", "image": media["warehouse"], "image_alt": "Cross-dock labels", "industry_link": "warehouse-logistics", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Load media on a ZQ500-series printer",
				"body": (
					"Distributor film for ZQ500-series clamshell load. This page is the "
					"ZQ521 Bluetooth kit (3762) — 4-inch rugged, not ZQ630 Plus."
				),
				"video_url": VIDEO_ZQ521_LOAD,
				"image": opened,
				"image_alt": "ZQ521 open media compartment",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "ZQ521 versus ZQ630 Plus",
				"body": (
					"Pick ZQ521 for MIL-STD field duty and a simple LCD. Pick ZQ630 Plus "
					"for colour touch-style LCD, 6600 mAh and indoor Plus features. RFID "
					"on a belt is ZQ630 RFID Plus."
				),
				"image": photo,
				"image_alt": "Zebra ZQ521",
				"link_label": "See ZQ630 Plus",
				"link_href": "/products/zebra-zq630-plus",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Installation", "description": "Bluetooth pairing, first 4-inch format and draft-mode check.", "sort_order": 1},
			{"icon": "consumables", "title": "Labels", "description": "4-inch DT media for ZQ521. Exoskeleton and extended battery quoted separately.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Batteries, platens and OneCare in Saudi Arabia.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Load, dual tear bar and glove use in the yard.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "ZQ521 printer (3762 — 203 dpi, Bluetooth, LCD)", "sort_order": 1},
			{"item_description": "3250 mAh PowerPrecision+ battery", "sort_order": 2},
			{"item_description": "Quick-start documentation", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which ZQ521 is this?", "answer": "RET.SYS.ZEB.3762 — 203 dpi, Bluetooth, LCD, 3250 mAh. Wi-Fi dual-radio is another kit.", "sort_order": 1},
			{"question": "Is ZQ521 a 3-inch printer?", "answer": "No. ZQ521 is 4.09 in / 104 mm. The 3-inch rugged sibling is ZQ511. ZQ620 Plus is the 3-inch indoor Plus.", "sort_order": 2},
			{"question": "ZQ521 or ZQ630 Plus?", "answer": "ZQ521 for MIL-STD / 6.6 ft field duty. ZQ630 Plus for colour LCD, 6600 mAh and indoor warehouse Plus features.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def update_zd621r_related():
	name = frappe.db.get_value("Website Product", {"slug": "zebra-zd621r"}, "name")
	if not name:
		return
	doc = frappe.get_doc("Website Product", name)
	set_related(doc, ["zebra-zd621", "zebra-zq630-rfid-plus", "zebra-zt411"])
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	print("Updated ZD621R related products to include ZQ630 RFID Plus")


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
	print("Wired mobile-printer related products")


def fill_zebra_mobile_printers():
	media = _media()
	fill_zq620_plus(media)
	fill_zq630_plus(media)
	fill_zq630_rfid_plus(media)
	fill_zq521(media)
	update_zd621r_related()
	wire_related()
	return "ok"
