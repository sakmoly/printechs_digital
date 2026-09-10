# Copyright (c) 2026, Printechs and contributors
"""Fill Website Product IND.SYS.KZT.4982 — Kezojet KT10 (UKCM KT / UK 10).

Official sources:
https://uk-cm.uk/thermal-transfer-inkjet-printer/
https://3sink.com/ukcm-kt10/
https://uk-cm.uk/how-to-choose-the-correct-tij-printer-for-different-applications-and-industries/
Kenjiete / Kezojet KT-10 series listing (controller size, throw, I/O, inks).

This SKU is the 10.1-inch twin-head package (mounting + anti-shock + line cable).
Do not mix KT5 / KT7 speeds or CIJ (K600) claims onto this page.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image

import frappe

NAME = "IND.SYS.KZT.4982"
SLUG = "kezojet-kt10"
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")

VIDEO_INTRO = "https://youtu.be/C-qfqaPoXjM"
VIDEO_SETUP = "https://youtu.be/h8X84TaEjqw"
VIDEO_ACCESS = "https://youtu.be/YeORprosv0A"
VIDEO_PIPE = "https://youtu.be/ryqBzvvecdw"

HERO_URLS = [
	"https://3sink.com/wp-content/uploads/2024/11/kt10.png",
]
HERO_PNG = "kezojet-kt10-product.png"
HERO_CARD = "kezojet-kt10-card.jpg"


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def download_file(filename: str, urls: list[str]) -> str:
	target = SITE_FILES / filename
	if target.exists() and target.stat().st_size > 0:
		return f"/files/{filename}"
	headers = {
		"User-Agent": (
			"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
			"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
		)
	}
	last_error = None
	for url in urls:
		try:
			request = Request(url, headers=headers)
			with urlopen(request, timeout=30) as response, target.open("wb") as handle:
				handle.write(response.read())
			if target.exists() and target.stat().st_size > 0:
				return f"/files/{filename}"
		except Exception as exc:
			last_error = exc
	if last_error:
		raise last_error
	frappe.throw(f"Could not download {filename}")


def catalog_card(source_name: str, dest_name: str) -> str:
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


def resolve_hero() -> tuple[str, str]:
	png = SITE_FILES / HERO_PNG
	if not (png.exists() and png.stat().st_size > 0):
		legacy = SITE_FILES / "kezojet-kt10-hero.jpg"
		if legacy.exists() and legacy.stat().st_size > 0:
			copy2(legacy, png)
		else:
			download_file(HERO_PNG, HERO_URLS)
	card = catalog_card(HERO_PNG, HERO_CARD)
	return f"/files/{HERO_PNG}", card


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


def fill_kezojet_kt10():
	"""Superseded by the UKCM cluster — keep this entry point so old bench commands still work."""
	from printechs_digital.setup.fill_ukcm import fill_kt10
	from printechs_digital.setup.ukcm_common import prepare_media

	return fill_kt10(prepare_media())


def _legacy_fill_kezojet_kt10():
	if not frappe.db.exists("Website Product", NAME):
		frappe.throw(f"Website Product {NAME} was not found")

	doc = frappe.get_doc("Website Product", NAME)
	hero_photo, hero_card = resolve_hero()
	food = copy_public_image("industry-food-beverage.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	pipe = copy_public_image("industry-pipe.jpg")
	dairy = copy_public_image("industry-dairy.jpg")

	doc.display_name = "Kezojet KT10"
	doc.website_product_name = "Kezojet KT10"
	doc.slug = SLUG
	if frappe.db.exists("Brand", "Kezojet"):
		doc.brand = "Kezojet"
	doc.brand_name = "Kezojet"
	doc.category = "Coding & Marking"
	doc.subcategory = "Thermal Inkjet"
	doc.category_label = "THERMAL INKJET PRINTER"
	doc.tagline = "10.1-inch TIJ station — 120 m/min, twin 1-inch head"
	doc.short_description = (
		"Kezojet KT10 is the UKCM KT / UK 10 thermal inkjet station: 10.1-inch colour "
		"touchscreen, Linux controller and a one-inch twin head (25.4 mm). This SKU "
		"ships with mounting, anti-shock and a cable cut for the line."
	)
	doc.long_description = (
		"<p>KT10 is Kezojet’s 10.1-inch online TIJ coder — the same UKCM KT series "
		"listed as UK 10. It is a sealed-cartridge thermal inkjet, not a CIJ and not "
		"the smaller KT5 / KT7 controllers.</p>"
		"<p>The distributor listing (3S Ink) rates the KT-10 at 300 dpi and up to "
		"120 m/min, with a capacitive 10.1-inch screen, about 20 operator languages "
		"and an embedded Linux OS. The controller can drive up to ten nozzles; "
		"IND.SYS.KZT.4982 is supplied as a one-inch twin head (two 12.7 mm cartridges, "
		"25.4 mm print band) with mounting, anti-shock and a tailored umbilical.</p>"
		"<p>TIJ uses HP45 / HP45si / Funai 42 ml cartridges. There is no makeup fluid "
		"and no long ink circuit. Water, solvent, oil, fast-dry and invisible inks "
		"cover carton, film, plastic, metal and pipe — confirm the cartridge before "
		"you lock the SKU. Throw distance is typically 2–5 mm.</p>"
		"<p>UKCM positions the KT series for food, beverage, medical devices, "
		"cosmetics, packaging and building materials, and shows bottle, pack and "
		"pipe examples. I/O is power, USB, RS-232 and Ethernet; wireless is a family "
		"option. Printechs supplies, installs and services KT10 in Riyadh, Jeddah "
		"and Dammam.</p>"
	)
	doc.hero_image = hero_card
	doc.hero_image_alt = "Kezojet KT10 UKCM 10.1-inch thermal inkjet controller with TIJ printhead and photocell"
	doc.video_url = VIDEO_INTRO
	doc.hero_trust_chips = (
		"10.1-inch capacitive HMI\n"
		"25.4 mm twin head\n"
		"120 m/min · 300 dpi\n"
		"Up to 10 nozzles on the controller"
	)
	doc.story_heading = "Large screen. Twin-head TIJ. Cartridge, not makeup."
	doc.visual_story_heading = "KT10 on packs, bottles and pipe"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.page_mode = "Full"
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.card_title = "KT10"
	doc.card_brand_label = "Kezojet"
	doc.card_summary = (
		"UKCM KT / UK 10 TIJ: 10.1-inch screen, 25.4 mm twin head, 120 m/min. "
		"Mounting and anti-shock included."
	)
	doc.card_image = hero_card
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.final_cta_heading = "Specify KT10 for your packaging line"
	doc.final_cta_description = (
		"Printechs will confirm head count, HP/Funai ink, throw, mounting and cable "
		"length for Kezojet KT10 in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Kezojet KT10 Thermal Inkjet Printer Saudi Arabia | Printechs"
	doc.meta_description = (
		"Kezojet KT10 (UKCM UK 10) TIJ coder: 10.1-inch screen, 25.4 mm twin head, "
		"120 m/min. Mounting and anti-shock. From Printechs in KSA."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "display",
				"title": "10.1-inch capacitive HMI",
				"description": (
					"Colour touchscreen and about 20 languages, including Arabic. "
					"Embedded Linux for message edit, ink level and print status."
				),
				"sort_order": 1,
			},
			{
				"icon": "print",
				"title": "One-inch twin head",
				"description": (
					"Two 12.7 mm TIJ cartridges, 25.4 mm print band — dates, barcodes, "
					"QR, logos and multi-line text in one pass."
				),
				"sort_order": 2,
			},
			{
				"icon": "speed",
				"title": "120 m/min at 300 dpi",
				"description": (
					"3S Ink rates KT-10 at 300 dpi and up to 120 metres/minute. "
					"Higher dpi is cartridge-dependent, not a KT5/KT7 40 m/min rating."
				),
				"sort_order": 3,
			},
			{
				"icon": "install",
				"title": "Ready to mount",
				"description": (
					"This SKU includes the bracket kit, anti-shock and a cable length "
					"cut for the conveyor, cartoner or case sealer."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "KT10 station",
				"image": hero_photo,
				"image_alt": "UKCM KT10 10.1-inch controller, TIJ head and photocell on a stand",
				"caption": "Official UKCM / 3S Ink station: 10.1-inch HMI, printhead and product sensor.",
				"sort_order": 1,
			},
			{
				"label": "Food and beverage",
				"image": food,
				"image_alt": "Food trays and bottles with date and lot codes",
				"caption": "Expiry and lot on trays, PET and cartons — UKCM’s bottle and pack examples.",
				"sort_order": 2,
			},
			{
				"label": "Milk and dairy",
				"image": dairy,
				"image_alt": "Milk bottles with manufacture, expiry and lot codes",
				"caption": "Sealed cartridge TIJ for cold-fill dairy packs. Confirm solvent vs water ink.",
				"sort_order": 3,
			},
			{
				"label": "Pipe and extrusion",
				"image": pipe,
				"image_alt": "HDPE pipe marked with batch number and size",
				"caption": "UKCM shows pipe coding in the KT series gallery. Confirm pigment/solvent ink.",
				"sort_order": 4,
			},
			{
				"label": "Pharma cartons",
				"image": pharma,
				"image_alt": "Pharmaceutical carton coding",
				"caption": "Batch, expiry and 2D codes on healthcare cartons.",
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "print", "title": "Thermal inkjet", "description": "HP45 / HP45si / Funai 42 ml", "sort_order": 1},
			{"icon": "lines", "title": "25.4 mm band", "description": "Twin 12.7 mm heads on this SKU", "sort_order": 2},
			{"icon": "display", "title": "10.1-inch HMI", "description": "Capacitive · ~20 languages · Linux", "sort_order": 3},
			{"icon": "speed", "title": "120 m/min", "description": "300 dpi (3S Ink KT-10 rating)", "sort_order": 4},
			{"icon": "connectivity", "title": "USB · RS-232 · Ethernet", "description": "Wireless is a family option", "sort_order": 5},
			{"icon": "install", "title": "This SKU", "description": "Mounting + anti-shock + line cable", "sort_order": 6},
		],
	)

	set_specs(
		doc,
		[
			(
				"This configuration",
				[
					("Model", "Kezojet KT10 — UKCM KT series / UK 10 (not KT5, not KT7, not K600 CIJ)"),
					("Item code", NAME),
					("Controller", "10.1-inch colour capacitive touchscreen, embedded Linux"),
					("Printheads on this SKU", "One-inch twin head — 25.4 mm print band"),
					("Controller capacity", "Up to 10 nozzles; this item is supplied as twin-head"),
					("Included", "Mounting accessories, anti-shock, cable length specified for the line"),
				],
			),
			(
				"Printing performance",
				[
					("Technology", "Thermal inkjet (HP TIJ 2.5 / thermal-bubble)"),
					("Cartridge family", "HP45 / HP45si / Funai, 42 ml typical"),
					("Resolution", "300 dpi (3S Ink KT-10); up to 600 dpi on some UKCM cartridges"),
					("Print height (this SKU)", "25.4 mm with two 12.7 mm heads"),
					("Print speed", "Up to 120 m/min at 300 dpi (3S Ink KT-10 listing)"),
					("Throw distance", "Typically 2–5 mm (KT-10 series listing)"),
					("Variable data", "Text, logo, Code 128/39, I2of5, UPC-A, EAN-13, QR, Data Matrix"),
					("Counter", "1–15 digit increment (series listing)"),
					("Substrates", "Paper, carton, film, plastic, metal, pipe and cable — ink-dependent"),
				],
			),
			(
				"Inks",
				[
					("Bases", "Water, solvent, oil, fast-dry and invisible (confirm per substrate)"),
					("Colours", "Black plus process colours and white on selected fast-dry cartridges"),
					("Recognition", "Cartridge type / ink-level monitoring on the 10.1-inch HMI"),
				],
			),
			(
				"Controller, I/O & environment",
				[
					("Display", "10.1-inch colour capacitive touchscreen"),
					("OS / languages", "Embedded Linux; about 20 languages including Arabic"),
					("Controller size", "250 × 158 × 35 mm aluminium (KT-10 series listing)"),
					("Head mass", "About 597 g per head without cartridge (series listing)"),
					("Interfaces", "Power, USB, RS-232, Ethernet; wireless is a KT-family option"),
					("Supply", "16 V, 3 A / 5 A adapter (series listing)"),
					("Climate", "0–40 °C, 10–80 % RH, non-condensing (series listing)"),
				],
			),
			(
				"Installation",
				[
					("Mounting", "Complete bracket kit included on this SKU"),
					("Anti-shock", "Included on this SKU"),
					("Cable", "Umbilical length specified for the line"),
					("Typical lines", "Conveyors, cartoners, flow wrappers, case sealers, pipe extrusion"),
				],
			),
		],
	)

	doc.set(
		"applications",
		[
			{
				"title": "Food and beverage",
				"description": "Expiry, lot and barcode on cartons, film, PET and trays at line speed.",
				"image": food,
				"image_alt": "Food and beverage packs with inkjet date and lot codes",
				"industry_link": "food-beverage",
				"sort_order": 1,
			},
			{
				"title": "Milk and dairy",
				"description": "Manufacture, expiry and lot on bottles and tubs. Confirm ink for wet halls.",
				"image": dairy,
				"image_alt": "Milk bottles coded on a dairy filling line",
				"industry_link": "dairy",
				"sort_order": 2,
			},
			{
				"title": "Pharmaceutical cartons",
				"description": "Batch and 2D codes on healthcare packs. 300 dpi for small text and GS1 codes.",
				"image": pharma,
				"image_alt": "Pharmaceutical packaging line coding",
				"industry_link": "pharmaceutical",
				"sort_order": 3,
			},
			{
				"title": "Pipe, tube and packs",
				"description": "Batch and size on pipe, plus high-resolution marks on cases and film.",
				"image": pipe,
				"image_alt": "Extruded pipe marked with batch and size",
				"industry_link": "pipe",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Meet the UKCM KT10",
				"body": (
					"Designer introduction to the UKCM online TIJ KT10 — the same 10.1-inch "
					"station Kezojet lists as KT10 / UK 10. Watch the HMI and head, then "
					"we size cartridges and throw for your pack."
				),
				"video_url": VIDEO_INTRO,
				"image": hero_photo,
				"image_alt": "Kezojet KT10 UKCM thermal inkjet station",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Set up the online TIJ station",
				"body": (
					"Yinojet’s KT10 setup film: stand, photocell, head and 10.1-inch "
					"controller. This SKU already includes mounting and anti-shock — "
					"Printechs sets throw (typically 2–5 mm) and the cable on site."
				),
				"video_url": VIDEO_SETUP,
				"image": hero_photo,
				"image_alt": "KT10 printhead, photocell and 10.1-inch controller",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Cartridges and line accessories",
				"body": (
					"Official UKCM online-TIJ accessories film. KT10 uses 42 ml HP45 / "
					"HP45si / Funai cartridges — water, solvent, oil, fast-dry or "
					"invisible. The HMI reads cartridge type and ink level."
				),
				"video_url": VIDEO_ACCESS,
				"image": packaging,
				"image_alt": "Packaging line ready for thermal inkjet cartridges",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "When plants choose TIJ instead of CIJ",
				"body": (
					"Thermal inkjet is a sealed cartridge. For many carton and film jobs "
					"it avoids CIJ makeup and a daily flush. KT10 is for date, batch, "
					"barcode and logo work — not a high-speed CIJ such as UX2 or UKCM K600.\n\n"
					"Need more than 25.4 mm? The same controller can take more nozzles "
					"(up to ten). This item is the twin-head package."
				),
				"image": packaging,
				"image_alt": "Carton coding on a packaging line",
				"link_label": "Coding and marking solutions",
				"link_href": "/solutions/coding-marking",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Bottle, pack and pipe examples",
				"body": (
					"UKCM’s KT-series gallery shows bottle, pack and pipe coding. The "
					"pipe film is a UKCM family clip — we still confirm solvent or "
					"pigment ink and throw on PE/PP before we lock KT10."
				),
				"video_url": VIDEO_PIPE,
				"image": pipe,
				"image_alt": "Pipe coding application for UKCM marking systems",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "KT10 vs KT7 / KT5, and Saudi Arabia support",
				"body": (
					"KT10 is the 10.1-inch, 120 m/min, up-to-10-nozzle controller. KT7 "
					"is a smaller screen and a 40 m/min / 6-nozzle listing. KT5 is the "
					"5-inch entry unit. Do not order those when you need this SKU.\n\n"
					"Printechs installs KT10 in Riyadh, Jeddah and Dammam with genuine "
					"cartridges, photocell setup and operator training."
				),
				"image": food,
				"image_alt": "Food line coding supported by Printechs in Saudi Arabia",
				"link_label": "Talk to a specialist",
				"link_href": "/contact",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Installation",
				"description": "Bracket, photocell, 2–5 mm throw, cable routing and first messages.",
				"sort_order": 1,
			},
			{
				"icon": "consumables",
				"title": "Cartridges",
				"description": "HP / Funai 42 ml — water, solvent, fast-dry or invisible, matched to the pack.",
				"sort_order": 2,
			},
			{
				"icon": "maintenance",
				"title": "Spares & service",
				"description": "Heads, cables, anti-shock parts and on-site support in KSA.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Operator training",
				"description": "Touchscreen messages, cartridge change, daily wipe and ink-level checks.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.primary_download_label = None
	doc.primary_download_file = None
	doc.set(
		"package_contents",
		[
			{"item_description": "KT10 / UK 10 controller with 10.1-inch colour touchscreen", "sort_order": 1},
			{"item_description": "One-inch twin TIJ printhead (25.4 mm band)", "sort_order": 2},
			{"item_description": "Complete mounting accessories", "sort_order": 3},
			{"item_description": "Anti-shock system", "sort_order": 4},
			{"item_description": "Cable length specified for the line", "sort_order": 5},
		],
	)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])
	doc.set("quote_options", [])

	related = [
		row
		for row in (
			related_by_slug("anser-sph-smart-printhead", 1),
			related_by_slug("hitachi-ux2-d150", 2),
			related_by_slug("hitachi-ux2-d160", 3),
		)
		if row
	]
	doc.set("related_products", related)

	doc.set(
		"faq_items",
		[
			{
				"question": "What is included with IND.SYS.KZT.4982?",
				"answer": (
					"Kezojet KT10 with the 10.1-inch screen, a one-inch twin printhead, "
					"complete mounting accessories, anti-shock, and a cable length "
					"specified for the line."
				),
				"sort_order": 1,
			},
			{
				"question": "Is KT10 the same as UKCM UK 10?",
				"answer": (
					"Yes. KT10 is the Kezojet / UKCM KT-series controller with the 10.1-inch "
					"touchscreen (UK 10). It is not KT5, KT7 or the K600 CIJ."
				),
				"sort_order": 2,
			},
			{
				"question": "How fast and how tall does it print?",
				"answer": (
					"3S Ink lists KT-10 at 300 dpi and up to 120 m/min. This SKU’s twin "
					"head is 25.4 mm tall. The controller can take up to ten nozzles if "
					"you later need a wider band."
				),
				"sort_order": 3,
			},
			{
				"question": "What can it print, and on which packs?",
				"answer": (
					"Text, logos, Code 128/39, interleaved 2 of 5, UPC-A, EAN-13, QR and "
					"Data Matrix — plus date, batch, expiry and a 1–15 digit counter. "
					"Carton, film, plastic, metal and pipe, depending on the 42 ml cartridge."
				),
				"sort_order": 4,
			},
			{
				"question": "Do you supply ink and installation in Saudi Arabia?",
				"answer": (
					"Yes. Printechs supplies the printer, HP/Funai cartridges, mounting "
					"and commissioning, and after-sales service in Riyadh, Jeddah and Dammam."
				),
				"sort_order": 5,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()

	if frappe.db.exists("Item", NAME):
		item = frappe.get_doc("Item", NAME)
		if item.image != hero_card:
			item.db_set("image", hero_card, update_modified=False)

	frappe.db.commit()
	print(f"Filled and published {doc.name} → /products/{doc.slug}")
	return doc.name
