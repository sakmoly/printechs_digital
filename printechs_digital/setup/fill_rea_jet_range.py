# Copyright (c) 2026, Printechs and contributors
"""REA JET range for Printechs — all US overview families except small-character CIJ.

Sources:
https://reajetus.com/product-overviews/
https://www.rea-jet.com/en/products/coding-and-marking-systems/
https://www.rea-jet.com/en/products/laser-systems/
https://www.rea-verifier.com/en/

Excluded: REA JET SC 2.0 / CIJ, DOD 1.X, HR 1.0 (superseded by HR 2.0),
HR pro OEM, NiceLabel, consumable Items.
"""

from printechs_digital.setup.rea_jet_common import (
	ASSETS,
	apply_identity,
	catalog_card,
	cover_card,
	get_or_create,
	ksa_section,
	official_image,
	save_product,
	set_related,
	set_specs,
	support_items,
	video_section,
)

# Official REA JET / REA LASER / REA VERIFIER films from rea-jet.com embeds.
# Unique YouTube ID per page. Never set Website Product.video_url (hero poster).
VIDEO_TITAN = "https://youtu.be/Zgj-7I_x97M"
VIDEO_HR = "https://youtu.be/k-XQxdtIi1s"
VIDEO_GK2 = "https://youtu.be/6MRNFPG1wpM"
VIDEO_UP = "https://youtu.be/dsaU83BSCEo"
VIDEO_LASER = "https://youtu.be/PXjbmx4Br30"
VIDEO_SPRAY = "https://youtu.be/9lUs8ecSMsg"
VIDEO_VERIFY = "https://youtu.be/D5IkuMp22cI"

import frappe


def _media():
	return {
		"hub": cover_card(ASSETS / "rea-jet-hub-overview.png", "rea-jet-hub-product.jpg"),
		"hub_wide": cover_card(ASSETS / "rea-jet-hub-overview.png", "rea-jet-hub-hero.jpg", (1600, 1000)),
		"hr2": catalog_card("rea-jet-hr2-1sk.jpg", "rea-jet-hr2-product.jpg"),
		"hr2_overview": official_image("rea-jet-hr2-overview.jpg"),
		"hr2_4sk": official_image("rea-jet-hr2-4sk.jpg"),
		"hr2_wet": official_image("rea-jet-hr2-wet.png"),
		"hr2_pouch": official_image("rea-jet-hr2-pouch.jpg"),
		"hr2_pipe": official_image("rea-jet-hr2-pipe.jpg"),
		"hr2_pharma": official_image("rea-jet-hr2-pharma.jpg"),
		"hr2_fiber": official_image("rea-jet-hr2-fiberglass.jpg"),
		"hr2_packs": official_image("rea-jet-hr2-packs.png"),
		"hr2_metal": official_image("rea-jet-hr2-metal.jpg"),
		"hr2_wood": official_image("rea-jet-hr2-wood.jpg"),
		"up": catalog_card("rea-jet-up-overview.png", "rea-jet-up-product.jpg"),
		"up_kombi": official_image("rea-jet-up-kombi.jpg"),
		"up_c1": official_image("rea-jet-up-carton-01.jpg"),
		"up_c3": official_image("rea-jet-up-carton-03.jpg"),
		"up_c4": official_image("rea-jet-up-carton-04.jpg"),
		"up_c8": official_image("rea-jet-up-carton-08.jpg"),
		"up_wood": official_image("rea-jet-up-wood.jpg"),
		"up_sec": official_image("rea-jet-up-secondary.jpg"),
		"gk2": catalog_card("rea-jet-gk2-overview.png", "rea-jet-gk2-product.jpg"),
		"gk2_384": official_image("rea-jet-gk2-384.jpg"),
		"gk2_768": official_image("rea-jet-gk2-768.jpg"),
		"gk2_hose": official_image("rea-jet-gk2-hose.jpg"),
		"gk2_pallet": official_image("rea-jet-gk2-pallet.jpg"),
		"gk2_carton": official_image("rea-jet-gk2-carton.jpg"),
		"gk2_bags": official_image("rea-jet-gk2-bags.jpg"),
		"gk2_plaster": official_image("rea-jet-gk2-plaster.jpg"),
		"cl": catalog_card("rea-jet-cl-product.jpg", "rea-jet-cl-card.jpg"),
		"cl_kombi": official_image("rea-jet-cl-kombi.jpg"),
		"cl_head": official_image("rea-jet-cl-head.jpg"),
		"cl_wood": official_image("rea-jet-cl-wood.jpg"),
		"cl_capsules": official_image("rea-jet-cl-capsules.jpg"),
		"cl_profile": official_image("rea-jet-cl-profile.jpg"),
		"cl_pharma": official_image("rea-jet-cl-pharma.jpg"),
		"cl_tire": official_image("rea-jet-cl-tire.jpg"),
		"fl": catalog_card("rea-jet-fl-product.jpg", "rea-jet-fl-card.jpg"),
		"fl_m2": official_image("rea-jet-fl-metal-02.jpg"),
		"fl_m3": official_image("rea-jet-fl-metal-03.jpg"),
		"fl_plastic": official_image("rea-jet-fl-plastic.jpg"),
		"fl_tweezers": official_image("rea-jet-fl-tweezers.jpg"),
		"fl_cap": official_image("rea-jet-fl-cap.jpg"),
		"fl_m1": official_image("rea-jet-fl-metal-01.jpg"),
		"spray": catalog_card("rea-jet-stc-system.jpg", "rea-jet-spray-product.jpg"),
		"stc_piston": official_image("rea-jet-stc-piston.jpg"),
		"stc_color": official_image("rea-jet-stc-color.jpg"),
		"stc_shaft": official_image("rea-jet-stc-shaft.jpg"),
		"stc_line": official_image("rea-jet-stc-line.jpg"),
		"stf_system": official_image("rea-jet-stf-system.png"),
		"stf_heads": official_image("rea-jet-stf-heads.jpg"),
		"stf_units": official_image("rea-jet-stf-units.jpg"),
		"stf_ring": official_image("rea-jet-stf-ring.jpg"),
		"stf_cable": official_image("rea-jet-stf-cable.jpg"),
		"eds_heads": official_image("rea-jet-eds-heads.jpg"),
		"eds_coupling": official_image("rea-jet-eds-coupling.jpg"),
		"verify": cover_card(ASSETS / "rea-jet-vericube-scene.png", "rea-jet-verify-product.jpg"),
		"pcscan": cover_card(ASSETS / "rea-jet-pcscan-scene.png", "rea-jet-pcscan.jpg", (1600, 1000)),
	}


RELATED = {
	"rea-jet-coding-systems": [
		"rea-jet-dod-2",
		"rea-jet-hr-2",
		"rea-jet-gk-2",
		"rea-jet-up",
		"rea-jet-cl",
		"rea-jet-fl",
		"rea-jet-spray-mark",
		"rea-jet-code-verification",
	],
	"rea-jet-hr-2": ["rea-jet-coding-systems", "rea-jet-gk-2", "rea-jet-up", "rea-jet-dod-2"],
	"rea-jet-gk-2": ["rea-jet-coding-systems", "rea-jet-up", "rea-jet-hr-2", "rea-jet-dod-2"],
	"rea-jet-up": ["rea-jet-coding-systems", "rea-jet-gk-2", "rea-jet-hr-2", "rea-jet-cl"],
	"rea-jet-cl": ["rea-jet-coding-systems", "rea-jet-fl", "rea-jet-up", "rea-jet-dod-2"],
	"rea-jet-fl": ["rea-jet-coding-systems", "rea-jet-cl", "rea-jet-spray-mark", "rea-jet-dod-2"],
	"rea-jet-spray-mark": ["rea-jet-coding-systems", "rea-jet-dod-2", "rea-jet-fl", "rea-jet-hr-2"],
	"rea-jet-code-verification": ["rea-jet-coding-systems", "rea-jet-hr-2", "rea-jet-up", "rea-jet-dod-2"],
}


def fill_hub(m):
	slug = "rea-jet-coding-systems"
	doc = get_or_create(slug, "REA JET Coding Systems", m["hub"])
	apply_identity(
		doc,
		slug=slug,
		display_name="REA JET Coding Systems",
		category_label="INDUSTRIAL CODING RANGE",
		subcategory="Coding & Marking",
		featured=1,
		is_hub=1,
	)
	doc.tagline = "Large-character, high-resolution, laser, spray mark and verification — one TITAN concept"
	doc.short_description = (
		"REA JET industrial coding for Saudi lines: DOD 2.0 large character, HR 2.0 thermal "
		"inkjet, GK 2.0 and UP piezo, CL / FL lasers, spray mark and REA VERIFIER. "
		"Printechs specifies, installs and services the range."
	)
	doc.long_description = (
		"<p>This is the REA JET range Printechs supplies in Saudi Arabia — mapped from the "
		"official <a href=\"https://reajetus.com/product-overviews/\">product overview</a> "
		"and current <a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/\">"
		"REA JET coding systems</a>. Small-character CIJ (SC 2.0) is not on this page.</p>"
		"<p><strong>Choose by the mark, not the brochure.</strong> "
		"<a href=\"/products/rea-jet-dod-2\">DOD 2.0</a> — large, readable codes on bags, "
		"pipe, steel and wood (up to 140 mm per head). "
		"<a href=\"/products/rea-jet-hr-2\">HR 2.0</a> — 600 dpi HP-cartridge thermal inkjet "
		"for dates, 1D/2D and serialization at up to 762 m/min. "
		"<a href=\"/products/rea-jet-gk-2\">GK 2.0</a> — piezo on absorbent carton, pallet "
		"and paper (up to 100 mm). "
		"<a href=\"/products/rea-jet-up\">UP</a> — high-resolution piezo on coated and "
		"painted packs (up to 108 mm). "
		"<a href=\"/products/rea-jet-cl\">CL</a> CO2 and <a href=\"/products/rea-jet-fl\">FL</a> "
		"fiber lasers for permanent, consumable-free marks. "
		"<a href=\"/products/rea-jet-spray-mark\">Spray mark</a> for paint dots, rings and "
		"reject marks. "
		"<a href=\"/products/rea-jet-code-verification\">Code verification</a> grades 1D and 2D.</p>"
		"<p>Every REA JET printer shares the TITAN operating concept. Operators train once. "
		"Printechs surveys substrate and speed in Riyadh, Jeddah and Dammam, then quotes "
		"the matching family — not a mixed SKU.</p>"
	)
	doc.hero_image = m["hub"]
	doc.card_image = m["hub"]
	doc.hero_image_alt = "Industrial coding cell with carton 2D codes, large-character bags and laser-marked metal"
	doc.hero_trust_chips = "DOD · TIJ · Piezo · Laser\nSpray mark · Verification\nTITAN one HMI\nRiyadh · Jeddah · Dammam"
	doc.story_heading = "The right REA JET technology for the pack in front of you"
	doc.visual_story_heading = "Official REA JET families — each on its own page"
	doc.card_title = "REA JET range"
	doc.card_summary = (
		"Large-character DOD, high-resolution TIJ and piezo, CO2 and fiber laser, spray "
		"mark and verification — specified by Printechs in Saudi Arabia."
	)
	doc.final_cta_heading = "Specify the REA JET family for your line"
	doc.final_cta_description = (
		"Send the pack, speed and code. We will map DOD, HR, GK, UP, laser, spray or verify."
	)
	doc.meta_title = "REA JET Coding Systems Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA JET DOD 2.0, HR 2.0, GK 2.0, UP, CL/FL lasers, spray mark and verification "
		"from Printechs in Saudi Arabia. Small-character CIJ excluded."
	)
	doc.set(
		"benefits",
		[
			{"icon": "print", "title": "Every mark type", "description": "Large character, high-res inkjet, laser, paint spray and ISO code grading.", "sort_order": 1},
			{"icon": "display", "title": "One TITAN HMI", "description": "Ink, paint and laser share one operating concept — shorter training.", "sort_order": 2},
			{"icon": "speed", "title": "Line-speed coding", "description": "HR 2.0 to 762 m/min. DOD 2.0 to 600 m/min. Lasers for permanent IDs.", "sort_order": 3},
			{"icon": "shield", "title": "Harsh halls", "description": "IP65 inkjet cabinets and consumable-free lasers for dusty or wet plants.", "sort_order": 4},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{"label": "DOD 2.0", "image": official_image("rea-jet-dod-2-heads.jpg") if False else m["hr2_packs"], "image_alt": "High-resolution REA JET codes on primary packs", "caption": "HR 2.0 dates and 2D on packs — DOD 2.0 handles the large bag and beam marks.", "sort_order": 1},
			{"label": "HR 2.0", "image": m["hr2_overview"], "image_alt": "REA JET HR 2.0 thermal inkjet system overview", "caption": "Current thermal inkjet — not SC 2.0 CIJ, not HR 1.0.", "sort_order": 2},
			{"label": "UP piezo", "image": m["up_kombi"], "image_alt": "REA JET UP piezo printer with print samples", "caption": "High-contrast carton and wood marks up to 108 mm.", "sort_order": 3},
			{"label": "Fiber laser", "image": m["fl_m1"], "image_alt": "REA LASER FL permanent mark on metal", "caption": "FL for metals and plastics. CL for organics, glass and rubber.", "sort_order": 4},
		],
	)
	# Fix first story item — do not invent dod-2-heads if we said we wouldn't reuse.
	# hr2_packs is unique to hub+HR page... wait HR page will also use hr2_packs.
	# Hub visual story cannot reuse SKU images. Use hub_wide and generated only?
	# Official images on hub that we reserve ONLY for hub:
	# I used hr2_overview, up_kombi, fl_m1, hr2_packs — those will also be on SKU pages.
	# Standing rule: don't duplicate the same product image across pages.
	# Hub related cards already show SKU card images (standard). Visual story should be unique.
	# Use hub_wide only + we need unique extras. I reserved nothing unique except hub photos.
	# Simplest: hub visual story uses only hub_wide cropped variants? That's duplicate of hero.
	# Better: DON'T put a visual story on hub, or use only the generated hub image once as hero
	# and skip visual story items that steal SKU photos.
	doc.set("visual_story_items", [])
	doc.visual_story_heading = ""
	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "DOD 2.0", "description": "Large character · 140 mm", "sort_order": 1},
			{"icon": "speed", "title": "HR 2.0", "description": "TIJ · 762 m/min · 600 dpi", "sort_order": 2},
			{"icon": "print", "title": "GK 2.0 / UP", "description": "Piezo · carton & coated", "sort_order": 3},
			{"icon": "scan", "title": "CL · FL · Verify", "description": "Laser + ISO grading", "sort_order": 4},
		],
	)
	set_specs(
		doc,
		[
			(
				"Range",
				[
					("Brand", "REA JET — supplied and supported by Printechs"),
					("Large character", "DOD 2.0 drop-on-demand — 7 / 16 / 32-nozzle heads"),
					("Thermal inkjet", "HR 2.0 (current TIJ). HR 1.0 is the previous generation — not this hub SKU"),
					("Piezo", "GK 2.0 on absorbent packs; UP on coated / painted surfaces"),
					("Laser", "REA LASER CL (CO2) and FL (fiber). Marking station quoted with the laser"),
					("Spray mark", "STC One-Dot, STF turnkey and EDS fine dots — one family page"),
					("Verification", "REA VERIFIER 1D and 2D (VeriCube / PC-Scan)"),
					("Not on this range", "SC 2.0 small-character CIJ, DOD 1.X, ink bottles and spare parts"),
				],
			),
			(
				"How we quote",
				[
					("Operating concept", "REA JET TITAN — one HMI across ink, paint and laser"),
					("KSA", "Survey, install and service from Riyadh, Jeddah and Dammam"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{"title": "Primary packs", "description": "Dates, lots and 2D on film, bottles and pharma cartons with HR 2.0 or laser.", "image": m["hr2_pouch"], "image_alt": "Film pouch coded with REA JET HR 2.0", "industry_link": "food-beverage", "sort_order": 1},
			{"title": "Secondary packs", "description": "Carton, pallet and bag marks with GK 2.0, UP or DOD 2.0.", "image": m["gk2_carton"], "image_alt": "Carton coding with REA JET GK 2.0", "industry_link": "packaging", "sort_order": 2},
			{"title": "Metal and parts", "description": "Permanent FL marks or spray-mark quality dots on shafts, springs and cable.", "image": m["fl_m2"], "image_alt": "Fiber laser mark on a metal part", "industry_link": "steel", "sort_order": 3},
		],
	)
	# Applications reuse SKU images - related cards do this too. Applications on hub showing
	# child application photos is common. The hard rule is hero/card uniqueness.
	# SKU heroes are product cutouts; these are application shots. OK if also on SKU pages
	# as applications. To be strict, I could leave applications with hub image only.
	# I'll keep unique-enough: hub applications use shots that SKUs also use as gallery.
	# That's the same image on two pages. Safer to use hub_wide for apps or omit.
	doc.set(
		"applications",
		[
			{"title": "Primary packs", "description": "Dates, lots and 2D on film, bottles and pharma cartons with HR 2.0 or laser.", "image": m["hub_wide"], "image_alt": "Industrial coding on cartons, bags and metal parts", "industry_link": "food-beverage", "sort_order": 1},
			{"title": "Secondary packs", "description": "Carton, pallet and bag marks with GK 2.0, UP or DOD 2.0.", "image": m["hub"], "image_alt": "Factory coding cell for secondary packaging", "industry_link": "packaging", "sort_order": 2},
		],
	)
	doc.set(
		"content_sections",
		[
			video_section(
				heading="One TITAN operating concept",
				body=(
					"REA’s official TITAN film — the same controller language across DOD, "
					"HR, GK, UP, laser and spray. Plays in this section, not on the hero "
					"photo. Unique to this hub."
				),
				video_url=VIDEO_TITAN,
				image=m["hub_wide"],
				image_alt="REA JET TITAN platform across coding technologies",
				sort_order=1,
			),
			{
				"section_type": "Industry Solution",
				"heading": "Not small-character CIJ",
				"body": (
					"SC 2.0 is REA’s continuous inkjet for tiny high-speed codes on foil and "
					"metal. This hub and its child pages are DOD, TIJ, piezo, laser, spray and "
					"verification only. If you need CIJ, ask for Hitachi UX2 — not a REA SC page."
				),
				"image": m["hub_wide"],
				"image_alt": "REA JET industrial coding overview",
				"link_label": "Open DOD 2.0",
				"link_href": "/products/rea-jet-dod-2",
				"sort_order": 2,
			},
			ksa_section(m["hub"], "Printechs specifying REA JET on a Saudi production line", 3),
		],
	)
	doc.set("support_items", support_items("Genuine REA inks & cartridges"))
	doc.set("package_contents", [
		{"item_description": "Quoted REA JET family (DOD, HR, GK, UP, laser, spray or verifier)", "sort_order": 1},
		{"item_description": "TITAN controller, photocell/encoder and KSA commissioning as surveyed", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "Which REA JET do I need?", "answer": "Large readable marks on bags/pipe/steel → DOD 2.0. Fine dates and 2D on packs → HR 2.0. Absorbent cartons/pallets → GK 2.0. Coated packs and logos → UP. Permanent no-ink → CL (organics) or FL (metal/plastic). Paint dots → spray mark. Grade the code → verification.", "sort_order": 1},
		{"question": "Do you sell REA JET small-character CIJ?", "answer": "Not on this range. SC 2.0 is excluded. For high-speed small codes we specify Hitachi UX2.", "sort_order": 2},
		{"question": "Is HR 1.0 still listed?", "answer": "REA’s current thermal inkjet is HR 2.0. We quote HR 2.0, not the previous HR 1.0 generation.", "sort_order": 3},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_hr2(m):
	slug = "rea-jet-hr-2"
	doc = get_or_create(slug, "REA JET HR 2.0", m["hr2"])
	apply_identity(doc, slug=slug, display_name="REA JET HR 2.0", category_label="THERMAL INKJET", subcategory="High-Resolution Inkjet")
	doc.tagline = "HP-cartridge TIJ — up to 600 × 1,500 dpi and 762 m/min"
	doc.short_description = (
		"REA JET HR 2.0 is the current thermal inkjet: a new print unit with every cartridge, "
		"up to 12.7 mm per head, 90 serialized prints/s and IP65 TITAN control. Dates, 1D/2D "
		"and logos on film, pharma packs, pipe and wood."
	)
	doc.long_description = (
		"<p>HR 2.0 is REA’s current high-resolution thermal inkjet — not HR 1.0, not GK piezo, "
		"not SC 2.0 CIJ. Official page: "
		"<a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-hr-2\">"
		"REA JET HR 2.0</a>.</p>"
		"<p>Each cartridge change fits a new print unit, so the head stays service-free. "
		"Vertical resolution is 300 or 600 dpi; horizontal 60–1,500 dpi in 26 steps. "
		"REA rates speed at up to 762 m/min and up to 90 serialized prints per second. "
		"Print height is 12.7 mm per head; two heads reach 25.4 mm, four heads 50.8 mm.</p>"
		"<p>Two TITAN controllers: 2SK (5.7\" rotary, two heads) and 4SK (10.1\" touch, "
		"four heads). Cabinet IP65, 24 V DC from an IP67 100–277 VAC supply. Ethernet "
		"1 Gbit and 3× USB. Optional bulk ink for high throughput. Wet-on-wet prints a "
		"colour field and code in one pass — a label alternative on metal and film.</p>"
		"<p>Printechs specifies cartridge type (standard, pigmented, food-approved, UV, "
		"fluorescent) to the pack in Saudi Arabia. Controllers shown on DOD 2.0 are the "
		"same TITAN family — we do not repeat those photos here.</p>"
	)
	doc.hero_image = m["hr2"]
	doc.card_image = m["hr2"]
	doc.hero_image_alt = "REA JET HR 2.0 thermal inkjet print head on a sliding plate"
	doc.hero_trust_chips = "Up to 600 × 1,500 dpi\n762 m/min · 90 prints/s\n12.7 mm per head\nIP65 · TITAN"
	doc.story_heading = "High-resolution dates, 2D and wet-on-wet without a label"
	doc.visual_story_heading = "Official HR 2.0 heads and print samples"
	doc.card_title = "HR 2.0"
	doc.card_summary = "Current REA thermal inkjet: 600 dpi, 762 m/min, HP cartridge — dates, 2D and serialization."
	doc.final_cta_heading = "Specify HR 2.0 for high-resolution packs"
	doc.final_cta_description = "Printechs will confirm 2SK vs 4SK, cartridge chemistry and encoder for your line."
	doc.meta_title = "REA JET HR 2.0 Thermal Inkjet Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA JET HR 2.0 TIJ: 600×1500 dpi, 762 m/min and IP65. High-resolution coding from "
		"Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "speed", "title": "762 m/min", "description": "REA’s fastest TIJ class — up to 90 serialized prints per second.", "sort_order": 1},
		{"icon": "scan", "title": "GS1-ready 2D", "description": "High first-pass rates on retail 2D and track-and-trace codes.", "sort_order": 2},
		{"icon": "maintenance", "title": "New unit every cartridge", "description": "No service printhead — swap the cartridge and keep running.", "sort_order": 3},
		{"icon": "print", "title": "Wet-on-wet", "description": "Colour field plus code in one pass — print instead of a label.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "System", "image": m["hr2_overview"], "image_alt": "REA JET HR 2.0 system overview", "caption": "Compact HR 2.0 — current TIJ generation.", "sort_order": 1},
		{"label": "Four heads", "image": m["hr2_4sk"], "image_alt": "REA JET HR 2.0 with four print heads", "caption": "4SK controller: up to 50.8 mm combined height.", "sort_order": 2},
		{"label": "Pharma", "image": m["hr2_pharma"], "image_alt": "HR 2.0 serialization on pharmaceutical packaging", "caption": "Serialization and late-stage customization.", "sort_order": 3},
		{"label": "Film pouch", "image": m["hr2_pouch"], "image_alt": "HR 2.0 food-approved ink on a film pouch", "caption": "Food-approved inks for primary film.", "sort_order": 4},
		{"label": "Pipe", "image": m["hr2_pipe"], "image_alt": "HR 2.0 marking on a water pipe", "caption": "DIN-style marks on extruded pipe.", "sort_order": 5},
		{"label": "Wet-on-wet", "image": m["hr2_metal"], "image_alt": "HR 2.0 wet-on-wet print on metal profiles", "caption": "Direct print on metal instead of a label.", "sort_order": 6},
	])
	doc.set("icon_specifications", [
		{"icon": "speed", "title": "762 m/min", "description": "Speed potential", "sort_order": 1},
		{"icon": "print", "title": "600 × 1,500 dpi", "description": "Vertical × horizontal", "sort_order": 2},
		{"icon": "display", "title": "2 or 4 heads", "description": "25.4 or 50.8 mm", "sort_order": 3},
		{"icon": "rugged", "title": "IP65", "description": "TITAN cabinet", "sort_order": 4},
	])
	set_specs(doc, [
		("Print", [
			("Technology", "Thermal inkjet (TIJ) with HP cartridge"),
			("Resolution", "300/600 dpi vertical; 60–1,500 dpi horizontal in 26 steps"),
			("Speed", "Up to 762 m/min; up to 90 serialized prints/s"),
			("Height", "12.7 mm per head; 25.4 mm (2 heads); 50.8 mm (4 heads)"),
			("Not this page", "HR 1.0 previous TIJ, GK/UP piezo, SC 2.0 CIJ, DOD 2.0"),
		]),
		("Controller", [
			("2SK", "5.7\" rotary HMI, two heads, about 3.9 kg"),
			("4SK", "10.1\" touch HMI, four heads, about 6.0 kg"),
			("I/O", "6 digital in / 4 digital out, 24 V DC; Ethernet 1 Gbit; 3× USB"),
			("Protection", "IP65 cabinet; IP67 100–277 VAC supply"),
		]),
	])
	doc.set("applications", [
		{"title": "Pharma serialization", "description": "2D and human-readable on folding boxes at line speed.", "image": m["hr2_pharma"], "image_alt": "HR 2.0 on pharma packs", "industry_link": "pharmaceutical", "sort_order": 1},
		{"title": "Food film", "description": "Best-before on pouches with food-approved ink.", "image": m["hr2_pouch"], "image_alt": "HR 2.0 on a film pouch", "industry_link": "food-beverage", "sort_order": 2},
		{"title": "Wood edge", "description": "CE and production data on cut timber edges.", "image": m["hr2_wood"], "image_alt": "HR 2.0 on a wood cut edge", "industry_link": "packaging", "sort_order": 3},
	])
	doc.set("content_sections", [
		video_section(
			heading="Official HR thermal-inkjet film",
			body=(
				"REA’s official HR film (HP cartridge TIJ). HR 2.0 is the current compact "
				"generation of this family. The clip plays here — not on the hero photo — "
				"and is unique to this page."
			),
			video_url=VIDEO_HR,
			image=m["hr2_packs"],
			image_alt="HR 2.0 print samples on packaging",
			sort_order=1,
		),
		{
			"section_type": "Core Module",
			"heading": "Cartridge chemistry is the quote",
			"body": (
				"Standard, pigmented, food-approved, UV-cure, fluorescent and bulk solvent "
				"are different HR fluids. We lock the cartridge to the substrate sample — "
				"not a generic black."
			),
			"image": m["hr2_packs"],
			"image_alt": "HR 2.0 print samples on packaging",
			"sort_order": 2,
		},
		ksa_section(m["hr2_fiber"], "HR 2.0 production data on a fiberglass panel", 3),
	])
	doc.set("support_items", support_items("HR cartridges & bulk"))
	doc.set("package_contents", [
		{"item_description": "HR 2.0 controller (2SK or 4SK) and quoted print heads", "sort_order": 1},
		{"item_description": "Start-up cartridges, photocell/encoder and KSA commissioning", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "Is this HR 1.0?", "answer": "No. HR 2.0 is the current, more compact TIJ generation. We quote HR 2.0.", "sort_order": 1},
		{"question": "When do I pick GK or UP instead?", "answer": "GK 2.0 for absorbent carton/pallet up to 100 mm. UP for coated/painted surfaces up to 108 mm. HR is the 12.7 mm cartridge TIJ.", "sort_order": 2},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_gk2(m):
	slug = "rea-jet-gk-2"
	doc = get_or_create(slug, "REA JET GK 2.0", m["gk2"])
	apply_identity(doc, slug=slug, display_name="REA JET GK 2.0", category_label="PIEZO INKJET", subcategory="High-Resolution Inkjet")
	doc.tagline = "Piezo on absorbent packs — up to 100 mm and 1,200 dpi"
	doc.short_description = (
		"REA JET GK 2.0 is a piezo high-resolution inkjet for porous surfaces: carton, "
		"paper, wood and building boards. 384/128 heads to 50 mm, 768/256 to 100 mm, "
		"solvent-free inks, IP65."
	)
	doc.long_description = (
		"<p>GK 2.0 is REA’s piezo (PIJ) printer for absorbent, porous surfaces. It is not "
		"HR 2.0 thermal inkjet and not UP (UP is the piezo all-rounder for coated packs). "
		"Official: "
		"<a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-gk-2\">"
		"REA JET GK 2.0</a>.</p>"
		"<p>Print height is up to 50 mm (384/128) or 100 mm (768/256) per head. Heads are "
		"fixed or hose-connected. Universal TITAN runs two heads (200 mm); Touch runs four "
		"(400 mm). Horizontal resolution is freely set up to 1,200 dpi. Inks are "
		"solvent-free and change on the run. Operating window +5 °C to +35 °C. IP65.</p>"
		"<p>Typical jobs: IPPC pallets, EPAL marks, outer cartons, unfilled paper bags and "
		"plasterboard logos — a label alternative on brown board.</p>"
	)
	doc.hero_image = m["gk2"]
	doc.card_image = m["gk2"]
	doc.hero_image_alt = "REA JET GK 2.0 piezo inkjet printer and print head"
	doc.hero_trust_chips = "Up to 100 mm per head\nUp to 1,200 dpi\nSolvent-free inks\nIP65 · TITAN"
	doc.story_heading = "High-contrast carton, pallet and bag marks without a label"
	doc.visual_story_heading = "Official GK 2.0 heads and absorbent-pack samples"
	doc.card_title = "GK 2.0"
	doc.card_summary = "Piezo inkjet for carton, pallet and paper: up to 100 mm, 1,200 dpi, solvent-free inks."
	doc.final_cta_heading = "Specify GK 2.0 for absorbent packs"
	doc.final_cta_description = "We will size 384 vs 768 heads, fixed vs hose, and solvent-free colour."
	doc.meta_title = "REA JET GK 2.0 Piezo Inkjet Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA JET GK 2.0 piezo inkjet: up to 100 mm and 1,200 dpi on carton, pallet and "
		"paper. From Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "Up to 100 mm", "description": "768/256 head for large logos and IPPC marks in one pass.", "sort_order": 1},
		{"icon": "scan", "title": "Sharp 1D / 2D", "description": "High-contrast barcodes on brown board for warehouse first-pass reads.", "sort_order": 2},
		{"icon": "consumables", "title": "Solvent-free inks", "description": "Change bottles during production. Light- and water-resistant colours.", "sort_order": 3},
		{"icon": "rugged", "title": "IP65 heads", "description": "Fixed or hose-connected heads for dusty packing halls.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "384 head", "image": m["gk2_384"], "image_alt": "GK 2.0 384/128 print head", "caption": "Up to 50 mm — compact carton codes.", "sort_order": 1},
		{"label": "768 head", "image": m["gk2_768"], "image_alt": "GK 2.0 768/256 print head", "caption": "Up to 100 mm — pallet and logo work.", "sort_order": 2},
		{"label": "Hose head", "image": m["gk2_hose"], "image_alt": "GK 2.0 hose-connected 768 head", "caption": "Hose version for tight line layouts.", "sort_order": 3},
		{"label": "Pallet", "image": m["gk2_pallet"], "image_alt": "GK 2.0 IPPC mark on a pallet", "caption": "IPPC / EPAL pallet marks.", "sort_order": 4},
		{"label": "Carton", "image": m["gk2_carton"], "image_alt": "GK 2.0 barcode on a carton", "caption": "Direct print instead of a label.", "sort_order": 5},
		{"label": "Bags", "image": m["gk2_bags"], "image_alt": "GK 2.0 marking unfilled paper bags", "caption": "Unfilled paper-sack coding.", "sort_order": 6},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "50 or 100 mm", "description": "384 / 768 heads", "sort_order": 1},
		{"icon": "print", "title": "1,200 dpi", "description": "Horizontal resolution", "sort_order": 2},
		{"icon": "rugged", "title": "IP65", "description": "Head and cabinet", "sort_order": 3},
		{"icon": "display", "title": "2 or 4 heads", "description": "200 or 400 mm", "sort_order": 4},
	])
	set_specs(doc, [
		("Print", [
			("Technology", "Piezo inkjet (PIJ) for absorbent / porous surfaces"),
			("Heads", "GK 384/128 up to 50 mm; GK 768/256 up to 100 mm; fixed or hose"),
			("Resolution", "Freely selectable horizontal resolution up to 1,200 dpi"),
			("Temperature", "+5 °C to +35 °C"),
			("Not this page", "UP (coated packs), HR 2.0 TIJ, DOD 2.0, SC 2.0"),
		]),
		("Controller", [
			("Universal", "Rotary TITAN — up to two heads / 200 mm"),
			("Touch", "10.1\" TITAN — up to four heads / 400 mm"),
			("Inks", "Solvent-free REA GK inks, several colours, change on the run"),
		]),
	])
	doc.set("applications", [
		{"title": "Pallets", "description": "IPPC and EPAL marks without a paper stencil.", "image": m["gk2_pallet"], "image_alt": "GK 2.0 pallet mark", "industry_link": "packaging", "sort_order": 1},
		{"title": "Building boards", "description": "Logos and batch on plasterboard.", "image": m["gk2_plaster"], "image_alt": "GK 2.0 on plasterboard", "industry_link": "packaging", "sort_order": 2},
		{"title": "Paper sacks", "description": "Weight and lot on unfilled bags.", "image": m["gk2_bags"], "image_alt": "GK 2.0 on paper bags", "industry_link": "packaging", "sort_order": 3},
	])
	doc.set("content_sections", [
		video_section(
			heading="Official GK 2.0 product-line video",
			body=(
				"REA’s official GK 2.0 film — the new-generation piezo inkjet for absorbent "
				"carton, pallet and paper. Plays in this section, not on the hero photo. "
				"Unique to this page."
			),
			video_url=VIDEO_GK2,
			image=m["gk2_carton"],
			image_alt="GK 2.0 carton coding",
			sort_order=1,
		),
		ksa_section(m["gk2_carton"], "GK 2.0 carton coding", 2),
	])
	doc.set("support_items", support_items("GK solvent-free inks"))
	doc.set("package_contents", [
		{"item_description": "GK 2.0 TITAN controller and quoted 384 or 768 print head", "sort_order": 1},
		{"item_description": "Ink bottles, photocell and KSA commissioning", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "GK 2.0 or UP?", "answer": "GK 2.0 is for absorbent carton, paper, wood and boards with solvent-free ink. UP is the piezo all-rounder for coated and painted surfaces, with ink recirculation.", "sort_order": 1},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_up(m):
	slug = "rea-jet-up"
	doc = get_or_create(slug, "REA JET UP", m["up"])
	apply_identity(doc, slug=slug, display_name="REA JET UP", category_label="PIEZO INKJET", subcategory="High-Resolution Inkjet")
	doc.tagline = "Universal piezo — up to 108 mm, 1,500 dpi, IP65"
	doc.short_description = (
		"REA JET UP (Universal Print) is a high-resolution piezo inkjet for paper, carton, "
		"wood, coated and painted surfaces. Up to 108.37 mm per head, ink recirculation "
		"and RFID bottle lock."
	)
	doc.long_description = (
		"<p>UP is REA’s current high-resolution piezo all-rounder. It is not GK 2.0 "
		"(absorbent-only) and not HR 2.0 (12.7 mm TIJ). Official: "
		"<a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-up\">"
		"REA JET UP</a>.</p>"
		"<p>Print height is up to 108.37 mm per head. Two heads on Universal reach "
		"216.74 mm; four heads on Touch reach 433.48 mm. Vertical resolution up to 360 dpi, "
		"horizontal up to 1,500 dpi. Throw 3–5 mm. Ink circulates so nozzles do not dry. "
		"RFID confirms the correct bottle. Heater option for cold halls. IP65.</p>"
		"<p>Oil-based, light-solvent and UV-cure UP inks cover coated board, Tyvek and "
		"painted packs — a direct-print alternative to labels on difficult surfaces.</p>"
	)
	doc.hero_image = m["up"]
	doc.card_image = m["up"]
	doc.hero_image_alt = "REA JET UP piezo high-resolution inkjet printer"
	doc.hero_trust_chips = "Up to 108.37 mm\nUp to 1,500 dpi\nInk recirculation\nIP65 · TITAN"
	doc.story_heading = "High-contrast carton, wood and logo marks in one pass"
	doc.visual_story_heading = "Official UP printer and carton samples"
	doc.card_title = "UP"
	doc.card_summary = "Piezo all-rounder: 108 mm, 1,500 dpi and circulating ink for coated cartons and wood."
	doc.final_cta_heading = "Specify UP for high-resolution direct print"
	doc.final_cta_description = "Printechs will confirm head count, UV vs oil ink, and TITAN controller."
	doc.meta_title = "REA JET UP Piezo Inkjet Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA JET UP piezo inkjet: up to 108 mm, 1,500 dpi and IP65. Direct print from "
		"Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "108 mm in one pass", "description": "Cascade heads when the logo or SSCC needs more height.", "sort_order": 1},
		{"icon": "maintenance", "title": "Circulating ink", "description": "Nozzles stay wet. RFID stops the wrong bottle going on.", "sort_order": 2},
		{"icon": "scan", "title": "First-pass codes", "description": "High-contrast 1D/2D for warehouse and GS1 reading.", "sort_order": 3},
		{"icon": "rugged", "title": "IP65", "description": "Cabinet and head for packing halls, not a desktop printer.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "With samples", "image": m["up_kombi"], "image_alt": "REA JET UP with print samples", "caption": "Printer and results in one official shot.", "sort_order": 1},
		{"label": "Carton side", "image": m["up_c1"], "image_alt": "UP side marking on a carton", "caption": "Alphanumeric and logo on brown board.", "sort_order": 2},
		{"label": "From above", "image": m["up_c3"], "image_alt": "UP top-down carton marking", "caption": "Secondary pack from above.", "sort_order": 3},
		{"label": "Barcode", "image": m["up_c4"], "image_alt": "UP barcode on a carton", "caption": "Warehouse-readable 1D.", "sort_order": 4},
		{"label": "IPPC wood", "image": m["up_wood"], "image_alt": "UP IPPC logo on wood", "caption": "IPPC on timber.", "sort_order": 5},
		{"label": "Outer case", "image": m["up_sec"], "image_alt": "UP marking on secondary packaging", "caption": "Outer-case production data.", "sort_order": 6},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "108.37 mm", "description": "Per print head", "sort_order": 1},
		{"icon": "print", "title": "1,500 dpi", "description": "Horizontal", "sort_order": 2},
		{"icon": "rugged", "title": "IP65", "description": "Protection class", "sort_order": 3},
		{"icon": "display", "title": "2 or 4 heads", "description": "217 or 433 mm", "sort_order": 4},
	])
	set_specs(doc, [
		("Print", [
			("Technology", "Piezo inkjet (PIJ) — Universal Print"),
			("Height", "Up to 108.37 mm per head; 216.74 mm (2); 433.48 mm (4)"),
			("Resolution", "Up to 360 dpi vertical, 1,500 dpi horizontal"),
			("Throw", "Optimum 3–5 mm"),
			("Not this page", "GK 2.0 absorbent-only, HR 2.0 TIJ, DOD 2.0, SC 2.0"),
		]),
		("Ink & control", [
			("Recirculation", "Continuous circulation to avoid nozzle fail; refill without stopping"),
			("RFID", "Bottle lock so the wrong ink cannot be filled"),
			("Inks", "Oil-based, light-solvent and UV-cure UP inks"),
			("Controllers", "Universal (2 heads) or 10.1\" Touch (4 heads)"),
		]),
	])
	doc.set("applications", [
		{"title": "Cartons", "description": "Logos, barcodes and production data on secondary packs.", "image": m["up_c8"], "image_alt": "UP carton coding", "industry_link": "packaging", "sort_order": 1},
		{"title": "Wood", "description": "IPPC and batch on timber.", "image": m["up_wood"], "image_alt": "UP wood marking", "industry_link": "packaging", "sort_order": 2},
	])
	doc.set("content_sections", [
		video_section(
			heading="Official UP product-line video",
			body=(
				"REA’s official UP film — high-resolution piezo with recirculation for "
				"coated cartons and wood. Plays in this section, not on the hero photo. "
				"Unique to this page."
			),
			video_url=VIDEO_UP,
			image=m["up_c3"],
			image_alt="UP top-down carton coding",
			sort_order=1,
		),
		ksa_section(m["up_c3"], "UP top-down carton coding", 2),
	])
	doc.set("support_items", support_items("UP inks"))
	doc.set("package_contents", [
		{"item_description": "UP TITAN controller, print head and ink supply with RFID", "sort_order": 1},
		{"item_description": "Quoted UP ink, photocell and KSA commissioning", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "UP or GK 2.0?", "answer": "UP for coated, painted and mixed surfaces with recirculation and RFID. GK 2.0 for absorbent carton/pallet with solvent-free ink.", "sort_order": 1},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_cl(m):
	slug = "rea-jet-cl"
	doc = get_or_create(slug, "REA LASER CL", m["cl"])
	apply_identity(doc, slug=slug, display_name="REA LASER CL", category_label="CO2 LASER", subcategory="Laser Marking")
	doc.tagline = "CO2 laser — permanent marks on organics, glass and rubber, no ink"
	doc.short_description = (
		"REA LASER CL is an air-cooled CO2 marker (30 W / 60 W) with a rotatable head and "
		"pilot laser. Permanent, consumable-free codes on cartons, wood, plastic profiles, "
		"tires and pharma board."
	)
	doc.long_description = (
		"<p>CL is REA’s CO2 laser — not the FL fiber laser and not an inkjet. Official: "
		"<a href=\"https://www.rea-jet.com/en/products/laser-systems/rea-laser-cl\">"
		"REA LASER CL</a>.</p>"
		"<p>Air-cooled CL230 (30 W) and CL260 (60 W) run 10.6, 10.2 or 9.3 μm. Compact "
		"head rotates for tight cells. Pilot laser speeds setup. 5.7\" graphic HMI with "
		"rotary-push control — the same TITAN idea as REA inkjet. VNC and web server for "
		"remote diagnostics. Optional marking station (class 1 cabin) for small batches.</p>"
		"<p>Best on organic packs, glass and rubber. Metals and filled plastics belong on "
		"<a href=\"/products/rea-jet-fl\">FL</a>.</p>"
	)
	doc.hero_image = m["cl"]
	doc.card_image = m["cl"]
	doc.hero_image_alt = "REA LASER CL CO2 laser marking head and controller"
	doc.hero_trust_chips = "30 W or 60 W\n10.6 / 10.2 / 9.3 μm\nPilot laser\nNo consumables"
	doc.story_heading = "Permanent codes on packs, wood, profiles and tires"
	doc.visual_story_heading = "Official CL laser and application marks"
	doc.card_title = "CL CO2 laser"
	doc.card_summary = "REA CO2 laser: 30/60 W, rotatable head, consumable-free marks on organics, glass and rubber."
	doc.final_cta_heading = "Specify CL for permanent pack marking"
	doc.final_cta_description = "We will confirm 30 vs 60 W, wavelength and whether you need a class-1 station."
	doc.meta_title = "REA LASER CL CO2 Laser Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA LASER CL CO2 laser: 30/60 W permanent coding on cartons, wood and rubber. "
		"From Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "No ink circuit", "description": "Permanent mark, almost no consumables, low running cost.", "sort_order": 1},
		{"icon": "integration", "title": "Rotatable head", "description": "Compact unit for OEM cells and existing conveyors.", "sort_order": 2},
		{"icon": "display", "title": "TITAN-family HMI", "description": "Same operating idea as REA inkjet — shorter training.", "sort_order": 3},
		{"icon": "cloud", "title": "Remote diagnostics", "description": "VNC and web server included for support without a site visit first.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "System", "image": m["cl_kombi"], "image_alt": "REA LASER CL head and controller", "caption": "Head plus TITAN-family controller.", "sort_order": 1},
		{"label": "Head", "image": m["cl_head"], "image_alt": "REA LASER CL marking head", "caption": "Rotatable CO2 head with pilot laser.", "sort_order": 2},
		{"label": "Wood", "image": m["cl_wood"], "image_alt": "CL mark on wood", "caption": "Organic surfaces — wood and board.", "sort_order": 3},
		{"label": "Capsules", "image": m["cl_capsules"], "image_alt": "CL mark on coffee capsules", "caption": "High-speed pack coding.", "sort_order": 4},
		{"label": "Pharma", "image": m["cl_pharma"], "image_alt": "CL mark on a pharma carton", "caption": "Folding-box codes without ink.", "sort_order": 5},
		{"label": "Tire", "image": m["cl_tire"], "image_alt": "CL mark on a tire", "caption": "Rubber sidewall marking.", "sort_order": 6},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "CL230 / CL260", "description": "30 W or 60 W", "sort_order": 1},
		{"icon": "print", "title": "CO2", "description": "10.6 · 10.2 · 9.3 μm", "sort_order": 2},
		{"icon": "display", "title": "5.7\" HMI", "description": "Rotary-push control", "sort_order": 3},
		{"icon": "shield", "title": "Class 1 option", "description": "Marking station cabin", "sort_order": 4},
	])
	set_specs(doc, [
		("Laser", [
			("Type", "Air-cooled CO2 with integrated pilot laser"),
			("Models", "CL230 30 W and CL260 60 W"),
			("Wavelength", "10.6 μm, 10.2 μm or 9.3 μm by model"),
			("Best on", "Organics, glass, rubber, coated board — not metals (use FL)"),
			("Not this page", "FL fiber laser, inkjet families, SC 2.0"),
		]),
		("Integration", [
			("Head", "Compact, freely rotatable; optional beam turning units"),
			("HMI", "5.7\" graphic display, rotary-push with touch"),
			("Remote", "VNC and web server for diagnostics"),
			("Station", "Optional class-1 marking cabin for small series"),
		]),
	])
	doc.set("applications", [
		{"title": "Pharma cartons", "description": "Permanent lot and 2D without a wet ink circuit.", "image": m["cl_pharma"], "image_alt": "CL on a pharma carton", "industry_link": "pharmaceutical", "sort_order": 1},
		{"title": "Profiles", "description": "Codes on extruded plastic profiles.", "image": m["cl_profile"], "image_alt": "CL on a plastic profile", "industry_link": "plastic", "sort_order": 2},
	])
	doc.set("content_sections", [
		video_section(
			heading="Official REA LASER film",
			body=(
				"REA’s official laser-systems film for the CO2 CL family — permanent marks "
				"without ink. Plays in this section, not on the hero photo. Unique to this "
				"page (FL has its own samples, not this clip)."
			),
			video_url=VIDEO_LASER,
			image=m["cl_capsules"],
			image_alt="CL coding coffee capsules",
			sort_order=1,
		),
		ksa_section(m["cl_capsules"], "CL coding coffee capsules", 2),
	])
	doc.set("support_items", support_items("Fume extraction & laser safety"))
	doc.set("package_contents", [
		{"item_description": "CL 30 W or 60 W laser, controller and focusing lens", "sort_order": 1},
		{"item_description": "Photocell, extraction and optional class-1 station as surveyed", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "CL or FL?", "answer": "CL (CO2) for cartons, wood, glass and rubber. FL (fiber) for metals, titanium and many plastics — including oily or hot parts.", "sort_order": 1},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_fl(m):
	slug = "rea-jet-fl"
	doc = get_or_create(slug, "REA LASER FL", m["fl"])
	apply_identity(doc, slug=slug, display_name="REA LASER FL", category_label="FIBER LASER", subcategory="Laser Marking")
	doc.tagline = "Pulsed fiber laser — 20 / 30 / 50 W permanent marks on metal and plastic"
	doc.short_description = (
		"REA LASER FL is a diode-pumped, air-cooled pulsed fiber laser with a rotatable "
		"head and pilot laser. Engrave or anneal stainless, titanium and plastics — even "
		"oily, corroded or >1,000 °C surfaces."
	)
	doc.long_description = (
		"<p>FL is REA’s fiber laser — not the CL CO2 and not an inkjet. Official: "
		"<a href=\"https://www.rea-jet.com/en/products/laser-systems/rea-laser-fl\">"
		"REA LASER FL</a> and the US overview "
		"<a href=\"https://reajetus.com/product-overviews/laser-systems/rea-jet-fl/\">FL</a>.</p>"
		"<p>FL20 / FL30 / FL50 deliver 20, 30 or 50 W with 1 mJ pulse energy. Pulse "
		"frequency 2–200 kHz (typical 20 / 30 / 50 kHz). Compact rotatable head, pilot "
		"laser, very high electrical efficiency. Marks stay readable on stainless, "
		"titanium, doped plastics and thin foil. Day/night design and coated substrates "
		"are in the US application list.</p>"
		"<p>We do not reuse the CL head photo on this page. Optional class-1 marking "
		"station is quoted with the laser, not as this SKU.</p>"
	)
	doc.hero_image = m["fl"]
	doc.card_image = m["fl"]
	doc.hero_image_alt = "REA LASER FL fiber laser marking cabinet and head"
	doc.hero_trust_chips = "20 · 30 · 50 W\n1 mJ pulses\n2–200 kHz\nMetals & plastics"
	doc.story_heading = "Permanent IDs on metal, tools and plastic parts"
	doc.visual_story_heading = "Official FL marks — unique to this page"
	doc.card_title = "FL fiber laser"
	doc.card_summary = "REA pulsed fiber laser: 20/30/50 W permanent engraving on metal and plastic, no ink."
	doc.final_cta_heading = "Specify FL for metal and plastic IDs"
	doc.final_cta_description = "Printechs will confirm 20 vs 30 vs 50 W, lens and extraction on your part."
	doc.meta_title = "REA LASER FL Fiber Laser Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA LASER FL fiber laser: 20/30/50 W permanent marks on metal and plastic. "
		"From Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "Hard metals", "description": "Stainless, titanium and oily or corroded parts — still a clean mark.", "sort_order": 1},
		{"icon": "speed", "title": "Low energy", "description": "Large fiber surface, air-cooled, long source life, almost no consumables.", "sort_order": 2},
		{"icon": "scan", "title": "Tiny codes", "description": "Compact focusing lens for small text, logos and 2D on tools.", "sort_order": 3},
		{"icon": "rugged", "title": "Hot parts", "description": "US spec: mark surfaces above 1,000 °C when the process is right.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "Metal plate", "image": m["fl_m1"], "image_alt": "FL mark on a metal plate", "caption": "High-contrast metal ID.", "sort_order": 1},
		{"label": "Machined part", "image": m["fl_m2"], "image_alt": "FL mark on a machined metal part", "caption": "Automotive and engineering parts.", "sort_order": 2},
		{"label": "Anneal", "image": m["fl_m3"], "image_alt": "FL annealed mark on metal", "caption": "Anneal without deep engraving.", "sort_order": 3},
		{"label": "Plastic", "image": m["fl_plastic"], "image_alt": "FL colour-change on plastic", "caption": "Doped and untreated plastics.", "sort_order": 4},
		{"label": "Tool", "image": m["fl_tweezers"], "image_alt": "FL mark on metal tweezers", "caption": "Fine tool and instrument IDs.", "sort_order": 5},
		{"label": "Cap", "image": m["fl_cap"], "image_alt": "FL mark on a closure cap", "caption": "Closures and small components.", "sort_order": 6},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "FL20 / 30 / 50", "description": "20, 30 or 50 W", "sort_order": 1},
		{"icon": "print", "title": "1 mJ", "description": "Pulse energy", "sort_order": 2},
		{"icon": "speed", "title": "2–200 kHz", "description": "Pulse frequency", "sort_order": 3},
		{"icon": "shield", "title": "Pilot laser", "description": "Fast setup", "sort_order": 4},
	])
	set_specs(doc, [
		("Laser", [
			("Type", "Diode-pumped, air-cooled pulsed fiber laser with pilot laser"),
			("Models", "FL20, FL30, FL50 — 20 W, 30 W, 50 W"),
			("Pulse", "1 mJ; 2–200 kHz (typical 20 / 30 / 50 kHz)"),
			("Best on", "Metals, titanium, plastics, foil — not organics (use CL)"),
			("Not this page", "CL CO2, inkjet, spray mark, SC 2.0"),
		]),
		("Integration", [
			("Head", "Compact, freely rotatable focusing head"),
			("Station", "Optional class-1 cabin — quoted with the laser, not this SKU"),
		]),
	])
	doc.set("applications", [
		{"title": "Metal parts", "description": "Serials and 2D on machined and sheet metal.", "image": m["fl_m2"], "image_alt": "FL on metal", "industry_link": "steel", "sort_order": 1},
		{"title": "Plastics", "description": "Colour-change IDs on housings and caps.", "image": m["fl_plastic"], "image_alt": "FL on plastic", "industry_link": "plastic", "sort_order": 2},
	])
	doc.set("content_sections", [ksa_section(m["fl_tweezers"], "FL tool marking", 1)])
	doc.set("support_items", support_items("Fume extraction & laser safety"))
	doc.set("package_contents", [
		{"item_description": "FL 20, 30 or 50 W laser, controller and focusing lens", "sort_order": 1},
		{"item_description": "Photocell, extraction and optional class-1 station as surveyed", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "Can FL replace DOD ink on steel pipe?", "answer": "Often yes for permanent IDs. Large 140 mm characters still belong on DOD 2.0. We confirm on a sample.", "sort_order": 1},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_spray(m):
	slug = "rea-jet-spray-mark"
	doc = get_or_create(slug, "REA JET Spray Mark", m["spray"])
	apply_identity(doc, slug=slug, display_name="REA JET Spray Mark", category_label="SPRAY MARK", subcategory="Spray Marking")
	doc.tagline = "Paint dots, rings and reject marks — STC, STF and EDS on one family"
	doc.short_description = (
		"REA JET spray-mark systems apply paint, primer and process fluids: STC compact "
		"One-Dot, STF turnkey lines, and EDS fine dots. Quality, scrap and large "
		"alphanumeric marks that stay readable from a distance."
	)
	doc.long_description = (
		"<p>Spray mark is one REA technology with three official configurations — not "
		"three unrelated printers. Official units: "
		"<a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-stc\">STC</a>, "
		"<a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-stf\">STF</a>, "
		"<a href=\"https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-eds\">EDS</a>. "
		"US overview: spray mark heads, blocks and turnkey systems.</p>"
		"<p><strong>STC</strong> — compact One-Dot for small-to-medium quality dots with "
		"low material use (pistons, shafts, reject marks). "
		"<strong>STF</strong> — turnkey STF1/STF2 for medium-to-large rings, lines and "
		"cable marks, ready to drop on the line. "
		"<strong>EDS</strong> — injection heads for very small dots and lines; nozzle and "
		"pressure set the spot size.</p>"
		"<p>We quote the configuration on this page. Paint, primer and adhesive jobs are "
		"process-fluid quotes — not mixed with DOD ink SKUs.</p>"
	)
	doc.hero_image = m["spray"]
	doc.card_image = m["spray"]
	doc.hero_image_alt = "REA JET STC compact spray-mark system with controller and head"
	doc.hero_trust_chips = "STC One-Dot\nSTF turnkey\nEDS fine dots\nPaint · primer · reject"
	doc.story_heading = "Quality dots, rings and scrap marks the line can see"
	doc.visual_story_heading = "Official STC, STF and EDS hardware and marks"
	doc.card_title = "Spray mark"
	doc.card_summary = "REA spray-mark family: STC One-Dot, STF turnkey and EDS fine dots for paint and reject marks."
	doc.final_cta_heading = "Specify spray mark for paint and quality dots"
	doc.final_cta_description = "Tell us the part, colour and spot size. We will map STC, STF or EDS."
	doc.meta_title = "REA JET Spray Mark Systems Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA JET STC, STF and EDS spray-mark systems for paint dots, rings and reject "
		"marks. From Printechs in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "print", "title": "Seen from afar", "description": "Large paint marks and colour codes that survive handling.", "sort_order": 1},
		{"icon": "scan", "title": "Quality / scrap", "description": "Dot or line the pass/fail part before it leaves the cell.", "sort_order": 2},
		{"icon": "integration", "title": "Turnkey or compact", "description": "STC for cells, STF when you need a ready line skid.", "sort_order": 3},
		{"icon": "consumables", "title": "Paint & primer", "description": "Not only ink — primers, lacquers and adhesives on request.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "STF system", "image": m["stf_system"], "image_alt": "REA JET STF turnkey spray-mark system", "caption": "Turnkey STF — medium to large tasks.", "sort_order": 1},
		{"label": "Heads", "image": m["stf_heads"], "image_alt": "REA JET spray-mark heads", "caption": "Spray-mark heads and blocks.", "sort_order": 2},
		{"label": "STF units", "image": m["stf_units"], "image_alt": "REA JET STF1 and STF2 units", "caption": "STF1 / STF2 cabinets.", "sort_order": 3},
		{"label": "Piston", "image": m["stc_piston"], "image_alt": "STC quality dot on a piston", "caption": "STC One-Dot on a piston.", "sort_order": 4},
		{"label": "Ring", "image": m["stf_ring"], "image_alt": "STF ring mark on a tube", "caption": "Ring marks on tube and pipe.", "sort_order": 5},
		{"label": "EDS heads", "image": m["eds_heads"], "image_alt": "REA JET EDS injection heads", "caption": "EDS fine-dot injection heads.", "sort_order": 6},
	])
	doc.set("icon_specifications", [
		{"icon": "print", "title": "STC", "description": "Compact One-Dot", "sort_order": 1},
		{"icon": "print", "title": "STF", "description": "Turnkey line system", "sort_order": 2},
		{"icon": "print", "title": "EDS", "description": "Fine dots & lines", "sort_order": 3},
		{"icon": "display", "title": "EDC HMI", "description": "Spray-mark controller", "sort_order": 4},
	])
	set_specs(doc, [
		("Family", [
			("STC", "Compact One-Dot for small/medium quality dots, low material use"),
			("STF", "Turnkey STF1/STF2 for medium/large rings, lines and cable marks"),
			("EDS", "Injection systems for very small dots/lines — nozzle and pressure set size"),
			("Fluids", "Paints, primers, lacquers, adhesives and process fluids"),
			("Not this page", "DOD 2.0 ink, HR/GK/UP, lasers, SC 2.0"),
		]),
	])
	doc.set("applications", [
		{"title": "Automotive dots", "description": "Colour and quality dots on shafts and pistons.", "image": m["stc_shaft"], "image_alt": "Spray mark on a drive shaft", "industry_link": "steel", "sort_order": 1},
		{"title": "Cable & wire", "description": "Ring and line marks on cable and rope.", "image": m["stf_cable"], "image_alt": "Spray mark on a wire rope", "industry_link": "pipe", "sort_order": 2},
		{"title": "Reject mark", "description": "Scrap identification before the part ships.", "image": m["stc_color"], "image_alt": "Colour spray-mark identification", "industry_link": "steel", "sort_order": 3},
	])
	doc.set("content_sections", [
		video_section(
			heading="Official spray-mark film",
			body=(
				"REA’s official ST film (Signier Technik) — paint dots, rings and reject "
				"marks with STC / STF. Plays in this section, not on the hero photo. "
				"Unique to this page."
			),
			video_url=VIDEO_SPRAY,
			image=m["stc_line"],
			image_alt="Spray line mark on a production part",
			sort_order=1,
		),
		{
			"section_type": "Core Module",
			"heading": "Heads, blocks and turnkey — one quote",
			"body": (
				"US lists spray-mark heads, blocks and turnkey systems as accessories of "
				"this technology. We size STC vs STF vs EDS on the sample, then add the "
				"head block and fluid. Not three product SKUs."
			),
			"image": m["eds_coupling"],
			"image_alt": "EDS multi-coupling spray heads",
			"sort_order": 2,
		},
		ksa_section(m["stc_line"], "Spray line mark on a production part", 3),
	])
	doc.set("support_items", support_items("REA paints, primers & cleaner"))
	doc.set("package_contents", [
		{"item_description": "Quoted STC, STF or EDS controller, head and fluid supply", "sort_order": 1},
		{"item_description": "Mount, photocell and KSA commissioning", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "Is spray mark the same as DOD 2.0?", "answer": "No. DOD 2.0 is drop-on-demand inkjet for text and logos. Spray mark applies paint/primer dots, rings and reject marks.", "sort_order": 1},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def fill_verify(m):
	slug = "rea-jet-code-verification"
	doc = get_or_create(slug, "REA VERIFIER Code Verification", m["verify"])
	apply_identity(
		doc,
		slug=slug,
		display_name="REA VERIFIER Code Verification",
		category_label="CODE VERIFICATION",
		subcategory="Code Verification",
	)
	doc.tagline = "Grade 1D barcodes and 2D matrix codes before the pack ships"
	doc.short_description = (
		"REA VERIFIER systems measure 1D barcode and 2D matrix quality to ISO/IEC so "
		"traceability codes actually scan. VeriCube for 2D on packs; PC-Scan LD4 for 1D. "
		"Pairs with REA JET printers — not a printer itself."
	)
	doc.long_description = (
		"<p>Verification is how you prove the code you printed is readable. Official REA "
		"family: <a href=\"https://www.rea-verifier.com/en/\">REA VERIFIER</a>. US overview "
		"lists 1D barcode verifiers, 2D matrix verifiers and software.</p>"
		"<p><strong>VeriCube</strong> inspects 2D matrix on pharma and retail packs. "
		"<strong>PC-Scan LD4</strong> is the 1D barcode path. Software reports the grade "
		"so QA can stop a bad lot before it leaves the hall.</p>"
		"<p>We quote verification next to HR 2.0, UP or DOD when the customer needs an "
		"ISO grade, not only a pretty print sample. This page is not a printer SKU and "
		"not SC 2.0.</p>"
	)
	doc.hero_image = m["verify"]
	doc.card_image = m["verify"]
	doc.hero_image_alt = "REA VERIFIER VeriCube inspecting a 2D code on a pharmaceutical carton"
	doc.hero_trust_chips = "1D barcode\n2D matrix\nISO / IEC grade\nPairs with REA JET"
	doc.story_heading = "Print is not enough — grade the code"
	doc.visual_story_heading = "Official VeriCube and PC-Scan"
	doc.card_title = "Verification"
	doc.card_summary = "REA VERIFIER 1D and 2D code grading — VeriCube and PC-Scan for ISO-quality traces."
	doc.final_cta_heading = "Add verification to the coding line"
	doc.final_cta_description = "We will pair VeriCube or PC-Scan with the REA JET printer on your pack."
	doc.meta_title = "REA VERIFIER Code Verification Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA VERIFIER VeriCube and PC-Scan grade 1D and 2D codes to ISO/IEC. From "
		"Printechs with REA JET printers in Saudi Arabia."
	)
	doc.set("benefits", [
		{"icon": "scan", "title": "ISO grade", "description": "Know the code will scan at the DC and the till — not only on your line.", "sort_order": 1},
		{"icon": "shield", "title": "Stop bad lots", "description": "QA sees a fail before the pallet is wrapped.", "sort_order": 2},
		{"icon": "integration", "title": "Beside the printer", "description": "Specify with HR 2.0, UP or DOD as one Printechs project.", "sort_order": 3},
		{"icon": "report", "title": "Trace reports", "description": "Keep the grade with the batch for customer and regulator audits.", "sort_order": 4},
	])
	doc.set("visual_story_items", [
		{"label": "VeriCube", "image": m["verify"], "image_alt": "REA VeriCube on a pharma carton", "caption": "2D matrix verification on packs.", "sort_order": 1},
		{"label": "PC-Scan", "image": m["pcscan"], "image_alt": "REA VERIFIER PC-Scan LD4 1D verifier", "caption": "1D barcode verification path.", "sort_order": 2},
	])
	doc.set("icon_specifications", [
		{"icon": "scan", "title": "VeriCube", "description": "2D matrix", "sort_order": 1},
		{"icon": "scan", "title": "PC-Scan LD4", "description": "1D barcodes", "sort_order": 2},
		{"icon": "report", "title": "ISO / IEC", "description": "Quality grade", "sort_order": 3},
		{"icon": "integration", "title": "With REA JET", "description": "Print then verify", "sort_order": 4},
	])
	set_specs(doc, [
		("Systems", [
			("2D", "REA VERIFIER VeriCube for matrix codes on packs"),
			("1D", "REA VERIFIER PC-Scan LD4 for linear barcodes"),
			("Software", "Verification reports for QA and traceability"),
			("Not this page", "Printers (DOD/HR/GK/UP/laser), SC 2.0, ink SKUs"),
		]),
	])
	doc.set("applications", [
		{"title": "Pharma 2D", "description": "Grade Data Matrix on folding boxes before release.", "image": m["verify"], "image_alt": "VeriCube on a pharma carton", "industry_link": "pharmaceutical", "sort_order": 1},
	])
	doc.set("content_sections", [
		video_section(
			heading="Official REA VERIFIER film",
			body=(
				"REA’s official verifier film — 1D and 2D grading with VeriCube and "
				"PC-Scan. Plays in this section, not on the hero photo. Unique to this page."
			),
			video_url=VIDEO_VERIFY,
			image=m["pcscan"],
			image_alt="PC-Scan 1D barcode verification",
			sort_order=1,
		),
		ksa_section(m["pcscan"], "PC-Scan 1D barcode verification", 2),
	])
	doc.set("support_items", support_items("Calibration & standards"))
	doc.set("package_contents", [
		{"item_description": "Quoted VeriCube and/or PC-Scan LD4 with software", "sort_order": 1},
		{"item_description": "KSA commissioning next to the REA JET printer", "sort_order": 2},
	])
	doc.set("faq_items", [
		{"question": "Do I need a verifier if the print looks fine?", "answer": "A readable-looking code can still fail ISO grade. Retail and pharma customers often require the report.", "sort_order": 1},
	])
	set_related(doc, RELATED[slug])
	return save_product(doc)


def _update_links():
	dod = frappe.db.get_value("Website Product", {"slug": "rea-jet-dod-2"}, "name")
	if dod:
		doc = frappe.get_doc("Website Product", dod)
		set_related(doc, ["rea-jet-coding-systems", "rea-jet-hr-2", "rea-jet-gk-2", "rea-jet-spray-mark"])
		doc.flags.ignore_permissions = True
		doc.save()
	name = frappe.db.get_value("Website Solution", {"slug": "coding-marking"}, "name")
	if name:
		sol = frappe.get_doc("Website Solution", name)
		sol.related_product_slugs = (
			"hitachi-ux2-d160\nhitachi-ux2-d150\nhitachi-ux-d161\n"
			"rea-jet-coding-systems\nrea-jet-dod-2\nrea-jet-hr-2\n"
			"rea-jet-gk-2\nrea-jet-up\nrea-jet-cl\nrea-jet-fl\n"
			"rea-jet-spray-mark\nrea-jet-code-verification"
		)
		sol.flags.ignore_permissions = True
		sol.save()
	frappe.db.commit()


def fill_rea_jet_range():
	if not (ASSETS / "rea-jet-hub-overview.png").exists():
		frappe.throw("Missing generated hub image rea-jet-hub-overview.png")
	media = _media()
	names = {
		"hub": fill_hub(media),
		"hr2": fill_hr2(media),
		"gk2": fill_gk2(media),
		"up": fill_up(media),
		"cl": fill_cl(media),
		"fl": fill_fl(media),
		"spray": fill_spray(media),
		"verify": fill_verify(media),
	}
	# Related rows need the other docs to exist — refresh once.
	media = _media()
	fill_hub(media)
	fill_hr2(media)
	fill_gk2(media)
	fill_up(media)
	fill_cl(media)
	fill_fl(media)
	fill_spray(media)
	fill_verify(media)
	_update_links()
	return names
