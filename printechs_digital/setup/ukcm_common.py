# Copyright (c) 2026, Printechs and contributors
"""Shared helpers and unique media for UKCM coding & marking fills."""

from pathlib import Path
from shutil import copy2

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
ASSETS_DIR = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
TMP_DIR = Path("/tmp/ukcm")
LIBRARY = SITE_FILES / "library" / "ukcm"
BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
BROCHURE_SRC = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital"
	"/attachments/54b1fc9f-5a66-4605-8319-a4b4dcd18b8a/TIJ-KT-10brochure.pdf"
)
BRAND = "UKCM"
ERP_ITEM_BRAND = "Kezojet"

# Unique official KT10 films — do not reuse these YouTube IDs on other pages.
VIDEO_KT10_INTRO = "https://youtu.be/C-qfqaPoXjM"
VIDEO_KT10_SETUP = "https://youtu.be/h8X84TaEjqw"
VIDEO_KT10_ACCESS = "https://youtu.be/YeORprosv0A"
VIDEO_KT10_PIPE = "https://youtu.be/ryqBzvvecdw"

APP_SCENE_KEYS = (
	"fiber-metal",
	"fiber-cable",
	"co2-bottle",
	"co2-carton",
	"uv-blister",
	"uv-electronics",
	"kt7-carton",
	"kt7-dairy",
	"kt10-carton",
	"kt10-pipe",
	"handjet-pallet",
	"handjet-pipe",
	"laser-range",
	"laser-lines",
)

KSA_SCENE_BY_SLUG: dict[str, tuple[str, str]] = {
	"ukcm-laser": ("ukcm-ksa-laser", "UKCM laser range consultation in a Saudi factory"),
	"ukcm-fiber-laser": ("ukcm-ksa-fiber", "KF130 fiber laser commissioning on a Saudi metal line"),
	"ukcm-co2-laser": ("ukcm-ksa-co2", "KC130 CO2 laser install on a Saudi beverage line"),
	"ukcm-uv-laser": ("ukcm-ksa-uv", "KU110 UV laser install in a Saudi pharma pack room"),
	"ukcm-kt7": ("ukcm-ksa-kt7", "KT7 TIJ station install in a Saudi snack plant"),
	"ukcm-kt10": ("ukcm-ksa-kt10", "KT10 TIJ station commissioning in a Saudi cosmetics factory"),
	"ukcm-hand-coder": ("ukcm-ksa-handjet", "UKCM hand coder training in a Saudi warehouse"),
}

APPLICATIONS_BY_SLUG: dict[str, list[tuple[str, str, str, str]]] = {
	"ukcm-laser": [
		("laser-range", "Choose the wavelength", "Fiber for metals, CO2 for packs and PET, UV for delicate plastics and foil.", "UKCM fiber, CO2 and UV laser marking heads"),
		("laser-lines", "Permanent codes, no ink", "Lot, expiry, 2D and serials without cartridges — specified per substrate.", "Factory lines using UKCM laser marking"),
	],
	"ukcm-fiber-laser": [
		("fiber-metal", "Metals and automotive", "Serials and 2D codes on aluminium, steel and coated metal parts.", "Fiber laser marking metal automotive parts"),
		("fiber-cable", "Cable and extrusion", "Meter marks and QR on PVC and jacketed cable at line speed.", "Fiber laser marking extruded cable"),
	],
	"ukcm-co2-laser": [
		("co2-bottle", "Beverage PET", "Expiry and lot on bottle shoulders without a wet ink circuit.", "CO2 laser coding PET bottles"),
		("co2-carton", "Cartons and paperboard", "High-contrast marks on secondary packs where ink would smear.", "CO2 laser coding cardboard cartons"),
	],
	"ukcm-uv-laser": [
		("uv-blister", "Pharma foil and blisters", "Fine 2D codes on heat-sensitive foil without burning the pack.", "UV laser marking pharmaceutical blister foil"),
		("uv-electronics", "Plastics and electronics", "High-contrast marks on white and medical-grade plastics.", "UV laser marking a plastic electronic housing"),
	],
	"ukcm-kt7": [
		("kt7-carton", "Carton coding", "300 dpi dates and barcodes on folding cartons at up to 40 m/min.", "KT7 TIJ coding snack cartons"),
		("kt7-dairy", "Food and dairy", "Sealed HP/Funai cartridges for bottles and trays — confirm water vs solvent ink.", "KT7 TIJ coding milk bottles"),
	],
	"ukcm-kt10": [
		("kt10-carton", "High-resolution packs", "10.1-inch HMI and a 25.4 mm twin head for batch, QR and logos.", "KT10 TIJ coding cosmetics cartons"),
		("kt10-pipe", "Pipe and extrusion", "Solvent or pigment cartridges on PE/PP pipe — throw typically 2–5 mm.", "KT10 TIJ coding HDPE pipe"),
	],
	"ukcm-hand-coder": [
		("handjet-pallet", "Cases and pallets", "Walk the code to the pack when there is no conveyor station.", "Handheld TIJ coding a warehouse carton"),
		("handjet-pipe", "Large or static items", "Batch marks on pipe, drums and building materials off the line.", "Handheld TIJ coding a plastic pipe"),
	],
}

KSA_BODY = (
	"Printechs supplies, installs and supports UKCM coding and marking across Saudi Arabia, "
	"including Riyadh, Jeddah, Dammam and other regions. We specify fiber, CO2, UV, KT7, "
	"KT10 or the hand coder against the substrate and line — then stay on for cartridges, "
	"service and operator training."
)


def site_file(filename: str) -> str:
	return f"/files/{filename}"


def make_card(src: Path, dest_name: str, background=(255, 255, 255)) -> str:
	dest = SITE_FILES / dest_name
	im = Image.open(src).convert("RGBA")
	scale = min(1040 / im.width, 1040 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), background)
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	canvas.save(dest, "JPEG", quality=92, optimize=True)
	return site_file(dest_name)


def save_app_scene(src: Path, dest_name: str, size: tuple[int, int] = (1600, 1200)) -> str:
	im = Image.open(src).convert("RGB")
	tw, th = size
	scale = max(tw / im.width, th / im.height)
	nw, nh = max(1, int(im.width * scale)), max(1, int(im.height * scale))
	im = im.resize((nw, nh), Image.Resampling.LANCZOS)
	left = (nw - tw) // 2
	top = (nh - th) // 2
	im = im.crop((left, top, left + tw, top + th))
	dest = SITE_FILES / dest_name
	im.save(dest, "JPEG", quality=90, optimize=True)
	return site_file(dest_name)


def _find(paths: list[Path], label: str) -> Path:
	for path in paths:
		if path.exists() and path.stat().st_size > 0:
			return path
	frappe.throw(f"Missing UKCM image: {label}")


def _find_scene(key: str) -> Path:
	return _find(
		[ASSETS_DIR / f"ukcm-app-{key}.png", ASSETS_DIR / f"ukcm-app-{key}.jpg", SITE_FILES / f"ukcm-app-{key}.jpg"],
		f"ukcm-app-{key}",
	)


def _find_ksa(stem: str) -> Path:
	return _find(
		[ASSETS_DIR / f"{stem}.png", ASSETS_DIR / f"{stem}.jpg", SITE_FILES / f"{stem}.jpg"],
		stem,
	)


def install_logo() -> str:
	src = _find([ASSETS_DIR / "brand-ukcm.png", SITE_FILES / "brand-ukcm.png"], "brand-ukcm.png")
	im = Image.open(src).convert("RGBA")
	bbox = im.getbbox()
	if bbox:
		im = im.crop(bbox)
	canvas = Image.new("RGBA", (400, 160), (255, 255, 255, 0))
	scale = min(360 / im.width, 120 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	x = (400 - new.width) // 2
	y = (160 - new.height) // 2
	canvas.paste(new, (x, y), new)
	for dest in (SITE_FILES / "brand-ukcm.png", BRAND_DIR / "brand-ukcm.png"):
		dest.parent.mkdir(parents=True, exist_ok=True)
		canvas.save(dest, "PNG")
	return site_file("brand-ukcm.png")


def install_brochure() -> str:
	if not BROCHURE_SRC.exists():
		frappe.throw(f"Missing attached UKCM KT-10 brochure: {BROCHURE_SRC}")
	dest_name = "ukcm-kt10-brochure.pdf"
	dest = SITE_FILES / dest_name
	copy2(BROCHURE_SRC, dest)
	(LIBRARY / "brochures").mkdir(parents=True, exist_ok=True)
	copy2(dest, LIBRARY / "brochures" / dest_name)
	return site_file(dest_name)


def apply_brochure(doc, brochure: str, label: str = "UKCM KT-10 brochure"):
	doc.primary_download_label = label
	doc.primary_download_file = brochure
	doc.set(
		"downloads",
		[{"label": label, "file": brochure, "download_type": "Brochure", "sort_order": 1}],
	)


def install_application_scenes() -> dict[str, str]:
	app_dir = LIBRARY / "applications"
	app_dir.mkdir(parents=True, exist_ok=True)
	media: dict[str, str] = {}
	for key in APP_SCENE_KEYS:
		filename = f"ukcm-app-{key}.jpg"
		path = save_app_scene(_find_scene(key), filename)
		copy2(SITE_FILES / filename, app_dir / filename)
		media[key] = path
	return media


def install_ksa_scenes() -> dict[str, str]:
	ksa_dir = LIBRARY / "ksa"
	ksa_dir.mkdir(parents=True, exist_ok=True)
	media: dict[str, str] = {}
	for slug, (stem, _alt) in KSA_SCENE_BY_SLUG.items():
		filename = f"{stem}.jpg"
		path = save_app_scene(_find_ksa(stem), filename)
		copy2(SITE_FILES / filename, ksa_dir / filename)
		media[f"ksa:{slug}"] = path
	return media


def prepare_media() -> dict[str, str]:
	SITE_FILES.mkdir(parents=True, exist_ok=True)
	(LIBRARY / "products").mkdir(parents=True, exist_ok=True)

	official = {
		"kt7": _find([TMP_DIR / "kt7.png", ASSETS_DIR / "kt7.png", SITE_FILES / "ukcm-kt7-product.png"], "KT7 official"),
		"kt10": _find([TMP_DIR / "kt10.png", ASSETS_DIR / "kt10.png", SITE_FILES / "kezojet-kt10-product.png"], "KT10 official"),
	}
	studios = {
		"fiber": _find([ASSETS_DIR / "ukcm-fiber-studio.png"], "fiber studio"),
		"co2": _find([ASSETS_DIR / "ukcm-co2-studio.png"], "CO2 studio"),
		"uv": _find([ASSETS_DIR / "ukcm-uv-studio.png"], "UV studio"),
		"handjet": _find([ASSETS_DIR / "ukcm-handjet-studio.png"], "handjet studio"),
		"hub": _find([ASSETS_DIR / "ukcm-app-laser-range.png"], "laser range scene"),
	}

	cards = {
		"hub": make_card(studios["hub"], "ukcm-laser-card.jpg"),
		"fiber": make_card(studios["fiber"], "ukcm-fiber-laser-card.jpg"),
		"co2": make_card(studios["co2"], "ukcm-co2-laser-card.jpg"),
		"uv": make_card(studios["uv"], "ukcm-uv-laser-card.jpg"),
		"kt7": make_card(official["kt7"], "ukcm-kt7-card.jpg"),
		"kt10": make_card(official["kt10"], "ukcm-kt10-card.jpg"),
		"handjet": make_card(studios["handjet"], "ukcm-hand-coder-card.jpg"),
	}
	for name in cards:
		src_name = Path(cards[name]).name
		copy2(SITE_FILES / src_name, LIBRARY / "products" / src_name)

	# Keep a product PNG for visual-story cutouts
	copy2(official["kt7"], SITE_FILES / "ukcm-kt7-product.png")
	copy2(official["kt10"], SITE_FILES / "ukcm-kt10-product.png")

	return {
		**cards,
		**install_application_scenes(),
		**install_ksa_scenes(),
		"kt7_photo": site_file("ukcm-kt7-product.png"),
		"kt10_photo": site_file("ukcm-kt10-product.png"),
		"logo": install_logo(),
		"brochure": install_brochure(),
	}


def scene_apps(media: dict[str, str], slug: str) -> list[dict]:
	rows = APPLICATIONS_BY_SLUG.get(slug)
	if not rows:
		frappe.throw(f"No unique application scenes mapped for {slug}")
	return [
		{
			"title": title,
			"description": description,
			"image": media[key],
			"image_alt": alt,
			"industry_link": "packaging",
			"sort_order": i,
		}
		for i, (key, title, description, alt) in enumerate(rows, start=1)
	]


def ksa_section(media: dict[str, str], slug: str, sort_order: int = 2) -> dict:
	key = f"ksa:{slug}"
	if key not in media or slug not in KSA_SCENE_BY_SLUG:
		frappe.throw(f"Missing unique KSA scene for {slug}")
	return {
		"section_type": "Industry Solution",
		"heading": "UKCM in Saudi Arabia",
		"body": KSA_BODY,
		"image": media[key],
		"image_alt": KSA_SCENE_BY_SLUG[slug][1],
		"link_label": "Talk to Our Industrial Team",
		"link_href": "/contact",
		"sort_order": sort_order,
	}


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


def set_related(doc, slugs: list[str]):
	rows = [related_by_slug(slug, i) for i, slug in enumerate(slugs, start=1)]
	doc.set("related_products", [row for row in rows if row])


def set_specs(doc, groups):
	rows = []
	sort = 1
	for group_title, items in groups:
		for label, value in items:
			if len(value) > 140:
				frappe.throw(f"Spec value too long ({len(value)}): {label} = {value}")
			rows.append({"group_title": group_title, "label": label, "value": value, "sort_order": sort})
			sort += 1
	doc.set("full_specifications", rows)


def ensure_erp_brand():
	if frappe.db.exists("Brand", BRAND):
		return
	doc = frappe.new_doc("Brand")
	doc.brand = BRAND
	doc.flags.ignore_permissions = True
	doc.insert()
	frappe.db.commit()


def get_or_create(slug: str, display_name: str, hero: str, item: str | None = None):
	if item and frappe.db.exists("Website Product", item):
		doc = frappe.get_doc("Website Product", item)
		doc.item = item
		return doc
	existing = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	if item:
		doc.item = item
	doc.slug = slug
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.short_description = f"{display_name} for industrial coding and marking."
	doc.long_description = f"<p>{display_name} for industrial coding and marking.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, category_label, subcategory, featured=0, is_hub=0):
	ensure_erp_brand()
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	doc.brand = BRAND
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.page_mode = "Full"
	doc.category = "Coding & Marking"
	doc.subcategory = subcategory
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = featured
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = "UKCM"
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1
	doc.is_hub = is_hub


def support_items(consumable: str):
	return [
		{"icon": "install", "title": "Line survey & install", "description": "Substrate, throw, photocell/encoder and mounting in Riyadh, Jeddah and Dammam.", "sort_order": 1},
		{"icon": "consumables", "title": consumable, "description": "Genuine cartridges or laser-safe integration parts quoted with the machine.", "sort_order": 2},
		{"icon": "maintenance", "title": "Service in KSA", "description": "Commissioning, spares and on-site support after the line is running.", "sort_order": 3},
		{"icon": "training", "title": "Operator training", "description": "Messages, codes, daily checks and changeover for the store or plant team.", "sort_order": 4},
	]


def save_product(doc):
	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	if doc.item and frappe.db.exists("Item", doc.item) and doc.card_image:
		item = frappe.get_doc("Item", doc.item)
		if item.image != doc.card_image:
			item.db_set("image", doc.card_image, update_modified=False)
	frappe.db.commit()
	print(f"Filled {doc.name} → /products/{doc.slug}")
	return doc.name
