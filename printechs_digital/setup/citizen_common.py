# Copyright (c) 2026, Printechs and contributors
"""Shared helpers for Citizen 80 mm POS printer website fills.

Do not attach spare-part Items (Wi-Fi cards, cables).
Do not set featured=1 — leave the homepage featured list unchanged.
Do not put YouTube on Website Product.video_url (hero poster stays a still).
Do not reuse the same official photo or YouTube ID across pages.
"""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
BASE = "https://www.citizen-systems.com"
BRAND = "Citizen"
CARD_BRAND = "Citizen"
HEADERS = {
	"User-Agent": (
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
		"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	),
	"Accept-Encoding": "identity",
}


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if target.exists() and target.stat().st_size > 8000:
		return f"/files/{filename}"
	request = Request(url, headers=HEADERS)
	with urlopen(request, timeout=45) as response:
		data = response.read()
	if data[:15].lstrip().startswith(b"<!DOCTYPE") or data[:6].lstrip().startswith(b"<html"):
		raise RuntimeError(f"Download was HTML, not an image: {url}")
	target.write_bytes(data)
	return f"/files/{filename}"


def catalog_card(source_name: str, dest_name: str) -> str:
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGBA")
	scale = 900 / max(im.size)
	new = im.resize((int(im.width * scale), int(im.height * scale)), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	canvas.paste(new.convert("RGB"), ((1200 - new.width) // 2, (1200 - new.height) // 2), new)
	canvas.save(dest, "JPEG", quality=92, optimize=True)
	return f"/files/{dest_name}"


def prepare_citizen_logo() -> str:
	"""Official Citizen wordmark, padded to the 400 × 160 website-brand slot."""
	raw = download_file("citizen-logo-official.png", f"{BASE}/assets/images/logo_dark.png")
	src = SITE_FILES / "citizen-logo-official.png"
	dest_name = "brand-citizen.png"
	im = Image.open(src).convert("RGBA")
	canvas = Image.new("RGBA", (400, 160), (0, 0, 0, 0))
	scale = min(360 / im.width, 120 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas.paste(new, ((400 - new.width) // 2, (160 - new.height) // 2), new)
	site_dest = SITE_FILES / dest_name
	canvas.save(site_dest, "PNG", optimize=True)
	BRAND_DIR.mkdir(parents=True, exist_ok=True)
	copy2(site_dest, BRAND_DIR / dest_name)
	return f"/files/{dest_name}"


def update_website_brand(logo: str):
	if not frappe.db.exists("Brand", BRAND):
		frappe.throw("ERP Brand Citizen was not found")
	name = frappe.db.get_value("Website Brand", {"slug": "citizen"}, "name")
	doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
	doc.brand = BRAND
	doc.display_name = "Citizen"
	doc.slug = "citizen"
	doc.logo = logo
	doc.summary = (
		"Citizen Systems 80 mm thermal POS printers for retail and hospitality "
		"checkout — supplied and supported by Printechs in Saudi Arabia."
	)
	doc.sort_order = 14
	doc.official_website = f"{BASE}/en/products/printer/pos/overview"
	doc.show_in_footer = 1
	doc.published = 1
	doc.meta_title = "Citizen POS Printers | Printechs Brands"
	doc.meta_description = (
		"Citizen 80 mm POS receipt and liner-free printers from Printechs in Saudi Arabia."
	)
	doc.flags.ignore_permissions = True
	if name:
		doc.save()
	else:
		doc.insert()
	frappe.db.commit()
	print(f"Website Brand Citizen → /brands/citizen ({doc.name})")
	return doc.name


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


def get_or_create(slug: str, display_name: str, hero: str):
	existing = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = slug
	doc.item = None
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "POS Hardware"
	doc.subcategory = "Receipt Printers"
	doc.short_description = f"{display_name} 80 mm Citizen POS printer."
	doc.long_description = f"<p>{display_name} 80 mm Citizen POS printer.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, category_label):
	doc.item = None
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	if frappe.db.exists("Brand", BRAND):
		doc.brand = BRAND
	doc.brand_name = CARD_BRAND
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.page_mode = "Full"
	doc.category = "POS Hardware"
	doc.subcategory = "Receipt Printers"
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = CARD_BRAND
	doc.show_item_code_on_website = 0
	doc.video_url = ""
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to Our Team"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1
	doc.is_hub = 0


def support_items():
	return [
		{
			"icon": "install",
			"title": "Counter survey & install",
			"description": "Checkout, hospitality or pharmacy mounting in Riyadh, Jeddah and Dammam.",
			"sort_order": 1,
		},
		{
			"icon": "integration",
			"title": "POS integration",
			"description": "Drivers and I/O for Modern POS, FEC terminals and other POS PCs.",
			"sort_order": 2,
		},
		{
			"icon": "consumables",
			"title": "80 mm media",
			"description": "Receipt rolls or liner-free labels quoted with the printer — not mixed as SKUs here.",
			"sort_order": 3,
		},
		{
			"icon": "maintenance",
			"title": "Service in KSA",
			"description": "Spares, cutters and on-site support after the lane is live.",
			"sort_order": 4,
		},
	]


def ksa_section(image: str, image_alt: str, sort_order: int = 1) -> dict:
	return {
		"section_type": "Industry Solution",
		"heading": "Specified and installed in Saudi Arabia",
		"body": (
			"Printechs specifies Citizen 80 mm POS printers for retail and hospitality "
			"lanes in Riyadh, Jeddah and Dammam — interface, cutter, colour and media "
			"locked to the counter, not a generic box."
		),
		"image": image,
		"image_alt": image_alt,
		"sort_order": sort_order,
	}


def video_section(*, heading, body, video_url, image, image_alt, sort_order):
	return {
		"section_type": "Industry Solution",
		"heading": heading,
		"body": body,
		"video_url": video_url,
		"image": image,
		"image_alt": image_alt,
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
