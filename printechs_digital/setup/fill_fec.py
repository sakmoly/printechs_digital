# Copyright (c) 2026, Printechs and contributors
"""FEC POS brand, hub, family pages and first-batch product pages."""

import frappe

from printechs_digital.setup.fec_common import (
	KSA_BODY,
	app_row,
	apply_identity,
	get_or_create,
	panel_h610_quote_options,
	prepare_media,
	q_check,
	q_select,
	save_product,
	set_related,
	set_specs,
	support_items,
	update_website_brand,
	xpos_quote_options,
)

RELATED = {
	"fec-pos-systems": [
		"fec-pos-terminals",
		"fec-panel-pc",
		"fec-xelf-ii",
		"fec-kitchen-display",
		"fec-box-pc",
		"fec-touch-monitors",
		"fec-pos-peripherals",
	],
	"fec-pos-terminals": ["fec-xp-4765w", "fec-xp-3765w", "fec-xp-4765", "fec-xp-3765", "fec-st-1130w"],
	"fec-panel-pc": ["fec-pp-9745w", "fec-pp-9735w", "fec-pp-9815w"],
	"fec-self-service-kiosk": ["fec-xelf-ii"],
	"fec-kitchen-display": ["fec-kp-9795w", "fec-kp-9155w"],
	"fec-box-pc": ["fec-xc-574", "fec-xc-373"],
	"fec-touch-monitors": ["fec-ld-9043w"],
	"fec-pos-peripherals": ["fec-tp-100"],
	"fec-xp-4765w": ["fec-xp-3765w", "fec-xp-4765", "fec-xelf-ii", "fec-tp-100"],
	"fec-xp-3765w": ["fec-xp-4765w", "fec-xp-3765", "fec-st-1130w"],
	"fec-xp-4765": ["fec-xp-4765w", "fec-xp-3765", "fec-pp-9745w"],
	"fec-xp-3765": ["fec-xp-3765w", "fec-xp-4765", "fec-st-1130w"],
	"fec-st-1130w": ["fec-xp-3765w", "fec-xelf-ii", "fec-tp-100"],
	"fec-xelf-ii": ["fec-xp-4765w", "fec-kp-9795w", "fec-ld-9043w"],
	"fec-pp-9745w": ["fec-pp-9735w", "fec-pp-9815w", "fec-xp-4765w"],
	"fec-pp-9735w": ["fec-pp-9745w", "fec-pp-9815w", "fec-xc-373"],
	"fec-pp-9815w": ["fec-pp-9745w", "fec-pp-9735w", "fec-xelf-ii"],
	"fec-kp-9795w": ["fec-kp-9155w", "fec-ld-9043w", "fec-xelf-ii"],
	"fec-kp-9155w": ["fec-kp-9795w", "fec-st-1130w", "fec-xelf-ii"],
	"fec-xc-574": ["fec-xc-373", "fec-pp-9745w", "fec-ld-9043w"],
	"fec-xc-373": ["fec-xc-574", "fec-pp-9735w", "fec-tp-100"],
	"fec-ld-9043w": ["fec-xelf-ii", "fec-kp-9795w", "fec-xp-4765w"],
	"fec-tp-100": ["fec-xp-4765w", "fec-xelf-ii", "fec-st-1130w"],
}


def _p(media, slug, display, subcategory, category_label, *, hero, card, tagline, short, long,
		chips, story, visual, card_title, card_summary, cta_h, cta_d, meta_t, meta_d,
		benefits, stories, icons, specs, apps, sections, faqs, quote=None, on_list=True,
		featured=0, is_hub=0, configure=0, pack=None):
	doc = get_or_create(slug, display, hero, subcategory)
	apply_identity(
		doc,
		slug=slug,
		display_name=display,
		subcategory=subcategory,
		category_label=category_label,
		on_list=on_list,
		featured=featured,
		is_hub=is_hub,
		configure=1 if (configure or quote) else 0,
	)
	doc.tagline = tagline
	doc.short_description = short
	doc.long_description = long
	doc.hero_image = hero
	doc.hero_image_alt = display
	doc.hero_trust_chips = chips
	doc.story_heading = story
	doc.visual_story_heading = visual
	doc.card_title = card_title
	doc.card_summary = card_summary
	doc.card_image = card
	doc.final_cta_heading = cta_h
	doc.final_cta_description = cta_d
	doc.meta_title = meta_t
	doc.meta_description = meta_d
	doc.set("benefits", benefits)
	doc.set("visual_story_items", stories)
	doc.set("icon_specifications", icons)
	set_specs(doc, specs)
	doc.set("applications", apps)
	doc.set("content_sections", sections)
	doc.set("support_items", support_items())
	doc.set("faq_items", faqs)
	doc.set("quote_options", quote or [])
	doc.set("package_contents", pack or [{"item_description": f"{display} as quoted", "sort_order": 1}])
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	return save_product(doc)


def _integration_section(image, alt, sort=2):
	return {
		"section_type": "Core Module",
		"heading": "Complete POS solution integration",
		"body": (
			"FEC terminals can form the hardware foundation of Printechs Modern POS — "
			"centralized items, pricing, promotions, loyalty, e-wallets, multi-payment "
			"workflows and ERPNext inventory, purchasing, customer and sales management. "
			"Add barcode scanners, receipt printers, customer displays, cash drawers, "
			"payment terminals, RFID and electronic shelf labels as the store requires."
		),
		"image": image,
		"image_alt": alt,
		"link_label": "Modern POS",
		"link_href": "/software/modern-pos",
		"sort_order": sort,
	}


def _ksa_section(image, alt, sort=3):
	return {
		"section_type": "Industry Solution",
		"heading": "Why Printechs in Saudi Arabia",
		"body": KSA_BODY,
		"image": image,
		"image_alt": alt,
		"link_label": "ERPNext Retail",
		"link_href": "/software/erpnext",
		"sort_order": sort,
	}


def fill_hub(m):
	_p(
		m,
		"fec-pos-systems",
		"FEC POS Systems & Intelligent Commerce Solutions in Saudi Arabia",
		"POS Systems",
		"FEC POS HARDWARE",
		hero=m["hub"],
		card=m["hub"],
		tagline="Reliable POS Hardware for Retail, Hospitality & Enterprise Operations",
		short=(
			"Printechs provides FEC POS hardware and intelligent commerce solutions for businesses "
			"across Saudi Arabia. The FEC portfolio combines modern industrial design, commercial-grade "
			"computing and flexible peripheral integration for demanding retail, hospitality, "
			"self-service and enterprise environments."
		),
		long=(
			"<p>From all-in-one POS terminals and modular panel PCs to self-service kiosks, kitchen "
			"displays, box PCs, touch monitors and peripherals, FEC provides a flexible hardware "
			"platform for building complete customer-facing and operational solutions.</p>"
			"<p>FEC — Firich Enterprises Co., Ltd. — positions its current catalogue around XPOS Plus "
			"POS terminals, XPPC panel PCs, XELF II self-service kiosks, KP kitchen panel PCs, "
			"XCOMP box systems, XMonitor displays and POS peripherals for retail, hospitality, "
			"healthcare and other service-driven environments.</p>"
			f"<p>{KSA_BODY}</p>"
		),
		chips="XPOS Plus · XPPC · XELF II\nKP kitchen · XCOMP · XMonitor\nPOS peripherals\nRiyadh · Jeddah · Dammam",
		story="Seven FEC families for checkout, self-service and back-of-house",
		visual="FEC solutions by industry",
		card_title="FEC POS Systems",
		card_summary="POS terminals, panel PCs, kiosks, kitchen displays, box PCs, monitors and peripherals from FEC.",
		cta_h="Specify FEC hardware for your stores",
		cta_d="Talk to a POS hardware specialist about XPOS Plus, XPPC, XELF II, KP, XCOMP, displays and peripherals.",
		meta_t="FEC POS Systems Saudi Arabia | POS Terminals, Kiosks & Panel PCs | Printechs",
		meta_d="Discover FEC POS systems in Saudi Arabia from Printechs, including touch POS terminals, panel PCs, self-service kiosks, kitchen displays, monitors, box PCs and POS peripherals.",
		benefits=[
			{"icon": "checkout", "title": "FEC XPOS Plus — all-in-one POS terminals", "description": "Modern commercial POS terminals for checkout counters that need reliability, processing performance and flexible peripheral integration. XPOS Plus combines a touchscreen computer with an intelligently designed stand and managed I/O.", "sort_order": 1},
			{"icon": "display", "title": "FEC XPPC — panel PCs", "description": "Commercial touchscreen panel computers for POS, kiosks, information terminals, operator stations and embedded applications — across screen sizes, processors and Windows/Android configurations.", "sort_order": 2},
			{"icon": "store", "title": "FEC XELF II — self-service kiosk", "description": "A modular self-service platform for order, check-in, check-out, payment and unattended service without a staffed counter.", "sort_order": 3},
			{"icon": "durability", "title": "FEC KP — kitchen display panel PCs", "description": "Commercial touchscreen computers specified for heat-resilient, high-pressure kitchen and food-service operations.", "sort_order": 4},
			{"icon": "device", "title": "FEC XCOMP — box PCs", "description": "Compact commercial computers when the PC must be separated from the display — POS, kiosks, signage and control stations.", "sort_order": 5},
			{"icon": "print", "title": "XMonitor, large displays and peripherals", "description": "Touch monitors including 22\", 32\" and 42/43\" models, plus TP-100 and MSR, RFID and fingerprint modules to complete the workstation.", "sort_order": 6},
		],
		stories=[
			{"label": "Fashion & apparel", "image": m["app_fashion"], "image_alt": "Fashion retail checkout", "caption": "Modern touch POS terminals and customer displays for multi-store fashion retailers.", "sort_order": 1},
			{"label": "Supermarkets & grocery", "image": m["app_grocery"], "image_alt": "Grocery retail", "caption": "POS workstations, touchscreen terminals, receipt printers and self-checkout infrastructure.", "sort_order": 2},
			{"label": "Food service & QSR", "image": m["app_qsr"], "image_alt": "Restaurant service", "caption": "Kitchen display panel PCs and self-service ordering infrastructure.", "sort_order": 3},
		],
		icons=[
			{"icon": "checkout", "title": "XPOS Plus", "description": "All-in-one touch POS", "sort_order": 1},
			{"icon": "display", "title": "XPPC", "description": "Panel PCs for POS & kiosk", "sort_order": 2},
			{"icon": "store", "title": "XELF II", "description": "Modular self-service", "sort_order": 3},
			{"icon": "durability", "title": "KP / XCOMP", "description": "Kitchen & box PCs", "sort_order": 4},
		],
		specs=[
			("Portfolio", [
				("Brand", "FEC (Firich Enterprises Co., Ltd.)"),
				("Positioning", "Intelligent commerce / POS hardware"),
				("Families", "XPOS Plus, XPPC, XELF II, KP, XCOMP, XMonitor, peripherals"),
				("Typical OS", "Windows IoT Enterprise or Android, by model"),
				("Supplied by", "Printechs Saudi Arabia"),
			]),
		],
		apps=[
			app_row(m, "fashion", "Fashion & apparel", "Modern touch POS terminals and customer displays for multi-store fashion retailers.", "Fashion store POS", "fashion", 1),
			app_row(m, "grocery", "Supermarkets & grocery", "POS workstations, touchscreen terminals, receipt printers and self-checkout infrastructure.", "Supermarket checkout", "retail", 2),
			app_row(m, "pharmacy", "Pharmacy & healthcare retail", "Compact touchscreen POS hardware for pharmacy and healthcare retail workflows.", "Pharmacy retail", "pharmaceutical", 3),
			app_row(m, "beauty", "Beauty & cosmetics", "Low-profile POS hardware for premium beauty and cosmetics stores.", "Cosmetics retail", "retail", 4),
			app_row(m, "hospitality", "Hospitality", "POS terminals, self-service kiosks and touchscreen systems for hotels, cafés and hospitality.", "Hotel lobby", "hospitality", 5),
			app_row(m, "qsr", "Food service & QSR", "Kitchen display panel PCs and self-service ordering infrastructure.", "QSR restaurant", "food-beverage", 6),
			app_row(m, "enterprise", "Enterprise self-service", "Kiosks and panel PCs for queueing, registration, information and customer interaction.", "Enterprise lobby kiosk", "retail", 7),
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "FEC POS Systems, Self-Service Kiosks & Commercial Touch Solutions", "body": "FEC POS Solutions from Printechs Saudi Arabia. Start with the families that match the project — then configure processor, OS and peripherals on the quote.", "image": m["src_hub-banner"], "image_alt": "FEC commercial hardware", "sort_order": 1},
			_integration_section(m["app_grocery"], "Retail POS software integration"),
			_ksa_section(m["app_hospitality"], "Hospitality and retail operations in Saudi Arabia"),
		],
		faqs=[
			{"question": "Is Printechs an FEC partner in Saudi Arabia?", "answer": "Printechs supplies and supports FEC POS hardware in Saudi Arabia. We specify the family, configure the machine and integrate Modern POS, ERPNext and peripherals.", "sort_order": 1},
			{"question": "Which FEC family should we start with?", "answer": "XPOS Plus for attended checkout, XPPC for compact or embedded touch PCs, XELF II for unattended journeys, KP for kitchens, XCOMP when the PC is separate from the display, and XMonitor or TP-100 to complete the station.", "sort_order": 2},
			{"question": "Can we configure processor, memory and OS on the quote?", "answer": "Yes. Individual FEC product pages open a configurable quotation form so you can choose published processor, memory, OS and optional modules before the sales team responds.", "sort_order": 3},
		],
		on_list=True,
		featured=1,
		is_hub=1,
	)


def fill_families(m):
	_p(
		m, "fec-pos-terminals", "FEC XPOS Plus All-in-One POS Terminals", "POS Terminals", "XPOS PLUS",
		hero=m["xpos"], card=m["xpos"],
		tagline="Touch POS terminals with modular docking and managed I/O",
		short="Modern commercial POS terminals designed for checkout counters requiring reliability, processing performance and flexible peripheral integration.",
		long="<p>XPOS Plus combines a touchscreen computer with an intelligently designed stand and managed I/O connectivity. FEC currently lists XP-3765, XP-3765W, XP-4765 and XP-4765W in this family, plus the compact Android ST-1130W smart terminal.</p><p>Best for fashion stores, supermarkets, pharmacies, specialty retail, department stores and service counters.</p>",
		chips="XP-4765W · XP-3765W\nXP-4765 · XP-3765\nST-1130W Android\nModular docking I/O",
		story="Choose the XPOS Plus form factor", visual="XPOS Plus at the counter",
		card_title="XPOS Plus Terminals", card_summary="All-in-one FEC touch POS terminals for attended retail checkout.",
		cta_h="Configure an XPOS Plus terminal", cta_d="Select XP-4765W, XP-3765W or ST-1130W and choose processor, OS and peripherals.",
		meta_t="FEC XPOS Plus POS Terminals Saudi Arabia | Touch POS | Printechs",
		meta_d="FEC XPOS Plus all-in-one POS terminals for retail checkout in Saudi Arabia. XP-4765W, XP-3765W, XP-4765, XP-3765 and ST-1130W from Printechs.",
		benefits=[
			{"icon": "checkout", "title": "Attended checkout", "description": "Built for fashion, grocery, pharmacy and specialty counters.", "sort_order": 1},
			{"icon": "device", "title": "Modular stand I/O", "description": "Cable management and cash-drawer, USB, COM, LAN and video connections in the dock.", "sort_order": 2},
			{"icon": "android", "title": "Windows or Android", "description": "XPOS Plus Windows IoT models plus ST-1130W Android smart POS.", "sort_order": 3},
		],
		stories=[
			{"label": "Widescreen POS", "image": m["src_xp-4765w-b"], "image_alt": "FEC XP-4765W", "caption": "15.6-inch XPOS Plus for modern counters.", "sort_order": 1},
			{"label": "Fashion", "image": m["app_fashion"], "image_alt": "Fashion POS", "caption": "Clean counter installation.", "sort_order": 2},
		],
		icons=[{"icon": "checkout", "title": "Family", "description": "XPOS Plus + ST-1130W", "sort_order": 1}],
		specs=[("Family", [("Models in this batch", "XP-4765W, XP-3765W, XP-4765, XP-3765, ST-1130W"), ("Use", "Attended retail and hospitality POS")])],
		apps=[app_row(m, "fashion", "Fashion & specialty", "Stylish POS with scanner, payment and customer display.", "Fashion POS", "fashion", 1),
		      app_row(m, "grocery", "Supermarket checkout", "Busy counters that need multiple peripherals.", "Grocery POS", "retail", 2)],
		sections=[_integration_section(m["app_fashion"], "Fashion POS"), _ksa_section(m["app_grocery"], "Grocery POS")],
		faqs=[{"question": "XP-4765W or XP-3765W?", "answer": "Both are XPOS Plus widescreen terminals. XP-4765W is the 15.6-inch performance model with published Intel Core options up to i7-12700. Confirm the live FEC datasheet for XP-3765W processor choices on the quote.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)
	_p(
		m, "fec-panel-pc", "FEC XPPC Panel PCs", "Panel PCs", "XPPC",
		hero=m["xppc"], card=m["xppc"],
		tagline="Commercial touchscreen panel computers for POS, kiosk and embedded use",
		short="XPPC lets integrators build compact installations without a traditional desktop POS form factor — across screen sizes, processors and Windows or Android.",
		long="<p>Best for retail counters, kiosks, healthcare, production terminals, queue systems and digital service points. This first batch publishes PP-9745W (H610 performance), PP-9735W (fanless J6412) and PP-9815W.</p>",
		chips="PP-9745W H610\nPP-9735W fanless J6412\nPP-9815W\nWindows / Android XPPC",
		story="Panel PCs instead of a boxed POS", visual="XPPC applications",
		card_title="XPPC Panel PCs", card_summary="FEC commercial panel PCs for POS, kiosk and embedded touch stations.",
		cta_h="Specify an XPPC", cta_d="Choose performance H610, fanless J6412 or PP-9815W and configure memory and OS.",
		meta_t="FEC XPPC Panel PC Saudi Arabia | Commercial Touch PCs | Printechs",
		meta_d="FEC XPPC panel PCs for POS, kiosks and commercial touchscreen applications in Saudi Arabia. PP-9745W, PP-9735W and PP-9815W from Printechs.",
		benefits=[{"icon": "display", "title": "All-in-one touch PC", "description": "Display and computer in one chassis for compact counters and kiosks.", "sort_order": 1},
		          {"icon": "durability", "title": "Fanless options", "description": "PP-9735W is the fanless 15.6-inch J6412 XPPC for quieter installs.", "sort_order": 2}],
		stories=[{"label": "Performance XPPC", "image": m["src_pp-9745w-a"], "image_alt": "PP-9745W", "caption": "H610-based 15.6-inch performance panel PC.", "sort_order": 1},
		         {"label": "Service point", "image": m["app_enterprise"], "image_alt": "Service terminal", "caption": "Queue and information terminals.", "sort_order": 2}],
		icons=[{"icon": "display", "title": "XPPC", "description": "POS · kiosk · embedded", "sort_order": 1}],
		specs=[("Family", [("First-batch models", "PP-9745W, PP-9735W, PP-9815W")])],
		apps=[app_row(m, "enterprise", "Service terminals", "Operator stations and queue systems.", "Service terminal", "retail", 1),
		      app_row(m, "pharmacy", "Healthcare retail", "Compact touch PCs at the counter.", "Pharmacy panel PC", "pharmaceutical", 2)],
		sections=[_integration_section(m["app_enterprise"], "Service terminal"), _ksa_section(m["app_pharmacy"], "Healthcare retail")],
		faqs=[{"question": "Panel PC or XPOS Plus?", "answer": "Use XPOS Plus when you want a retail dock with cash-drawer and managed I/O. Use XPPC when you need a VESA or embedded panel without a traditional POS stand.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)
	_p(
		m, "fec-self-service-kiosk", "FEC Self-Service Kiosks", "Self-Service Kiosks", "XELF",
		hero=m["xelf"], card=m["xelf"],
		tagline="Modular kiosks for checkout, ordering, hotel check-in and unattended service",
		short="FEC designed XELF II around configurable displays, peripherals and mounting so one architecture can cover several customer journeys.",
		long="<p>Start with XELF II for retail self-checkout, QSR ordering, hotel check-in, queueing and customer service. Older XELF pages are not published in this first batch.</p>",
		chips="XELF II modular\nSelf-checkout · ordering\nHotel check-in\nQueue & ticketing",
		story="One architecture, several journeys", visual="Self-service in retail and hospitality",
		card_title="Self-Service Kiosks", card_summary="FEC XELF II modular self-service kiosks for retail and hotels.",
		cta_h="Plan an XELF II deployment", cta_d="Tell us the journey — checkout, ordering, hotel or queue — and we will map display and peripherals.",
		meta_t="FEC Self-Service Kiosk Saudi Arabia | XELF II | Printechs",
		meta_d="FEC XELF II modular self-service kiosks for self-checkout, ordering, hotel check-in and unattended service in Saudi Arabia.",
		benefits=[{"icon": "store", "title": "Modular", "description": "Displays, peripherals and mounting arranged per site.", "sort_order": 1}],
		stories=[{"label": "XELF II", "image": m["src_xelf-ii-a"], "image_alt": "XELF II", "caption": "Modular self-service platform.", "sort_order": 1},
		         {"label": "Self-checkout", "image": m["app_selfservice"], "image_alt": "Self-checkout", "caption": "Scan, pay and leave.", "sort_order": 2}],
		icons=[{"icon": "store", "title": "XELF II", "description": "Retail · hotel · QSR", "sort_order": 1}],
		specs=[("Family", [("Lead model", "XELF II")])],
		apps=[app_row(m, "selfservice", "Retail self-checkout", "Scan, review and pay without a staffed lane.", "Self-checkout kiosk", "retail", 1),
		      app_row(m, "hospitality", "Hotel check-in", "Automated guest arrival and departure.", "Hotel kiosk", "hospitality", 2)],
		sections=[_integration_section(m["app_selfservice"], "Self-checkout"), _ksa_section(m["app_hospitality"], "Hotel kiosk")],
		faqs=[{"question": "Do you publish the older XELF?", "answer": "Not in this first batch. XELF II is the current modular platform we recommend.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)
	_p(
		m, "fec-kitchen-display", "FEC KP Kitchen Display Panel PCs", "Kitchen Displays", "KP SERIES",
		hero=m["kp"], card=m["kp"],
		tagline="Commercial kitchen touchscreens for KDS, QSR and food production",
		short="FEC describes the KP family around heat resilience and high-pressure kitchen operations. This batch includes Windows KP-9795W and Android KP-9155W.",
		long="<p>Best for kitchen display systems, QSR, cafeterias, cloud kitchens, food production and restaurant back-of-house systems.</p>",
		chips="KP-9795W Windows\nKP-9155W Android\nKDS / QSR\nKitchen-rated touch PCs",
		story="Windows or Android KDS hardware", visual="Kitchen operations",
		card_title="KP Kitchen Displays", card_summary="FEC KP kitchen panel PCs for restaurant KDS and food-service.",
		cta_h="Specify a kitchen display", cta_d="Choose Windows KP-9795W or Android KP-9155W and confirm mounting and KDS software.",
		meta_t="FEC Kitchen Display System Saudi Arabia | KP Series | Printechs",
		meta_d="FEC KP kitchen display panel PCs for restaurant KDS, QSR and food-service operations in Saudi Arabia. KP-9795W and KP-9155W from Printechs.",
		benefits=[{"icon": "durability", "title": "Kitchen first", "description": "Specified for heat and high-pressure food-service, not a generic office panel.", "sort_order": 1},
		          {"icon": "android", "title": "Windows or Android", "description": "KP-9795W Windows N-series / Core 3 options; KP-9155W MediaTek G700 Android.", "sort_order": 2}],
		stories=[{"label": "Windows KP", "image": m["src_kp-9795w-a"], "image_alt": "KP-9795W", "caption": "Windows kitchen panel PC.", "sort_order": 1},
		         {"label": "Kitchen", "image": m["app_kitchen"], "image_alt": "Commercial kitchen", "caption": "Order preparation and KDS.", "sort_order": 2}],
		icons=[{"icon": "durability", "title": "KP", "description": "Windows · Android KDS", "sort_order": 1}],
		specs=[("Family", [("Models", "KP-9795W, KP-9155W"), ("Use", "Kitchen Display Systems")])],
		apps=[app_row(m, "kitchen", "Kitchen Display System", "Order tickets and production status on a dedicated touch PC.", "Kitchen KDS", "food-beverage", 1),
		      app_row(m, "qsr", "QSR", "Fast-food and cafeteria lines.", "QSR kitchen", "food-beverage", 2)],
		sections=[_integration_section(m["app_qsr"], "QSR"), _ksa_section(m["app_kitchen"], "Kitchen KDS")],
		faqs=[{"question": "Windows or Android KDS?", "answer": "Match the KDS application. KP-9795W is the Windows kitchen panel PC; KP-9155W is the Android MediaTek G700 platform.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)
	_p(
		m, "fec-box-pc", "FEC XCOMP Box PCs", "Box PCs", "XCOMP",
		hero=m["xcomp"], card=m["xcomp"],
		tagline="Compact commercial computers when the PC is separate from the display",
		short="XCOMP is FEC's box-system family. This batch includes the higher-performance XC-574 H610 platform and the compact XC-373 J6412 platform.",
		long="<p>Best for POS systems, kiosks, digital signage, control stations and embedded commercial applications.</p>",
		chips="XC-574 H610\nXC-373 J6412\nPOS · kiosk · signage\nSeparate from the display",
		story="Put the computer where the display is not", visual="XCOMP platforms",
		card_title="XCOMP Box PCs", card_summary="FEC commercial box PCs for POS, kiosk and signage computers.",
		cta_h="Configure an XCOMP", cta_d="Choose XC-574 or XC-373 and set memory, storage and OS on the quote.",
		meta_t="FEC XCOMP Box PC Saudi Arabia | POS & Kiosk Computers | Printechs",
		meta_d="FEC XCOMP commercial box PCs for POS, kiosks and digital signage in Saudi Arabia. XC-574 H610 and XC-373 J6412 from Printechs.",
		benefits=[{"icon": "device", "title": "Separated compute", "description": "Hide the PC and use any FEC or third-party commercial display.", "sort_order": 1}],
		stories=[{"label": "XC-574", "image": m["src_xc-574-a"], "image_alt": "XC-574", "caption": "H610 performance box PC.", "sort_order": 1},
		         {"label": "Signage", "image": m["app_enterprise"], "image_alt": "Digital signage computer", "caption": "Kiosk and signage PCs.", "sort_order": 2}],
		icons=[{"icon": "device", "title": "XCOMP", "description": "H610 · J6412", "sort_order": 1}],
		specs=[("Family", [("Models", "XC-574, XC-373")])],
		apps=[app_row(m, "enterprise", "Embedded commercial PC", "Control stations and signage players.", "Box PC", "retail", 1),
		      app_row(m, "selfservice", "Kiosk computer", "Compute for unattended enclosures.", "Kiosk PC", "retail", 2)],
		sections=[_integration_section(m["app_enterprise"], "Box PC"), _ksa_section(m["src_xc-373-a"], "FEC XC-373")],
		faqs=[{"question": "XC-574 or XC-373?", "answer": "XC-574 is the H610 performance XCOMP. XC-373 is the compact Intel J6412 fanless-class platform.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)
	_p(
		m, "fec-touch-monitors", "FEC XMonitor & Large Displays", "Touch Monitors", "XMONITOR",
		hero=m["monitor"], card=m["monitor"],
		tagline="Touchscreen and commercial displays from POS size to 43 inches",
		short="FEC offers POS-sized monitors and larger displays including 22-inch, 32-inch and 42/43-inch models. This batch starts with LD-9043W.",
		long="<p>Use cases include customer-facing displays, operator screens, kitchen systems, information terminals and digital signage.</p>",
		chips="LD-9043W 42.5″\nFull HD PCAP\n500 nits · HDMI / VGA\nSignage · KDS · customer screen",
		story="Second screens and interactive displays", visual="Large-format FEC displays",
		card_title="Touch Monitors", card_summary="FEC commercial touch displays including the 43-inch LD-9043W.",
		cta_h="Specify a commercial display", cta_d="Start with LD-9043W for 42.5-inch Full HD touch signage, kitchen or customer screens.",
		meta_t="FEC Touch Monitors Saudi Arabia | Commercial Displays | Printechs",
		meta_d="FEC XMonitor and large commercial touch displays in Saudi Arabia, including the LD-9043W 43-inch Full HD PCAP display from Printechs.",
		benefits=[{"icon": "display", "title": "Large format", "description": "LD-9043W is a 42.5-inch Full HD true-flat PCAP display.", "sort_order": 1}],
		stories=[{"label": "LD-9043W", "image": m["src_ld-9043w-a"], "image_alt": "LD-9043W", "caption": "42.5-inch commercial touch display.", "sort_order": 1},
		         {"label": "Signage", "image": m["app_enterprise"], "image_alt": "Lobby display", "caption": "Customer and information screens.", "sort_order": 2}],
		icons=[{"icon": "display", "title": "LD series", "description": "22″ · 32″ · 43″", "sort_order": 1}],
		specs=[("Family", [("First model", "LD-9043W 42.5-inch")])],
		apps=[app_row(m, "enterprise", "Digital signage", "Lobby and marketing screens.", "Signage display", "retail", 1),
		      app_row(m, "kitchen", "Kitchen display", "Large-format KDS screens.", "Kitchen display", "food-beverage", 2)],
		sections=[_ksa_section(m["src_ld-9043w-b"], "FEC LD-9043W")],
		faqs=[{"question": "Are 22-inch and 32-inch models available?", "answer": "FEC lists LD-9022W and LD-9032W. Those pages will follow once LD-9043W is live. Ask on the quote if you need a smaller size now.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)
	_p(
		m, "fec-pos-peripherals", "FEC POS Peripherals", "POS Peripherals", "PERIPHERALS",
		hero=m["peripherals"], card=m["peripherals"],
		tagline="Receipt printers and identity modules that complete the FEC workstation",
		short="Complete the POS workstation with receipt printers, customer displays, RFID, magnetic-stripe readers, fingerprint readers and other compatible devices.",
		long="<p>This first batch publishes the TP-100 thermal receipt printer. MSR, RFID and fingerprint modules can be requested on XPOS Plus quotations.</p>",
		chips="TP-100 80 mm\nUSB · serial · Ethernet\nMSR · RFID · fingerprint\nUp to 250 mm/s",
		story="Finish the counter", visual="POS peripherals",
		card_title="POS Peripherals", card_summary="FEC TP-100 receipt printer plus RFID, MSR and fingerprint options.",
		cta_h="Add FEC peripherals", cta_d="Quote TP-100 now, or add RFID, MSR and fingerprint on the XPOS Plus configuration form.",
		meta_t="FEC POS Peripherals Saudi Arabia | TP-100 Receipt Printer | Printechs",
		meta_d="FEC POS peripherals from Printechs Saudi Arabia, starting with the TP-100 80 mm thermal receipt printer plus RFID, MSR and fingerprint options.",
		benefits=[{"icon": "print", "title": "TP-100", "description": "Compact 80 mm thermal printer with USB, serial and Ethernet.", "sort_order": 1}],
		stories=[{"label": "TP-100", "image": m["src_tp-100-a"], "image_alt": "TP-100", "caption": "80 mm thermal receipt printer.", "sort_order": 1},
		         {"label": "Checkout", "image": m["app_grocery"], "image_alt": "Retail checkout", "caption": "Printers and ID modules at POS.", "sort_order": 2}],
		icons=[{"icon": "print", "title": "TP-100", "description": "250 mm/s · 80 mm", "sort_order": 1}],
		specs=[("Family", [("Lead model", "TP-100"), ("Also quoted", "MSR, RFID, fingerprint modules")])],
		apps=[app_row(m, "grocery", "Checkout printing", "Receipts at grocery and specialty POS.", "Receipt printer", "retail", 1)],
		sections=[_integration_section(m["src_tp-100-b"], "TP-100"), _ksa_section(m["app_grocery"], "Retail checkout")],
		faqs=[{"question": "Can I add RFID or MSR on the same quote?", "answer": "Yes — those options appear on XPOS Plus product quote forms. TP-100 has its own cutter and media questions.", "sort_order": 1}],
		on_list=False, is_hub=1,
	)


def fill_products(m):
	_p(
		m, "fec-xp-4765w", "FEC XP-4765W 15.6″ Modular POS Terminal", "POS Terminals", "XPOS PLUS",
		hero=m["xp-4765w"], card=m["xp-4765w"],
		tagline="15.6-inch Full HD PCAP XPOS Plus with Intel options up to Core i7",
		short="The FEC XP-4765W is a premium 15.6-inch modular all-in-one POS terminal from the XPOS Plus family, designed for modern retail and customer-service environments requiring performance, reliability and a clean counter installation.",
		long=(
			"<p>The touchscreen panel computer can be attached or detached from its dual-hinge docking "
			"stand, while connectivity built into the stand provides centralized cable management and "
			"integration with POS peripherals.</p>"
			"<p>Published FEC characteristics include a 15.6-inch Full HD 1920 × 1080 true-flat PCAP "
			"touchscreen, Intel processor options up to Core i7-12700, up to 32 GB DDR4, M.2 PCIe "
			"storage, Windows 10/11 IoT Enterprise, USB/COM/LAN/HDMI and cash-drawer connectivity, "
			"optional RFID, 2D scanner, camera/LED and Wi-Fi/Bluetooth, VESA mounting and TPM 2.0.</p>"
			f"<p>{KSA_BODY}</p>"
		),
		chips="15.6″ FHD PCAP\nUp to Intel Core i7-12700\nUp to 32 GB DDR4 · M.2\nWindows 10/11 IoT",
		story="Why XP-4765W at the checkout", visual="Display, dock and peripherals",
		card_title="XP-4765W", card_summary="15.6-inch modular XPOS Plus POS terminal with Full HD PCAP touch and Intel options up to i7.",
		cta_h="Configure XP-4765W", cta_d="Choose processor, memory, OS and optional RFID, scanner, camera or Wi-Fi on the quote form.",
		meta_t="FEC XP-4765W POS Terminal Saudi Arabia | 15.6″ XPOS Plus | Printechs",
		meta_d="FEC XP-4765W 15.6-inch modular POS terminal with Full HD PCAP touchscreen, Intel processors, Windows IoT and flexible peripheral integration. Available from Printechs Saudi Arabia.",
		benefits=[
			{"icon": "display", "title": "15.6″ Full HD PCAP", "description": "1920 × 1080 true-flat projected capacitive touch for a modern counter.", "sort_order": 1},
			{"icon": "speed", "title": "Performance options", "description": "Published Intel Celeron G6900 through Core i7-12700, up to 32 GB DDR4 and M.2 PCIe storage.", "sort_order": 2},
			{"icon": "device", "title": "Dual-hinge modular dock", "description": "Attach or detach the panel; I/O and cable management live in the stand.", "sort_order": 3},
			{"icon": "connectivity", "title": "POS I/O", "description": "USB, COM, LAN, HDMI and cash-drawer connectivity for scanners, printers and payment.", "sort_order": 4},
			{"icon": "scan", "title": "Optional modules", "description": "RFID, 2D barcode scanner, camera/LED and Wi-Fi/Bluetooth as published by FEC.", "sort_order": 5},
			{"icon": "shield", "title": "TPM 2.0", "description": "TPM 2.0 support for commercial Windows IoT deployments.", "sort_order": 6},
		],
		stories=[
			{"label": "Modular dock", "image": m["src_xp-4765w-a"], "image_alt": "XP-4765W front", "caption": "Panel PC plus dual-hinge stand.", "sort_order": 1},
			{"label": "Counter angle", "image": m["src_xp-4765w-b"], "image_alt": "XP-4765W angle", "caption": "Clean cable-managed installation.", "sort_order": 2},
			{"label": "I/O", "image": m["src_xp-4765w-c"], "image_alt": "XP-4765W connectivity", "caption": "Stand-integrated POS connectivity.", "sort_order": 3},
		],
		icons=[
			{"icon": "display", "title": "15.6″ FHD", "description": "1920 × 1080 PCAP", "sort_order": 1},
			{"icon": "speed", "title": "Up to i7-12700", "description": "12th-gen Intel options", "sort_order": 2},
			{"icon": "device", "title": "Modular dock", "description": "Dual-hinge + cable management", "sort_order": 3},
			{"icon": "connectivity", "title": "POS I/O", "description": "USB · COM · LAN · HDMI · DK", "sort_order": 4},
		],
		specs=[
			("Display & touch", [
				("Size", "15.6-inch"),
				("Resolution", "1920 × 1080 Full HD"),
				("Touch", "True-flat projected capacitive"),
			]),
			("Performance", [
				("Processor options", "Celeron G6900; i3-12100; i3-12100TE; i5-12400; i5-12500TE; i7-12700"),
				("Memory", "Up to 32 GB DDR4"),
				("Storage", "M.2 PCIe"),
				("OS", "Windows 10 IoT Enterprise / Windows 11 IoT Enterprise"),
				("Security", "TPM 2.0 support"),
			]),
			("Integration", [
				("Design", "Dual-hinge modular docking stand"),
				("I/O", "USB, COM, LAN, HDMI and cash-drawer connectivity"),
				("Options", "RFID, 2D scanner, camera/LED, Wi-Fi/Bluetooth"),
				("Mounting", "VESA mounting support"),
			]),
		],
		apps=[
			app_row(m, "fashion", "Fashion & apparel retail", "Stylish POS with barcode scanning, card payment and customer display integration.", "Fashion POS terminal", "fashion", 1),
			app_row(m, "grocery", "Supermarkets & grocery", "Busy checkout counters needing multiple peripheral connections.", "Supermarket POS", "retail", 2),
			app_row(m, "pharmacy", "Pharmacy & healthcare retail", "Configure with scanners, customer displays and payment hardware.", "Pharmacy POS", "pharmaceutical", 3),
			app_row(m, "electronics", "Specialty retail", "Cosmetics, electronics, footwear, jewellery, convenience and other specialty operations.", "Specialty retail POS", "retail", 4),
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "Performance, display and POS peripheral integration", "body": "Specify the Intel SKU, memory and Windows IoT build for the store, then add RFID, 2D scanning, camera/LED or wireless only when the counter needs them. VESA remains available if the dock is not used.", "image": m["src_xp-4765w-c"], "image_alt": "XP-4765W I/O", "sort_order": 1},
			_integration_section(m["app_fashion"], "Fashion POS with Modern POS"),
			_ksa_section(m["app_grocery"], "Saudi retail checkout"),
		],
		faqs=[
			{"question": "Which processors does FEC publish for XP-4765W?", "answer": "Intel Celeron G6900, Core i3-12100, i3-12100TE, i5-12400, i5-12500TE and i7-12700. Choose one on the quote form.", "sort_order": 1},
			{"question": "Will this run Modern POS?", "answer": "Yes. Printechs can image Windows IoT and connect XP-4765W to Modern POS, ERPNext, scanners, printers and payment terminals.", "sort_order": 2},
			{"question": "Do you sell spare FEC parts on this page?", "answer": "No. This page is the XP-4765W system. Adapters and spare boards are quoted separately if needed.", "sort_order": 3},
		],
		quote=xpos_quote_options(), configure=1, featured=1,
	)
	_p(
		m, "fec-xp-3765w", "FEC XP-3765W XPOS Plus Touch POS Terminal", "POS Terminals", "XPOS PLUS",
		hero=m["xp-3765w"], card=m["xp-3765w"],
		tagline="Slim widescreen XPOS Plus for compact professional checkout",
		short="The FEC XP-3765W combines a slim widescreen touch interface with the modular XPOS Plus platform. It is designed for retailers seeking a professional, compact checkout workstation with flexible customer display, scanner, payment and peripheral options.",
		long="<p>Recommended sectors: fashion, cosmetics, pharmacy, electronics, specialty retail, supermarket and service businesses.</p>" + f"<p>{KSA_BODY}</p>",
		chips="XPOS Plus widescreen\nModular POS platform\nRetail & hospitality\nFlexible peripherals",
		story="Compact XPOS Plus for everyday retail", visual="XP-3765W on the counter",
		card_title="XP-3765W", card_summary="XPOS Plus widescreen touch POS terminal for compact retail and hospitality checkout.",
		cta_h="Configure XP-3765W", cta_d="Confirm the live FEC processor list, then choose memory, OS and optional modules.",
		meta_t="FEC XP-3765W POS Terminal Saudi Arabia | XPOS Plus Touch POS",
		meta_d="FEC XP-3765W XPOS Plus touchscreen POS terminal for retail and hospitality. Modern modular design, commercial performance and flexible POS peripheral connectivity.",
		benefits=[
			{"icon": "display", "title": "Slim widescreen", "description": "Professional touch interface on the modular XPOS Plus platform.", "sort_order": 1},
			{"icon": "checkout", "title": "Compact checkout", "description": "Built for fashion, cosmetics, pharmacy and specialty counters.", "sort_order": 2},
			{"icon": "connectivity", "title": "POS peripherals", "description": "Customer display, scanner, payment and printer options on the quote.", "sort_order": 3},
		],
		stories=[
			{"label": "Front", "image": m["src_xp-3765w-a"], "image_alt": "XP-3765W", "caption": "Slim XPOS Plus widescreen.", "sort_order": 1},
			{"label": "Angle", "image": m["src_xp-3765w-b"], "image_alt": "XP-3765W angle", "caption": "Compact professional checkout.", "sort_order": 2},
			{"label": "Family", "image": m["src_xp-3765w-c"], "image_alt": "XP-3765W side", "caption": "Modular XPOS Plus stand.", "sort_order": 3},
		],
		icons=[{"icon": "checkout", "title": "XPOS Plus", "description": "Widescreen touch POS", "sort_order": 1},
		       {"icon": "connectivity", "title": "Peripherals", "description": "Scanner · printer · payment", "sort_order": 2}],
		specs=[
			("Platform", [
				("Family", "XPOS Plus"),
				("Model", "XP-3765W"),
				("Use", "Retail and hospitality touch POS"),
				("Processor", "Confirm against the current FEC XP-3765W specification on the quote"),
			]),
		],
		apps=[
			app_row(m, "beauty", "Cosmetics & specialty", "Low-profile widescreen POS for premium counters.", "Cosmetics POS", "retail", 1),
			app_row(m, "pharmacy", "Pharmacy", "Compact professional checkout.", "Pharmacy POS", "pharmaceutical", 2),
			app_row(m, "fashion", "Fashion", "Clean counter installation.", "Fashion POS", "fashion", 3),
		],
		sections=[_integration_section(m["app_beauty"], "Beauty POS"), _ksa_section(m["app_pharmacy"], "Pharmacy POS")],
		faqs=[{"question": "Is XP-3765W the same as XP-4765W?", "answer": "Both are XPOS Plus. XP-4765W is the 15.6-inch model with a published Intel list up to i7-12700. Confirm XP-3765W processors from the live FEC datasheet when you quote.", "sort_order": 1}],
		quote=[
			q_select("Platform", "Processor", ["Confirm against current FEC XP-3765W specification", "Match a listed XPOS Plus Intel SKU"], sort=1),
			q_select("Platform", "Memory", ["8 GB DDR4", "16 GB DDR4", "32 GB DDR4"], sort=2),
			q_select("Software", "Operating system", ["Windows 10 IoT Enterprise", "Windows 11 IoT Enterprise", "No OS (hardware only)"], sort=3),
			q_check("Options", "Optional modules", ["Customer display", "2D barcode scanner", "Wi-Fi and Bluetooth"], sort=4),
		],
		configure=1,
	)
	_p(
		m, "fec-xp-4765", "FEC XP-4765 POS Terminal", "POS Terminals", "XPOS PLUS",
		hero=m["xp-4765"], card=m["xp-4765"],
		tagline="XPOS Plus POS system for attended retail checkout",
		short="FEC XP-4765 is the XPOS Plus sibling of XP-4765W — a commercial all-in-one POS system for retailers that want the same modular family without the W widescreen designation.",
		long="<p>Use this page when the project is specified as XP-4765. For 15.6-inch Full HD published options, see XP-4765W. Processor, memory and OS are collected on the quote against the current FEC datasheet.</p>",
		chips="XPOS Plus\nModular POS system\nRetail checkout\nConfigurable Intel platform",
		story="XP-4765 in the XPOS Plus family", visual="Classic XPOS Plus",
		card_title="XP-4765", card_summary="FEC XPOS Plus POS system for attended retail checkout.",
		cta_h="Quote XP-4765", cta_d="Configure processor, memory and OS against the current FEC XP-4765 datasheet.",
		meta_t="FEC XP-4765 POS System Saudi Arabia | XPOS Plus | Printechs",
		meta_d="FEC XP-4765 XPOS Plus POS system for retail checkout in Saudi Arabia. Modular commercial POS hardware from Printechs.",
		benefits=[{"icon": "checkout", "title": "XPOS Plus system", "description": "All-in-one commercial POS in the same family as XP-4765W.", "sort_order": 1},
		          {"icon": "device", "title": "Modular family", "description": "Stand, I/O and peripheral story shared with XPOS Plus.", "sort_order": 2}],
		stories=[{"label": "XP-4765", "image": m["src_xp-4765-a"], "image_alt": "XP-4765", "caption": "XPOS Plus POS system.", "sort_order": 1},
		         {"label": "Dock", "image": m["src_xp-4765-b"], "image_alt": "XP-4765 dock", "caption": "Modular stand design.", "sort_order": 2}],
		icons=[{"icon": "checkout", "title": "XP-4765", "description": "XPOS Plus POS system", "sort_order": 1}],
		specs=[("Platform", [("Family", "XPOS Plus"), ("Model", "XP-4765"), ("Related", "See XP-4765W for the published 15.6-inch Full HD specification")])],
		apps=[app_row(m, "grocery", "Retail checkout", "Supermarket and specialty POS.", "Retail POS", "retail", 1),
		      app_row(m, "electronics", "Specialty stores", "Electronics and service counters.", "Specialty POS", "retail", 2)],
		sections=[_integration_section(m["app_electronics"], "Specialty POS"), _ksa_section(m["app_grocery"], "Retail POS")],
		faqs=[{"question": "XP-4765 or XP-4765W?", "answer": "XP-4765W is the 15.6-inch Full HD model with the published Intel list on this site. Choose XP-4765 when that exact SKU is specified.", "sort_order": 1}],
		quote=xpos_quote_options(), configure=1,
	)
	_p(
		m, "fec-xp-3765", "FEC XP-3765 POS Machine", "POS Terminals", "XPOS PLUS",
		hero=m["xp-3765"], card=m["xp-3765"],
		tagline="XPOS Plus POS machine for compact attended checkout",
		short="FEC XP-3765 is the XPOS Plus POS machine alongside XP-3765W. Use it when the project specifies the non-W model.",
		long="<p>Configure memory, OS and peripherals on the quote. Confirm processor options from the current FEC XP-3765 datasheet — this page does not invent a chip list.</p>",
		chips="XPOS Plus\nPOS machine\nCompact checkout\nConfigurable quote",
		story="XP-3765 for everyday POS", visual="XPOS Plus compact",
		card_title="XP-3765", card_summary="FEC XPOS Plus POS machine for compact retail checkout.",
		cta_h="Quote XP-3765", cta_d="Confirm the live FEC specification and the peripherals you need at the counter.",
		meta_t="FEC XP-3765 POS Machine Saudi Arabia | XPOS Plus | Printechs",
		meta_d="FEC XP-3765 XPOS Plus POS machine for retail checkout in Saudi Arabia. Commercial touch POS hardware from Printechs.",
		benefits=[{"icon": "checkout", "title": "POS machine", "description": "Compact XPOS Plus for attended checkout.", "sort_order": 1}],
		stories=[{"label": "XP-3765", "image": m["src_xp-3765-a"], "image_alt": "XP-3765", "caption": "XPOS Plus POS machine.", "sort_order": 1},
		         {"label": "Angle", "image": m["src_xp-3765-b"], "image_alt": "XP-3765 angle", "caption": "Compact commercial POS.", "sort_order": 2}],
		icons=[{"icon": "checkout", "title": "XP-3765", "description": "XPOS Plus POS machine", "sort_order": 1}],
		specs=[("Platform", [("Family", "XPOS Plus"), ("Model", "XP-3765")])],
		apps=[app_row(m, "fashion", "Fashion checkout", "Compact attended POS.", "Fashion POS", "fashion", 1)],
		sections=[_ksa_section(m["app_fashion"], "Fashion POS")],
		faqs=[{"question": "XP-3765 or XP-3765W?", "answer": "Use the W model when the project specifies the widescreen XP-3765W. Use this page for XP-3765.", "sort_order": 1}],
		quote=[
			q_select("Platform", "Processor", ["Confirm against current FEC XP-3765 specification"], sort=1),
			q_select("Software", "Operating system", ["Windows 10 IoT Enterprise", "Windows 11 IoT Enterprise", "No OS (hardware only)"], sort=2),
			q_check("Options", "Optional modules", ["Customer display", "2D barcode scanner"], sort=3),
		],
		configure=1,
	)
	_p(
		m, "fec-st-1130w", "FEC ST-1130W Android Smart POS Terminal", "POS Terminals", "SMART POS",
		hero=m["st-1130w"], card=m["st-1130w"],
		tagline="Compact Android smart POS for ordering, QR and customer interaction",
		short="The ST-1130W is FEC's compact Android smart terminal designed for applications where space, mobility of interaction and simplicity are important.",
		long="<p>Its display can be repositioned to face the customer, providing possibilities for ordering, QR interaction, customer information and payment-related workflows. FEC promotes the unit for small shops, queue management and customer engagement applications.</p>",
		chips="Android smart POS\nRepositionable display\nQR · queue · ordering\nSmall-shop friendly",
		story="Android POS that can face the customer", visual="ST-1130W interaction",
		card_title="ST-1130W", card_summary="Compact Android smart POS for small retail, QR payments, queueing and customer engagement.",
		cta_h="Configure ST-1130W", cta_d="Tell us whether the display faces staff or the customer, and which payment or QR workflow you need.",
		meta_t="FEC ST-1130W Android POS Terminal Saudi Arabia | Smart POS",
		meta_d="FEC ST-1130W compact Android smart POS terminal for retail, ordering, QR payments, queue management and customer interaction applications in Saudi Arabia.",
		benefits=[
			{"icon": "android", "title": "Android smart POS", "description": "Compact terminal for simple retail and engagement apps.", "sort_order": 1},
			{"icon": "display", "title": "Repositionable display", "description": "Turn the screen toward the customer for QR, ordering or information.", "sort_order": 2},
			{"icon": "loyalty", "title": "Customer journeys", "description": "Ordering, queueing, loyalty registration and reception counters.", "sort_order": 3},
		],
		stories=[
			{"label": "Operator view", "image": m["src_st-1130w-a"], "image_alt": "ST-1130W", "caption": "Compact Android smart POS.", "sort_order": 1},
			{"label": "Customer face", "image": m["src_st-1130w-b"], "image_alt": "ST-1130W tilted", "caption": "Display can face the customer.", "sort_order": 2},
		],
		icons=[{"icon": "android", "title": "Android", "description": "Smart POS terminal", "sort_order": 1},
		       {"icon": "display", "title": "Reversible", "description": "Staff or customer facing", "sort_order": 2}],
		specs=[("Platform", [("Model", "ST-1130W"), ("OS", "Android smart terminal"), ("Use", "Small retail, QR, queue, reception, self-service interaction")])],
		apps=[
			app_row(m, "fashion", "Small retail stores", "Compact Android POS where a full XPOS Plus dock is more than you need.", "Small retail Android POS", "retail", 1),
			app_row(m, "qsr", "Customer ordering", "Face the guest for ordering and QR workflows.", "Ordering terminal", "food-beverage", 2),
			app_row(m, "enterprise", "Queue management", "Ticket and queue registration at reception.", "Queue terminal", "retail", 3),
		],
		sections=[_integration_section(m["app_qsr"], "Ordering terminal"), _ksa_section(m["app_enterprise"], "Queue terminal")],
		faqs=[{"question": "Is ST-1130W a full Windows POS?", "answer": "No. It is FEC's compact Android smart terminal. Use XPOS Plus when you need Windows IoT and a full dock.", "sort_order": 1}],
		quote=[
			q_select("Application", "Primary use", [
				"Small retail POS",
				"Customer ordering",
				"Queue management",
				"QR / loyalty",
				"Reception / information",
				"Self-service",
			], sort=1),
			q_select("Installation", "Display orientation", ["Operator facing", "Customer facing", "Both / repositionable"], sort=2),
			q_check("Options", "Project needs", ["Payment integration", "QR / e-wallet", "Wall or counter mount"], sort=3),
		],
		configure=1,
	)
	_p(
		m, "fec-xelf-ii", "FEC XELF II Modular Self-Service Kiosk", "Self-Service Kiosks", "XELF II",
		hero=m["xelf-ii"], card=m["xelf-ii"],
		tagline="One modular architecture for checkout, ordering, hotel check-in and service",
		short="The FEC XELF II is a modular self-service platform designed to support multiple customer journeys from a common hardware architecture.",
		long=(
			"<p>Rather than adapting one fixed kiosk for different projects, FEC designed XELF II around "
			"configurable displays, peripherals and mounting arrangements, making it suitable for varying "
			"environments and workflows. FEC positions XELF II for retail, hospitality and unattended service.</p>"
			f"<p>{KSA_BODY}</p>"
		),
		chips="Modular kiosk\nSelf-checkout · ordering\nHotel check-in\nQueue & customer service",
		story="Several journeys, one hardware architecture", visual="XELF II configurations",
		card_title="XELF II", card_summary="Modular FEC self-service kiosk for checkout, ordering, hotel check-in and unattended service.",
		cta_h="Configure XELF II", cta_d="Choose the journey, mounting style and peripherals — scanner, payment, printer, RFID or camera.",
		meta_t="FEC XELF II Self-Service Kiosk Saudi Arabia | Retail & Hotel Kiosk",
		meta_d="FEC XELF II modular self-service kiosk for self-checkout, ordering, hotel check-in, payment and unattended customer service applications in Saudi Arabia.",
		benefits=[
			{"icon": "store", "title": "Modular by design", "description": "Displays, peripherals and mounting change with the site — not a single rigid kiosk.", "sort_order": 1},
			{"icon": "checkout", "title": "Self-checkout", "description": "Customers scan products, review the basket and pay.", "sort_order": 2},
			{"icon": "loyalty", "title": "Hospitality & service", "description": "Hotel check-in/out, queueing, ticketing and membership enrolment.", "sort_order": 3},
		],
		stories=[
			{"label": "Floor kiosk", "image": m["src_xelf-ii-a"], "image_alt": "XELF II", "caption": "Modular self-service enclosure.", "sort_order": 1},
			{"label": "Service point", "image": m["src_xelf-ii-b"], "image_alt": "XELF II configuration", "caption": "Configurable display and peripherals.", "sort_order": 2},
			{"label": "Family", "image": m["src_xelf-ii-c"], "image_alt": "XELF II variant", "caption": "Retail, hotel and QSR journeys.", "sort_order": 3},
		],
		icons=[{"icon": "store", "title": "Modular", "description": "Display · mount · I/O", "sort_order": 1},
		       {"icon": "checkout", "title": "Journeys", "description": "Checkout · hotel · QSR", "sort_order": 2}],
		specs=[("Platform", [
			("Family", "XELF II"),
			("Architecture", "Modular self-service platform"),
			("Mounting", "Configurable — confirm floor, counter or wall on the quote"),
			("Sectors", "Retail, hospitality, unattended service"),
		])],
		apps=[
			app_row(m, "selfservice", "Retail self-checkout", "Scan products, review transactions and complete payment.", "Self-checkout kiosk Saudi Arabia", "retail", 1),
			app_row(m, "qsr", "Self-ordering", "QSR, cafeterias and food-service ordering.", "Self-ordering kiosk", "food-beverage", 2),
			app_row(m, "hospitality", "Hotel self check-in", "Automated guest arrival and departure workflows.", "Hotel self check-in kiosk", "hospitality", 3),
			app_row(m, "enterprise", "Queue, ticketing & service", "Ticket generation, queue registration, membership and information.", "Queue kiosk", "retail", 4),
		],
		sections=[
			{"section_type": "Industry Solution", "heading": "Self-service keywords that matter in KSA", "body": "This page targets FEC self service kiosk Saudi Arabia, self checkout kiosk Saudi Arabia, hotel self check in kiosk Saudi Arabia, retail kiosk KSA and self ordering kiosk Saudi Arabia — not only the model name XELF II.", "image": m["app_selfservice"], "image_alt": "Self-checkout", "sort_order": 1},
			_integration_section(m["app_qsr"], "Self-ordering"),
			_ksa_section(m["app_hospitality"], "Hotel self check-in"),
		],
		faqs=[
			{"question": "Can one XELF II design cover hotel and retail?", "answer": "The architecture is shared. Display size, mounting and peripherals (scanner, payment, printer, RFID, passport/ID, camera) are specified per journey on the quote.", "sort_order": 1},
			{"question": "Do you still sell the older XELF?", "answer": "XELF II is the current modular platform we publish first. Ask if a legacy XELF spare or expansion is required.", "sort_order": 2},
		],
		quote=[
			q_select("Application", "Primary journey", [
				"Retail self-checkout",
				"Self-ordering (QSR / cafeteria)",
				"Hotel self check-in",
				"Queue and ticketing",
				"Customer service / membership",
			], sort=1),
			q_select("Installation", "Mounting", ["Floor-standing", "Counter / desktop", "Wall-mount", "Confirm during survey"], sort=2),
			q_check("Peripherals", "Modules required", [
				"2D barcode scanner",
				"Payment terminal",
				"Receipt printer",
				"RFID / NFC",
				"Passport / ID reader",
				"Camera",
			], sort=3),
		],
		configure=1, featured=1,
	)
	_p(
		m, "fec-pp-9745w", "FEC PP-9745W 15.6″ Performance Panel PC", "Panel PCs", "XPPC",
		hero=m["pp-9745w"], card=m["pp-9745w"],
		tagline="15.6-inch H610 performance XPPC for POS, kiosk and embedded touch",
		short="The PP-9745W is part of FEC's performance XPPC family, combining touchscreen operation with an integrated commercial computing platform.",
		long="<p>The model is designed for applications requiring greater processing capability than entry-level fanless systems, including advanced POS, kiosks, service terminals and embedded commercial applications. FEC identifies PP-9745W as a 15.6-inch H610-based performance XPPC.</p>",
		chips="15.6″ XPPC\nIntel H610 platform\ni3 / i5 / i7 options\nPerformance panel PC",
		story="When a fanless J-series panel is not enough", visual="PP-9745W performance XPPC",
		card_title="PP-9745W", card_summary="15.6-inch H610 performance panel PC for POS, kiosk and enterprise touch applications.",
		cta_h="Configure PP-9745W", cta_d="Select i3-12100, i5-12400 or i7-12700 plus memory, storage and Windows IoT.",
		meta_t="FEC PP-9745W Panel PC Saudi Arabia | 15.6″ Touchscreen PC",
		meta_d="FEC PP-9745W 15.6-inch performance panel PC for POS, kiosk, retail, industrial and enterprise touchscreen applications. Available from Printechs Saudi Arabia.",
		benefits=[{"icon": "speed", "title": "H610 performance", "description": "Headroom beyond entry-level fanless J6412 panel PCs.", "sort_order": 1},
		          {"icon": "display", "title": "15.6-inch touch", "description": "Integrated commercial touchscreen computer.", "sort_order": 2}],
		stories=[{"label": "PP-9745W", "image": m["src_pp-9745w-a"], "image_alt": "PP-9745W", "caption": "15.6-inch performance XPPC.", "sort_order": 1},
		         {"label": "I/O", "image": m["src_pp-9745w-b"], "image_alt": "PP-9745W I/O", "caption": "Commercial connectivity.", "sort_order": 2}],
		icons=[{"icon": "speed", "title": "H610", "description": "i3 / i5 / i7 options", "sort_order": 1},
		       {"icon": "display", "title": "15.6″", "description": "Performance XPPC", "sort_order": 2}],
		specs=[("Platform", [
			("Model", "PP-9745W"),
			("Family", "XPPC performance"),
			("Display", "15.6-inch"),
			("Chipset", "Intel H610"),
			("Typical processors", "Core i3-12100, i5-12400, i7-12700"),
		])],
		apps=[app_row(m, "enterprise", "Service terminals", "Advanced POS and operator stations.", "Panel PC terminal", "retail", 1),
		      app_row(m, "selfservice", "Kiosk compute + display", "Embedded commercial touch.", "Kiosk panel PC", "retail", 2)],
		sections=[_integration_section(m["app_enterprise"], "Panel PC POS"), _ksa_section(m["src_pp-9745w-b"], "PP-9745W")],
		faqs=[{"question": "PP-9745W or PP-9735W?", "answer": "PP-9745W is the H610 performance 15.6-inch XPPC. PP-9735W is the fanless Intel J6412 15.6-inch model.", "sort_order": 1}],
		quote=panel_h610_quote_options(), configure=1,
	)
	_p(
		m, "fec-pp-9735w", "FEC PP-9735W Fanless Panel PC", "Panel PCs", "XPPC",
		hero=m["pp-9735w"], card=m["pp-9735w"],
		tagline="Fanless 15.6-inch XPPC on Intel J6412",
		short="The PP-9735W is a fanless 15.6-inch XPPC built around FEC's compact commercial panel-PC architecture.",
		long="<p>Fanless operation makes it attractive for installations where low noise, reduced mechanical maintenance and compact installation are important. FEC currently lists the PP-9735W with an Intel J6412 platform.</p>",
		chips="15.6″ fanless\nIntel J6412\nLow noise XPPC\nPOS · kiosk · service",
		story="Quiet panel PC for compact installs", visual="PP-9735W fanless XPPC",
		card_title="PP-9735W", card_summary="Fanless 15.6-inch FEC panel PC with Intel J6412 for POS, kiosks and service counters.",
		cta_h="Configure PP-9735W", cta_d="Set memory, storage and Windows IoT on the J6412 fanless platform.",
		meta_t="FEC PP-9735W Fanless Panel PC Saudi Arabia | 15.6″ Touch PC",
		meta_d="FEC PP-9735W fanless 15.6-inch panel PC for POS, kiosks, service counters and commercial touchscreen applications. FEC solutions from Printechs KSA.",
		benefits=[{"icon": "durability", "title": "Fanless", "description": "No fan for quieter counters and less mechanical maintenance.", "sort_order": 1},
		          {"icon": "device", "title": "Intel J6412", "description": "Compact commercial platform published by FEC for PP-9735W.", "sort_order": 2}],
		stories=[{"label": "PP-9735W", "image": m["src_pp-9735w-a"], "image_alt": "PP-9735W", "caption": "15.6-inch fanless XPPC.", "sort_order": 1},
		         {"label": "Angle", "image": m["src_pp-9735w-b"], "image_alt": "PP-9735W angle", "caption": "Compact commercial panel.", "sort_order": 2}],
		icons=[{"icon": "durability", "title": "Fanless", "description": "J6412 XPPC", "sort_order": 1},
		       {"icon": "display", "title": "15.6″", "description": "Touch panel PC", "sort_order": 2}],
		specs=[("Platform", [("Model", "PP-9735W"), ("Display", "15.6-inch"), ("Processor", "Intel J6412"), ("Cooling", "Fanless")])],
		apps=[app_row(m, "pharmacy", "Quiet counters", "Pharmacy and service desks that do not want a fan.", "Fanless panel PC", "pharmaceutical", 1),
		      app_row(m, "enterprise", "Embedded touch", "Compact kiosk and information terminals.", "Service panel PC", "retail", 2)],
		sections=[_ksa_section(m["app_pharmacy"], "Quiet retail counter")],
		faqs=[{"question": "Is PP-9735W the same as PP-9735?", "answer": "No. PP-9735W is the 15.6-inch fanless model. PP-9735 / PP-9735L / WL pages are not in this first batch.", "sort_order": 1}],
		quote=[
			q_select("Platform", "Memory", ["8 GB DDR4", "16 GB DDR4"], sort=1),
			q_select("Platform", "Storage", ["128 GB SSD", "256 GB SSD", "512 GB SSD"], sort=2),
			q_select("Software", "Operating system", ["Windows 10 IoT Enterprise", "Windows 11 IoT Enterprise", "No OS (hardware only)"], sort=3),
		],
		configure=1,
	)
	_p(
		m, "fec-pp-9815w", "FEC PP-9815W Panel PC", "Panel PCs", "XPPC",
		hero=m["pp-9815w"], card=m["pp-9815w"],
		tagline="FEC panel PC for POS and kiosk touch installations",
		short="PP-9815W is part of FEC's current XPPC catalogue — a commercial touchscreen panel PC for POS and kiosk projects that need a widescreen XPPC rather than a docked XPOS Plus terminal.",
		long="<p>Configure the live FEC PP-9815W processor, memory and OS on the quote. Do not treat this page as PP-9815 (non-W) or PP-9812W.</p>",
		chips="XPPC PP-9815W\nPOS & kiosk touch PC\nWidescreen panel\nConfigurable quote",
		story="Another XPPC size for integrators", visual="PP-9815W",
		card_title="PP-9815W", card_summary="FEC XPPC panel PC for POS and kiosk touchscreen installations.",
		cta_h="Configure PP-9815W", cta_d="Confirm the published FEC PP-9815W platform and the OS you will image.",
		meta_t="FEC PP-9815W Panel PC Saudi Arabia | POS & Kiosk Touch PC",
		meta_d="FEC PP-9815W panel PC for POS and kiosk touchscreen applications in Saudi Arabia. Commercial XPPC hardware from Printechs.",
		benefits=[{"icon": "display", "title": "XPPC widescreen", "description": "Panel PC form factor for POS and kiosk builds.", "sort_order": 1}],
		stories=[{"label": "PP-9815W", "image": m["src_pp-9815w-a"], "image_alt": "PP-9815W", "caption": "FEC XPPC panel PC.", "sort_order": 1},
		         {"label": "Family", "image": m["src_pp-9815w-b"], "image_alt": "PP-9815W family", "caption": "POS and kiosk touch PC.", "sort_order": 2}],
		icons=[{"icon": "display", "title": "PP-9815W", "description": "XPPC panel PC", "sort_order": 1}],
		specs=[("Platform", [("Model", "PP-9815W"), ("Family", "XPPC"), ("Use", "POS and kiosk touch PC")])],
		apps=[app_row(m, "enterprise", "POS & kiosk", "Widescreen XPPC for counters and enclosures.", "PP-9815W", "retail", 1)],
		sections=[_ksa_section(m["src_pp-9815w-b"], "PP-9815W")],
		faqs=[{"question": "PP-9815W or PP-9745W?", "answer": "PP-9745W is the published 15.6-inch H610 performance XPPC. Use PP-9815W when that exact catalogue model is specified.", "sort_order": 1}],
		quote=[
			q_select("Platform", "Configuration", ["Confirm against current FEC PP-9815W specification"], sort=1),
			q_select("Software", "Operating system", ["Windows 10 IoT Enterprise", "Windows 11 IoT Enterprise", "Android", "No OS (hardware only)"], sort=2),
		],
		configure=1,
	)
	fill_remaining_products(m)


def fill_remaining_products(m):
	_p(
		m, "fec-kp-9795w", "FEC KP-9795W Kitchen Display Panel PC", "Kitchen Displays", "KP SERIES",
		hero=m["kp-9795w"], card=m["kp-9795w"],
		tagline="Windows kitchen touchscreen for high-demand KDS",
		short="The KP-9795W is a Windows-based FEC kitchen panel PC designed for high-demand food-service operations.",
		long="<p>It provides a dedicated commercial touchscreen platform for kitchen display software, order preparation, production status management and restaurant back-of-house workflows. FEC's current catalogue lists the Windows KP-9795W with Intel N97 / N150 / Core 3 N355 platform options.</p>",
		chips="Windows KDS\nIntel N97 / N150 / Core 3 N355\nKitchen panel PC\nQSR & back-of-house",
		story="Windows hardware for kitchen display software", visual="KP-9795W in food service",
		card_title="KP-9795W", card_summary="Windows FEC kitchen panel PC for KDS, QSR and restaurant back-of-house.",
		cta_h="Configure KP-9795W", cta_d="Choose N97, N150 or Core 3 N355 plus memory and storage for your KDS application.",
		meta_t="FEC KP-9795W Kitchen Display System Saudi Arabia | Windows KDS",
		meta_d="FEC KP-9795W commercial Windows kitchen touchscreen panel PC for KDS, QSR, restaurant and food-service operations. Available from Printechs Saudi Arabia.",
		benefits=[
			{"icon": "durability", "title": "Kitchen-first Windows PC", "description": "Dedicated commercial touchscreen for KDS software, not an office panel moved into the kitchen.", "sort_order": 1},
			{"icon": "speed", "title": "N-series / Core 3 options", "description": "Published Intel N97, N150 and Core 3 N355 platforms.", "sort_order": 2},
		],
		stories=[
			{"label": "KP-9795W", "image": m["src_kp-9795w-a"], "image_alt": "KP-9795W", "caption": "Windows kitchen panel PC.", "sort_order": 1},
			{"label": "Kitchen line", "image": m["app_kitchen"], "image_alt": "Commercial kitchen", "caption": "Order preparation and KDS.", "sort_order": 2},
		],
		icons=[
			{"icon": "durability", "title": "Windows KDS", "description": "KP-9795W", "sort_order": 1},
			{"icon": "speed", "title": "N97 / N150 / N355", "description": "Published FEC options", "sort_order": 2},
		],
		specs=[("Platform", [
			("Model", "KP-9795W"),
			("OS", "Windows kitchen panel PC"),
			("Processor options", "Intel N97, Intel N150, Intel Core 3 N355"),
			("Use", "KDS, QSR, restaurant back-of-house"),
		])],
		apps=[
			app_row(m, "kitchen", "Kitchen Display System", "Tickets and production status on a dedicated Windows touch PC.", "Restaurant KDS Saudi Arabia", "food-beverage", 1),
			app_row(m, "qsr", "QSR & cafeterias", "High-pressure kitchen lines.", "QSR kitchen display", "food-beverage", 2),
		],
		sections=[_integration_section(m["app_qsr"], "QSR KDS"), _ksa_section(m["app_kitchen"], "Kitchen touchscreen KSA")],
		faqs=[{"question": "KP-9795W or KP-9155W?", "answer": "KP-9795W is Windows (N97 / N150 / Core 3 N355). KP-9155W is the Android MediaTek G700 kitchen panel PC. Match the KDS application.", "sort_order": 1}],
		quote=[
			q_select("Platform", "Processor", ["Intel N97", "Intel N150", "Intel Core 3 N355", "Confirm during survey"], sort=1),
			q_select("Platform", "Memory", ["8 GB", "16 GB"], sort=2),
			q_select("Platform", "Storage", ["128 GB SSD", "256 GB SSD", "512 GB SSD"], sort=3),
			q_select("Software", "Operating system", ["Windows 10 IoT Enterprise", "Windows 11 IoT Enterprise"], sort=4),
		],
		configure=1,
	)
	_p(
		m, "fec-kp-9155w", "FEC KP-9155W Android Kitchen Display", "Kitchen Displays", "KP SERIES",
		hero=m["kp-9155w"], card=m["kp-9155w"],
		tagline="Android kitchen panel PC on MediaTek G700",
		short="A commercial Android touchscreen platform intended for Kitchen Display System and restaurant back-of-house deployments.",
		long="<p>FEC lists the current KP-9155W platform using MediaTek G700 architecture. Use this page when the KDS application is Android, not Windows KP-9795W.</p>",
		chips="Android KDS\nMediaTek G700\nRestaurant kitchen\nOrder preparation",
		story="Android hardware for kitchen display apps", visual="KP-9155W",
		card_title="KP-9155W", card_summary="Android FEC kitchen panel PC for restaurant KDS and food-service operations.",
		cta_h="Configure KP-9155W", cta_d="Confirm the Android KDS application and how the panel will be mounted in the kitchen.",
		meta_t="FEC KP-9155W Android Kitchen Display Saudi Arabia | KDS Touchscreen",
		meta_d="FEC KP-9155W Android kitchen panel PC for restaurant KDS, QSR kitchens, order preparation and food-service operations in Saudi Arabia.",
		benefits=[
			{"icon": "android", "title": "Android kitchen PC", "description": "MediaTek G700 platform as published by FEC for KP-9155W.", "sort_order": 1},
			{"icon": "durability", "title": "Back-of-house", "description": "Specified as a kitchen display panel, not a consumer tablet.", "sort_order": 2},
		],
		stories=[
			{"label": "KP-9155W", "image": m["src_kp-9155w-a"], "image_alt": "KP-9155W", "caption": "Android kitchen panel PC.", "sort_order": 1},
			{"label": "QSR", "image": m["app_qsr"], "image_alt": "QSR kitchen", "caption": "Order preparation lines.", "sort_order": 2},
		],
		icons=[{"icon": "android", "title": "Android", "description": "MediaTek G700", "sort_order": 1}],
		specs=[("Platform", [
			("Model", "KP-9155W"),
			("OS", "Android kitchen panel PC"),
			("Processor", "MediaTek G700"),
			("Use", "KDS and restaurant back-of-house"),
		])],
		apps=[
			app_row(m, "kitchen", "Android KDS", "Kitchen tickets on an Android commercial panel.", "Android kitchen display", "food-beverage", 1),
			app_row(m, "qsr", "QSR kitchens", "Fast-food and cafeteria preparation.", "QSR Android KDS", "food-beverage", 2),
		],
		sections=[_ksa_section(m["app_kitchen"], "Android kitchen display")],
		faqs=[{"question": "Will this run Windows KDS software?", "answer": "No. KP-9155W is Android (MediaTek G700). Use KP-9795W for Windows kitchen display software.", "sort_order": 1}],
		quote=[
			q_select("Application", "Kitchen use", ["Kitchen Display System", "QSR preparation", "Food production"], sort=1),
			q_select("Installation", "Mounting", ["Wall / bracket", "Shelf / stand", "Confirm during survey"], sort=2),
		],
		configure=1,
	)
	_p(
		m, "fec-xc-574", "FEC XC-574 Box PC", "Box PCs", "XCOMP",
		hero=m["xc-574"], card=m["xc-574"],
		tagline="H610 commercial box PC for POS, kiosk and signage",
		short="FEC's current product catalogue identifies XC-574 as its H610-based XCOMP platform — a high-performance commercial box PC when the computer is separate from the display.",
		long="<p>Typical uses are POS systems, kiosks, digital signage and embedded retail applications. Configure processor, memory, storage and OS on the quote.</p>",
		chips="XCOMP XC-574\nIntel H610\nPOS · kiosk · signage\nSeparated compute",
		story="Performance box PC for commercial enclosures", visual="XC-574",
		card_title="XC-574", card_summary="High-performance FEC XCOMP box PC on Intel H610 for POS, kiosk and signage.",
		cta_h="Configure XC-574", cta_d="Choose the H610 processor, memory, storage and Windows IoT build.",
		meta_t="FEC XC-574 Box PC Saudi Arabia | Commercial POS & Kiosk Computer",
		meta_d="FEC XC-574 high-performance commercial Box PC for POS, kiosks, digital signage and embedded retail applications. Available from Printechs Saudi Arabia.",
		benefits=[
			{"icon": "speed", "title": "H610 XCOMP", "description": "Higher-performance box platform versus the J6412 XC-373.", "sort_order": 1},
			{"icon": "device", "title": "Separate from the display", "description": "Hide the PC and pair it with FEC or third-party commercial screens.", "sort_order": 2},
		],
		stories=[
			{"label": "XC-574", "image": m["src_xc-574-a"], "image_alt": "XC-574", "caption": "H610 commercial box PC.", "sort_order": 1},
			{"label": "I/O", "image": m["src_xc-574-b"], "image_alt": "XC-574 ports", "caption": "POS, kiosk and signage I/O.", "sort_order": 2},
		],
		icons=[{"icon": "device", "title": "XC-574", "description": "H610 XCOMP", "sort_order": 1}],
		specs=[("Platform", [
			("Model", "XC-574"),
			("Family", "XCOMP"),
			("Chipset", "Intel H610"),
			("Use", "POS, kiosk, digital signage, embedded retail"),
		])],
		apps=[
			app_row(m, "enterprise", "Embedded retail PC", "Control stations and signage players.", "Commercial box PC", "retail", 1),
			app_row(m, "selfservice", "Kiosk computer", "Compute for unattended enclosures.", "Kiosk box PC", "retail", 2),
		],
		sections=[_integration_section(m["app_enterprise"], "Box PC + Modern POS"), _ksa_section(m["src_xc-574-b"], "XC-574")],
		faqs=[{"question": "XC-574 or XC-373?", "answer": "XC-574 is the H610 performance XCOMP. XC-373 is the compact Intel J6412 platform.", "sort_order": 1}],
		quote=panel_h610_quote_options(), configure=1,
	)
	_p(
		m, "fec-xc-373", "FEC XC-373 Fanless Box PC", "Box PCs", "XCOMP",
		hero=m["xc-373"], card=m["xc-373"],
		tagline="Compact Intel J6412 XCOMP for POS, kiosk and signage",
		short="FEC currently identifies the XC-373 XCOMP with an Intel J6412 platform — a compact commercial box PC for business applications where the display is separate.",
		long="<p>Use XC-373 when you want the smaller J6412 XCOMP rather than the H610 XC-574. Memory, storage and OS are set on the quote.</p>",
		chips="XCOMP XC-373\nIntel J6412\nCompact box PC\nPOS · kiosk · signage",
		story="Compact XCOMP next to the display", visual="XC-373",
		card_title="XC-373", card_summary="Compact FEC XCOMP box PC with Intel J6412 for POS, kiosk and digital signage.",
		cta_h="Configure XC-373", cta_d="Set memory, storage and Windows IoT on the J6412 box platform.",
		meta_t="FEC XC-373 Fanless Box PC Saudi Arabia | POS & Kiosk Computer",
		meta_d="FEC XC-373 compact commercial Box PC with Intel J6412 platform for POS, kiosks, digital signage and business applications in Saudi Arabia.",
		benefits=[
			{"icon": "device", "title": "Compact J6412", "description": "Smaller XCOMP platform published by FEC for XC-373.", "sort_order": 1},
			{"icon": "durability", "title": "Quiet commercial PC", "description": "Suitable when the computer is hidden in a counter or kiosk.", "sort_order": 2},
		],
		stories=[
			{"label": "XC-373", "image": m["src_xc-373-a"], "image_alt": "XC-373", "caption": "Compact J6412 box PC.", "sort_order": 1},
			{"label": "Ports", "image": m["src_xc-373-b"], "image_alt": "XC-373 ports", "caption": "Commercial I/O for POS and signage.", "sort_order": 2},
		],
		icons=[{"icon": "device", "title": "XC-373", "description": "J6412 XCOMP", "sort_order": 1}],
		specs=[("Platform", [
			("Model", "XC-373"),
			("Family", "XCOMP"),
			("Processor", "Intel J6412"),
			("Use", "POS, kiosk, digital signage, business PC"),
		])],
		apps=[
			app_row(m, "enterprise", "Business box PC", "Hidden compute for counters and control desks.", "Fanless box PC", "retail", 1),
			app_row(m, "selfservice", "Kiosk / signage", "Compact PC beside a commercial display.", "Kiosk computer", "retail", 2),
		],
		sections=[_ksa_section(m["src_xc-373-b"], "XC-373")],
		faqs=[{"question": "Is XC-373 fanless?", "answer": "FEC positions XC-373 as the compact J6412 XCOMP. Confirm cooling and enclosure limits on the quote for your install.", "sort_order": 1}],
		quote=[
			q_select("Platform", "Memory", ["8 GB DDR4", "16 GB DDR4"], sort=1),
			q_select("Platform", "Storage", ["128 GB SSD", "256 GB SSD", "512 GB SSD"], sort=2),
			q_select("Software", "Operating system", ["Windows 10 IoT Enterprise", "Windows 11 IoT Enterprise", "No OS (hardware only)"], sort=3),
		],
		configure=1,
	)
	_p(
		m, "fec-ld-9043w", "FEC LD-9043W 42.5″ Commercial Touch Display", "Touch Monitors", "XMONITOR",
		hero=m["ld-9043w"], card=m["ld-9043w"],
		tagline="42.5-inch Full HD PCAP display for signage, kitchen and customer screens",
		short="FEC promotes the LD-9043W for second-screen, marketing, digital signage and kitchen applications.",
		long="<p>Important published specifications: 42.5-inch TFT, 1920 × 1080 Full HD, true-flat PCAP touch, 500 nits, 50,000-hour MTBF, HDMI, VGA, USB, VESA 400 × 400, optional anti-glare coating and optional hovering-touch support.</p>",
		chips="42.5″ Full HD\nTrue-flat PCAP\n500 nits · 50,000 h MTBF\nHDMI · VGA · VESA 400×400",
		story="A large commercial touch display, not a TV", visual="LD-9043W",
		card_title="LD-9043W", card_summary="42.5-inch Full HD commercial touch display for signage, kitchen and interactive screens.",
		cta_h="Configure LD-9043W", cta_d="Choose anti-glare or hovering-touch options and how the 400 × 400 VESA mount will be installed.",
		meta_t="FEC LD-9043W 43″ Touch Display Saudi Arabia | Commercial Monitor",
		meta_d="FEC LD-9043W 42.5-inch Full HD commercial touch display for digital signage, kitchen displays, customer screens and interactive applications.",
		benefits=[
			{"icon": "display", "title": "42.5″ Full HD PCAP", "description": "True-flat projected capacitive touch at 1920 × 1080.", "sort_order": 1},
			{"icon": "durability", "title": "500 nits · 50,000 h MTBF", "description": "Commercial brightness and published lifetime, not a consumer television.", "sort_order": 2},
			{"icon": "connectivity", "title": "HDMI, VGA, USB", "description": "VESA 400 × 400 mounting for walls, arms or kitchen brackets.", "sort_order": 3},
		],
		stories=[
			{"label": "LD-9043W", "image": m["src_ld-9043w-a"], "image_alt": "LD-9043W", "caption": "42.5-inch commercial touch display.", "sort_order": 1},
			{"label": "Install", "image": m["src_ld-9043w-b"], "image_alt": "LD-9043W angle", "caption": "Signage, kitchen or customer screen.", "sort_order": 2},
		],
		icons=[
			{"icon": "display", "title": "42.5″ FHD", "description": "1920 × 1080 PCAP", "sort_order": 1},
			{"icon": "durability", "title": "500 nits", "description": "50,000-hour MTBF", "sort_order": 2},
		],
		specs=[
			("Display", [
				("Size", "42.5-inch TFT"),
				("Resolution", "1920 × 1080 Full HD"),
				("Touch", "True-flat PCAP"),
				("Brightness", "500 nits"),
				("MTBF", "50,000 hours"),
			]),
			("Connectivity & options", [
				("Video", "HDMI, VGA"),
				("Touch interface", "USB"),
				("Mounting", "VESA 400 × 400"),
				("Options", "Anti-glare coating; hovering-touch support"),
			]),
		],
		apps=[
			app_row(m, "enterprise", "Digital signage", "Lobby and marketing second screens.", "Commercial touch display", "retail", 1),
			app_row(m, "kitchen", "Kitchen display", "Large-format KDS or production boards.", "Kitchen touch display", "food-beverage", 2),
			app_row(m, "selfservice", "Interactive information", "Customer-facing interactive screens.", "Interactive display", "retail", 3),
		],
		sections=[_ksa_section(m["app_enterprise"], "Commercial display in KSA")],
		faqs=[
			{"question": "Is it 43-inch or 42.5-inch?", "answer": "FEC specifies 42.5-inch. Marketing often says 43-inch. The published panel size is 42.5-inch Full HD.", "sort_order": 1},
			{"question": "Do you have 22-inch and 32-inch?", "answer": "FEC lists LD-9022W and LD-9032W. Those pages follow this first batch — ask on the quote if you need them now.", "sort_order": 2},
		],
		quote=[
			q_check("Options", "Published options", ["Anti-glare coating", "Hovering-touch support"], sort=1),
			q_select("Installation", "Mounting", ["VESA 400 × 400 wall / arm", "Stand / trolley", "Confirm during survey"], sort=2),
		],
		configure=1,
	)
	_p(
		m, "fec-tp-100", "FEC TP-100 Thermal Receipt Printer", "POS Peripherals", "PERIPHERALS",
		hero=m["tp-100"], card=m["tp-100"],
		tagline="Compact 80 mm POS printer with USB, serial and Ethernet",
		short="FEC TP-100 is a compact thermal POS receipt printer with USB, serial and Ethernet connectivity, up to 250 mm/s printing and 80 mm printable width.",
		long="<p>Published specifications include thermal printing, maximum 250 mm/sec, serial, USB and Ethernet, 57.5 / 80 / 82.5 mm media support, maximum printable width 80 mm, full or partial cutter, and a compact 127 × 134 × 127 mm body.</p>",
		chips="Thermal 80 mm\nUp to 250 mm/s\nUSB · serial · Ethernet\nFull or partial cutter",
		story="The receipt printer for an FEC workstation", visual="TP-100",
		card_title="TP-100", card_summary="Compact FEC 80 mm thermal POS receipt printer with USB, serial and Ethernet.",
		cta_h="Configure TP-100", cta_d="Choose media width and full or partial cutter for the checkout or kiosk.",
		meta_t="FEC TP-100 Thermal Receipt Printer Saudi Arabia | 80mm POS Printer",
		meta_d="FEC TP-100 compact thermal POS receipt printer with USB, serial and Ethernet connectivity, up to 250 mm/s printing and 80mm printable width.",
		benefits=[
			{"icon": "print", "title": "Up to 250 mm/s", "description": "Thermal receipts at commercial checkout speed.", "sort_order": 1},
			{"icon": "connectivity", "title": "USB, serial, Ethernet", "description": "Connect to FEC terminals, kiosks or other POS PCs.", "sort_order": 2},
			{"icon": "device", "title": "Compact body", "description": "127 × 134 × 127 mm with full or partial cutter.", "sort_order": 3},
		],
		stories=[
			{"label": "TP-100", "image": m["src_tp-100-a"], "image_alt": "TP-100", "caption": "Compact 80 mm thermal printer.", "sort_order": 1},
			{"label": "Counter", "image": m["src_tp-100-b"], "image_alt": "TP-100 angle", "caption": "USB, serial and Ethernet POS printer.", "sort_order": 2},
		],
		icons=[
			{"icon": "print", "title": "250 mm/s", "description": "80 mm printable width", "sort_order": 1},
			{"icon": "connectivity", "title": "3 interfaces", "description": "USB · serial · Ethernet", "sort_order": 2},
		],
		specs=[
			("Printer", [
				("Type", "Thermal receipt printer"),
				("Speed", "Maximum 250 mm/sec"),
				("Printable width", "80 mm"),
				("Media", "57.5 / 80 / 82.5 mm"),
				("Cutter", "Full or partial"),
				("Interfaces", "Serial, USB, Ethernet"),
				("Body", "127 × 134 × 127 mm"),
			]),
		],
		apps=[
			app_row(m, "grocery", "Retail checkout", "Receipts at grocery and specialty POS.", "POS receipt printer", "retail", 1),
			app_row(m, "qsr", "Hospitality & QSR", "Order receipts at cafés and quick service.", "Hospitality receipt printer", "food-beverage", 2),
		],
		sections=[_integration_section(m["app_grocery"], "Receipt printer + Modern POS"), _ksa_section(m["src_tp-100-b"], "TP-100")],
		faqs=[{"question": "Does TP-100 include USB, serial and Ethernet?", "answer": "Yes. FEC publishes serial, USB and Ethernet on TP-100. Choose media width and cutter type on the quote.", "sort_order": 1}],
		quote=[
			q_select("Media", "Paper width", ["57.5 mm", "80 mm", "82.5 mm"], sort=1),
			q_select("Cutter", "Cutter type", ["Full cutter", "Partial cutter"], sort=2),
		],
		configure=1,
	)


def fill_fec():
	media = prepare_media()
	update_website_brand(media["logo"])
	fill_hub(media)
	fill_families(media)
	fill_products(media)
	for slug, related in RELATED.items():
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		set_related(doc, related)
		if slug == "fec-pos-systems":
			doc.final_cta_primary_label = "Talk to a POS Hardware Specialist"
			doc.final_cta_primary_href = "/contact"
			doc.final_cta_secondary_label = "Request a Quote"
			doc.final_cta_secondary_href = "/products/fec-pos-systems/quote"
		doc.flags.ignore_permissions = True
		doc.save()
	frappe.db.commit()
	print("Wired FEC related products and brand")
	return "ok"
