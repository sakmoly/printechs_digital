# Copyright (c) 2026, Printechs and contributors
"""Shared helpers for Zebra barcode-printer website fills."""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image, ImageFilter, ImageDraw

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
TMP_DIR = Path("/tmp/zebra-lineup")

HEADERS = {
	"User-Agent": (
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
		"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	)
}


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def download_file(filename: str, urls: list[str], tmp_name: str | None = None) -> str:
	target = SITE_FILES / filename
	if target.exists() and target.stat().st_size > 20000:
		return f"/files/{filename}"
	last_error = None
	for url in urls:
		try:
			request = Request(url, headers=HEADERS)
			with urlopen(request, timeout=30) as response, target.open("wb") as handle:
				handle.write(response.read())
			if target.exists() and target.stat().st_size > 20000:
				return f"/files/{filename}"
		except Exception as exc:
			last_error = exc
	if tmp_name:
		fallback = TMP_DIR / tmp_name
		if fallback.exists() and fallback.stat().st_size > 20000:
			copy2(fallback, target)
			return f"/files/{filename}"
	if last_error:
		raise last_error
	frappe.throw(f"Could not download {filename}")


def wipe_reseller_badge(filename: str) -> str:
	"""Remove blue Wi-Fi 6 pills without cutting the printer body."""
	path = SITE_FILES / filename
	im = Image.open(path)
	fmt = (im.format or path.suffix.lstrip(".")).upper()
	if fmt == "JPG":
		fmt = "JPEG"
	rgba = im.convert("RGBA")
	pixels = rgba.load()
	w, h = rgba.size
	ys = range(int(h * 0.62), h)
	xs = list(range(0, int(w * 0.42))) + list(range(int(w * 0.58), w))
	blue_xy = []
	for y in ys:
		for x in xs:
			r, g, b, a = pixels[x, y]
			if a > 20 and b > 150 and b > r + 50 and b > g + 30:
				blue_xy.append((x, y))
	if blue_xy:
		xs_b = [p[0] for p in blue_xy]
		ys_b = [p[1] for p in blue_xy]
		pad = max(18, int(min(w, h) * 0.018))
		box = (
			max(0, min(xs_b) - pad),
			max(0, min(ys_b) - pad),
			min(w, max(xs_b) + pad),
			min(h, max(ys_b) + pad),
		)
		mask = Image.new("L", (w, h), 0)
		draw = ImageDraw.Draw(mask)
		draw.rounded_rectangle(box, radius=pad, fill=255)
		mask = mask.filter(ImageFilter.GaussianBlur(2))
		white = Image.new("RGBA", (w, h), (255, 255, 255, 255))
		rgba = Image.composite(white, rgba, mask)
	if fmt == "PNG":
		rgba.save(path, "PNG", optimize=True)
	else:
		rgba.convert("RGB").save(path, "JPEG", quality=92, optimize=True)
	return f"/files/{filename}"


def catalog_card(source_name: str, dest_name: str, crop_badge: bool = False) -> str:
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGBA")
	scale = min(1040 / im.width, 1040 / im.height)
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


def get_or_create(slug: str, display_name: str, item: str, hero: str, subcategory: str):
	existing = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = slug
	if item and frappe.db.exists("Item", item):
		other = frappe.db.get_value("Website Product", {"item": item}, "name")
		if not other:
			doc.item = item
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = subcategory
	doc.short_description = f"{display_name} barcode label printer."
	doc.long_description = f"<p>{display_name} barcode label printer.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, item, subcategory, category_label):
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	if item and frappe.db.exists("Item", item) and not doc.item:
		other = frappe.db.get_value("Website Product", {"item": item}, "name")
		if not other or other == doc.name:
			doc.item = item
	if frappe.db.exists("Brand", "Zebra"):
		doc.brand = "Zebra"
	doc.brand_name = "Zebra"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.page_mode = "Full"
	doc.category = "Barcode & Mobility"
	doc.subcategory = subcategory
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = 0
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = "Zebra"
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to Our Team"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1


def save_product(doc, card: str | None = None):
	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	if card and doc.item and frappe.db.exists("Item", doc.item):
		item = frappe.get_doc("Item", doc.item)
		if item.image != card:
			item.db_set("image", card, update_modified=False)
	frappe.db.commit()
	print(f"Filled {doc.name} → /products/{doc.slug}")
	return doc.name
