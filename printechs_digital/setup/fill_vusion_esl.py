# Copyright (c) 2026, Printechs and contributors
"""Vusion / SES-imagotag ESL and connected-store cluster for Printechs.

Brand + ESL hub + V100/V300/Waterproof/Freezer/V700/E300 + EdgeSense +
VusionCloud + Captana + retail media. URLs are /products/{slug} and /brands/vusion.
"""

import frappe

from printechs_digital.setup.vusion_common import (
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
	"vusion-esl": ["vusion-v300", "vusion-v300-waterproof", "vusion-edgesense", "vusion-captana"],
	"vusion-v100": ["vusion-v300", "vusion-esl", "vusion-vusioncloud"],
	"vusion-v300": ["vusion-v300-waterproof", "vusion-v300-freezer", "vusion-v700", "vusion-esl"],
	"vusion-v300-waterproof": ["vusion-v300-freezer", "vusion-v300", "vusion-esl"],
	"vusion-v300-freezer": ["vusion-v300-waterproof", "vusion-v300", "vusion-esl"],
	"vusion-v700": ["vusion-retail-media", "vusion-v300", "vusion-esl"],
	"vusion-e300": ["vusion-edgesense", "vusion-v300", "vusion-vusioncloud"],
	"vusion-edgesense": ["vusion-e300", "vusion-captana", "vusion-vusioncloud", "vusion-esl"],
	"vusion-vusioncloud": ["vusion-esl", "vusion-edgesense", "vusion-e300"],
	"vusion-captana": ["vusion-edgesense", "vusion-esl", "vusion-vusioncloud"],
	"vusion-retail-media": ["vusion-v700", "vusion-esl", "vusion-vusioncloud"],
}


def _p() -> str:
	return f"<p>{KSA_BODY}</p>"


def _page(media, slug, card_key, product_name, h1, category_label, tagline, short, long, hero_alt, chips, story, visual, card_title, card_summary, cta_h, cta_d, meta_title, meta_desc, benefits, story_items, icons, specs, ideal_h, ideal_b, ideal_img, ideal_alt, pack, faqs):
	card = media[card_key]
	doc = get_or_create(slug, product_name, card)
	apply_identity(doc, slug=slug, display_name=h1, category_label=category_label)
	doc.tagline = tagline
	doc.short_description = short
	doc.long_description = long + _p()
	doc.hero_image = card
	doc.hero_image_alt = hero_alt
	doc.hero_trust_chips = chips
	doc.story_heading = story
	doc.visual_story_heading = visual
	doc.card_title = card_title
	doc.card_summary = card_summary
	doc.card_image = card
	doc.final_cta_heading = cta_h
	doc.final_cta_description = cta_d
	doc.meta_title = meta_title
	doc.meta_description = meta_desc
	doc.set("benefits", benefits)
	doc.set("visual_story_items", story_items)
	doc.set("icon_specifications", icons)
	set_specs(doc, specs)
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": ideal_h, "body": ideal_b, "image": media[ideal_img], "image_alt": ideal_alt, "sort_order": 1},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": pack, "sort_order": 1},
		{"item_description": "Survey, integration, installation and store-team briefing as quoted", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", faqs)
	return save_product(doc)


def fill_hub(media):
	slug = "vusion-esl"
	card = media["hub"]
	doc = get_or_create(slug, "Vusion Electronic Shelf Labels", card)
	apply_identity(doc, slug=slug, display_name="Vusion Electronic Shelf Labels & Connected Retail Solutions", category_label="VUSION / SES-IMAGOTAG ESL")
	doc.tagline = "Turn every shelf into a connected digital asset — not another paper ticket."
	doc.short_description = (
		"Printechs delivers Vusion / SES-imagotag Electronic Shelf Labels, smart-shelf infrastructure, "
		"computer vision, retail IoT and store-automation across Saudi Arabia."
	)
	doc.long_description = (
		"<p>Vusion electronic shelf labels replace paper shelf tickets with centrally managed digital "
		"displays tied to retail pricing, POS, ERP and inventory. Prices move from headquarters to "
		"every facing in a store — or an entire Saudi chain — without a night crew reprinting labels.</p>"
		"<p>The connected shelf is more than a price. It can carry promotions, inventory cues, "
		"picking workflows, shopper QR/NFC journeys and associate flash-to-light. Vusion’s current "
		"architecture joins labels with EdgeSense rails, VusionCloud, Captana computer vision and "
		"in-store retail media.</p>"
		"<p><strong>How to choose.</strong> "
		"<a href=\"/products/vusion-v100\">V100</a> — reliable entry pricing. "
		"<a href=\"/products/vusion-v300\">V300</a> — four-colour promotions (the usual KSA specification). "
		"<a href=\"/products/vusion-v300-waterproof\">Waterproof</a> and "
		"<a href=\"/products/vusion-v300-freezer\">Freezer</a> — fresh and −25 °C. "
		"<a href=\"/products/vusion-v700\">V700</a> / <a href=\"/products/vusion-retail-media\">retail media</a> — full-colour shelf advertising. "
		"<a href=\"/products/vusion-e300\">E300</a> and <a href=\"/products/vusion-edgesense\">EdgeSense</a> — Bluetooth connected-store. "
		"<a href=\"/products/vusion-captana\">Captana</a> — shelf cameras. "
		"<a href=\"/products/vusion-vusioncloud\">VusionCloud</a> — the estate layer Printechs integrates to ERP and POS.</p>"
		"<p>A third-party 2026 outlook estimates the Saudi ESL market at about US$58.3 million in 2026, "
		"with a projected path toward US$179.7 million by 2033 (Grand View Research). Treat those as "
		"estimates, not audited totals — they do show why chains are budgeting now.</p>"
		+ _p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "Supermarket aisle with Vusion electronic shelf labels"
	doc.hero_trust_chips = "ESL → smart shelves → computer vision\nERP / POS integration\nRiyadh · Jeddah · Dammam\nVusion / SES-imagotag"
	doc.story_heading = "Electronic Shelf Labels Saudi Arabia — a connected store, not a tag catalogue"
	doc.visual_story_heading = "Labels, rails, cameras and cloud"
	doc.card_title = "Vusion ESL"
	doc.card_summary = "Vusion / SES-imagotag electronic shelf labels and connected-store systems for Saudi retail."
	doc.card_image = card
	doc.final_cta_heading = "Request an ESL consultation"
	doc.final_cta_description = (
		"Tell Printechs the format — supermarket, pharmacy, cosmetics or electronics — and we will "
		"map V100, V300, EdgeSense and Captana to the store."
	)
	doc.meta_title = "Vusion Electronic Shelf Labels Saudi Arabia | SES-imagotag ESL | Printechs"
	doc.meta_description = (
		"Deploy Vusion and SES-imagotag Electronic Shelf Labels in Saudi Arabia with Printechs. "
		"Automate shelf pricing, promotions, picking and store operations across retail chains."
	)
	doc.set("benefits", [
		{"icon": "speed", "title": "Automated shelf prices", "description": "Push price and promotion changes to every facing instead of reprinting paper.", "sort_order": 1},
		{"icon": "integration", "title": "POS, ERP and inventory", "description": "Printechs connects item, price and promotion masters into VusionCloud.", "sort_order": 2},
		{"icon": "display", "title": "Promotions shoppers can see", "description": "Four-colour V300 and full-colour V700 carry offers at the decision point.", "sort_order": 3},
		{"icon": "scan", "title": "Pick-to-light and NFC/QR", "description": "Flash associates to the SKU; let shoppers open product or online journeys.", "sort_order": 4},
		{"icon": "cloud", "title": "Multi-store control", "description": "One cloud estate for device health, templates and chain-wide consistency.", "sort_order": 5},
		{"icon": "report", "title": "Shelf truth with Captana", "description": "Add computer vision when empty facings and planograms need a camera, not a walk.", "sort_order": 6},
	])
	doc.set("visual_story_items", [
		{"label": "Grocery aisles", "image": media["supermarket-aisle"], "image_alt": "ESL supermarket", "caption": "Every facing on the same price file as the till.", "sort_order": 1},
		{"label": "Pharmacy", "image": media["pharmacy-shelf"], "image_alt": "ESL pharmacy", "caption": "OTC accuracy without a paper farm.", "sort_order": 2},
		{"label": "Four-colour V300", "image": media["v300"], "image_alt": "V300 ESL", "caption": "The label we specify most often in KSA.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "display", "title": "V-Series", "description": "V100 · V300 · V700", "sort_order": 1},
		{"icon": "connectivity", "title": "E-Series / EdgeSense", "description": "Bluetooth connected shelf", "sort_order": 2},
		{"icon": "cloud", "title": "VusionCloud", "description": "Estate & integrations", "sort_order": 3},
		{"icon": "scan", "title": "Captana", "description": "Shelf computer vision", "sort_order": 4},
	])
	set_specs(doc, [
		("Portfolio", [
			("Brand", "Vusion (SES-imagotag)"),
			("V-Series", "V100 entry; V300 4-colour; Waterproof IP68; Freezer −25 °C; V700 8.2-inch full colour"),
			("E-Series", "E300 BLE connected ESL; E700 full-colour connected display"),
			("Platform", "VusionCloud, VusionOX (BLE), EdgeSense rails, Captana / ShelfEye"),
			("Infrastructure", "Native, integrated or standalone (V:Gate) access-point models"),
		]),
		("Store outcomes", [
			("Pricing", "Central updates synchronised with POS"),
			("Operations", "Pick-to-light, flash-to-light, associate shelf data"),
			("Shopper", "QR / NFC journeys where configured"),
			("Security", "Encrypted low-power radio; AES-128 cited on Vusion ESL communications"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Connected store — not tag price",
			"body": (
				"ERP / Modern POS → Printechs integration → VusionCloud → V300 / E300 / EdgeSense → "
				"shelf → Captana → associate task. Competitors can quote a cheaper label. We specify "
				"the stack that keeps prices, stock and promotions on the same page."
			),
			"image": media["hq-dashboard"],
			"image_alt": "ESL estate dashboard",
			"link_label": "VusionCloud",
			"link_href": "/products/vusion-vusioncloud",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": "Quoted Vusion ESL mix, rails/fixtures and connectivity", "sort_order": 1},
		{"item_description": "VusionCloud activation and ERP/POS integration scope", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Is this SES-imagotag or Vusion?", "answer": "Same manufacturer. SES-imagotag is the historic brand name; Vusion is the current group and product name. Buyers still search both — we use both in Saudi conversations.", "sort_order": 1},
		{"question": "Which label should a supermarket start with?", "answer": "Most grocery projects lead with V300, then add Waterproof and Freezer by department. EdgeSense and Captana come in when location and shelf cameras are in scope.", "sort_order": 2},
		{"question": "Can you integrate our POS or ERP?", "answer": "Yes. Printechs maps item, price, promotion and store masters into VusionCloud — including Modern POS / ERPNext programmes we already run.", "sort_order": 3},
	])
	return save_product(doc)


def fill_series(media):
	_page(
		media, "vusion-v100", "v100",
		"Vusion V100 Electronic Shelf Labels",
		"Vusion V100 Electronic Shelf Labels",
		"ENTRY ESL",
		"Reliable digital pricing without extra colour complexity.",
		"V100 is Vusion’s accessible ESL for automated prices and promotions when four-colour marketing is not the main requirement.",
		"<p>V100 is the practical first step off paper. It focuses on price accuracy, promotion updates "
		"and day-to-day digital shelf management — the work most convenience, pharmacy and small-format "
		"Saudi stores need on day one.</p>"
		"<p>Vusion lists black, white and red display configurations in approximately "
		"<strong>1.5, 1.6, 2.1, 2.2 and 2.6 inch</strong> sizes. When promotional colour becomes the "
		"priority, step up to <a href=\"/products/vusion-v300\">V300</a>.</p>",
		"Vusion V100 electronic shelf labels",
		"Entry digital pricing\nB/W/R displays\n1.5\"–2.6\"\nChain-ready via VusionCloud",
		"Digital prices without a science project",
		"The accessible Vusion label",
		"V100",
		"Entry Vusion ESL for accurate digital pricing and promotion automation.",
		"Quote V100 for compact Saudi stores",
		"Printechs will confirm V100 versus V300 from your promotion mix and cost-per-facing target.",
		"Vusion V100 Electronic Shelf Labels Saudi Arabia | SES-imagotag | Printechs",
		"Vusion V100 electronic shelf labels provide reliable digital pricing and promotion automation for retail stores. Available from Printechs across Saudi Arabia.",
		[
			{"icon": "speed", "title": "Price automation first", "description": "Central updates for everyday prices and simple promotions.", "sort_order": 1},
			{"icon": "store", "title": "Built for volume roll-outs", "description": "A rugged entry label when cost per facing decides the business case.", "sort_order": 2},
			{"icon": "display", "title": "Black, white and red", "description": "Enough colour for sale flashes without a four-colour specification.", "sort_order": 3},
			{"icon": "cloud", "title": "Same cloud estate", "description": "Managed in VusionCloud beside V300 and connected-store devices.", "sort_order": 4},
		],
		[
			{"label": "V100", "image": media["v100"], "image_alt": "V100 ESL", "caption": "Compact entry labels for everyday pricing.", "sort_order": 1},
			{"label": "Convenience", "image": media["convenience"], "image_alt": "Convenience ESL", "caption": "Neighbourhood stores that reprint too often.", "sort_order": 2},
			{"label": "Small format", "image": media["small-electronics"], "image_alt": "Small electronics ESL", "caption": "Specialty shops that still need POS sync.", "sort_order": 3},
		],
		[
			{"icon": "display", "title": "Colours", "description": "Black · white · red", "sort_order": 1},
			{"icon": "device", "title": "Sizes", "description": "1.5\" · 1.6\" · 2.1\" · 2.2\" · 2.6\"", "sort_order": 2},
			{"icon": "store", "title": "Role", "description": "Entry digital pricing", "sort_order": 3},
			{"icon": "cloud", "title": "Platform", "description": "VusionCloud", "sort_order": 4},
		],
		[
			("Series", [
				("Series", "Vusion V100"),
				("Role", "Accessible ESL for price and promotion automation"),
				("Display colours", "Black, white, red"),
				("Published sizes", "Approx. 1.5\", 1.6\", 2.1\", 2.2\", 2.6\""),
			]),
			("Operations", [
				("Management", "VusionCloud multi-store"),
				("Typical step-up", "V300 when four-colour promotions are required"),
			]),
		],
		"Ideal for compact KSA retail",
		"Convenience stores, pharmacies, small-format grocery and any chain that wants digital prices first and marketing colour later.",
		"convenience", "Convenience store ESL",
		"Quoted Vusion V100 labels and fixtures",
		[
			{"question": "Is V100 enough for a supermarket?", "answer": "It can be, if promotions are simple. Most Saudi grocery projects still prefer V300 so yellow/red offers read from the aisle.", "sort_order": 1},
			{"question": "Can V100 share the same cloud as V300?", "answer": "Yes. Mixed estates are normal; we template both in VusionCloud.", "sort_order": 2},
			{"question": "Do you install V100 in KSA?", "answer": "Yes — survey, fixings, cloud activation and POS/ERP mapping.", "sort_order": 3},
		],
	)

	_page(
		media, "vusion-v300", "v300",
		"Vusion V300 4-Color Electronic Shelf Labels",
		"Vusion V300 4-Color Electronic Shelf Labels",
		"4-COLOUR ESL",
		"Black, white, red and yellow — prices and promotions on one facing.",
		"V300 is the four-colour ESL we specify most often in Saudi grocery, pharmacy, electronics and beauty.",
		"<p>V300 is the workhorse digital shelf for retailers that need promotional colour, not only a "
		"price. Selected labels show <strong>black, white, red and yellow</strong> so regular price, "
		"offer and product information stay distinct on the same ticket.</p>"
		"<p>Published sizes run from about <strong>1.5\" to 9.7\"</strong> "
		"(1.5, 1.6 chemical-resistant, 2.1, 2.2, 2.6, 2.9, 3.5, 4.2, 4.5, 5.9, 6.0, 7.4 and 9.7). "
		"LED flash, QR and NFC can support associate and shopper workflows where configured.</p>"
		"<p>Fresh and frozen need their own pages: "
		"<a href=\"/products/vusion-v300-waterproof\">V300 Waterproof</a> and "
		"<a href=\"/products/vusion-v300-freezer\">V300 Freezer</a>.</p>",
		"Vusion V300 four-color electronic shelf label",
		"BWRY four-colour\n1.5\"–9.7\"\nPOS / ERP sync\nSaudi grocery & pharmacy favourite",
		"The ESL we actively market in Saudi Arabia",
		"Four colours. One price file.",
		"V300",
		"Vusion V300 4-colour ESL for pricing, promotions and smart shelf workflows.",
		"Specify V300 for your next store",
		"Share department mix and promotion calendar — Printechs will size V300, Waterproof and Freezer together.",
		"Vusion V300 Electronic Shelf Labels Saudi Arabia | 4-Color ESL | Printechs",
		"Vusion V300 4-color Electronic Shelf Labels deliver accurate pricing, promotions and smart retail workflows. From Printechs Saudi Arabia.",
		[
			{"icon": "display", "title": "Four-colour e-paper", "description": "Black, white, red and yellow for price versus promotion.", "sort_order": 1},
			{"icon": "device", "title": "Grocery to gondola sizes", "description": "From compact 1.5\" tickets to 9.7\" promotional faces.", "sort_order": 2},
			{"icon": "speed", "title": "Chain-wide consistency", "description": "The same offer lands on every store the same morning.", "sort_order": 3},
			{"icon": "scan", "title": "LED, QR and NFC", "description": "Flash associates; open shopper journeys where you enable them.", "sort_order": 4},
		],
		[
			{"label": "V300", "image": media["v300"], "image_alt": "V300", "caption": "Four-colour promotional ESL.", "sort_order": 1},
			{"label": "Grocery", "image": media["grocery-promo"], "image_alt": "Grocery V300", "caption": "Yellow and red that read from the aisle.", "sort_order": 2},
			{"label": "Beauty", "image": media["cosmetics-shelf"], "image_alt": "Beauty V300", "caption": "Brand colour without a paper flash.", "sort_order": 3},
		],
		[
			{"icon": "display", "title": "Colours", "description": "Black · white · red · yellow", "sort_order": 1},
			{"icon": "device", "title": "Sizes", "description": "1.5\" to 9.7\"", "sort_order": 2},
			{"icon": "integration", "title": "Systems", "description": "POS · ERP · promotions", "sort_order": 3},
			{"icon": "cloud", "title": "Platform", "description": "VusionCloud", "sort_order": 4},
		],
		[
			("Series", [
				("Series", "Vusion V300 BWRY"),
				("Display colours", "Black, white, red, yellow"),
				("Published sizes", "1.5\", 1.6\" (chemical resistant), 2.1\", 2.2\", 2.6\", 2.9\", 3.5\", 4.2\", 4.5\", 5.9\", 6.0\", 7.4\", 9.7\""),
				("Related", "Waterproof IP68 and Freezer −25 °C are separate series"),
			]),
			("Workflows", [
				("Pricing", "Automatic updates synchronised with POS/ERP"),
				("Associates", "LED-supported pick / flash workflows where configured"),
				("Shopper", "QR / NFC interaction where configured"),
			]),
		],
		"Saudi sectors we specify V300 for",
		"Hypermarkets and supermarkets, pharmacies, electronics, cosmetics/beauty and fashion accessories — anywhere promotional colour and POS sync pay back faster than paper.",
		"cosmetics-shelf", "Beauty gondola V300",
		"Quoted Vusion V300 labels by size and finish",
		[
			{"question": "Why not put Waterproof on this page?", "answer": "Different environment, different search, different fixture. Fresh and freezer are their own specifications.", "sort_order": 1},
			{"question": "Do all sizes include yellow?", "answer": "Vusion states four-colour on specific V300 sizes. We confirm the exact size/colour matrix on quotation.", "sort_order": 2},
			{"question": "Can Printechs roll V300 across a KSA chain?", "answer": "Yes. Survey, templates, POS/ERP integration, install and Care options.", "sort_order": 3},
		],
	)

	_page(
		media, "vusion-v300-waterproof", "waterproof",
		"Vusion V300 Waterproof ESL",
		"Vusion V300 Waterproof Electronic Shelf Labels",
		"IP68 ESL",
		"IP68 digital prices for ice, mist, wash-down and humidity.",
		"V300 Waterproof is the IP68 ESL for seafood, meat, produce and any department that soaks a normal label.",
		"<p>Paper tickets curl. Standard electronics fail. V300 Waterproof is specified for water, "
		"humidity, condensation, ice and frequent cleaning — the fresh-food reality in Saudi "
		"hypermarkets.</p>"
		"<p>Vusion rates the range <strong>IP68</strong>. Published formats are about "
		"<strong>2.6\" and 4.2\"</strong>, with four-colour display capability and multi-colour LED "
		"for associate flash. Pair it with <a href=\"/products/vusion-v300-freezer\">V300 Freezer</a> "
		"for the cold chain behind the glass.</p>",
		"Vusion V300 Waterproof IP68 electronic shelf label",
		"IP68 protection\n2.6\" and 4.2\"\nFour-colour + LED\nFresh & wash-down",
		"Digital prices that survive the hose",
		"Fresh food is a different label",
		"V300 Waterproof",
		"IP68 Vusion V300 ESL for fresh, seafood, produce and wash-down departments.",
		"Protect fresh departments with Waterproof V300",
		"We will count wet facings and specify 2.6\" versus 4.2\" with the right fixture.",
		"Vusion V300 Waterproof Electronic Shelf Labels Saudi Arabia | IP68 ESL",
		"Vusion V300 Waterproof IP68 electronic shelf labels for fresh food, seafood, produce and wash-down retail. From Printechs Saudi Arabia.",
		[
			{"icon": "shield", "title": "IP68 protection", "description": "Specified for water, ice, humidity and hygiene wash-down.", "sort_order": 1},
			{"icon": "inventory", "title": "Fresh departments", "description": "Seafood, meat, produce, dairy and chilled displays.", "sort_order": 2},
			{"icon": "display", "title": "Four-colour + LED", "description": "Promotions stay readable; associates still get a flash.", "sort_order": 3},
			{"icon": "device", "title": "2.6\" and 4.2\"", "description": "The published Waterproof formats for grocery counters.", "sort_order": 4},
		],
		[
			{"label": "Waterproof V300", "image": media["waterproof"], "image_alt": "Waterproof ESL", "caption": "A label designed to get wet.", "sort_order": 1},
			{"label": "Seafood", "image": media["seafood-ice"], "image_alt": "Seafood ESL", "caption": "Ice, spray and stainless edges.", "sort_order": 2},
			{"label": "Produce", "image": media["produce-mist"], "image_alt": "Produce ESL", "caption": "Misting without a paper replacement ritual.", "sort_order": 3},
		],
		[
			{"icon": "shield", "title": "Rating", "description": "IP68", "sort_order": 1},
			{"icon": "device", "title": "Sizes", "description": "2.6\" · 4.2\"", "sort_order": 2},
			{"icon": "display", "title": "Colours", "description": "BWRY · 7-colour LED", "sort_order": 3},
			{"icon": "inventory", "title": "Zones", "description": "Fresh · wet · hygiene", "sort_order": 4},
		],
		[
			("Series", [
				("Series", "Vusion V300 Waterproof"),
				("Protection", "IP68"),
				("Published sizes", "Approximately 2.6\" and 4.2\""),
				("Display", "Four-colour capability; multi-colour LED"),
			]),
			("Environment", [
				("Use", "Water, humidity, ice, condensation, wash-down"),
				("Departments", "Seafood, meat, produce, dairy, chilled"),
			]),
		],
		"Search terms this page is built for",
		"Waterproof electronic shelf label, IP68 electronic price tag, ESL for fresh food, supermarket wet-counter pricing — specified and installed by Printechs in KSA.",
		"seafood-ice", "Seafood waterproof ESL",
		"Quoted V300 Waterproof labels and wet-area fixtures",
		[
			{"question": "Is every V300 waterproof?", "answer": "No. Only the Waterproof series is specified IP68. Do not mount a standard V300 on a hose-down counter.", "sort_order": 1},
			{"question": "What sizes are available?", "answer": "Vusion currently publishes 2.6\" and 4.2\" Waterproof formats.", "sort_order": 2},
			{"question": "Do you install in Saudi fresh counters?", "answer": "Yes. We survey ice beds, misting and hygiene rules before we quote fixtures.", "sort_order": 3},
		],
	)

	_page(
		media, "vusion-v300-freezer", "freezer",
		"Vusion V300 Freezer ESL",
		"Vusion V300 Freezer Electronic Shelf Labels",
		"FREEZER ESL",
		"Digital prices that stay readable down to −25 °C.",
		"V300 Freezer is the cold-chain ESL for frozen aisles, ice cream wells and cold rooms.",
		"<p>A freezer door that ices over will kill a standard label and a paper ticket. V300 Freezer "
		"is specified for frozen and cold retail, with operation as low as <strong>−25 °C</strong>.</p>"
		"<p>Published sizes include about <strong>2.1, 2.2, 2.6, 2.9 and 3.5 inch</strong>. "
		"Multi-colour LED flash helps gloved associates find the SKU in fog. Display colours on this "
		"series are published as black and white.</p>",
		"Vusion V300 Freezer electronic shelf label",
		"Down to −25 °C\n2.1\"–3.5\"\n7-colour LED flash\nFrozen & cold rooms",
		"Frozen is not a V300 with a thicker case",
		"Prices that survive the freezer door",
		"V300 Freezer",
		"Vusion V300 Freezer ESL for digital pricing down to −25 °C.",
		"Specify Freezer V300 for cold aisles",
		"We will count freezer doors and wells separately from ambient V300.",
		"Vusion Freezer Electronic Shelf Labels Saudi Arabia | V300 Freezer ESL",
		"Vusion V300 Freezer electronic shelf labels operate in cold environments down to -25°C. Digital pricing for frozen-food retailers from Printechs Saudi Arabia.",
		[
			{"icon": "shield", "title": "−25 °C operation", "description": "Specified for frozen aisles and cold rooms, not just a chilled cabinet.", "sort_order": 1},
			{"icon": "display", "title": "LED flash in the fog", "description": "Seven-colour LED helps picking and replenishment in gloves.", "sort_order": 2},
			{"icon": "inventory", "title": "Frozen grocery", "description": "Ice cream, meat, seafood freezers and specialty frozen stores.", "sort_order": 3},
			{"icon": "device", "title": "2.1\" to 3.5\"", "description": "Published freezer formats for door and well fixtures.", "sort_order": 4},
		],
		[
			{"label": "Freezer V300", "image": media["freezer"], "image_alt": "Freezer ESL", "caption": "A label specified for frost.", "sort_order": 1},
			{"label": "Frozen aisle", "image": media["frozen-aisle"], "image_alt": "Frozen aisle ESL", "caption": "Prices inside the cold case.", "sort_order": 2},
			{"label": "Ice cream", "image": media["ice-cream"], "image_alt": "Ice cream ESL", "caption": "Open wells still need a readable ticket.", "sort_order": 3},
		],
		[
			{"icon": "shield", "title": "Temperature", "description": "Down to −25 °C", "sort_order": 1},
			{"icon": "device", "title": "Sizes", "description": "2.1\" · 2.2\" · 2.6\" · 2.9\" · 3.5\"", "sort_order": 2},
			{"icon": "display", "title": "LED", "description": "7-colour flash", "sort_order": 3},
			{"icon": "display", "title": "Pixels", "description": "Black / white published", "sort_order": 4},
		],
		[
			("Series", [
				("Series", "Vusion V300 Freezer"),
				("Operating temperature", "As low as −25 °C"),
				("Published sizes", "Approximately 2.1\", 2.2\", 2.6\", 2.9\", 3.5\""),
				("Display colours", "Black and white (published)"),
				("LED", "7-colour blinking for associate tasks"),
			]),
		],
		"Ideal cold-chain sites",
		"Frozen supermarket aisles, hypermarket wells, meat and seafood freezers, cold rooms, dairy cold stores and specialty frozen retailers.",
		"frozen-aisle", "Frozen aisle ESL",
		"Quoted V300 Freezer labels and cold-case fixtures",
		[
			{"question": "Can a standard V300 go in the freezer?", "answer": "Do not assume that. Vusion publishes a dedicated Freezer series for −25 °C. We specify it separately.", "sort_order": 1},
			{"question": "Does it have four-colour yellow?", "answer": "Vusion currently lists black and white on Freezer, plus 7-colour LED. Confirm the matrix on quotation.", "sort_order": 2},
			{"question": "Do you install freezer ESL in KSA?", "answer": "Yes. We survey door types, wells and condensation before choosing fixtures.", "sort_order": 3},
		],
	)

	_page(
		media, "vusion-v700", "v700",
		"Vusion V700 Full Color ESL",
		"Vusion V700 Full-Color Electronic Shelf Display",
		"FULL-COLOUR ESL",
		"An 8.2-inch full-colour shelf display for campaigns, not only a price.",
		"V700 is the marketing-oriented digital shelf: branding, product imagery and high-impact promotions at the buying decision.",
		"<p>V700 is not a small price ticket. The <strong>8.2-inch full-colour</strong> display is "
		"built for product photography, brand graphics and promotional stories beside the merchandise.</p>"
		"<p>Use it on cosmetics end caps, electronics accessories, pharmacy feature bays and FMCG "
		"retail-media programmes. Seven-colour LED remains available for associate flash. Campaign "
		"operations sit with <a href=\"/products/vusion-retail-media\">in-store retail media</a>.</p>",
		"Vusion V700 full-color electronic shelf display",
		"8.2\" full colour\n7-colour LED\nShelf-edge retail media\nBeauty · electronics · pharmacy",
		"Digital shelf advertising that still knows the price",
		"Imagery at the shelf edge",
		"V700",
		"8.2-inch full-colour Vusion shelf display for promotions and retail media.",
		"Add V700 to feature bays",
		"Printechs will map which facings should stay V300 and which deserve a V700 campaign screen.",
		"Vusion V700 Full Color Electronic Shelf Display Saudi Arabia | Printechs",
		"Create high-impact shelf promotions with the Vusion V700 full-color electronic shelf display. Digital retail media from Printechs Saudi Arabia.",
		[
			{"icon": "display", "title": "Full-colour 8.2\"", "description": "Room for product imagery, not only a numeral.", "sort_order": 1},
			{"icon": "loyalty", "title": "Brand at the decision", "description": "Feature bays that used to hold a paper poster.", "sort_order": 2},
			{"icon": "report", "title": "Retail-media ready", "description": "A physical slot brands can buy for a launch week.", "sort_order": 3},
			{"icon": "cloud", "title": "Centrally scheduled", "description": "Change creative with the same cloud that changes prices.", "sort_order": 4},
		],
		[
			{"label": "V700", "image": media["v700"], "image_alt": "V700", "caption": "Full-colour shelf display.", "sort_order": 1},
			{"label": "Beauty", "image": media["beauty-endcap"], "image_alt": "Beauty V700", "caption": "End-cap campaigns in cosmetics.", "sort_order": 2},
			{"label": "Electronics", "image": media["electronics-promo"], "image_alt": "Electronics V700", "caption": "Accessories that need a picture.", "sort_order": 3},
		],
		[
			{"icon": "display", "title": "Size", "description": "8.2\" full colour", "sort_order": 1},
			{"icon": "device", "title": "LED", "description": "7 colours", "sort_order": 2},
			{"icon": "loyalty", "title": "Use", "description": "Retail media / feature", "sort_order": 3},
			{"icon": "cloud", "title": "Control", "description": "VusionCloud", "sort_order": 4},
		],
		[
			("Series", [
				("Series", "Vusion V700 full colour"),
				("Display", "Full-colour electronic shelf display"),
				("Published size", "8.2 inches"),
				("LED", "7 colours"),
			]),
			("Use", [
				("Role", "High-impact product and promotional communication at the shelf"),
				("Pair with", "V300 for standard facings; retail-media page for campaign ops"),
			]),
		],
		"Where V700 earns its facing",
		"Cosmetics, electronics, pharmacies, premium supermarket features, brand-sponsored bays and FMCG launch weeks.",
		"beauty-endcap", "V700 beauty end cap",
		"Quoted V700 displays and feature-bay fixtures",
		[
			{"question": "Is V700 an ESL or a screen?", "answer": "It is Vusion’s full-colour electronic shelf display — priced and scheduled like ESL, used like shelf media.", "sort_order": 1},
			{"question": "Do we replace every V300 with V700?", "answer": "No. V700 is for feature and campaign facings. Ambient grocery stays on V300.", "sort_order": 2},
			{"question": "Can brands pay for the slot?", "answer": "That is the retail-media model. See the dedicated retail-media page.", "sort_order": 3},
		],
	)

	_page(
		media, "vusion-e300", "e300",
		"Vusion E300 Electronic Shelf Labels",
		"Vusion E300 Bluetooth Electronic Shelf Labels",
		"CONNECTED ESL",
		"A BLE shelf endpoint — not only an electronic price ticket.",
		"E300 is Vusion’s connected-store ESL generation: pricing plus product location, guided picking and Bluetooth workflows.",
		"<p>Sell E300 as an intelligent digital shelf endpoint, not a cheaper price tag. Bluetooth Low "
		"Energy places it in a spatially aware store: geolocation, guided picking, shopper navigation "
		"and device-to-device interactions with EdgeSense and applications.</p>"
		"<p>Vusion also lists E300 Waterproof (IP68 fresh) and E300 Freezer (−25 °C) as variants of "
		"this generation, plus larger-format <strong>E700</strong> full-colour connected displays. "
		"The rail and location layer is <a href=\"/products/vusion-edgesense\">EdgeSense</a>.</p>",
		"Vusion E300 Bluetooth electronic shelf label",
		"Bluetooth Low Energy\nGeolocation & guided pick\nWaterproof / freezer variants\nE700 full-colour option",
		"The connected-store label generation",
		"Price today. Location tomorrow.",
		"E300",
		"Bluetooth Vusion E300 ESL for pricing, product location and guided picking.",
		"Scope E300 with EdgeSense",
		"If the project includes picking or SKU location, we will quote E300 with rails and VusionCloud — not labels alone.",
		"Vusion E300 Electronic Shelf Labels Saudi Arabia | Bluetooth ESL | Printechs",
		"Vusion E300 Bluetooth electronic shelf labels enable pricing automation, product location, guided picking and connected-store workflows. From Printechs Saudi Arabia.",
		[
			{"icon": "connectivity", "title": "Bluetooth Low Energy", "description": "A standard radio for shelf devices, associates and applications.", "sort_order": 1},
			{"icon": "scan", "title": "Guided picking", "description": "Flash and locate the SKU instead of hunting the bay.", "sort_order": 2},
			{"icon": "store", "title": "Waterproof & freezer variants", "description": "Same generation for fresh IP68 and −25 °C aisles.", "sort_order": 3},
			{"icon": "display", "title": "E700 full colour", "description": "Larger connected displays for high-impact communication.", "sort_order": 4},
		],
		[
			{"label": "E300", "image": media["e300"], "image_alt": "E300", "caption": "Connected ESL endpoint.", "sort_order": 1},
			{"label": "Pick-to-light", "image": media["pick-to-light"], "image_alt": "Pick to light", "caption": "Associates follow the flash.", "sort_order": 2},
			{"label": "Dark store", "image": media["dark-store"], "image_alt": "Dark store", "caption": "Omnichannel aisles that cannot wait.", "sort_order": 3},
		],
		[
			{"icon": "connectivity", "title": "Radio", "description": "Bluetooth LE", "sort_order": 1},
			{"icon": "scan", "title": "Workflows", "description": "Pick · locate · navigate", "sort_order": 2},
			{"icon": "shield", "title": "Variants", "description": "WP IP68 · freezer −25 °C", "sort_order": 3},
			{"icon": "display", "title": "E700", "description": "Full-colour connected", "sort_order": 4},
		],
		[
			("Series", [
				("Series", "Vusion E300"),
				("Role", "BLE ESL for pricing and connected-store workflows"),
				("Variants", "E300 Waterproof (IP68) and E300 Freezer (−25 °C)"),
				("Related display", "E700 larger-format full-colour connected ESL"),
			]),
			("Platform", [
				("Connectivity", "Bluetooth Low Energy; VusionOX / EdgeSense ecosystem"),
				("Capabilities", "Geolocation, guided picking, shopper navigation when configured"),
			]),
		],
		"When to choose E300 over V300",
		"Choose E300 when the store needs location, hands-free picking or a path to EdgeSense — not only a cheaper colour ticket. Dark stores and omnichannel grocery are typical.",
		"pick-to-light", "E300 pick-to-light",
		"Quoted E300 labels (and WP/freezer variants as surveyed)",
		[
			{"question": "Is E300 just a Bluetooth V300?", "answer": "It is the connected-store generation. Pricing still matters; geolocation and workflows are why you pay for E-Series.", "sort_order": 1},
			{"question": "Do I need EdgeSense rails?", "answer": "For full location and rail-bus behaviour, yes. We will say so in the survey instead of hiding it.", "sort_order": 2},
			{"question": "Where does E700 sit?", "answer": "E700 is the large full-colour connected display in this family. Campaign ops are covered on the retail-media page.", "sort_order": 3},
		],
	)


def fill_edgesense(media):
	_page(
		media, "vusion-edgesense", "edgesense",
		"Vusion EdgeSense",
		"Vusion EdgeSense Connected Smart Shelf Platform",
		"SMART SHELF",
		"The shelf becomes a data layer — not a row of isolated tags.",
		"EdgeSense combines intelligent rails, Bluetooth connectivity, SKU location and connected applications for picking, replenishment and proximity interaction.",
		"<p>EdgeSense is the platform competitors cannot match with a cheaper clip-on tag. The "
		"<strong>EdgeSense Rail</strong> (IP52, 0–40 °C, rail-bus) powers and connects labels along "
		"the shelf. Products can be located, associates get pick and replenishment guidance, "
		"merchandising teams see execution, and shoppers can get proximity services.</p>"
		"<p>Published rail-bus labels include <strong>1.5\" BWRY</strong> (200×200, 186 DPI), "
		"<strong>2.1\" BWRY</strong> (248×128, 135 DPI) and <strong>2.6\" BWRY</strong> "
		"(296×152, 125 DPI), with RGB or BWR LEDs as specified. VusionOX supplies BLE, OTA upgrades "
		"and interoperability; VusionCloud is the estate layer. Captana cameras can sit on the same "
		"connected-store idea.</p>",
		"Vusion EdgeSense smart shelf rails with ESL labels",
		"SKU-level location\nRail-bus labels 1.5\"–2.6\"\nIP52 rail · 0–40 °C\nVusionOX + VusionCloud",
		"Connected store infrastructure — this is the differentiator",
		"One rail. Many devices.",
		"EdgeSense",
		"Vusion EdgeSense smart rails, BLE location and connected-shelf workflows.",
		"Scope EdgeSense as infrastructure",
		"We quote rails, labels, VusionCloud and associate apps together — not a tag unit price in isolation.",
		"Vusion EdgeSense Saudi Arabia | Connected Smart Shelf System | Printechs",
		"Transform retail shelves with Vusion EdgeSense in Saudi Arabia. Bluetooth smart rails, product geolocation, picking and replenishment from Printechs.",
		[
			{"icon": "connectivity", "title": "Shelf-edge rail bus", "description": "Labels sit on one powered, communicating rail instead of living alone.", "sort_order": 1},
			{"icon": "scan", "title": "SKU-level location", "description": "Find the product — then flash the facing for pick or replenishment.", "sort_order": 2},
			{"icon": "store", "title": "Merchandising compliance", "description": "Shelf execution data for planograms and promotions.", "sort_order": 3},
			{"icon": "integration", "title": "VusionOX interoperability", "description": "BLE standard, OTA upgrades and room for partner devices.", "sort_order": 4},
		],
		[
			{"label": "EdgeSense rails", "image": media["edgesense"], "image_alt": "EdgeSense rails", "caption": "The physical backbone.", "sort_order": 1},
			{"label": "Rail-bus label", "image": media["edgesense_label"], "image_alt": "EdgeSense label", "caption": "BWRY label designed for the rail.", "sort_order": 2},
			{"label": "In the aisle", "image": media["smart-rail"], "image_alt": "Smart rail grocery", "caption": "A continuous shelf-edge, not clips.", "sort_order": 3},
		],
		[
			{"icon": "device", "title": "Rail", "description": "IP52 · 0–40 °C", "sort_order": 1},
			{"icon": "display", "title": "Labels", "description": "1.5\" · 2.1\" · 2.6\" BWRY", "sort_order": 2},
			{"icon": "connectivity", "title": "Radio", "description": "BLE · VusionOX", "sort_order": 3},
			{"icon": "cloud", "title": "Cloud", "description": "VusionCloud", "sort_order": 4},
		],
		[
			("Platform", [
				("Platform", "Vusion EdgeSense"),
				("Rail", "EdgeSense Rail · rail-bus · IP52 · 0 °C to 40 °C · CE / RoHS / FCC/IC"),
				("1.5\" BWRY", "46.2 × 37.5 × 12.9 mm · 200 × 200 px · 186 DPI · RGB LED"),
				("2.1\" BWRY", "66.8 × 35.2 × 12.9 mm · 248 × 128 px · 135 DPI · RGB LED"),
				("2.6\" BWRY", "80.2 × 42.3 × 12.81 mm · 296 × 152 px · 125 DPI · BWR LED"),
			]),
			("Stack", [
				("VusionOX", "BLE standard, OTA upgrades, third-party interoperability"),
				("VusionCloud", "Geolocation, bi-directional beaconing, estate management"),
				("Optional", "Captana computer vision on the same connected-store programme"),
			]),
		],
		"How Printechs sells EdgeSense",
		"Not tag price — connected-store infrastructure with ERP/POS, handhelds, optional RFID and analytics. Hypermarkets, dark stores and omnichannel grocery are the usual KSA fits.",
		"associate-picking", "EdgeSense associate picking",
		"Quoted EdgeSense rails, rail-bus labels and VusionCloud scope",
		[
			{"question": "Do I need a page per 1.5 / 2.1 / 2.6?", "answer": "No. Those are sizes on this platform. We quote the mix after a shelf survey.", "sort_order": 1},
			{"question": "What is VusionOX?", "answer": "The BLE technology layer under EdgeSense — OTA upgrades and a path for other IoT devices on the same idea.", "sort_order": 2},
			{"question": "Can this work with Captana?", "answer": "Yes. Vusion positions EdgeSense with ESL and computer vision as one connected shelf.", "sort_order": 3},
		],
	)


def fill_cloud(media):
	_page(
		media, "vusion-vusioncloud", "cloud",
		"VusionCloud",
		"VusionCloud Retail IoT Platform",
		"RETAIL IOT CLOUD",
		"One cloud for labels, rails and store devices — integrated to your ERP and POS.",
		"VusionCloud is the estate layer for ESL and connected devices: deployment, health, pricing consistency and APIs.",
		"<p>Hardware only works if headquarters can trust it. VusionCloud centralises device "
		"management, connectivity, roll-out and monitoring so thousands of labels stay on the same "
		"price file as the till.</p>"
		"<p>Printechs’ job is the integration layer: ERP, POS, product master, pricing, promotions, "
		"inventory, store master and associate mobile apps. Connectivity options include native "
		"access-point integration, add-on integration and standalone <strong>V:Gate</strong> "
		"infrastructure — Vusion cites architectures that can support up to <strong>10,000 ESLs</strong> "
		"per access-point design, depending on configuration.</p>",
		"VusionCloud retail IoT management",
		"Multi-store device health\nERP / POS APIs\nNative · integrated · V:Gate\nUp to 10,000 ESL / AP architecture",
		"This is where Printechs earns the project",
		"Cloud first. Then the labels.",
		"VusionCloud",
		"Cloud management for Vusion ESL estates, integrations and device lifecycle.",
		"Integrate VusionCloud with your POS",
		"Bring the pricing source of truth — we will map it to labels, stores and health dashboards.",
		"VusionCloud Retail IoT Platform Saudi Arabia | ESL Management | Printechs",
		"Manage Electronic Shelf Labels and connected retail devices across multiple stores with VusionCloud. Cloud retail IoT from Printechs Saudi Arabia.",
		[
			{"icon": "cloud", "title": "Estate management", "description": "Deploy, monitor and update labels and IoT devices from one place.", "sort_order": 1},
			{"icon": "integration", "title": "ERP and POS APIs", "description": "Item, price, promotion, inventory and store master — not a USB file drop.", "sort_order": 2},
			{"icon": "report", "title": "Health dashboards", "description": "See a dark facing before a shopper does.", "sort_order": 3},
			{"icon": "connectivity", "title": "Flexible in-store radio", "description": "Native AP, integrated, or standalone V:Gate when the LAN cannot host ESL.", "sort_order": 4},
		],
		[
			{"label": "Cloud studio", "image": media["cloud"], "image_alt": "VusionCloud", "caption": "Estate view for labels and devices.", "sort_order": 1},
			{"label": "HQ", "image": media["hq-dashboard"], "image_alt": "HQ dashboard", "caption": "Consistency across the chain.", "sort_order": 2},
			{"label": "In store", "image": media["store-tablet"], "image_alt": "Store tablet", "caption": "Health in the manager’s hand.", "sort_order": 3},
		],
		[
			{"icon": "cloud", "title": "Layer", "description": "VusionCloud", "sort_order": 1},
			{"icon": "integration", "title": "Systems", "description": "ERP · POS · inventory", "sort_order": 2},
			{"icon": "connectivity", "title": "In-store", "description": "Native · integrated · V:Gate", "sort_order": 3},
			{"icon": "device", "title": "Scale", "description": "Up to 10k ESL / AP design", "sort_order": 4},
		],
		[
			("Platform", [
				("Platform", "VusionCloud"),
				("Role", "Central cloud for ESL and connected-store devices"),
				("APIs", "Integration for pricing, promotions, item and store masters"),
				("Operations", "Device lifecycle, health dashboards, multi-store deployment"),
			]),
			("Connectivity", [
				("Native", "Uses existing store access points (infraless model)"),
				("Integrated", "Minimal extra hardware on the current LAN"),
				("Standalone V:Gate", "Dedicated ESL connectivity; up to 10,000 ESLs per AP architecture"),
			]),
		],
		"What we integrate in Saudi projects",
		"Modern POS, ERPNext, Retail Pro and other pricing sources; promotion calendars; store master; associate devices. Cloud activation and per-store appliances already exist as SES service SKUs in our ERP when a project needs them.",
		"hq-dashboard", "VusionCloud HQ",
		"VusionCloud subscription / activation and integration scope as quoted",
		[
			{"question": "Is this on-premise or cloud?", "answer": "VusionCloud is the cloud estate. Some stores still use appliances or existing APs — we confirm during survey.", "sort_order": 1},
			{"question": "What is V:Gate?", "answer": "Standalone plug-and-play ESL connectivity when you cannot or should not share the store Wi-Fi.", "sort_order": 2},
			{"question": "Can you connect ERPNext or Modern POS?", "answer": "Yes. That integration layer is a core Printechs service, not a Vusion brochure line.", "sort_order": 3},
		],
	)


def fill_captana(media):
	_page(
		media, "vusion-captana", "captana",
		"Vusion Captana Computer Vision",
		"AI-Powered Retail Shelf Monitoring with Vusion Captana",
		"SHELF COMPUTER VISION",
		"Know the shelf without walking every aisle.",
		"Captana uses connected cameras and computer vision to find stockouts, planogram errors and misplaced products — then turn them into associate tasks.",
		"<p>Captana watches facings, not people. GDPR-oriented shelf cameras analyse images for empty "
		"slots, location errors, merchandising drift and inventory discrepancies, then raise "
		"prioritised work.</p>"
		"<p><strong>ShelfEye</strong> is the shelf-focused camera: Vusion and partners describe a "
		"shelf-optimised unit (commonly cited around 12 MP), autofocus, motion sensing, Easylock "
		"positioning, rechargeable batteries and a configurable status LED. It can run with supported "
		"integrations even when the project is not an ESL-only estate.</p>"
		"<p>Vusion has published directional outcomes on some programmes (for example on-shelf "
		"availability and labour efficiency). We treat those as vendor figures and size KSA benefits "
		"from your own gap-scan baseline.</p>",
		"Vusion Captana ShelfEye camera and shelf-monitoring dashboard",
		"Out-of-stock detection\nPlanogram compliance\nShelfEye cameras\nTasks to associates",
		"A camera that creates work, not a photo album",
		"See the gap. Send the task.",
		"Captana",
		"Vusion Captana computer vision and ShelfEye cameras for shelf availability and planograms.",
		"Add Captana to grocery and hypermarket projects",
		"We will say whether cameras should ride with ESL/EdgeSense or stand alone against your VMS and task app.",
		"Vusion Captana Retail Computer Vision Saudi Arabia | Shelf Monitoring AI | Printechs",
		"Detect out-of-stock products, planogram errors and shelf execution issues with Vusion Captana Computer Vision. Smart shelf monitoring by Printechs Saudi Arabia.",
		[
			{"icon": "scan", "title": "Out-of-stock detection", "description": "Empty facings become a task, not a surprise at audit.", "sort_order": 1},
			{"icon": "store", "title": "Planogram compliance", "description": "See misplaced or missing items without a clipboard walk.", "sort_order": 2},
			{"icon": "device", "title": "ShelfEye cameras", "description": "Shelf-optimised, low-power cameras with Easylock positioning.", "sort_order": 3},
			{"icon": "report", "title": "Associate workflows", "description": "Insights become replenishment and merchandising work.", "sort_order": 4},
		],
		[
			{"label": "Captana + ShelfEye", "image": media["captana"], "image_alt": "Captana", "caption": "Camera plus the operations view.", "sort_order": 1},
			{"label": "Empty facing", "image": media["empty-shelf"], "image_alt": "Empty shelf", "caption": "The gap the walk used to miss.", "sort_order": 2},
			{"label": "Planogram", "image": media["planogram"], "image_alt": "Planogram", "caption": "Continuous shelf truth.", "sort_order": 3},
		],
		[
			{"icon": "scan", "title": "Detect", "description": "OOS · misplace · gaps", "sort_order": 1},
			{"icon": "device", "title": "ShelfEye", "description": "Shelf camera · Easylock", "sort_order": 2},
			{"icon": "cloud", "title": "Platform", "description": "Cloud shelf analytics", "sort_order": 3},
			{"icon": "report", "title": "Output", "description": "Associate tasks", "sort_order": 4},
		],
		[
			("Solution", [
				("Solution", "Vusion Captana computer vision"),
				("Hardware", "ShelfEye shelf-optimised cameras (autofocus, motion sensor, Easylock, rechargeable)"),
				("Privacy", "Vusion positions cameras as GDPR-oriented shelf monitoring, not people tracking"),
				("Use cases", "OOS, availability, planogram, misplaced product, shelf audit, replenishment priority"),
			]),
			("Operations", [
				("Output", "Alerts and tasks for store associates"),
				("Independence", "Can operate with supported integrations outside a pure ESL stack"),
			]),
		],
		"Strongest KSA fit",
		"Hypermarkets and supermarkets that already lose hours to gap scans. Pair with V300/EdgeSense when you want price, location and availability in one programme.",
		"empty-shelf", "Captana empty shelf",
		"Quoted ShelfEye cameras, Captana cloud and task integration",
		[
			{"question": "Is ShelfEye a separate product page?", "answer": "No. ShelfEye is the camera inside Captana. One page keeps the conversation on the outcome.", "sort_order": 1},
			{"question": "Does it photograph shoppers?", "answer": "Vusion positions the system for shelf monitoring with motion/privacy design. We still review KSA privacy expectations in the survey.", "sort_order": 2},
			{"question": "Can it run without ESL?", "answer": "Supported integrations allow shelf monitoring without making every facing an ESL first. Many projects still combine both.", "sort_order": 3},
		],
	)


def fill_media(media):
	_page(
		media, "vusion-retail-media", "media",
		"Vusion In-Store Retail Media",
		"Vusion In-Store Digital Retail Media",
		"RETAIL MEDIA",
		"Turn shelf traffic into a scheduled advertising channel.",
		"Vusion in-store retail media lets retailers and brands run centrally managed campaigns on e-paper, V700 full-colour ESL and LCD — next to the product.",
		"<p>This is how the conversation leaves “save paper.” A retailer can sell a two-week launch "
		"slot at the shelf; a brand can put creative where the hand reaches; both sides can look at "
		"campaign analytics instead of a faded cardboard header.</p>"
		"<p>Supported faces include low-power e-paper, larger full-colour ESL such as "
		"<a href=\"/products/vusion-v700\">V700</a> / E700, and LCD video where the bay needs motion. "
		"Scheduling lives with the same connected-store cloud as pricing.</p>"
		"<p>Typical Saudi stories: an FMCG launch in a hypermarket, a cosmetics range in beauty, an "
		"electronics accessory push. We do not invent brand contracts — we build the channel those "
		"contracts can buy.</p>",
		"Vusion full-color digital shelf retail media display",
		"Shelf-edge campaigns\nV700 / E700 / LCD\nCentral scheduling\nBrand + retailer revenue",
		"From saving paper to earning the facing",
		"Creative where the basket is decided",
		"Retail Media",
		"In-store digital shelf advertising with Vusion ESL and full-colour displays.",
		"Design a shelf-media pilot",
		"Pick one category — beauty, grocery feature or electronics — and we will spec screens, scheduling and measurement.",
		"Vusion Retail Media Saudi Arabia | Digital Shelf Advertising | Printechs",
		"Turn retail shelves into digital advertising channels with Vusion in-store retail media. Targeted promotions from Printechs Saudi Arabia.",
		[
			{"icon": "loyalty", "title": "A new revenue line", "description": "Sell scheduled shelf slots instead of one printed header a season.", "sort_order": 1},
			{"icon": "display", "title": "The right screen per bay", "description": "E-paper, V700 full colour or LCD — not one panel everywhere.", "sort_order": 2},
			{"icon": "cloud", "title": "Central control", "description": "Start and stop campaigns with the same discipline as prices.", "sort_order": 3},
			{"icon": "report", "title": "Campaign analytics", "description": "Give brands proof the facing actually ran.", "sort_order": 4},
		],
		[
			{"label": "Display", "image": media["media"], "image_alt": "Retail media display", "caption": "Full-colour shelf creative.", "sort_order": 1},
			{"label": "Shopper", "image": media["shopper-media"], "image_alt": "Shopper media", "caption": "The decision is at the shelf.", "sort_order": 2},
			{"label": "End cap", "image": media["brand-campaign"], "image_alt": "Brand campaign", "caption": "A bay brands can book.", "sort_order": 3},
		],
		[
			{"icon": "display", "title": "Faces", "description": "E-paper · V700 · LCD", "sort_order": 1},
			{"icon": "loyalty", "title": "Buyer", "description": "Retailer + brand", "sort_order": 2},
			{"icon": "cloud", "title": "Control", "description": "Scheduled campaigns", "sort_order": 3},
			{"icon": "report", "title": "Proof", "description": "Campaign analytics", "sort_order": 4},
		],
		[
			("Programme", [
				("Programme", "Vusion in-store digital retail media / Engage"),
				("Displays", "Low-power e-paper, full-colour ESL (V700/E700), LCD video"),
				("Control", "Centrally scheduled campaigns"),
				("Hardware page", "V700 for the 8.2-inch full-colour shelf display"),
			]),
		],
		"Saudi categories that buy this first",
		"Cosmetics and beauty, electronics accessories, pharmacy feature, and FMCG launch end caps in hypermarkets.",
		"brand-campaign", "Retail media end cap",
		"Quoted campaign displays, scheduling and measurement scope",
		[
			{"question": "Is this the same as V700?", "answer": "V700 is a display. This page is the commercial model — who pays, who schedules, what is measured.", "sort_order": 1},
			{"question": "Do we need ESL everywhere first?", "answer": "A pilot can start on feature bays. Chain-wide ESL still helps because price and creative share one cloud.", "sort_order": 2},
			{"question": "Can Printechs run a pilot in KSA?", "answer": "Yes. We spec hardware, cloud scheduling and a simple measurement story with the retailer.", "sort_order": 3},
		],
	)


def fill_vusion_esl():
	media = prepare_media()
	fill_hub(media)
	fill_series(media)
	fill_edgesense(media)
	fill_cloud(media)
	fill_captana(media)
	fill_media(media)
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
	print("Wired Vusion related products and brand")
	return "ok"


def _update_brand(media):
	logo = media["logo"]
	name = frappe.db.get_value("Website Brand", {"slug": "vusion"}, "name")
	doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
	if not frappe.db.exists("Brand", "SES-imagotag"):
		frappe.throw("ERP Brand SES-imagotag was not found")
	doc.brand = "SES-imagotag"
	doc.display_name = "Vusion"
	doc.slug = "vusion"
	doc.logo = logo
	doc.summary = (
		"Vusion / SES-imagotag electronic shelf labels, EdgeSense, Captana and VusionCloud "
		"for Saudi grocery, pharmacy and retail chains — integrated by Printechs."
	)
	doc.sort_order = 8
	doc.published = 1
	doc.meta_title = "Vusion ESL Saudi Arabia | SES-imagotag | Printechs Brands"
	doc.meta_description = (
		"Vusion and SES-imagotag electronic shelf labels, smart shelves and computer vision "
		"from Printechs in Saudi Arabia."
	)
	doc.flags.ignore_permissions = True
	if name:
		doc.save()
	else:
		doc.insert()
	frappe.db.commit()
