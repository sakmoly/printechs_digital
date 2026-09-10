# Copyright (c) 2026, Printechs and contributors
"""Shared helpers and unique media for Nedap RF EAS Website Product fills."""

from pathlib import Path
from shutil import copy2

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
TMP_DIR = Path("/tmp/nedap")
ASSETS_DIR = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
LIBRARY = SITE_FILES / "library" / "nedap"
BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
BRAND = "Nedap"
SUBCATEGORY = "Electronic Article Surveillance"

APP_SCENE_KEYS = (
	"fashion-mall",
	"supermarket-carts",
	"self-checkout",
	"boutique-narrow",
	"pharmacy",
	"fashion-chain",
	"hypermarket",
	"premium-lumen",
	"counting-entrance",
	"pos-lane",
	"grocery-till",
	"cart-aisle",
	"luxury-open",
	"plexi-boutique",
	"night-sleep",
	"apparel-labels",
	"chilled-labels",
	"deactivation-pad",
	"security-ops",
	"cosmetics-sco",
	"electronics",
	"sports-retail",
	"department-store",
	"discreet-staff",
	"grey-gate",
	"high-traffic",
	"branded-entrance",
	"cosmetics-luxury",
	"upward-light",
	"tablet-health",
	"beauty-labels",
	"sco-deactivator",
	"fashion-till-pad",
	"vms-wall",
	"staff-phone",
	"metal-detect",
)

# slug → (scene_key, title, description, image_alt)
APPLICATIONS_BY_SLUG: dict[str, list[tuple[str, str, str, str]]] = {
	"nedap-rf-eas": [
		("fashion-mall", "Fashion and mall retail", "Connected RF EAS at premium storefronts without closing the entrance.", "Fashion mall entrance with RF EAS gates"),
		("supermarket-carts", "Supermarkets and grocery", "Transparent and compact antennas that keep carts and families moving.", "Supermarket entrance with shopping carts"),
		("self-checkout", "Self-checkout zones", "Place detection where staff can still respond — at SCO exits and tills.", "Self-checkout hall with compact EAS antennas"),
	],
	"nedap-i15-go": [
		("boutique-narrow", "Narrow fashion entrances", "A ~15 cm antenna that protects the door without blocking merchandise.", "Compact EAS antenna at a boutique door"),
		("pharmacy", "Pharmacies and convenience", "Slim protection for neighbourhood stores where every centimetre counts.", "Pharmacy doorway with compact RF EAS"),
		("cosmetics-sco", "Beauty self-checkout", "Compact RF EAS beside SCO kiosks in cosmetics and specialty retail.", "Cosmetics self-checkout with slim EAS antenna"),
	],
	"nedap-i45": [
		("fashion-chain", "Fashion chains", "A robust RF antenna specified once and rolled out across many stores.", "Fashion-chain mall entrance with RF EAS"),
		("hypermarket", "Hypermarkets", "High-performance detection at wide, high-traffic grocery entrances.", "Hypermarket entrance with RF EAS pedestals"),
		("department-store", "Department stores", "Scalable RF EAS for multi-level retail and shared service teams.", "Department store atrium with EAS gates"),
	],
	"nedap-il45": [
		("premium-lumen", "Premium fashion", "Lumen lighting makes alarms visible without a harsh storefront aesthetic.", "Premium boutique entrance with Lumen EAS"),
		("counting-entrance", "Traffic and conversion", "Integrated customer counting turns the entrance into a visitor sensor.", "Department-store entrance with people counting"),
		("electronics", "Electronics retail", "Configurable light and sound help staff react on a busy sales floor.", "Electronics store entrance with RF EAS"),
	],
	"nedap-checkout-antenna": [
		("pos-lane", "Staffed checkout lanes", "Detection at the till so cashiers can respond before the customer leaves.", "Supermarket checkout with EAS at the POS"),
		("grocery-till", "High-volume grocery", "Keep the conversation at the belt — not at the exit after payment.", "Grocery till with checkout EAS antenna"),
		("discreet-staff", "Fashion cash wrap", "Quieter, more discreet intervention while staff already have eye contact.", "Fashion cashier beside a checkout EAS panel"),
	],
	"nedap-i37": [
		("cart-aisle", "Cart and trolley exits", "A slim transparent panel that stays out of the way of grocery traffic.", "Shopping carts passing transparent EAS gates"),
		("grey-gate", "Black or grey finishes", "Match supermarket interiors with black or grey i37 editions.", "Grey transparent supermarket EAS gates"),
		("high-traffic", "Peak grocery hours", "Robust RF EAS for Friday and evening rushes in KSA hypermarkets.", "Busy supermarket exit with EAS gates"),
	],
	"nedap-i30": [
		("luxury-open", "Luxury and fashion", "An open silver frame that reads as store design, not a security cage.", "Luxury fashion lobby with open EAS gate"),
		("branded-entrance", "Flagship store concepts", "Adapt the look so the antenna follows the brand, not the other way around.", "Fashion flagship entrance with slender EAS"),
		("cosmetics-luxury", "Cosmetics galleries", "Keep perfume and beauty halls visually open while protecting merchandise.", "Luxury cosmetics hall with open EAS antenna"),
	],
	"nedap-il33": [
		("plexi-boutique", "Premium boutiques", "Full plexiglass Lumen design for interiors that cannot accept a heavy frame.", "Plexiglass EAS antenna in a boutique"),
		("sports-retail", "Sports and lifestyle", "Transparent security that does not compete with product displays.", "Sports store entrance with plexiglass EAS"),
		("upward-light", "Staff-visible alarms", "Upward lighting helps teams see an event from inside the store.", "Plexiglass EAS with upward alarm illumination"),
	],
	"nedap-isenseos": [
		("night-sleep", "Sleep Mode overnight", "Standby supported systems after close to cut energy use across the estate.", "Closed store at night with EAS on standby"),
		("tablet-health", "Remote health monitoring", "See antenna status across Riyadh, Jeddah and Dammam stores from one view.", "Facilities manager reviewing EAS system health"),
		("security-ops", "Security operations", "Turn each alarm into context for the loss-prevention team.", "Retail security room monitoring store cameras"),
	],
	"nedap-rf-eas-labels": [
		("apparel-labels", "Dry merchandise", "Power Labels for boxes, cartons, bottles and fashion source tagging.", "RF security labels applied to apparel"),
		("chilled-labels", "Chilled and frozen", "Cool Labels specified for meat, fish, cheese and freezer conditions.", "RF labels on chilled supermarket packs"),
		("beauty-labels", "Health and beauty", "Compact Beauty Labels for curved, metallic or small cosmetic packs.", "Small RF labels on cosmetics packaging"),
	],
	"nedap-eas-deactivation": [
		("deactivation-pad", "Staffed POS", "360° deactivation at the scanner so paid merchandise leaves quietly.", "RF deactivation pad at a grocery checkout"),
		("sco-deactivator", "Self-checkout", "Plug-in deactivation for common SCO platforms used in KSA grocery.", "Self-checkout with built-in RF deactivator"),
		("fashion-till-pad", "Fashion cash wrap", "Deactivate tags at the desk without a separate removal step.", "Fashion till with RF deactivation pad"),
	],
	"nedap-eas-integrations": [
		("vms-wall", "CCTV and VMS", "Bookmark and retrieve the camera moment that matches an EAS event.", "Video wall highlighting an entrance event"),
		("staff-phone", "Staff notifications", "Push the alarm to the device already in a supervisor’s hand.", "Store supervisor reading a phone alert"),
		("metal-detect", "Metal detection", "Add booster-bag detection at the same entrance as RF EAS.", "Supermarket entrance with metal-detection EAS"),
	],
}

KSA_BODY = (
	"Printechs provides consultation, supply, installation, configuration and support "
	"for Nedap retail EAS solutions across Saudi Arabia, including Riyadh, Jeddah, "
	"Dammam and other regions. We specify the antenna, labels, deactivation and "
	"iSenseOS integrations for each store format — then stay on for service."
)

# Unique 4:3 KSA service scenes — never reuse industry-retail.jpg or another page's KSA image.
KSA_SCENE_BY_SLUG: dict[str, tuple[str, str]] = {
	"nedap-rf-eas": ("nedap-ksa-hub", "Nedap RF EAS commissioning at a Saudi mall entrance"),
	"nedap-i15-go": ("nedap-ksa-i15", "Compact i15 Go EAS install beside Saudi self-checkout"),
	"nedap-i45": ("nedap-ksa-i45", "i45 RF EAS installation at a Saudi fashion-chain storefront"),
	"nedap-il45": ("nedap-ksa-il45", "iL45 Lumen EAS install at a Saudi premium boutique"),
	"nedap-checkout-antenna": ("nedap-ksa-checkout", "Checkout EAS antenna fitted into a Saudi grocery till"),
	"nedap-i37": ("nedap-ksa-i37", "i37 wide-aisle EAS commissioning at a Saudi supermarket exit"),
	"nedap-i30": ("nedap-ksa-i30", "i30 open-frame EAS install at a Saudi pharmacy entrance"),
	"nedap-il33": ("nedap-ksa-il33", "iL33 Lumen EAS install at a Saudi boutique storefront"),
	"nedap-isenseos": ("nedap-ksa-isenseos", "Retail team reviewing iSenseOS store health in KSA"),
	"nedap-rf-eas-labels": ("nedap-ksa-labels", "RF EAS labels applied in a Saudi apparel stockroom"),
	"nedap-eas-deactivation": ("nedap-ksa-deact", "RF deactivation pad install at a Saudi grocery checkout"),
	"nedap-eas-integrations": ("nedap-ksa-integrations", "EAS controller integration with POS in a Saudi IT workshop"),
}


def site_file(filename: str) -> str:
	return f"/files/{filename}"


def make_card(src: Path, dest_name: str) -> str:
	"""1200×1200 white-padded JPEG catalog / hero card."""
	dest = SITE_FILES / dest_name
	im = Image.open(src).convert("RGBA")
	scale = min(1040 / im.width, 1040 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
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
	src = TMP_DIR / "nedap-logo.png"
	if not src.exists():
		frappe.throw("Missing Nedap logo at /tmp/nedap/nedap-logo.png")
	im = Image.open(src).convert("RGBA")
	canvas = Image.new("RGBA", (400, 160), (255, 255, 255, 0))
	scale = min(360 / im.width, 120 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	x = (400 - new.width) // 2
	y = (160 - new.height) // 2
	canvas.paste(new, (x, y), new)
	for dest in (SITE_FILES / "brand-nedap.png", BRAND_DIR / "brand-nedap.png"):
		dest.parent.mkdir(parents=True, exist_ok=True)
		canvas.save(dest, "PNG")
	return site_file("brand-nedap.png")


def _find_scene(key: str) -> Path:
	candidates = [
		ASSETS_DIR / f"nedap-app-{key}.png",
		ASSETS_DIR / f"nedap-app-{key}.jpg",
		SITE_FILES / f"nedap-app-{key}.jpg",
	]
	for path in candidates:
		if path.exists():
			return path
	frappe.throw(f"Missing Nedap application scene: nedap-app-{key}")


def _find_ksa(stem: str) -> Path:
	for path in (ASSETS_DIR / f"{stem}.png", ASSETS_DIR / f"{stem}.jpg", SITE_FILES / f"{stem}.jpg"):
		if path.exists():
			return path
	frappe.throw(f"Missing unique Nedap KSA scene: {stem}")


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
		filename = f"nedap-app-{key}.jpg"
		path = save_app_scene(_find_scene(key), filename)
		copy2(SITE_FILES / filename, app_dir / filename)
		media[key] = path
	return media


def prepare_media() -> dict[str, str]:
	SITE_FILES.mkdir(parents=True, exist_ok=True)
	(LIBRARY / "products").mkdir(parents=True, exist_ok=True)

	official = {
		"i15": TMP_DIR / "i15.jpg",
		"i37": TMP_DIR / "i37.jpg",
		"i30": TMP_DIR / "i30.jpg",
		"il45": TMP_DIR / "il45.jpg",
		"il33": TMP_DIR / "il33.jpg",
		"checkout": TMP_DIR / "checkout.jpg",
	}
	for key, path in official.items():
		if not path.exists():
			frappe.throw(f"Missing official Nedap photo: {path}")

	studios = {
		"i45": ASSETS_DIR / "nedap-i45-studio.png",
		"labels": ASSETS_DIR / "nedap-labels-studio.png",
		"deactivator": ASSETS_DIR / "nedap-deactivator-studio.png",
		"isenseos": ASSETS_DIR / "nedap-isenseos-studio.png",
		"integrations": ASSETS_DIR / "nedap-integrations-studio.png",
	}
	for key, path in studios.items():
		if not path.exists():
			frappe.throw(f"Missing generated Nedap studio image: {path}")

	cards = {
		"i15": make_card(official["i15"], "nedap-i15-go-card.jpg"),
		"i45": make_card(studios["i45"], "nedap-i45-card.jpg"),
		"il45": make_card(official["il45"], "nedap-il45-card.jpg"),
		"checkout": make_card(official["checkout"], "nedap-checkout-antenna-card.jpg"),
		"i37": make_card(official["i37"], "nedap-i37-card.jpg"),
		"i30": make_card(official["i30"], "nedap-i30-card.jpg"),
		"il33": make_card(official["il33"], "nedap-il33-card.jpg"),
		"labels": make_card(studios["labels"], "nedap-rf-eas-labels-card.jpg"),
		"deactivator": make_card(studios["deactivator"], "nedap-eas-deactivation-card.jpg"),
		"isenseos": make_card(studios["isenseos"], "nedap-isenseos-card.jpg"),
		"integrations": make_card(studios["integrations"], "nedap-eas-integrations-card.jpg"),
	}
	hub_src = ASSETS_DIR / "nedap-app-fashion-mall.png"
	cards["hub"] = make_card(hub_src, "nedap-rf-eas-card.jpg")

	for name in (
		"nedap-i15-go-card.jpg",
		"nedap-i45-card.jpg",
		"nedap-il45-card.jpg",
		"nedap-checkout-antenna-card.jpg",
		"nedap-i37-card.jpg",
		"nedap-i30-card.jpg",
		"nedap-il33-card.jpg",
		"nedap-rf-eas-labels-card.jpg",
		"nedap-eas-deactivation-card.jpg",
		"nedap-isenseos-card.jpg",
		"nedap-eas-integrations-card.jpg",
		"nedap-rf-eas-card.jpg",
	):
		copy2(SITE_FILES / name, LIBRARY / "products" / name)

	media = {
		**cards,
		**install_application_scenes(),
		**install_ksa_scenes(),
		"logo": install_logo(),
	}
	return media


def scene_apps(media: dict[str, str], slug: str) -> list[dict]:
	rows = APPLICATIONS_BY_SLUG.get(slug)
	if not rows:
		frappe.throw(f"No unique application scenes mapped for {slug}")
	out = []
	for i, (key, title, description, alt) in enumerate(rows, start=1):
		out.append({
			"title": title,
			"description": description,
			"image": media[key],
			"image_alt": alt,
			"industry_link": "retail",
			"sort_order": i,
		})
	return out


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
	doc.short_description = f"{display_name} for retail loss prevention."
	doc.long_description = f"<p>{display_name} for retail loss prevention.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, category_label, featured=0):
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
	doc.featured = featured
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = "Nedap"
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
		{
			"icon": "install",
			"title": "Site survey & installation",
			"description": "Entrance, SCO and POS surveys in Riyadh, Jeddah and Dammam — then professional install.",
			"sort_order": 1,
		},
		{
			"icon": "consumables",
			"title": "Labels & deactivation",
			"description": "Power, Cool and Beauty RF labels plus 360° deactivation specified with the antennas.",
			"sort_order": 2,
		},
		{
			"icon": "maintenance",
			"title": "Service & warranty",
			"description": "Factory warranty is 1 year; extended 3- or 5-year cover can be quoted with local service.",
			"sort_order": 3,
		},
		{
			"icon": "training",
			"title": "Team training",
			"description": "Alarm response, label placement and iSenseOS monitoring for store and LP teams.",
			"sort_order": 4,
		},
	]


def ksa_section(media: dict[str, str], slug: str, sort_order: int = 2) -> dict:
	key = f"ksa:{slug}"
	if key not in media or slug not in KSA_SCENE_BY_SLUG:
		frappe.throw(f"Missing unique KSA scene for {slug}")
	return {
		"section_type": "Industry Solution",
		"heading": "Nedap EAS Solutions in Saudi Arabia",
		"body": KSA_BODY,
		"image": media[key],
		"image_alt": KSA_SCENE_BY_SLUG[slug][1],
		"link_label": "Talk to Our Retail Security Team",
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
