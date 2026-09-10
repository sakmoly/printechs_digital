# Copyright (c) 2026, Printechs and contributors
"""Nedap Connected RF EAS lineup for Printechs (Saudi commercial pages).

Hub + 7 antennas + iSenseOS + labels + 360° deactivation + integrations.
URLs are /products/{slug} and /brands/nedap.
"""

import frappe

from printechs_digital.setup.nedap_common import (
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
	"nedap-rf-eas": ["nedap-i15-go", "nedap-il45", "nedap-checkout-antenna", "nedap-isenseos"],
	"nedap-i15-go": ["nedap-checkout-antenna", "nedap-il45", "nedap-rf-eas", "nedap-isenseos"],
	"nedap-i45": ["nedap-il45", "nedap-i30", "nedap-rf-eas", "nedap-isenseos"],
	"nedap-il45": ["nedap-i45", "nedap-il33", "nedap-isenseos", "nedap-rf-eas"],
	"nedap-checkout-antenna": ["nedap-i15-go", "nedap-eas-deactivation", "nedap-rf-eas", "nedap-i37"],
	"nedap-i37": ["nedap-i15-go", "nedap-checkout-antenna", "nedap-rf-eas", "nedap-eas-deactivation"],
	"nedap-i30": ["nedap-il33", "nedap-i45", "nedap-rf-eas", "nedap-il45"],
	"nedap-il33": ["nedap-il45", "nedap-i30", "nedap-isenseos", "nedap-rf-eas"],
	"nedap-isenseos": ["nedap-eas-integrations", "nedap-rf-eas", "nedap-il45", "nedap-eas-deactivation"],
	"nedap-rf-eas-labels": ["nedap-eas-deactivation", "nedap-rf-eas", "nedap-i15-go", "nedap-checkout-antenna"],
	"nedap-eas-deactivation": ["nedap-rf-eas-labels", "nedap-checkout-antenna", "nedap-isenseos", "nedap-rf-eas"],
	"nedap-eas-integrations": ["nedap-isenseos", "nedap-rf-eas", "nedap-checkout-antenna", "nedap-il45"],
}


def _ksa_p() -> str:
	return f"<p>{KSA_BODY}</p>"


def fill_hub(media):
	slug = "nedap-rf-eas"
	card = media["hub"]
	doc = get_or_create(slug, "Nedap RF EAS Systems", card)
	apply_identity(doc, slug=slug, display_name="Nedap RF EAS Systems for Intelligent Retail Loss Prevention", category_label="NEDAP RF EAS")
	doc.tagline = "Connected electronic article surveillance that goes beyond the alarm."
	doc.short_description = (
		"Reduce retail shrink across fashion stores, supermarkets, department stores and "
		"self-checkout environments with connected Nedap RF EAS solutions from Printechs."
	)
	doc.long_description = (
		"<p>Nedap RF Electronic Article Surveillance systems combine intelligent merchandise "
		"protection with connected retail technology. Designed for modern stores, supermarkets, "
		"fashion outlets, department stores and self-checkout environments, Nedap EAS solutions "
		"help Saudi retailers reduce shrink while keeping the shopping floor open and welcoming.</p>"
		"<p>Unlike traditional standalone security gates, Nedap EAS antennas run on "
		"<strong>iSenseOS</strong>, Nedap’s connected EAS platform. Retailers can monitor system "
		"health, analyse alarm information and join EAS events to CCTV, video management, staff "
		"notifications, customer counting and metal detection.</p>"
		"<p>Choose the antenna for the entrance: compact <a href=\"/products/nedap-i15-go\">i15 Go</a> "
		"for narrow doors and SCO, scalable <a href=\"/products/nedap-i45\">i45</a> / "
		"<a href=\"/products/nedap-il45\">iL45 Lumen</a> for chain roll-outs, "
		"<a href=\"/products/nedap-checkout-antenna\">Checkout Antenna</a> at the POS, "
		"<a href=\"/products/nedap-i37\">i37</a> for supermarket traffic, "
		"<a href=\"/products/nedap-i30\">i30</a> for design-led fashion, and "
		"<a href=\"/products/nedap-il33\">iL33 Lumen</a> for full-plexiglass interiors. "
		"Complete the system with <a href=\"/products/nedap-rf-eas-labels\">RF labels</a> and "
		"<a href=\"/products/nedap-eas-deactivation\">360° deactivation</a>.</p>"
		"<p><strong>Which gate do you need?</strong> i15 Go — small entrances and self-checkout "
		"(very compact). i45 — general retail and multi-store (performance and scale). "
		"iL45 — fashion, premium and large retail (customer counting plus light/sound). "
		"Checkout Antenna — security at the POS. i37 — supermarket (robust transparent design). "
		"i30 — fashion and design-focused stores (open, adaptable look). "
		"iL33 — premium retail (full plexiglass plus customer counting).</p>"
		+ _ksa_p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "Nedap RF EAS security gates at a modern retail entrance"
	doc.hero_trust_chips = "iSenseOS connected EAS\nFashion · grocery · SCO · POS\nRiyadh · Jeddah · Dammam\nLabels, deactivation and service"
	doc.story_heading = "Nedap EAS Security Systems for Retailers in Saudi Arabia"
	doc.visual_story_heading = "Gates, labels, deactivation and iSenseOS"
	doc.card_title = "Nedap RF EAS"
	doc.card_summary = "Connected RF anti-theft gates, labels and deactivation for Saudi retail — powered by iSenseOS."
	doc.card_image = card
	doc.final_cta_heading = "Protect your stores with Nedap EAS"
	doc.final_cta_description = (
		"Talk to Printechs about the right Nedap EAS configuration for fashion, supermarket, "
		"department and self-checkout stores in Saudi Arabia."
	)
	doc.meta_title = "Nedap EAS Systems Saudi Arabia | RF Anti-Theft Gates | Printechs"
	doc.meta_description = (
		"Nedap RF EAS systems in Saudi Arabia from Printechs. Intelligent retail anti-theft "
		"gates powered by iSenseOS for fashion, supermarkets, self-checkout and modern stores."
	)
	doc.set("benefits", [
		{"icon": "shield", "title": "Reliable RF merchandise protection", "description": "8.2 MHz RF EAS detection designed for fashion, grocery and mixed retail merchandise.", "sort_order": 1},
		{"icon": "cloud", "title": "Connected through iSenseOS", "description": "Monitor health, review events and update supported systems remotely instead of living with a lone beep.", "sort_order": 2},
		{"icon": "integration", "title": "Security ecosystem", "description": "Join EAS events to CCTV/VMS, staff notifications, customer counting and metal detection.", "sort_order": 3},
		{"icon": "store", "title": "Every checkout format", "description": "Compact SCO antennas, POS checkout panels and entrance gates for staffed or self-service floors.", "sort_order": 4},
		{"icon": "report", "title": "Estate-wide scale", "description": "Specify once and support consistent performance across multi-store Saudi retail networks.", "sort_order": 5},
		{"icon": "battery", "title": "Sleep Mode on supported systems", "description": "Standby overnight through iSenseOS — already used on more than 10,000 in-store EAS systems worldwide.", "sort_order": 6},
	])
	doc.set("visual_story_items", [
		{"label": "Fashion entrances", "image": media["fashion-mall"], "image_alt": "Fashion mall EAS", "caption": "Open storefronts still need merchandise protection.", "sort_order": 1},
		{"label": "Grocery traffic", "image": media["supermarket-carts"], "image_alt": "Supermarket EAS", "caption": "Carts, families and peak hours — without a wall of pedestals.", "sort_order": 2},
		{"label": "Self-checkout", "image": media["self-checkout"], "image_alt": "SCO EAS", "caption": "Put detection where the transaction actually happens.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "shield", "title": "Technology", "description": "RF EAS · 8.2 MHz", "sort_order": 1},
		{"icon": "cloud", "title": "Platform", "description": "iSenseOS on Nedap antennas", "sort_order": 2},
		{"icon": "store", "title": "Formats", "description": "Entrance · SCO · POS", "sort_order": 3},
		{"icon": "integration", "title": "Add-ons", "description": "Counting · metal · VMS", "sort_order": 4},
	])
	set_specs(doc, [
		("Connected RF EAS portfolio", [
			("Platform", "iSenseOS on Nedap RF EAS antennas"),
			("Antennas", "i15 Go, i45, iL45 Lumen, Checkout Antenna, i37, i30, iL33 Lumen"),
			("Labels", "Power (dry), Cool (chilled/frozen) and Beauty RF labels"),
			("Deactivation", "360° Smart Deactivator for staffed and self-checkout"),
			("RF frequency", "Standard 8.2 MHz RF EAS"),
		]),
		("Retail operations", [
			("Integrations", "CCTV/VMS, staff notifications, customer counting, metal detection, I/O"),
			("Sleep Mode", "Standby overnight on supported systems via iSenseOS"),
			("Warranty", "1 year factory warranty; optional 3- or 5-year extended cover"),
			("Deployment", "Nedap network covering 120+ countries; Printechs installs in KSA"),
			("Advertising", "Optional advertising panels on supported antenna configurations"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Compare Nedap RF EAS antennas",
			"body": (
				"i15 Go — small entrances and self-checkout; very compact (~15 cm wide). "
				"i45 — general retail and multi-store; performance and easy maintenance. "
				"iL45 Lumen — fashion, premium and large retail; customer counting plus configurable light and sound. "
				"Checkout Antenna — POS lanes; staff respond before the shopper leaves the till. "
				"i37 — supermarket; robust transparent design in black or grey. "
				"i30 — fashion and design-led stores; open, adaptable appearance. "
				"iL33 Lumen — premium retail; full plexiglass with upward alarm lighting and counting."
			),
			"image": media["counting-entrance"],
			"image_alt": "Retail entrance with Nedap EAS",
			"link_label": "See iSenseOS",
			"link_href": "/products/nedap-isenseos",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": "Quoted Nedap RF EAS antennas and mounting hardware", "sort_order": 1},
		{"item_description": "RF labels and 360° deactivation as specified", "sort_order": 2},
		{"item_description": "iSenseOS connectivity and agreed integrations", "sort_order": 3},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Which Nedap gate do I need?", "answer": "i15 Go for narrow doors and SCO. i45 for scalable chain roll-outs. iL45 when you want counting plus configurable light/sound. Checkout Antenna at the POS. i37 for supermarket trolley traffic. i30 when store design leads. iL33 for full-plexiglass premium interiors.", "sort_order": 1},
		{"question": "Is Nedap only an exit alarm?", "answer": "No. iSenseOS turns EAS events into health data, analytics and integrations with CCTV/VMS, staff devices, counting and metal detection — so the system is more than a beep at the door.", "sort_order": 2},
		{"question": "Do you install Nedap EAS in Saudi Arabia?", "answer": "Yes. Printechs consults, supplies, installs, configures and supports Nedap EAS in Riyadh, Jeddah, Dammam and other regions.", "sort_order": 3},
	])
	return save_product(doc)


def _gate_page(media, cfg):
	slug = cfg["slug"]
	card = media[cfg["card"]]
	doc = get_or_create(slug, cfg["product_name"], card)
	apply_identity(doc, slug=slug, display_name=cfg["h1"], category_label=cfg["category_label"])
	doc.tagline = cfg["tagline"]
	doc.short_description = cfg["short"]
	doc.long_description = cfg["long"] + _ksa_p()
	doc.hero_image = card
	doc.hero_image_alt = cfg["hero_alt"]
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
	doc.set("visual_story_items", cfg["story_items"](media, card))
	doc.set("icon_specifications", cfg["icons"])
	set_specs(doc, cfg["specs"])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": cfg["ideal_h"],
			"body": cfg["ideal_b"],
			"image": media[cfg["ideal_img"]],
			"image_alt": cfg["ideal_alt"],
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": cfg["pack"], "sort_order": 1},
		{"item_description": "Installation, commissioning and store-team briefing as quoted", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", cfg["faqs"])
	return save_product(doc)


def gate_configs(media):
	return [
		{
			"slug": "nedap-i15-go",
			"card": "i15",
			"product_name": "Nedap i15 Go RF EAS Antenna",
			"h1": "Nedap i15 Go – Compact RF EAS Security for Modern Retail",
			"category_label": "COMPACT RF EAS",
			"tagline": "Slim RF protection for narrow doors and self-checkout.",
			"short": (
				"The Nedap i15 Go is a compact RF EAS antenna for stores where floor space is valuable. "
				"Its slim design suits narrow retail entrances, merchandise close to the exit, and self-checkout zones."
			),
			"long": (
				"<p>Saudi fashion, pharmacy and convenience formats increasingly need loss prevention that "
				"does not steal the aisle or hide the merchandise. The Nedap i15 Go answers that with RF EAS "
				"detection, a contemporary slim pedestal and iSenseOS connectivity.</p>"
				"<p>Antenna width is approximately <strong>15 cm</strong> (1564 × 150 × 71.4 mm). That lets "
				"Printechs place protection where a conventional pedestal would block customer flow or a SCO lane.</p>"
				"<p>An always-on status light shows the system is operating. If that indication disappears, "
				"store staff can see immediately that the antenna needs attention — without waiting for a failed audit.</p>"
			),
			"hero_alt": "Nedap i15 Go compact RF EAS antenna",
			"chips": "Approx. 15 cm wide\nSelf-checkout and small doors\niSenseOS connected\nAlways-on status light",
			"story": "Compact RF EAS that leaves the aisle open",
			"visual": "Small antenna, full entrance job",
			"card_title": "i15 Go",
			"card_summary": "Compact ~15 cm RF EAS antenna for narrow entrances and self-checkout zones.",
			"cta_h": "Specify i15 Go for tight Saudi storefronts",
			"cta_d": "Ask Printechs for an entrance or SCO survey — we will confirm i15 Go versus a wider Nedap antenna.",
			"meta_title": "Nedap i15 Go EAS Antenna Saudi Arabia | Printechs",
			"meta_desc": "Nedap i15 Go compact RF EAS system for retail entrances and self-checkout areas. Connected anti-theft protection powered by iSenseOS in Saudi Arabia.",
			"benefits": [
				{"icon": "store", "title": "Compact RF EAS antenna", "description": "Approximately 15 cm wide so narrow doors and SCO exits stay usable.", "sort_order": 1},
				{"icon": "checkout", "title": "Built for self-checkout", "description": "Place detection at the SCO hall without a pair of full-size pedestals.", "sort_order": 2},
				{"icon": "cloud", "title": "iSenseOS connected", "description": "Remote health monitoring and the same connected platform as larger Nedap gates.", "sort_order": 3},
				{"icon": "display", "title": "Always-on status light", "description": "Staff see immediately if the system is no longer indicating normal operation.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Nedap i15 Go", "caption": "Slim charcoal pedestal — easy to place, easy to live with.", "sort_order": 1},
				{"label": "Boutique door", "image": m["boutique-narrow"], "image_alt": "Boutique i15 Go", "caption": "Protect the exit without blocking the rail.", "sort_order": 2},
				{"label": "SCO", "image": m["cosmetics-sco"], "image_alt": "SCO i15 Go", "caption": "Beauty and specialty self-checkout.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Width", "description": "Approx. 15 cm · 1564 mm tall", "sort_order": 1},
				{"icon": "connectivity", "title": "Connect", "description": "Ethernet · USB service", "sort_order": 2},
				{"icon": "cloud", "title": "Platform", "description": "iSenseOS · Sleep Mode", "sort_order": 3},
				{"icon": "install", "title": "Mounting", "description": "Floor · ~10 kg", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap i15 Go"),
					("Technology", "RF EAS · 8.2 MHz"),
					("Platform", "iSenseOS"),
					("Best for", "Narrow entrances, SCO zones, compact retail"),
				]),
				("Physical", [
					("Dimensions", "1564 × 150 × 71.4 mm"),
					("Weight", "Approximately 10 kg"),
					("Mounting", "Floor mounted"),
					("Status indication", "Permanent visual status light"),
				]),
				("Power & connectivity", [
					("Mains", "100–240 V"),
					("Average consumption", "12 W per antenna"),
					("Connectivity", "Ethernet; USB service port only"),
					("Operating temperature", "0–45 °C"),
					("Sleep Mode", "Yes, with iSenseOS"),
				]),
			],
			"ideal_h": "Ideal for compact Saudi retail",
			"ideal_b": "Supermarkets, convenience stores, fashion, cosmetics, pharmacies, self-checkout halls and any compact store where a full-size pedestal would fight the merchandise.",
			"ideal_img": "pharmacy",
			"ideal_alt": "Pharmacy entrance with compact EAS",
			"pack": "Quoted Nedap i15 Go antenna(s) and floor mounting kit",
			"faqs": [
				{"question": "How wide is the i15 Go?", "answer": "Approximately 15 cm (150 mm). Overall dimensions are 1564 × 150 × 71.4 mm.", "sort_order": 1},
				{"question": "Is it only for self-checkout?", "answer": "No. SCO is a primary use, but i15 Go also fits small fashion, pharmacy and convenience doors where floor space is tight.", "sort_order": 2},
				{"question": "Can Printechs install i15 Go in KSA?", "answer": "Yes. We survey the door or SCO lane, install, connect iSenseOS and train the store team.", "sort_order": 3},
			],
		},
		{
			"slug": "nedap-i45",
			"card": "i45",
			"product_name": "Nedap i45 RF EAS Antenna",
			"h1": "Nedap i45 – High-Performance RF EAS for Retail",
			"category_label": "RF EAS ANTENNA",
			"tagline": "Robust RF EAS built to roll out across many stores.",
			"short": (
				"The Nedap i45 is a robust RF EAS antenna for retailers that need reliable performance, "
				"scalability and straightforward installation and maintenance."
			),
			"long": (
				"<p>The Nedap i45 is the workhorse RF antenna when a Saudi chain needs one specification "
				"that installers can repeat — including programmes that grow to hundreds of stores.</p>"
				"<p>Nedap highlights strong detection, scalability and easier installation/maintenance. "
				"With iSenseOS the i45 sits in a connected loss-prevention estate instead of operating as "
				"an isolated door alarm.</p>"
				"<p>Need visitor counting and richer light/sound? See the Lumen edition, "
				"<a href=\"/products/nedap-il45\">Nedap iL45</a>. An RFID upgrade path can be discussed "
				"when a store later specifies hybrid RF/RFID — this page is the RF EAS antenna.</p>"
			),
			"hero_alt": "Nedap i45 RF EAS antenna",
			"chips": "Multi-store scalability\nRobust RF detection\nEasy install & service\niSenseOS connected",
			"story": "The RF antenna for chain-wide roll-outs",
			"visual": "Performance first, then the Lumen extras",
			"card_title": "i45",
			"card_summary": "Robust RF EAS antenna for scalable multi-store retail loss prevention.",
			"cta_h": "Plan an i45 roll-out with Printechs",
			"cta_d": "We will map entrance widths, label strategy and whether i45 or iL45 Lumen is the right pedestal.",
			"meta_title": "Nedap i45 RF EAS System Saudi Arabia | Retail Security | Printechs",
			"meta_desc": "Nedap i45 RF EAS antenna for reliable retail loss prevention. Scalable, connected and easy to maintain for multi-store retailers in Saudi Arabia.",
			"benefits": [
				{"icon": "shield", "title": "High-performance RF EAS", "description": "A robust open-frame antenna specified for everyday retail detection.", "sort_order": 1},
				{"icon": "store", "title": "Built to scale", "description": "The same platform Nedap cites for installations across hundreds of stores.", "sort_order": 2},
				{"icon": "install", "title": "Easier to install and service", "description": "A practical choice when facilities teams must keep many sites online.", "sort_order": 3},
				{"icon": "cloud", "title": "iSenseOS estate view", "description": "Remote health, event insight and security-ecosystem integration.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Nedap i45", "caption": "Open-frame RF antenna for general retail.", "sort_order": 1},
				{"label": "Fashion chain", "image": m["fashion-chain"], "image_alt": "Fashion chain i45", "caption": "Repeatable specification for mall stores.", "sort_order": 2},
				{"label": "Hypermarket", "image": m["hypermarket"], "image_alt": "Hypermarket i45", "caption": "Wide grocery entrances that still need RF protection.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Size", "description": "1668 × 462 × 100 mm", "sort_order": 1},
				{"icon": "durability", "title": "Weight", "description": "9.5 kg floor-mounted", "sort_order": 2},
				{"icon": "connectivity", "title": "Power", "description": "100–240 V · ~12 W", "sort_order": 3},
				{"icon": "cloud", "title": "Platform", "description": "iSenseOS", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap i45 RF EAS antenna"),
					("Technology", "RF EAS · 8.2 MHz"),
					("Platform", "iSenseOS"),
					("Related model", "iL45 Lumen adds customer counting and configurable light/sound"),
				]),
				("Physical", [
					("Dimensions", "1668 × 462 × 100 mm"),
					("Weight", "9.5 kg"),
					("Mounting", "Floor mounted"),
					("Alarm signalling", "Audio and visual lights"),
				]),
				("Power", [
					("Mains", "100–240 V"),
					("Average consumption", "12 W per antenna"),
				]),
			],
			"ideal_h": "Ideal for multi-store retail",
			"ideal_b": "Fashion chains, department stores, hypermarkets, supermarkets, large retail networks and specialty stores that want one RF antenna they can repeat.",
			"ideal_img": "department-store",
			"ideal_alt": "Department store with i45-class EAS",
			"pack": "Quoted Nedap i45 antenna(s) and floor mounting kit",
			"faqs": [
				{"question": "How is i45 different from iL45?", "answer": "i45 is the robust RF workhorse. iL45 Lumen adds integrated customer counting and configurable multicolour light and sound.", "sort_order": 1},
				{"question": "Is this page an RFID gate?", "answer": "No. This page is the RF EAS i45. An upgrade path toward hybrid RF/RFID can be discussed when a project specifies it.", "sort_order": 2},
				{"question": "Can you roll i45 out across KSA stores?", "answer": "Yes. Printechs surveys, installs and supports multi-store programmes in Riyadh, Jeddah, Dammam and other regions.", "sort_order": 3},
			],
		},
		{
			"slug": "nedap-il45",
			"card": "il45",
			"product_name": "Nedap iL45 Lumen RF EAS Antenna",
			"h1": "Nedap iL45 Lumen – Intelligent EAS with Customer Counting",
			"category_label": "LUMEN RF EAS",
			"tagline": "RF protection plus visitor counting and configurable alarms.",
			"short": (
				"The Nedap iL45 combines RF EAS merchandise protection with integrated customer counting "
				"and advanced visual and audible alarm capabilities."
			),
			"long": (
				"<p>When a Saudi fashion or department-store team wants more than a door beep, iL45 Lumen "
				"adds store intelligence on the same pedestal: visitor counts, multicolour LED indication "
				"and configurable audible alarms that staff can actually recognise.</p>"
				"<p>Nedap lists the antenna at approximately <strong>1690 × 462 × 100 mm</strong>, with "
				"Ethernet connectivity and a USB service port. Lighting can use different colours and "
				"patterns; audible alarms can support different audio options.</p>"
				"<p>iL45 participates in the connected retail ecosystem through iSenseOS. For the same "
				"frame without Lumen extras, see <a href=\"/products/nedap-i45\">Nedap i45</a>.</p>"
			),
			"hero_alt": "Nedap iL45 Lumen RF EAS antenna",
			"chips": "Integrated customer counting\nConfigurable light & sound\nEthernet + USB service\niSenseOS insights",
			"story": "The Lumen antenna we highlight for intelligent entrances",
			"visual": "Count visitors. Show the alarm. Keep the store open.",
			"card_title": "iL45 Lumen",
			"card_summary": "Lumen RF EAS with customer counting and configurable light and sound.",
			"cta_h": "Add counting and clearer alarms with iL45",
			"cta_d": "Printechs will confirm iL45 versus i45 and how counting data should reach your team.",
			"meta_title": "Nedap iL45 Lumen EAS Gate Saudi Arabia | Printechs",
			"meta_desc": "Nedap iL45 Lumen RF EAS antenna with customer counting, configurable lights and sound, connected retail security and iSenseOS capabilities.",
			"benefits": [
				{"icon": "report", "title": "Integrated customer counting", "description": "Visitor information from the same entrance that protects merchandise.", "sort_order": 1},
				{"icon": "display", "title": "Configurable light patterns", "description": "Multicolour LED indication so staff see the event, not just hear a beep.", "sort_order": 2},
				{"icon": "device", "title": "Configurable audible alarms", "description": "Different audio options to match store policy and noise levels.", "sort_order": 3},
				{"icon": "connectivity", "title": "Ethernet + USB service", "description": "Networked monitoring with a USB port reserved for service.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Nedap iL45", "caption": "Lumen edition of the i45 family.", "sort_order": 1},
				{"label": "Premium fashion", "image": m["premium-lumen"], "image_alt": "Premium iL45", "caption": "Lighting that belongs in a flagship.", "sort_order": 2},
				{"label": "Counting", "image": m["counting-entrance"], "image_alt": "Counting entrance", "caption": "Traffic data at the door.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Size", "description": "1690 × 462 × 100 mm", "sort_order": 1},
				{"icon": "report", "title": "Counting", "description": "Integrated customer counters", "sort_order": 2},
				{"icon": "connectivity", "title": "Connect", "description": "Ethernet · USB service", "sort_order": 3},
				{"icon": "display", "title": "Alarms", "description": "Multicolour LED · audio", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap iL45 Lumen"),
					("Technology", "RF EAS merchandise protection"),
					("Platform", "iSenseOS"),
					("Lumen extras", "Customer counting, configurable lights and sound"),
				]),
				("Physical", [
					("Dimensions", "1690 × 462 × 100 mm"),
					("Weight", "10 kg"),
					("Mounting", "Floor mounted"),
					("Alarm signalling", "Audible and multicolour light"),
				]),
				("Connectivity & power", [
					("Connectivity", "Ethernet; USB service port"),
					("Mains", "100–240 V"),
				]),
			],
			"ideal_h": "Ideal for intelligent flagship floors",
			"ideal_b": "Fashion stores, department stores, premium retail, electronics, sports retail and supermarkets that want counting and clearer alarms — not only detection.",
			"ideal_img": "electronics",
			"ideal_alt": "Electronics store with Lumen EAS",
			"pack": "Quoted Nedap iL45 Lumen antenna(s) and floor mounting kit",
			"faqs": [
				{"question": "Does iL45 include people counting?", "answer": "Yes. Nedap specifies integrated customer counters on the iL45 Lumen edition.", "sort_order": 1},
				{"question": "Can lights and sounds be configured?", "answer": "Yes. Multicolour LED patterns and different audible options are part of the Lumen proposition.", "sort_order": 2},
				{"question": "Do you support iL45 in Saudi Arabia?", "answer": "Yes. Printechs supplies, installs and supports iL45 with iSenseOS across KSA regions.", "sort_order": 3},
			],
		},
		{
			"slug": "nedap-checkout-antenna",
			"card": "checkout",
			"product_name": "Nedap Checkout RF EAS Antenna",
			"h1": "Nedap Checkout Antenna – EAS Protection Directly at the POS",
			"category_label": "CHECKOUT EAS",
			"tagline": "Move detection to the till — where staff already stand.",
			"short": (
				"The Nedap Checkout Antenna brings EAS protection closer to the transaction by placing "
				"detection directly around the checkout area."
			),
			"long": (
				"<p>Traditional EAS sits at the exit. By then the shopper has paid — or walked out — and "
				"intervention is public. Nedap’s Checkout Antenna puts RF detection at the cashier so "
				"staff already in conversation can react immediately and more discreetly.</p>"
				"<p>That placement is especially relevant for Saudi supermarkets and self-service projects: "
				"the closer the antenna is to the point of sale, the higher the chance of a useful response.</p>"
				"<p>Pair it with <a href=\"/products/nedap-eas-deactivation\">360° deactivation</a> so paid "
				"labels die at the scanner, and with <a href=\"/products/nedap-i15-go\">i15 Go</a> if the "
				"SCO exit still needs a slim pedestal.</p>"
			),
			"hero_alt": "Nedap Checkout Antenna at a retail till",
			"chips": "EAS at the POS\nFaster staff response\nMore discreet intervention\nGrocery and fashion tills",
			"story": "Security that happens during the sale",
			"visual": "Eye contact first, then the alarm",
			"card_title": "Checkout Antenna",
			"card_summary": "RF EAS at the POS so staff can respond before the customer leaves the till.",
			"cta_h": "Secure the checkout, not only the exit",
			"cta_d": "Ask Printechs to review lane layout, SCO mix and whether Checkout Antenna plus deactivation is the right pair.",
			"meta_title": "Nedap Checkout EAS Antenna Saudi Arabia | POS Security | Printechs",
			"meta_desc": "Nedap Checkout Antenna provides RF EAS protection directly at the POS checkout, helping retail staff respond to security alarms quickly and discreetly.",
			"benefits": [
				{"icon": "checkout", "title": "EAS at the checkout", "description": "RF detection around the till instead of only at the store exit.", "sort_order": 1},
				{"icon": "speed", "title": "Faster employee response", "description": "Staff already facing the customer can act before the shopper leaves the lane.", "sort_order": 2},
				{"icon": "store", "title": "More discreet intervention", "description": "Handle the event at the belt — less stress for customers and teams.", "sort_order": 3},
				{"icon": "integration", "title": "Connected EAS ecosystem", "description": "Works with Nedap labels, deactivation and iSenseOS monitoring.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Checkout Antenna", "caption": "Panel integrated into the checkout furniture.", "sort_order": 1},
				{"label": "Grocery lane", "image": m["pos-lane"], "image_alt": "POS lane", "caption": "Detection while the transaction is still open.", "sort_order": 2},
				{"label": "Fashion desk", "image": m["discreet-staff"], "image_alt": "Fashion till", "caption": "Quiet handling at the cash wrap.", "sort_order": 3},
			],
			"icons": [
				{"icon": "checkout", "title": "Placement", "description": "At the POS / till", "sort_order": 1},
				{"icon": "shield", "title": "Technology", "description": "RF merchandise detection", "sort_order": 2},
				{"icon": "store", "title": "Formats", "description": "Staffed and SCO strategies", "sort_order": 3},
				{"icon": "cloud", "title": "Platform", "description": "Nedap EAS ecosystem", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap Checkout Antenna"),
					("Technology", "RF EAS at the point of sale"),
					("Role", "Detection around the checkout, not only the exit"),
					("Typical pairing", "360° deactivation and optional i15 Go at SCO exits"),
				]),
				("Application", [
					("Environments", "Conventional cashier lanes and modern checkout security layouts"),
					("Staff benefit", "Eye contact with the customer when an event occurs"),
					("Platform", "Connected through Nedap’s EAS / iSenseOS ecosystem"),
				]),
			],
			"ideal_h": "Ideal for Saudi checkout projects",
			"ideal_b": "Supermarkets, hypermarkets, self-service retail, fashion, department stores and any high-volume checkout where response time at the till matters more than a beep at the door.",
			"ideal_img": "grocery-till",
			"ideal_alt": "Grocery till with checkout EAS",
			"pack": "Quoted Nedap Checkout Antenna and till integration hardware as specified",
			"faqs": [
				{"question": "Does this replace exit gates?", "answer": "Not always. Many stores combine Checkout Antenna at the POS with a compact exit antenna or supermarket gate. Printechs will map the flow.", "sort_order": 1},
				{"question": "Is it for self-checkout?", "answer": "It supports modern checkout strategies. SCO projects often add 360° deactivation and, where needed, i15 Go at the SCO exit.", "sort_order": 2},
				{"question": "Can you fit it to existing tills?", "answer": "We survey belt, furniture and cable routes in KSA stores before confirming the configuration.", "sort_order": 3},
			],
		},
		{
			"slug": "nedap-i37",
			"card": "i37",
			"product_name": "Nedap i37 RF EAS Gate",
			"h1": "Nedap i37 – Robust RF EAS Security for Supermarkets",
			"category_label": "SUPERMARKET EAS",
			"tagline": "Transparent RF EAS for grocery traffic — black or grey.",
			"short": (
				"The Nedap i37 is a robust, transparent RF EAS antenna designed particularly for "
				"supermarket and high-volume retail environments."
			),
			"long": (
				"<p>Supermarket security has to survive carts, peak hours and wet-floor reality while "
				"shoppers still see an open store. The Nedap i37 uses a transparent panel so the gate "
				"does not dominate the entrance.</p>"
				"<p>Nedap lists the i37 in <strong>black and grey</strong> editions. Typical dimensions "
				"are <strong>1500 × 370 × 40 mm</strong> at about 10.6 kg, with Ethernet and a USB "
				"service port — a slim, robust supermarket antenna on iSenseOS.</p>"
			),
			"hero_alt": "Nedap i37 transparent RF EAS gate",
			"chips": "Transparent supermarket design\nBlack and grey editions\nSlim 40 mm panel\niSenseOS connected",
			"story": "Grocery-grade RF EAS that stays visually light",
			"visual": "Carts first. Then the gate.",
			"card_title": "i37",
			"card_summary": "Robust transparent RF EAS gate for supermarket environments, in black or grey.",
			"cta_h": "Specify i37 for grocery entrances",
			"cta_d": "Printechs will check trolley width, finish (black/grey) and whether Checkout Antenna should sit at the lanes.",
			"meta_title": "Nedap i37 EAS Gate Saudi Arabia | Supermarket EAS | Printechs",
			"meta_desc": "Nedap i37 RF EAS gate designed for supermarket and retail environments. Robust transparent design available in black and grey configurations.",
			"benefits": [
				{"icon": "shield", "title": "RF EAS for grocery", "description": "Robust detection specified for supermarket and high-volume retail.", "sort_order": 1},
				{"icon": "store", "title": "Transparent panel", "description": "Keeps sightlines open for carts, families and merchandising.", "sort_order": 2},
				{"icon": "device", "title": "Black or grey", "description": "Match the store interior instead of forcing one colour.", "sort_order": 3},
				{"icon": "cloud", "title": "Enterprise connectivity", "description": "Ethernet, USB service and iSenseOS for multi-store grocery groups.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Nedap i37", "caption": "Slim transparent supermarket gate.", "sort_order": 1},
				{"label": "Cart aisle", "image": m["cart-aisle"], "image_alt": "Carts and i37", "caption": "Trolleys pass without a visual wall.", "sort_order": 2},
				{"label": "Grey edition", "image": m["grey-gate"], "image_alt": "Grey i37", "caption": "Finish options for different interiors.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Size", "description": "1500 × 370 × 40 mm", "sort_order": 1},
				{"icon": "durability", "title": "Weight", "description": "10.6 kg", "sort_order": 2},
				{"icon": "connectivity", "title": "Connect", "description": "Ethernet · USB service", "sort_order": 3},
				{"icon": "store", "title": "Finishes", "description": "Black and grey", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap i37"),
					("Technology", "RF EAS"),
					("Design", "Robust transparent gate for supermarket environments"),
					("Finishes", "Black and grey editions"),
				]),
				("Physical", [
					("Dimensions", "1500 × 370 × 40 mm"),
					("Weight", "10.6 kg"),
					("Mounting", "Floor mounted"),
					("Alarm signalling", "Audio, visual and/or signal messages"),
				]),
				("Connectivity & power", [
					("Connectivity", "Ethernet; USB service port only"),
					("Mains", "100–240 V"),
					("Platform", "iSenseOS-connected EAS architecture"),
				]),
			],
			"ideal_h": "Ideal for grocery and high traffic",
			"ideal_b": "Supermarkets, hypermarkets, grocery retail, department stores and high-traffic stores where carts and families define the entrance.",
			"ideal_img": "high-traffic",
			"ideal_alt": "Busy supermarket with i37",
			"pack": "Quoted Nedap i37 antenna(s) in black or grey and floor mounting kit",
			"faqs": [
				{"question": "Black or grey?", "answer": "Nedap lists both editions. We match the finish to the supermarket interior during the site survey.", "sort_order": 1},
				{"question": "Will shopping carts fit?", "answer": "The 40 mm transparent panel is designed for supermarket movement. We still measure trolley width and door geometry on site.", "sort_order": 2},
				{"question": "Do you install i37 in KSA grocery groups?", "answer": "Yes. Printechs supports supermarket programmes in Riyadh, Jeddah, Dammam and other regions.", "sort_order": 3},
			],
		},
		{
			"slug": "nedap-i30",
			"card": "i30",
			"product_name": "Nedap i30 RF EAS Gate",
			"h1": "Nedap i30 – EAS Security Designed Around Your Store",
			"category_label": "DESIGN RF EAS",
			"tagline": "Open modern RF EAS that can follow the store concept.",
			"short": (
				"The Nedap i30 combines RF EAS merchandise protection with an open, contemporary antenna "
				"design developed to complement modern retail interiors."
			),
			"long": (
				"<p>Loss prevention should protect merchandise without flattening a retailer’s store concept. "
				"The Nedap i30 is the open silver frame for fashion and premium interiors that refuse a "
				"heavy security look.</p>"
				"<p>The appearance can be adapted to the brand or store so the gate integrates with the "
				"entrance instead of sitting in front of it. Typical dimensions are "
				"<strong>1665 × 322 × 100 mm</strong> at about 7.5 kg, with audible and multicolour "
				"alarm signalling on iSenseOS.</p>"
				"<p>Visitor counting and metal detection can be added on the same single-cable installation "
				"when the project specifies those options.</p>"
			),
			"hero_alt": "Nedap i30 open RF EAS gate",
			"chips": "Open modern frame\nAdaptable store look\n~7.5 kg\nOptional counting / metal detection",
			"story": "Design the entrance. Then protect it.",
			"visual": "An antenna that can wear the brand",
			"card_title": "i30",
			"card_summary": "Open, modern RF EAS gate that can be adapted to fashion and premium store design.",
			"cta_h": "Match i30 to your store concept",
			"cta_d": "Share interior references with Printechs — we will confirm i30 versus iL33 plexiglass or iL45 Lumen.",
			"meta_title": "Nedap i30 EAS Gate Saudi Arabia | Modern Retail Security | Printechs",
			"meta_desc": "Nedap i30 RF EAS security gate with an open modern design that can be adapted to complement fashion, department and premium retail environments.",
			"benefits": [
				{"icon": "store", "title": "Open modern design", "description": "A slender frame that strengthens the entrance instead of closing it.", "sort_order": 1},
				{"icon": "display", "title": "Adaptable appearance", "description": "Specify the look against the store or brand concept.", "sort_order": 2},
				{"icon": "shield", "title": "RF merchandise protection", "description": "Full RF EAS duty in a design-led pedestal.", "sort_order": 3},
				{"icon": "integration", "title": "Optional counting and metal", "description": "Add visitor counting or metal detection on the same cable path when specified.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Nedap i30", "caption": "Open silver frame for design-led stores.", "sort_order": 1},
				{"label": "Luxury lobby", "image": m["luxury-open"], "image_alt": "Luxury i30", "caption": "Security that reads as architecture.", "sort_order": 2},
				{"label": "Flagship", "image": m["branded-entrance"], "image_alt": "Flagship i30", "caption": "Coordinate the gate with the interior.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Size", "description": "1665 × 322 × 100 mm", "sort_order": 1},
				{"icon": "durability", "title": "Weight", "description": "7.5 kg", "sort_order": 2},
				{"icon": "display", "title": "Alarms", "description": "Audible · multicolour light", "sort_order": 3},
				{"icon": "cloud", "title": "Power", "description": "100–240 V · ~12 W", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap i30"),
					("Technology", "RF EAS"),
					("Design", "Open modern frame, adaptable to store concept"),
					("Options", "Integrated visitor counting and metal detection when specified"),
				]),
				("Physical", [
					("Dimensions", "1665 × 322 × 100 mm"),
					("Weight", "7.5 kg"),
					("Mounting", "Floor mounted"),
					("Alarm signalling", "Audible and multicolour light"),
				]),
				("Power & platform", [
					("Mains", "100–240 V"),
					("Average consumption", "12 W per antenna"),
					("Platform", "iSenseOS-connected architecture"),
				]),
			],
			"ideal_h": "Ideal for design-led retail",
			"ideal_b": "Fashion, luxury retail, cosmetics, department stores, electronics and sports retail — anywhere the entrance is part of the brand.",
			"ideal_img": "cosmetics-luxury",
			"ideal_alt": "Luxury cosmetics hall with i30",
			"pack": "Quoted Nedap i30 antenna(s), finish options and floor mounting kit",
			"faqs": [
				{"question": "Can the look be customised?", "answer": "Nedap positions i30 as adaptable to brand or store design. We confirm available finish and panel options during quotation.", "sort_order": 1},
				{"question": "i30 or iL33?", "answer": "i30 is the open frame. iL33 Lumen is full plexiglass with upward lighting and integrated counting. We choose from the interior, not a catalogue photo.", "sort_order": 2},
				{"question": "Is i30 used in Saudi fashion stores?", "answer": "Yes. Printechs specifies i30 for design-led fashion and department projects across KSA.", "sort_order": 3},
			],
		},
		{
			"slug": "nedap-il33",
			"card": "il33",
			"product_name": "Nedap iL33 Lumen RF EAS Antenna",
			"h1": "Nedap iL33 Lumen – Transparent Intelligent EAS Security",
			"category_label": "LUMEN PLEXIGLASS EAS",
			"tagline": "Full plexiglass Lumen EAS with counting and upward lights.",
			"short": (
				"The Nedap iL33 Lumen is a full-plexiglass RF EAS antenna combining transparent retail "
				"design with integrated customer counting and configurable alarm indications."
			),
			"long": (
				"<p>iL33 Lumen is for Saudi boutiques and premium halls that want merchandise protection "
				"without a metal cage at the door. Full plexiglass keeps the entrance visually light.</p>"
				"<p>Integrated customer counting adds visitor information. Multiple light and sound options "
				"help staff recognise events. Nedap positions the alarm lighting so it "
				"<strong>shines upward</strong> — easier to see from inside the store than a side-facing beacon.</p>"
				"<p>Typical dimensions are <strong>1534.3 × 328.6 × 97.7 mm</strong> at about 15 kg, with "
				"Ethernet and a USB service port. One-cable Ethernet installation is cited for data and power.</p>"
			),
			"hero_alt": "Nedap iL33 Lumen plexiglass RF EAS antenna",
			"chips": "Full plexiglass Lumen\nCustomer counting\nUpward alarm lighting\nConfigurable light & sound",
			"story": "Transparent security staff can actually see",
			"visual": "Light goes up. Teams look up.",
			"card_title": "iL33 Lumen",
			"card_summary": "Full-plexiglass Lumen RF EAS with customer counting and upward alarm lighting.",
			"cta_h": "Specify iL33 for premium plexiglass entrances",
			"cta_d": "Printechs will compare iL33 with i30 and iL45 against your interior and counting requirements.",
			"meta_title": "Nedap iL33 Lumen EAS Gate Saudi Arabia | Printechs",
			"meta_desc": "Nedap iL33 Lumen transparent RF EAS antenna with integrated customer counting and configurable light and sound alarms for modern retail stores.",
			"benefits": [
				{"icon": "store", "title": "Full plexiglass antenna", "description": "Transparent Lumen design for premium interiors that reject a heavy frame.", "sort_order": 1},
				{"icon": "report", "title": "Integrated customer counters", "description": "Visitor information from the same elegant pedestal.", "sort_order": 2},
				{"icon": "display", "title": "Upward-facing alarm light", "description": "Illumination aimed up so staff see the event from the sales floor.", "sort_order": 3},
				{"icon": "device", "title": "Configurable light and sound", "description": "Multiple visual and audible options in the Lumen series.", "sort_order": 4},
			],
			"story_items": lambda m, card: [
				{"label": "Product", "image": card, "image_alt": "Nedap iL33", "caption": "Full plexiglass Lumen antenna.", "sort_order": 1},
				{"label": "Boutique", "image": m["plexi-boutique"], "image_alt": "Boutique iL33", "caption": "Security that stays visually quiet.", "sort_order": 2},
				{"label": "Upward light", "image": m["upward-light"], "image_alt": "Upward iL33 light", "caption": "Alarms aimed where staff can see them.", "sort_order": 3},
			],
			"icons": [
				{"icon": "device", "title": "Size", "description": "1534.3 × 328.6 × 97.7 mm", "sort_order": 1},
				{"icon": "durability", "title": "Weight", "description": "15 kg", "sort_order": 2},
				{"icon": "report", "title": "Counting", "description": "Integrated counters", "sort_order": 3},
				{"icon": "connectivity", "title": "Install", "description": "Ethernet · USB service", "sort_order": 4},
			],
			"specs": [
				("Model", [
					("Model", "Nedap iL33 Lumen"),
					("Technology", "RF EAS"),
					("Design", "Full plexiglass Lumen series antenna"),
					("Lighting", "Alarm lights positioned to shine upward"),
				]),
				("Physical", [
					("Dimensions", "1534.3 × 328.6 × 97.7 mm"),
					("Weight", "15 kg"),
					("Mounting", "Floor mounted"),
					("Alarm signalling", "Coloured lights and different sounds"),
				]),
				("Connectivity & power", [
					("Connectivity", "Ethernet; USB service port only"),
					("Mains", "100–240 V"),
					("Installation note", "One-cable Ethernet installation cited for data and power"),
					("Platform", "iSenseOS connected capability"),
				]),
			],
			"ideal_h": "Ideal for premium transparent interiors",
			"ideal_b": "Fashion, luxury retail, cosmetics, department stores, sports retail and premium boutiques that want plexiglass plus counting — not a steel frame.",
			"ideal_img": "sports-retail",
			"ideal_alt": "Sports retail with iL33",
			"pack": "Quoted Nedap iL33 Lumen antenna(s) and floor mounting kit",
			"faqs": [
				{"question": "Why do the lights shine upward?", "answer": "Nedap positions iL33 alarm lighting upward so store staff have a clearer view than side-facing beacons.", "sort_order": 1},
				{"question": "Does iL33 include people counting?", "answer": "Yes. Integrated customer counters are part of the Lumen series proposition on iL33.", "sort_order": 2},
				{"question": "Can Printechs install iL33 in KSA?", "answer": "Yes. We supply, install and support iL33 Lumen across Saudi fashion and premium retail.", "sort_order": 3},
			],
		},
	]


def fill_isenseos(media):
	slug = "nedap-isenseos"
	card = media["isenseos"]
	doc = get_or_create(slug, "Nedap iSenseOS", card)
	apply_identity(doc, slug=slug, display_name="Nedap iSenseOS – Connected EAS Platform", category_label="CONNECTED EAS PLATFORM")
	doc.tagline = "Turn EAS alarms into actionable retail security information."
	doc.short_description = (
		"iSenseOS is the software intelligence behind Nedap’s connected RF EAS. It lets Saudi retailers "
		"monitor health, learn from events and join EAS to the rest of the loss-prevention stack."
	)
	doc.long_description = (
		"<p>Standalone beeping does not stop shrink in omnichannel retail — it creates noise. "
		"iSenseOS is the operating system on Nedap RF EAS antennas that connects, monitors and "
		"learns from every event.</p>"
		"<p>Integrations can include CCTV and VMS bookmarks, text or voice notifications, customer "
		"counting, metal detection, physical I/O and APIs. For almost all integrations Nedap notes "
		"that middleware is not required.</p>"
		"<p>Sleep Mode lets supported systems stand by overnight. Nedap states the feature can run on "
		"more than 10,000 existing in-store EAS systems because iSenseOS updates remotely.</p>"
		+ _ksa_p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "Connected Nedap iSenseOS operations view"
	doc.hero_trust_chips = "Health & performance\nData & analytics\nCCTV / VMS / notifications\nSleep Mode on supported systems"
	doc.story_heading = "Beyond the beep — for every Nedap antenna"
	doc.visual_story_heading = "Monitor. Integrate. Act."
	doc.card_title = "iSenseOS"
	doc.card_summary = "Connected EAS platform for health monitoring, analytics and security integrations."
	doc.card_image = card
	doc.final_cta_heading = "Put iSenseOS behind your Nedap gates"
	doc.final_cta_description = "Printechs will map which integrations and monitoring views matter for your KSA stores."
	doc.meta_title = "Nedap iSenseOS Saudi Arabia | Connected EAS Platform | Printechs"
	doc.meta_description = (
		"Nedap iSenseOS in Saudi Arabia from Printechs. Connect RF EAS alarms to CCTV, staff "
		"notifications, counting, metal detection and remote system health."
	)
	doc.set("benefits", [
		{"icon": "cloud", "title": "Remote health & performance", "description": "See which antennas need attention before a store notices a dead gate.", "sort_order": 1},
		{"icon": "report", "title": "Data and analytics", "description": "Alarm, visitor and deactivation insight for LP and store operations.", "sort_order": 2},
		{"icon": "integration", "title": "Security ecosystem", "description": "CCTV/VMS, notifications, counting, metal detection and I/O — see Integrations.", "sort_order": 3},
		{"icon": "battery", "title": "Sleep Mode", "description": "Standby supported systems at night; remote updates reach existing estates.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Sleep Mode", "image": media["night-sleep"], "image_alt": "Night standby", "caption": "Energy saving after close.", "sort_order": 1},
		{"label": "Health", "image": media["tablet-health"], "image_alt": "System health", "caption": "Estate status on a tablet.", "sort_order": 2},
		{"label": "Operations", "image": media["security-ops"], "image_alt": "Security ops", "caption": "Alarms with camera context.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "cloud", "title": "Health", "description": "Remote monitor & update", "sort_order": 1},
		{"icon": "report", "title": "Analytics", "description": "Alarms · visitors · health", "sort_order": 2},
		{"icon": "integration", "title": "Connect", "description": "API · I/O · VMS", "sort_order": 3},
		{"icon": "battery", "title": "Sleep Mode", "description": "Overnight standby", "sort_order": 4},
	])
	set_specs(doc, [
		("Platform", [
			("Name", "Nedap iSenseOS"),
			("Role", "Operating system on Nedap RF EAS antennas"),
			("Purpose", "Connect, monitor and learn from EAS events"),
			("Sleep Mode", "Standby overnight on supported systems; remote update path"),
		]),
		("Capability areas", [
			("Integrations", "CCTV/VMS, notifications, counting, metal detection, I/O, API"),
			("Health & performance", "Remote identification and faster resolution of issues"),
			("Data & analytics", "Theft events, visitor traffic and system health"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Core Module",
			"heading": "Integrations, health and analytics",
			"body": (
				"Treat iSenseOS as three conversations: Integrations (what the alarm should trigger), "
				"Health & Performance (is the gate alive?), and Data & Analytics (what should LP change "
				"this week?). See the dedicated Integrations page for CCTV, notifications and I/O."
			),
			"image": media["tablet-health"],
			"image_alt": "iSenseOS health",
			"link_label": "EAS integrations",
			"link_href": "/products/nedap-eas-integrations",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": "iSenseOS connectivity on quoted Nedap antennas", "sort_order": 1},
		{"item_description": "Agreed integrations and monitoring scope", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Does every Nedap gate use iSenseOS?", "answer": "Nedap states that its RF EAS antennas run on iSenseOS — that is the connected layer behind the hardware pages.", "sort_order": 1},
		{"question": "What is Sleep Mode?", "answer": "A standby mode for supported systems at night to save energy, rolled out remotely via iSenseOS — including many existing installations.", "sort_order": 2},
		{"question": "Can Printechs configure iSenseOS in KSA?", "answer": "Yes. We include platform setup, health views and agreed integrations in the installation scope.", "sort_order": 3},
	])
	return save_product(doc)


def fill_labels(media):
	slug = "nedap-rf-eas-labels"
	card = media["labels"]
	doc = get_or_create(slug, "Nedap RF EAS Labels", card)
	apply_identity(doc, slug=slug, display_name="Nedap RF EAS Labels – Power, Cool and Beauty", category_label="RF EAS LABELS")
	doc.tagline = "The right 8.2 MHz label for dry, chilled and beauty merchandise."
	doc.short_description = (
		"Nedap RF labels protect merchandise so shoppers can deactivate at checkout instead of waiting "
		"for a hard-tag removal. Power, Cool and Beauty cover dry, chilled and cosmetic packs."
	)
	doc.long_description = (
		"<p>Gates only detect what is labelled. Printechs specifies Nedap RF labels with the antenna "
		"and deactivator so Saudi grocery, fashion and beauty programmes do not mix the wrong tag "
		"with the wrong product.</p>"
		"<p><strong>Power Labels</strong> are for regular dry products such as boxes, cartons and "
		"bottles. Nedap states they are tested 100% of the time against a minimum performance level, "
		"and they work with standard <strong>8.2 MHz</strong> RF systems.</p>"
		"<p><strong>Cool Labels</strong> are for chilled and frozen products such as meat, fish and "
		"cheese — where humidity, temperature and packaging change how a standard label behaves.</p>"
		"<p><strong>Beauty Labels</strong> address small, curved or metal-influenced cosmetic packs "
		"where a generic label will not sit or detect reliably.</p>"
		+ _ksa_p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "Nedap RF EAS security labels"
	doc.hero_trust_chips = "8.2 MHz RF labels\nPower · Cool · Beauty\n100% tested Power Labels\nSource tagging support"
	doc.story_heading = "Label the merchandise. Then the gate can work."
	doc.visual_story_heading = "Dry, chilled and beauty"
	doc.card_title = "RF EAS Labels"
	doc.card_summary = "8.2 MHz Power, Cool and Beauty RF security labels for Saudi retail merchandise."
	doc.card_image = card
	doc.final_cta_heading = "Specify labels with the antennas"
	doc.final_cta_description = "Tell Printechs the category mix — fashion, grocery or beauty — and we will quote the right Nedap RF labels."
	doc.meta_title = "RF Security Labels Saudi Arabia | 8.2 MHz EAS Labels | Printechs"
	doc.meta_description = (
		"Nedap RF EAS labels in Saudi Arabia from Printechs. 8.2 MHz Power, Cool and Beauty labels "
		"for dry, chilled and cosmetic merchandise."
	)
	doc.set("benefits", [
		{"icon": "consumables", "title": "Power Labels for dry goods", "description": "Boxes, cartons and bottles on standard 8.2 MHz RF — 100% tested, says Nedap.", "sort_order": 1},
		{"icon": "inventory", "title": "Cool Labels for cold chain", "description": "Specified for chilled and frozen meat, fish and cheese conditions.", "sort_order": 2},
		{"icon": "store", "title": "Beauty Labels", "description": "Small, curved or metal-influenced cosmetic packs that defeat generic tags.", "sort_order": 3},
		{"icon": "checkout", "title": "Deactivate, don’t remove", "description": "Labels stay on the pack; 360° deactivation clears them at SCO or staffed POS.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Apparel", "image": media["apparel-labels"], "image_alt": "Apparel RF labels", "caption": "Dry merchandise and source tagging.", "sort_order": 1},
		{"label": "Chilled", "image": media["chilled-labels"], "image_alt": "Cool labels", "caption": "Cold-chain packs need Cool Labels.", "sort_order": 2},
		{"label": "Beauty", "image": media["beauty-labels"], "image_alt": "Beauty labels", "caption": "Tiny packs, reliable RF.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "shield", "title": "Frequency", "description": "Standard 8.2 MHz RF", "sort_order": 1},
		{"icon": "consumables", "title": "Power", "description": "Dry merchandise", "sort_order": 2},
		{"icon": "inventory", "title": "Cool", "description": "Chilled / frozen", "sort_order": 3},
		{"icon": "store", "title": "Beauty", "description": "Health & cosmetics", "sort_order": 4},
	])
	set_specs(doc, [
		("Label families", [
			("Power Labels", "RF labels for regular dry products; compatible with standard 8.2 MHz RF"),
			("Cool Labels", "Designed for chilled and frozen products such as meat, fish and cheese"),
			("Beauty Labels", "For compact, curved or metal-influenced health and beauty packs"),
			("Testing", "Nedap states Power Labels are tested 100% of the time"),
		]),
		("Programme options", [
			("Visibility", "Invisible labels or visual deterrents, including custom designs"),
			("Microwave", "Microwave-tested label options where misuse risk exists"),
			("Source tagging", "In-store, DC and supplier tagging programmes with training"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Labels that match Saudi grocery and fashion",
			"body": (
				"A supermarket in Riyadh cannot use the same label on a freezer pack and a carton of "
				"oil. We specify Power versus Cool versus Beauty with deactivation and the antenna, "
				"then train tagging teams or support source tagging with suppliers."
			),
			"image": media["chilled-labels"],
			"image_alt": "Chilled RF labels",
			"link_label": "360° deactivation",
			"link_href": "/products/nedap-eas-deactivation",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": "Quoted Power, Cool and/or Beauty RF label volumes", "sort_order": 1},
		{"item_description": "Tagging guidance or source-tagging support as agreed", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Are these 8.2 MHz labels?", "answer": "Yes. Nedap Power Labels are specified for standard 8.2 MHz RF EAS systems.", "sort_order": 1},
		{"question": "What is the difference between Power and Cool?", "answer": "Power is for dry merchandise. Cool is for chilled and frozen products where standard labels lose performance.", "sort_order": 2},
		{"question": "Can Printechs supply labels in KSA?", "answer": "Yes. We quote labels with the gates and deactivators and can support in-store or source tagging.", "sort_order": 3},
	])
	return save_product(doc)


def fill_deactivation(media):
	slug = "nedap-eas-deactivation"
	card = media["deactivator"]
	doc = get_or_create(slug, "Nedap 360° Deactivation", card)
	apply_identity(doc, slug=slug, display_name="Nedap 360° Deactivation – Smart RF Deactivator", category_label="EAS DEACTIVATION")
	doc.tagline = "Deactivate live RF labels at staffed and self-checkout."
	doc.short_description = (
		"Nedap 360° Deactivation uses the Smart Deactivator so paid merchandise leaves quietly — "
		"labels in any orientation, one burst when a live label is found."
	)
	doc.long_description = (
		"<p>If labels stay live after payment, honest shoppers set off the gate. Nedap’s 360° "
		"Deactivation is the checkout half of Connected RF EAS: a Smart Deactivator for staffed "
		"lanes and self-checkout.</p>"
		"<p>A special detect mode fires <strong>one strong burst</strong> only when a live RF label "
		"is present — saving energy versus continuous pulsing. Labels are detected in any position, "
		"so orientation at the scanner matters less.</p>"
		"<p>Nedap positions the solution as plug-and-play for common SCO platforms, including "
		"technology from Zebra, Datalogic, Toshiba, NCR, Diebold Nixdorf and Pan Oston. It connects "
		"to Nedap’s analytics, supports wireless synchronisation, and offers audio/visual feedback.</p>"
		+ _ksa_p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "Nedap RF label deactivation pad"
	doc.hero_trust_chips = "360° label detection\nBurst only when live\nStaffed POS and SCO\nAnalytics connected"
	doc.story_heading = "Paid goods should not beep at the door"
	doc.visual_story_heading = "Deactivate at the scanner"
	doc.card_title = "360° Deactivation"
	doc.card_summary = "Smart RF deactivator for staffed and self-checkout — 360° detect, one burst when live."
	doc.card_image = card
	doc.final_cta_heading = "Add deactivation to your Nedap EAS project"
	doc.final_cta_description = "Printechs will match the Smart Deactivator to your POS or SCO stack and label mix."
	doc.meta_title = "Nedap 360° EAS Deactivation Saudi Arabia | Printechs"
	doc.meta_description = (
		"Nedap 360° RF deactivation in Saudi Arabia from Printechs. Smart Deactivator for "
		"supermarket POS and self-checkout with 8.2 MHz labels."
	)
	doc.set("benefits", [
		{"icon": "checkout", "title": "Staffed and SCO", "description": "The same deactivation idea at conventional tills and self-checkout zones.", "sort_order": 1},
		{"icon": "scan", "title": "Any label orientation", "description": "Detect mode finds live RF labels flat, side-on or angled.", "sort_order": 2},
		{"icon": "battery", "title": "Burst only when live", "description": "One targeted burst when a live label is detected — not constant RF noise.", "sort_order": 3},
		{"icon": "integration", "title": "Common SCO platforms", "description": "Nedap cites Zebra, Datalogic, Toshiba, NCR, Diebold Nixdorf and Pan Oston.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "POS pad", "image": media["deactivation-pad"], "image_alt": "POS deactivator", "caption": "Clear the label at the grocery scanner.", "sort_order": 1},
		{"label": "SCO", "image": media["sco-deactivator"], "image_alt": "SCO deactivator", "caption": "Self-checkout without a second process.", "sort_order": 2},
		{"label": "Fashion till", "image": media["fashion-till-pad"], "image_alt": "Fashion deactivator", "caption": "Soft-tag fashion at the cash wrap.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "scan", "title": "Detection", "description": "360° live-label detect", "sort_order": 1},
		{"icon": "checkout", "title": "Use", "description": "POS and SCO", "sort_order": 2},
		{"icon": "report", "title": "Data", "description": "Analytics connected", "sort_order": 3},
		{"icon": "display", "title": "Feedback", "description": "Audio and visual", "sort_order": 4},
	])
	set_specs(doc, [
		("System", [
			("Name", "Nedap 360° Deactivation · Smart Deactivator"),
			("Function", "Deactivate live RF labels at checkout"),
			("Detect mode", "One strong burst when a live RF label is detected"),
			("Orientation", "Labels detected in any position"),
		]),
		("Checkout fit", [
			("Staffed POS", "Integrated at conventional cashier lanes"),
			("Self-checkout", "Plug-and-play positioning for common SCO systems"),
			("Cited SCO brands", "Zebra, Datalogic, Toshiba, NCR, Diebold Nixdorf, Pan Oston"),
			("Operations", "Wireless synchronisation, audio/visual, analytics"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Industry Solution",
			"heading": "Deactivation for KSA grocery SCO projects",
			"body": (
				"Self-checkout only works if paid labels die at the kiosk. We specify the Smart "
				"Deactivator with your SCO vendor, Nedap labels and the exit antenna so honest "
				"shoppers are not stopped at the door."
			),
			"image": media["sco-deactivator"],
			"image_alt": "SCO deactivation",
			"link_label": "RF EAS labels",
			"link_href": "/products/nedap-rf-eas-labels",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": "Quoted Smart Deactivator / 360° deactivation hardware", "sort_order": 1},
		{"item_description": "POS or SCO integration scope as surveyed", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Does it work with 8.2 MHz labels?", "answer": "It is the deactivation half of Nedap’s RF EAS proposition and is specified with Nedap RF labels.", "sort_order": 1},
		{"question": "Can it integrate with our SCO?", "answer": "Nedap lists major SCO vendors. Printechs confirms the exact stack during the site survey.", "sort_order": 2},
		{"question": "Do you install deactivators in KSA?", "answer": "Yes — with the antennas and labels, including grocery SCO programmes.", "sort_order": 3},
	])
	return save_product(doc)


def fill_integrations(media):
	slug = "nedap-eas-integrations"
	card = media["integrations"]
	doc = get_or_create(slug, "Nedap EAS Integrations", card)
	apply_identity(doc, slug=slug, display_name="Nedap EAS Integrations – CCTV, Alerts and Counting", category_label="EAS INTEGRATIONS")
	doc.tagline = "Connect every alarm to the next action your team already uses."
	doc.short_description = (
		"iSenseOS integrations turn RF EAS into store security intelligence: CCTV/VMS bookmarks, "
		"staff notifications, customer counting, metal detection and physical I/O."
	)
	doc.long_description = (
		"<p>An alarm is only useful if someone sees the right camera, gets a message, or can trust "
		"the gate. iSenseOS integrations are how Nedap RF EAS joins the systems Saudi retailers "
		"already run.</p>"
		"<p>Connect through software triggers and APIs, or through physical inputs and outputs when "
		"the store network is isolated. Nedap notes that almost all integrations need no middleware.</p>"
		"<p>Typical outcomes: bookmark the VMS at the moment of the event, notify a supervisor’s "
		"phone, enrich visitor analytics, detect booster bags with metal detection, or fire a "
		"shutter/IO action. Deep platform context lives on "
		"<a href=\"/products/nedap-isenseos\">iSenseOS</a>.</p>"
		+ _ksa_p()
	)
	doc.hero_image = card
	doc.hero_image_alt = "Connected retail security ecosystem"
	doc.hero_trust_chips = "CCTV / VMS bookmarks\nStaff smartphone alerts\nCustomer counting\nMetal detection & I/O"
	doc.story_heading = "The alarm should start a workflow"
	doc.visual_story_heading = "Video, people, metal, messages"
	doc.card_title = "EAS Integrations"
	doc.card_summary = "Connect Nedap RF EAS to CCTV/VMS, staff alerts, counting and metal detection."
	doc.card_image = card
	doc.final_cta_heading = "Integrate Nedap EAS with your security stack"
	doc.final_cta_description = "Tell Printechs which VMS, radios and counting tools you already use — we will scope the iSenseOS connections."
	doc.meta_title = "Nedap EAS Integrations Saudi Arabia | CCTV VMS Counting | Printechs"
	doc.meta_description = (
		"Connect Nedap RF EAS in Saudi Arabia to CCTV, VMS, staff notifications, customer "
		"counting and metal detection through iSenseOS. Supplied by Printechs."
	)
	doc.set("benefits", [
		{"icon": "integration", "title": "CCTV and VMS", "description": "Send bookmarks, alerts and triggers so teams find the recording with the alarm.", "sort_order": 1},
		{"icon": "device", "title": "Staff notifications", "description": "Push events to smartphones or voice headsets instead of hoping someone heard the gate.", "sort_order": 2},
		{"icon": "report", "title": "Customer counting", "description": "Integrated or advanced external counters enrich traffic and conversion views.", "sort_order": 3},
		{"icon": "shield", "title": "Metal detection & I/O", "description": "Detect booster bags at the entrance and drive physical actions on isolated networks.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "VMS", "image": media["vms-wall"], "image_alt": "VMS wall", "caption": "Find the camera moment that matches the gate.", "sort_order": 1},
		{"label": "Staff alert", "image": media["staff-phone"], "image_alt": "Staff phone", "caption": "Notify the person already on the floor.", "sort_order": 2},
		{"label": "Metal detection", "image": media["metal-detect"], "image_alt": "Metal detection", "caption": "Booster-bag risk at the same entrance.", "sort_order": 3},
	])
	doc.set("icon_specifications", [
		{"icon": "integration", "title": "Video", "description": "CCTV / VMS bookmarks", "sort_order": 1},
		{"icon": "device", "title": "Notify", "description": "Phone and voice alerts", "sort_order": 2},
		{"icon": "report", "title": "Count", "description": "Visitor counters", "sort_order": 3},
		{"icon": "shield", "title": "Detect", "description": "Metal detection · I/O", "sort_order": 4},
	])
	set_specs(doc, [
		("Integration methods", [
			("Software", "Triggers, APIs and web sockets for local integration"),
			("Physical I/O", "Input/output signals for isolated networks or shutters"),
			("Middleware", "Nedap states almost all integrations need no middleware"),
			("Platform", "iSenseOS on Nedap RF EAS antennas"),
		]),
		("Typical connections", [
			("CCTV / VMS", "Bookmarks, alerts and triggers to start or find recordings"),
			("Notifications", "Push to smart devices; optional AI voice headsets"),
			("Customer counting", "Integrated or advanced external counters"),
			("Metal detection", "Integrated or advanced external metal detection"),
			("Add-ons", "I/O boxes and RFID upgrades when a project specifies them"),
		]),
	])
	doc.set("applications", scene_apps(media, slug))
	doc.set("content_sections", [
		{
			"section_type": "Core Module",
			"heading": "What we connect in Saudi stores",
			"body": (
				"Most KSA projects start with VMS bookmarks and a supervisor notification. "
				"Grocery groups often add counting and metal detection at the same entrance. "
				"We confirm the camera vendor, radio/PDA estate and whether the store can use "
				"API or needs dry-contact I/O."
			),
			"image": media["vms-wall"],
			"image_alt": "Retail VMS wall",
			"link_label": "iSenseOS platform",
			"link_href": "/products/nedap-isenseos",
			"sort_order": 1,
		},
		ksa_section(media, slug, 2),
	])
	doc.set("support_items", support_items())
	doc.set("package_contents", [
		{"item_description": "Agreed iSenseOS integrations scoped against your VMS and devices", "sort_order": 1},
		{"item_description": "Commissioning and store-team briefing", "sort_order": 2},
	])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])
	doc.set("faq_items", [
		{"question": "Do we need extra middleware?", "answer": "Nedap states that almost all iSenseOS integrations need no middleware. We still confirm your VMS and network during survey.", "sort_order": 1},
		{"question": "Can you connect our existing CCTV?", "answer": "That is a primary use. We bookmark or trigger the VMS you already operate whenever the interface is supported.", "sort_order": 2},
		{"question": "Is metal detection a separate pedestal?", "answer": "Nedap integrates metal detection into EAS antennas on supported configurations. We confirm the option per model.", "sort_order": 3},
	])
	return save_product(doc)


def fill_nedap_eas():
	media = prepare_media()
	fill_hub(media)
	for cfg in gate_configs(media):
		_gate_page(media, cfg)
	fill_isenseos(media)
	fill_labels(media)
	fill_deactivation(media)
	fill_integrations(media)
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
	print("Wired Nedap related products and brand")
	return "ok"


def _update_brand(media):
	from printechs_digital.setup.nedap_common import install_logo

	logo = media.get("logo") or install_logo()
	name = frappe.db.get_value("Website Brand", {"slug": "nedap"}, "name")
	doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
	if not frappe.db.exists("Brand", "Nedap"):
		frappe.throw("ERP Brand Nedap was not found")
	doc.brand = "Nedap"
	doc.display_name = "Nedap"
	doc.slug = "nedap"
	doc.logo = logo
	doc.summary = (
		"Connected RF EAS gates, labels, 360° deactivation and iSenseOS for Saudi fashion, "
		"supermarket and self-checkout stores — supplied and installed by Printechs."
	)
	doc.sort_order = 7
	doc.published = 1
	doc.meta_title = "Nedap EAS Saudi Arabia | RF Anti-Theft Gates | Printechs Brands"
	doc.meta_description = (
		"Nedap RF EAS systems, iSenseOS, labels and deactivation from Printechs in Saudi Arabia. "
		"Fashion, supermarket, department and self-checkout security."
	)
	doc.flags.ignore_permissions = True
	if name:
		doc.save()
	else:
		doc.insert()
	frappe.db.commit()
