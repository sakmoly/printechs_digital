# Copyright (c) 2026, Printechs and contributors
"""Shared helpers and unique media for Vusion / SES-imagotag ESL fills."""

from pathlib import Path
from shutil import copy2

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
TMP_DIR = Path("/tmp/vusion")
ASSETS_DIR = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
LIBRARY = SITE_FILES / "library" / "vusion"
BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
BRAND = "SES-imagotag"
SUBCATEGORY = "Electronic Shelf Labels"

APP_SCENE_KEYS = (
	"supermarket-aisle",
	"pharmacy-shelf",
	"convenience",
	"small-electronics",
	"grocery-promo",
	"cosmetics-shelf",
	"seafood-ice",
	"produce-mist",
	"frozen-aisle",
	"ice-cream",
	"beauty-endcap",
	"electronics-promo",
	"pick-to-light",
	"dark-store",
	"smart-rail",
	"associate-picking",
	"hq-dashboard",
	"store-tablet",
	"empty-shelf",
	"planogram",
	"shopper-media",
	"brand-campaign",
)

APPLICATIONS_BY_SLUG: dict[str, list[tuple[str, str, str, str]]] = {
	"vusion-esl": [
		("supermarket-aisle", "Supermarkets and hypermarkets", "Central price and promotion updates across every grocery facing.", "Supermarket aisle with electronic shelf labels"),
		("pharmacy-shelf", "Pharmacies", "Accurate OTC and health pricing without reprinting paper tickets.", "Pharmacy shelves with ESL price labels"),
	],
	"vusion-v100": [
		("convenience", "Convenience stores", "Reliable digital prices where cost per label and uptime matter most.", "Convenience store with compact ESL labels"),
		("small-electronics", "Small-format retail", "Entry ESL for neighbourhood electronics and specialty shops.", "Small electronics shop with digital price labels"),
	],
	"vusion-v300": [
		("grocery-promo", "Grocery promotions", "Black, white, red and yellow make offers readable from the aisle.", "Supermarket aisle with four-color ESL promotions"),
		("cosmetics-shelf", "Beauty and cosmetics", "Promotional colour without a separate paper flash.", "Cosmetics gondola with four-color ESL"),
	],
	"vusion-v300-waterproof": [
		("seafood-ice", "Seafood and meat", "IP68 labels that stay on the wet counter through wash-down.", "Waterproof ESL on a seafood ice counter"),
		("produce-mist", "Produce and dairy", "Humidity and misting will not take the price ticket offline.", "Waterproof ESL on a misted produce rack"),
	],
	"vusion-v300-freezer": [
		("frozen-aisle", "Frozen grocery", "Digital prices that remain readable at −25 °C.", "ESL labels inside a supermarket freezer"),
		("ice-cream", "Ice cream and cold rooms", "LED flash helps associates pick in gloves and fog.", "ESL labels in an ice-cream freezer well"),
	],
	"vusion-v700": [
		("beauty-endcap", "Beauty end caps", "An 8.2-inch full-colour display at the buying decision.", "Full-color digital shelf display in cosmetics"),
		("electronics-promo", "Electronics promotions", "Product imagery and price on the same shelf face.", "Full-color ESL beside electronics accessories"),
	],
	"vusion-e300": [
		("pick-to-light", "Guided picking", "Bluetooth ESL endpoints that flash associates to the SKU.", "Associate following pick-to-light ESL LEDs"),
		("dark-store", "Dark stores and omnichannel", "Connected-shelf workflows for rapid fulfillment aisles.", "Dark-store aisle with ESL pick indicators"),
	],
	"vusion-edgesense": [
		("smart-rail", "Connected shelf rails", "The rail is the network — labels sit in one shelf-edge bus.", "Smart shelf rail with seated ESL labels"),
		("associate-picking", "Location-aware tasks", "Guide replenishment and picks to the exact SKU position.", "Associate guided to a blinking smart-rail label"),
	],
	"vusion-vusioncloud": [
		("hq-dashboard", "Multi-store control", "One cloud view for device health and pricing consistency.", "Retail HQ dashboard for ESL estates"),
		("store-tablet", "Store operations", "See label status in the store before a facing goes dark.", "Store manager reviewing ESL health on a tablet"),
	],
	"vusion-captana": [
		("empty-shelf", "Out-of-stock detection", "Cameras see the gap; associates get the task.", "Empty supermarket facing watched by a shelf camera"),
		("planogram", "Planogram compliance", "Continuous shelf images instead of weekly clipboard audits.", "Grocery gondola photographed for planogram review"),
	],
	"vusion-retail-media": [
		("shopper-media", "Shopper-facing campaigns", "Brand content at the shelf, next to the product.", "Shopper viewing a digital shelf campaign"),
		("brand-campaign", "Retail-media end caps", "Schedule shelf advertising the way you schedule prices.", "Supermarket end-cap with digital shelf campaign screens"),
	],
}

KSA_BODY = (
	"Printechs provides consultation, integration, installation and support for Vusion / "
	"SES-imagotag electronic shelf labels across Saudi Arabia, including Riyadh, Jeddah, "
	"Dammam and other regions. We connect pricing from ERP and POS into VusionCloud, "
	"then specify labels, rails, computer vision and associate workflows for each format."
)

# Unique 4:3 KSA service scenes — never reuse industry-retail.jpg or another page's KSA image.
KSA_SCENE_BY_SLUG: dict[str, tuple[str, str]] = {
	"vusion-esl": ("vus-ksa-esl", "Vusion ESL installation in a Saudi supermarket aisle"),
	"vusion-v100": ("vus-ksa-v100", "Compact V100 ESL labels in a Saudi convenience store"),
	"vusion-v300": ("vus-ksa-v300", "Four-colour V300 ESL promotions in a Saudi grocery aisle"),
	"vusion-v300-waterproof": ("vus-ksa-waterproof", "Waterproof ESL labels on a Saudi fresh-food counter"),
	"vusion-v300-freezer": ("vus-ksa-freezer", "Freezer ESL labels in a Saudi frozen aisle"),
	"vusion-v700": ("vus-ksa-v700", "Full-colour V700 shelf display in a Saudi cosmetics bay"),
	"vusion-e300": ("vus-ksa-e300", "E300 pick-to-light ESL in a Saudi fulfillment aisle"),
	"vusion-edgesense": ("vus-ksa-edgesense", "EdgeSense smart rail install in a Saudi grocery gondola"),
	"vusion-vusioncloud": ("vus-ksa-cloud", "Retail team reviewing VusionCloud device health in KSA"),
	"vusion-captana": ("vus-ksa-captana", "Captana shelf-camera install in a Saudi supermarket"),
	"vusion-retail-media": ("vus-ksa-media", "Retail-media shelf campaign install in a Saudi cosmetics end-cap"),
}


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


def install_logo() -> str:
	src = ASSETS_DIR / "brand-vusion.png"
	if not src.exists():
		frappe.throw("Missing generated Vusion logo brand-vusion.png")
	im = Image.open(src).convert("RGBA")
	# crop near-white margins then pad to 400×160
	bbox = im.getbbox()
	if bbox:
		im = im.crop(bbox)
	canvas = Image.new("RGBA", (400, 160), (255, 255, 255, 0))
	scale = min(360 / im.width, 120 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	x = (400 - new.width) // 2
	y = (160 - new.height) // 2
	canvas.paste(new, (x, y), new)
	for dest in (SITE_FILES / "brand-vusion.png", BRAND_DIR / "brand-vusion.png"):
		dest.parent.mkdir(parents=True, exist_ok=True)
		canvas.save(dest, "PNG")
	return site_file("brand-vusion.png")


def _find_scene(key: str) -> Path:
	for path in (ASSETS_DIR / f"vus-app-{key}.png", ASSETS_DIR / f"vus-app-{key}.jpg", SITE_FILES / f"vus-app-{key}.jpg"):
		if path.exists():
			return path
	frappe.throw(f"Missing Vusion application scene: vus-app-{key}")


def _find_ksa(stem: str) -> Path:
	for path in (ASSETS_DIR / f"{stem}.png", ASSETS_DIR / f"{stem}.jpg", SITE_FILES / f"{stem}.jpg"):
		if path.exists():
			return path
	frappe.throw(f"Missing unique Vusion KSA scene: {stem}")


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


def install_application_scenes() -> dict[str, str]:
	app_dir = LIBRARY / "applications"
	app_dir.mkdir(parents=True, exist_ok=True)
	media: dict[str, str] = {}
	for key in APP_SCENE_KEYS:
		filename = f"vus-app-{key}.jpg"
		path = save_app_scene(_find_scene(key), filename)
		copy2(SITE_FILES / filename, app_dir / filename)
		media[key] = path
	return media


def prepare_media() -> dict[str, str]:
	SITE_FILES.mkdir(parents=True, exist_ok=True)
	(LIBRARY / "products").mkdir(parents=True, exist_ok=True)

	official = {
		"v100": TMP_DIR / "v100.png",
		"v300": TMP_DIR / "v300.png",
		"waterproof": TMP_DIR / "waterproof.png",
		"freezer": TMP_DIR / "freezer.png",
		"v700": TMP_DIR / "v700.png",
		"edgesense": TMP_DIR / "edgesense-rail.png",
		"edgesense_label": TMP_DIR / "edgesense.png",
		"captana": TMP_DIR / "captana.webp",
	}
	for key, path in official.items():
		if not path.exists():
			frappe.throw(f"Missing official Vusion photo: {path}")

	studios = {
		"e300": ASSETS_DIR / "vus-e300-studio.png",
		"cloud": ASSETS_DIR / "vus-cloud-studio.png",
		"media": ASSETS_DIR / "vus-media-studio.png",
		"hub": ASSETS_DIR / "vus-app-supermarket-aisle.png",
	}
	for key, path in studios.items():
		if not path.exists():
			frappe.throw(f"Missing generated Vusion image: {path}")

	cards = {
		"hub": make_card(studios["hub"], "vusion-esl-card.jpg"),
		"v100": make_card(official["v100"], "vusion-v100-card.jpg"),
		"v300": make_card(official["v300"], "vusion-v300-card.jpg"),
		"waterproof": make_card(official["waterproof"], "vusion-v300-waterproof-card.jpg"),
		"freezer": make_card(official["freezer"], "vusion-v300-freezer-card.jpg"),
		"v700": make_card(official["v700"], "vusion-v700-card.jpg"),
		"e300": make_card(studios["e300"], "vusion-e300-card.jpg"),
		"edgesense": make_card(official["edgesense"], "vusion-edgesense-card.jpg", background=(10, 14, 18)),
		"cloud": make_card(studios["cloud"], "vusion-vusioncloud-card.jpg"),
		"captana": make_card(official["captana"], "vusion-captana-card.jpg", background=(255, 214, 10)),
		"media": make_card(studios["media"], "vusion-retail-media-card.jpg"),
		"edgesense_label": make_card(official["edgesense_label"], "vusion-edgesense-label.jpg", background=(10, 14, 18)),
	}
	for name in (
		"vusion-esl-card.jpg",
		"vusion-v100-card.jpg",
		"vusion-v300-card.jpg",
		"vusion-v300-waterproof-card.jpg",
		"vusion-v300-freezer-card.jpg",
		"vusion-v700-card.jpg",
		"vusion-e300-card.jpg",
		"vusion-edgesense-card.jpg",
		"vusion-vusioncloud-card.jpg",
		"vusion-captana-card.jpg",
		"vusion-retail-media-card.jpg",
	):
		copy2(SITE_FILES / name, LIBRARY / "products" / name)

	return {
		**cards,
		**install_application_scenes(),
		**install_ksa_scenes(),
		"logo": install_logo(),
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
			"industry_link": "retail",
			"sort_order": i,
		}
		for i, (key, title, description, alt) in enumerate(rows, start=1)
	]


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


def get_or_create(slug: str, display_name: str, hero: str):
	existing = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = slug
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Retail Systems"
	doc.subcategory = SUBCATEGORY
	doc.short_description = f"{display_name} for retail pricing and store operations."
	doc.long_description = f"<p>{display_name} for retail pricing and store operations.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, category_label):
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	if frappe.db.exists("Brand", BRAND):
		doc.brand = BRAND
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.page_mode = "Full"
	doc.category = "Retail Systems"
	doc.subcategory = SUBCATEGORY
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = "Vusion"
	doc.show_item_code_on_website = 0
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to Our Team"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1
	doc.video_url = ""
	doc.is_hub = 0


def support_items():
	return [
		{"icon": "install", "title": "Store survey & install", "description": "Tag count, rail type, AP/gateway and department survey in Riyadh, Jeddah and Dammam.", "sort_order": 1},
		{"icon": "integration", "title": "ERP / POS integration", "description": "Pricing, promotions, item master and store master into VusionCloud.", "sort_order": 2},
		{"icon": "maintenance", "title": "Care & lifecycle", "description": "Optional Vusion Care programmes, battery/refurbishment path and on-site service.", "sort_order": 3},
		{"icon": "training", "title": "Team training", "description": "Studio templates, associate flash-to-light and day-to-day label operations.", "sort_order": 4},
	]


def ksa_section(media: dict[str, str], slug: str, sort_order: int = 2) -> dict:
	key = f"ksa:{slug}"
	if key not in media or slug not in KSA_SCENE_BY_SLUG:
		frappe.throw(f"Missing unique KSA scene for {slug}")
	return {
		"section_type": "Industry Solution",
		"heading": "Vusion ESL in Saudi Arabia",
		"body": KSA_BODY,
		"image": media[key],
		"image_alt": KSA_SCENE_BY_SLUG[slug][1],
		"link_label": "Talk to Our Retail Team",
		"link_href": "/contact",
		"sort_order": sort_order,
	}


def save_product(doc):
	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	frappe.db.commit()
	print(f"Filled {doc.name} → /products/{doc.slug}")
	return doc.name
