# Copyright (c) 2026, Printechs and contributors
"""Avery Berkel retail weighing lineup for Printechs.

Hub + Xs / XTs / XTi series pages + 17 model pages.

Hero is always a high-quality product image (no video overlay).
YouTube IDs are unique and used only on series pages, never in the hero.
Manufacturer naming: Xs, XTs, XTi.
"""

import frappe

from printechs_digital.setup.avery_berkel_common import (
	apply_brochures,
	apply_identity,
	get_or_create,
	prepare_media,
	save_product,
	scene_apps,
	set_related,
	set_specs,
	support_items,
)
from printechs_digital.setup.avery_berkel_specs import specs_for

VIDEO_XS = "https://youtu.be/ile0NPpzS8M"  # XS100/200/400 PLU setup — Xs series only
VIDEO_XT = "https://youtu.be/Euy6-TDba8I"  # XTi/XTs label cassette — XTs series only

RELATED = {
	"avery-berkel": [
		"avery-berkel-xti420",
		"avery-berkel-xti400",
		"avery-berkel-xti300",
		"avery-berkel-xts500",
	],
	"avery-berkel-xs-series": ["avery-berkel-xs100", "avery-berkel-xs200", "avery-berkel-xs400", "avery-berkel-xs500"],
	"avery-berkel-xts-series": ["avery-berkel-xts100", "avery-berkel-xts420", "avery-berkel-xts500", "avery-berkel-xts600"],
	"avery-berkel-xti-series": ["avery-berkel-xti420", "avery-berkel-xti400", "avery-berkel-xti200", "avery-berkel-xti300"],
	"avery-berkel-xs100": ["avery-berkel-xs200", "avery-berkel-xs400", "avery-berkel-xts100"],
	"avery-berkel-xs200": ["avery-berkel-xs100", "avery-berkel-xs400", "avery-berkel-xts200"],
	"avery-berkel-xs400": ["avery-berkel-xs200", "avery-berkel-xs100", "avery-berkel-xti400"],
	"avery-berkel-xs500": ["avery-berkel-xts500", "avery-berkel-xs100", "avery-berkel-xs400"],
	"avery-berkel-xts100": ["avery-berkel-xts200", "avery-berkel-xti100", "avery-berkel-xs100"],
	"avery-berkel-xts200": ["avery-berkel-xts100", "avery-berkel-xti200", "avery-berkel-xs200"],
	"avery-berkel-xts400": ["avery-berkel-xts420", "avery-berkel-xti400", "avery-berkel-xs400"],
	"avery-berkel-xts420": ["avery-berkel-xts400", "avery-berkel-xti420", "avery-berkel-xts200"],
	"avery-berkel-xts500": ["avery-berkel-xs500", "avery-berkel-xti300", "avery-berkel-xts100"],
	"avery-berkel-xts600": ["avery-berkel-xti600", "avery-berkel-xts700", "avery-berkel-xts100"],
	"avery-berkel-xts700": ["avery-berkel-xts600", "avery-berkel-xti420", "avery-berkel-xts400"],
	"avery-berkel-xti100": ["avery-berkel-xti200", "avery-berkel-xts100", "avery-berkel-xti400"],
	"avery-berkel-xti200": ["avery-berkel-xti400", "avery-berkel-xti420", "avery-berkel-xts200"],
	"avery-berkel-xti300": ["avery-berkel-xti200", "avery-berkel-xts500", "avery-berkel-xti400"],
	"avery-berkel-xti400": ["avery-berkel-xti420", "avery-berkel-xti200", "avery-berkel-xts400"],
	"avery-berkel-xti420": ["avery-berkel-xti400", "avery-berkel-xts420", "avery-berkel-xti600"],
	"avery-berkel-xti600": ["avery-berkel-xts600", "avery-berkel-xti420", "avery-berkel-xti400"],
}


def _ksa(model: str) -> str:
	return (
		f"Printechs supplies and supports Avery Berkel {model} across Saudi Arabia, "
		f"including Jeddah, Riyadh and Dammam — installation, labels, MXBusiness and service."
	)


def fill_hub(media):
	slug = "avery-berkel"
	card = media["hub"]
	doc = get_or_create(slug, "Avery Berkel Retail Weighing", "", card, "Retail Weighing")
	apply_identity(
		doc,
		slug=slug,
		display_name="Avery Berkel Retail Weighing",
		item="",
		subcategory="Retail Weighing",
		category_label="AVERY BERKEL RETAIL SCALES",
		featured=0,
	)
	doc.tagline = "Tactile Xs, affordable XTs touchscreen, premium XTi — one fresh-food platform"
	doc.short_description = (
		"Avery Berkel retail weighing and labelling for Saudi supermarkets, butcheries, "
		"delis, bakeries and seafood counters. Choose Xs for tactile keys, XTs for 7-inch "
		"touch, or XTi for 10.1-inch and self-service — with Printechs installation and MXBusiness."
	)
	doc.long_description = (
		"<p>Avery Berkel is Printechs’ retail weighing brand for fresh-food counters in "
		"Saudi Arabia. Official naming is Xs, XTs and XTi — not a single generic “scale”.</p>"
		"<p><strong>Xs</strong> is the cost-effective tactile-key range: compact Xs100, "
		"raised-display Xs200, tower Xs400 and hanging Xs500 for wet/fish counters.</p>"
		"<p><strong>XTs</strong> is the entry XT touchscreen platform (7-inch operator "
		"display, high-speed cassette printer, ValuMax, Ethernet / compatible Wi-Fi). "
		"XTs600 is a non-weighing label/EPOS terminal. XTs700 is a complementary second printer.</p>"
		"<p><strong>XTi</strong> is the premium XT configuration — typically a 10.1-inch "
		"operator touchscreen. XTi300 is the 18.5-inch self-service model. XTi420 is the "
		"dual-printer counter/POS workstation. XTi600 is the non-weighing bakery/pre-pack terminal.</p>"
		"<p>Printechs specifies the right family for Jeddah, Riyadh and Dammam stores, "
		"then supports labels, networking and MXBusiness / MXi-Pro.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Avery Berkel retail scale on a fresh-food service counter"
	doc.hero_trust_chips = "Xs tactile · XTs 7-inch · XTi 10.1-inch\nLabels, receipts and pre-pack\nMXBusiness central management\nJeddah · Riyadh · Dammam"
	doc.story_heading = "Three families, one Saudi retail weighing partner"
	doc.visual_story_heading = "Xs → XTs → XTi"
	doc.card_title = "Avery Berkel Scales"
	doc.card_summary = "Xs tactile, XTs touchscreen and XTi premium retail weighing for KSA fresh-food counters."
	doc.card_image = card
	doc.final_cta_heading = "Specify Avery Berkel for your counters"
	doc.final_cta_description = "Tell Printechs the department, capacity and label vs receipt workflow. We will map Xs, XTs or XTi."
	doc.meta_title = "Avery Berkel Retail Weighing Scales Saudi Arabia | Printechs"
	doc.meta_description = (
		"Avery Berkel Xs, XTs and XTi retail weighing and label printing scales for "
		"supermarkets, butcheries and delis in Saudi Arabia. Supplied by Printechs."
	)
	doc.set("benefits", [
		{"icon": "store", "title": "Xs — tactile and cost-effective", "description": "Physical PLU keys for busy butcher, deli and grocery counters that prefer a keyboard.", "sort_order": 1},
		{"icon": "display", "title": "XTs — affordable colour touch", "description": "7-inch operator touchscreen, promotions on the customer display, XT printer platform.", "sort_order": 2},
		{"icon": "checkout", "title": "XTi — premium and self-service", "description": "Larger screens, dual-printer XTi420, 18.5-inch XTi300 self-service, bakery XTi600.", "sort_order": 3},
		{"icon": "print", "title": "Labels, receipts, pre-pack", "description": "One vendor for counter labels, nutrition labels and receipt/POS — not a bare scale.", "sort_order": 4},
		{"icon": "connectivity", "title": "MXBusiness in the store", "description": "Network scales for product, price and configuration updates from the back office.", "sort_order": 5},
		{"icon": "shield", "title": "Printechs in KSA", "description": "Local specification, labels, installation and service in Jeddah, Riyadh and Dammam.", "sort_order": 6},
	])
	doc.set("visual_story_items", [
		{"label": "At the counter", "image": media["hub_scene"], "image_alt": "Service counter with Avery Berkel scale", "caption": "Weigh, price and label in front of the customer.", "sort_order": 1},
		{"label": "Xs family", "image": media["xs_series_scene"], "image_alt": "Avery Berkel Xs on a fresh-food counter", "caption": "Tactile Xs — the cost-effective starting point.", "sort_order": 2},
		{"label": "XTi family", "image": media["food"], "image_alt": "Fresh-food retail", "caption": "Premium XTi — weigh, promote and print at the counter.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "store", "title": "Xs", "description": "Tactile keys · 15 kg AVR", "sort_order": 1},
		{"icon": "display", "title": "XTs", "description": "7-inch colour touch", "sort_order": 2},
		{"icon": "checkout", "title": "XTi", "description": "10.1-inch · self-service", "sort_order": 3},
		{"icon": "print", "title": "Print", "description": "Labels · receipts · linerless", "sort_order": 4},
	])
	set_specs(doc, specs_for(slug))
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "Avery Berkel technology", "body": "ValuMax keeps weighing accurate when the counter is not perfectly level. CodeChecker watches print quality. XT prints up to 150 mm/sec with edge-to-edge and linerless options. Network scales to MXBusiness.", "image": media["hub_scene"], "image_alt": "Avery Berkel service counter", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Why Printechs in Saudi Arabia", "body": "We specify Xs vs XTs vs XTi for each department, then install, load PLUs, supply labels and support MXBusiness in Jeddah, Riyadh and Dammam — a retail weighing solution, not a box on a pallet.", "image": media["retail"], "image_alt": "Retail", "link_label": "See Modern POS", "link_href": "/software/modern-pos", "sort_order": 2},
	])
	doc.set("support_items", support_items("Counter survey, capacity and label vs receipt workflow.", "Label stock, linerless, receipts and print-head kits.", "Calibration, spare parts and on-site service in KSA.", "Operator PLU, hygiene and MXBusiness admin."))
	apply_brochures(doc, slug)
	doc.set("package_contents", [{"item_description": "Quoted Xs, XTs or XTi model", "sort_order": 1}, {"item_description": "Starter label/receipt media as quoted", "sort_order": 2}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Xs, XTs or XTi?", "answer": "Xs is tactile and cost-effective. XTs is 7-inch touch. XTi is the larger-screen premium and self-service family. Printechs will map the department before you buy.", "sort_order": 1},
		{"question": "Are all models weighing scales?", "answer": "No. XTs600 and XTi600 are non-weighing terminals/printers. XTs700 is a complementary second printer. XTi300 is self-service. Xs500 and XTs500 are hanging scales for wet/fish counters.", "sort_order": 2},
		{"question": "Do you support Avery Berkel in Saudi Arabia?", "answer": "Yes. Printechs is the local partner for specification, labels, installation, MXBusiness and service in Jeddah, Riyadh and Dammam.", "sort_order": 3},
	])
	return save_product(doc, card)


def fill_xs_series(media):
	slug = "avery-berkel-xs-series"
	card = media["xs-series"]
	doc = get_or_create(slug, "Avery Berkel Xs Series", "", card, "Tactile Retail Scales")
	apply_identity(doc, slug=slug, display_name="Avery Berkel Xs Series", item="", subcategory="Tactile Retail Scales", category_label="XS TACTILE RETAIL SCALES", on_list=False)
	doc.tagline = "Cost-effective tactile-key retail weighing — Xs100, Xs200, Xs400, Xs500"
	doc.short_description = (
		"Avery Berkel Xs is the tactile-key retail weighing range: monobloc Xs100, "
		"raised-display Xs200, tower Xs400 and hanging Xs500. Built for butcheries, "
		"delis and grocery counters that want physical PLU keys and integrated printing."
	)
	doc.long_description = (
		"<p>Xs is Avery Berkel’s cost-effective tactile retail family. Operators who prefer "
		"physical keys get fast PLU selection, integrated label/receipt printing and "
		"networked prices — without a full colour touchscreen.</p>"
		"<p>Xs100 is the compact monobloc. Xs200 lifts the customer display. Xs400 puts "
		"keyboard and displays on a tower to free the counter. Xs500 hangs the pan for "
		"fish and wet food. Typical weighing is 15 kg AVR; other capacities depend on version.</p>"
		"<p>Use Xs when the job is traditional counter service. Step to XTs or XTi when "
		"you want colour promotions, larger touch targets or dual printers.</p>"
		f"<p>{_ksa('Xs series')}</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Avery Berkel Xs100 on a fresh-food counter"
	doc.hero_trust_chips = "Tactile PLU keyboard\nXs100 · Xs200 · Xs400 · Xs500\nLabel and receipt printing\nEthernet / compatible Wi-Fi"
	doc.story_heading = "Physical keys, professional labels"
	doc.visual_story_heading = "Xs family"
	doc.card_title = "Xs Series"
	doc.card_summary = "Tactile-key retail scales: Xs100, Xs200, Xs400 and hanging Xs500."
	doc.card_image = card
	doc.final_cta_heading = "Choose an Xs form factor"
	doc.final_cta_description = "Confirm monobloc, pole display, tower or hanging — and 15 kg AVR vs other capacities."
	doc.meta_title = "Avery Berkel Xs Series Retail Scales Saudi Arabia | Printechs"
	doc.meta_description = "Avery Berkel Xs tactile retail weighing scales for Saudi butcheries, delis and grocery counters. Xs100, Xs200, Xs400 and hanging Xs500 from Printechs."
	doc.set("benefits", [
		{"icon": "store", "title": "Tactile and fast", "description": "Physical PLU and function keys for operators who do not want a touch-only UI.", "sort_order": 1},
		{"icon": "print", "title": "Labels and receipts", "description": "Integrated thermal printing with CodeChecker print-head diagnostics.", "sort_order": 2},
		{"icon": "device", "title": "Four form factors", "description": "Monobloc, raised customer display, raised keyboard, or hanging pan.", "sort_order": 3},
		{"icon": "connectivity", "title": "Network ready", "description": "Ethernet and compatible Wi-Fi for centrally managed products and prices.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Xs on the counter", "image": media["xs_series_scene"], "image_alt": "Xs100 scene", "caption": "Compact monobloc — keyboard, displays and printer in one unit.", "sort_order": 1},
		{"label": "Service", "image": media["hub_scene"], "image_alt": "Xs service counter", "caption": "Tactile keys for butcher, deli and grocery.", "sort_order": 2},
		{"label": "Fresh food", "image": media["food"], "image_alt": "Fresh food", "caption": "Hanging Xs500 covers fish and wet counters.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "store", "title": "Interface", "description": "Tactile PLU keyboard", "sort_order": 1},
		{"icon": "print", "title": "Print", "description": "Thermal label / receipt", "sort_order": 2},
		{"icon": "inventory", "title": "Capacity", "description": "Typically 15 kg AVR", "sort_order": 3},
		{"icon": "connectivity", "title": "Network", "description": "Ethernet · Wi-Fi option", "sort_order": 4},
	])
	set_specs(doc, specs_for(slug))
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "Set up products on Xs", "body": "Independent tutorial for Xs100 / Xs200 / Xs400 PLU setup. This page is the Xs tactile family — not XTs or XTi.", "video_url": VIDEO_XS, "image": media["xs_series_scene"], "image_alt": "Xs family", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "Xs with Printechs in KSA", "body": _ksa("Xs") + " Ask for Xs100 if space is tight, Xs400 if you want a clear counter, Xs500 for fish.", "image": media["retail"], "image_alt": "Retail", "sort_order": 2},
	])
	doc.set("support_items", support_items("Choose form factor and capacity.", "Xs label/receipt media.", "Keyboard overlays and print heads.", "PLU and CodeChecker basics."))
	apply_brochures(doc, slug)
	doc.set("package_contents", [{"item_description": "Quoted Xs model", "sort_order": 1}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Is Xs a touchscreen?", "answer": "No. Xs uses a tactile keyboard. Colour touch is XTs (7-inch) or XTi (10.1-inch and larger).", "sort_order": 1},
		{"question": "Which Xs for fish?", "answer": "Xs500 is the hanging model designed for wet areas. Do not specify a bench Xs100 for a seafood well.", "sort_order": 2},
		{"question": "Can I network Xs scales?", "answer": "Yes. Ethernet and compatible Wi-Fi support centrally managed product and price data.", "sort_order": 3},
	])
	return save_product(doc, card)


def fill_xts_series(media):
	slug = "avery-berkel-xts-series"
	card = media["xts-series"]
	doc = get_or_create(slug, "Avery Berkel XTs Series", "", card, "Touchscreen Retail Scales")
	apply_identity(doc, slug=slug, display_name="Avery Berkel XTs Series", item="", subcategory="Touchscreen Retail Scales", category_label="XTS TOUCHSCREEN SCALES", on_list=False)
	doc.tagline = "7-inch colour touch + tactile keys — the affordable XT platform"
	doc.short_description = (
		"Avery Berkel XTs is the entry XT touchscreen family: 7-inch operator display, "
		"high-speed cassette printing, ValuMax and MXBusiness. Includes hanging XTs500, "
		"dual-printer XTs420 and non-weighing XTs600 / complementary XTs700."
	)
	doc.long_description = (
		"<p>XTs shares the XT architecture — Linux, cassette printer up to 150 mm/sec, "
		"70 mm print width, edge-to-edge, CodeChecker, greyscale/logos and linerless "
		"where configured — with a 7-inch colour operator touchscreen and tactile keys.</p>"
		"<p>XTs100 is the compact monobloc. XTs200 raises the customer display. XTs400 "
		"raises both displays. XTs420 adds a second clamshell printer. XTs500 hangs for "
		"seafood. XTs600 is a non-weighing label/EPOS terminal. XTs700 is a USB secondary printer.</p>"
		f"<p>{_ksa('XTs series')} Step up to XTi when you need a 10.1-inch operator screen or 18.5-inch self-service.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Avery Berkel XTs420 and XTs600 XT family pair"
	doc.hero_trust_chips = "7-inch operator touch\nUp to 150 mm/sec print\nValuMax · CodeChecker\nXTs420 dual printer"
	doc.story_heading = "Affordable colour touch for fresh-food counters"
	doc.visual_story_heading = "XTs family"
	doc.card_title = "XTs Series"
	doc.card_summary = "7-inch XT touchscreen scales, hanging XTs500, dual-print XTs420 and XTs600 terminal."
	doc.card_image = card
	doc.final_cta_heading = "Specify an XTs configuration"
	doc.final_cta_description = "Confirm 7/7 displays, hanging vs bench, one printer vs XTs420, or a non-weighing XTs600."
	doc.meta_title = "Avery Berkel XTs Series Touchscreen Scales Saudi Arabia | Printechs"
	doc.meta_description = "Avery Berkel XTs 7-inch touchscreen retail scales for Saudi Arabia. Label printing, hanging seafood, dual printers and XTs600 terminals from Printechs."
	doc.set("benefits", [
		{"icon": "display", "title": "7-inch colour + keys", "description": "Touch for pictures and promotions; tactile keys for speed on a busy counter.", "sort_order": 1},
		{"icon": "print", "title": "XT printer platform", "description": "Cassette printer, 150 mm/sec, edge-to-edge, CodeChecker, linerless options.", "sort_order": 2},
		{"icon": "speed", "title": "ValuMax", "description": "Automatic level correction on weighing models so a slightly unlevel counter still trades.", "sort_order": 3},
		{"icon": "device", "title": "More than one shape", "description": "Monobloc, pole, tower, hanging, dual-print, terminal and secondary printer.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "XTs family", "image": media["xts_series_pair"], "image_alt": "XTs420 and XTs600", "caption": "Raised dual-print XTs beside a non-weighing 600 terminal.", "sort_order": 1},
		{"label": "Fresh food", "image": media["food"], "image_alt": "Fresh food", "caption": "7-inch colour touch for supermarket counters.", "sort_order": 2},
		{"label": "Retail", "image": media["retail"], "image_alt": "Retail", "caption": "Hanging XTs500 covers seafood and wet counters.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "display", "title": "Operator", "description": "7-inch colour touch", "sort_order": 1},
		{"icon": "print", "title": "Print", "description": "150 mm/sec cassette", "sort_order": 2},
		{"icon": "connectivity", "title": "I/O", "description": "Ethernet · Wi-Fi · USB", "sort_order": 3},
		{"icon": "cloud", "title": "Software", "description": "MXBusiness compatible", "sort_order": 4},
	])
	set_specs(doc, specs_for(slug))
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "Change an XT label cassette", "body": "How to load labels on XTs / XTi cassette printers. This page is the XTs 7-inch family — not XTi 10.1-inch and not Xs.", "video_url": VIDEO_XT, "image": media["xts_series_pair"], "image_alt": "XTs family", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "XTs in Saudi stores", "body": _ksa("XTs") + " Quote Eco III SKUs only when that is the stocked configuration — this family page is not a single Item.", "image": media["retail"], "image_alt": "Retail", "sort_order": 2},
	])
	doc.set("support_items", support_items("7/7 vs raised displays and printer count.", "Cassette labels, linerless and receipts.", "ValuMax check and print-head service.", "Touch + key operation and MXBusiness."))
	apply_brochures(doc, slug)
	doc.set("package_contents", [{"item_description": "Quoted XTs model", "sort_order": 1}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "XTs or XTi?", "answer": "XTs is 7-inch operator touch. XTi is typically 10.1-inch (18.5-inch on XTi300). Same XT print and network ideas; different screen class.", "sort_order": 1},
		{"question": "What is XTs600?", "answer": "A non-weighing label printer / EPOS terminal. Pair it with an external platform if you still need weight.", "sort_order": 2},
		{"question": "What is XTs700?", "answer": "A complementary USB printer so a second label size stays loaded — not a scale.", "sort_order": 3},
	])
	return save_product(doc, card)


def fill_xti_series(media):
	slug = "avery-berkel-xti-series"
	card = media["xti-series"]
	doc = get_or_create(slug, "Avery Berkel XTi Series", "", card, "Premium Touchscreen Scales")
	apply_identity(doc, slug=slug, display_name="Avery Berkel XTi Series", item="", subcategory="Premium Touchscreen Scales", category_label="XTI PREMIUM TOUCHSCREEN", on_list=False)
	doc.tagline = "Premium XT — 10.1-inch touch, self-service XTi300, dual-printer XTi420"
	doc.short_description = (
		"Avery Berkel XTi is the advanced XT configuration: 10.1-inch operator touchscreens "
		"(18.5-inch on XTi300), ValuMax, five USB ports, Ethernet / Wi-Fi and 150 mm/sec "
		"printing. Flagship XTi420 weighs, labels and prints receipts at one station."
	)
	doc.long_description = (
		"<p>XTi is the premium touchscreen side of the XT platform. Most models use a "
		"10.1-inch operator display and a 7-inch or 10.1-inch customer display. Linux, "
		"Ethernet, compatible Wi-Fi, five USB interfaces, edge-to-edge thermal printing "
		"and ValuMax on weighing models are the shared foundation.</p>"
		"<p>XTi100 is the compact monobloc. XTi200 raises the customer display. XTi300 is "
		"the 18.5-inch self-service produce scale. XTi400 raises both displays. XTi420 "
		"adds dual printers for weigh + label + receipt/POS. XTi600 is the non-weighing "
		"bakery / pre-pack / EPOS terminal.</p>"
		f"<p>{_ksa('XTi series')} These six models deserve the strongest SEO and sales attention on the Printechs site.</p>"
	)
	doc.hero_image = card
	doc.hero_image_alt = "Avery Berkel XTi scale on a butchery counter"
	doc.hero_trust_chips = "10.1-inch operator touch\nXTi300 18.5-inch self-service\nXTi420 dual printers\nValuMax · MXBusiness"
	doc.story_heading = "Premium touchscreen retail weighing"
	doc.visual_story_heading = "XTi family"
	doc.card_title = "XTi Series"
	doc.card_summary = "Premium XT: 10.1-inch touch, XTi300 self-service, XTi420 dual-printer, XTi600 terminal."
	doc.card_image = card
	doc.final_cta_heading = "Specify an XTi workstation"
	doc.final_cta_description = "Confirm screen sizes, one vs two printers, self-service vs attended, or a non-weighing XTi600."
	doc.meta_title = "Avery Berkel XTi Series Premium Scales Saudi Arabia | Printechs"
	doc.meta_description = "Avery Berkel XTi premium touchscreen weighing scales for Saudi Arabia. XTi420 dual-printer, XTi300 self-service and XTi600 terminals from Printechs."
	doc.set("benefits", [
		{"icon": "display", "title": "Larger operator canvas", "description": "10.1-inch colour touch (13.1-inch option on XTi420; 18.5-inch on XTi300).", "sort_order": 1},
		{"icon": "checkout", "title": "Weigh + label + POS", "description": "XTi420 keeps two media loaded so the counter does not stop to change rolls.", "sort_order": 2},
		{"icon": "loyalty", "title": "Self-service produce", "description": "XTi300 lets shoppers pick a photo, weigh and print their own label.", "sort_order": 3},
		{"icon": "print", "title": "XT print quality", "description": "150 mm/sec, 70 mm width, edge-to-edge, CodeChecker, linerless options.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Counter service", "image": media["xti_series_counter"], "image_alt": "XTi at a meat counter", "caption": "Raised customer display for price, weight and promotions.", "sort_order": 1},
		{"label": "Fresh food", "image": media["food"], "image_alt": "Fresh food", "caption": "Dual-printer XTi420 is the flagship attended workstation.", "sort_order": 2},
		{"label": "Produce", "image": media["bakery"], "image_alt": "Bakery and produce", "caption": "XTi300 self-service and XTi600 bakery terminals sit in this family.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "display", "title": "Operator", "description": "10.1-inch typical", "sort_order": 1},
		{"icon": "scan", "title": "Self-service", "description": "XTi300 18.5-inch", "sort_order": 2},
		{"icon": "print", "title": "Dual print", "description": "XTi420 two printers", "sort_order": 3},
		{"icon": "connectivity", "title": "USB", "description": "Five USB interfaces", "sort_order": 4},
	])
	set_specs(doc, specs_for(slug))
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{"section_type": "Industry Solution", "heading": "XTi technology on the counter", "body": "ValuMax, CodeChecker, 150 mm/sec edge-to-edge printing and MXBusiness sit under every XTi. This page is the 10.1-inch / 18.5-inch family — not 7-inch XTs and not tactile Xs.", "image": media["xti_series_counter"], "image_alt": "XTi counter", "sort_order": 1},
		{"section_type": "Industry Solution", "heading": "XTi with Modern POS in KSA", "body": _ksa("XTi") + " Dual-printer XTi420 is the natural partner when the same station must land a receipt on Modern POS / ERPNext.", "image": media["retail"], "image_alt": "Retail", "link_label": "See Modern POS", "link_href": "/software/modern-pos", "sort_order": 2},
	])
	doc.set("support_items", support_items("Screen size, printer count and self-service vs attended.", "10.1 / 13.1 / 18.5 display care and label SKUs.", "OneCare-style service and calibration in KSA.", "Self-service UI, dual-print and MXBusiness."))
	apply_brochures(doc, slug)
	doc.set("package_contents", [{"item_description": "Quoted XTi model", "sort_order": 1}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Why is XTi420 featured?", "answer": "It is the reduced-footprint dual-printer model: weigh, print a product label and issue a receipt/POS ticket without changing media.", "sort_order": 1},
		{"question": "Is XTi300 for staff?", "answer": "No. XTi300 is the self-service 18.5-inch model for shoppers in produce and similar departments.", "sort_order": 2},
		{"question": "XTi600 vs XTs600?", "answer": "Both are non-weighing terminals. XTi600 uses the larger 10.1-inch XTi operator canvas; XTs600 uses the 7-inch XTs canvas.", "sort_order": 3},
	])
	return save_product(doc, card)


def _finish(doc, media, card, slug, extras):
	doc.hero_image = card
	doc.card_image = card
	apply_brochures(doc, slug)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("support_items", extras["support"])
	doc.set("package_contents", extras["pack"])
	return save_product(doc, card)


def fill_model(media, cfg):
	slug = cfg["slug"]
	card = media[cfg["card_key"]]
	doc = get_or_create(slug, cfg["display"], cfg.get("item") or "", card, cfg["sub"])
	apply_identity(
		doc,
		slug=slug,
		display_name=cfg["display"],
		item=cfg.get("item") or "",
		subcategory=cfg["sub"],
		category_label=cfg["label"],
		featured=cfg.get("featured", 0),
	)
	doc.tagline = cfg["tagline"]
	doc.short_description = cfg["short"]
	doc.long_description = cfg["long"]
	doc.hero_image_alt = cfg["hero_alt"]
	doc.hero_trust_chips = cfg["chips"]
	doc.story_heading = cfg["story"]
	doc.visual_story_heading = cfg["visual"]
	doc.card_title = cfg["card_title"]
	doc.card_summary = cfg["card_summary"]
	doc.final_cta_heading = cfg["cta_h"]
	doc.final_cta_description = cfg["cta_d"]
	doc.meta_title = cfg["meta_title"]
	doc.meta_description = cfg["meta_desc"]
	doc.set("benefits", cfg["benefits"])
	doc.set("visual_story_items", cfg["story_items"])
	doc.set("icon_specifications", cfg["icons"])
	set_specs(doc, specs_for(slug))
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", cfg["sections"])
	doc.set("faq_items", cfg["faqs"])
	return _finish(doc, media, card, slug, cfg)


def models(media):
	r, food, bakery = media["retail"], media["food"], media["bakery"]
	return [
		{
			"slug": "avery-berkel-xs100",
			"display": "Avery Berkel Xs100",
			"item": "RET.SYS.AVR.2234",
			"sub": "Tactile Retail Scales",
			"label": "RETAIL WEIGHING & LABEL PRINTING SCALE",
			"card_key": "xs100",
			"tagline": "Compact monobloc tactile scale — weigh, select PLU and print in one unit",
			"short": (
				"Avery Berkel Xs100 is a compact professional retail weighing scale for food "
				"counters where space, accuracy and fast product keys matter. Monobloc design "
				"combines platform, tactile keyboard, operator/customer displays and a thermal "
				"label/receipt printer."
			),
			"long": (
				"<p>The Avery Berkel Xs100 is a compact monobloc weighing terminal: platform, "
				"tactile PLU keyboard, operator and customer displays and an integrated "
				"label/receipt printer in one counter unit. Avery Berkel positions Xs as the "
				"cost-effective tactile-key range — not a wall price checker and not a touchscreen XT.</p>"
				"<p>Operators who prefer physical keys get rapid PLU selection. The scale can "
				"run independently or on Ethernet / compatible Wi-Fi with other scales and "
				"back-office systems so product, price and transaction data stay central. "
				"CodeChecker helps watch print-head quality. Typical capacity is 15 kg AVR; "
				"25 kg versions exist as a different Item.</p>"
				"<p>This page is RET.SYS.AVR.2234 (Xs-100 15 kg). Do not treat RET.SYS.AVR.2604 "
				"(25 kg) as this configuration. Ideal for butcher shops, supermarkets, delis, "
				"cheese counters, bakeries and grocery service in Jeddah, Riyadh and Dammam.</p>"
				f"<p>{_ksa('Xs100')}</p>"
			),
			"hero_alt": "Avery Berkel Xs100 monobloc tactile retail scale",
			"chips": "Monobloc tactile Xs\n15 kg AVR (this Item)\nLabel / receipt printer\nEthernet · CodeChecker",
			"story": "Compact tactile weighing for tight counters",
			"visual": "Xs100",
			"card_title": "Xs100",
			"card_summary": "Compact monobloc tactile scale with integrated label/receipt printing. 15 kg AVR.",
			"cta_h": "Quote Avery Berkel Xs100",
			"cta_d": "Confirm 15 kg vs 25 kg, label stock and whether the counter should stay monobloc.",
			"meta_title": "Avery Berkel Xs100 Retail Weighing Scale Saudi Arabia | Printechs",
			"meta_desc": "Avery Berkel Xs100 retail weighing and label printing scale for supermarkets, butcheries, delis and food retailers in Saudi Arabia. Available from Printechs.",
			"benefits": [
				{"icon": "store", "title": "Monobloc, small footprint", "description": "Platform, keys, displays and printer in one practical counter unit.", "sort_order": 1},
				{"icon": "speed", "title": "Tactile PLU keys", "description": "Physical keys for operators who want rapid product selection without a touch UI.", "sort_order": 2},
				{"icon": "print", "title": "Labels and receipts", "description": "Integrated thermal printing with CodeChecker diagnostics.", "sort_order": 3},
				{"icon": "connectivity", "title": "Networked prices", "description": "Ethernet and compatible Wi-Fi for centrally managed PLUs.", "sort_order": 4},
			],
			"story_items": [
				{"label": "Xs100", "image": media["xs100"], "image_alt": "Xs100", "caption": "Monobloc tactile — not Xs200 (pole display) and not XTs100 (touch).", "sort_order": 1},
				{"label": "On the counter", "image": media["bakery"], "image_alt": "Bakery counter", "caption": "Built for butcher, deli, cheese, bakery and grocery service.", "sort_order": 2},
				{"label": "Fresh food", "image": food, "image_alt": "Fresh food", "caption": "Saudi supermarket and speciality counters.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Form", "description": "Compact monobloc", "sort_order": 1},
				{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
				{"icon": "print", "title": "Print", "description": "Label / receipt thermal", "sort_order": 3},
				{"icon": "connectivity", "title": "Network", "description": "Ethernet · Wi-Fi option", "sort_order": 4},
			],
			"specs": [
				("This configuration", [
					("Item on this page", "RET.SYS.AVR.2234 — Xs-100 15 kg"),
					("Also quote", "RET.SYS.AVR.2604 is Xs-100 25 kg × 5 g — different Item"),
					("Not this page", "Xs200 pole, Xs400 tower, Xs500 hanging, XTs100 touch"),
				]),
				("Weighing & print", [
					("Capacity", "15 kg AVR on this Item"),
					("Interface", "Tactile PLU and function keyboard"),
					("Displays", "Integrated operator and customer displays"),
					("Printer", "Thermal label and receipt; CodeChecker"),
				]),
				("Connectivity", [
					("Network", "Ethernet; compatible Wi-Fi"),
					("Management", "Central product, price and transaction data"),
				]),
			],
			"apps": [
				{"title": "Butcher shops", "description": "Fast keys and labels on a short counter.", "image": media["hub_scene"], "image_alt": "Butchery", "industry_link": "retail", "sort_order": 1},
				{"title": "Delicatessens", "description": "Cheese and prepared-food PLUs with barcode labels.", "image": food, "image_alt": "Deli", "industry_link": "retail", "sort_order": 2},
				{"title": "Bakeries", "description": "Service weighing where a monobloc fits the glass counter.", "image": bakery, "image_alt": "Bakery", "industry_link": "retail", "sort_order": 3},
			],
			"sections": [
				{"section_type": "Industry Solution", "heading": "Xs100 technology", "body": "Tactile keys, CodeChecker print diagnostics and Ethernet/Wi-Fi for MX-managed prices. This page is the monobloc Xs100 — not a hanging scale and not XTs touch.", "image": media["xs100"], "image_alt": "Xs100", "sort_order": 1},
				{"section_type": "Industry Solution", "heading": "Xs100 in Saudi Arabia", "body": "Avery Berkel Xs100 retail weighing scale for Jeddah, Riyadh and Dammam counters. Printechs loads PLUs, supplies labels and supports the network.", "image": r, "image_alt": "Retail", "sort_order": 2},
			],
			"faqs": [
				{"question": "Is Xs100 a price checker?", "answer": "No. It is a full retail weighing and labelling terminal the operator uses at the counter.", "sort_order": 1},
				{"question": "15 kg or 25 kg?", "answer": "This page is the 15 kg Item RET.SYS.AVR.2234. Ask for 2604 if you need 25 kg × 5 g.", "sort_order": 2},
				{"question": "When should I pick Xs200?", "answer": "When the customer needs a raised display. Xs100 keeps both displays in the monobloc.", "sort_order": 3},
			],
			"support": support_items("Monobloc placement and first PLU load.", "Xs label/receipt rolls.", "Keyboard and print-head parts.", "Tactile PLU and hygiene."),
			"pack": [{"item_description": "Xs100 15 kg as Item 2234", "sort_order": 1}, {"item_description": "Quick-start; media quoted separately", "sort_order": 2}],
		},
	]


def fill_remaining(media):
	"""Xs200–XTi600 — unique copy, unique hero cards, no hero video."""
	from printechs_digital.setup.fill_avery_berkel_xti_models import xti_models

	r, food, bakery = media["retail"], media["food"], media["bakery"]
	cfgs = [
		_xs200(media, r, food),
		_xs400(media, r, food),
		_xs500(media, r, food),
		_xts100(media, r, food),
		_xts200(media, r, food),
		_xts400(media, r, food),
		_xts420(media, r, food),
		_xts500(media, r, food),
		_xts600(media, r, bakery),
		_xts700(media, r, food),
		*xti_models(media, r, food, bakery),
	]
	for cfg in cfgs:
		fill_model(media, cfg)


def _base(slug, display, item, sub, label, card_key, featured=0):
	return {
		"slug": slug,
		"display": display,
		"item": item,
		"sub": sub,
		"label": label,
		"card_key": card_key,
		"featured": featured,
	}


def _xs200(m, r, food):
	d = _base("avery-berkel-xs200", "Avery Berkel Xs200", "RET.SYS.AVR.2235", "Tactile Retail Scales", "RETAIL WEIGHING SCALE", "xs200")
	d.update({
		"tagline": "Xs platform with a raised customer display for clearer service",
		"short": "Avery Berkel Xs200 pairs the Xs tactile weighing and printing platform with a raised customer-facing display so weight and price stay visible while keys stay at counter level.",
		"long": (
			"<p>Xs200 uses the same tactile keyboard and weighing characteristics as monobloc "
			"Xs100, then moves the customer display onto a column. Busy fresh-food departments "
			"get accurate weighing, PLU selection, price calculation and professional "
			"label/receipt printing from one device — with better customer visibility.</p>"
			"<p>Typical capacity is 15 kg AVR. Ethernet and compatible Wi-Fi support networked "
			"retail. CodeChecker watches the print head. This page is RET.SYS.AVR.2235 "
			"(Xs-200 15 kg). RET.SYS.AVR.2605 is the 25 kg Item — quote it separately.</p>"
			f"<p>{_ksa('Xs200')} Best for supermarkets, butcheries, delis and grocery service counters.</p>"
		),
		"hero_alt": "Avery Berkel Xs200 with raised customer display",
		"chips": "Raised customer display\nTactile Xs keyboard\n15 kg AVR this Item\nLabel / receipt printer",
		"story": "Customer-visible pricing, keys at the counter",
		"visual": "Xs200",
		"card_title": "Xs200",
		"card_summary": "Tactile Xs scale with raised customer display and integrated printing. 15 kg AVR.",
		"cta_h": "Quote Avery Berkel Xs200",
		"cta_d": "Confirm 15 kg vs 25 kg and how tall the customer display should sit on the counter.",
		"meta_title": "Avery Berkel Xs200 Retail Scale & Label Printer Saudi Arabia | Printechs",
		"meta_desc": "Avery Berkel Xs200 weighing and label printing scale with raised customer display for supermarkets, butcheries and fresh-food retailers in Saudi Arabia.",
		"benefits": [
			{"icon": "display", "title": "Raised customer display", "description": "Weight and price at eye level without moving the keyboard off the deck.", "sort_order": 1},
			{"icon": "store", "title": "Same Xs keys as Xs100", "description": "Tactile PLU workflow operators already know.", "sort_order": 2},
			{"icon": "print", "title": "Integrated printer", "description": "Label and receipt printing with CodeChecker.", "sort_order": 3},
			{"icon": "connectivity", "title": "Networked retail", "description": "Ethernet and compatible Wi-Fi for store-wide prices.", "sort_order": 4},
		],
		"story_items": [
			{"label": "Xs200", "image": m["xs200"], "image_alt": "Xs200", "caption": "Column customer display — not the Xs400 raised keyboard.", "sort_order": 1},
			{"label": "From the customer side", "image": m["xs200_scene"], "image_alt": "Raised display", "caption": "Clear transaction information during service.", "sort_order": 2},
			{"label": "Supermarket", "image": food, "image_alt": "Retail", "caption": "Service counters where visibility matters.", "sort_order": 3},
		],
		"icons": [
			{"icon": "display", "title": "Customer", "description": "Raised column display", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Label / receipt", "sort_order": 3},
			{"icon": "store", "title": "Keys", "description": "Tactile at counter level", "sort_order": 4},
		],
		"specs": [
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.2235 — Xs-200 15 kg"),
				("Also quote", "RET.SYS.AVR.2605 is Xs-200 25 kg — different Item"),
				("Not this page", "Xs100 monobloc, Xs400 tower keyboard, XTs200"),
			]),
			("Weighing & print", [
				("Capacity", "15 kg AVR on this Item"),
				("Display", "Raised customer-facing display"),
				("Printer", "Integrated thermal label/receipt; CodeChecker"),
			]),
		],
		"apps": [
			{"title": "Supermarkets", "description": "Customer-readable totals on a service island.", "image": food, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 1},
			{"title": "Butcheries", "description": "Keys stay low; the shopper sees the price.", "image": m["hub_scene"], "image_alt": "Butchery", "industry_link": "retail", "sort_order": 2},
			{"title": "Grocery service", "description": "Networked PLUs with a visible customer display.", "image": r, "image_alt": "Grocery", "industry_link": "retail", "sort_order": 3},
		],
		"sections": [
			{"section_type": "Industry Solution", "heading": "Xs200 technology", "body": "Raised customer display plus the Xs tactile keyboard, CodeChecker and Ethernet. This is not Xs400 (raised keyboard) and not XTs200 (touch).", "image": m["xs200"], "image_alt": "Xs200", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "Xs200 in KSA", "body": "Retail weighing scale with raised display for Jeddah, Riyadh and Dammam. Printechs supplies the scale, labels and network setup.", "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		"faqs": [
			{"question": "Xs200 vs Xs100?", "answer": "Same tactile platform. Xs200 adds a raised customer display; Xs100 keeps displays in the monobloc.", "sort_order": 1},
			{"question": "Xs200 vs Xs400?", "answer": "Xs400 raises the keyboard and both displays on a tower. Xs200 only raises the customer display.", "sort_order": 2},
			{"question": "Which Item is this?", "answer": "RET.SYS.AVR.2235, 15 kg. The 25 kg Xs200 is 2605.", "sort_order": 3},
		],
		"support": support_items("Column height and 15 vs 25 kg.", "Xs media.", "Display and printer parts.", "Customer-facing totals."),
		"pack": [{"item_description": "Xs200 15 kg as Item 2235", "sort_order": 1}],
	})
	return d


def _xs400(m, r, food):
	d = _base("avery-berkel-xs400", "Avery Berkel Xs400", "RET.SYS.AVR.2232", "Tactile Retail Scales", "RETAIL COUNTER WEIGHING SCALE", "xs400")
	d.update({
		"tagline": "Raised keyboard and displays — more counter space, eye-level service",
		"short": "Avery Berkel Xs400 is a two-piece tactile scale: keyboard and displays sit on a raised tower so the weighing platform stays clear and transaction information is closer to eye level.",
		"long": (
			"<p>Unlike Xs100 and Xs200, Xs400 places the keyboard and displays on a raised "
			"tower. Avery Berkel describes it as a two-piece design intended to maximise "
			"eye-level interaction while reducing equipment on the working surface.</p>"
			"<p>You still get the Xs tactile PLU keyboard, 15 kg AVR (and selected other "
			"capacities), integrated thermal label/receipt printing, Ethernet / optional "
			"wireless and retail management connectivity.</p>"
			"<p>This page is RET.SYS.AVR.2232 (Xs-400 15 kg). Premium butcheries, supermarket "
			"islands, deli and cheese counters in Saudi Arabia are the usual fit.</p>"
			f"<p>{_ksa('Xs400')}</p>"
		),
		"hero_alt": "Avery Berkel Xs400 tower keyboard retail scale",
		"chips": "Raised keyboard + displays\nReduced counter footprint\n15 kg AVR this Item\nTactile PLU · printing",
		"story": "A cleaner counter, conversation at eye level",
		"visual": "Xs400",
		"card_title": "Xs400",
		"card_summary": "Tower tactile scale: raised keyboard and displays, integrated printer, 15 kg AVR.",
		"cta_h": "Quote Avery Berkel Xs400",
		"cta_d": "Confirm tower height, 15 kg AVR and label formats for a premium counter.",
		"meta_title": "Avery Berkel Xs400 Counter Scale Saudi Arabia | Label Printing Scale",
		"meta_desc": "Avery Berkel Xs400 retail weighing scale with elevated operator and customer displays, integrated printing and a compact counter footprint.",
		"benefits": [
			{"icon": "device", "title": "Two-piece tower", "description": "Keyboard and displays leave the platform clear for cutting and packing.", "sort_order": 1},
			{"icon": "display", "title": "Eye-level service", "description": "Operator and customer see the transaction without hunching over a monobloc.", "sort_order": 2},
			{"icon": "print", "title": "Printer in the base", "description": "Thermal labels and receipts stay in the platform housing.", "sort_order": 3},
			{"icon": "store", "title": "Tactile Xs keys", "description": "Same PLU idea as Xs100, raised for a premium counter.", "sort_order": 4},
		],
		"story_items": [
			{"label": "Xs400", "image": m["xs400"], "image_alt": "Xs400", "caption": "Raised keyboard — not Xs200 (keys stay on the deck).", "sort_order": 1},
			{"label": "Service", "image": m["hub_scene"], "image_alt": "Counter service", "caption": "Designed for conversation over a clean platter area.", "sort_order": 2},
			{"label": "Deli", "image": food, "image_alt": "Deli", "caption": "High-volume fresh-food departments.", "sort_order": 3},
		],
		"icons": [
			{"icon": "device", "title": "Form", "description": "Raised two-piece", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Base thermal printer", "sort_order": 3},
			{"icon": "store", "title": "Keys", "description": "Tactile on the tower", "sort_order": 4},
		],
		"specs": [
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.2232 — Xs-400 15 kg"),
				("Not this page", "Xs100, Xs200, XTs400, XTi400"),
			]),
			("Design", [
				("Layout", "Raised operator keyboard; elevated operator and customer displays"),
				("Printer", "Integrated thermal label/receipt in the base"),
				("Network", "Ethernet; optional/compatible wireless"),
			]),
		],
		"apps": [
			{"title": "Premium butcheries", "description": "Clear workspace around the platter.", "image": m["hub_scene"], "image_alt": "Butchery", "industry_link": "retail", "sort_order": 1},
			{"title": "Cheese and deli", "description": "Eye-level totals on a tight island.", "image": food, "image_alt": "Deli", "industry_link": "retail", "sort_order": 2},
			{"title": "Supermarket service", "description": "Reduced footprint versus a deep monobloc.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 3},
		],
		"sections": [
			{"section_type": "Industry Solution", "heading": "Xs400 technology", "body": "Two-piece Xs with CodeChecker printing and networked prices. Not XTs400 (7-inch touch on a tower).", "image": m["xs400"], "image_alt": "Xs400", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "Xs400 in Saudi Arabia", "body": "Counter scale with elevated displays for KSA premium fresh-food departments. Printechs installs and labels the tower.", "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		"faqs": [
			{"question": "Why not Xs200?", "answer": "Xs200 only raises the customer display. Xs400 also raises the keyboard so the platter area stays clear.", "sort_order": 1},
			{"question": "Is this a touchscreen?", "answer": "No. Xs400 is tactile. XTs400 / XTi400 are the touchscreen towers.", "sort_order": 2},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.2232, Xs-400 15 kg.", "sort_order": 3},
		],
		"support": support_items("Tower vs monobloc layout.", "Xs media.", "Column and printer parts.", "Eye-level service."),
		"pack": [{"item_description": "Xs400 15 kg as Item 2232", "sort_order": 1}],
	})
	return d


def _xs500(m, r, food):
	d = _base("avery-berkel-xs500", "Avery Berkel Xs500", "RET.SYS.AVR.2549", "Hanging Retail Scales", "HANGING RETAIL WEIGHING SCALE", "xs500")
	d.update({
		"tagline": "Hanging tactile scale for fish, seafood and wet food counters",
		"short": "Avery Berkel Xs500 is the hanging model in the Xs family: a suspended pan keeps wet product off the counter while vendor/customer displays and label/receipt printing stay in one retail scale.",
		"long": (
			"<p>Xs500 is specifically for applications where the weighing platform should "
			"not sit on the counter — fishmongers, seafood departments and wet retail. "
			"Avery Berkel describes it as a hanging scale designed for wet areas.</p>"
			"<p>You still get tactile product keys, vendor and customer displays, 15 kg AVR "
			"(5 g on this Item), integrated thermal printing, Ethernet and networked "
			"product/price management.</p>"
			"<p>This page is RET.SYS.AVR.2549 (XS500 15 kg × 5 g). For a touchscreen hanging "
			"scale specify XTs500 instead.</p>"
			f"<p>{_ksa('Xs500')}</p>"
		),
		"hero_alt": "Avery Berkel Xs500 hanging retail scale with stainless pan",
		"chips": "Suspended weighing pan\nWet-area Xs\n15 kg × 5 g this Item\nTactile keys · printing",
		"story": "Keep fish off the counter, keep Xs keys",
		"visual": "Xs500",
		"card_title": "Xs500",
		"card_summary": "Hanging tactile retail scale for seafood and wet counters. 15 kg × 5 g.",
		"cta_h": "Quote Avery Berkel Xs500",
		"cta_d": "Confirm hanging hardware, pan type and whether the counter should stay tactile or move to XTs500.",
		"meta_title": "Avery Berkel Xs500 Hanging Scale Saudi Arabia | Fish & Seafood Scale",
		"meta_desc": "Avery Berkel Xs500 hanging retail scale for fish, seafood and wet food counters with integrated label and receipt printing. Available from Printechs KSA.",
		"benefits": [
			{"icon": "inventory", "title": "Hanging pan", "description": "Wet product stays off the worktop; easier handling for fish.", "sort_order": 1},
			{"icon": "durability", "title": "Wet-area intent", "description": "Specified as a hanging scale for wet retail — not a dry monobloc.", "sort_order": 2},
			{"icon": "print", "title": "Full retail functions", "description": "Displays, tactile keys and label/receipt printing in the hanging head.", "sort_order": 3},
			{"icon": "connectivity", "title": "Networked PLUs", "description": "Same store prices as bench Xs scales.", "sort_order": 4},
		],
		"story_items": [
			{"label": "Xs500", "image": m["xs500"], "image_alt": "Xs500", "caption": "Tactile hanging — not XTs500 (colour touch in the head).", "sort_order": 1},
			{"label": "Seafood", "image": food, "image_alt": "Seafood", "caption": "Fish markets and supermarket wet sections.", "sort_order": 2},
			{"label": "Retail", "image": r, "image_alt": "Retail", "caption": "Specialist fresh-food shops in KSA.", "sort_order": 3},
		],
		"icons": [
			{"icon": "inventory", "title": "Pan", "description": "Suspended stainless", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg × 5 g this Item", "sort_order": 2},
			{"icon": "store", "title": "Keys", "description": "Tactile in the head", "sort_order": 3},
			{"icon": "print", "title": "Print", "description": "Label / receipt", "sort_order": 4},
		],
		"specs": [
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.2549 — XS500 15 kg × 5 g"),
				("Not this page", "Bench Xs100, XTs500 touch hanging, XM-500 legacy"),
			]),
			("Weighing", [
				("Design", "Hanging / suspended pan for wet areas"),
				("Capacity", "15 kg × 5 g on this Item"),
				("Printer", "Integrated thermal label/receipt"),
			]),
		],
		"apps": [
			{"title": "Fish markets", "description": "Hang the pan over ice or a well.", "image": food, "image_alt": "Fish", "industry_link": "retail", "sort_order": 1},
			{"title": "Supermarket seafood", "description": "Same Xs labels as the meat counter, different form.", "image": r, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 2},
			{"title": "Wet food sections", "description": "Where a bench platter would stay wet all day.", "image": m["xs500"], "image_alt": "Xs500", "industry_link": "retail", "sort_order": 3},
		],
		"sections": [
			{"section_type": "Industry Solution", "heading": "Xs500 technology", "body": "Hanging Xs with tactile keys, CodeChecker printing and Ethernet. Primary keyword: Avery Berkel hanging scale Saudi Arabia.", "image": m["xs500"], "image_alt": "Xs500", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "Hanging scales in KSA", "body": "Printechs specifies Xs500 vs XTs500 for seafood halls in Jeddah, Riyadh and Dammam.", "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		"faqs": [
			{"question": "Xs500 or XTs500?", "answer": "Xs500 is tactile. XTs500 adds the 7-inch colour touch hanging head. Same wet-area idea.", "sort_order": 1},
			{"question": "Can I use Xs100 for fish?", "answer": "You can, but the hanging pan is the right tool for wet product. This page is the hanging Item.", "sort_order": 2},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.2549, 15 kg × 5 g.", "sort_order": 3},
		],
		"support": support_items("Hang point, pan and drain.", "Wet-area labels.", "Head and printer service.", "Seafood PLUs."),
		"pack": [{"item_description": "Xs500 15 kg × 5 g as Item 2549", "sort_order": 1}],
	})
	return d


def _xt_model(slug, display, item, sub, label, card_key, featured, **kw):
	d = _base(slug, display, item, sub, label, card_key, featured)
	d.update(kw)
	return d


def _xts100(m, r, food):
	return _xt_model(
		"avery-berkel-xts100", "Avery Berkel XTs100", "RET.SYS.AVR.4203",
		"Touchscreen Retail Scales", "TOUCHSCREEN RETAIL SCALE", "xts100", 0,
		tagline="Compact 7-inch monobloc — colour touch where vertical space is limited",
		short="Avery Berkel XTs100 is a compact monobloc touchscreen retail scale: weighing, product selection, customer information and high-speed label/receipt printing in one counter unit.",
		long=(
			"<p>XTs100 integrates a 7-inch operator touchscreen, 7-inch customer display, "
			"15 kg AVR weighing (this Item) and a cassette label/receipt printer. Colour "
			"touch shows products and functions; tactile keys keep busy counters fast. "
			"Multimedia and promotions can run on the customer display. Linux, ValuMax, "
			"Ethernet, compatible Wi-Fi, USB and CodeChecker / linerless compatibility "
			"are the XT foundation.</p>"
			"<p>This page is RET.SYS.AVR.4203 (XTs100 15 kg AVR, 7/7). Eco III Item 4600 "
			"is a different stocked configuration — quote it only when that is the unit "
			"on the floor. Not Xs100 (tactile-only) and not XTi100 (10.1-inch).</p>"
			f"<p>{_ksa('XTs100')}</p>"
		),
		hero_alt="Avery Berkel XTs100 7-inch monobloc touchscreen scale",
		chips="7-inch operator + 7-inch customer\n15 kg AVR this Item\nCassette printer · ValuMax\nLinux · Ethernet / Wi-Fi",
		story="Colour touch in a low-height monobloc",
		visual="XTs100",
		card_title="XTs100",
		card_summary="Compact 7-inch monobloc touchscreen scale with cassette printing. 15 kg AVR.",
		cta_h="Quote Avery Berkel XTs100",
		cta_d="Confirm 7/7 displays and whether the stocked unit is standard 4203 or Eco III 4600.",
		meta_title="Avery Berkel XTs100 Touchscreen Retail Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTs100 compact touchscreen retail weighing and label printing scale for butcheries, supermarkets, delis and fresh-food retailers in KSA.",
		benefits=[
			{"icon": "display", "title": "7-inch colour + keys", "description": "Pictures and promotions on-screen; tactile keys for speed.", "sort_order": 1},
			{"icon": "device", "title": "Low vertical space", "description": "Monobloc when a tower will not fit the glass counter.", "sort_order": 2},
			{"icon": "print", "title": "XT cassette printer", "description": "High-speed labels/receipts, CodeChecker, linerless options.", "sort_order": 3},
			{"icon": "speed", "title": "ValuMax", "description": "Automatic level correction on this weighing model.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTs100", "image": m["xts100"], "image_alt": "XTs100", "caption": "7-inch monobloc — not XTi100 (larger screen) and not Xs100.", "sort_order": 1},
			{"label": "Fresh food", "image": food, "image_alt": "Fresh food", "caption": "Butcheries, delis and supermarket service.", "sort_order": 2},
			{"label": "Retail", "image": r, "image_alt": "Retail", "caption": "Networked to MXBusiness.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Screens", "description": "7 / 7 inch", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Cassette thermal", "sort_order": 3},
			{"icon": "connectivity", "title": "I/O", "description": "Ethernet · Wi-Fi · USB", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4203 — XTs100 15 kg AVR, 7/7"),
				("Also quote", "RET.SYS.AVR.4600 Eco III — different Item"),
				("Not this page", "Xs100, XTi100, XTs200"),
			]),
			("XT platform", [
				("Displays", "7-inch operator touch; 7-inch customer"),
				("Print / OS", "Cassette thermal; Linux; ValuMax"),
			]),
		],
		apps=[
			{"title": "Compact butcher counters", "description": "Touch PLUs without a tower.", "image": m["hub_scene"], "image_alt": "Butchery", "industry_link": "retail", "sort_order": 1},
			{"title": "Supermarkets", "description": "Colour products on a short run.", "image": food, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 2},
			{"title": "Delis", "description": "Promotions on the 7-inch customer display.", "image": r, "image_alt": "Deli", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs100 technology", "body": "7-inch XT monobloc with ValuMax, 150 mm/sec-class cassette printing and MXBusiness. Not the 10.1-inch XTi100.", "image": m["xts100"], "image_alt": "XTs100", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTs100 in KSA", "body": _ksa("XTs100"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "XTs100 or XTi100?", "answer": "XTs100 is 7/7. XTi100 is 10.1-inch operator with a 7-inch customer display.", "sort_order": 1},
			{"question": "Standard or Eco III?", "answer": "This page is Item 4203. Eco III is 4600 — same family, different stock line.", "sort_order": 2},
			{"question": "Is this Xs100?", "answer": "No. Xs100 is tactile-only. XTs100 is the colour-touch monobloc.", "sort_order": 3},
		],
		support=support_items("7/7 monobloc vs Eco III.", "Cassette labels.", "ValuMax and print-head.", "Touch + key training."),
		pack=[{"item_description": "XTs100 15 kg AVR 7/7 as Item 4203", "sort_order": 1}],
	)


def _xts200(m, r, food):
	return _xt_model(
		"avery-berkel-xts200", "Avery Berkel XTs200", "RET.SYS.AVR.4193",
		"Touchscreen Retail Scales", "TOUCHSCREEN RETAIL WEIGHING SCALE", "xts200", 0,
		tagline="7-inch operator touch with a raised colour customer display",
		short="Avery Berkel XTs200 combines a compact touchscreen operator station with a raised 7-inch customer display so weight, pricing and promotions stay visible during service.",
		long=(
			"<p>XTs200 keeps the 7-inch colour operator touchscreen at the deck and lifts "
			"a 7-inch customer display. The customer screen can show advertising and "
			"special offers while people wait — useful for complementary products at "
			"the counter.</p>"
			"<p>15 kg AVR, cassette printer, Ethernet, compatible Wi-Fi, CodeChecker and "
			"MXBusiness compatibility are standard XT. This page is RET.SYS.AVR.4193 "
			"(XTs200 15 kg AVR, 7/7). Eco III 4601 is a different Item.</p>"
			f"<p>{_ksa('XTs200')}</p>"
		),
		hero_alt="Avery Berkel XTs200 with raised customer display",
		chips="7-inch operator touch\nRaised 7-inch customer display\n15 kg AVR this Item\nCassette printer · MXBusiness",
		story="Promotions at eye level, touch at the keys",
		visual="XTs200",
		card_title="XTs200",
		card_summary="7-inch touchscale with raised customer display and fast label printing. 15 kg AVR.",
		cta_h="Quote Avery Berkel XTs200",
		cta_d="Confirm 7/7 raised customer display and standard 4193 vs Eco III 4601.",
		meta_title="Avery Berkel XTs200 Retail Weighing Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTs200 touchscreen weighing scale with raised customer display, fast label printing and retail connectivity for supermarkets and food counters.",
		benefits=[
			{"icon": "display", "title": "Raised customer colour", "description": "Weight, price and adverts while the operator stays on the 7-inch touch.", "sort_order": 1},
			{"icon": "loyalty", "title": "Counter promotions", "description": "Show offers while the shopper waits — not a blank pole.", "sort_order": 2},
			{"icon": "print", "title": "Cassette printer", "description": "XT label/receipt speed with CodeChecker.", "sort_order": 3},
			{"icon": "connectivity", "title": "MXBusiness", "description": "Central products and prices across the store.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTs200", "image": m["xts200"], "image_alt": "XTs200", "caption": "Raised customer display — operator stays on the deck.", "sort_order": 1},
			{"label": "Advertising", "image": food, "image_alt": "Customer-facing retail", "caption": "Full-colour offers during service on the raised customer display.", "sort_order": 2},
			{"label": "Supermarket", "image": food, "image_alt": "Retail", "caption": "Saudi fresh-food counters.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Customer", "description": "Raised 7-inch colour", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Cassette thermal", "sort_order": 3},
			{"icon": "cloud", "title": "Software", "description": "MXBusiness", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4193 — XTs200 15 kg AVR, 7/7"),
				("Also quote", "RET.SYS.AVR.4601 Eco III — different Item"),
				("Not this page", "XTs100, XTs400, XTi200"),
			]),
			("Displays & print", [
				("Operator", "7-inch colour touch + tactile keys"),
				("Customer", "Raised 7-inch colour, advertising capable"),
			]),
		],
		apps=[
			{"title": "Supermarket islands", "description": "Shoppers see the total and the offer.", "image": food, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 1},
			{"title": "Service counters", "description": "Promotions without a second screen SKU.", "image": r, "image_alt": "Counter", "industry_link": "retail", "sort_order": 2},
			{"title": "Delis", "description": "Colour PLUs plus a raised customer face.", "image": m["xts200"], "image_alt": "XTs200", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs200 technology", "body": "Raised 7-inch customer advertising display on the affordable XT platform. Not XTi200 (10.1-inch operator).", "image": m["xts200"], "image_alt": "XTs200", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTs200 in KSA", "body": _ksa("XTs200"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "XTs200 or XTi200?", "answer": "Same raised-customer idea. XTs200 is 7-inch operator; XTi200 is 10.1-inch operator.", "sort_order": 1},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.4193. Eco III is 4601.", "sort_order": 2},
			{"question": "Can it show adverts?", "answer": "Yes. The raised full-colour customer display is intended for promotions as well as totals.", "sort_order": 3},
		],
		support=support_items("Column and 4193 vs 4601.", "Cassette media.", "Customer display glass.", "Promotion playlist."),
		pack=[{"item_description": "XTs200 15 kg AVR 7/7 as Item 4193", "sort_order": 1}],
	)


def _xts400(m, r, food):
	return _xt_model(
		"avery-berkel-xts400", "Avery Berkel XTs400", "RET.SYS.AVR.4194",
		"Touchscreen Retail Scales", "RETAIL WEIGHING & LABELLING SCALE", "xts400", 0,
		tagline="Raised 7-inch operator and customer displays — more working space",
		short="Avery Berkel XTs400 relocates operator and customer displays above the platter so staff keep eye contact and the counter stays clearer. Customer display options include 7-inch and 10.1-inch.",
		long=(
			"<p>XTs400 is the reduced-footprint raised-display XTs. The 7-inch operator "
			"touchscreen sits on the tower; the customer display is 7-inch on this Item "
			"(4194, 7/7) with 10.1-inch customer options in the family. 15 kg AVR, "
			"selected 30 kg configurations, ValuMax, high-speed thermal printing, "
			"Ethernet/Wi-Fi and multimedia are the XT package.</p>"
			"<p>Eco III Item 4602 is a different stock line. Dual printers are XTs420, "
			"not this page. Premium food counters in Saudi Arabia that want XTs touch "
			"and a clean platter use XTs400.</p>"
			f"<p>{_ksa('XTs400')}</p>"
		),
		hero_alt="Avery Berkel XTs400 raised touchscreen retail scale",
		chips="Raised 7-inch operator\n7-inch customer this Item\n15 kg AVR · ValuMax\nReduced footprint",
		story="Touchscreen tower, platter left clear",
		visual="XTs400",
		card_title="XTs400",
		card_summary="Raised 7-inch XTs tower scale with cassette printing. 15 kg AVR, 7/7.",
		cta_h="Quote Avery Berkel XTs400",
		cta_d="Confirm 7/7 vs 7/10.1 customer display and 4194 vs Eco III 4602.",
		meta_title="Avery Berkel XTs400 Retail Touchscreen Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTs400 touchscreen retail scale with elevated operator and customer displays, compact footprint and professional label printing.",
		benefits=[
			{"icon": "device", "title": "Raised assembly", "description": "More working space around the stainless platter.", "sort_order": 1},
			{"icon": "display", "title": "7-inch operator touch", "description": "Colour PLUs at eye level with tactile keys beside the screen.", "sort_order": 2},
			{"icon": "print", "title": "Base cassette printer", "description": "XT speed, ValuMax on the weigh platform.", "sort_order": 3},
			{"icon": "loyalty", "title": "Multimedia customer face", "description": "7-inch on this Item; 10.1-inch customer is a family option.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTs400", "image": m["xts400"], "image_alt": "XTs400", "caption": "Raised 7-inch — one printer. Dual printers are XTs420.", "sort_order": 1},
			{"label": "Premium counter", "image": m["xti_series_counter"], "image_alt": "Counter", "caption": "Eye contact over a clear platter.", "sort_order": 2},
			{"label": "Retail", "image": food, "image_alt": "Retail", "caption": "Supermarket and speciality food.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "Operator", "description": "Raised 7-inch touch", "sort_order": 1},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Single cassette", "sort_order": 3},
			{"icon": "device", "title": "Footprint", "description": "Reduced tower base", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4194 — XTs400 15 kg AVR, 7/7"),
				("Also quote", "7/10.1 customer; Eco III 4602; 30 kg family options"),
				("Not this page", "XTs420 dual printer, XTi400, Xs400"),
			]),
			("Displays", [
				("Operator", "7-inch colour touch, raised"),
				("Customer", "7-inch on this Item; 10.1-inch available in family"),
			]),
		],
		apps=[
			{"title": "Premium food counters", "description": "Presentation and a clear work area.", "image": m["xti_series_counter"], "image_alt": "Counter", "industry_link": "retail", "sort_order": 1},
			{"title": "Supermarkets", "description": "Tower XTs without a second printer.", "image": food, "image_alt": "Supermarket", "industry_link": "retail", "sort_order": 2},
			{"title": "Cheese / deli", "description": "Eye-level colour PLUs.", "image": r, "image_alt": "Deli", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs400 technology", "body": "Raised XTs with ValuMax and a single cassette printer. Need two printers? See XTs420.", "image": m["xts400"], "image_alt": "XTs400", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTs400 in KSA", "body": _ksa("XTs400"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "XTs400 or XTs420?", "answer": "XTs400 has one cassette printer. XTs420 adds a second clamshell printer in the head.", "sort_order": 1},
			{"question": "7/7 or 10.1 customer?", "answer": "This Item is 7/7. Ask if you need a 10.1-inch customer display.", "sort_order": 2},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.4194. Eco III is 4602.", "sort_order": 3},
		],
		support=support_items("7/7 vs 7/10.1.", "Cassette media.", "Tower glass.", "Raised-touch operation."),
		pack=[{"item_description": "XTs400 15 kg AVR 7/7 as Item 4194", "sort_order": 1}],
	)


def _xts420(m, r, food):
	return _xt_model(
		"avery-berkel-xts420", "Avery Berkel XTs420", "",
		"Touchscreen Retail Scales", "DUAL PRINTER RETAIL SCALE", "xts420", 0,
		tagline="Raised XTs with two printers — labels and receipts without changing media",
		short="Avery Berkel XTs420 combines the raised-display XTs architecture with a cassette printer in the base and a second clamshell printer in the upper assembly for busy supermarket and fresh-food counters.",
		long=(
			"<p>XTs420 is for counters that need two print jobs without swapping rolls. "
			"A common setup prints product labels from one printer and customer receipts "
			"from the other — weigh + label + ticket on the affordable 7-inch XT platform.</p>"
			"<p>7-inch touchscreen, raised operator and customer displays, 15 kg AVR, "
			"reduced footprint, high-speed printing, Ethernet/Wi-Fi, customer advertising, "
			"CodeChecker and central scale management. No XTs420 Item is listed yet — "
			"quote the dual-printer tower separately from XTs400 Item 4194.</p>"
			f"<p>{_ksa('XTs420')}</p>"
		),
		hero_alt="Avery Berkel XTs420 dual-printer raised touchscreen scale",
		chips="Dual label/receipt printers\nRaised 7-inch touch\n15 kg AVR\nReduced footprint",
		story="Two printers, one 7-inch workstation",
		visual="XTs420",
		card_title="XTs420",
		card_summary="Raised XTs with dual printers for label + receipt without changing media.",
		cta_h="Quote Avery Berkel XTs420",
		cta_d="Confirm label vs receipt media in each printer. No XTs420 Item yet — we quote the dual-printer tower.",
		meta_title="Avery Berkel XTs420 Dual Printer Retail Scale Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTs420 weighing scale with touchscreen, customer display and dual label/receipt printers for busy supermarket and fresh-food counters.",
		benefits=[
			{"icon": "print", "title": "Two printers", "description": "Cassette in the base, clamshell in the head — two label sizes or label + receipt.", "sort_order": 1},
			{"icon": "checkout", "title": "Weigh + ticket", "description": "Combined weighing and POS-style receipts without stopping the queue.", "sort_order": 2},
			{"icon": "display", "title": "Raised 7-inch", "description": "Same eye-level idea as XTs400, with more print capacity.", "sort_order": 3},
			{"icon": "connectivity", "title": "Networked XT", "description": "Ethernet/Wi-Fi and central management.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTs420", "image": m["xts420"], "image_alt": "XTs420", "caption": "Dual-printer tower. XTi420 is the 10.1-inch premium twin.", "sort_order": 1},
			{"label": "Retail counter", "image": r, "image_alt": "Retail counter", "caption": "Raised dual-print XTs for supermarket throughput.", "sort_order": 2},
			{"label": "Fresh food", "image": food, "image_alt": "Retail", "caption": "Supermarket fresh-food throughput.", "sort_order": 3},
		],
		icons=[
			{"icon": "print", "title": "Printers", "description": "Cassette + clamshell", "sort_order": 1},
			{"icon": "display", "title": "Operator", "description": "Raised 7-inch touch", "sort_order": 2},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR", "sort_order": 3},
			{"icon": "device", "title": "Footprint", "description": "Reduced tower", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "No XTs420 Item yet — quote dual-printer XTs420"),
				("Not this page", "XTs400 single printer (4194), XTi420 premium dual"),
			]),
			("Hardware", [
				("Printers", "Base cassette + upper clamshell label/receipt"),
				("Displays", "Raised 7-inch operator; customer display"),
				("Capacity", "15 kg AVR"),
			]),
		],
		apps=[
			{"title": "Combined weigh / POS", "description": "Label the pack and print the ticket.", "image": food, "image_alt": "POS", "industry_link": "retail", "sort_order": 1},
			{"title": "High-volume counters", "description": "No media change mid-rush.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 2},
			{"title": "Fresh food", "description": "Two label sizes permanently loaded.", "image": m["xts420"], "image_alt": "XTs420", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs420 technology", "body": "Dual XT printers on the 7-inch raised platform. For the 10.1-inch dual-printer flagship see XTi420.", "image": m["xts420"], "image_alt": "XTs420", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTs420 in KSA", "body": _ksa("XTs420") + " Pair receipts with Modern POS when the ticket must post in ERPNext.", "image": r, "image_alt": "Retail", "link_label": "See Modern POS", "link_href": "/software/modern-pos", "sort_order": 2},
		],
		faqs=[
			{"question": "XTs420 or XTi420?", "answer": "Both are dual-printer towers. XTs420 is 7-inch operator; XTi420 is 10.1- or 13.1-inch operator with a 10.1-inch customer display.", "sort_order": 1},
			{"question": "Is there an Item code?", "answer": "Not yet. Do not use XTs400 4194 as this page — that Item is a single printer.", "sort_order": 2},
			{"question": "Label + receipt?", "answer": "Yes. That is the usual dual-media story. Confirm both roll widths on the quote.", "sort_order": 3},
		],
		support=support_items("Two media types and tower layout.", "Cassette + clamshell stock.", "Two print heads.", "Label vs receipt workflow."),
		pack=[{"item_description": "XTs420 dual-printer tower as quoted", "sort_order": 1}],
	)


def _xts500(m, r, food):
	return _xt_model(
		"avery-berkel-xts500", "Avery Berkel XTs500", "RET.SYS.AVR.4556",
		"Hanging Retail Scales", "TOUCHSCREEN HANGING SCALE", "xts500", 1,
		tagline="7-inch hanging touchscale for fish and seafood — 15 kg AVR",
		short="Avery Berkel XTs500 combines XT touchscreen technology with a hanging pan for fish, seafood and wet-area retail. 15 kg AVR, ValuMax, cassette printing and a 7-inch customer display.",
		long=(
			"<p>XTs500 keeps wet product on a suspended pan and the 7-inch operator "
			"touchscreen in an elevated head — more comfortable and better protected than "
			"a bench scale over ice. 7-inch customer display, cassette printer, Ethernet/Wi-Fi, "
			"high-speed printing, multimedia and CodeChecker complete the XT hanging story.</p>"
			"<p>This page is RET.SYS.AVR.4556 (XTs500 15 kg AVR, 7/7). Featured for Saudi "
			"seafood because hanging + colour touch is a clear niche versus tactile Xs500.</p>"
			f"<p>{_ksa('XTs500')}</p>"
		),
		hero_alt="Avery Berkel XTs500 hanging touchscreen seafood scale",
		chips="Hanging 7-inch touch\n15 kg AVR this Item\nValuMax · cassette printer\nSeafood / wet area",
		story="Colour touch over a hanging seafood pan",
		visual="XTs500",
		card_title="XTs500",
		card_summary="Hanging 7-inch touchscreen scale for seafood and wet counters. 15 kg AVR.",
		cta_h="Quote Avery Berkel XTs500",
		cta_d="Confirm hang point, pan and 7/7 seafood PLUs for Item 4556.",
		meta_title="Avery Berkel XTs500 Hanging Scale Saudi Arabia | Seafood Retail Scale",
		meta_desc="Avery Berkel XTs500 touchscreen hanging scale for fish and seafood counters with 15kg AVR weighing and integrated label/receipt printing.",
		benefits=[
			{"icon": "inventory", "title": "Hanging pan", "description": "Fish stays off the equipment body.", "sort_order": 1},
			{"icon": "display", "title": "7-inch colour head", "description": "Photos and allergens on a wet-area scale.", "sort_order": 2},
			{"icon": "inventory", "title": "Hanging seafood head", "description": "Suspended pan and elevated 7-inch touch. ValuMax is not specified on XTs500.", "sort_order": 3},
			{"icon": "print", "title": "Cassette printer", "description": "Labels customers can scan at checkout.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTs500", "image": m["xts500"], "image_alt": "XTs500", "caption": "Touch hanging head — not tactile Xs500.", "sort_order": 1},
			{"label": "Angle", "image": m["xts500_angle"], "image_alt": "XTs500 angle", "caption": "Suspended pan under the XT head.", "sort_order": 2},
			{"label": "Seafood", "image": food, "image_alt": "Seafood", "caption": "Fish counters in KSA supermarkets.", "sort_order": 3},
		],
		icons=[
			{"icon": "inventory", "title": "Pan", "description": "Suspended", "sort_order": 1},
			{"icon": "display", "title": "Screens", "description": "7 / 7 inch", "sort_order": 2},
			{"icon": "inventory", "title": "Capacity", "description": "15 kg AVR this Item", "sort_order": 3},
			{"icon": "print", "title": "Print", "description": "Cassette thermal", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "RET.SYS.AVR.4556 — XTs500 15 kg AVR, 7/7"),
				("Not this page", "Xs500 tactile hanging, bench XTs100"),
			]),
			("Hardware", [
				("Design", "Hanging weighing; elevated operator interface"),
				("Displays", "7-inch touch + 7-inch customer"),
				("ValuMax / print", "Yes / cassette thermal"),
			]),
		],
		apps=[
			{"title": "Seafood counters", "description": "The featured hanging touchscale.", "image": food, "image_alt": "Seafood", "industry_link": "retail", "sort_order": 1},
			{"title": "Wet supermarket sections", "description": "Protect the electronics above the well.", "image": m["xts500"], "image_alt": "XTs500", "industry_link": "retail", "sort_order": 2},
			{"title": "Specialist fish shops", "description": "Colour PLUs for mixed catch.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs500 technology", "body": "Hanging XT with ValuMax, CodeChecker and 7-inch colour. Featured seafood scale for Printechs.", "image": m["xts500"], "image_alt": "XTs500", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "Seafood weighing in KSA", "body": _ksa("XTs500"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "XTs500 or Xs500?", "answer": "XTs500 is colour touch. Xs500 is tactile. Both hang. This featured page is the touch model.", "sort_order": 1},
			{"question": "Which Item?", "answer": "RET.SYS.AVR.4556, 15 kg AVR, 7/7.", "sort_order": 2},
			{"question": "Self-service?", "answer": "No. XTi300 is self-service produce. XTs500 is staffed seafood.", "sort_order": 3},
		],
		support=support_items("Hang kit and 4556.", "Wet-area cassette labels.", "Head sealing and printer.", "Seafood PLUs and photos."),
		pack=[{"item_description": "XTs500 15 kg AVR 7/7 as Item 4556", "sort_order": 1}],
	)


def _xts600(m, r, bakery):
	return _xt_model(
		"avery-berkel-xts600", "Avery Berkel XTs600", "",
		"Label Printers & Terminals", "LABEL PRINTER & EPOS TERMINAL", "xts600", 0,
		tagline="Non-weighing 7-inch terminal — bakery, pre-pack and EPOS printing",
		short="Avery Berkel XTs600 is a non-weighing retail terminal: standalone label printing, bakery/pre-pack or EPOS, with optional pairing to an external platform scale.",
		long=(
			"<p>Unlike weighing XTs models, XTs600 has no platter. Use it when weight is "
			"predetermined, comes from another device, or is not required. 7-inch "
			"touchscreen, cassette thermal printer, Ethernet/Wi-Fi, USB and central "
			"product management on the XT Linux platform.</p>"
			"<p>No XTs600 Item is listed yet. Do not treat XTi600 Item 4606 as this page "
			"— that terminal uses the 10.1-inch XTi canvas.</p>"
			f"<p>{_ksa('XTs600')}</p>"
		),
		hero_alt="Avery Berkel XTs600 non-weighing touchscreen label terminal",
		chips="Non-weighing terminal\n7-inch touch\nCassette label/receipt\nEPOS · external platform",
		story="Printing and EPOS without a weigh platter",
		visual="XTs600",
		card_title="XTs600",
		card_summary="Non-weighing 7-inch XT terminal for labels, bakery pre-pack and EPOS.",
		cta_h="Quote Avery Berkel XTs600",
		cta_d="Confirm standalone labels vs EPOS vs an external platform. No XTs600 Item yet.",
		meta_title="Avery Berkel XTs600 Label Printer & EPOS Terminal Saudi Arabia",
		meta_desc="Avery Berkel XTs600 non-weighing touchscreen label printer and EPOS terminal for bakeries, pre-pack operations and food retailers in Saudi Arabia.",
		benefits=[
			{"icon": "print", "title": "Not a scale", "description": "Dedicated label/EPOS terminal — say so on the quote.", "sort_order": 1},
			{"icon": "display", "title": "7-inch XT touch", "description": "Same affordable canvas as XTs100, without the platter.", "sort_order": 2},
			{"icon": "integration", "title": "External platform", "description": "Pair a floor or bench scale when weight is still needed.", "sort_order": 3},
			{"icon": "store", "title": "Bakery / pre-pack", "description": "Fixed-price or pre-weighed items, still on MXBusiness.", "sort_order": 4},
		],
		story_items=[
			{"label": "XTs600", "image": m["xts600"], "image_alt": "XTs600", "caption": "No platter. XTi600 is the larger-screen twin.", "sort_order": 1},
			{"label": "Bakery", "image": bakery, "image_alt": "Bakery", "caption": "Pre-pack and counter labels.", "sort_order": 2},
			{"label": "Retail", "image": r, "image_alt": "Retail", "caption": "EPOS workstation option.", "sort_order": 3},
		],
		icons=[
			{"icon": "print", "title": "Role", "description": "Non-weighing terminal", "sort_order": 1},
			{"icon": "display", "title": "Screen", "description": "7-inch touch", "sort_order": 2},
			{"icon": "print", "title": "Print", "description": "Cassette thermal", "sort_order": 3},
			{"icon": "connectivity", "title": "I/O", "description": "Ethernet · Wi-Fi · USB", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "No XTs600 Item yet — quote the 7-inch non-weighing terminal"),
				("Not this page", "XTi600 (4606), XTs100 weighing monobloc, XTs700 printer"),
			]),
			("Functions", [
				("Modes", "Standalone labels, bakery/pre-pack, EPOS"),
				("Weighing", "None on-board; optional external platform"),
			]),
		],
		apps=[
			{"title": "Bakeries", "description": "Fixed-price packs and counter labels.", "image": bakery, "image_alt": "Bakery", "industry_link": "retail", "sort_order": 1},
			{"title": "Pre-pack rooms", "description": "Print without a weigh platter on this device.", "image": r, "image_alt": "Pre-pack", "industry_link": "retail", "sort_order": 2},
			{"title": "EPOS", "description": "Receipt workstation on the XT network.", "image": m["xts600"], "image_alt": "XTs600", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs600 technology", "body": "Non-weighing XT terminal. Do not describe it as a weighing scale. XTs700 is the add-on printer, not this unit.", "image": m["xts600"], "image_alt": "XTs600", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "XTs600 in KSA bakeries", "body": _ksa("XTs600"), "image": bakery, "image_alt": "Bakery", "sort_order": 2},
		],
		faqs=[
			{"question": "Does XTs600 weigh?", "answer": "No. It is a terminal/printer. Add an external platform if you need weight.", "sort_order": 1},
			{"question": "XTs600 or XTi600?", "answer": "XTs600 is 7-inch. XTi600 is 10.1-inch (Item 4606).", "sort_order": 2},
			{"question": "Is this XTs700?", "answer": "No. XTs700 is a complementary second printer attached to a weighing XT.", "sort_order": 3},
		],
		support=support_items("Terminal vs platform pairing.", "Bakery label formats.", "Cassette printer.", "EPOS keys."),
		pack=[{"item_description": "XTs600 non-weighing terminal as quoted", "sort_order": 1}],
	)


def _xts700(m, r, food):
	return _xt_model(
		"avery-berkel-xts700", "Avery Berkel XTs700", "",
		"Label Printers & Terminals", "SECONDARY RETAIL LABEL PRINTER", "xts700", 0,
		tagline="USB second printer for XT scales — two label sizes always loaded",
		short="Avery Berkel XTs700 is a complementary thermal printer, not a scale. It connects to compatible XT equipment over USB so a second label size or format stays available for dual-label, nutrition and pre-pack work.",
		long=(
			"<p>XTs700 is different from every other XTs model: it does not weigh. Avery "
			"Berkel promotes it for dual-label printing — front branding/price on the scale "
			"printer and a larger ingredients, nutrition or allergen label on the XTs700 — "
			"without stopping to change stock.</p>"
			"<p>USB to XT, thermal label/receipt, high-speed printing, multiple label-size "
			"workflows. No XTs700 Item is listed yet. Do not sell it as a standalone scale.</p>"
			f"<p>{_ksa('XTs700')}</p>"
		),
		hero_alt="Avery Berkel XT cassette printer used as XTs700 secondary printer",
		chips="Secondary USB printer\nNot a weighing scale\nDual-label workflows\nNutrition / pre-pack",
		story="Keep a second label format in the counter",
		visual="XTs700",
		card_title="XTs700",
		card_summary="Complementary XT USB printer for a second label size. Not a scale.",
		cta_h="Quote Avery Berkel XTs700",
		cta_d="Pair it with the host XT (XTs or XTi). Confirm both label widths.",
		meta_title="Avery Berkel XTs700 Secondary Label Printer Saudi Arabia | Printechs",
		meta_desc="Avery Berkel XTs700 secondary label and receipt printer for XT weighing scales, ideal for dual-label, nutrition and pre-pack applications.",
		benefits=[
			{"icon": "print", "title": "Second format always ready", "description": "Price label on the scale; nutrition label on the XTs700.", "sort_order": 1},
			{"icon": "integration", "title": "USB to XT", "description": "Sits beside a compatible XTs or XTi host.", "sort_order": 2},
			{"icon": "consumables", "title": "Pre-pack and allergens", "description": "Larger rear labels without swapping the front roll.", "sort_order": 3},
			{"icon": "device", "title": "Not a scale", "description": "Do not specify a platter or AVR capacity on this page.", "sort_order": 4},
		],
		story_items=[
			{"label": "Cassette", "image": m["xts700"], "image_alt": "Cassette printer", "caption": "Easy-load XT cassette — the complementary printer story.", "sort_order": 1},
			{"label": "Label", "image": m["xts700_label"], "image_alt": "Printed label", "caption": "Ingredients, barcode and price on thermal stock.", "sort_order": 2},
			{"label": "Host scale", "image": r, "image_alt": "Retail host scale", "caption": "Pairs with a weighing XT, not instead of one.", "sort_order": 3},
		],
		icons=[
			{"icon": "print", "title": "Role", "description": "Secondary printer", "sort_order": 1},
			{"icon": "connectivity", "title": "Link", "description": "USB to XT host", "sort_order": 2},
			{"icon": "consumables", "title": "Use", "description": "Dual label sizes", "sort_order": 3},
			{"icon": "speed", "title": "Print", "description": "High-speed thermal", "sort_order": 4},
		],
		specs=[
			("This configuration", [
				("Item on this page", "No XTs700 Item yet — quote as XT complementary printer"),
				("Not this page", "XTs600 terminal, any weighing Xs/XTs/XTi"),
			]),
			("Use", [
				("Connection", "USB to compatible XT equipment"),
				("Workflows", "Front/rear labels, nutrition, pre-pack, second receipt"),
			]),
		],
		apps=[
			{"title": "Dual-label packs", "description": "Brand/price plus ingredients.", "image": m["xts700_label"], "image_alt": "Label", "industry_link": "retail", "sort_order": 1},
			{"title": "Pre-pack rooms", "description": "Two sizes loaded all shift.", "image": food, "image_alt": "Pre-pack", "industry_link": "retail", "sort_order": 2},
			{"title": "Allergen labels", "description": "Larger format without stopping the host scale.", "image": r, "image_alt": "Retail", "industry_link": "retail", "sort_order": 3},
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "XTs700 technology", "body": "Complementary XT printer. Avery Berkel’s dual-label story — not a weighing scale and not XTs600.", "image": m["xts700"], "image_alt": "XTs700", "sort_order": 1},
			{"section_type": "Industry Solution", "heading": "Second printers in KSA", "body": _ksa("XTs700"), "image": r, "image_alt": "Retail", "sort_order": 2},
		],
		faqs=[
			{"question": "Is XTs700 a scale?", "answer": "No. It is a USB complementary printer for a host XT.", "sort_order": 1},
			{"question": "XTs700 or XTs600?", "answer": "XTs600 is a standalone non-weighing terminal. XTs700 attaches to a weighing (or terminal) XT.", "sort_order": 2},
			{"question": "What host?", "answer": "Compatible XTs and XTi equipment. Confirm the USB pairing on the quote.", "sort_order": 3},
		],
		support=support_items("Host XT pairing.", "Second label width.", "Print-head on the add-on.", "Dual-label workflow."),
		pack=[{"item_description": "XTs700 complementary printer as quoted", "sort_order": 1}],
	)



def fill_avery_berkel_lineup():
	media = prepare_media()
	fill_hub(media)
	fill_xs_series(media)
	fill_xts_series(media)
	fill_xti_series(media)
	for cfg in models(media):
		fill_model(media, cfg)
	fill_remaining(media)
	for slug, related in RELATED.items():
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		set_related(doc, related)
		doc.flags.ignore_permissions = True
		doc.save()
	frappe.db.commit()
	_update_brand()
	print("Wired Avery Berkel related products")
	return "ok"


def _update_brand():
	name = frappe.db.get_value("Website Brand", {"slug": "avery-berkel"}, "name")
	if not name:
		return
	doc = frappe.get_doc("Website Brand", name)
	doc.summary = (
		"Avery Berkel Xs tactile, XTs 7-inch touch and XTi premium retail weighing "
		"for Saudi fresh-food counters — specified, labelled and supported by Printechs."
	)
	doc.meta_title = "Avery Berkel Retail Weighing Scales Saudi Arabia | Printechs Brands"
	doc.meta_description = (
		"Avery Berkel Xs, XTs and XTi retail weighing and label printing scales from "
		"Printechs in Saudi Arabia. Supermarket, butchery, deli, bakery and seafood."
	)
	doc.published = 1
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
