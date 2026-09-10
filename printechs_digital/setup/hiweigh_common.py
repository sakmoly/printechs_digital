# Copyright (c) 2026, Printechs and contributors
"""Shared helpers and unique media for HiWEIGH industrial weighing fills."""

from pathlib import Path
from shutil import copy2

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
ASSETS_DIR = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
TMP_DIR = Path("/tmp/hiweigh")
LIBRARY = SITE_FILES / "library" / "hiweigh"
BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
BRAND = "Hiweigh"
DISPLAY_BRAND = "HiWEIGH"

# Official HiWEIGH films on their support page are for other families (X2, WSS, DA, CCX).
# Do not attach those IDs to these pages.

APP_SCENE_KEYS = (
	"k9",
	"k9-2",
	"k7p",
	"k7p-2",
	"k7",
	"k7-2",
	"k7s",
	"k7s-2",
	"bxt",
	"bxt-2",
	"k9t",
	"k9t-2",
	"bhb",
	"bhb-2",
	"bsw",
	"bsw-2",
	"fod",
	"fod-2",
	"fd",
	"fd-2",
	"fdl",
	"fdl-2",
	"fwr",
	"fwr-2",
	"ax",
	"ax-2",
	"axc",
	"axc-2",
	"axr",
	"axr-2",
	"titan",
	"titan-2",
	"ag",
	"ag-2",
	"avs",
	"avs-2",
	"aps",
	"aps-2",
	"ap",
	"ap-2",
	"m15f",
	"m15f-2",
	"m13",
	"m13-2",
)

KSA_SCENE_BY_SLUG: dict[str, tuple[str, str]] = {
	"hiweigh-k9": ("hw-ksa-k9", "K9 waterproof indicator commissioning in a Saudi food plant"),
	"hiweigh-k7p": ("hw-ksa-k7p", "K7P indicator with printer at a Saudi packing station"),
	"hiweigh-k7": ("hw-ksa-k7", "K7 livestock indicator on a Saudi cattle farm"),
	"hiweigh-k7s": ("hw-ksa-k7s", "K7S stainless indicator in a Saudi warehouse"),
	"hiweigh-bxt": ("hw-ksa-bxt", "BXT washdown platform in a Saudi hygienic plant"),
	"hiweigh-k9t": ("hw-ksa-k9t", "K9T waterproof bench scale in a Saudi meat plant"),
	"hiweigh-bhb": ("hw-ksa-bhb", "BHB stainless bench scale in a Saudi pharma room"),
	"hiweigh-bsw": ("hw-ksa-bsw", "BSW OIML platform in a Saudi factory"),
	"hiweigh-fod": ("hw-ksa-fod", "FOD bench scale in a Saudi bakery packing room"),
	"hiweigh-fd": ("hw-ksa-fd", "FD floor scale in a Saudi warehouse"),
	"hiweigh-fdl": ("hw-ksa-fdl", "FDL low-profile floor scale in a Dammam warehouse"),
	"hiweigh-fwr": ("hw-ksa-fwr", "FWR hygienic floor scale in a Saudi food plant"),
	"hiweigh-ax": ("hw-ksa-ax", "AX portable axle pads at a Saudi fleet yard"),
	"hiweigh-axc": ("hw-ksa-axc", "AXC axle pads at a Saudi highway weigh check"),
	"hiweigh-axr": ("hw-ksa-axr", "AXR portable weighbridge on a Saudi construction site"),
	"hiweigh-titan": ("hw-ksa-titan", "TiTAN mining axle pad under a Saudi quarry truck"),
	"hiweigh-ag": ("hw-ksa-ag", "AG cattle crate on a Saudi ranch"),
	"hiweigh-avs": ("hw-ksa-avs", "AVS crate scale on a Saudi sheep farm"),
	"hiweigh-aps": ("hw-ksa-aps", "APS aluminum pig scale in a Saudi livestock barn"),
	"hiweigh-ap": ("hw-ksa-ap", "AP veterinary scale in a Riyadh clinic"),
	"hiweigh-m15f": ("hw-ksa-m15f", "M15F load cell fitted in a Saudi OEM workshop"),
	"hiweigh-m13": ("hw-ksa-m13", "M13 load cell assembly in a Saudi scale workshop"),
}

APPLICATIONS_BY_SLUG: dict[str, list[tuple[str, str, str, str, str]]] = {
	"hiweigh-k9": [
		("k9", "Seafood and washdown lines", "Sealed housing and capacitive keys for meat, fish and dairy rooms that are hosed down every shift.", "K9 indicator in a seafood washdown hall", "food-beverage"),
		("k9-2", "Dairy and hygienic rooms", "IP68 / IP69K electronics stay readable when steam and high-pressure cleaning are part of the process.", "K9 indicator in a dairy washdown room", "dairy"),
	],
	"hiweigh-k7p": [
		("k7p", "Weight tickets at the station", "Print a weight record or receipt at the packing bench without a separate printer.", "K7P printing a warehouse weight ticket", "warehouse-logistics"),
		("k7p-2", "Food packing labels", "Useful where a portion or case needs a paper record before it leaves the line.", "K7P printing food packing labels", "food-beverage"),
	],
	"hiweigh-k7": [
		("k7", "Cattle and livestock races", "Animal-weighing firmware and an IP67 housing for dusty, wet farm yards.", "K7 livestock indicator on a farm post", "food-beverage"),
		("k7-2", "Movement and dust", "Built for yards where animals move and the indicator cannot be treated as indoor electronics.", "K7 indicator beside a cattle race", "food-beverage"),
	],
	"hiweigh-k7s": [
		("k7s", "Warehouse platforms", "Stainless housing for industrial and agricultural platforms that need a durable indicator.", "K7S stainless indicator on a warehouse column", "warehouse-logistics"),
		("k7s-2", "Feed and farm stores", "A practical indicator when the platform is mild steel or stainless and the room is not full washdown.", "K7S indicator weighing feed bags", "food-beverage"),
	],
	"hiweigh-bxt": [
		("bxt", "Open-frame washdown", "Open construction lets water drain so the platform can take intensive cleaning.", "BXT open-frame platform being washed down", "food-beverage"),
		("bxt-2", "Meat and hygienic packing", "Pair with a K9-class indicator when the room must stay hygienic after every batch.", "BXT platform on a meat packing table", "food-beverage"),
	],
	"hiweigh-k9t": [
		("k9t", "Meat, seafood and dairy", "Complete waterproof bench: K9 electronics plus a hygienic platform for washdown rooms.", "K9T bench scale in a hygienic packing room", "food-beverage"),
		("k9t-2", "Bakery and pharma washdown", "Choose K9T when a standard bench scale will not survive high-pressure cleaning.", "K9T bench scale in a bakery washdown room", "bakery"),
	],
	"hiweigh-bhb": [
		("bhb", "Food and chemical benches", "Sealed stainless construction for corrosive or hygienic bench work up to about 100 kg.", "BHB stainless bench scale on a process bench", "food-beverage"),
		("bhb-2", "Pharmaceutical rooms", "SUS304 (optional 316) when the room needs a sealed hygienic bench, not a mild-steel platform.", "BHB scale in a pharmaceutical room", "pharmaceutical"),
	],
	"hiweigh-bsw": [
		("bsw", "Factory platforms", "OIML / NTEP load cells, mild-steel frame and a stainless top for legal-for-trade industrial work.", "BSW industrial platform in a factory", "warehouse-logistics"),
		("bsw-2", "Warehouse receiving", "A practical 300–1,000 kg class platform when you do not need a full floor scale.", "BSW platform used for warehouse receiving", "warehouse-logistics"),
	],
	"hiweigh-fod": [
		("fod", "Food packing and counting", "Multi-function bench for portioning, inventory counts and simple batching.", "FOD bench scale used for food packing", "food-beverage"),
		("fod-2", "Bakery portioning", "6–150 kg family — not a high-pressure washdown scale; use K9T when the hose is daily.", "FOD scale portioning bakery trays", "bakery"),
	],
	"hiweigh-fd": [
		("fd", "Warehouse pallets", "U-beam floor scale for palletised goods, up to 5,000 kg depending on configuration.", "FD floor scale weighing a warehouse pallet", "warehouse-logistics"),
		("fd-2", "Receiving docks", "Specify length, width and capacity — this page is the 1.5 × 1.5 m / 5 t configuration we stock.", "FD floor scale at a factory receiving dock", "warehouse-logistics"),
	],
	"hiweigh-fdl": [
		("fdl", "Pallet-jack access", "Low profile plus dual ramps so trolleys roll on without a pit.", "FDL low-profile scale with a warehouse trolley", "warehouse-logistics"),
		("fdl-2", "Production aisles", "1.5 t / 3 t class for logistics and production floors that need easy drive-on access.", "FDL scale in a production aisle", "warehouse-logistics"),
	],
	"hiweigh-fwr": [
		("fwr", "Hygienic wet floors", "Stainless floor system with ramp access and IP-rated cells for food and washdown rooms.", "FWR hygienic floor scale being washed", "food-beverage"),
		("fwr-2", "Dairy crate handling", "Stocked FW hygienic floors can be quoted when you need a 1.2 or 1.5 m stainless deck.", "FWR hygienic floor scale in a dairy plant", "dairy"),
	],
	"hiweigh-ax": [
		("ax", "Fleet axle checks", "Portable pads with OIML load cells for truck and fleet axle weighing.", "AX portable axle pad under a truck tire", "warehouse-logistics"),
		("ax-2", "Yard enforcement", "Move the pads to the yard instead of pouring a weighbridge pit.", "AX pads used for fleet yard weighing", "warehouse-logistics"),
	],
	"hiweigh-axc": [
		("axc", "Integrated-ramp pads", "7075 aluminium pads with built-in ramps — typically up to about 20 t per pad.", "AXC aluminium axle pad with a truck tire", "warehouse-logistics"),
		("axc-2", "Two-pad lanes", "Pair pads for axle-by-axle checks at a temporary roadside or site lane.", "AXC two-pad portable truck weighing lane", "warehouse-logistics"),
	],
	"hiweigh-axr": [
		("axr", "No-foundation weighbridge", "Portable truck scale for sites that cannot pour a permanent pit — around 30 t depending on deck.", "AXR portable weighbridge with a tractor-trailer", "warehouse-logistics"),
		("axr-2", "Temporary project sites", "Relocate the decks when the project moves — construction, logistics yards and industrial camps.", "AXR modules being positioned on a temporary site", "warehouse-logistics"),
	],
	"hiweigh-titan": [
		("titan", "Mining truck axles", "Ultra-heavy pads — 50 / 100 / 200 t options per pad for quarry and mine trucks.", "TiTAN pad under a mining dump-truck tire", "steel"),
		("titan-2", "Static and dynamic checks", "Combine 2, 4 or 6 pads and show axle or total weight at the cabin.", "TiTAN mine weigh-station display", "steel"),
	],
	"hiweigh-ag": [
		("ag", "Cattle crates", "Heavy-duty crate for safe cattle weighing on farms and ranches.", "AG cattle crate scale in a farm yard", "food-beverage"),
		("ag-2", "Handling alleys", "Sheeted sides and weigh-bar mounts keep animals and operators safer during the weigh.", "AG crate at the end of a cattle alley", "food-beverage"),
	],
	"hiweigh-avs": [
		("avs", "Sheep, goats and hogs", "Crate scale with single-position control of four sliding doors.", "AVS crate scale for sheep and goats", "food-beverage"),
		("avs-2", "Sorting on the farm", "600 kg or 1,500 kg class — pair with a livestock indicator such as K7.", "AVS crate used for livestock sorting", "food-beverage"),
	],
	"hiweigh-aps": [
		("aps", "Pig alleyways", "All-aluminium construction and waterproof electronics for wet farm buildings.", "APS aluminum pig scale in a barn", "food-beverage"),
		("aps-2", "Washable livestock lines", "Lighter than a steel cattle crate and happier in corrosive, washed-down pens.", "APS aluminum livestock scale on a wet floor", "food-beverage"),
	],
	"hiweigh-ap": [
		("ap", "Veterinary clinics", "SUS304 platform and a removable mat for hygienic pet weighing.", "AP veterinary scale with a dog in clinic", "pharmaceutical"),
		("ap-2", "Grooming and shelters", "Handle and wheels on selected sizes so the scale can move between rooms.", "AP pet scale with anti-slip mat", "retail"),
	],
	"hiweigh-m15f": [
		("m15f", "Platform and retail OEM", "C3 single-point cell, IP65, typical capacities 50–400 kg for industrial platforms.", "M15F single-point load cell on a bench", "packaging"),
		("m15f-2", "Legal-for-trade builds", "Used in OEM platforms and retail scales that need an approved single-point sensor.", "M15F load cell being fitted under a platform", "packaging"),
	],
	"hiweigh-m13": [
		("m13", "Table-top OEM", "OIML C3 single-point for compact benches — typical 5–50 kg family.", "M13 single-point load cell close-up", "packaging"),
		("m13-2", "Small legal-for-trade scales", "M13 / M13M when the platform is a table-top, not a 400 kg industrial deck.", "M13 load cell in a table-top scale chassis", "packaging"),
	],
}

KSA_BODY = (
	"Printechs supplies, installs and supports HiWEIGH industrial weighing across Saudi Arabia, "
	"including Riyadh, Jeddah, Dammam and other regions. We specify the indicator, platform, "
	"floor scale, axle pad or livestock crate to the site — then stay on for commissioning, "
	"spares and operator training."
)

OFFICIAL_SOURCES: dict[str, list[Path]] = {
	"k9": [TMP_DIR / "k9-front.jpg", TMP_DIR / "k9.jpg"],
	"k7p": [TMP_DIR / "k7p.jpg"],
	"k7": [TMP_DIR / "k7.jpg"],
	"k7s": [TMP_DIR / "k7s.jpg"],
	"bxt": [TMP_DIR / "bxt.jpg"],
	"k9t": [TMP_DIR / "k9t.jpg"],
	"bhb": [TMP_DIR / "bhb2.jpg", TMP_DIR / "bhb.jpg"],
	"bsw": [TMP_DIR / "bsw.jpg"],
	"fod": [TMP_DIR / "fod.jpg"],
	"fd": [TMP_DIR / "fd.jpg"],
	"fdl": [TMP_DIR / "fdl.jpg"],
	"fwr": [TMP_DIR / "fwr.jpg"],
	"ax": [TMP_DIR / "ax.png"],
	"axc": [TMP_DIR / "axc.jpg"],
	"axr": [TMP_DIR / "axr.jpg"],
	"titan": [TMP_DIR / "titan.jpg"],
	"ag": [TMP_DIR / "ag.jpg"],
	"avs": [TMP_DIR / "avs.jpg"],
	"aps": [TMP_DIR / "aps.jpg"],
	"ap": [TMP_DIR / "ap.jpg"],
	"m15f": [TMP_DIR / "m15f.jpg"],
	"m13": [TMP_DIR / "m13.jpg"],
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


def _find(paths: list[Path], label: str) -> Path:
	for path in paths:
		if path.exists() and path.stat().st_size > 0:
			return path
	frappe.throw(f"Missing HiWEIGH image: {label}")


def _find_scene(key: str) -> Path:
	return _find(
		[
			ASSETS_DIR / f"hw-app-{key}.png",
			ASSETS_DIR / f"hw-app-{key}.jpg",
			SITE_FILES / f"hw-app-{key}.jpg",
		],
		f"hw-app-{key}",
	)


def _find_ksa(stem: str) -> Path:
	return _find(
		[ASSETS_DIR / f"{stem}.png", ASSETS_DIR / f"{stem}.jpg", SITE_FILES / f"{stem}.jpg"],
		stem,
	)


def install_logo() -> str:
	src = _find(
		[ASSETS_DIR / "brand-hiweigh-src.png", ASSETS_DIR / "brand-hiweigh.png", SITE_FILES / "brand-hiweigh.png"],
		"brand-hiweigh.png",
	)
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
	for dest in (SITE_FILES / "brand-hiweigh.png", BRAND_DIR / "brand-hiweigh.png"):
		dest.parent.mkdir(parents=True, exist_ok=True)
		canvas.save(dest, "PNG")
	return site_file("brand-hiweigh.png")


def install_application_scenes() -> dict[str, str]:
	app_dir = LIBRARY / "applications"
	app_dir.mkdir(parents=True, exist_ok=True)
	media: dict[str, str] = {}
	for key in APP_SCENE_KEYS:
		filename = f"hw-app-{key}.jpg"
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
	cards = {}
	for key, paths in OFFICIAL_SOURCES.items():
		src = _find(paths, f"{key} official")
		filename = f"hiweigh-{key}-card.jpg"
		cards[f"card:{key}"] = make_card(src, filename)
		copy2(SITE_FILES / filename, LIBRARY / "products" / filename)
	return {
		**install_application_scenes(),
		**install_ksa_scenes(),
		**cards,
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
			"industry_link": industry,
			"sort_order": i,
		}
		for i, (key, title, description, alt, industry) in enumerate(rows, start=1)
	]


def ksa_section(media: dict[str, str], slug: str, sort_order: int = 2) -> dict:
	key = f"ksa:{slug}"
	if key not in media or slug not in KSA_SCENE_BY_SLUG:
		frappe.throw(f"Missing unique KSA scene for {slug}")
	return {
		"section_type": "Industry Solution",
		"heading": "HiWEIGH in Saudi Arabia",
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
	doc.category = "Industrial Weighing"
	doc.short_description = f"{display_name} for industrial weighing."
	doc.long_description = f"<p>{display_name} for industrial weighing.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, category_label, subcategory, featured=0, featured_sort=0):
	ensure_erp_brand()
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	doc.brand = BRAND
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.page_mode = "Full"
	doc.category = "Industrial Weighing"
	doc.subcategory = subcategory
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = featured
	doc.featured_sort_order = featured_sort
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = DISPLAY_BRAND
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1
	doc.is_hub = 0


def support_items():
	return [
		{
			"icon": "install",
			"title": "Site survey & install",
			"description": "Capacity, platform size, washdown rating and mounting specified for Riyadh, Jeddah and Dammam.",
			"sort_order": 1,
		},
		{
			"icon": "consumables",
			"title": "Cells, indicators & spares",
			"description": "Matching load cells, indicators, ramps and spare parts quoted with the system.",
			"sort_order": 2,
		},
		{
			"icon": "maintenance",
			"title": "Service in KSA",
			"description": "Commissioning, calibration support and on-site service after the scale is in use.",
			"sort_order": 3,
		},
		{
			"icon": "training",
			"title": "Operator training",
			"description": "Zero, tare, print and daily checks for the warehouse, plant or farm team.",
			"sort_order": 4,
		},
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
