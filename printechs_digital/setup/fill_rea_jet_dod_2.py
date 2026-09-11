# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product rea-jet-dod-2 (REA JET DOD 2.0).

Official source is a single product page — 7 / 16 / 32-nozzle heads are
options of one system, not separate SKUs:
https://www.rea-jet.com/en/products/coding-and-marking-systems/rea-jet-dod-2

Do not mix DOD 1.X, HR, GK or ink SKUs onto this page.
Do not attach consumable or spare-part Items.
"""

from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SLUG = "rea-jet-dod-2"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
BASE = "https://www.rea-jet.com"
VIDEO_PRODUCT = "https://youtu.be/VR5EHuFnMro"

OFFICIAL_IMAGES = {
	"rea-jet-dod-2-heads.jpg": f"{BASE}/product/rea-jet/dod-2/1206/image-thumb__1206__lightbox_image/dod-2-schreibkopf-trio@2x.ecae57a3.jpg",
	"rea-jet-dod-2-heads-alt.jpg": f"{BASE}/product/rea-jet/dod-2/1216/image-thumb__1216__lightbox_image/dod-2-schreibkopf-trio-03@2x.291530c7.jpg",
	"rea-jet-dod-2-controllers.jpg": f"{BASE}/product/rea-jet/dod-2/1212/image-thumb__1212__lightbox_image/dod-2-steuereinheiten-duo@2x.7b2d8a13.jpg",
	"rea-jet-dod-2-touch.jpg": f"{BASE}/product/rea-jet/dod-2/1213/image-thumb__1213__lightbox_image/dod-2-touch-controller@2x.75f7c5b0.jpg",
	"rea-jet-dod-2-universal.jpg": f"{BASE}/product/rea-jet/dod-2/1214/image-thumb__1214__lightbox_image/dod-2-universal-controller@2x.2acd9dbf.jpg",
	"rea-jet-dod-2-pvc.jpg": f"{BASE}/product/rea-jet/dod-2/770/image-thumb__770__lightbox_image/dod-2-pvc-rohre@2x.aa524f54.jpg",
	"rea-jet-dod-2-bags.jpg": f"{BASE}/product/rea-jet/dod-2/777/image-thumb__777__lightbox_image/dod-2-sackbeschriftung-01@2x.7598f61e.jpg",
	"rea-jet-dod-2-pallet.jpg": f"{BASE}/product/rea-jet/dod-2/780/image-thumb__780__lightbox_image/dod-2-sackbeschriftung-palette@2x.2b8b1019.jpg",
	"rea-jet-dod-2-steel.jpg": f"{BASE}/product/rea-jet/dod-2/724/image-thumb__724__lightbox_image/dod-2-stahlrohr-kennzeichnung@2x.72a5326e.jpg",
	"rea-jet-dod-2-beam.jpg": f"{BASE}/product/rea-jet/dod-2/755/image-thumb__755__lightbox_image/dod-2-stahltraeger@2x.f888a353.jpg",
	"rea-jet-dod-2-wood.jpg": f"{BASE}/product/rea-jet/dod-2/766/image-thumb__766__lightbox_image/dod-2-holzbretter@2x.d4d1cbf1.jpg",
	"rea-jet-dod-2-lube.jpg": f"{BASE}/product/rea-jet/dod-2/1286/image-thumb__1286__lightbox_image/dod-2-schmierstoffe-lube@2x.76265426.jpg",
	"rea-jet-dod-2-sleeper.jpg": f"{BASE}/product/rea-jet/dod-2/783/image-thumb__783__lightbox_image/dod-2-betonschwellen@2x.200253ff.jpg",
	"rea-jet-dod-2-cable.jpg": f"{BASE}/product/rea-jet/dod-2/744/image-thumb__744__lightbox_image/dod-2-kabelmarkierung-stahlseil@2x.a006ec35.jpg",
}


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"})
		with urlopen(request, timeout=45) as response, target.open("wb") as handle:
			handle.write(response.read())
	return f"/files/{filename}"


def official_image(filename: str) -> str:
	target = SITE_FILES / filename
	if target.exists():
		return f"/files/{filename}"
	return download_file(filename, OFFICIAL_IMAGES[filename])


def catalog_card(source_name: str, dest_name: str) -> str:
	official_image(source_name)
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGBA")
	scale = 900 / max(im.size)
	new = im.resize((int(im.width * scale), int(im.height * scale)), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


def related_by_slug(slug: str, sort_order: int) -> dict | None:
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if not name:
		return None
	related = frappe.get_doc("Website Product", name)
	return {
		"related_website_product": name,
		"display_name_override": related.display_name or related.website_product_name,
		"summary_override": related.card_summary or related.short_description,
		"href": f"/products/{related.slug}",
		"image": related.card_image or related.hero_image,
		"sort_order": sort_order,
	}


def get_or_create():
	existing = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = SLUG
	doc.website_product_name = "REA JET DOD 2.0"
	doc.display_name = "REA JET DOD 2.0"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.short_description = "REA JET DOD 2.0 large character inkjet printer."
	doc.long_description = "<p>REA JET DOD 2.0 large character inkjet printer.</p>"
	doc.hero_image = official_image("rea-jet-dod-2-heads.jpg")
	return doc


def set_specs(doc, groups):
	rows = []
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			if len(value) > 140:
				frappe.throw(f"Spec value too long ({len(value)}): {label}")
			rows.append(
				{
					"group_title": group_title,
					"label": label,
					"value": value,
					"sort_order": sort,
				}
			)
			sort += 1
	doc.set("full_specifications", rows)


def fill_rea_jet_dod_2():
	doc = get_or_create()
	hero = catalog_card("rea-jet-dod-2-heads.jpg", "rea-jet-dod-2-product.jpg")
	heads = official_image("rea-jet-dod-2-heads.jpg")
	heads_alt = official_image("rea-jet-dod-2-heads-alt.jpg")
	controllers = official_image("rea-jet-dod-2-controllers.jpg")
	touch = official_image("rea-jet-dod-2-touch.jpg")
	universal = official_image("rea-jet-dod-2-universal.jpg")
	pvc = official_image("rea-jet-dod-2-pvc.jpg")
	bags = official_image("rea-jet-dod-2-bags.jpg")
	pallet = official_image("rea-jet-dod-2-pallet.jpg")
	steel = official_image("rea-jet-dod-2-steel.jpg")
	beam = official_image("rea-jet-dod-2-beam.jpg")
	wood = official_image("rea-jet-dod-2-wood.jpg")
	lube = official_image("rea-jet-dod-2-lube.jpg")
	sleeper = official_image("rea-jet-dod-2-sleeper.jpg")
	cable = official_image("rea-jet-dod-2-cable.jpg")

	doc.item = None
	doc.show_item_code_on_website = 0
	doc.website_product_name = "REA JET DOD 2.0"
	doc.display_name = "REA JET DOD 2.0"
	doc.slug = SLUG
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.subcategory = "Large Character Inkjet"
	doc.category_label = "DROP-ON-DEMAND LARGE CHARACTER"
	if frappe.db.exists("Brand", "Reajet"):
		doc.brand = "Reajet"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.featured = 0
	doc.index_page = 1
	doc.published = 1
	doc.is_hub = 0
	doc.card_brand_label = "REA JET"
	doc.card_title = "DOD 2.0"
	doc.hero_image = hero
	doc.card_image = hero
	doc.hero_image_alt = "REA JET DOD 2.0 print heads with 7, 16 and 32 nozzles"
	doc.video_url = VIDEO_PRODUCT
	doc.tagline = "Large-character drop-on-demand inkjet for dusty, wet and high-speed lines"
	doc.short_description = (
		"REA JET DOD 2.0 is a large-character drop-on-demand inkjet: 7, 16 or 32-nozzle "
		"heads, up to 140 mm print height per head, 600 m/min and IP65. Text, logos and "
		"variable data on bags, pipe, steel, wood and building materials."
	)
	doc.long_description = (
		"<p>DOD 2.0 is REA JET’s current large-character inkjet — one modular system, "
		"not a family of separate printers. Print heads with 7, 16 or 32 nozzles sit on "
		"the same TITAN controller and ink supply. It is not DOD 1.X, not HR thermal "
		"inkjet, and not GK piezo.</p>"
		"<p>REA rates speed potential at up to 600 m/min and print height at up to 140 mm "
		"per head. Heads cascade for large logos — up to 1,024 addressable nozzles, or "
		"up to 16 heads on one device. Individually fired nozzles mark absorbent and "
		"non-absorbent surfaces: paper, carton, metal, glass, ceramic, stone, wood, "
		"plastic, rubber, film, carpet and textiles.</p>"
		"<p>The cabinet is specified IP65. The system tolerates dust, moisture, vibration "
		"and −5 °C to +45 °C. Purge &amp; Clean flushes the head from the controller. "
		"Micro-Slanting trims character height/width. Dot Size Control sets drop volume "
		"so ink is not wasted on a small code.</p>"
		"<p>Two controllers share the TITAN interface: Universal (rotary knob, number "
		"pad, cursor) and Universal Touch (10.1\" glove-ready tile UI). Drivers are "
		"sold by nozzle count — 16-nozzle or 32-nozzle — so a 16-nozzle driver can run "
		"one 16-nozzle head or two 7-nozzle heads.</p>"
		"<p>Ink units mix pigmented and dye fluids, resist sedimentation, and take an "
		"optional automatic flush. REA lists more than 500 DOD inks and primers. "
		"Printechs specifies heads, controller and ink for pipe, bag, steel and wood "
		"lines in Riyadh, Jeddah and Dammam.</p>"
	)
	doc.hero_trust_chips = (
		"Up to 140 mm per head\n"
		"Up to 600 m/min\n"
		"7 / 16 / 32-nozzle heads\n"
		"IP65 · TITAN controller"
	)
	doc.story_heading = "Large-character DOD for bags, pipe, steel and timber"
	doc.visual_story_heading = "Official REA JET DOD 2.0 heads, controllers and line shots"
	doc.card_summary = (
		"Large-character DOD inkjet: 7 / 16 / 32-nozzle heads, up to 140 mm and 600 m/min, "
		"IP65 — for bags, pipe, steel and wood."
	)
	doc.final_cta_heading = "Specify DOD 2.0 for your marking line"
	doc.final_cta_description = (
		"Printechs can size 7, 16 or 32-nozzle heads, TITAN controller and ink for dusty "
		"or high-speed lines in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "REA JET DOD 2.0 Large Character Inkjet Saudi Arabia | Printechs"
	doc.meta_description = (
		"REA JET DOD 2.0 drop-on-demand large-character inkjet: 7/16/32-nozzle heads, "
		"140 mm, 600 m/min, IP65. Supplied by Printechs in KSA."
	)
	doc.canonical_path = f"/products/{SLUG}"

	doc.set(
		"benefits",
		[
			{
				"icon": "lines",
				"title": "7, 16 or 32 nozzles",
				"description": (
					"One line at 5–27 mm, one–two lines at 5–67 mm, or one–five lines at "
					"5–140 mm. Cascade heads when the logo is taller than one head."
				),
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Up to 600 m/min",
				"description": (
					"REA’s DOD 2.0 speed potential for timber, bag and extrusion lines — "
					"large characters without a second or third printer."
				),
				"sort_order": 2,
			},
			{
				"icon": "rugged",
				"title": "IP65 in dust and wash",
				"description": (
					"Specified for dust, moisture, vibration and −5 °C to +45 °C. Purge & "
					"Clean clears the head from the controller without a bench teardown."
				),
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "TITAN + Industry 4.0",
				"description": (
					"One REA JET TITAN operating concept on Universal or 10.1\" Touch. "
					"Ethernet and higher-level interfaces for PLC and plant systems."
				),
				"sort_order": 4,
			},
		],
	)
	doc.set(
		"visual_story_items",
		[
			{
				"label": "7 / 16 / 32-nozzle heads",
				"image": heads,
				"image_alt": "REA JET DOD 2.0 print heads with 7, 16 and 32 nozzles",
				"caption": "Official REA photo: the three DOD 2.0 print-head sizes on one system.",
				"sort_order": 1,
			},
			{
				"label": "Heads on the line",
				"image": heads_alt,
				"image_alt": "REA JET DOD 2.0 print head trio for large character marking",
				"caption": "Cascade heads for logos wider or taller than 140 mm.",
				"sort_order": 2,
			},
			{
				"label": "Universal and Touch controllers",
				"image": controllers,
				"image_alt": "REA JET DOD 2.0 Universal Controller and Universal Touch Controller",
				"caption": "Same TITAN software — keypad Universal or 10.1\" glove-ready Touch.",
				"sort_order": 3,
			},
			{
				"label": "PVC pipe, 32-nozzle head",
				"image": pvc,
				"image_alt": "REA JET DOD 2.0 marking PVC pipes with a 32-nozzle print head",
				"caption": "Official application: large characters on extruded PVC pipe.",
				"sort_order": 4,
			},
			{
				"label": "Filled bags",
				"image": bags,
				"image_alt": "REA JET DOD 2.0 bag marking with weight, batch and date",
				"caption": "Official application: weight, batch and best-before on dusty bag lines.",
				"sort_order": 5,
			},
			{
				"label": "Steel pipe",
				"image": steel,
				"image_alt": "REA JET DOD 2.0 large character marking on steel pipe",
				"caption": "Official application: high-contrast codes on steel tube.",
				"sort_order": 6,
			},
			{
				"label": "Concrete sleepers",
				"image": sleeper,
				"image_alt": "REA JET DOD 2.0 marking on concrete railroad sleepers",
				"caption": "Official application: identity marks on concrete sleepers.",
				"sort_order": 7,
			},
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": "scan", "title": "7 / 16 / 32 nozzles", "description": "5–27 / 5–67 / 5–140 mm height", "sort_order": 1},
			{"icon": "speed", "title": "600 m/min", "description": "REA speed potential", "sort_order": 2},
			{"icon": "lines", "title": "1,024 nozzles", "description": "Cascade · up to 16 heads", "sort_order": 3},
			{"icon": "rugged", "title": "IP65", "description": "−5 °C to +45 °C", "sort_order": 4},
			{"icon": "display", "title": "10.1\" Touch", "description": "Or keypad Universal", "sort_order": 5},
			{"icon": "consumables", "title": "500+ inks", "description": "Pigment, dye and primer", "sort_order": 6},
		],
	)
	set_specs(
		doc,
		[
			(
				"Print heads",
				[
					("7-nozzle head", "Single-line marking, 5–27 mm height"),
					("16-nozzle head", "One to two lines, 5–67 mm height"),
					("32-nozzle head", "One to five lines, 5–140 mm height"),
					("Cascade", "Combine heads; up to 1,024 addressable nozzles"),
					("Heads per device", "Up to 16 print heads"),
					("Print speed", "Up to 600 m/min"),
					("Purge & Clean", "Head flush from the controller"),
					("Micro-Slanting", "Fine height/width ratio of the printed font"),
					("Dot Size Control", "Adjustable drop volume for ink economy"),
				],
			),
			(
				"Controllers",
				[
					("Platform", "REA JET TITAN — one operating concept"),
					("Universal Controller", "Rotary/push knob, number pad and cursor block"),
					("Universal Touch", "10.1\" tile UI, glove operation, no hardware keys"),
					("Nozzles per controller", "Up to 1,024 nozzles on one controller"),
				],
			),
			(
				"Print-head drivers",
				[
					("16-nozzle driver", "One 16-nozzle head, or two 7-nozzle heads"),
					("32-nozzle driver", "Any mix of heads that totals 32 nozzles"),
				],
			),
			(
				"Ink and environment",
				[
					("Inks and primers", "500+ pigmented and non-pigmented fluids"),
					("Ink units", "Chemical-resistant mixers; optional automatic flush"),
					("Operation", "Automatic or manual ink supply"),
					("Protection", "IP65 — dust-tight, splash water"),
					("Temperature", "−5 °C to +45 °C"),
					("Surfaces", "Absorbent and non-absorbent: paper, metal, wood, plastic, film"),
				],
			),
		],
	)
	doc.set(
		"applications",
		[
			{
				"title": "Bags and bulk sacks",
				"description": "Weight, batch and best-before on filled or empty sacks in dusty halls.",
				"image": bags,
				"image_alt": "Official REA JET DOD 2.0 bag marking",
				"industry_link": "packaging",
				"sort_order": 1,
			},
			{
				"title": "PVC and steel pipe",
				"description": "Large identity codes on extrusion and tube lines with a 32-nozzle head.",
				"image": pvc,
				"image_alt": "Official REA JET DOD 2.0 PVC pipe marking",
				"industry_link": "pipe",
				"sort_order": 2,
			},
			{
				"title": "Steel beams and cable",
				"description": "High-contrast lot marks on beams, tube and steel cable.",
				"image": beam,
				"image_alt": "Official REA JET DOD 2.0 steel beam marking",
				"industry_link": "steel",
				"sort_order": 3,
			},
			{
				"title": "Timber and boards",
				"description": "Grade, length and mill marks on wood in harsh sawmill conditions.",
				"image": wood,
				"image_alt": "Official REA JET DOD 2.0 wooden board marking",
				"industry_link": "packaging",
				"sort_order": 4,
			},
		],
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Core Module",
				"heading": "One DOD 2.0 system — three head sizes",
				"body": (
					"REA publishes DOD 2.0 as a single product. 7, 16 and 32-nozzle heads "
					"are options, not separate printers. A 16-nozzle driver can run one "
					"16-nozzle head or two 7-nozzle heads. Cascade when the mark is taller "
					"than 140 mm."
				),
				"image": heads,
				"image_alt": "REA JET DOD 2.0 7, 16 and 32-nozzle print heads",
				"sort_order": 1,
			},
			{
				"section_type": "Core Module",
				"heading": "Official product-line video",
				"body": (
					"REA JET’s official DOD 2.0 film (Großschrift Tintenstrahldrucker) plays "
					"in the hero. It shows the 7/16/32-nozzle heads, TITAN controller and "
					"large-character marks — the clip is unique to this page."
				),
				"image": heads_alt,
				"image_alt": "REA JET DOD 2.0 print heads from the official product film",
				"sort_order": 2,
			},
			{
				"section_type": "Core Module",
				"heading": "Universal or 10.1\" Touch",
				"body": (
					"Both controllers run TITAN. Universal uses a rotary knob, number pad "
					"and cursor. Touch is a 10.1\" tile screen with no hardware keys — "
					"REA specifies glove use. Up to 1,024 nozzles on one controller."
				),
				"image": touch,
				"image_alt": "REA JET DOD 2.0 Universal Touch Controller 10.1 inch display",
				"sort_order": 3,
			},
			{
				"section_type": "Core Module",
				"heading": "Keypad Universal Controller",
				"body": (
					"Choose Universal when operators already work with a hardware keypad "
					"and status LEDs. Same TITAN jobs, Ethernet and USB as Touch — only "
					"the front panel changes."
				),
				"image": universal,
				"image_alt": "REA JET DOD 2.0 Universal Controller with keypad",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Bag marking in dust",
				"body": (
					"REA’s bag application: filled or empty sacks, high dust, temperature "
					"swings and vibration. DOD 2.0 keeps weight, batch and best-before "
					"readable without a label. Pallet-stack codes use the same heads."
				),
				"image": bags,
				"image_alt": "Official REA JET DOD 2.0 marking on filled paper bags",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Palletised sacks",
				"body": (
					"Official REA still of palletised bags after DOD 2.0 coding. One "
					"controller can drive several heads so each face or each lane gets "
					"its own message."
				),
				"image": pallet,
				"image_alt": "Official REA JET DOD 2.0 codes on palletised bags",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "PVC pipe — 32-nozzle head",
				"body": (
					"REA’s PVC-pipe still is shot with a 32-nozzle head (5–140 mm). "
					"Identity, size and shift stay on the extrusion without a wipe-on "
					"label. Steel tube uses the same head family."
				),
				"image": pvc,
				"image_alt": "Official REA JET DOD 2.0 32-nozzle marking on PVC pipes",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Steel tube and beams",
				"body": (
					"Official steel-pipe and beam stills. Oil-penetrating DOD inks are "
					"on REA’s list when the surface is oily — specify ink with the head, "
					"do not assume the carton ink will hold on mill scale."
				),
				"image": steel,
				"image_alt": "Official REA JET DOD 2.0 marking on steel pipe",
				"sort_order": 8,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Timber, sleepers and cable",
				"body": (
					"Wooden boards, concrete sleepers and steel cable are in REA’s DOD 2.0 "
					"gallery. 7-nozzle heads suit cable; 32-nozzle heads suit sleeper and "
					"board faces.\n\n"
					"Printechs sizes heads, TITAN controller and ink in Riyadh, Jeddah "
					"and Dammam. DOD 1.X remains a different generation."
				),
				"image": wood,
				"image_alt": "Official REA JET DOD 2.0 marking on wooden boards",
				"link_label": "Talk to Our Industrial Team",
				"link_href": "/contact",
				"sort_order": 9,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Mist-free lubricant application",
				"body": (
					"REA also specifies DOD 2.0 for local lubricant on blanks and coil — "
					"mist-free, aerosol-free, only where the forming tool needs it. That "
					"is a wetting job, not a date code. Call it out separately on the quote."
				),
				"image": lube,
				"image_alt": "Official REA JET DOD 2.0 mist-free lubricant application",
				"sort_order": 10,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Concrete sleepers and steel cable",
				"body": (
					"Two more official gallery stills: railroad sleeper identity and "
					"7-nozzle marks on steel cable. Same DOD 2.0 controller — different "
					"head and ink."
				),
				"image": cable,
				"image_alt": "Official REA JET DOD 2.0 7-nozzle marking on steel cable",
				"sort_order": 11,
			},
		],
	)
	# Extra visual used in last section body via related still
	doc.set(
		"support_items",
		[
			{
				"icon": "scan",
				"title": "Head sizing",
				"description": "7, 16 or 32 nozzles from mark height and line count — we size before you buy ink.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "TITAN and mounting",
				"description": "Universal or Touch controller, photocell, encoder and bracket on your conveyor.",
				"sort_order": 2,
			},
			{
				"icon": "consumables",
				"title": "500+ DOD inks",
				"description": "Pigment, dye, oil-penetrating and food-contact options — not HR cartridges.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Install, Purge & Clean training and genuine fluids in Riyadh, Jeddah and Dammam.",
				"sort_order": 4,
			},
		],
	)
	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "DOD 2.0 print head — 7, 16 or 32 nozzles as specified", "sort_order": 1},
			{"item_description": "16-nozzle or 32-nozzle print-head driver", "sort_order": 2},
			{"item_description": "Universal Controller or Universal Touch Controller (TITAN)", "sort_order": 3},
			{"item_description": "Ink / primer supply unit (fluids ordered to substrate)", "sort_order": 4},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set(
		"faq_items",
		[
			{
				"question": "What is REA JET DOD 2.0?",
				"answer": "REA’s current large-character drop-on-demand inkjet: 7/16/32-nozzle heads, up to 140 mm per head, 600 m/min and IP65. One system with head options — not three separate products.",
				"sort_order": 1,
			},
			{
				"question": "Is this the same as DOD 1.X?",
				"answer": "No. DOD 1.X is the previous large-character generation on REA’s site. DOD 2.0 is the current TITAN platform with Purge & Clean, Micro-Slanting and Dot Size Control.",
				"sort_order": 2,
			},
			{
				"question": "Do I need three product pages for 7, 16 and 32 nozzles?",
				"answer": "No. REA sells those as heads on one DOD 2.0 system. We quote the head count on this page.",
				"sort_order": 3,
			},
			{
				"question": "Which controller should I choose?",
				"answer": "Universal has a keypad and rotary knob. Universal Touch is a 10.1\" glove-ready display. Both run TITAN and up to 1,024 nozzles.",
				"sort_order": 4,
			},
			{
				"question": "Can it apply lubricant as well as ink?",
				"answer": "REA specifies mist-free local lubricant on blanks and coil as a DOD 2.0 wetting job. That is quoted separately from date/lot coding.",
				"sort_order": 5,
			},
		],
	)
	related = [
		row
		for row in (
			related_by_slug("hitachi-ux2-d160", 1),
			related_by_slug("hitachi-ux-d160", 2),
			related_by_slug("hitachi-ux-d161", 3),
		)
		if row
	]
	doc.set("related_products", related)

	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()

	name = frappe.db.get_value("Website Solution", {"slug": "coding-marking"}, "name")
	if name:
		sol = frappe.get_doc("Website Solution", name)
		slugs = [s.strip() for s in (sol.related_product_slugs or "").splitlines() if s.strip()]
		if SLUG not in slugs:
			slugs = [s for s in slugs if s != "rea-jet-coding-systems"]
			slugs.append(SLUG)
			sol.related_product_slugs = "\n".join(slugs)
			sol.flags.ignore_permissions = True
			sol.save()

	frappe.db.commit()
	return doc.name
