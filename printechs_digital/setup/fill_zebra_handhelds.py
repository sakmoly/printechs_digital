# Copyright (c) 2026, Printechs and contributors
"""Create and fill the Printechs Zebra handheld lineup.

TC53e / TC58e — retail & enterprise mobility
TC73 / TC78 — rugged enterprise mobility
MC3400 / MC3450 — warehouse keypad mobility

Official:
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/tc53e-tc53e-rfid-tc58e-spec-sheet-en-us.pdf
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/tc73-tc78-spec-sheet-en-us.pdf
https://www.zebra.com/content/dam/zebra_dam/en/spec-sheets/mc3400-mc3450-spec-sheet-en-us.pdf

Images and YouTube IDs are unique to these pages — do not reuse printer assets.
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

VIDEO_TC53E = "https://youtu.be/WgYJoZfuBdA"  # Barcode Warehouse: TC53e / TC58e
VIDEO_TC73_OV = "https://youtu.be/F2RTBXPp6Bw"  # Official TC73/TC78 overview
VIDEO_TC73_IN = "https://youtu.be/0NONT8Wk3gg"  # Official introducing TC73/TC78
VIDEO_MC34 = "https://youtu.be/-lU7wkDSUPA"  # Official MC3400/MC3450 vs MC3300

IMAGES = {
	"zebra-tc53e-front.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4481/10140/Store-01__73065.1747312206.png",
		],
		"tc53e-store.png",
	),
	"zebra-tc53e-angle.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4481/9535/cq5dam.web.1280.1280_6__90433.1747312206.png",
		],
		"tc53e-b.png",
	),
	"zebra-tc53e-scan.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4481/9534/cq5dam.web.1280.1280_5__43595.1747312178.png",
		],
		"tc53e-a.png",
	),
	"zebra-tc73-front.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4764/10176/Zebra_TC73-01__37843.1750269464.png",
		],
		"tc73-01.png",
	),
	"zebra-tc73-back.png": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4764/10178/Zebra_TC73-02__28009.1750264109.png",
		],
		"tc73-02.png",
	),
	"zebra-mc3400-shooter.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4859/10395/cq5dam.web.1280.1280_1__51221.1766405259.jpg",
		],
		"mc34-1.jpg",
	),
	"zebra-mc3400-gun.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4859/10390/cq5dam.web.1280.1280_6__48981.1766405258.jpg",
		],
		"mc34-6.jpg",
	),
	"zebra-mc3400-gun-scan.jpg": (
		[
			"https://cdn11.bigcommerce.com/s-im2p1/images/stencil/1280x1280/products/4859/10396/cq5dam.web.1280.1280_3__13436.1766405259.jpg",
		],
		"mc34-3.jpg",
	),
}

LINEUP_RELATED = {
	"zebra-tc53e-tc58e": ["zebra-tc73-tc78", "zebra-mc3400-mc3450", "zebra-zq620-plus"],
	"zebra-tc73-tc78": ["zebra-tc53e-tc58e", "zebra-mc3400-mc3450", "zebra-zq630-plus"],
	"zebra-mc3400-mc3450": ["zebra-tc73-tc78", "zebra-tc53e-tc58e", "zebra-zt411"],
}


def _media():
	paths = {}
	for filename, (urls, tmp_name) in IMAGES.items():
		paths[filename] = download_file(filename, urls, tmp_name)
	paths["retail"] = copy_public_image("industry-retail.jpg")
	paths["warehouse"] = copy_public_image("industry-warehouse-logistics.jpg")
	paths["packaging"] = copy_public_image("industry-packaging.jpg")
	return paths


def fill_tc53e_tc58e(media):
	slug = "zebra-tc53e-tc58e"
	item = ""
	card = catalog_card("zebra-tc53e-front.png", "zebra-tc53e-tc58e-card.jpg")
	front = media["zebra-tc53e-front.png"]
	angle = media["zebra-tc53e-angle.png"]
	scan = media["zebra-tc53e-scan.png"]
	doc = get_or_create(slug, "Zebra TC53e / TC58e", item, card, "Mobile Computers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra TC53e / TC58e",
		item=item,
		subcategory="Mobile Computers",
		category_label="RETAIL & ENTERPRISE MOBILITY",
	)
	doc.tagline = "Premium 6-inch TC5e — Wi-Fi 6E, Android, optional 5G and RFID"
	doc.short_description = (
		"Zebra TC53e (WLAN) and TC58e (5G) are Printechs’ premium retail and field-sales "
		"handhelds: 6-inch FHD+ display, Qualcomm 4490, Wi-Fi 6E, Bluetooth 5.3 and "
		"enterprise scanning. Inventory, price check, receiving, fulfilment and van sales."
	)
	doc.long_description = (
		"<p>TC53e / TC58e is the current TC5 Series for the sales floor and the van. Official "
		"display is 6.0 in FHD+ (1080 × 2160, 600 nits), CPU is Qualcomm 4490 octa-core at "
		"2.4 GHz, and wireless is Wi-Fi 6E plus Bluetooth 5.3. TC53e is WLAN. "
		"<strong>TC58e adds 2nd-generation 5G</strong> (nano SIM + eSIM). Memory options are "
		"6 GB / 64 GB or 8 GB / 128 GB. Standard battery is 4680 mAh PowerPrecision+ with "
		"warm swap; 7000 mAh extended, BLE and Qi wireless-charge packs are options.</p>"
		"<p>Scan engines on the e-series are SE4720, SE55 IntelliFocus, or SE4770 on TC58e. "
		"IP65 / IP68. Drop is 6 ft / 1.8 m to tile over concrete stand-alone (8 ft / 2.4 m "
		"to concrete with boot). TC53e-RFID is a separate short-range UHF SKU — not on the "
		"standard TC53e/TC58e.</p>"
		"<p>Printechs does not yet list a TC53e/TC58e Item. <strong>RET.SYS.ZEB.4537 is "
		"TC53 (not e)</strong> — WLAN, 4 GB / 64 GB, SE4720, 4680 mAh. Do not treat 4537 as "
		"an e-series or 5G device. Quote TC53e for Wi-Fi 6E retail, TC58e for 5G field sales. "
		"Step up to TC73/TC78 for 10 ft ultra-rugged logistics, or MC3400 when pickers need "
		"a physical keypad.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra TC53e 6-inch enterprise handheld, front view"
	doc.video_url = VIDEO_TC53E
	doc.hero_trust_chips = "6-inch FHD+ · 600 nits\nWi-Fi 6E · BT 5.3\nTC58e = 5G\nQualcomm 4490 · Android"
	doc.story_heading = "The TC5e in the store and on the route"
	doc.visual_story_heading = "TC53e / TC58e"
	doc.card_title = "TC53e / TC58e"
	doc.card_summary = (
		"Premium 6-inch retail and field handheld. Wi-Fi 6E; TC58e adds 5G. Not the TC53 4537."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify TC53e or TC58e for store mobility"
	doc.final_cta_description = (
		"Printechs will confirm WLAN vs 5G, SE4720 vs SE55, 6/64 vs 8/128, and whether "
		"you need TC53e-RFID or the stocked TC53 (4537)."
	)
	doc.meta_title = "Zebra TC53e / TC58e Handheld | Printechs"
	doc.meta_description = (
		"Zebra TC53e and TC58e 6-inch enterprise handhelds: Wi-Fi 6E, Android, optional 5G. "
		"Retail inventory, price check and field sales from Printechs."
	)
	doc.set(
		"benefits",
		[
			{"icon": "android", "title": "TC5e platform", "description": "Qualcomm 4490, Android enterprise, 6-inch FHD+. Nearly 2× the prior TC5 CPU class.", "sort_order": 1},
			{"icon": "connectivity", "title": "Wi-Fi 6E and 5G", "description": "TC53e is WLAN + BT 5.3. TC58e adds 2nd-gen 5G. Radios are model choices, not field cards.", "sort_order": 2},
			{"icon": "scan", "title": "Enterprise scan", "description": "SE4720, SE55 IntelliFocus, or SE4770 on TC58e. Optional TC53e-RFID is a different SKU.", "sort_order": 3},
			{"icon": "store", "title": "Retail & van sales", "description": "Inventory, price check, receiving, stock lookup, fulfilment and field service.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "TC53e / TC58e", "image": front, "image_alt": "Zebra TC53e front", "caption": "6-inch e-series handheld — not TC73, not MC3400.", "sort_order": 1},
			{"label": "In hand", "image": angle, "image_alt": "TC53e angled view", "caption": "Green scan button and 6-inch FHD+ for the sales floor.", "sort_order": 2},
			{"label": "Scan window", "image": scan, "image_alt": "TC53e top scan engine", "caption": "SE4720 or SE55 on TC53e; SE4770 option on TC58e.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "display", "title": "Display", "description": "6 in FHD+ · 600 nits · Gorilla", "sort_order": 1},
			{"icon": "connectivity", "title": "Wireless", "description": "Wi-Fi 6E · BT 5.3 · TC58e 5G", "sort_order": 2},
			{"icon": "battery", "title": "Battery", "description": "4680 mAh PP+ · warm swap", "sort_order": 3},
			{"icon": "rugged", "title": "Duty", "description": "IP65/68 · 6 ft stand-alone", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Models", "Zebra TC53e (WLAN) and TC58e (5G). TC53e-RFID is a separate short-range UHF SKU"),
					("Item on this page", "No e-series Item yet — quote TC53e or TC58e. Do not treat 4537 as e-series"),
					("Stocked TC5 sibling", "RET.SYS.ZEB.4537 = TC53 (not e): WLAN, 4 GB/64 GB, SE4720, 4680 mAh"),
					("Not this page", "TC73/TC78 ultra-rugged, MC3400 keypad, TC22"),
				],
			),
			(
				"Compute, display & capture",
				[
					("CPU / OS", "Qualcomm 4490 Kryo octa-core 2.4 GHz. Android (see zebra.com/android-versions)"),
					("Memory", "6 GB/64 GB or 8 GB/128 GB UFS — confirm on the quote"),
					("Display", "6.0 in FHD+ 1080 × 2160, 600 nits, optically bonded, Gorilla Glass"),
					("Scanning", "SE4720 or SE55 IntelliFocus; SE4770 on TC58e only"),
					("Cameras", "Typical TC5e class: 16 MP rear, 8 MP front (confirm SKU)"),
					("Size / weight", "6.48 × 3.04 × 0.66 in (165 × 77 × 17 mm); 9.9 oz / 282 g with std battery"),
				],
			),
			(
				"Wireless, power & environment",
				[
					("WLAN / BT", "Wi-Fi 6E (802.11ax) 2×2 MU-MIMO; Bluetooth 5.3 + secondary BLE"),
					("WWAN", "TC58e only: 2nd-gen 5G, 1 nano SIM + 1 eSIM. Not on TC53e or 4537"),
					("Battery", "4680 mAh PP+ standard; 7000 mAh extended; BLE or Qi packs optional"),
					("Sealing / drop", "IP65 and IP68. 6 ft / 1.8 m stand-alone; 8 ft / 2.4 m with boot"),
					("Tumble", "1000 × 1.6 ft without boot; 1000 × 3.2 ft with boot"),
					("Warranty", "Zebra 1-year limited. OneCare and LifeGuard available"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Inventory & price check", "description": "Scan the bay, correct the price, move on — 6-inch screen for the associate.", "image": media["retail"], "image_alt": "Retail inventory", "industry_link": "retail", "sort_order": 1},
			{"title": "Receiving & fulfilment", "description": "Store receiving, stock lookup and BOPIS / order fulfilment on WLAN or 5G.", "image": media["retail"], "image_alt": "Store receiving", "industry_link": "retail", "sort_order": 2},
			{"title": "Van sales & field service", "description": "TC58e 5G for routes that leave the store Wi-Fi.", "image": media["warehouse"], "image_alt": "Field sales", "industry_link": "warehouse-logistics", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "TC53e and TC58e on the floor",
				"body": (
					"Distributor film covering TC53e / TC58e Wi-Fi and 5G mobility. This page "
					"is the e-series — not RET.SYS.ZEB.4537 (TC53) and not TC73."
				),
				"video_url": VIDEO_TC53E,
				"image": front,
				"image_alt": "Zebra TC53e",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "When to step up from TC5e",
				"body": (
					"Stay on TC53e/TC58e for retail and van sales. Choose TC73/TC78 for "
					"10 ft / IP68 warehouse and outdoor duty. Choose MC3400/MC3450 when "
					"pickers still want a physical keypad."
				),
				"image": angle,
				"image_alt": "TC53e handheld",
				"link_label": "See TC73 / TC78",
				"link_href": "/products/zebra-tc73-tc78",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Deployment", "description": "StageNow, WLAN/5G and first inventory or price-check app.", "sort_order": 1},
			{"icon": "device", "title": "Accessories", "description": "TC53/TC58/TC53e shared cradles, boots and trigger handles in ERP.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "Batteries, boots and OneCare in Saudi Arabia.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Scan buttons, warm-swap and Mobility DNA basics.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "TC53e or TC58e handheld (configuration as quoted)", "sort_order": 1},
			{"item_description": "4680 mAh PowerPrecision+ battery (typical)", "sort_order": 2},
			{"item_description": "Quick-start documentation (cradle and boot quoted separately)", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Is this the same as RET.SYS.ZEB.4537?", "answer": "No. 4537 is TC53 (not e): 4 GB/64 GB, SE4720, WLAN only. This page is TC53e/TC58e. Quote the e-series when you want 4490, 6/64 or 8/128, and optional 5G.", "sort_order": 1},
			{"question": "TC53e or TC58e?", "answer": "TC53e is Wi-Fi 6E inside the four walls. TC58e adds 2nd-generation 5G for van sales and field service.", "sort_order": 2},
			{"question": "Does it include RFID?", "answer": "Standard TC53e/TC58e do not. TC53e-RFID is a separate short-range UHF model. RFD40/RFD90 sleds are accessories.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_tc73_tc78(media):
	slug = "zebra-tc73-tc78"
	item = "RET.SYS.ZEB.4551"
	card = catalog_card("zebra-tc73-front.png", "zebra-tc73-tc78-card.jpg")
	front = media["zebra-tc73-front.png"]
	back = media["zebra-tc73-back.png"]
	doc = get_or_create(slug, "Zebra TC73 / TC78", item, card, "Mobile Computers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra TC73 / TC78",
		item=item,
		subcategory="Mobile Computers",
		category_label="RUGGED ENTERPRISE MOBILITY",
	)
	doc.tagline = "Ultra-rugged 6-inch — 10 ft drop, IP65/IP68, Wi-Fi 6E, TC78 5G"
	doc.short_description = (
		"Zebra TC73/TC78 sits above TC53e/TC58e for demanding logistics, outdoor and "
		"warehouse work. This page is linked to the TC73 WLAN kit. TC78 is the 5G sibling."
	)
	doc.long_description = (
		"<p>TC73 and TC78 are Zebra’s premium rugged handhelds: thinner grip, 6-inch FHD+ "
		"display, Qualcomm 6490 at 2.7 GHz, Wi-Fi 6E and Bluetooth 5.2. Official drop is "
		"10 ft / 3.05 m to concrete at room temp (MIL-STD 810H) and 8 ft / 2.4 m across "
		"operating temperature, plus 2,000 tumbles from 3.3 ft. Sealing is IP65 and IP68.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.4551</strong> — TC73, WLAN, 6.0-inch, Wi-Fi 6E, "
		"4 GB / 64 GB, SE4770, 8 MP front / 16 MP rear, warm swap, 4680 mAh, GMS, ROW. "
		"<strong>RET.SYS.ZEB.4843 is TC78</strong> — WAN Sub-6 5G, 8 GB / 128 GB, SE4770, "
		"wireless-charge enabled, 4680 mAh. SE55 IntelliFocus (to ~40 ft) is a family option, "
		"not on 4551 or 4843.</p>"
		"<p>Use TC53e/TC58e for retail and van sales. Use MC3400/MC3450 when the warehouse "
		"still wants a keypad. Pair TC73 with ZQ630 Plus when labels print on the same cart.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra TC73 ultra-rugged handheld with protective boot"
	doc.video_url = VIDEO_TC73_OV
	doc.hero_trust_chips = "10 ft / 3.05 m drop\nIP65 + IP68\nWi-Fi 6E · TC78 = 5G\nSE4770 on 4551 / 4843"
	doc.story_heading = "The rugged TC7 above the TC5e"
	doc.visual_story_heading = "TC73 / TC78"
	doc.card_title = "TC73 / TC78"
	doc.card_summary = (
		"Ultra-rugged 6-inch logistics handheld. This SKU is TC73 WLAN 4/64 SE4770. TC78 is 5G."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify TC73 or TC78 for rugged mobility"
	doc.final_cta_description = (
		"Confirm WLAN vs 5G, 4/64 vs 8/128, SE4770 vs SE55, and standard vs wireless-charge battery."
	)
	doc.meta_title = "Zebra TC73 / TC78 Rugged Handheld | Printechs"
	doc.meta_description = (
		"Zebra TC73 and TC78 ultra-rugged handhelds: 10 ft drop, IP68, Wi-Fi 6E. TC73 WLAN "
		"kit RET.SYS.ZEB.4551. TC78 5G is 4843. From Printechs."
	)
	doc.set(
		"benefits",
		[
			{"icon": "rugged", "title": "Above TC5e", "description": "10 ft / 3.05 m to concrete, 2,000 tumbles, IP65/IP68. Thinner grip than prior TC7X.", "sort_order": 1},
			{"icon": "android", "title": "6490 class", "description": "Qualcomm 6490 octa-core 2.7 GHz. 4/64 on 4551; 8/128 on TC78 4843.", "sort_order": 2},
			{"icon": "scan", "title": "SE4770 on these kits", "description": "Standard range on 4551 and 4843. SE55 to ~40 ft / 12.2 m is another engine.", "sort_order": 3},
			{"icon": "connectivity", "title": "Wi-Fi 6E / 5G", "description": "TC73 is WLAN. TC78 4843 adds Sub-6 5G and wireless-charge battery support.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "TC73", "image": front, "image_alt": "Zebra TC73 front with boot", "caption": "Booted TC73 — 6-inch FHD+. Not the slimmer TC53e.", "sort_order": 1},
			{"label": "Ultra-rugged back", "image": back, "image_alt": "TC73 rear and battery door", "caption": "Sealed battery door, warm swap on 4551, dual scan buttons.", "sort_order": 2},
			{"label": "Warehouse", "image": media["warehouse"], "image_alt": "Warehouse logistics", "caption": "Dock, yard and outdoor routes where 10 ft drop matters.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "rugged", "title": "Rugged", "description": "10 ft · IP65/68 · 2000 tumbles", "sort_order": 1},
			{"icon": "display", "title": "Display", "description": "6 in FHD+ · glove / wet touch", "sort_order": 2},
			{"icon": "connectivity", "title": "On 4551", "description": "Wi-Fi 6E · BT 5.2 · USB-C", "sort_order": 3},
			{"icon": "battery", "title": "Battery", "description": "4680 mAh · 7000 mAh option", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Models", "TC73 (WLAN) and TC78 (5G). This page is not TC53e and not TC72/TC77"),
					("Item on this page", "RET.SYS.ZEB.4551 — TC73, Wi-Fi 6E, 4 GB/64 GB, SE4770, 4680 mAh"),
					("Also available", "4843 = TC78 5G, 8 GB/128 GB, SE4770, wireless charging enabled"),
					("Not on 4551 / 4843", "SE55 IntelliFocus, 7000 mAh pack (optional), keypad (that is MC3400)"),
				],
			),
			(
				"Compute, display & capture",
				[
					("CPU / OS", "Qualcomm 6490 octa-core 2.7 GHz. Android (see zebra.com/android-versions)"),
					("Memory", "4 GB/64 GB on 4551; 8 GB/128 GB on 4843; microSD up to 2 TB"),
					("Display", "6.0 in FHD+ 1080 × 2160, optically bonded, Gorilla Glass, glove/wet"),
					("Scanning", "SE4770 on both listed items. SE55 to ~40 ft is a family option"),
					("Cameras", "8 MP front, 16 MP rear on 4551 and 4843. OIS/ToF are premium SKUs"),
					("Size / weight", "6.96 × 3.38 × 1.12 in (177 × 86 × 28 mm); 12.3 oz / 349 g std battery"),
				],
			),
			(
				"Wireless, power & environment",
				[
					("WLAN / BT", "Wi-Fi 6E 2×2 MU-MIMO; Bluetooth 5.2 + secondary BLE"),
					("WWAN", "TC78 only (4843): Sub-6 5G, nano SIM + eSIM. Not on TC73 4551"),
					("Battery", "4680 mAh PP+ on these kits; 7000 mAh, BLE and Qi packs optional"),
					("Sealing / drop", "IP65 and IP68. 10 ft / 3.05 m room temp; 8 ft / 2.4 m across temp"),
					("Tumble", "2000 × 3.3 ft / 1.0 m"),
					("Warranty", "Zebra 1-year limited. OneCare and LifeGuard available"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Warehouse & DC", "description": "Receiving, put-away and pick on a device built for concrete and hoses.", "image": media["warehouse"], "image_alt": "Warehouse handheld use", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Outdoor logistics", "description": "Yard, under-wing and DSD routes — IP68 and 10 ft drop.", "image": media["warehouse"], "image_alt": "Outdoor logistics", "industry_link": "warehouse-logistics", "sort_order": 2},
			{"title": "Pack & ship", "description": "Scan every label on the carton; pair with ZQ630 Plus on the same cart.", "image": media["packaging"], "image_alt": "Packing scan", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "TC73 / TC78 product overview",
				"body": (
					"Official Zebra overview of the ultra-rugged TC73/TC78. This page is "
					"RET.SYS.ZEB.4551 (TC73 WLAN, SE4770). 5G is TC78 4843."
				),
				"video_url": VIDEO_TC73_OV,
				"image": front,
				"image_alt": "Zebra TC73",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Why Zebra introduced TC73 / TC78",
				"body": (
					"Official introduction film. Choose TC73/TC78 over TC53e when drop, "
					"IP68 and outdoor duty come first. Choose MC3400 when the job is keypad pick."
				),
				"video_url": VIDEO_TC73_IN,
				"image": back,
				"image_alt": "TC73 rear",
				"link_label": "See MC3400 / MC3450",
				"link_href": "/products/zebra-mc3400-mc3450",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Deployment", "description": "WLAN or 5G, StageNow and first WMS / TE session.", "sort_order": 1},
			{"icon": "device", "title": "Accessories", "description": "Shared TC73/TC78 boots, holsters and RFD90 cups in ERP.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "4680/7000 mAh packs, windows and OneCare in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "Warm swap, dual scan keys and Mobility DNA.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "TC73 handheld (4551 — WLAN, 4/64, SE4770) or TC78 as quoted", "sort_order": 1},
			{"item_description": "4680 mAh PowerPrecision+ battery", "sort_order": 2},
			{"item_description": "Quick-start documentation (boot and cradle quoted separately)", "sort_order": 3},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which TC73 is this?", "answer": "RET.SYS.ZEB.4551 — WLAN, 4 GB/64 GB, SE4770, 4680 mAh. TC78 5G 8/128 is 4843.", "sort_order": 1},
			{"question": "Why not TC53e?", "answer": "TC53e is the retail/field 6-inch. TC73/TC78 is 10 ft, IP68 and built for warehouse and outdoor logistics.", "sort_order": 2},
			{"question": "Does 4551 include 5G or SE55?", "answer": "No. 5G is TC78 4843. SE55 long-range is a different engine — ask if you need ~40 ft scans.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


def fill_mc3400_mc3450(media):
	slug = "zebra-mc3400-mc3450"
	item = "RET.SYS.ZEB.5050"
	card = catalog_card("zebra-mc3400-shooter.jpg", "zebra-mc3400-mc3450-card.jpg")
	shooter = media["zebra-mc3400-shooter.jpg"]
	gun = media["zebra-mc3400-gun.jpg"]
	gun_scan = media["zebra-mc3400-gun-scan.jpg"]
	doc = get_or_create(slug, "Zebra MC3400 / MC3450", item, card, "Mobile Computers")
	apply_identity(
		doc,
		slug=slug,
		display_name="Zebra MC3400 / MC3450",
		item=item,
		subcategory="Mobile Computers",
		category_label="WAREHOUSE KEYPAD MOBILITY",
	)
	doc.tagline = "Physical keypad handhelds — 29 / 38 / 47 key, Wi-Fi 6E, MC3450 5G"
	doc.short_description = (
		"Zebra MC3400/MC3450 is the keypad warehouse computer so the site is not "
		"touch-screen only. This page is the MC3400 straight-shooter 38-key kit. "
		"Gun and 5G MC3450 are other configurations."
	)
	doc.long_description = (
		"<p>Many warehouse teams still pick faster on a physical keypad than on glass. "
		"MC3400 (WLAN) and MC3450 (5G, data only) continue the MC3000 family with a "
		"4-inch WVGA display, Qualcomm 4490, Wi-Fi 6E and a choice of 29-key numeric, "
		"38-key function-numeric or 47-key alphanumeric. Form factors are straight shooter "
		"or gun. Standard battery is 7000 mAh with hot-swap backup.</p>"
		"<p>This page is <strong>RET.SYS.ZEB.5050</strong> — MC3400 straight shooter, "
		"Wi-Fi 6E, 4 GB / 64 GB, 38-key, SE4710, 7000 mAh, software licence included. "
		"<strong>RET.SYS.ZEB.4629 is an MC34 gun</strong> — WLAN, 6 GB / 64 GB, 47-key, "
		"SE4770, 7000 mAh. There is no MC3450 (WWAN 5G) Item in ERP yet — quote it when "
		"the site needs cellular.</p>"
		"<p>Official rugged ratings: 8 ft / 2.4 m to concrete at room temp, 6 ft / 1.8 m "
		"across temperature, 4,000 tumbles from 3.3 ft, IP65 and IP67. Accessories are "
		"backward-compatible with MC3300 / MC3300x / MC3300ax chargers and batteries.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Zebra MC3400 straight-shooter handheld with physical keypad"
	doc.video_url = VIDEO_MC34
	doc.hero_trust_chips = "29 / 38 / 47-key keypad\nStraight shooter or gun\nWi-Fi 6E · MC3450 = 5G\n7000 mAh · IP65/67"
	doc.story_heading = "Keypad mobility for the warehouse"
	doc.visual_story_heading = "MC3400 / MC3450"
	doc.card_title = "MC3400 / MC3450"
	doc.card_summary = (
		"Warehouse keypad computer. This SKU is MC3400 38-key straight shooter SE4710 (5050)."
	)
	doc.card_image = card
	doc.final_cta_heading = "Specify MC3400 or MC3450 for keypad pick"
	doc.final_cta_description = (
		"Confirm 38- vs 47- vs 29-key, shooter vs gun, SE4710 vs SE4770, and WLAN vs 5G."
	)
	doc.meta_title = "Zebra MC3400 / MC3450 Keypad Handheld | Printechs"
	doc.meta_description = (
		"Zebra MC3400 and MC3450 warehouse keypad handhelds: 38- or 47-key, Wi-Fi 6E, "
		"optional 5G. Item RET.SYS.ZEB.5050. From Printechs."
	)
	doc.set(
		"benefits",
		[
			{"icon": "inventory", "title": "Physical keypad", "description": "29-, 38- or 47-key. This kit is 38-key. Gun 4629 is 47-key. Gloves welcome.", "sort_order": 1},
			{"icon": "scan", "title": "SE4710 on 5050", "description": "Straight-shooter SE4710. Gun 4629 is SE4770. SE55/SE58 are long-range options.", "sort_order": 2},
			{"icon": "battery", "title": "7000 mAh", "description": "Standard 7000 mAh on 5050 and 4629, with hot-swap session persistence.", "sort_order": 3},
			{"icon": "rugged", "title": "MC3 duty", "description": "8 ft room-temp drop, 4,000 tumbles, IP65/IP67. MC33 accessory compatible.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "MC3400 shooter", "image": shooter, "image_alt": "MC3400 straight shooter with keypad", "caption": "5050 — 38-key straight shooter. Not a touch-only TC5/TC7.", "sort_order": 1},
			{"label": "Gun / 47-key", "image": gun, "image_alt": "MC34 gun with keypad", "caption": "4629 is the WLAN gun, 47-key, SE4770, 6 GB/64 GB.", "sort_order": 2},
			{"label": "Scan window", "image": gun_scan, "image_alt": "MC34 gun scan engine", "caption": "Trigger scan on gun; side scan keys on the straight shooter.", "sort_order": 3},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "inventory", "title": "This SKU", "description": "38-key · shooter · SE4710", "sort_order": 1},
			{"icon": "display", "title": "Display", "description": "4 in WVGA · 800 × 480", "sort_order": 2},
			{"icon": "connectivity", "title": "On 5050", "description": "Wi-Fi 6E · BT · USB", "sort_order": 3},
			{"icon": "battery", "title": "Battery", "description": "7000 mAh · hot swap", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Models", "MC3400 (WLAN) and MC3450 (5G data). Straight shooter or gun"),
					("Item on this page", "RET.SYS.ZEB.5050 — MC3400 shooter, Wi-Fi 6E, 4/64, 38-key, SE4710"),
					("Also available", "4629 = MC34 gun, WLAN, 6/64, 47-key, SE4770, 7000 mAh"),
					("Not in ERP yet", "MC3450 WWAN 5G. 29-key numeric is a family keypad option"),
				],
			),
			(
				"Compute, keypad & capture",
				[
					("CPU / OS", "Qualcomm 4490 octa-core 2.4 GHz. Android (see zebra.com/android-versions)"),
					("Memory", "4 GB/64 GB on 5050; 6 GB/64 GB on 4629"),
					("Display", "4.0 in WVGA 800 × 480 (350–600 nits by configuration)"),
					("Keypad", "5050 = 38-key; 4629 = 47-key; 29-key numeric also offered"),
					("Scanning", "SE4710 on 5050; SE4770 on 4629. SE55 / SE58 are long-range options"),
					("Cameras", "5 MP front, 13 MP rear (family). Confirm if required on the kit"),
				],
			),
			(
				"Wireless, power & environment",
				[
					("WLAN / BT", "Wi-Fi 6E and Bluetooth on both listed items"),
					("WWAN", "MC3450 only: 5G data, nano SIM + eSIM, GNSS. Not on 5050 or 4629"),
					("Battery", "7000 mAh standard; optional BLE 7000 mAh; hot-swap backup"),
					("Size / weight", "Shooter 8.2 × 2.9 × 1.5 in, 15.6 oz. Gun 8.2 × 2.9 × 6.5 in, 18.6 oz"),
					("Sealing / drop", "IP65 and IP67. 8 ft / 2.4 m room temp; 6 ft / 1.8 m across temp"),
					("Tumble / warranty", "4000 × 3.3 ft. Zebra 1-year limited. MC34XX OneCare 5043"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Picking", "description": "Enter qty on the 38- or 47-key pad without looking down at glass.", "image": media["warehouse"], "image_alt": "Warehouse picking", "industry_link": "warehouse-logistics", "sort_order": 1},
			{"title": "Inventory / cycle count", "description": "Keyed adjustments and scan-heavy counts on a gun or shooter.", "image": media["warehouse"], "image_alt": "Cycle count", "industry_link": "warehouse-logistics", "sort_order": 2},
			{"title": "Packing", "description": "Confirm SKU and qty at the pack station with a real keypad.", "image": media["packaging"], "image_alt": "Packing keypad", "industry_link": "packaging", "sort_order": 3},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "MC3400 / MC3450 — the MC3300 upgrade",
				"body": (
					"Official Zebra film: MC3400/MC3450 as the keypad upgrade from MC3300. "
					"This page is RET.SYS.ZEB.5050 (38-key shooter). Gun 47-key is 4629."
				),
				"video_url": VIDEO_MC34,
				"image": shooter,
				"image_alt": "Zebra MC3400 straight shooter",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Keypad versus all-touch",
				"body": (
					"Keep MC3400 on the pick line. Use TC73/TC78 when the job is all-touch "
					"and 10 ft rugged. Use TC53e/TC58e in the store. The website is not "
					"touch-screen handhelds only."
				),
				"image": gun,
				"image_alt": "MC34 gun keypad",
				"link_label": "See TC73 / TC78",
				"link_href": "/products/zebra-tc73-tc78",
				"sort_order": 2,
			},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Deployment", "description": "Keypad map, WMS/TE and first pick walk.", "sort_order": 1},
			{"icon": "device", "title": "Accessories", "description": "MC33/MC34 shared four-slot chargers (5042) and holsters.", "sort_order": 2},
			{"icon": "maintenance", "title": "Service", "description": "7000 mAh packs and MC34XX OneCare 5043 in KSA.", "sort_order": 3},
			{"icon": "training", "title": "Training", "description": "38- vs 47-key layers, side scan keys and hot-swap.", "sort_order": 4},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "MC3400 straight shooter (5050 — 38-key, SE4710, Wi-Fi 6E)", "sort_order": 1},
			{"item_description": "7000 mAh battery", "sort_order": 2},
			{"item_description": "Software licence (as supplied on 5050)", "sort_order": 3},
			{"item_description": "Quick-start documentation", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set(
		"faq_items",
		[
			{"question": "Which MC3400 is this?", "answer": "RET.SYS.ZEB.5050 — straight shooter, 38-key, 4 GB/64 GB, SE4710, Wi-Fi 6E. Gun 47-key SE4770 is 4629.", "sort_order": 1},
			{"question": "Where is MC3450?", "answer": "MC3450 is the 5G (data) family model. No MC3450 Item is listed yet — ask for a WWAN quote. 5050 and 4629 are WLAN.", "sort_order": 2},
			{"question": "Why not a TC73?", "answer": "TC73 is all-touch ultra-rugged. MC3400 exists so pickers keep a physical keypad. Many DCs still prefer keys for qty entry.", "sort_order": 3},
		],
	)
	return save_product(doc, card)


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
	print("Wired handheld related products")


def fill_zebra_handhelds():
	media = _media()
	fill_tc53e_tc58e(media)
	fill_tc73_tc78(media)
	fill_mc3400_mc3450(media)
	wire_related()
	return "ok"
