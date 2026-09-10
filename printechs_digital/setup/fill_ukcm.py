# Copyright (c) 2026, Printechs and contributors
"""UKCM coding & marking cluster for Printechs.

Laser hub + KF130 fiber + KC130 CO2 + KU110 UV + KT7 + KT10 + hand coder.
Official sources: uk-cm.uk, attached TIJ-KT-10 brochure, 3S Ink KT7/KT10 listings,
Kenjiete KC130/KU110 datasheets, Desk items under Kezojet / UKCM.

Do not mix KT7 speeds onto KT10, or laser wavelengths onto the wrong page.
"""

import frappe

from printechs_digital.setup.ukcm_common import (
	KSA_BODY,
	VIDEO_KT10_ACCESS,
	VIDEO_KT10_INTRO,
	VIDEO_KT10_PIPE,
	VIDEO_KT10_SETUP,
	apply_brochure,
	apply_identity,
	get_or_create,
	ksa_section,
	prepare_media,
	save_product,
	scene_apps,
	set_related,
	set_specs,
	support_items,
)

RELATED = {
	"ukcm-laser": ["ukcm-fiber-laser", "ukcm-co2-laser", "ukcm-uv-laser", "ukcm-kt10"],
	"ukcm-fiber-laser": ["ukcm-co2-laser", "ukcm-uv-laser", "ukcm-laser"],
	"ukcm-co2-laser": ["ukcm-fiber-laser", "ukcm-uv-laser", "ukcm-laser"],
	"ukcm-uv-laser": ["ukcm-fiber-laser", "ukcm-co2-laser", "ukcm-laser"],
	"ukcm-kt7": ["ukcm-kt10", "ukcm-hand-coder", "ukcm-laser"],
	"ukcm-kt10": ["ukcm-kt7", "ukcm-hand-coder", "ukcm-laser"],
	"ukcm-hand-coder": ["ukcm-kt7", "ukcm-kt10", "ukcm-laser"],
}


def _p() -> str:
	return f"<p>{KSA_BODY}</p>"


def fill_laser_hub(media):
	slug = "ukcm-laser"
	card = media["hub"]
	doc = get_or_create(slug, "UKCM Laser Marking Range", card)
	apply_identity(
		doc,
		slug=slug,
		display_name="UKCM Laser Marking Range",
		category_label="LASER MARKING",
		subcategory="Laser Marking",
		featured=1,
		is_hub=1,
	)
	doc.tagline = "Fiber, CO2 and UV — permanent codes without ink."
	doc.short_description = (
		"UKCM laser marking for Saudi factories: fiber on metals, CO2 on packs and PET, "
		"UV on delicate plastics and foil. Printechs specifies the wavelength to the line."
	)
	doc.long_description = (
		"<p>UKCM (UK Coding &amp; Marking) builds flying laser markers for industrial "
		"identification — lot, expiry, serial, barcode and 2D — without a wet ink circuit. "
		"The official range on <a href=\"https://uk-cm.uk/laser-marking-machine/\">uk-cm.uk</a> "
		"is CO2, fiber, UV and a handheld laser. This page is the range; each wavelength "
		"has its own product page.</p>"
		"<p><strong>How to choose.</strong> "
		"<a href=\"/products/ukcm-fiber-laser\">Fiber (KF130)</a> — metals, some hard plastics, "
		"cable and automotive parts. "
		"<a href=\"/products/ukcm-co2-laser\">CO2 (KC130)</a> — cartons, PET, wood and many "
		"organic packs. "
		"<a href=\"/products/ukcm-uv-laser\">UV (KU110)</a> — foil, medical plastics and fine "
		"electronics marks. A 30 W handheld fiber (KFH130) can be quoted when the part "
		"cannot come to a fixed head. Do not treat those as one SKU.</p>"
		"<p>UKCM cites high-speed marking (up to 600 characters/s on their laser guide), "
		"long source life, a small spot and MES/ERP integration. We still survey the "
		"substrate and code before we lock power and lens.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM fiber, CO2 and UV laser marking heads"
	doc.video_url = ""
	doc.hero_trust_chips = "Fiber · CO2 · UV\nNo ink circuit\nFlying or static mark\nRiyadh · Jeddah · Dammam"
	doc.story_heading = "Pick the laser by material — not by brochure headline"
	doc.visual_story_heading = "Three wavelengths, one Saudi installer"
	doc.card_title = "Laser range"
	doc.card_summary = "UKCM fiber, CO2 and UV laser markers specified and installed by Printechs."
	doc.card_image = card
	doc.final_cta_heading = "Specify a UKCM laser for your line"
	doc.final_cta_description = "Tell us the pack, speed and code. We will map KF130, KC130 or KU110."
	doc.meta_title = "UKCM Laser Marking Machines Saudi Arabia | Fiber, CO2, UV | Printechs"
	doc.meta_description = (
		"UKCM fiber, CO2 and UV laser marking in Saudi Arabia. Permanent lot, expiry and "
		"2D codes — specified and installed by Printechs."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "Permanent, no ink", "description": "Engrave, anneal or colour-change the surface. No makeup, no cartridge decap.", "sort_order": 1},
		{"icon": "speed", "title": "Line-speed marking", "description": "Flying mark with photocell or encoder. UKCM cites up to 600 characters/s on the laser guide.", "sort_order": 2},
		{"icon": "scan", "title": "Traceable codes", "description": "Text, logos, Code 39/128 and QR sized to the part — not a paper label that peels.", "sort_order": 3},
		{"icon": "shield", "title": "Harsh environments", "description": "Marks that stay readable through wash-down, heat and handling when the process is right.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Range", "image": media["laser-range"], "image_alt": "Fiber, CO2 and UV heads", "caption": "Specify one wavelength per substrate family.", "sort_order": 1},
		{"label": "Fiber", "image": media["fiber"], "image_alt": "KF130 fiber laser", "caption": "KF130 30 W flying fiber — metals and cable.", "sort_order": 2},
		{"label": "CO2", "image": media["co2"], "image_alt": "KC130 CO2 laser", "caption": "KC130 30 W — PET, carton and organics.", "sort_order": 3},
		{"label": "UV", "image": media["uv"], "image_alt": "KU110 UV laser", "caption": "KU110 10 W — foil and delicate plastics.", "sort_order": 4},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "Fiber KF130", "description": "30 W · metals & cable", "sort_order": 1},
		{"icon": "print", "title": "CO2 KC130", "description": "30 W · 10.6 µm · packs", "sort_order": 2},
		{"icon": "print", "title": "UV KU110", "description": "10 W · 355 nm · foil", "sort_order": 3},
		{"icon": "display", "title": "Linux HMI", "description": "10.2-inch family controller", "sort_order": 4},
	])
	set_specs(doc, [
		("Range", [
			("Brand", "UKCM (UK Coding & Marking) — supplied by Printechs"),
			("Fiber", "KF130 30 W flying marker; 60 W JPT MOPA + Scanlab can be quoted"),
			("CO2", "KC130 30 W, 10600 nm, air-cooled (Kenjiete KC130 listing)"),
			("UV", "KU110 10 W, 355 nm (Kenjiete KU110 listing)"),
			("Handheld laser", "KFH130 30 W mobile fiber — quoted when the part cannot reach a fixed head"),
			("Not on this page", "TIJ KT7 / KT10 and the hand coder have their own pages"),
		]),
		("Typical outcomes", [
			("Codes", "Lot, expiry, serial, logo, Code 39/128, QR"),
			("Integration", "Photocell, encoder, start/status I/O — survey required"),
			("Consumables", "No ink; fume extraction and safety interlocks are specified per site"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Wavelength first, then power",
			"body": (
				"A cheaper 30 W fiber will not mark a PET bottle the way KC130 does. "
				"UV will not anneal stainless like KF130. We lock the page to the "
				"substrate samples you send — then quote the matching Item."
			),
			"image": media["laser-lines"],
			"image_alt": "UKCM lasers on mixed production lines",
			"link_label": "Fiber KF130",
			"link_href": "/products/ukcm-fiber-laser",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items("Safety & extraction"))
	doc.set("package_contents", [
		{"item_description": "Quoted UKCM laser head, controller and focusing lens", "sort_order": 1},
		{"item_description": "Photocell / encoder, stand and commissioning as surveyed", "sort_order": 2},
	])
	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Which UKCM laser do I need?", "answer": "Fiber (KF130) for metals and many cables. CO2 (KC130) for cartons, PET and wood. UV (KU110) for foil, medical plastics and fine electronics. We confirm on samples.", "sort_order": 1},
		{"question": "Is there a handheld laser?", "answer": "Yes — Kezojet / UKCM KFH130 is a 30 W mobile fiber. It is not this hub SKU and it is not the TIJ hand coder.", "sort_order": 2},
		{"question": "Do you install in Saudi Arabia?", "answer": "Yes. Printechs consults, supplies, installs, configures and supports UKCM lasers in Riyadh, Jeddah, Dammam and other regions.", "sort_order": 3},
	])
	return save_product(doc)


def fill_fiber(media):
	slug = "ukcm-fiber-laser"
	item = "IND.SYS.KZT.4628"
	card = media["fiber"]
	doc = get_or_create(slug, "UKCM KF130 Fiber Laser", card, item=item)
	apply_identity(doc, slug=slug, display_name="UKCM KF130 30W Fiber Laser", category_label="FIBER LASER", subcategory="Laser Marking")
	doc.tagline = "30 W flying fiber — metals, cable and hard plastics."
	doc.short_description = (
		"UKCM / Kezojet KF130 is a 30 W, AC220 V fiber laser with a high-speed "
		"galvanometer. Permanent serials and 2D codes on metal and selected plastics."
	)
	doc.long_description = (
		"<p>KF130 is the 30 W flying fiber marker we stock as "
		"<strong>IND.SYS.KZT.4628</strong>. Fiber (typically 1064 nm) couples into "
		"metals — aluminium, steel, coated parts — and some hard plastics. It is not "
		"the CO2 pack coder and not the UV foil marker.</p>"
		"<p>The Item is specified with a high-speed galvanometer for on-the-fly marks. "
		"The Kenjiete laser family that includes KF120 / KF130 / KF150 shares a Linux "
		"touch controller, photocell/encoder modes and start/status I/O. We confirm "
		"lens field (commonly 110 × 110 mm) and working distance on the survey.</p>"
		"<p>Need deeper contrast on stainless or colour-change on some alloys? A "
		"<strong>60 W JPT MOPA with Scanlab galvo</strong> (IND.SYS.KZT.4896) can be "
		"quoted. Need the head to go to the part? Ask for KFH130 handheld fiber — "
		"that is a different Item.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM KF130 30 watt flying fiber laser marking head and controller"
	doc.video_url = ""
	doc.hero_trust_chips = "KF130 · 30 W fiber\nHigh-speed galvo\nAC220 V\nMetals & cable"
	doc.story_heading = "Fiber when the code must stay on metal"
	doc.visual_story_heading = "Automotive parts and cable jackets"
	doc.card_title = "KF130 fiber"
	doc.card_summary = "30 W flying fiber laser with high-speed galvanometer for metal and cable codes."
	doc.card_image = card
	doc.final_cta_heading = "Quote KF130 for your metal or cable line"
	doc.final_cta_description = "Send a sample part. We confirm lens, galvo and whether 30 W or 60 W MOPA is right."
	doc.meta_title = "UKCM KF130 Fiber Laser 30W Saudi Arabia | Printechs"
	doc.meta_description = (
		"UKCM KF130 30 W fiber laser with high-speed galvanometer. Permanent metal and "
		"cable codes. Installed by Printechs in KSA."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "Metal-first wavelength", "description": "Fiber couples into aluminium, steel and many coated metals where CO2 will not.", "sort_order": 1},
		{"icon": "speed", "title": "High-speed galvo", "description": "This SKU is the flying KF130 — photocell or encoder, not a desktop hobby engraver.", "sort_order": 2},
		{"icon": "scan", "title": "2D that stays", "description": "Serials and QR that survive heat, oil and handling better than a paper label.", "sort_order": 3},
		{"icon": "integration", "title": "Line I/O", "description": "Start, status and fault signals on the Kenjiete family controller — surveyed per line.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "KF130", "image": card, "image_alt": "KF130 fiber laser", "caption": "30 W flying fiber head and controller.", "sort_order": 1},
		{"label": "Metal parts", "image": media["fiber-metal"], "image_alt": "Fiber on metal", "caption": "Automotive and fabricated parts.", "sort_order": 2},
		{"label": "Cable", "image": media["fiber-cable"], "image_alt": "Fiber on cable", "caption": "Meter marks and QR on jackets.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "30 W fiber", "description": "KF130 · AC220 V 60 Hz", "sort_order": 1},
		{"icon": "speed", "title": "Flying galvo", "description": "High-speed scan head", "sort_order": 2},
		{"icon": "display", "title": "Linux HMI", "description": "Family 10.2-inch controller", "sort_order": 3},
		{"icon": "connectivity", "title": "Line signals", "description": "Photocell / encoder / I/O", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "UKCM / Kezojet KF130 flying fiber laser"),
			("Item code", item),
			("Power", "30 W (this SKU). 60 W JPT MOPA + Scanlab is IND.SYS.KZT.4896 — quote separately"),
			("Supply", "AC220 V, 60 Hz (Item specification)"),
			("Scan head", "High-speed galvanometer (Item specification)"),
			("Not included", "KFH130 handheld fiber, CO2 KC130, UV KU110"),
		]),
		("Marking (family / survey)", [
			("Wavelength", "Fiber — typically 1064 nm (UKCM / Kenjiete fiber family)"),
			("Typical field", "110 × 110 mm common; other F-theta lenses quoted after survey"),
			("Codes", "Text, logo, Code 39/128, QR — content sized to the part"),
			("Cooling", "Air-cooled family design; confirm on the serial plate"),
			("Controller", "Linux touch controller with static / analogue / encoder modes (Kenjiete family)"),
		]),
		("Environment", [
			("Use", "Metals, coated metals, some hard plastics and cable jackets — sample required"),
			("Safety", "Class 4 industrial laser: enclosure, interlocks and eyewear specified per site"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "30 W KF130 vs 60 W MOPA",
			"body": (
				"IND.SYS.KZT.4628 is the 30 W KF130 flying marker. Deep anneal, colour "
				"change or very large fields may need the 60 W JPT MOPA with Scanlab "
				"galvo. We do not put that extra source on this Item."
			),
			"image": media["fiber-metal"],
			"image_alt": "Fiber laser on metal parts",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items("Laser safety kit"))
	doc.set("package_contents", [
		{"item_description": "KF130 30 W fiber laser with high-speed galvanometer", "sort_order": 1},
		{"item_description": "Controller, focusing lens, photocell and stand as quoted", "sort_order": 2},
	])
	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "What Item is this?", "answer": "IND.SYS.KZT.4628 — Kezojet KF130, 30 W, AC220 V, 60 Hz, fiber laser with high-speed galvanometer.", "sort_order": 1},
		{"question": "Will it mark PET bottles?", "answer": "Usually no — that is the CO2 KC130 job. Fiber is for metals and selected plastics. We mark samples first.", "sort_order": 2},
		{"question": "Can I have 60 W MOPA instead?", "answer": "Yes, as a separate quote (IND.SYS.KZT.4896). Do not assume this 30 W SKU includes a JPT MOPA or Scanlab head.", "sort_order": 3},
	])
	return save_product(doc)


def fill_co2(media):
	slug = "ukcm-co2-laser"
	item = "IND.SYS.KZT.4243"
	card = media["co2"]
	doc = get_or_create(slug, "UKCM KC130 CO2 Laser", card, item=item)
	apply_identity(doc, slug=slug, display_name="UKCM KC130 30W CO2 Laser", category_label="CO2 LASER", subcategory="Laser Marking")
	doc.tagline = "10.6 µm CO2 — PET, cartons and organic packs."
	doc.short_description = (
		"UKCM / Kezojet KC130 is a 30 W air-cooled CO2 laser with stand. Permanent "
		"codes on PET, paperboard and many non-metals — not a fiber metal marker."
	)
	doc.long_description = (
		"<p>KC130 is the 30 W CO2 flying marker we stock as "
		"<strong>IND.SYS.KZT.4243</strong> (AC220 V, with stand). CO2 at "
		"<strong>10600 nm</strong> marks cartons, PET, wood and many organic packs. "
		"It is a poor choice for bare metals — that is KF130.</p>"
		"<p>Kenjiete’s KC130 listing: air-cooled 30 W (40 W KC140 and 60 W KC160 exist "
		"as other models), ≤7000 mm/s scan, 10.2-inch Linux controller, 160 mm focus "
		"lens, 110 × 110 mm field (optional), 0.03 mm minimum line, production-line "
		"speed up to 280 m/min depending on material, head 640 × 178 × 150 mm, "
		"controller 416 × 170 × 267 mm, about 32 kg, ~800 W draw, 0–45 °C.</p>"
		"<p>This page is the 30 W KC130 with stand. Do not assume a 60 W source or a "
		"fiber galvo on this Item.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM KC130 30 watt CO2 laser marking head and controller"
	doc.video_url = ""
	doc.hero_trust_chips = "KC130 · 30 W CO2\n10600 nm · air cooled\n10.2-inch Linux HMI\nStand included"
	doc.story_heading = "CO2 when the pack is paper, PET or board"
	doc.visual_story_heading = "Bottles and cartons without ink"
	doc.card_title = "KC130 CO2"
	doc.card_summary = "30 W air-cooled CO2 laser with stand for PET, carton and organic packs."
	doc.card_image = card
	doc.final_cta_heading = "Quote KC130 for bottles or cartons"
	doc.final_cta_description = "Send pack samples. We confirm contrast, line speed and extraction."
	doc.meta_title = "UKCM KC130 CO2 Laser 30W Saudi Arabia | Printechs"
	doc.meta_description = (
		"UKCM KC130 30 W CO2 laser (10600 nm) for PET and cartons. Air-cooled, Linux "
		"HMI, stand included. Printechs in KSA."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "10.6 µm for packs", "description": "CO2 marks PET, carton and many organics that fiber will barely tint.", "sort_order": 1},
		{"icon": "speed", "title": "Flying mark", "description": "Kenjiete lists ≤7000 mm/s scan and up to 280 m/min line speed, material-dependent.", "sort_order": 2},
		{"icon": "display", "title": "10.2-inch Linux HMI", "description": "Static, analogue or encoder modes; Arabic among operator languages.", "sort_order": 3},
		{"icon": "install", "title": "Stand on this SKU", "description": "IND.SYS.KZT.4243 includes the stand — we still survey throw and extraction.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "KC130", "image": card, "image_alt": "KC130 CO2 laser", "caption": "30 W air-cooled CO2 with stand.", "sort_order": 1},
		{"label": "PET", "image": media["co2-bottle"], "image_alt": "CO2 on bottles", "caption": "Expiry on bottle shoulders.", "sort_order": 2},
		{"label": "Cartons", "image": media["co2-carton"], "image_alt": "CO2 on cartons", "caption": "Lot marks on paperboard.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "30 W CO2", "description": "10600 nm · air cooled", "sort_order": 1},
		{"icon": "speed", "title": "≤7000 mm/s", "description": "Kenjiete KC130 listing", "sort_order": 2},
		{"icon": "display", "title": "10.2-inch HMI", "description": "Linux · encoder / photocell", "sort_order": 3},
		{"icon": "install", "title": "With stand", "description": "This Item includes the stand", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "UKCM / Kezojet KC130 CO2 laser with stand"),
			("Item code", item),
			("Power", "30 W (KC130). KC140 40 W and KC160 60 W are other models — not this Item"),
			("Supply", "AC220 V, 50 Hz class (Kenjiete listing); Item also notes 5 Hz nameplate — confirm on serial"),
			("Included", "Stand (Item description)"),
		]),
		("Kenjiete KC130 listing", [
			("Wavelength", "10600 nm CO2"),
			("Cooling", "Air cooling"),
			("Scan speed", "≤7000 mm/s"),
			("Focus lens", "160 mm"),
			("Field", "110 × 110 mm (optional other fields)"),
			("Min. line / repeat", "0.03 mm / 0.01 mm"),
			("Line speed", "0–280 m/min depending on material"),
			("Head / box", "640×178×150 mm head; 416×170×267 mm controller"),
			("Mass / draw", "About 32 kg; about 800 W (30/40 W class)"),
			("Climate", "0–45 °C, humidity ≤95 %"),
			("Files / codes", "BMP, DXF, HPGL, JPEG, PLT; Code 39/128, QR"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "CO2 is not a metal annealer",
			"body": (
				"If the part is bare steel or aluminium, specify KF130 fiber. KC130 is "
				"for packs, PET and organics. We mark your bottle or carton before we "
				"lock the lens."
			),
			"image": media["co2-bottle"],
			"image_alt": "CO2 laser on PET bottles",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items("Extraction & filters"))
	doc.set("package_contents", [
		{"item_description": "KC130 30 W CO2 laser", "sort_order": 1},
		{"item_description": "Stand, controller and focusing lens as quoted", "sort_order": 2},
	])
	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "What Item is this?", "answer": "IND.SYS.KZT.4243 — Kezojet KC130, 30 W CO2 laser with stand.", "sort_order": 1},
		{"question": "Will it mark stainless steel?", "answer": "Not as a primary process. Use KF130 fiber for metals. KC130 is for PET, carton and organics.", "sort_order": 2},
		{"question": "Is 60 W included?", "answer": "No. This SKU is 30 W KC130. 40 W / 60 W CO2 are other Kenjiete models.", "sort_order": 3},
	])
	return save_product(doc)


def fill_uv(media):
	slug = "ukcm-uv-laser"
	item = "IND.SYS.KZT.4557"
	card = media["uv"]
	doc = get_or_create(slug, "UKCM KU110 UV Laser", card, item=item)
	apply_identity(doc, slug=slug, display_name="UKCM KU110 10W UV Laser", category_label="UV LASER", subcategory="Laser Marking")
	doc.tagline = "355 nm UV — foil, medical plastics and fine electronics."
	doc.short_description = (
		"UKCM / Kezojet KU110 is a 10 W UV laser for heat-sensitive packs: blister "
		"foil, white plastics and small 2D codes that CO2 or fiber would scorch."
	)
	doc.long_description = (
		"<p>KU110 is the 10 W UV marker we stock as <strong>IND.SYS.KZT.4557</strong>. "
		"UV at <strong>355 nm</strong> makes high-contrast marks on many plastics and "
		"foils with less heat than IR fiber or CO2. It is the usual UKCM choice for "
		"pharma blisters, medical plastics and small electronics housings.</p>"
		"<p>Kenjiete’s KU110 listing: 3 W (KU103) / 5 W (KU105) / 10 W (KU110), "
		"≤12000 mm/s, 10.2-inch controller, air cooling, 160 mm lens, 0.01 mm minimum "
		"line, 0.001 mm repeat, 110 × 110 mm field (optional), line speed up to "
		"350 m/min depending on material, about 40 kg for 10 W, ~800 W draw, "
		"head 500 × 103 × 110 mm, controller 640 × 160 × 206 mm.</p>"
		"<p>This page is the 10 W KU110 only. Do not mix 3 W / 5 W ratings or fiber "
		"metal claims onto this Item.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM KU110 10 watt UV laser marking head and controller"
	doc.video_url = ""
	doc.hero_trust_chips = "KU110 · 10 W UV\n355 nm\nFine 2D on foil\nAir cooled"
	doc.story_heading = "UV when the pack cannot take heat"
	doc.visual_story_heading = "Blisters and plastic housings"
	doc.card_title = "KU110 UV"
	doc.card_summary = "10 W 355 nm UV laser for foil, medical plastics and fine electronics codes."
	doc.card_image = card
	doc.final_cta_heading = "Quote KU110 for foil or medical plastics"
	doc.final_cta_description = "Send blister or housing samples. We confirm contrast without burning the film."
	doc.meta_title = "UKCM KU110 UV Laser 10W Saudi Arabia | Printechs"
	doc.meta_description = (
		"UKCM KU110 10 W UV laser (355 nm) for pharma foil and delicate plastics. "
		"Installed by Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "355 nm, low heat", "description": "Cold-ish UV mark on foils and plastics that IR lasers scorch.", "sort_order": 1},
		{"icon": "scan", "title": "Fine 2D", "description": "Kenjiete lists 0.01 mm minimum line — sized for small UDI and electronics codes.", "sort_order": 2},
		{"icon": "speed", "title": "≤12000 mm/s", "description": "KU110 listing scan speed; real line speed still depends on the code and film.", "sort_order": 3},
		{"icon": "shield", "title": "Pharma-ready process", "description": "We set contrast for GS1 / UDI readability — the machine does not replace validation.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "KU110", "image": card, "image_alt": "KU110 UV laser", "caption": "10 W 355 nm UV marker.", "sort_order": 1},
		{"label": "Blisters", "image": media["uv-blister"], "image_alt": "UV on blister foil", "caption": "2D on heat-sensitive foil.", "sort_order": 2},
		{"label": "Electronics", "image": media["uv-electronics"], "image_alt": "UV on plastic housing", "caption": "Serials on white plastics.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "10 W UV", "description": "355 nm · KU110", "sort_order": 1},
		{"icon": "speed", "title": "≤12000 mm/s", "description": "Kenjiete KU110 listing", "sort_order": 2},
		{"icon": "scan", "title": "0.01 mm line", "description": "Fine 2D and UDI", "sort_order": 3},
		{"icon": "display", "title": "10.2-inch HMI", "description": "Family Linux controller", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "UKCM / Kezojet KU110 10 W UV laser"),
			("Item code", item),
			("Power", "10 W (KU110). KU103 3 W and KU105 5 W are other models"),
			("Wavelength", "355 nm"),
		]),
		("Kenjiete KU110 listing", [
			("Scan speed", "≤12000 mm/s"),
			("Cooling", "Air cooling"),
			("Focus lens", "160 mm"),
			("Min. line / repeat", "0.01 mm / 0.001 mm"),
			("Field", "110 × 110 mm (optional other fields)"),
			("Line speed", "0–350 m/min depending on material"),
			("Mass / draw", "About 40 kg (10 W); about 800 W"),
			("Head / box", "500×103×110 mm head; 640×160×206 mm controller"),
			("Climate", "0–45 °C, humidity ≤95 %"),
			("Codes", "Code 39/128, QR plus text and logos"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "UV is not a 30 W metal laser",
			"body": (
				"KU110 will not replace KF130 on stainless. It will mark many foils and "
				"white plastics that fiber or CO2 damage. Always send the actual film."
			),
			"image": media["uv-blister"],
			"image_alt": "UV laser on blister foil",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items("Sample marking"))
	doc.set("package_contents", [
		{"item_description": "KU110 10 W UV laser", "sort_order": 1},
		{"item_description": "Controller, lens and line integration as quoted", "sort_order": 2},
	])
	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "What Item is this?", "answer": "IND.SYS.KZT.4557 — Kezojet 10 W UV laser model KU110.", "sort_order": 1},
		{"question": "Is it 3 W or 5 W?", "answer": "This SKU is 10 W KU110. KU103 / KU105 are other powers — do not order those when you need this page.", "sort_order": 2},
		{"question": "Pharma UDI?", "answer": "KU110 can mark small 2D codes on foil and plastics. Readability and validation stay your quality process; we set the mark.", "sort_order": 3},
	])
	return save_product(doc)


def fill_kt7(media):
	slug = "ukcm-kt7"
	item = "IND.SYS.KZT.4008"
	card = media["kt7"]
	doc = get_or_create(slug, "UKCM KT7 Thermal Inkjet", card, item=item)
	apply_identity(doc, slug=slug, display_name="UKCM KT7 TIJ Printer", category_label="THERMAL INKJET", subcategory="Thermal Inkjet")
	doc.tagline = "7-inch TIJ station — 300 dpi, up to 40 m/min."
	doc.short_description = (
		"UKCM KT7 (UK 7) is the 7-inch thermal inkjet controller. This SKU is the "
		"half-inch head package. 300 dpi and up to 40 m/min — not the KT10 120 m/min station."
	)
	doc.long_description = (
		"<p>KT7 is UKCM’s mid-size online TIJ — listed as <strong>UK 7</strong> on "
		"<a href=\"https://uk-cm.uk/thermal-transfer-inkjet-printer/\">uk-cm.uk</a> and "
		"as KT-7 on 3S Ink. It is a sealed HP/Funai cartridge printer, not a CIJ and "
		"not KT10.</p>"
		"<p>3S Ink rates KT-7 at <strong>300 dpi</strong> and <strong>40 m/min</strong>, "
		"print heights of 25 mm or 50 mm depending on heads, and up to "
		"<strong>six nozzles</strong> on the controller. "
		"<strong>IND.SYS.KZT.4008</strong> is the half-inch (12.7 mm) 7-inch-screen "
		"package. A one-inch KT7 (IND.SYS.KZT.4094) can be quoted if you need a "
		"25.4 mm band — that is a different Item.</p>"
		"<p>Need 10.1-inch HMI, 120 m/min and up to ten nozzles? That is "
		"<a href=\"/products/ukcm-kt10\">KT10</a>. Need to walk the code to a pallet? "
		"See the <a href=\"/products/ukcm-hand-coder\">hand coder</a>.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM KT7 7-inch thermal inkjet controller with TIJ printhead"
	doc.video_url = ""
	doc.hero_trust_chips = "7-inch HMI\nHalf-inch head on this SKU\n300 dpi · 40 m/min\nUp to 6 nozzles"
	doc.story_heading = "Compact TIJ when KT10 is more station than you need"
	doc.visual_story_heading = "Cartons and dairy packs"
	doc.card_title = "KT7"
	doc.card_summary = "UK 7 TIJ: 7-inch screen, 300 dpi, 40 m/min. This SKU is the half-inch head."
	doc.card_image = card
	doc.final_cta_heading = "Quote KT7 for a compact TIJ station"
	doc.final_cta_description = "We confirm head count, ink (water/solvent) and whether KT10 is the better controller."
	doc.meta_title = "UKCM KT7 Thermal Inkjet Printer Saudi Arabia | Printechs"
	doc.meta_description = (
		"UKCM KT7 (UK 7) TIJ coder: 7-inch screen, 300 dpi, 40 m/min, half-inch head. "
		"Supplied and installed by Printechs in KSA."
	)
	doc.set("benefits", [
		{"icon": "display", "title": "7-inch controller", "description": "UK 7 HMI for date, batch, barcode and logo — smaller than the KT10 10.1-inch station.", "sort_order": 1},
		{"icon": "speed", "title": "40 m/min at 300 dpi", "description": "3S Ink KT-7 rating. Do not use the KT10 120 m/min figure on this page.", "sort_order": 2},
		{"icon": "print", "title": "Half-inch on this SKU", "description": "IND.SYS.KZT.4008 is 12.7 mm. One-inch KT7 is a separate Item.", "sort_order": 3},
		{"icon": "consumables", "title": "HP / Funai 42 ml", "description": "Water or solvent cartridges with RFID chip — same family inks as KT10.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "KT7 station", "image": media["kt7_photo"], "image_alt": "Official KT7 TIJ station", "caption": "Official 3S Ink / UKCM KT7 controller and head.", "sort_order": 1},
		{"label": "Cartons", "image": media["kt7-carton"], "image_alt": "KT7 on cartons", "caption": "Dates and barcodes on folding cartons.", "sort_order": 2},
		{"label": "Dairy", "image": media["kt7-dairy"], "image_alt": "KT7 on bottles", "caption": "Confirm solvent vs water ink for wet halls.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "Thermal inkjet", "description": "HP / Funai 42 ml", "sort_order": 1},
		{"icon": "display", "title": "7-inch HMI", "description": "UK 7 controller", "sort_order": 2},
		{"icon": "speed", "title": "40 m/min", "description": "300 dpi (3S Ink KT-7)", "sort_order": 3},
		{"icon": "lines", "title": "12.7 mm", "description": "Half-inch head on this SKU", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "UKCM KT7 / UK 7 — not KT10, not KT5, not CIJ"),
			("Item code", item),
			("Head on this SKU", "Half-inch (12.7 mm) TIJ"),
			("Other KT7 Item", "One-inch KT7 is IND.SYS.KZT.4094 — quote separately"),
			("Controller capacity", "Up to 6 nozzles (3S Ink KT-7); this Item is supplied as half-inch"),
		]),
		("Printing (3S Ink KT-7)", [
			("Technology", "Thermal inkjet (HP TIJ 2.5 / thermal-bubble)"),
			("Resolution", "300 dpi"),
			("Speed", "Up to 40 m/min"),
			("Print height options", "25 mm or 50 mm depending on head count — not automatic on this SKU"),
			("Throw", "Typically 2–5 mm (KT series)"),
			("Inks", "Water or solvent 42 ml HP/Funai with RFID — confirm per substrate"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "KT7 vs KT10",
			"body": (
				"KT7 is the 7-inch, 40 m/min, up-to-6-nozzle controller. KT10 is the "
				"10.1-inch, 100–120 m/min, up-to-10-nozzle station. Order the page that "
				"matches the line — do not mix the ratings."
			),
			"image": media["kt7-carton"],
			"image_alt": "KT7 carton coding",
			"link_label": "See KT10",
			"link_href": "/products/ukcm-kt10",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items("TIJ cartridges"))
	apply_brochure(doc, media["brochure"], "UKCM KT-10 / KT series brochure")
	doc.set("package_contents", [
		{"item_description": "KT7 / UK 7 controller with 7-inch touchscreen", "sort_order": 1},
		{"item_description": "Half-inch TIJ printhead (this SKU)", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "What Item is this?", "answer": "IND.SYS.KZT.4008 — Kezojet KT7 half-inch TIJ with 7-inch screen.", "sort_order": 1},
		{"question": "Is this as fast as KT10?", "answer": "No. 3S Ink lists KT7 at 40 m/min and KT10 at up to 120 m/min. Use KT10 when the line needs that controller.", "sort_order": 2},
		{"question": "Can I download a brochure?", "answer": "Yes — the official UKCM KT-10 series brochure is attached (same KT family: cartridges, I/O and heads). KT7 ratings on this page follow the KT7 listing.", "sort_order": 3},
	])
	return save_product(doc)


def fill_kt10(media):
	slug = "ukcm-kt10"
	item = "IND.SYS.KZT.4982"
	card = media["kt10"]
	doc = get_or_create(slug, "UKCM KT10 Thermal Inkjet", card, item=item)
	apply_identity(doc, slug=slug, display_name="UKCM KT10 TIJ Printer", category_label="THERMAL INKJET", subcategory="Thermal Inkjet")
	doc.tagline = "10.1-inch TIJ — 25.4 mm twin head, up to 100–120 m/min."
	doc.short_description = (
		"UKCM KT10 (UK 10) thermal inkjet: 10.1-inch capacitive Linux HMI and a "
		"one-inch twin head. This SKU includes mounting, anti-shock and a line cable."
	)
	doc.long_description = (
		"<p>KT10 is UKCM’s flagship online TIJ — <strong>UK 10</strong> on uk-cm.uk, "
		"KT-10 on the official brochure you attached. It is not KT7 (7-inch / 40 m/min) "
		"and not a CIJ.</p>"
		"<p>The <strong>TIJ-KT-10 brochure</strong> lists: Linux OS, aluminium controller "
		"<strong>250 × 158 × 35 mm</strong>, 10.1-inch capacitive screen, TIJ hot-foam "
		"nozzles, head mass about 597 g without cartridge, 300 / 150 dpi, 1–15 digit "
		"counter, 2–5 mm throw, 42 ml cartridges, print height 2–25.4 mm (up to 250 mm "
		"with more heads), adapter 16 V 3 A / 5 A, 0–40 °C / 10–80 % RH, interfaces "
		"power / USB / RS-232 / Ethernet (Wi-Fi and HDMI on the family diagrams), "
		"barcodes UPCA, EAN, Int 25, Code 39/128, PDF417, Data Matrix, QR. The brochure "
		"table states <strong>100 m/min</strong>; 3S Ink lists <strong>120 m/min</strong> "
		"at 300 dpi. We treat 100–120 m/min as the family range and confirm on the line.</p>"
		"<p><strong>IND.SYS.KZT.4982</strong> is the one-inch twin-head package (25.4 mm) "
		"with mounting, anti-shock and a tailored umbilical. The controller can drive "
		"up to ten nozzles; this Item is supplied as twin-head.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM KT10 10.1-inch thermal inkjet controller with TIJ printhead and photocell"
	doc.video_url = VIDEO_KT10_INTRO
	doc.hero_trust_chips = "10.1-inch capacitive HMI\n25.4 mm twin head\n100–120 m/min · 300 dpi\nUp to 10 nozzles"
	doc.story_heading = "Large screen. Twin-head TIJ. Cartridge, not makeup."
	doc.visual_story_heading = "Official KT10 station, cartons and pipe"
	doc.card_title = "KT10"
	doc.card_summary = "UK 10 TIJ: 10.1-inch screen, 25.4 mm twin head, 100–120 m/min. Brochure attached."
	doc.card_image = card
	doc.final_cta_heading = "Specify KT10 for your packaging line"
	doc.final_cta_description = "Printechs will confirm heads, HP/Funai ink, throw, mounting and cable length."
	doc.meta_title = "UKCM KT10 Thermal Inkjet Printer Saudi Arabia | Printechs"
	doc.meta_description = (
		"UKCM KT10 (UK 10) TIJ: 10.1-inch screen, 25.4 mm twin head, 100–120 m/min. "
		"Official brochure. Installed by Printechs in KSA."
	)
	doc.set("benefits", [
		{"icon": "display", "title": "10.1-inch capacitive HMI", "description": "Linux, ~20 languages including Arabic, RFID cartridge ID and ink-level on screen (brochure).", "sort_order": 1},
		{"icon": "print", "title": "One-inch twin head", "description": "Two 12.7 mm cartridges, 25.4 mm band — dates, barcodes, QR and logos in one pass.", "sort_order": 2},
		{"icon": "speed", "title": "100–120 m/min", "description": "Brochure table 100 m/min; 3S Ink 120 m/min at 300 dpi. Not the KT7 40 m/min rating.", "sort_order": 3},
		{"icon": "install", "title": "Ready to mount", "description": "This SKU includes bracket kit, anti-shock and a cable cut for the conveyor.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "KT10 station", "image": media["kt10_photo"], "image_alt": "Official KT10 station", "caption": "Official UKCM / 3S Ink 10.1-inch station.", "sort_order": 1},
		{"label": "Cartons", "image": media["kt10-carton"], "image_alt": "KT10 on cartons", "caption": "Batch and QR on folding cartons.", "sort_order": 2},
		{"label": "Pipe", "image": media["kt10-pipe"], "image_alt": "KT10 on pipe", "caption": "Confirm solvent/pigment ink and 2–5 mm throw.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "Thermal inkjet", "description": "42 ml HP / Funai", "sort_order": 1},
		{"icon": "lines", "title": "25.4 mm band", "description": "Twin 12.7 mm on this SKU", "sort_order": 2},
		{"icon": "display", "title": "10.1-inch HMI", "description": "Capacitive · Linux", "sort_order": 3},
		{"icon": "speed", "title": "100–120 m/min", "description": "300 / 150 dpi (brochure)", "sort_order": 4},
		{"icon": "connectivity", "title": "USB · RS-232 · Ethernet", "description": "Wi-Fi / HDMI family options", "sort_order": 5},
		{"icon": "install", "title": "This SKU", "description": "Mounting + anti-shock + cable", "sort_order": 6},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "UKCM KT-10 Printer / UK 10 (not KT7, not KT5, not CIJ)"),
			("Item code", item),
			("Printheads on this SKU", "One-inch twin head — 25.4 mm print band"),
			("Controller capacity", "Up to 10 nozzles (brochure); this Item is supplied as twin-head"),
			("Included", "Mounting accessories, anti-shock, cable length specified for the line"),
		]),
		("Official KT-10 brochure", [
			("System", "Linux"),
			("Controller size / material", "250 × 158 × 35 mm aluminium"),
			("Screen", "10.1-inch capacitive"),
			("Nozzle", "TIJ hot-foaming"),
			("Head mass", "About 597 g without cartridge"),
			("Resolution", "300 dpi / 150 dpi"),
			("Speed", "100 m/min (brochure table); 3S Ink lists 120 m/min at 300 dpi"),
			("Throw", "2–5 mm"),
			("Print height", "2–25.4 mm; up to 250 mm with additional heads"),
			("Cartridge", "42 ml; dry / wet / oil; water and fast-dry colour sets"),
			("Adapter", "16 V 3 A / 5 A"),
			("Counter", "1–15 digits"),
			("Barcodes", "UPCA, EAN, Int 25, Code 39/128, PDF417, Data Matrix, QR"),
			("I/O", "Power, USB, RS-232, Ethernet; Wi-Fi / HDMI / encoder / photocell on family diagrams"),
			("Climate", "0–40 °C, 10–80 % RH"),
			("Languages", "Chinese, English, Russian, French, Spanish, Japanese, Korean, Arabic and others"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Meet the UKCM KT10",
			"body": "Official introduction to the 10.1-inch online TIJ station. Watch the HMI and head, then we size cartridges and throw for your pack.",
			"video_url": VIDEO_KT10_INTRO,
			"image": media["kt10_photo"],
			"image_alt": "UKCM KT10 thermal inkjet station",
			"sort_order": 1,
		},
		{
			"section_type": "Industry Solution",
			"heading": "Set up the online TIJ station",
			"body": "Stand, photocell, head and 10.1-inch controller. This SKU already includes mounting and anti-shock — Printechs sets the 2–5 mm throw on site.",
			"video_url": VIDEO_KT10_SETUP,
			"image": media["kt10-carton"],
			"image_alt": "KT10 printhead and controller on a line",
			"sort_order": 2,
		},
		{
			"section_type": "Industry Solution",
			"heading": "Cartridges and accessories",
			"body": "42 ml HP45 / Funai cartridges — water, solvent, oil, fast-dry or invisible. The HMI reads cartridge type and ink level via RFID (brochure).",
			"video_url": VIDEO_KT10_ACCESS,
			"image": media["kt10-carton"],
			"image_alt": "KT10 carton coding",
			"sort_order": 3,
		},
		{
			"section_type": "Industry Solution",
			"heading": "Pipe and extrusion examples",
			"body": "The KT series is shown on pipe as well as packs. We still confirm solvent or pigment ink and throw on PE/PP before we lock KT10.",
			"video_url": VIDEO_KT10_PIPE,
			"image": media["kt10-pipe"],
			"image_alt": "KT10 pipe coding",
			"sort_order": 4,
		},
		ksa_section(media, slug, 5),
	])
	doc.set("support_items", support_items("TIJ cartridges"))
	apply_brochure(doc, media["brochure"], "UKCM KT-10 brochure")
	doc.set("package_contents", [
		{"item_description": "KT10 / UK 10 controller with 10.1-inch colour touchscreen", "sort_order": 1},
		{"item_description": "One-inch twin TIJ printhead (25.4 mm band)", "sort_order": 2},
		{"item_description": "Complete mounting accessories, anti-shock and line cable", "sort_order": 3},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "What is included with IND.SYS.KZT.4982?", "answer": "KT10 with the 10.1-inch screen, a one-inch twin printhead, mounting accessories, anti-shock, and a cable length specified for the line.", "sort_order": 1},
		{"question": "Is KT10 the same as UK 10?", "answer": "Yes. KT10 is the UKCM KT-series controller with the 10.1-inch touchscreen (UK 10). It is not KT7 or a CIJ.", "sort_order": 2},
		{"question": "Where is the brochure?", "answer": "The official TIJ-KT-10 brochure is attached on this page (Downloads). Specs on this page follow that PDF plus the 3S Ink speed listing.", "sort_order": 3},
	])
	return save_product(doc)


def fill_hand(media):
	slug = "ukcm-hand-coder"
	item = "IND.SYS.KZT.4977"
	card = media["handjet"]
	doc = get_or_create(slug, "UKCM Hand Coder", card, item=item)
	apply_identity(doc, slug=slug, display_name="UKCM Hand Coder (Mobile TIJ)", category_label="HAND CODER", subcategory="Thermal Inkjet")
	doc.tagline = "Portable TIJ gun — take the code to the pack."
	doc.short_description = (
		"UKCM handjet / mobile coder: a handheld thermal inkjet for cartons, pipe and "
		"static goods. This SKU is the single-head half-inch gun — not KT7/KT10 and not a laser."
	)
	doc.long_description = (
		"<p>The UKCM TIJ range on uk-cm.uk includes <strong>UK MINI</strong> — the "
		"portable / handheld coder — beside UK 7 and UK 10. We sell that class as the "
		"<strong>UKCM Handjet</strong> (Kezojet UKCM handjet Items).</p>"
		"<p><strong>IND.SYS.KZT.4977</strong> is the <strong>single-head half-inch</strong> "
		"handjet. A one-inch handjet (IND.SYS.KZT.4978) can be quoted when you need a "
		"taller band. Both are cartridge TIJ guns: walk to the pallet, drum or pipe "
		"when there is no conveyor station.</p>"
		"<p>UKCM’s TIJ page lists portable/compact design, wireless transfer, long "
		"battery life, variable data (QR, serial, expiry, batch), quick-dry ink and "
		"easy cartridge change. This page is the handheld gun only — not the EBS-250 "
		"or 16-nozzle MIC hand coder, and not the KFH130 handheld fiber laser.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "UKCM handheld thermal inkjet gun with 12.7 mm cartridge"
	doc.video_url = ""
	doc.hero_trust_chips = "Handheld TIJ\nHalf-inch head on this SKU\nBattery / mobile\nCartons · pipe · drums"
	doc.story_heading = "When the pack will not come to the printer"
	doc.visual_story_heading = "Pallets and large items"
	doc.card_title = "Hand coder"
	doc.card_summary = "UKCM mobile TIJ gun — half-inch single head for cartons, pipe and static goods."
	doc.card_image = card
	doc.final_cta_heading = "Quote a UKCM hand coder"
	doc.final_cta_description = "Tell us the pack size. We confirm half-inch vs one-inch and the ink."
	doc.meta_title = "UKCM Hand Coder Mobile TIJ Saudi Arabia | Printechs"
	doc.meta_description = (
		"UKCM handheld thermal inkjet (handjet) for cartons, pipe and pallets. "
		"Half-inch mobile coder from Printechs in KSA."
	)
	doc.set("benefits", [
		{"icon": "battery", "title": "Mobile, not a line station", "description": "Take the gun to pallets, drums and pipe. KT7/KT10 stay on the conveyor.", "sort_order": 1},
		{"icon": "print", "title": "Half-inch on this SKU", "description": "IND.SYS.KZT.4977 is 12.7 mm single head. One-inch handjet is 4978.", "sort_order": 2},
		{"icon": "scan", "title": "Variable data in the hand", "description": "Batch, expiry, QR and serials from UKCM’s TIJ feature set — confirm message on the gun.", "sort_order": 3},
		{"icon": "consumables", "title": "Swap the cartridge", "description": "Sealed TIJ cartridge. No CIJ makeup. Match water vs solvent to the pack.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Handjet", "image": card, "image_alt": "UKCM hand coder", "caption": "Half-inch mobile TIJ gun.", "sort_order": 1},
		{"label": "Pallets", "image": media["handjet-pallet"], "image_alt": "Hand coder on cartons", "caption": "Codes on cases at the dock.", "sort_order": 2},
		{"label": "Pipe", "image": media["handjet-pipe"], "image_alt": "Hand coder on pipe", "caption": "Batch marks on large items.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "Handheld TIJ", "description": "UK MINI / UKCM Handjet", "sort_order": 1},
		{"icon": "lines", "title": "12.7 mm", "description": "Half-inch single head", "sort_order": 2},
		{"icon": "battery", "title": "Mobile", "description": "Battery / portable use", "sort_order": 3},
		{"icon": "consumables", "title": "42 ml class", "description": "HP-style TIJ cartridge", "sort_order": 4},
	])
	set_specs(doc, [
		("This configuration", [
			("Model", "UKCM Handjet / UK MINI class handheld TIJ"),
			("Item code", item),
			("Head on this SKU", "Single head, half-inch (12.7 mm)"),
			("Other handjet", "One-inch single head is IND.SYS.KZT.4978"),
			("Not this page", "EBS-250, MIC 16-nozzle, KFH130 handheld fiber, KT7/KT10 stations"),
		]),
		("Handheld TIJ (UKCM TIJ page + this Item)", [
			("Technology", "Thermal inkjet cartridge"),
			("Use", "Portable coding on cartons, pipe, drums and static goods"),
			("Data", "Batch, expiry, serial, QR and barcodes — message set on the gun"),
			("Ink", "Quick-dry water or solvent cartridge — confirm per substrate"),
			("Power", "Battery / portable operation (UKCM TIJ portable features)"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Gun vs station",
			"body": (
				"If every pack passes a conveyor, specify KT7 or KT10. The hand coder is "
				"for pallets, returns, large pipe and jobs with no fixed photocell. "
				"Do not order EBS-250 or a 16-nozzle MIC when you want this UKCM handjet."
			),
			"image": media["handjet-pallet"],
			"image_alt": "Handheld TIJ on a warehouse carton",
			"link_label": "See KT7",
			"link_href": "/products/ukcm-kt7",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items("Handjet cartridges"))
	apply_brochure(doc, media["brochure"], "UKCM KT-10 / TIJ family brochure")
	doc.set("package_contents", [
		{"item_description": "UKCM Handjet single-head half-inch printer", "sort_order": 1},
		{"item_description": "Starter cartridge and charger as quoted", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "What Item is this?", "answer": "IND.SYS.KZT.4977 — Kezojet UKCM Handjet single-head half-inch printer.", "sort_order": 1},
		{"question": "Is this a laser?", "answer": "No. This is a handheld TIJ ink gun. The mobile fiber laser is KFH130 on the laser range page.", "sort_order": 2},
		{"question": "Half-inch or one-inch?", "answer": "This page is half-inch. Ask for IND.SYS.KZT.4978 when you need a one-inch handjet.", "sort_order": 3},
	])
	return save_product(doc)


def fill_ukcm():
	media = prepare_media()
	fill_laser_hub(media)
	fill_fiber(media)
	fill_co2(media)
	fill_uv(media)
	fill_kt7(media)
	fill_kt10(media)
	fill_hand(media)
	for slug, related in RELATED.items():
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		set_related(doc, related)
		doc.flags.ignore_permissions = True
		doc.save()
	frappe.db.commit()
	_update_brand(media)
	print("Wired UKCM related products and brand")
	return "ok"


def _update_brand(media):
	from printechs_digital.setup.ukcm_common import ensure_erp_brand

	ensure_erp_brand()
	# Keep Kezojet brand page from listing empty after KT10 moves to UKCM.
	kz = frappe.db.get_value("Website Brand", {"slug": "kezojet"}, "name")
	if kz:
		old = frappe.get_doc("Website Brand", kz)
		old.published = 0
		old.flags.ignore_permissions = True
		old.save()

	logo = media["logo"]
	name = frappe.db.get_value("Website Brand", {"slug": "ukcm"}, "name")
	doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
	doc.brand = "UKCM"
	doc.display_name = "UKCM"
	doc.slug = "ukcm"
	doc.logo = logo
	doc.summary = (
		"UKCM (UK Coding & Marking) fiber, CO2 and UV lasers plus KT7, KT10 and "
		"handheld TIJ — supplied and installed by Printechs in Saudi Arabia."
	)
	doc.sort_order = 9
	doc.published = 1
	doc.meta_title = "UKCM Coding & Marking Saudi Arabia | Printechs Brands"
	doc.meta_description = (
		"UKCM laser marking and thermal inkjet from Printechs in Saudi Arabia — "
		"fiber, CO2, UV, KT7, KT10 and hand coders."
	)
	doc.flags.ignore_permissions = True
	if name:
		doc.save()
	else:
		doc.insert()
	frappe.db.commit()
