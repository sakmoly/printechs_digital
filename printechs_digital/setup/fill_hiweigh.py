# Copyright (c) 2026, Printechs and contributors
"""HiWEIGH industrial weighing cluster for Printechs.

Curated family pages (not every capacity SKU). Official sources: hiweigh.com.
Do not attach spare-part Items. Only link Industrial Systems when the family matches.
"""

import frappe

from printechs_digital.setup.hiweigh_common import (
	KSA_BODY,
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
	"hiweigh-k9": ["hiweigh-k9t", "hiweigh-bxt", "hiweigh-k7s"],
	"hiweigh-k7p": ["hiweigh-k7", "hiweigh-k7s", "hiweigh-fod"],
	"hiweigh-k7": ["hiweigh-ag", "hiweigh-avs", "hiweigh-k9"],
	"hiweigh-k7s": ["hiweigh-k7p", "hiweigh-k7", "hiweigh-bsw"],
	"hiweigh-bxt": ["hiweigh-k9t", "hiweigh-k9", "hiweigh-fwr"],
	"hiweigh-k9t": ["hiweigh-k9", "hiweigh-bxt", "hiweigh-fwr"],
	"hiweigh-bhb": ["hiweigh-k9t", "hiweigh-fod", "hiweigh-bsw"],
	"hiweigh-bsw": ["hiweigh-fod", "hiweigh-fd", "hiweigh-k7s"],
	"hiweigh-fod": ["hiweigh-bhb", "hiweigh-bsw", "hiweigh-k7p"],
	"hiweigh-fd": ["hiweigh-fdl", "hiweigh-fwr", "hiweigh-bsw"],
	"hiweigh-fdl": ["hiweigh-fd", "hiweigh-fwr", "hiweigh-axr"],
	"hiweigh-fwr": ["hiweigh-k9t", "hiweigh-fd", "hiweigh-bxt"],
	"hiweigh-ax": ["hiweigh-axc", "hiweigh-axr", "hiweigh-titan"],
	"hiweigh-axc": ["hiweigh-axr", "hiweigh-ax", "hiweigh-titan"],
	"hiweigh-axr": ["hiweigh-axc", "hiweigh-titan", "hiweigh-ax"],
	"hiweigh-titan": ["hiweigh-axr", "hiweigh-axc", "hiweigh-ax"],
	"hiweigh-ag": ["hiweigh-avs", "hiweigh-aps", "hiweigh-k7"],
	"hiweigh-avs": ["hiweigh-ag", "hiweigh-aps", "hiweigh-ap"],
	"hiweigh-aps": ["hiweigh-avs", "hiweigh-ag", "hiweigh-k9"],
	"hiweigh-ap": ["hiweigh-avs", "hiweigh-ag", "hiweigh-k9t"],
	"hiweigh-m15f": ["hiweigh-m13", "hiweigh-bsw", "hiweigh-fod"],
	"hiweigh-m13": ["hiweigh-m15f", "hiweigh-fod", "hiweigh-bhb"],
}


def _p() -> str:
	return f"<p>{KSA_BODY}</p>"


def _fill(media, cfg):
	slug = cfg["slug"]
	card = media[f"card:{cfg['card']}"]
	doc = get_or_create(slug, cfg["display"], card, item=cfg.get("item"))
	apply_identity(
		doc,
		slug=slug,
		display_name=cfg["display"],
		category_label=cfg["label"],
		subcategory=cfg["sub"],
		featured=cfg.get("featured", 0),
		featured_sort=cfg.get("featured_sort", 0),
	)
	doc.tagline = cfg["tagline"]
	doc.short_description = cfg["short"]
	doc.long_description = cfg["long"]
	doc.hero_image = card
	doc.hero_image_alt = cfg["hero_alt"]
	doc.video_url = ""
	doc.hero_trust_chips = cfg["chips"]
	doc.story_heading = cfg["story"]
	doc.visual_story_heading = cfg["visual"]
	doc.card_title = cfg["card_title"]
	doc.card_summary = cfg["card_summary"]
	doc.card_image = card
	doc.final_cta_heading = cfg["cta_h"]
	doc.final_cta_description = cfg["cta_d"]
	doc.meta_title = cfg["meta_title"]
	doc.meta_description = cfg["meta_desc"]
	doc.set("benefits", cfg["benefits"])
	doc.set(
		"visual_story_items",
		[
			{"label": cfg["story_labels"][0], "image": card, "image_alt": cfg["hero_alt"], "caption": cfg["story_caps"][0], "sort_order": 1},
			{"label": cfg["story_labels"][1], "image": media[cfg["app1"]], "image_alt": cfg["story_alts"][1], "caption": cfg["story_caps"][1], "sort_order": 2},
			{"label": cfg["story_labels"][2], "image": media[f"ksa:{slug}"], "image_alt": cfg["story_alts"][2], "caption": cfg["story_caps"][2], "sort_order": 3},
		],
	)
	doc.set("icon_specifications", cfg["icons"])
	set_specs(doc, cfg["specs"])
	doc.set("applications", scene_apps(media, slug))
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": cfg["section_h"],
				"body": cfg["section_b"],
				"image": media[cfg["app2"]],
				"image_alt": cfg["section_alt"],
				"link_label": "Request a Quote",
				"link_href": f"/products/{slug}/quote",
				"sort_order": 1,
			},
			ksa_section(media, slug, 2),
		],
	)
	doc.set("support_items", support_items())
	doc.set("package_contents", cfg["pack"])
	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", cfg["faqs"])
	return save_product(doc)


def pages():
	return [
		{
			"slug": "hiweigh-k9",
			"display": "HiWEIGH K9 Waterproof Weighing Indicator",
			"card": "k9",
			"sub": "Weighing Indicators",
			"label": "WATERPROOF WEIGHING INDICATOR",
			"featured": 1,
			"featured_sort": 4,
			"tagline": "IP68 & IP69K indicator for food, seafood and washdown rooms.",
			"short": (
				"Heavy-duty waterproof weighing indicator for food processing, seafood, meat, dairy, "
				"livestock and washdown environments. Designed to withstand moisture and intensive cleaning."
			),
			"long": (
				"<p>The HiWEIGH K9 is an IP68 &amp; IP69K waterproof weighing indicator for rooms that "
				"are washed down every shift — meat, seafood, dairy, livestock and hygienic packing. "
				"The housing is PBT+PC with capacitive keys so there are no gaps for water to sit in. "
				"It is the indicator, not the complete bench; see "
				"<a href=\"/products/hiweigh-k9t\">K9T</a> when you need the platform as well.</p>"
				"<p>Official K9 specifications include dual RS232, 1/3,000–1/30,000 internal resolution, "
				"−10 to 40 °C operation, 1–6 × 350 Ω or 1–12 × 750 Ω load-cell drive, and 100–240 V AC "
				"or 9–24 V DC. Bluetooth, Wi-Fi and USB are optional. Do not treat K7 (livestock IP67) "
				"or K7P (printer) as this page.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH K9 IP68 IP69K waterproof weighing indicator",
			"chips": "IP68 · IP69K\nCapacitive keys\nDual RS232\nFood · seafood · dairy",
			"story": "An indicator that can take the hose",
			"visual": "K9 in washdown rooms",
			"card_title": "K9 Indicator",
			"card_summary": "IP68 & IP69K waterproof weighing indicator for food, seafood and washdown lines.",
			"cta_h": "Quote HiWEIGH K9",
			"cta_d": "Tell us the platform, cell count and whether you need Bluetooth, Wi-Fi or USB.",
			"meta_title": "HiWEIGH K9 Waterproof Weighing Indicator Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH K9 IP68 & IP69K waterproof weighing indicator for food, seafood, meat, dairy and washdown rooms. Available from Printechs Saudi Arabia.",
			"app1": "k9",
			"app2": "k9-2",
			"story_labels": ("K9", "Washdown", "In KSA"),
			"story_alts": ("", "K9 in a seafood hall", "K9 commissioning in a Saudi food plant"),
			"story_caps": (
				"Official K9 waterproof indicator — not K7, K7P or K7S.",
				"Built for rooms that are cleaned with high-pressure water.",
				"Specified and supported by Printechs in Saudi Arabia.",
			),
			"icons": [
				{"icon": "rugged", "title": "Protection", "description": "IP68 & IP69K", "sort_order": 1},
				{"icon": "display", "title": "Keys", "description": "Capacitive keypad", "sort_order": 2},
				{"icon": "connectivity", "title": "Ports", "description": "Dual RS232", "sort_order": 3},
				{"icon": "device", "title": "Drive", "description": "1–6 × 350 Ω cells", "sort_order": 4},
			],
			"benefits": [
				{"icon": "rugged", "title": "IP68 & IP69K", "description": "Sealed for moisture and intensive cleaning in food and livestock rooms.", "sort_order": 1},
				{"icon": "display", "title": "Capacitive keys", "description": "No membrane gaps for water to collect after washdown.", "sort_order": 2},
				{"icon": "connectivity", "title": "Dual RS232", "description": "Connect printers, PCs or PLCs; optional Bluetooth, Wi-Fi and USB.", "sort_order": 3},
				{"icon": "shield", "title": "Food-room housing", "description": "PBT+PC enclosure specified for hygienic industrial use.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH K9 waterproof weighing indicator"),
					("Official page", "hiweigh.com/product-details/k9-waterproof-indicator/"),
					("Not this page", "K9T complete bench, K7 livestock, K7P printer, K7S stainless"),
				]),
				("Protection & display", [
					("Ingress", "IP68 and IP69K"),
					("Housing", "PBT+PC; capacitive keys"),
					("Temperature", "−10 to 40 °C operating (official K9 series)"),
				]),
				("Weighing & I/O", [
					("Resolution", "1/3,000 to 1/30,000"),
					("Load cells", "1–6 × 350 Ω or 1–12 × 750 Ω"),
					("Power", "100–240 V AC or 9–24 V DC"),
					("Serial", "Dual RS232; optional Bluetooth, Wi-Fi, USB"),
				]),
			],
			"section_h": "Why K9 instead of a standard indicator",
			"section_b": "A warehouse IP54 indicator will not last on a seafood or meat line. K9 is the washdown electronics; K9T is the complete hygienic bench. We specify cell count and options on the survey.",
			"section_alt": "K9 indicator in a dairy washdown room",
			"pack": [
				{"item_description": "Quoted K9 indicator, power and mounting as surveyed", "sort_order": 1},
				{"item_description": "Platform, cells and options quoted separately", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is K9 the complete scale?", "answer": "No. K9 is the waterproof indicator. K9T is the complete hygienic bench scale.", "sort_order": 1},
				{"question": "How is K9 different from K7?", "answer": "K7 is an IP67 livestock indicator. K9 is IP68/IP69K for high-pressure washdown in food rooms.", "sort_order": 2},
				{"question": "Do you install in Saudi Arabia?", "answer": "Yes. Printechs supplies, installs and supports HiWEIGH K9 in Riyadh, Jeddah, Dammam and other regions.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-k7p",
			"display": "HiWEIGH K7P Weighing Indicator with Printer",
			"card": "k7p",
			"sub": "Weighing Indicators",
			"label": "WEIGHING INDICATOR WITH PRINTER",
			"tagline": "Industrial indicator with a built-in weight-record printer.",
			"short": (
				"Industrial weighing indicator with integrated printer for producing weight records, "
				"labels and receipts. Suitable for warehouses, packing stations and food processing."
			),
			"long": (
				"<p>The HiWEIGH K7P adds a built-in printer to an industrial weighing indicator so the "
				"packing station or warehouse can produce a weight record, label or receipt without a "
				"second device. Official paper width is about 57.5 mm (384 dots / 8 dots/mm). RS232 is "
				"standard; Modbus is optional.</p>"
				"<p>This is not the K9 washdown indicator and not the K7 livestock indicator. Spare-part "
				"codes exist in Desk for K7-family boards — they are not this Website Product. Ask for "
				"the complete K7P indicator, paper roll and the platform you will connect.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH K7P weighing indicator with built-in printer",
			"chips": "Built-in printer\n~57.5 mm paper\nRS232\nWarehouse · packing",
			"story": "Print the weight where you weigh",
			"visual": "K7P at the packing station",
			"card_title": "K7P with printer",
			"card_summary": "Industrial weighing indicator with integrated printer for tickets and receipts.",
			"cta_h": "Quote HiWEIGH K7P",
			"cta_d": "Tell us the platform, ticket format and whether you need Modbus.",
			"meta_title": "HiWEIGH K7P Weighing Indicator with Printer Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH K7P industrial weighing indicator with built-in printer for warehouses, packing stations and food processing. Available from Printechs Saudi Arabia.",
			"app1": "k7p",
			"app2": "k7p-2",
			"story_labels": ("K7P", "Tickets", "In KSA"),
			"story_alts": ("", "K7P printing a weight ticket", "K7P at a Saudi packing station"),
			"story_caps": (
				"Indicator plus printer in one housing.",
				"Weight records at the warehouse or packing bench.",
				"Supplied and supported by Printechs in Saudi Arabia.",
			),
			"icons": [
				{"icon": "print", "title": "Printer", "description": "~57.5 mm thermal", "sort_order": 1},
				{"icon": "connectivity", "title": "Serial", "description": "RS232 · Modbus opt.", "sort_order": 2},
				{"icon": "display", "title": "Use", "description": "Tickets & receipts", "sort_order": 3},
				{"icon": "inventory", "title": "Sites", "description": "Warehouse · packing", "sort_order": 4},
			],
			"benefits": [
				{"icon": "print", "title": "Built-in printer", "description": "Weight records, labels and receipts without a separate printer.", "sort_order": 1},
				{"icon": "speed", "title": "Packing stations", "description": "Useful where every case or portion needs a paper record.", "sort_order": 2},
				{"icon": "connectivity", "title": "RS232", "description": "Connect the platform and optional Modbus devices.", "sort_order": 3},
				{"icon": "store", "title": "Warehouse ready", "description": "A practical indicator when washdown IP69K is not the requirement.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH K7P weighing indicator with printer"),
					("Official page", "hiweigh.com/product-details/k7p-weighing-indicator/"),
					("Not this page", "K9 washdown, K7 livestock, K7S stainless — spare boards are not this SKU"),
				]),
				("Print & I/O", [
					("Paper", "About 57.5 mm; 384 dots / 8 dots/mm"),
					("Serial", "RS232; optional Modbus"),
					("Role", "Weight records, labels and receipts at the station"),
				]),
			],
			"section_h": "When to choose K7P",
			"section_b": "Choose K7P when the operator must leave with a printed weight. Choose K9 when the room is washdown. Choose K7 when the site is a livestock yard.",
			"section_alt": "K7P printing food packing labels",
			"pack": [
				{"item_description": "Quoted K7P indicator with built-in printer", "sort_order": 1},
				{"item_description": "Paper rolls and platform quoted separately", "sort_order": 2},
			],
			"faqs": [
				{"question": "Does K7P include a platform?", "answer": "No. It is the indicator with printer. We quote the matching bench or floor platform separately.", "sort_order": 1},
				{"question": "Is this the K9 washdown indicator?", "answer": "No. K7P is the printer model. K9 is IP68/IP69K washdown.", "sort_order": 2},
				{"question": "Do you supply paper?", "answer": "Yes. We quote genuine-size rolls with the indicator.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-k7",
			"display": "HiWEIGH K7 Livestock Weighing Indicator",
			"card": "k7",
			"sub": "Weighing Indicators",
			"label": "LIVESTOCK WEIGHING INDICATOR",
			"tagline": "Rugged IP67 indicator for cattle and livestock yards.",
			"short": (
				"Rugged IP67 indicator designed specifically for cattle and livestock weighing "
				"where dust, moisture and movement are common."
			),
			"long": (
				"<p>The HiWEIGH K7 is a PBT IP67 livestock weighing indicator with animal-weighing "
				"functions, dual RS232 and 1/3,000–1/30,000 resolution. It is built for dusty, wet "
				"yards — not for high-pressure food-room washdown (that is K9) and not for a built-in "
				"printer (that is K7P).</p>"
				"<p>Pair K7 with <a href=\"/products/hiweigh-ag\">AG cattle crates</a>, "
				"<a href=\"/products/hiweigh-avs\">AVS</a> or <a href=\"/products/hiweigh-aps\">APS</a>. "
				"Desk spare codes for K7 boards are not this Website Product.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH K7 IP67 livestock weighing indicator",
			"chips": "IP67 PBT\nAnimal weighing\nDual RS232\nCattle · sheep · hogs",
			"story": "An indicator that belongs on the farm",
			"visual": "K7 on livestock yards",
			"card_title": "K7 Livestock",
			"card_summary": "IP67 livestock weighing indicator for dusty, wet cattle and farm yards.",
			"cta_h": "Quote HiWEIGH K7",
			"cta_d": "Tell us the crate or load bars and whether you need animal-hold firmware options.",
			"meta_title": "HiWEIGH K7 Livestock Weighing Indicator Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH K7 IP67 livestock weighing indicator for cattle and farm yards. Available from Printechs Saudi Arabia.",
			"app1": "k7",
			"app2": "k7-2",
			"story_labels": ("K7", "Yards", "In KSA"),
			"story_alts": ("", "K7 on a farm post", "K7 on a Saudi cattle farm"),
			"story_caps": (
				"Livestock firmware in an IP67 housing.",
				"Dust, moisture and animal movement are expected.",
				"Installed with crates and load bars by Printechs.",
			),
			"icons": [
				{"icon": "rugged", "title": "Protection", "description": "IP67 PBT housing", "sort_order": 1},
				{"icon": "device", "title": "Firmware", "description": "Animal weighing", "sort_order": 2},
				{"icon": "connectivity", "title": "Ports", "description": "Dual RS232", "sort_order": 3},
				{"icon": "inventory", "title": "Pair with", "description": "AG · AVS · APS", "sort_order": 4},
			],
			"benefits": [
				{"icon": "rugged", "title": "IP67 farm housing", "description": "PBT enclosure for dust, moisture and yard use.", "sort_order": 1},
				{"icon": "speed", "title": "Animal weighing", "description": "Firmware intended for livestock that will not stand still.", "sort_order": 2},
				{"icon": "connectivity", "title": "Dual RS232", "description": "Connect printers or farm software when required.", "sort_order": 3},
				{"icon": "integration", "title": "Crate ready", "description": "Specify with AG, AVS or APS — not as a spare board.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH K7 livestock weighing indicator"),
					("Official page", "hiweigh.com/product-details/k7-weight-indicator/"),
					("Not this page", "K9 washdown, K7P printer, K7S stainless; spare Items are not this page"),
				]),
				("Weighing", [
					("Ingress", "IP67 PBT housing"),
					("Resolution", "1/3,000 to 1/30,000"),
					("Serial", "Dual RS232"),
					("Use", "Cattle and livestock yards"),
				]),
			],
			"section_h": "K7 with a crate, not on its own",
			"section_b": "The indicator is only half the system. We quote K7 with the crate or load bars that match the animals — AG for cattle, AVS for sheep/goats/hogs, APS for pigs.",
			"section_alt": "K7 indicator beside a cattle race",
			"pack": [
				{"item_description": "Quoted K7 livestock indicator and mounting", "sort_order": 1},
				{"item_description": "Crate, load bars and cells quoted to the animals", "sort_order": 2},
			],
			"faqs": [
				{"question": "Can I use K7 in a meat plant washdown room?", "answer": "Use K9 or K9T for IP68/IP69K food-room washdown. K7 is the livestock IP67 indicator.", "sort_order": 1},
				{"question": "Does this page include the cattle crate?", "answer": "No. See the AG, AVS or APS pages for the mechanical system.", "sort_order": 2},
				{"question": "Do you install on farms in Saudi Arabia?", "answer": "Yes. Printechs supplies and supports HiWEIGH livestock systems across the Kingdom.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-k7s",
			"display": "HiWEIGH K7S Stainless Steel Weighing Indicator",
			"card": "k7s",
			"sub": "Weighing Indicators",
			"label": "STAINLESS STEEL WEIGHT INDICATOR",
			"tagline": "SUS304 industrial indicator for warehouse and farm platforms.",
			"short": (
				"Stainless-steel industrial indicator suitable for demanding warehouse, "
				"agricultural and industrial applications."
			),
			"long": (
				"<p>The HiWEIGH K7S is a SUS304 stainless industrial indicator with a 37 mm FSTN "
				"display, dual RS232, and IP54 or IP65 depending on configuration. It is the stainless "
				"general-purpose indicator — not the K9 high-pressure washdown unit and not the K7 "
				"livestock firmware package.</p>"
				"<p>Use K7S on warehouse and agricultural platforms such as "
				"<a href=\"/products/hiweigh-bsw\">BSW</a> when the room is demanding but not a "
				"hose-down food hall. Spare-part Items for K7S are not this Website Product.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH K7S stainless steel weighing indicator",
			"chips": "SUS304\nIP54 or IP65\n37 mm FSTN\nDual RS232",
			"story": "Stainless indicator for industrial platforms",
			"visual": "K7S in warehouses",
			"card_title": "K7S Stainless",
			"card_summary": "SUS304 industrial weighing indicator for warehouse and agricultural platforms.",
			"cta_h": "Quote HiWEIGH K7S",
			"cta_d": "Confirm IP54 vs IP65 and the platform you will connect.",
			"meta_title": "HiWEIGH K7S Stainless Steel Weighing Indicator Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH K7S stainless-steel industrial weighing indicator for warehouse and agricultural platforms. Available from Printechs Saudi Arabia.",
			"app1": "k7s",
			"app2": "k7s-2",
			"story_labels": ("K7S", "Platforms", "In KSA"),
			"story_alts": ("", "K7S on a warehouse column", "K7S in a Saudi warehouse"),
			"story_caps": (
				"SUS304 housing with a large FSTN display.",
				"Pair with industrial platforms, not livestock crates by default.",
				"Specified by Printechs for Saudi warehouses and farms.",
			),
			"icons": [
				{"icon": "durability", "title": "Housing", "description": "SUS304 stainless", "sort_order": 1},
				{"icon": "display", "title": "Display", "description": "37 mm FSTN", "sort_order": 2},
				{"icon": "rugged", "title": "Ingress", "description": "IP54 or IP65", "sort_order": 3},
				{"icon": "connectivity", "title": "Ports", "description": "Dual RS232", "sort_order": 4},
			],
			"benefits": [
				{"icon": "durability", "title": "SUS304 housing", "description": "Stainless indicator for industrial and agricultural rooms.", "sort_order": 1},
				{"icon": "display", "title": "Large FSTN", "description": "37 mm digits that stay readable on the warehouse floor.", "sort_order": 2},
				{"icon": "rugged", "title": "IP54 / IP65", "description": "Choose the sealing that matches dust and splash — not IP69K washdown.", "sort_order": 3},
				{"icon": "connectivity", "title": "Dual RS232", "description": "Printers and PCs without moving to K7P unless you need built-in print.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH K7S stainless steel weight indicator"),
					("Official page", "hiweigh.com/product-details/k7s-weight-indicator/"),
					("Not this page", "K9 IP69K, K7 livestock, K7P printer"),
				]),
				("Construction", [
					("Material", "SUS304 stainless housing"),
					("Display", "37 mm FSTN"),
					("Ingress", "IP54 or IP65 depending on configuration"),
					("Serial", "Dual RS232"),
				]),
			],
			"section_h": "K7S is not a washdown K9",
			"section_b": "If the room is high-pressure washed, specify K9 or K9T. K7S is the stainless general indicator for warehouses, farms and industrial platforms.",
			"section_alt": "K7S indicator weighing feed bags",
			"pack": [
				{"item_description": "Quoted K7S indicator, column or wall mount", "sort_order": 1},
				{"item_description": "Platform and cells quoted separately", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is K7S IP69K?", "answer": "No. Official options are IP54 or IP65. Use K9 for IP68/IP69K washdown.", "sort_order": 1},
				{"question": "Does it include a printer?", "answer": "No. See K7P for a built-in printer.", "sort_order": 2},
				{"question": "Can it drive a BSW platform?", "answer": "Yes — we quote K7S with BSW or similar industrial platforms.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-bxt",
			"display": "HiWEIGH BXT IP68 IP69K Washdown Platform",
			"card": "bxt",
			"sub": "Waterproof & Hygienic Scales",
			"label": "WASHDOWN WEIGHING PLATFORM",
			"featured": 1,
			"featured_sort": 5,
			"tagline": "Open-frame stainless platform that does not hold water.",
			"short": (
				"Hygienic stainless-steel weighing platform with an open construction designed to "
				"prevent water accumulation and allow intensive cleaning."
			),
			"long": (
				"<p>The HiWEIGH BXT is an open-frame hygienic washdown platform. Water drains instead "
				"of pooling, which is why food and pharma rooms specify it instead of a closed mild-steel "
				"deck. Official options include SUS304 or SUS316, capacities up to about 300 kg, and "
				"IP67 or IP68/IP69K load cells.</p>"
				"<p>BXT is the platform. Pair it with <a href=\"/products/hiweigh-k9\">K9</a> or order "
				"the complete <a href=\"/products/hiweigh-k9t\">K9T</a> bench. It is not a floor scale "
				"(see FWR) and not a sealed BHB bench.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH BXT open-frame washdown weighing platform",
			"chips": "Open-frame stainless\nIP67 or IP68/IP69K cells\nUp to ~300 kg\nFood · pharma",
			"story": "A platform you can actually wash",
			"visual": "BXT open-frame hygiene",
			"card_title": "BXT Washdown",
			"card_summary": "Open-frame stainless washdown platform for hygienic food and pharma rooms.",
			"cta_h": "Quote HiWEIGH BXT",
			"cta_d": "Confirm capacity, SUS304 vs 316, cell IP rating and the indicator.",
			"meta_title": "HiWEIGH BXT IP68 IP69K Washdown Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH BXT open-frame IP68/IP69K washdown weighing platform for hygienic food and pharmaceutical rooms. Available from Printechs Saudi Arabia.",
			"app1": "bxt",
			"app2": "bxt-2",
			"story_labels": ("BXT", "Washdown", "In KSA"),
			"story_alts": ("", "BXT being washed down", "BXT in a Saudi hygienic plant"),
			"story_caps": (
				"Open construction so water does not sit on the frame.",
				"Intensive cleaning without a sealed mild-steel box.",
				"Specified by Printechs for Saudi food and pharma rooms.",
			),
			"icons": [
				{"icon": "durability", "title": "Frame", "description": "Open SUS304 / 316", "sort_order": 1},
				{"icon": "rugged", "title": "Cells", "description": "IP67 or IP68/IP69K", "sort_order": 2},
				{"icon": "inventory", "title": "Capacity", "description": "Up to about 300 kg", "sort_order": 3},
				{"icon": "device", "title": "Pair with", "description": "K9 or complete K9T", "sort_order": 4},
			],
			"benefits": [
				{"icon": "durability", "title": "Open frame", "description": "Designed so wash water drains instead of pooling.", "sort_order": 1},
				{"icon": "rugged", "title": "Hygienic cells", "description": "IP67 or IP68/IP69K load-cell options.", "sort_order": 2},
				{"icon": "shield", "title": "SUS304 / 316", "description": "Specify 316 when chlorides or aggressive chemistry are present.", "sort_order": 3},
				{"icon": "integration", "title": "K9 ready", "description": "Complete as K9T when you want indicator and platform together.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH BXT washdown platform"),
					("Official page", "hiweigh.com/product-details/bxt-washdown-platform-scale/"),
					("Not this page", "K9T complete bench, BHB sealed bench, FWR hygienic floor"),
				]),
				("Construction", [
					("Frame", "Open hygienic stainless; SUS304 or SUS316"),
					("Capacity", "Up to approximately 300 kg depending on configuration"),
					("Load cells", "IP67 or IP68/IP69K options"),
				]),
			],
			"section_h": "Open frame versus a closed bench",
			"section_b": "Closed platforms hold water and product. BXT is specified where inspectors expect an open, cleanable structure. Ask for K9T if you want the matching waterproof indicator already mounted.",
			"section_alt": "BXT platform on a meat packing table",
			"pack": [
				{"item_description": "Quoted BXT platform, size and cell rating", "sort_order": 1},
				{"item_description": "K9 indicator or complete K9T quoted as required", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is BXT a complete scale?", "answer": "It is the washdown platform. Add K9, or order K9T as a complete bench.", "sort_order": 1},
				{"question": "SUS304 or 316?", "answer": "304 is the usual food-room choice. We quote 316 for harsher chemistry.", "sort_order": 2},
				{"question": "Can it take a floor-scale load?", "answer": "No. BXT is a bench/platform family up to about 300 kg. See FD or FWR for floors.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-k9t",
			"display": "HiWEIGH K9T Waterproof Bench Scale",
			"item": "IND.SYS.HIW.4002",
			"card": "k9t",
			"sub": "Waterproof & Hygienic Scales",
			"label": "WATERPROOF HYGIENIC BENCH SCALE",
			"featured": 1,
			"featured_sort": 1,
			"tagline": "K9 electronics on a hygienic bench — IP68 & IP69K.",
			"short": (
				"Complete waterproof bench scale combining the K9 indicator with a heavy-duty hygienic "
				"weighing platform. Available from approximately 6 kg to 150 kg configurations."
			),
			"long": (
				"<p>HiWEIGH K9T is the complete hygienic bench: the K9 IP68/IP69K indicator plus a "
				"heavy-duty washdown platform. Official sizes include 300 mm, 400 mm and 400 × 500 mm "
				"pans and capacities from about 6 kg to 150 kg. The display is a 30 mm FSTN with dual "
				"RS232.</p>"
				"<p>This page is the stocked configuration <strong>IND.SYS.HIW.4002</strong> — K9T5150 "
				"150 kg × 20 g. A 60 kg K9T5060 is quoted as <strong>IND.SYS.HIW.4001</strong> and is "
				"not mixed onto this Item. K9T is the washdown bench; FOD is the affordable stainless "
				"bench that is not high-pressure washdown.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH K9T IP68 IP69K hygienic waterproof bench scale",
			"chips": "K9T5150 · 150 kg × 20 g\nIP68 · IP69K\n6–150 kg family\nMeat · seafood · dairy · pharma",
			"story": "The hygienic bench for rooms that get hosed",
			"visual": "K9T on washdown lines",
			"card_title": "K9T Bench",
			"card_summary": "IP68 & IP69K waterproof hygienic bench scale. This page is the 150 kg K9T5150.",
			"cta_h": "Quote HiWEIGH K9T",
			"cta_d": "Confirm 60 kg vs 150 kg, pan size and whether the room needs SUS316.",
			"meta_title": "HiWEIGH K9T Waterproof Bench Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH K9T IP68 & IP69K waterproof bench scale for hygienic weighing in food, meat, seafood, dairy, pharmaceutical and industrial applications. Available from Printechs Saudi Arabia.",
			"app1": "k9t",
			"app2": "k9t-2",
			"story_labels": ("K9T", "Hygiene", "In KSA"),
			"story_alts": ("", "K9T in a hygienic packing room", "K9T in a Saudi meat plant"),
			"story_caps": (
				"Complete waterproof bench — indicator and platform.",
				"Specified for meat, seafood, dairy and washdown packing.",
				"This Item is K9T5150 150 kg; 60 kg is quoted separately.",
			),
			"icons": [
				{"icon": "rugged", "title": "Protection", "description": "IP68 & IP69K", "sort_order": 1},
				{"icon": "inventory", "title": "This Item", "description": "150 kg × 20 g", "sort_order": 2},
				{"icon": "display", "title": "Display", "description": "30 mm FSTN", "sort_order": 3},
				{"icon": "connectivity", "title": "Ports", "description": "2 × RS232", "sort_order": 4},
			],
			"benefits": [
				{"icon": "rugged", "title": "True washdown bench", "description": "IP68/IP69K electronics and a hygienic platform in one system.", "sort_order": 1},
				{"icon": "shield", "title": "Food and pharma rooms", "description": "Meat, seafood, dairy, bakery and pharmaceutical packing.", "sort_order": 2},
				{"icon": "inventory", "title": "6–150 kg family", "description": "This page is 150 kg × 20 g; 60 kg is a different Item.", "sort_order": 3},
				{"icon": "connectivity", "title": "Dual RS232", "description": "Printers and PCs without treating K7P as this SKU.", "sort_order": 4},
			],
			"specs": [
				("This configuration", [
					("Item on this page", "IND.SYS.HIW.4002 — K9T5150 150 kg × 20 g"),
					("Also quote", "IND.SYS.HIW.4001 is K9T5060 60 kg × 10 g — different Item"),
					("Official page", "hiweigh.com/product-details/k9t-ip68-ip69k-scale-hygienic-weighing/"),
					("Not this page", "FOD affordable bench, BHB sealed bench, BXT platform-only"),
				]),
				("Weighing", [
					("Family capacities", "Approximately 6 kg to 150 kg"),
					("Pans", "300 mm, 400 mm, 400 × 500 mm typical"),
					("Ingress", "IP68 and IP69K"),
					("Display", "FSTN 30 mm; 2 × RS232"),
				]),
			],
			"section_h": "K9T is the washdown differentiator",
			"section_b": "If the scale will be high-pressure cleaned, do not buy a standard stainless bench and hope. K9T is the hygienic complete scale. FOD and BHB are different families.",
			"section_alt": "K9T bench scale in a bakery washdown room",
			"pack": [
				{"item_description": "K9T5150 150 kg × 20 g as Item IND.SYS.HIW.4002", "sort_order": 1},
				{"item_description": "60 kg K9T5060 and other pans quoted on request", "sort_order": 2},
			],
			"faqs": [
				{"question": "150 kg or 60 kg?", "answer": "This page is IND.SYS.HIW.4002 (150 kg × 20 g). Ask for 4001 if you need 60 kg × 10 g.", "sort_order": 1},
				{"question": "Is FOD the same scale?", "answer": "No. FOD is an affordable multi-function bench. It is not high-pressure washdown.", "sort_order": 2},
				{"question": "Do you install in food plants?", "answer": "Yes. Printechs specifies, installs and supports K9T in Saudi food, dairy and pharma rooms.", "sort_order": 3},
			],
		},
	]


def more_pages():
	"""Remaining 16 family pages."""
	return [
		{
			"slug": "hiweigh-bhb",
			"display": "HiWEIGH BHB Stainless Steel Bench Scale",
			"card": "bhb",
			"sub": "Bench & Platform Scales",
			"label": "STAINLESS STEEL BENCH SCALE",
			"tagline": "Sealed hygienic bench for food, pharma and chemicals.",
			"short": (
				"Hygienic corrosion-resistant bench scale designed for food, pharmaceutical "
				"and chemical weighing applications."
			),
			"long": (
				"<p>The HiWEIGH BHB is a sealed SUS304 stainless bench (optional SUS316) for food, "
				"pharmaceutical and chemical rooms. Official capacity is up to about 100 kg, with "
				"OIML/NTEP load cells and IP65 / IP67 / IP68 &amp; IP69K cell options. Four anti-slip "
				"feet and overload protection are standard on the official page.</p>"
				"<p>BHB is a sealed bench, not the open-frame BXT and not the complete K9T washdown "
				"system. Choose K9T when the whole scale — indicator included — must take the hose.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH BHB stainless steel hygienic bench scale",
			"chips": "100% SUS304\nUp to ~100 kg\nOIML/NTEP cells\nFood · pharma · chemical",
			"story": "Sealed stainless for corrosive benches",
			"visual": "BHB in hygienic rooms",
			"card_title": "BHB Bench",
			"card_summary": "Sealed SUS304 hygienic bench scale for food, pharmaceutical and chemical rooms.",
			"cta_h": "Quote HiWEIGH BHB",
			"cta_d": "Confirm capacity, SUS304 vs 316 and the load-cell IP rating.",
			"meta_title": "HiWEIGH BHB Stainless Steel Bench Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH BHB hygienic stainless-steel bench scale for food, pharmaceutical and chemical weighing. Available from Printechs Saudi Arabia.",
			"app1": "bhb",
			"app2": "bhb-2",
			"story_labels": ("BHB", "Pharma", "In KSA"),
			"story_alts": ("", "BHB on a process bench", "BHB in a Saudi pharma room"),
			"story_caps": (
				"Sealed stainless bench — not an open BXT frame.",
				"Food, pharmaceutical and chemical weighing.",
				"Quoted by Printechs for Saudi process rooms.",
			),
			"icons": [
				{"icon": "durability", "title": "Body", "description": "SUS304 (316 opt.)", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "Up to about 100 kg", "sort_order": 2},
				{"icon": "shield", "title": "Cells", "description": "OIML / NTEP", "sort_order": 3},
				{"icon": "rugged", "title": "IP options", "description": "IP65 to IP69K cells", "sort_order": 4},
			],
			"benefits": [
				{"icon": "durability", "title": "All-stainless", "description": "Structure, pan and feet in SUS304; 316 quoted for harsher chemistry.", "sort_order": 1},
				{"icon": "shield", "title": "Approved cells", "description": "OIML/NTEP load cells with several waterproof options.", "sort_order": 2},
				{"icon": "rugged", "title": "Sealed bench", "description": "Different from BXT open-frame and from K9T complete washdown.", "sort_order": 3},
				{"icon": "inventory", "title": "To ~100 kg", "description": "A bench family — not a 5 t floor scale.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH BHB stainless steel bench scale"),
					("Official page", "hiweigh.com/product-details/bhb/"),
					("Not this page", "K9T washdown bench, BXT open platform, FOD multi-function bench"),
				]),
				("Construction", [
					("Material", "100% SUS304 structure, pan and feet; optional SUS316"),
					("Capacity", "Up to approximately 100 kg"),
					("Load cells", "OIML/NTEP; IP65, IP67 or IP68 & IP69K options"),
					("Feet", "Four anti-slip adjusting feet; overload protection"),
				]),
			],
			"section_h": "Sealed BHB versus washdown K9T",
			"section_b": "BHB is a sealed hygienic bench with selectable cell IP ratings. If the entire indicator must take a high-pressure hose, specify K9T instead.",
			"section_alt": "BHB scale in a pharmaceutical room",
			"pack": [
				{"item_description": "Quoted BHB bench, capacity and cell IP rating", "sort_order": 1},
				{"item_description": "SUS316 and indicator options quoted on request", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is BHB the same as K9T?", "answer": "No. K9T is the complete IP68/IP69K washdown bench. BHB is a sealed stainless bench family.", "sort_order": 1},
				{"question": "What capacity?", "answer": "Official BHB capacity is up to about 100 kg. We confirm the exact range on the quote.", "sort_order": 2},
				{"question": "Food or pharma?", "answer": "Both. We also quote BHB for chemical rooms that need corrosion resistance.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-bsw",
			"display": "HiWEIGH BSW OIML Industrial Platform Scale",
			"item": "IND.SYS.HIW.0737",
			"card": "bsw",
			"sub": "Bench & Platform Scales",
			"label": "OIML INDUSTRIAL PLATFORM SCALE",
			"tagline": "Mild-steel frame, stainless top, legal-for-trade cells.",
			"short": (
				"Industrial platform featuring a mild-steel frame, SUS304 stainless top and IP65 "
				"protection, with capacities reaching approximately 1,000 kg depending on configuration."
			),
			"long": (
				"<p>The HiWEIGH BSW is an OIML industrial platform: mild-steel frame, SUS304 top and "
				"IP65 protection. Official capacities typically run to 600 kg with an optional 1,000 kg "
				"class. Load cells are OIML/NTEP.</p>"
				"<p>This page is <strong>IND.SYS.HIW.0737</strong> — BSW (SQ) 600 × 600 mm, 500 kg. "
				"Other sizes are quoted, not mixed onto this Item. BSW is not a 5 t floor scale "
				"(see FD) and not a washdown hygienic bench (see K9T).</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH BSW OIML industrial platform scale",
			"chips": "600 × 600 mm · 500 kg\nOIML / NTEP cells\nIP65\nMild steel + SUS304 top",
			"story": "A legal-for-trade factory platform",
			"visual": "BSW on the factory floor",
			"card_title": "BSW Platform",
			"card_summary": "OIML industrial platform. This page is 600 × 600 mm / 500 kg.",
			"cta_h": "Quote HiWEIGH BSW",
			"cta_d": "Confirm 600 mm vs other sizes and 500 kg vs higher capacities.",
			"meta_title": "HiWEIGH BSW OIML Industrial Platform Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH BSW OIML industrial platform scale with mild-steel frame and SUS304 top. This page is the 600 × 600 mm 500 kg configuration from Printechs Saudi Arabia.",
			"app1": "bsw",
			"app2": "bsw-2",
			"story_labels": ("BSW", "Factory", "In KSA"),
			"story_alts": ("", "BSW in a factory", "BSW in a Saudi factory"),
			"story_caps": (
				"This Item is 600 × 600 mm / 500 kg.",
				"OIML/NTEP cells for industrial and warehouse work.",
				"Other BSW sizes are quoted separately.",
			),
			"icons": [
				{"icon": "inventory", "title": "This Item", "description": "600 mm · 500 kg", "sort_order": 1},
				{"icon": "shield", "title": "Approval", "description": "OIML / NTEP cells", "sort_order": 2},
				{"icon": "rugged", "title": "Ingress", "description": "IP65", "sort_order": 3},
				{"icon": "durability", "title": "Deck", "description": "SUS304 on mild steel", "sort_order": 4},
			],
			"benefits": [
				{"icon": "shield", "title": "OIML cells", "description": "Legal-for-trade load cells on an industrial platform.", "sort_order": 1},
				{"icon": "durability", "title": "Practical deck", "description": "Mild-steel frame with a stainless top — not a hygienic open frame.", "sort_order": 2},
				{"icon": "inventory", "title": "To ~1,000 kg", "description": "Family capacity; this Item is 500 kg.", "sort_order": 3},
				{"icon": "integration", "title": "Indicator choice", "description": "Often paired with K7S; K9 when the room is washdown.", "sort_order": 4},
			],
			"specs": [
				("This configuration", [
					("Item on this page", "IND.SYS.HIW.0737 — BSW 600 × 600 mm, 500 kg"),
					("Also quote", "Other BSW sizes and the optional ~1,000 kg class"),
					("Official page", "hiweigh.com/product-details/bsw-oiml-weighing-platform/"),
					("Not this page", "FD floor scale, K9T washdown bench, FOD compact bench"),
				]),
				("Construction", [
					("Frame / top", "Mild-steel frame, SUS304 stainless top"),
					("Ingress", "IP65"),
					("Family capacity", "Typically to 600 kg; optional about 1,000 kg"),
					("Load cells", "OIML / NTEP"),
				]),
			],
			"section_h": "Platform, not a floor scale",
			"section_b": "BSW sits on the floor or a low stand and is quoted by pan size. Pallet and 3–5 t work belongs on FD, FDL or FWR.",
			"section_alt": "BSW platform used for warehouse receiving",
			"pack": [
				{"item_description": "BSW 600 × 600 mm 500 kg as Item IND.SYS.HIW.0737", "sort_order": 1},
				{"item_description": "Indicator and other sizes quoted separately", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is this 500 kg only?", "answer": "This page is Item 0737 (500 kg, 600 × 600 mm). Other BSW sizes are quoted.", "sort_order": 1},
				{"question": "OIML approved?", "answer": "Official BSW uses OIML/NTEP load cells. We confirm the approval needed for your trade use.", "sort_order": 2},
				{"question": "Can I wash it like K9T?", "answer": "IP65 is splash protection, not IP69K washdown. Use K9T or BXT for hose-down rooms.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-fod",
			"display": "HiWEIGH FOD Stainless Steel Bench Scale",
			"card": "fod",
			"sub": "Bench & Platform Scales",
			"label": "STAINLESS STEEL BENCH SCALE",
			"tagline": "Affordable multi-function bench — 6 to 150 kg.",
			"short": (
				"Multi-function bench scale for food weighing, packaging, inventory counting and "
				"batching. Capacities include 6, 15, 30, 60 and 150 kg models."
			),
			"long": (
				"<p>The HiWEIGH FOD is an affordable stainless multi-function bench for food packing, "
				"inventory counting and simple batching. Official capacities are 6, 15, 30, 60 and "
				"150 kg on an approximately 315 × 315 mm pan, with an IP66 load cell and a K7S-class "
				"indicator.</p>"
				"<p>FOD is not high-pressure washdown. If the room is hosed every shift, specify "
				"<a href=\"/products/hiweigh-k9t\">K9T</a>. FOD is the practical bench for bakeries, "
				"packing tables and stores that need stainless without IP69K.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH FOD affordable stainless steel bench scale",
			"chips": "6 / 15 / 30 / 60 / 150 kg\n~315 × 315 mm\nIP66 cell\nPack · count · batch",
			"story": "Everyday stainless bench weighing",
			"visual": "FOD on packing tables",
			"card_title": "FOD Bench",
			"card_summary": "Affordable stainless multi-function bench, 6–150 kg. Not a washdown K9T.",
			"cta_h": "Quote HiWEIGH FOD",
			"cta_d": "Pick 6, 15, 30, 60 or 150 kg and tell us if you need counting or batching.",
			"meta_title": "HiWEIGH FOD Stainless Steel Bench Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH FOD stainless steel bench scale for food packing, counting and batching. 6–150 kg models from Printechs Saudi Arabia.",
			"app1": "fod",
			"app2": "fod-2",
			"story_labels": ("FOD", "Packing", "In KSA"),
			"story_alts": ("", "FOD used for food packing", "FOD in a Saudi bakery"),
			"story_caps": (
				"Affordable stainless bench — not K9T washdown.",
				"Portioning, counting and simple batching.",
				"Quoted by capacity; family page, not one spare Item.",
			),
			"icons": [
				{"icon": "inventory", "title": "Capacities", "description": "6–150 kg family", "sort_order": 1},
				{"icon": "device", "title": "Pan", "description": "~315 × 315 mm", "sort_order": 2},
				{"icon": "rugged", "title": "Cell", "description": "IP66", "sort_order": 3},
				{"icon": "display", "title": "Indicator", "description": "K7S-class", "sort_order": 4},
			],
			"benefits": [
				{"icon": "inventory", "title": "Five capacities", "description": "6, 15, 30, 60 and 150 kg — quoted as the size you need.", "sort_order": 1},
				{"icon": "speed", "title": "Count and batch", "description": "Multi-function firmware for packing and inventory checks.", "sort_order": 2},
				{"icon": "durability", "title": "Stainless bench", "description": "Practical food-room stainless, not IP69K washdown.", "sort_order": 3},
				{"icon": "store", "title": "Compact pan", "description": "About 315 × 315 mm for packing tables.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH FOD stainless steel bench scale"),
					("Official page", "hiweigh.com/product-details/fod-bench-scale/"),
					("Not this page", "K9T IP69K washdown bench, BHB sealed hygienic bench"),
				]),
				("Weighing", [
					("Capacities", "6, 15, 30, 60 and 150 kg"),
					("Platform", "Approximately 315 × 315 mm"),
					("Load cell", "IP66"),
					("Indicator", "K7S-class (not K9 washdown electronics)"),
				]),
			],
			"section_h": "Affordable bench, not washdown",
			"section_b": "FOD is the everyday stainless bench. If inspectors or hygiene rules require high-pressure cleaning of the whole scale, move to K9T.",
			"section_alt": "FOD scale portioning bakery trays",
			"pack": [
				{"item_description": "Quoted FOD bench in the chosen capacity", "sort_order": 1},
				{"item_description": "Counting / batching setup as specified", "sort_order": 2},
			],
			"faqs": [
				{"question": "Which capacity do I need?", "answer": "Official FOD sizes are 6, 15, 30, 60 and 150 kg. We confirm readability on the quote.", "sort_order": 1},
				{"question": "Can I hose it like K9T?", "answer": "No. FOD uses an IP66 cell and a K7S-class indicator. Use K9T for IP68/IP69K washdown.", "sort_order": 2},
				{"question": "Does it count pieces?", "answer": "Yes — FOD is specified as a multi-function bench including inventory counting.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-fd",
			"display": "HiWEIGH FD Heavy-Duty Industrial Floor Scale",
			"item": "IND.SYS.HIW.0746",
			"card": "fd",
			"sub": "Floor Scales",
			"label": "HEAVY-DUTY FLOOR SCALE",
			"featured": 1,
			"featured_sort": 6,
			"tagline": "U-beam floor scale — this page is 1.5 × 1.5 m / 5 t.",
			"short": (
				"Heavy-duty U-beam floor scale available in multiple platform dimensions and "
				"capacities up to 5,000 kg, suitable for warehouses and manufacturing facilities."
			),
			"long": (
				"<p>The HiWEIGH FD is a carbon-steel U-beam floor scale for palletised and bulk goods. "
				"Official capacities include 1.5, 3 and 5 t with platform sizes from about 1.0 to 2.0 m "
				"and four IP67 shear-beam cells.</p>"
				"<p>This page is <strong>IND.SYS.HIW.0746</strong> — FD1550M 1.5 × 1.5 m, 5,000 kg. "
				"Other FD sizes (including 0744, 0745, 0747, 0748, 2077, 2078) are quoted, not mixed "
				"onto this Item. Need dual ramps? See FDL. Need stainless hygiene? See FWR.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH FD heavy-duty industrial floor scale",
			"chips": "FD1550M · 1.5 × 1.5 m\n5,000 kg\nU-beam carbon steel\n4 × IP67 shear beam",
			"story": "The warehouse floor scale",
			"visual": "FD under pallets",
			"card_title": "FD Floor Scale",
			"card_summary": "Heavy-duty U-beam floor scale. This page is 1.5 × 1.5 m / 5,000 kg.",
			"cta_h": "Quote HiWEIGH FD",
			"cta_d": "Confirm deck size and 1.5 / 3 / 5 t. Other FD Items are quoted separately.",
			"meta_title": "HiWEIGH FD Heavy Duty Floor Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH FD heavy-duty industrial floor scale up to 5,000 kg for warehouses and manufacturing. This page is the 1.5 × 1.5 m 5 t configuration from Printechs Saudi Arabia.",
			"app1": "fd",
			"app2": "fd-2",
			"story_labels": ("FD", "Pallets", "In KSA"),
			"story_alts": ("", "FD weighing a warehouse pallet", "FD in a Saudi warehouse"),
			"story_caps": (
				"This Item is FD1550M 1.5 × 1.5 m / 5 t.",
				"U-beam carbon steel for warehouse and factory floors.",
				"Other FD sizes stay on their own Items.",
			),
			"icons": [
				{"icon": "inventory", "title": "This Item", "description": "5,000 kg · 1.5 m", "sort_order": 1},
				{"icon": "durability", "title": "Frame", "description": "U-beam carbon steel", "sort_order": 2},
				{"icon": "rugged", "title": "Cells", "description": "4 × IP67 shear beam", "sort_order": 3},
				{"icon": "device", "title": "Family", "description": "1.5 / 3 / 5 t", "sort_order": 4},
			],
			"benefits": [
				{"icon": "inventory", "title": "Up to 5 t", "description": "This configuration is 5,000 kg on a 1.5 × 1.5 m deck.", "sort_order": 1},
				{"icon": "durability", "title": "U-beam deck", "description": "Carbon-steel industrial floor scale, not a hygienic stainless pit.", "sort_order": 2},
				{"icon": "rugged", "title": "IP67 cells", "description": "Four shear-beam load cells for warehouse and factory use.", "sort_order": 3},
				{"icon": "integration", "title": "Size options", "description": "Other FD decks are quoted — they are not this Item.", "sort_order": 4},
			],
			"specs": [
				("This configuration", [
					("Item on this page", "IND.SYS.HIW.0746 — FD1550M 1.5 × 1.5 m, 5,000 kg"),
					("Also quote", "Other FD sizes: 0744, 0745, 0747, 0748, 2077, 2078"),
					("Official page", "hiweigh.com/product-details/fd-floor-scale/"),
					("Not this page", "FDL dual-ramp, FWR hygienic stainless, BSW 500 kg platform"),
				]),
				("Construction", [
					("Frame", "U-beam carbon steel"),
					("Family capacities", "1.5 / 3 / 5 t"),
					("Family sizes", "About 1.0–2.0 m decks"),
					("Load cells", "4 × IP67 shear beam"),
				]),
			],
			"section_h": "Heavy floor scale, one Item at a time",
			"section_b": "A 1.2 m deck is not this 1.5 m / 5 t Item. We quote the size you need and keep the SKUs separate so receiving and service stay clear.",
			"section_alt": "FD floor scale at a factory receiving dock",
			"pack": [
				{"item_description": "FD1550M 1.5 × 1.5 m 5,000 kg as Item IND.SYS.HIW.0746", "sort_order": 1},
				{"item_description": "Indicator, ramps and other FD sizes quoted separately", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is every FD 5 tonnes?", "answer": "No. The family includes 1.5, 3 and 5 t. This page is the 5 t / 1.5 × 1.5 m Item.", "sort_order": 1},
				{"question": "Do I need ramps?", "answer": "FD is the flat U-beam deck. FDL adds dual ramps for pallet jacks.", "sort_order": 2},
				{"question": "Stainless food version?", "answer": "See FWR (and stocked FW hygienic floors) for wet food rooms.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-fdl",
			"display": "HiWEIGH FDL Low-Profile Floor Scale",
			"card": "fdl",
			"sub": "Floor Scales",
			"label": "LOW-PROFILE FLOOR SCALE",
			"featured": 1,
			"featured_sort": 7,
			"tagline": "Dual ramps, low deck — pallet jacks roll on.",
			"short": (
				"Rugged carbon-steel floor scale with dual ramps for easy pallet and trolley access. "
				"Designed for warehouses, logistics and production facilities."
			),
			"long": (
				"<p>The HiWEIGH FDL is a low-profile carbon-steel floor scale with dual 300 mm ramps "
				"so pallet jacks and trolleys can roll on without a pit. Official capacities are 1.5 t "
				"and 3 t with 1,200 mm or 1,500 mm decks.</p>"
				"<p>FDL is not the 5 t U-beam FD and not the stainless hygienic FWR. There is no single "
				"Desk system Item locked to this family page — we quote the deck and capacity you need.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH FDL low-profile floor scale with dual ramps",
			"chips": "Dual 300 mm ramps\n1.5 t / 3 t\n1200 or 1500 mm\nNo pit required",
			"story": "Drive-on weighing without a pit",
			"visual": "FDL with pallet-jack access",
			"card_title": "FDL Low Profile",
			"card_summary": "Low-profile carbon-steel floor scale with dual ramps for pallet-jack access.",
			"cta_h": "Quote HiWEIGH FDL",
			"cta_d": "Confirm 1.2 vs 1.5 m deck and 1.5 t vs 3 t.",
			"meta_title": "HiWEIGH FDL Low Profile Floor Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH FDL low-profile floor scale with dual ramps for warehouses, logistics and production. Available from Printechs Saudi Arabia.",
			"app1": "fdl",
			"app2": "fdl-2",
			"story_labels": ("FDL", "Ramps", "In KSA"),
			"story_alts": ("", "FDL with a warehouse trolley", "FDL in a Dammam warehouse"),
			"story_caps": (
				"Low deck plus two ramps — no foundation pit.",
				"1.5 t or 3 t; 1,200 or 1,500 mm.",
				"Quoted as a family page, not a spare-part Item.",
			),
			"icons": [
				{"icon": "device", "title": "Access", "description": "Dual 300 mm ramps", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "1.5 t or 3 t", "sort_order": 2},
				{"icon": "durability", "title": "Deck", "description": "1200 or 1500 mm", "sort_order": 3},
				{"icon": "rugged", "title": "Build", "description": "Carbon steel", "sort_order": 4},
			],
			"benefits": [
				{"icon": "speed", "title": "Roll-on access", "description": "Dual ramps for pallet jacks and cage trolleys.", "sort_order": 1},
				{"icon": "install", "title": "No pit", "description": "Low-profile deck sits on the finished floor.", "sort_order": 2},
				{"icon": "inventory", "title": "1.5 / 3 t", "description": "Not the 5 t FD U-beam family.", "sort_order": 3},
				{"icon": "store", "title": "Logistics floors", "description": "Warehouses, production aisles and receiving.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH FDL low-profile floor scale"),
					("Official page", "hiweigh.com/product-details/fdl-floor-scale/"),
					("Not this page", "FD 5 t U-beam, FWR hygienic stainless, AXR truck decks"),
				]),
				("Construction", [
					("Ramps", "Dual 300 mm ramps"),
					("Capacities", "1.5 t and 3 t"),
					("Decks", "1,200 mm or 1,500 mm"),
					("Material", "Carbon steel"),
				]),
			],
			"section_h": "Low profile when forklifts are not the only traffic",
			"section_b": "If operators live on pallet jacks, FDL is usually easier than a high U-beam FD. If you need 5 t or a larger deck, we look at FD instead.",
			"section_alt": "FDL scale in a production aisle",
			"pack": [
				{"item_description": "Quoted FDL deck, capacity and dual ramps", "sort_order": 1},
				{"item_description": "Indicator and installation as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "Does FDL need a pit?", "answer": "No. It is a low-profile deck with ramps on a finished floor.", "sort_order": 1},
				{"question": "5 tonne version?", "answer": "Official FDL is 1.5 / 3 t. For 5 t see FD.", "sort_order": 2},
				{"question": "Stainless food version?", "answer": "See FWR for hygienic stainless floors with a ramp.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-fwr",
			"display": "HiWEIGH FWR Stainless Steel Hygienic Floor Scale",
			"card": "fwr",
			"sub": "Floor Scales",
			"label": "HYGIENIC FLOOR SCALE",
			"featured": 1,
			"featured_sort": 8,
			"tagline": "Stainless hygienic floor with ramp access.",
			"short": (
				"Stainless hygienic floor weighing system with ramp access and IP-rated load cells "
				"for food processing and wet industrial environments."
			),
			"long": (
				"<p>The HiWEIGH FWR is a SUS304 hygienic floor scale with ramp access for wet food "
				"rooms. Official capacity reaches about 2,000 kg with IP67 or IP68 load cells.</p>"
				"<p>This is a family page. Stocked hygienic floors in Desk are the FW series — "
				"<strong>IND.SYS.HIW.4003</strong> FW1230M 1.2 × 1.2 m / 3 t and "
				"<strong>IND.SYS.HIW.4004</strong> FW1530M 1.5 × 1.5 m / 3 t (also FW1015M 4725). "
				"We quote FWR or FW to the deck you need and do not attach those Items to this page "
				"so the autoname stays the family slug.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH FWR stainless hygienic floor scale with ramp",
			"chips": "SUS304 hygienic\nRamp access\nTo ~2,000 kg FWR\nIP67 / IP68 cells",
			"story": "A floor scale you can wash",
			"visual": "FWR in food plants",
			"card_title": "FWR Hygienic Floor",
			"card_summary": "Stainless hygienic floor scale with ramp. Stocked FW 3 t decks can be quoted.",
			"cta_h": "Quote HiWEIGH FWR / FW",
			"cta_d": "Tell us deck size, 2 t vs 3 t, and whether the room is full washdown.",
			"meta_title": "HiWEIGH FWR Stainless Steel Hygienic Floor Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH FWR stainless hygienic floor scale with ramp for food processing and wet industry. Stocked FW decks available from Printechs Saudi Arabia.",
			"app1": "fwr",
			"app2": "fwr-2",
			"story_labels": ("FWR", "Washdown", "In KSA"),
			"story_alts": ("", "FWR being washed", "FWR in a Saudi food plant"),
			"story_caps": (
				"Stainless hygienic floor with ramp access.",
				"Food rooms — not a painted carbon-steel FD.",
				"Stocked FW 1.2 / 1.5 m 3 t decks can be quoted.",
			),
			"icons": [
				{"icon": "durability", "title": "Deck", "description": "SUS304 hygienic", "sort_order": 1},
				{"icon": "rugged", "title": "Cells", "description": "IP67 or IP68", "sort_order": 2},
				{"icon": "inventory", "title": "FWR capacity", "description": "To about 2,000 kg", "sort_order": 3},
				{"icon": "device", "title": "Stocked FW", "description": "1.2 / 1.5 m · 3 t", "sort_order": 4},
			],
			"benefits": [
				{"icon": "durability", "title": "Stainless floor", "description": "Hygienic deck and ramp for wet food and dairy rooms.", "sort_order": 1},
				{"icon": "rugged", "title": "IP-rated cells", "description": "IP67 or IP68 load cells — not a dry warehouse FD.", "sort_order": 2},
				{"icon": "install", "title": "Ramp access", "description": "Crates and trolleys roll on without a painted carbon deck.", "sort_order": 3},
				{"icon": "inventory", "title": "FW stock options", "description": "1.2 m and 1.5 m 3 t FW decks are available to quote.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH FWR hygienic floor scale (family page)"),
					("Official page", "hiweigh.com/product-details/fwr-hygienic-floor-scale/"),
					("Stocked configs", "FW1230M 4003 and FW1530M 4004 — quoted, not mixed onto this slug"),
					("Not this page", "FD carbon floor, FDL dual-ramp, K9T bench"),
				]),
				("Construction", [
					("Material", "SUS304 hygienic floor with ramp"),
					("FWR capacity", "Up to approximately 2,000 kg"),
					("Load cells", "IP67 or IP68"),
					("FW stock", "FW1230M / FW1530M 3,000 kg stainless washdown platforms"),
				]),
			],
			"section_h": "Hygienic floor, not a painted deck",
			"section_b": "Carbon-steel FD will rust in a washdown hall. FWR / FW is the stainless floor family. We match official FWR capacity and stocked FW 3 t decks on the quote.",
			"section_alt": "FWR hygienic floor scale in a dairy plant",
			"pack": [
				{"item_description": "Quoted FWR or FW hygienic floor, deck and cells", "sort_order": 1},
				{"item_description": "Ramp, indicator and install as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "FWR or FW?", "answer": "FWR is the official hygienic-floor family. FW1230M and FW1530M are stocked stainless washdown floors we can quote.", "sort_order": 1},
				{"question": "Why is there no Item on this page?", "answer": "So the URL stays the family slug. Attaching 4003 would rename the page to that Item code.", "sort_order": 2},
				{"question": "Is this a bench scale?", "answer": "No. For benches see K9T or BHB. FWR is a floor system with a ramp.", "sort_order": 3},
			],
		},
	]


def axle_livestock_pages():
	return [
		{
			"slug": "hiweigh-ax",
			"display": "HiWEIGH AX Portable Axle Weighing Platform",
			"card": "ax",
			"sub": "Truck & Axle Weighing",
			"label": "PORTABLE AXLE WEIGHING PLATFORM",
			"tagline": "OIML load-cell pads for fleet and truck axle checks.",
			"short": (
				"Portable axle weighing system using OIML-certified load cells. Suitable for fleet "
				"management, truck weighing and road enforcement applications."
			),
			"long": (
				"<p>The HiWEIGH AX is a portable axle-weighing platform in 7075/6061 aluminium with "
				"OIML load cells (IP67). Official pad capacities include 10, 15 and 20 t, with optional "
				"ramps or wireless. It is the classic portable pad — AXC adds built-in ramps, AXR is "
				"the foundation-free weighbridge, TiTAN is the mining pad.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH AX portable axle weighing platform",
			"chips": "7075 / 6061 aluminium\n10 / 15 / 20 t pads\nOIML cells · IP67\nFleet · enforcement",
			"story": "Weigh the axle without pouring a pit",
			"visual": "AX in the yard",
			"card_title": "AX Axle Pad",
			"card_summary": "Portable OIML axle weighing pads for fleet, truck and enforcement use.",
			"cta_h": "Quote HiWEIGH AX",
			"cta_d": "Confirm pad capacity, number of pads and whether you need ramps or wireless.",
			"meta_title": "HiWEIGH AX Portable Axle Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH AX portable axle weighing platform with OIML load cells for fleet, truck and enforcement weighing. Available from Printechs Saudi Arabia.",
			"app1": "ax",
			"app2": "ax-2",
			"story_labels": ("AX", "Fleet", "In KSA"),
			"story_alts": ("", "AX pad under a truck tire", "AX at a Saudi fleet yard"),
			"story_caps": (
				"Portable aluminium axle pads — not a weighbridge deck.",
				"10 / 15 / 20 t pad options with OIML cells.",
				"Specified by Printechs for Saudi fleet yards.",
			),
			"icons": [
				{"icon": "durability", "title": "Pad", "description": "7075 / 6061 Al", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "10 / 15 / 20 t", "sort_order": 2},
				{"icon": "shield", "title": "Cells", "description": "OIML · IP67", "sort_order": 3},
				{"icon": "connectivity", "title": "Options", "description": "Ramps · wireless", "sort_order": 4},
			],
			"benefits": [
				{"icon": "rugged", "title": "Portable pads", "description": "Move the weighing lane to the yard instead of pouring a pit.", "sort_order": 1},
				{"icon": "shield", "title": "OIML cells", "description": "Certified load cells with IP67 protection.", "sort_order": 2},
				{"icon": "inventory", "title": "10–20 t pads", "description": "Choose pad capacity; pair two or more for axle-by-axle checks.", "sort_order": 3},
				{"icon": "device", "title": "Not TiTAN", "description": "Mining 50–200 t pads are the TiTAN family.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH AX portable axle weighing platform"),
					("Official page", "hiweigh.com/product-details/ax-axle-weighing-platform/"),
					("Not this page", "AXC built-in ramps, AXR portable weighbridge, TiTAN mining pads"),
				]),
				("Construction", [
					("Material", "7075 / 6061 aluminium"),
					("Pad capacities", "10, 15 and 20 t"),
					("Load cells", "OIML certified, IP67"),
					("Options", "Ramps or wireless connectivity"),
				]),
			],
			"section_h": "Pads, not a weighbridge",
			"section_b": "AX is the portable pad family. If you need integrated ramps choose AXC. If you need a relocatable truck deck choose AXR. Mining trucks belong on TiTAN.",
			"section_alt": "AX pads used for fleet yard weighing",
			"pack": [
				{"item_description": "Quoted AX pads, capacity and indicator", "sort_order": 1},
				{"item_description": "Ramps, wireless and extra pads as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "How is AX different from AXC?", "answer": "AXC is a 7075 pad with built-in ramps. AX is the portable pad family with optional ramps.", "sort_order": 1},
				{"question": "Can it weigh a whole truck at once?", "answer": "AX is axle-by-axle. For a portable multi-axle deck see AXR.", "sort_order": 2},
				{"question": "Mining trucks?", "answer": "See TiTAN for 50 / 100 / 200 t pads.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-axc",
			"display": "HiWEIGH AXC Portable Vehicle Axle Scale",
			"card": "axc",
			"sub": "Truck & Axle Weighing",
			"label": "PORTABLE VEHICLE AXLE SCALE",
			"featured": 1,
			"featured_sort": 9,
			"tagline": "7075 aluminium pads with built-in ramps — to ~20 t each.",
			"short": (
				"Aircraft-grade 7075 aluminum axle weighing pad capable of supporting up to "
				"approximately 20 tonnes per pad, with integrated ramps for portable vehicle weighing."
			),
			"long": (
				"<p>The HiWEIGH AXC is a 7075 aluminium axle pad with built-in ramps so vehicles can "
				"roll on without a separate ramp kit. Official capacity is up to about 20 t per pad. "
				"It is the featured portable axle product for fleet and roadside checks — not the "
				"foundation-free AXR weighbridge and not the 200 t TiTAN mining pad.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH AXC portable aluminum axle scale with integrated ramps",
			"chips": "7075 aluminium\nBuilt-in ramps\nUp to ~20 t / pad\nPortable vehicle weighing",
			"story": "Roll onto the pad — ramps are already there",
			"visual": "AXC on the lane",
			"card_title": "AXC Axle Scale",
			"card_summary": "7075 aluminium axle pad with built-in ramps, up to about 20 t per pad.",
			"cta_h": "Quote HiWEIGH AXC",
			"cta_d": "Tell us how many pads, the heaviest axle and whether you need a two-pad lane.",
			"meta_title": "HiWEIGH AXC Portable Truck Axle Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH AXC portable 7075 aluminium truck axle scale with built-in ramps, up to about 20 tonnes per pad. Available from Printechs Saudi Arabia.",
			"app1": "axc",
			"app2": "axc-2",
			"story_labels": ("AXC", "Lane", "In KSA"),
			"story_alts": ("", "AXC pad with a truck tire", "AXC at a Saudi highway check"),
			"story_caps": (
				"7075 pad with integrated ramps.",
				"Pair pads for a temporary axle lane.",
				"Featured portable axle solution from Printechs.",
			),
			"icons": [
				{"icon": "durability", "title": "Alloy", "description": "7075 aluminium", "sort_order": 1},
				{"icon": "device", "title": "Ramps", "description": "Built-in", "sort_order": 2},
				{"icon": "inventory", "title": "Per pad", "description": "Up to about 20 t", "sort_order": 3},
				{"icon": "rugged", "title": "Use", "description": "Fleet · roadside", "sort_order": 4},
			],
			"benefits": [
				{"icon": "speed", "title": "Integrated ramps", "description": "Vehicles roll on without a separate ramp kit.", "sort_order": 1},
				{"icon": "durability", "title": "7075 aluminium", "description": "Aircraft-grade pad for portable truck weighing.", "sort_order": 2},
				{"icon": "inventory", "title": "~20 t per pad", "description": "Confirm the heaviest axle before we lock the quote.", "sort_order": 3},
				{"icon": "integration", "title": "Two-pad lanes", "description": "Use a pair for axle-by-axle checks at a temporary site.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH AXC portable vehicle axle scale"),
					("Official page", "hiweigh.com/product-details/axc-axle-scale/"),
					("Not this page", "AX optional-ramp pads, AXR weighbridge, TiTAN 50–200 t mining"),
				]),
				("Construction", [
					("Material", "Aircraft-grade 7075 aluminium"),
					("Ramps", "Integrated"),
					("Capacity", "Up to approximately 20 t per pad"),
					("Use", "Portable vehicle and truck axle weighing"),
				]),
			],
			"section_h": "The everyday portable axle pad",
			"section_b": "AXC is the featured portable axle product: 7075 aluminium and built-in ramps. Move to AXR when you need a truck-length deck, or TiTAN when the vehicle is a mine truck.",
			"section_alt": "AXC two-pad portable truck weighing lane",
			"pack": [
				{"item_description": "Quoted AXC pads with built-in ramps", "sort_order": 1},
				{"item_description": "Indicator, extra pads and cases as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "How many pads do I need?", "answer": "Often two for a lane. We confirm against the vehicle and whether you weigh axle-by-axle or total.", "sort_order": 1},
				{"question": "Is this a weighbridge?", "answer": "No. AXR is the foundation-free portable weighbridge.", "sort_order": 2},
				{"question": "20 tonnes per truck?", "answer": "Official capacity is up to about 20 t per pad — not per truck. Confirm axle loads.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-axr",
			"display": "HiWEIGH AXR Portable Weighbridge",
			"card": "axr",
			"sub": "Truck & Axle Weighing",
			"label": "PORTABLE WEIGHBRIDGE",
			"featured": 1,
			"featured_sort": 2,
			"tagline": "Foundation-free truck scale you can relocate.",
			"short": (
				"Foundation-free portable truck scale designed for temporary sites and operations "
				"where the weighing system may need to be relocated. Capacity around 30 tonnes "
				"depending on configuration."
			),
			"long": (
				"<p>The HiWEIGH AXR is a foundation-free portable weighbridge for construction sites, "
				"logistics yards and industrial facilities that do not want a permanent pit. Official "
				"capacity is about 30 t with decks 2100 / 3600 / 4200 × 760 mm and eight OIML H8C "
				"load cells.</p>"
				"<p>This is one of the three products that differentiate Printechs’ HiWEIGH offer: "
				"relocatable truck weighing without civil works. It is not an axle pad (AX / AXC) "
				"and not a 200 t mining pad (TiTAN).</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH AXR foundation-free portable truck weighbridge",
			"chips": "No foundation pit\n~30 t class\n2100 / 3600 / 4200 × 760 mm\n8 × OIML H8C",
			"story": "A weighbridge that can move with the project",
			"visual": "AXR on temporary sites",
			"card_title": "AXR Weighbridge",
			"card_summary": "Foundation-free portable truck scale, around 30 t, for sites that must relocate.",
			"cta_h": "Quote HiWEIGH AXR",
			"cta_d": "Tell us the longest vehicle, site surface and whether the decks must move later.",
			"meta_title": "HiWEIGH AXR Portable Weighbridge Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH AXR foundation-free portable weighbridge for construction, logistics and industrial sites. Around 30 tonnes depending on configuration. Available from Printechs Saudi Arabia.",
			"app1": "axr",
			"app2": "axr-2",
			"story_labels": ("AXR", "Relocate", "In KSA"),
			"story_alts": ("", "AXR with a tractor-trailer", "AXR on a Saudi construction site"),
			"story_caps": (
				"Portable truck decks — no permanent pit.",
				"Move the modules when the project moves.",
				"A HiWEIGH differentiator for Saudi temporary sites.",
			),
			"icons": [
				{"icon": "install", "title": "Civil works", "description": "No foundation pit", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "About 30 t class", "sort_order": 2},
				{"icon": "device", "title": "Decks", "description": "2100–4200 × 760 mm", "sort_order": 3},
				{"icon": "shield", "title": "Cells", "description": "8 × OIML H8C", "sort_order": 4},
			],
			"benefits": [
				{"icon": "install", "title": "No pit", "description": "Foundation-free decks for temporary and relocatable sites.", "sort_order": 1},
				{"icon": "speed", "title": "Project sites", "description": "Construction, logistics yards and industrial camps.", "sort_order": 2},
				{"icon": "inventory", "title": "~30 t class", "description": "Confirm vehicle GVW — this is not a 200 t mining pad.", "sort_order": 3},
				{"icon": "shield", "title": "OIML H8C", "description": "Eight official H8C cells on the published configuration.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH AXR portable weighbridge"),
					("Official page", "hiweigh.com/product-details/axr-portable-truck-scale/"),
					("Not this page", "AX / AXC axle pads, TiTAN mining pads, FD warehouse floor"),
				]),
				("Construction", [
					("Foundation", "None — portable, relocatable decks"),
					("Capacity", "Around 30 t depending on configuration"),
					("Decks", "2100 / 3600 / 4200 × 760 mm"),
					("Load cells", "8 × OIML H8C"),
				]),
			],
			"section_h": "When you do not want a permanent weighbridge",
			"section_b": "If the site is temporary — or the weighing point will move — AXR avoids civil works. Permanent pit weighbridges and mining pads are different families.",
			"section_alt": "AXR modules being positioned on a temporary site",
			"pack": [
				{"item_description": "Quoted AXR decks, cells and approaches", "sort_order": 1},
				{"item_description": "Indicator, installation and relocation plan as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "Do I need a concrete pit?", "answer": "No. AXR is specified as a foundation-free portable truck scale.", "sort_order": 1},
				{"question": "Is 30 tonnes per axle?", "answer": "Official capacity is around 30 t for the published configuration — we confirm against your vehicles.", "sort_order": 2},
				{"question": "Mining dump trucks?", "answer": "See TiTAN for 50 / 100 / 200 t pads.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-titan",
			"display": "HiWEIGH TiTAN Mining Truck Scale",
			"card": "titan",
			"sub": "Truck & Axle Weighing",
			"label": "HEAVY-DUTY MINING AXLE SCALE",
			"featured": 1,
			"featured_sort": 3,
			"tagline": "50 / 100 / 200 t pads for quarry and mine trucks.",
			"short": (
				"Heavy-capacity portable weighing pad developed for mining trucks, supporting up to "
				"approximately 200 tonnes per pad and compatible with wheel/total-weight indication systems."
			),
			"long": (
				"<p>The HiWEIGH TiTAN is the heavy mining axle pad: official capacities of 50, 100 and "
				"200 t per pad, IP68 protection, 120% F.S. overload limit, and 0–40 °C operation. "
				"Two, four or six pads can be combined for static or dynamic weighing with axle or "
				"total-weight indication.</p>"
				"<p>This is the third HiWEIGH differentiator for Printechs — genuine high-capacity "
				"weighing for mining, quarry, construction and heavy transport. It is not a 20 t AXC "
				"pad and not a 30 t AXR weighbridge.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH TiTAN heavy-duty mining axle weighing pad",
			"chips": "50 / 100 / 200 t per pad\nIP68\n2 / 4 / 6 pad systems\nStatic & dynamic",
			"story": "Weigh the truck the quarry actually uses",
			"visual": "TiTAN on the mine road",
			"card_title": "TiTAN Mining",
			"card_summary": "Heavy-capacity mining axle pad — 50, 100 or 200 t per pad, static or dynamic.",
			"cta_h": "Quote HiWEIGH TiTAN",
			"cta_d": "Tell us truck type, pad count and whether you need static, dynamic or both.",
			"meta_title": "HiWEIGH TiTAN Mining Truck Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH TiTAN mining truck axle scale supporting up to about 200 tonnes per pad for quarry, mine and heavy transport. Available from Printechs Saudi Arabia.",
			"app1": "titan",
			"app2": "titan-2",
			"story_labels": ("TiTAN", "Mine", "In KSA"),
			"story_alts": ("", "TiTAN under a dump-truck tire", "TiTAN at a Saudi quarry"),
			"story_caps": (
				"Ultra-heavy pads — not a 20 t fleet axle scale.",
				"Combine 2, 4 or 6 pads; axle or total weight.",
				"A HiWEIGH differentiator for Saudi mining and quarry sites.",
			),
			"icons": [
				{"icon": "inventory", "title": "Per pad", "description": "50 / 100 / 200 t", "sort_order": 1},
				{"icon": "rugged", "title": "Ingress", "description": "IP68", "sort_order": 2},
				{"icon": "device", "title": "System", "description": "2 / 4 / 6 pads", "sort_order": 3},
				{"icon": "display", "title": "Modes", "description": "Static & dynamic", "sort_order": 4},
			],
			"benefits": [
				{"icon": "inventory", "title": "Mining capacity", "description": "Official 50, 100 and 200 t pad options for ultra-heavy vehicles.", "sort_order": 1},
				{"icon": "rugged", "title": "IP68 pads", "description": "Built for dusty, wet quarry and mine roads.", "sort_order": 2},
				{"icon": "integration", "title": "Multi-pad systems", "description": "2, 4 or 6 pads with wheel or total-weight indication.", "sort_order": 3},
				{"icon": "speed", "title": "Static and dynamic", "description": "Official TiTAN positioning covers both weighing modes.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH TiTAN heavy-duty mining axle scale"),
					("Official page", "hiweigh.com/product-details/titan/"),
					("Not this page", "AX / AXC fleet pads, AXR 30 t portable weighbridge"),
				]),
				("Construction", [
					("Pad capacities", "50 t, 100 t and 200 t options"),
					("System", "2, 4 or 6 pads; axle or total weight"),
					("Ingress", "IP68"),
					("Overload / temperature", "120% F.S.; 0–40 °C operating; −25–55 °C storage"),
				]),
			],
			"section_h": "A genuinely industrial HiWEIGH product",
			"section_b": "Fleet axle pads stop around 20 t. TiTAN is for mining trucks and quarry vehicles. We specify pad count and static versus dynamic on the site survey.",
			"section_alt": "TiTAN mine weigh-station display",
			"pack": [
				{"item_description": "Quoted TiTAN pads, capacity and pad count", "sort_order": 1},
				{"item_description": "Indication system, ramps and commissioning as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "200 tonnes per truck or per pad?", "answer": "Official options are 50, 100 and 200 t per pad. We size the system to the vehicle.", "sort_order": 1},
				{"question": "Is this the same as AXR?", "answer": "No. AXR is a ~30 t foundation-free truck deck. TiTAN is the mining pad family.", "sort_order": 2},
				{"question": "Do you support quarry sites in Saudi Arabia?", "answer": "Yes. Printechs specifies and supports TiTAN for mining, quarry and heavy transport customers.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-ag",
			"display": "HiWEIGH AG Cattle Crate Scale",
			"card": "ag",
			"sub": "Livestock Weighing",
			"label": "CATTLE CRATE SCALE",
			"featured": 1,
			"featured_sort": 10,
			"tagline": "Heavy-duty cattle crate for safe farm weighing.",
			"short": (
				"Heavy-duty cattle weighing crate designed for safe livestock weighing in farms, "
				"ranches and agricultural facilities."
			),
			"long": (
				"<p>The HiWEIGH AG is a heavy-duty cattle crate scale. Official capacity is 3,000 kg "
				"with four M28/H8C IP67 load cells. Sheeted sides and weigh-bar mounts keep animals "
				"and operators safer during the weigh.</p>"
				"<p>Pair AG with <a href=\"/products/hiweigh-k7\">K7</a> (or K9 when the yard is "
				"washdown). Sheep, goats and hogs belong on AVS; pigs on an alleyway belong on APS.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH AG heavy-duty cattle crate scale",
			"chips": "3,000 kg cattle crate\n4 × M28/H8C IP67\nSheeted sides\nFarms · ranches",
			"story": "Weigh cattle without improvising a platform",
			"visual": "AG on the ranch",
			"card_title": "AG Cattle Scale",
			"card_summary": "Heavy-duty 3,000 kg cattle crate scale for farms and ranches.",
			"cta_h": "Quote HiWEIGH AG",
			"cta_d": "Tell us herd size, race layout and whether you need the K7 livestock indicator.",
			"meta_title": "HiWEIGH AG Cattle Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH AG cattle crate scale for safe livestock weighing on farms and ranches. Available from Printechs Saudi Arabia.",
			"app1": "ag",
			"app2": "ag-2",
			"story_labels": ("AG", "Alley", "In KSA"),
			"story_alts": ("", "AG crate in a farm yard", "AG on a Saudi ranch"),
			"story_caps": (
				"3 t cattle crate — not a sheep crate.",
				"Sheeted sides and weigh-bar mounts.",
				"Featured livestock system from Printechs.",
			),
			"icons": [
				{"icon": "inventory", "title": "Capacity", "description": "3,000 kg", "sort_order": 1},
				{"icon": "rugged", "title": "Cells", "description": "4 × M28/H8C IP67", "sort_order": 2},
				{"icon": "durability", "title": "Crate", "description": "Heavy-duty sheeted", "sort_order": 3},
				{"icon": "device", "title": "Indicator", "description": "Typically K7", "sort_order": 4},
			],
			"benefits": [
				{"icon": "rugged", "title": "Cattle-duty crate", "description": "Heavy-duty construction for farms and ranches.", "sort_order": 1},
				{"icon": "shield", "title": "Safer handling", "description": "Sheeted sides and mounts for weigh bars.", "sort_order": 2},
				{"icon": "inventory", "title": "3,000 kg", "description": "Official AG capacity with four IP67 cells.", "sort_order": 3},
				{"icon": "integration", "title": "K7 ready", "description": "Livestock indicator quoted with the crate.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH AG cattle crate scale"),
					("Official page", "hiweigh.com/product-details/ag-cattle-scale/"),
					("Not this page", "AVS sheep/goat/hog crate, APS pig alleyway, AP veterinary"),
				]),
				("Construction", [
					("Capacity", "3,000 kg"),
					("Load cells", "4 × M28 / H8C IP67"),
					("Use", "Cattle on farms, ranches and agricultural facilities"),
					("Indicator", "Typically K7 livestock; K9 if the yard is washdown"),
				]),
			],
			"section_h": "Cattle, not sheep",
			"section_b": "AG is the featured cattle crate. AVS is the smaller crate with single-position door control. APS is the aluminium pig alleyway.",
			"section_alt": "AG crate at the end of a cattle alley",
			"pack": [
				{"item_description": "Quoted AG cattle crate and load cells", "sort_order": 1},
				{"item_description": "K7 or K9 indicator and farm install as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "Will AG work for sheep?", "answer": "Use AVS for sheep, goats and hogs. AG is the cattle crate.", "sort_order": 1},
				{"question": "Does the page include the indicator?", "answer": "The crate is quoted with K7 (or K9). They are specified together, not mixed as one Item.", "sort_order": 2},
				{"question": "Do you install on Saudi farms?", "answer": "Yes. Printechs supplies and supports HiWEIGH livestock systems across the Kingdom.", "sort_order": 3},
			],
		},
	]


def small_livestock_and_cells():
	return [
		{
			"slug": "hiweigh-avs",
			"display": "HiWEIGH AVS Sheep, Goat & Hog Crate Scale",
			"card": "avs",
			"sub": "Livestock Weighing",
			"label": "SHEEP GOAT & HOG CRATE SCALE",
			"tagline": "Four sliding doors, one control position.",
			"short": (
				"Livestock crate weighing system for sheep, goats and pigs featuring a practical "
				"single-position door-control arrangement for easier animal handling."
			),
			"long": (
				"<p>The HiWEIGH AVS smart crate scale is built for sheep, goats and hogs. Four sliding "
				"doors are operated from a single position. Official capacities are 600 kg and 1,500 kg "
				"with four IP67 OIML/NTEP H8C alloy-steel load cells. Compatible with livestock "
				"indicators such as K7.</p>"
				"<p>AVS is not the 3 t AG cattle crate and not the aluminium APS pig alleyway.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH AVS sheep goat and hog crate scale",
			"chips": "600 kg or 1,500 kg\n4 sliding doors\n4 × IP67 H8C\nSheep · goats · hogs",
			"story": "Sort smaller livestock from one position",
			"visual": "AVS on the farm",
			"card_title": "AVS Crate",
			"card_summary": "Sheep, goat and hog crate scale with single-position door control.",
			"cta_h": "Quote HiWEIGH AVS",
			"cta_d": "Confirm 600 kg vs 1,500 kg and the livestock indicator.",
			"meta_title": "HiWEIGH AVS Sheep & Goat Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH AVS crate scale for sheep, goats and pigs with single-position door control. Available from Printechs Saudi Arabia.",
			"app1": "avs",
			"app2": "avs-2",
			"story_labels": ("AVS", "Sorting", "In KSA"),
			"story_alts": ("", "AVS crate for sheep and goats", "AVS on a Saudi sheep farm"),
			"story_caps": (
				"Smaller livestock crate — not AG cattle.",
				"Four doors from one operating position.",
				"600 kg or 1,500 kg quoted with K7.",
			),
			"icons": [
				{"icon": "inventory", "title": "Capacity", "description": "600 or 1,500 kg", "sort_order": 1},
				{"icon": "device", "title": "Doors", "description": "4 from one position", "sort_order": 2},
				{"icon": "rugged", "title": "Cells", "description": "4 × IP67 H8C", "sort_order": 3},
				{"icon": "integration", "title": "Indicator", "description": "K7 livestock", "sort_order": 4},
			],
			"benefits": [
				{"icon": "speed", "title": "Single-position doors", "description": "All four sliding doors operated from one place.", "sort_order": 1},
				{"icon": "inventory", "title": "Two capacities", "description": "600 kg or 1,500 kg for different livestock sizes.", "sort_order": 2},
				{"icon": "shield", "title": "Approved cells", "description": "OIML and NTEP H8C IP67 load cells.", "sort_order": 3},
				{"icon": "store", "title": "Sheep, goats, hogs", "description": "Not a 3 t cattle crate — that is AG.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH AVS hog, goat and sheep crate scale"),
					("Official page", "hiweigh.com/product-details/avs-crate-scale/"),
					("Not this page", "AG cattle crate, APS aluminium pig alleyway, AP veterinary"),
				]),
				("Construction", [
					("Capacities", "600 kg and 1,500 kg"),
					("Doors", "Four sliding doors, single-position control"),
					("Load cells", "Four IP67 alloy-steel OIML/NTEP H8C"),
					("Indicator", "Compatible with livestock indicators such as K7"),
				]),
			],
			"section_h": "The practical small-stock crate",
			"section_b": "AVS is specified where one operator must control all doors. Cattle still need AG. A washed pig alleyway may be happier on APS aluminium.",
			"section_alt": "AVS crate used for livestock sorting",
			"pack": [
				{"item_description": "Quoted AVS crate in 600 kg or 1,500 kg", "sort_order": 1},
				{"item_description": "K7 indicator and farm install as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "600 kg or 1,500 kg?", "answer": "Official AVS options are both. We match the animals and the race.", "sort_order": 1},
				{"question": "Will it hold cattle?", "answer": "No. Use AG for cattle.", "sort_order": 2},
				{"question": "Does it include the indicator?", "answer": "The crate is quoted with a livestock indicator such as K7.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-aps",
			"display": "HiWEIGH APS Aluminum Pig Scale",
			"card": "aps",
			"sub": "Livestock Weighing",
			"label": "ALUMINUM PIG SCALE",
			"tagline": "All-aluminium alleyway scale for wet pig buildings.",
			"short": (
				"Lightweight corrosion-resistant livestock scale with aluminum construction and "
				"waterproof weighing electronics for demanding farm environments."
			),
			"long": (
				"<p>The HiWEIGH APS is an all-aluminium pig alleyway scale for wet, corrosive farm "
				"buildings. Official positioning pairs it with waterproof electronics — typically the "
				"K9 indicator — rather than a painted steel cattle crate.</p>"
				"<p>APS is not AVS (steel crate, four doors) and not AG (3 t cattle). Choose APS when "
				"weight and corrosion in a pig building matter more than a sheeted cattle crate.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH APS aluminum waterproof pig scale",
			"chips": "All-aluminium\nPig alleyway\nWaterproof electronics\nPairs with K9",
			"story": "A livestock scale that likes a wet barn",
			"visual": "APS in pig buildings",
			"card_title": "APS Pig Scale",
			"card_summary": "Aluminium pig alleyway scale with waterproof electronics for wet farm buildings.",
			"cta_h": "Quote HiWEIGH APS",
			"cta_d": "Tell us alley width, animal size and whether you want K9 washdown electronics.",
			"meta_title": "HiWEIGH APS Waterproof Pig Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH APS aluminium waterproof pig scale for demanding farm environments. Available from Printechs Saudi Arabia.",
			"app1": "aps",
			"app2": "aps-2",
			"story_labels": ("APS", "Washable", "In KSA"),
			"story_alts": ("", "APS in a barn", "APS in a Saudi livestock barn"),
			"story_caps": (
				"Aluminium alleyway — lighter than a steel cattle crate.",
				"Happy in washed-down pig buildings.",
				"Typically paired with K9 waterproof electronics.",
			),
			"icons": [
				{"icon": "durability", "title": "Frame", "description": "All-aluminium", "sort_order": 1},
				{"icon": "rugged", "title": "Electronics", "description": "Waterproof · K9", "sort_order": 2},
				{"icon": "device", "title": "Form", "description": "Pig alleyway", "sort_order": 3},
				{"icon": "inventory", "title": "Use", "description": "Wet farm buildings", "sort_order": 4},
			],
			"benefits": [
				{"icon": "durability", "title": "Aluminium", "description": "Corrosion-resistant alleyway for wet pig buildings.", "sort_order": 1},
				{"icon": "rugged", "title": "Waterproof electronics", "description": "Officially paired with washdown-class indicators such as K9.", "sort_order": 2},
				{"icon": "speed", "title": "Lighter handling", "description": "Easier to site than a 3 t steel cattle crate.", "sort_order": 3},
				{"icon": "store", "title": "Pigs, not cattle", "description": "Cattle still belong on AG.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH APS aluminum pig scale"),
					("Official page", "hiweigh.com/product-details/aps-aluminum-pig-scale/"),
					("Not this page", "AG cattle crate, AVS sheep/goat/hog crate, AP veterinary"),
				]),
				("Construction", [
					("Frame", "All-aluminium alleyway"),
					("Electronics", "Waterproof; typically paired with K9"),
					("Use", "Pig weight monitoring in harsh farm environments"),
				]),
			],
			"section_h": "Aluminium for the wet building",
			"section_b": "Steel crates rust where pig buildings are washed every day. APS is the aluminium alleyway; quote K9 when the electronics must match that environment.",
			"section_alt": "APS aluminum livestock scale on a wet floor",
			"pack": [
				{"item_description": "Quoted APS aluminium alleyway scale", "sort_order": 1},
				{"item_description": "K9 or livestock indicator as surveyed", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is APS a crate with doors?", "answer": "It is an aluminium pig alleyway scale. AVS is the four-door crate for sheep, goats and hogs.", "sort_order": 1},
				{"question": "Which indicator?", "answer": "Official APS positioning uses waterproof electronics; we typically quote K9.", "sort_order": 2},
				{"question": "Cattle?", "answer": "Use AG.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-ap",
			"display": "HiWEIGH AP Veterinary & Pet Scale",
			"card": "ap",
			"sub": "Livestock Weighing",
			"label": "VETERINARY / PET SCALE",
			"tagline": "SUS304 platform with a removable anti-slip mat.",
			"short": (
				"SUS304 stainless-steel veterinary platform with removable anti-slip mat for safe "
				"and hygienic animal weighing."
			),
			"long": (
				"<p>The HiWEIGH AP veterinary / pet scale uses a SUS304 platform and a removable "
				"anti-slip rubber mat. Official models include AP5060 60 kg × 20 g, AP5150 / AP9150 "
				"150 kg × 50 g and AP9300 300 kg × 100 g. Selected sizes have a handle and two wheels.</p>"
				"<p>AP is a clinic and grooming scale — not a farm crate (AG / AVS / APS).</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH AP SUS304 veterinary and pet scale",
			"chips": "SUS304 + rubber mat\n60 / 150 / 300 kg\nHandle & wheels on selected\nClinics · grooming",
			"story": "Hygienic weighing for clinics and pets",
			"visual": "AP in the clinic",
			"card_title": "AP Vet / Pet",
			"card_summary": "SUS304 veterinary platform with removable mat. 60, 150 and 300 kg models.",
			"cta_h": "Quote HiWEIGH AP",
			"cta_d": "Pick 60, 150 or 300 kg and tell us if the scale must move between rooms.",
			"meta_title": "HiWEIGH AP Veterinary & Pet Scale Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH AP SUS304 veterinary and pet scale with removable anti-slip mat for clinics and grooming. Available from Printechs Saudi Arabia.",
			"app1": "ap",
			"app2": "ap-2",
			"story_labels": ("AP", "Clinic", "In KSA"),
			"story_alts": ("", "AP with a dog in clinic", "AP in a Riyadh clinic"),
			"story_caps": (
				"Clinic platform — not a farm crate.",
				"Removable mat for hygiene between animals.",
				"60 / 150 / 300 kg official models.",
			),
			"icons": [
				{"icon": "durability", "title": "Platform", "description": "SUS304 + mat", "sort_order": 1},
				{"icon": "inventory", "title": "Models", "description": "60 / 150 / 300 kg", "sort_order": 2},
				{"icon": "device", "title": "Move", "description": "Handle & wheels*", "sort_order": 3},
				{"icon": "store", "title": "Sites", "description": "Clinic · grooming", "sort_order": 4},
			],
			"benefits": [
				{"icon": "shield", "title": "Hygienic platform", "description": "SUS304 with a removable anti-slip mat.", "sort_order": 1},
				{"icon": "inventory", "title": "Four official models", "description": "60 kg, two 150 kg sizes and 300 kg.", "sort_order": 2},
				{"icon": "install", "title": "Portable options", "description": "Handle and two wheels on selected sizes.", "sort_order": 3},
				{"icon": "store", "title": "Clinics and shelters", "description": "Not a livestock crate for the farm race.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH AP veterinary / pet scale"),
					("Official page", "hiweigh.com/product-details/ap-veterinary-pet-scale/"),
					("Not this page", "AG / AVS / APS farm crates"),
				]),
				("Models", [
					("AP5060", "60 kg × 20 g"),
					("AP5150 / AP9150", "150 kg × 50 g"),
					("AP9300", "300 kg × 100 g"),
					("Platform", "SUS304; removable anti-slip rubber mat; 4 rubber feet"),
				]),
			],
			"section_h": "Clinic scale, farm crate is a different page",
			"section_b": "AP is specified for veterinary rooms, grooming and shelters. Farm races still need AG, AVS or APS.",
			"section_alt": "AP pet scale with anti-slip mat",
			"pack": [
				{"item_description": "Quoted AP model (60, 150 or 300 kg) and mat", "sort_order": 1},
				{"item_description": "Indicator and wheels as specified", "sort_order": 2},
			],
			"faqs": [
				{"question": "Which AP do I need?", "answer": "Official models are 60 kg × 20 g, 150 kg × 50 g and 300 kg × 100 g.", "sort_order": 1},
				{"question": "Can I use it for cattle?", "answer": "No. Use AG for cattle.", "sort_order": 2},
				{"question": "Is the mat included?", "answer": "Official AP includes a removable anti-slip rubber mat.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-m15f",
			"display": "HiWEIGH M15F Single Point Load Cell",
			"card": "m15f",
			"sub": "Load Cells",
			"label": "SINGLE POINT LOAD CELL",
			"tagline": "C3 aluminium single-point — 50 to 400 kg, IP65.",
			"short": (
				"C3 single-point industrial load cell with IP65 protection, suitable for platform "
				"scales, retail scales and legal-for-trade weighing systems."
			),
			"long": (
				"<p>The HiWEIGH M15F / M15FM is an OIML aluminium-alloy single-point load cell. "
				"Official capacity is 50–400 kg, C3 accuracy, 2.0 ± 0.2 mV/V and IP65. It is the "
				"industrial / retail platform cell — not the smaller M13 table-top family (5–50 kg).</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH M15F C3 single point industrial load cell",
			"chips": "C3 · IP65\n50–400 kg\n2.0 ± 0.2 mV/V\nOEM platforms · retail",
			"story": "The single-point cell for industrial platforms",
			"visual": "M15F in OEM builds",
			"card_title": "M15F Load Cell",
			"card_summary": "C3 IP65 single-point load cell, 50–400 kg, for platforms and retail OEM.",
			"cta_h": "Quote HiWEIGH M15F",
			"cta_d": "Confirm capacity, cable length and whether you need M15F or M15FM.",
			"meta_title": "HiWEIGH M15F Single Point Load Cell Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH M15F C3 single-point industrial load cell, IP65, 50–400 kg for platforms and legal-for-trade OEM. Available from Printechs Saudi Arabia.",
			"app1": "m15f",
			"app2": "m15f-2",
			"story_labels": ("M15F", "OEM", "In KSA"),
			"story_alts": ("", "M15F on a bench", "M15F in a Saudi workshop"),
			"story_caps": (
				"C3 single-point, 50–400 kg.",
				"Fitted under industrial and retail platforms.",
				"M13 is the smaller 5–50 kg table-top cell.",
			),
			"icons": [
				{"icon": "shield", "title": "Accuracy", "description": "C3", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "50–400 kg", "sort_order": 2},
				{"icon": "rugged", "title": "Ingress", "description": "IP65", "sort_order": 3},
				{"icon": "device", "title": "Output", "description": "2.0 ± 0.2 mV/V", "sort_order": 4},
			],
			"benefits": [
				{"icon": "shield", "title": "C3 legal-for-trade", "description": "Specified for approved platform and retail builds.", "sort_order": 1},
				{"icon": "inventory", "title": "50–400 kg", "description": "The industrial single-point range — not the 5–50 kg M13.", "sort_order": 2},
				{"icon": "rugged", "title": "IP65", "description": "Sealed for typical platform and OEM environments.", "sort_order": 3},
				{"icon": "integration", "title": "M15F / M15FM", "description": "Confirm the variant when we quote cable and mounting.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH M15F / M15FM single-point load cell"),
					("Official page", "hiweigh.com/product-details/m15f/"),
					("Not this page", "M13 / M13M 5–50 kg table-top single-point"),
				]),
				("Electrical", [
					("Capacity", "50–400 kg"),
					("Accuracy", "C3"),
					("Sensitivity", "2.0 ± 0.2 mV/V"),
					("Ingress", "IP65"),
					("Creep / zero", "Creep 0.02% FS (30 min); zero balance ±2%"),
				]),
			],
			"section_h": "Platform cell, not a table-top cell",
			"section_b": "M15F covers the 50–400 kg single-point band used under industrial and retail platforms. Compact 5–50 kg benches use M13.",
			"section_alt": "M15F load cell being fitted under a platform",
			"pack": [
				{"item_description": "Quoted M15F or M15FM cell and capacity", "sort_order": 1},
				{"item_description": "Cable, mounts and spare cells as specified", "sort_order": 2},
			],
			"faqs": [
				{"question": "M15F or M13?", "answer": "M15F is 50–400 kg. M13 is the 5–50 kg table-top family.", "sort_order": 1},
				{"question": "Is it OIML?", "answer": "Official M15F is positioned as an OIML aluminium single-point with C3 accuracy.", "sort_order": 2},
				{"question": "Do you supply complete platforms?", "answer": "Yes — see BSW, FOD and K9T. This page is the load cell.", "sort_order": 3},
			],
		},
		{
			"slug": "hiweigh-m13",
			"display": "HiWEIGH M13 OIML Single Point Load Cell",
			"card": "m13",
			"sub": "Load Cells",
			"label": "OIML SINGLE POINT LOAD CELL",
			"tagline": "OIML C3 single-point for table-top scales — 5 to 50 kg.",
			"short": (
				"OIML-approved single-point load cell for industrial weighing platforms and OEM "
				"weighing equipment."
			),
			"long": (
				"<p>The HiWEIGH M13 / M13M is the OIML C3 single-point for compact table-top scales. "
				"Official capacities are 5, 10, 20, 30, 35, 40 and 50 kg, IP65, 2.0 ± 0.2 mV/V. It is "
				"not the 50–400 kg M15F industrial platform cell.</p>"
				+ _p()
			),
			"hero_alt": "HiWEIGH M13 OIML single point load cell",
			"chips": "OIML C3 · IP65\n5–50 kg\nM13 / M13M\nTable-top OEM",
			"story": "The cell inside a compact legal-for-trade bench",
			"visual": "M13 in table-top OEM",
			"card_title": "M13 Load Cell",
			"card_summary": "OIML C3 single-point load cell, 5–50 kg, for table-top OEM scales.",
			"cta_h": "Quote HiWEIGH M13",
			"cta_d": "Confirm 5–50 kg capacity and M13 vs M13M.",
			"meta_title": "HiWEIGH M13 OIML Single Point Load Cell Saudi Arabia | Printechs",
			"meta_desc": "HiWEIGH M13 OIML single-point load cell for table-top and OEM weighing equipment. Available from Printechs Saudi Arabia.",
			"app1": "m13",
			"app2": "m13-2",
			"story_labels": ("M13", "Table-top", "In KSA"),
			"story_alts": ("", "M13 close-up", "M13 in a Saudi workshop"),
			"story_caps": (
				"OIML C3, 5–50 kg table-top family.",
				"M13 and M13M — confirm the variant.",
				"M15F is the 50–400 kg platform cell.",
			),
			"icons": [
				{"icon": "shield", "title": "Approval", "description": "OIML C3", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "5–50 kg", "sort_order": 2},
				{"icon": "rugged", "title": "Ingress", "description": "IP65", "sort_order": 3},
				{"icon": "device", "title": "Variants", "description": "M13 / M13M", "sort_order": 4},
			],
			"benefits": [
				{"icon": "shield", "title": "OIML C3", "description": "Approved single-point for compact legal-for-trade benches.", "sort_order": 1},
				{"icon": "inventory", "title": "5–50 kg", "description": "Table-top range — not the 400 kg M15F.", "sort_order": 2},
				{"icon": "integration", "title": "OEM benches", "description": "Specified into compact platforms and retail table-tops.", "sort_order": 3},
				{"icon": "device", "title": "M13 / M13M", "description": "Two official variants; we quote the matching part.", "sort_order": 4},
			],
			"specs": [
				("This page", [
					("Model", "HiWEIGH M13 / M13M OIML single-point load cell"),
					("Official page", "hiweigh.com/product-details/m13-load-cell/"),
					("Not this page", "M15F / M15FM 50–400 kg industrial single-point"),
				]),
				("Electrical", [
					("Capacity", "5 | 10 | 20 | 30 | 35 | 40 | 50 kg"),
					("Accuracy", "C3"),
					("Sensitivity", "2.0 ± 0.2 mV/V"),
					("Ingress", "IP65"),
				]),
			],
			"section_h": "Table-top cell, not a 400 kg cell",
			"section_b": "M13 is specified into compact benches. If the platform is an industrial 50–400 kg deck, use M15F.",
			"section_alt": "M13 load cell in a table-top scale chassis",
			"pack": [
				{"item_description": "Quoted M13 or M13M cell and capacity", "sort_order": 1},
				{"item_description": "Cable and spare cells as specified", "sort_order": 2},
			],
			"faqs": [
				{"question": "Which capacities?", "answer": "Official M13 / M13M capacities are 5, 10, 20, 30, 35, 40 and 50 kg.", "sort_order": 1},
				{"question": "Can I put M13 under a 300 kg platform?", "answer": "No. Use M15F for 50–400 kg single-point platforms.", "sort_order": 2},
				{"question": "Do you sell complete benches?", "answer": "Yes — FOD, BHB and K9T. This page is the load cell only.", "sort_order": 3},
			],
		},
	]


def fill_hiweigh():
	media = prepare_media()
	for cfg in pages() + more_pages() + axle_livestock_pages() + small_livestock_and_cells():
		_fill(media, cfg)
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
	print("Wired HiWEIGH related products and brand")
	return "ok"


def _update_brand(media):
	from printechs_digital.setup.hiweigh_common import ensure_erp_brand

	ensure_erp_brand()
	logo = media["logo"]
	name = frappe.db.get_value("Website Brand", {"slug": "hiweigh"}, "name")
	doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
	doc.brand = "Hiweigh"
	doc.display_name = "HiWEIGH"
	doc.slug = "hiweigh"
	doc.logo = logo
	doc.summary = (
		"HiWEIGH industrial weighing — waterproof benches, floor scales, portable truck "
		"weighing and livestock systems — supplied and installed by Printechs in Saudi Arabia."
	)
	doc.sort_order = 10
	doc.published = 1
	doc.meta_title = "HiWEIGH Industrial Weighing Saudi Arabia | Printechs Brands"
	doc.meta_description = (
		"HiWEIGH waterproof, floor, truck and livestock weighing from Printechs in Saudi Arabia — "
		"K9T, AXR, TiTAN and the curated industrial range."
	)
	doc.flags.ignore_permissions = True
	if name:
		doc.save()
	else:
		doc.insert()
	frappe.db.commit()
