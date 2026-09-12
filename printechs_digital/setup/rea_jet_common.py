# Copyright (c) 2026, Printechs and contributors
"""Shared helpers for REA JET Website Product fills.

Do not reuse DOD 2.0 controller photos or YouTube IDs on other REA pages.
Do not attach consumable or spare-part Items.
"""

from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
ASSETS = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
BASE = "https://www.rea-jet.com"
BRAND = "Reajet"
CARD_BRAND = "REA JET"

OFFICIAL_IMAGES = {
	# HR 2.0 — skip TITAN controllers already used on rea-jet-dod-2
	"rea-jet-hr2-overview.jpg": f"{BASE}/product/rea-jet/hr-2/1232/image-thumb__1232__lightbox_image/hr-2-uebersicht-02@2x.bacdce8f.jpg",
	"rea-jet-hr2-1sk.jpg": f"{BASE}/product/rea-jet/hr-2/541/image-thumb__541__lightbox_image/HR%202.0%20-%201%20SK@2x.b7960cdf.jpg",
	"rea-jet-hr2-4sk.jpg": f"{BASE}/product/rea-jet/hr-2/537/image-thumb__537__lightbox_image/HR%202.0%20-%204%20SK@2x.800a4e2b.jpg",
	"rea-jet-hr2-wet.png": f"{BASE}/product/rea-jet/hr-2/539/image-thumb__539__lightbox_image/HR%202.0%20-%20Nass-in-Nass-Druck@2x.cbf845b7.png",
	"rea-jet-hr2-pouch.jpg": f"{BASE}/product/rea-jet/hr-2/543/image-thumb__543__lightbox_image/HR%202.0%20-%20Folienschlauchbeutel@2x.daf4ae68.jpg",
	"rea-jet-hr2-pipe.jpg": f"{BASE}/product/rea-jet/hr-2/558/image-thumb__558__lightbox_image/hr-2-wasserrohr@2x.28d051fe.jpg",
	"rea-jet-hr2-pharma.jpg": f"{BASE}/product/rea-jet/hr-2/560/image-thumb__560__lightbox_image/HR%202.0%20-%20Pharmaverpackungen@2x.162fcb35.jpg",
	"rea-jet-hr2-fiberglass.jpg": f"{BASE}/product/rea-jet/hr-2/559/image-thumb__559__lightbox_image/HR%202.0%20-%20Fiberglassplatte@2x.aabb1807.jpg",
	"rea-jet-hr2-packs.png": f"{BASE}/product/rea-jet/hr-2/1237/image-thumb__1237__lightbox_image/hr-2-verpackungen@2x.7021d5d1.png",
	"rea-jet-hr2-metal.jpg": f"{BASE}/product/rea-jet/hr-2/1238/image-thumb__1238__lightbox_image/hr-2-metallprofile-nass-in-nass-druck@2x.b70373d5.jpg",
	"rea-jet-hr2-wood.jpg": f"{BASE}/product/rea-jet/hr-2/544/image-thumb__544__lightbox_image/HR%202.0%20-%20Holzschnittkante@2x.8c886826.jpg",
	# UP
	"rea-jet-up-overview.png": f"{BASE}/product/rea-jet/up/1422/image-thumb__1422__lightbox_image/up-uebersicht@2x.0847788f.png",
	"rea-jet-up-kombi.jpg": f"{BASE}/product/rea-jet/up/1549/image-thumb__1549__lightbox_image/up-kombi-03@2x.d7a025dd.jpg",
	"rea-jet-up-carton-01.jpg": f"{BASE}/product/rea-jet/up/1413/image-thumb__1413__lightbox_image/up-kartonage-01@2x.504502b5.jpg",
	"rea-jet-up-carton-03.jpg": f"{BASE}/product/rea-jet/up/1414/image-thumb__1414__lightbox_image/up-kartonage-03@2x.bd640de7.jpg",
	"rea-jet-up-carton-04.jpg": f"{BASE}/product/rea-jet/up/1405/image-thumb__1405__lightbox_image/up-kartonage-04@2x.bca05c0b.jpg",
	"rea-jet-up-carton-08.jpg": f"{BASE}/product/rea-jet/up/1404/image-thumb__1404__lightbox_image/up-kartonage-08@2x.d26637cb.jpg",
	"rea-jet-up-wood.jpg": f"{BASE}/product/rea-jet/up/1417/image-thumb__1417__lightbox_image/up-holz-01@2x.0f726b8c.jpg",
	"rea-jet-up-secondary.jpg": f"{BASE}/product/rea-jet/up/1402/image-thumb__1402__lightbox_image/up-umverpackung@2x.132890f2.jpg",
	# GK 2.0
	"rea-jet-gk2-overview.png": f"{BASE}/product/rea-jet/gk-2/1397/image-thumb__1397__lightbox_image/gk-2-gesamtansicht@2x.f3a64eca.png",
	"rea-jet-gk2-384.jpg": f"{BASE}/product/rea-jet/gk-2/1375/image-thumb__1375__lightbox_image/gk-2-384-fest@2x.e8eb8a75.jpg",
	"rea-jet-gk2-768.jpg": f"{BASE}/product/rea-jet/gk-2/1376/image-thumb__1376__lightbox_image/gk-2-768-fest@2x.c9fe2daf.jpg",
	"rea-jet-gk2-hose.jpg": f"{BASE}/product/rea-jet/gk-2/1373/image-thumb__1373__lightbox_image/gk-2-768-mit-schlauch-01@2x.2fefd4ae.jpg",
	"rea-jet-gk2-pallet.jpg": f"{BASE}/product/rea-jet/gk-2/1380/image-thumb__1380__lightbox_image/gk-2-palette-01@2x.671e4d0b.jpg",
	"rea-jet-gk2-carton.jpg": f"{BASE}/product/rea-jet/gk-2/1384/image-thumb__1384__lightbox_image/gk-2-karton-02@2x.b78a0c53.jpg",
	"rea-jet-gk2-bags.jpg": f"{BASE}/product/rea-jet/gk-2/1387/image-thumb__1387__lightbox_image/gk-2-papiersaecke-01@2x.2332c917.jpg",
	"rea-jet-gk2-plaster.jpg": f"{BASE}/product/rea-jet/gk-2/1385/image-thumb__1385__lightbox_image/gk-2-gipskarton@2x.e206e892.jpg",
	# CL laser
	"rea-jet-cl-product.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1650/image-thumb__1650__lightbox_image/rea-laser-cl@2x.739adb42.jpg",
	"rea-jet-cl-kombi.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1933/image-thumb__1933__lightbox_image/rea-laser-cl-kombi-02@2x.ce60ee05.jpg",
	"rea-jet-cl-head.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1942/image-thumb__1942__lightbox_image/rea-laser-lasereinheit@2x.cb90e3a5.jpg",
	"rea-jet-cl-wood.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1670/image-thumb__1670__lightbox_image/rea-laser-cl-holz@2x.2367d975.jpg",
	"rea-jet-cl-capsules.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1663/image-thumb__1663__lightbox_image/rea-laser-cl-kaffeekapseln@2x.76b1cd5c.jpg",
	"rea-jet-cl-profile.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1659/image-thumb__1659__lightbox_image/rea-laser-cl-kunststoffprofil-02@2x.c6604db1.jpg",
	"rea-jet-cl-pharma.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1668/image-thumb__1668__lightbox_image/rea-laser-cl-pharmafaltschachtel-01@2x.1b7543ac.jpg",
	"rea-jet-cl-tire.jpg": f"{BASE}/product/rea-laser/rea-laser-cl/1653/image-thumb__1653__lightbox_image/rea-laser-cl-reifen-01@2x.5e944ce6.jpg",
	# FL laser — unique metal/plastic shots, own cabinet photo
	"rea-jet-fl-product.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1690/image-thumb__1690__lightbox_image/rea-laser-fl@2x.0216f7c4.jpg",
	"rea-jet-fl-metal-02.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1682/image-thumb__1682__lightbox_image/rea-laser-fl-metall-02@2x.ff140bb1.jpg",
	"rea-jet-fl-metal-03.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1686/image-thumb__1686__lightbox_image/rea-laser-fl-metall-03@2x.3441e630.jpg",
	"rea-jet-fl-plastic.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1684/image-thumb__1684__lightbox_image/rea-laser-fl-kunststoffteil-01@2x.9ed31811.jpg",
	"rea-jet-fl-tweezers.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1685/image-thumb__1685__lightbox_image/rea-laser-fl-pinzette-01@2x.cd50af25.jpg",
	"rea-jet-fl-cap.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1681/image-thumb__1681__lightbox_image/rea-laser-fl-verschlusskappe@2x.0fba022e.jpg",
	"rea-jet-fl-metal-01.jpg": f"{BASE}/product/rea-laser/rea-laser-fl/1689/image-thumb__1689__lightbox_image/rea-laser-fl-metall-01@2x.0801ebaa.jpg",
	# Spray mark family
	"rea-jet-stc-system.jpg": f"{BASE}/product/rea-jet/stc/2988/image-thumb__2988__lightbox_image/stc-flexiles-system-01@2x.e93165e9.jpg",
	"rea-jet-stc-piston.jpg": f"{BASE}/product/rea-jet/stc/1484/image-thumb__1484__lightbox_image/st-punktmarkierung-kolben-02@2x.ea960da0.jpg",
	"rea-jet-stc-color.jpg": f"{BASE}/product/rea-jet/stc/1491/image-thumb__1491__lightbox_image/stc-farbkennzeichnung-01@2x.ee207cfe.jpg",
	"rea-jet-stc-shaft.jpg": f"{BASE}/product/rea-jet/stc/1519/image-thumb__1519__lightbox_image/stc-antriebswelle@2x.e9e9f00e.jpg",
	"rea-jet-stc-line.jpg": f"{BASE}/product/rea-jet/stc/1487/image-thumb__1487__lightbox_image/stc-linienmarkierung-01@2x.df26f35f.jpg",
	"rea-jet-stf-system.png": f"{BASE}/product/rea-jet/stf/1483/image-thumb__1483__lightbox_image/st-komplettsystem-03@2x.bc6a24b5.png",
	"rea-jet-stf-heads.jpg": f"{BASE}/product/rea-jet/stf/1477/image-thumb__1477__lightbox_image/st-signierkoepfe-01@2x.dfb90469.jpg",
	"rea-jet-stf-units.jpg": f"{BASE}/product/rea-jet/stf/2993/image-thumb__2993__lightbox_image/stf1-stf2-01@2x.5bb22fc0.jpg",
	"rea-jet-stf-ring.jpg": f"{BASE}/product/rea-jet/stf/1467/image-thumb__1467__lightbox_image/st-ringmarkierung-01@2x.3befbf1b.jpg",
	"rea-jet-stf-cable.jpg": f"{BASE}/product/rea-jet/stf/1466/image-thumb__1466__lightbox_image/st-drahtseil@2x.e07ae805.jpg",
	"rea-jet-eds-heads.jpg": f"{BASE}/product/rea-jet/eds/2974/image-thumb__2974__lightbox_image/eds-schreibkoepfe01@2x.caa7d3a2.jpg",
	"rea-jet-eds-coupling.jpg": f"{BASE}/product/rea-jet/eds/1458/image-thumb__1458__lightbox_image/eds-fuenf-kupplung@2x.ccab9310.jpg",
}


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"})
		with urlopen(request, timeout=45) as response:
			data = response.read()
		if data[:15].lstrip().startswith(b"<!DOCTYPE") or data[:6].lstrip().startswith(b"<html"):
			raise RuntimeError(f"Download was HTML, not an image: {url}")
		target.write_bytes(data)
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
	canvas.paste(new.convert("RGB"), ((1200 - new.width) // 2, (1200 - new.height) // 2), new)
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


def cover_card(source: Path, dest_name: str, size=(1200, 1200)) -> str:
	dest = SITE_FILES / dest_name
	im = Image.open(source).convert("RGB")
	target_ratio = size[0] / size[1]
	width, height = im.size
	if width / height > target_ratio:
		new_w = int(height * target_ratio)
		left = (width - new_w) // 2
		im = im.crop((left, 0, left + new_w, height))
	else:
		new_h = int(width / target_ratio)
		top = (height - new_h) // 2
		im = im.crop((0, top, width, top + new_h))
	im = im.resize(size, Image.Resampling.LANCZOS)
	im.save(dest, "JPEG", quality=90, optimize=True)
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
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.short_description = f"{display_name} industrial coding and marking."
	doc.long_description = f"<p>{display_name} industrial coding and marking.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, category_label, subcategory, featured=0, is_hub=0):
	doc.item = None
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	if frappe.db.exists("Brand", BRAND):
		doc.brand = BRAND
	doc.product_type = "Industrial"
	doc.division = "Industrial"
	doc.category = "Coding & Marking"
	doc.subcategory = subcategory
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.featured = featured
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.card_brand_label = CARD_BRAND
	doc.show_item_code_on_website = 0
	doc.video_url = ""
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
		{"icon": "install", "title": "Line survey & install", "description": "Substrate, throw, photocell and mounting in Riyadh, Jeddah and Dammam.", "sort_order": 1},
		{"icon": "consumables", "title": consumable, "description": "Genuine REA fluids or laser-safe integration quoted with the machine — not mixed onto this page as SKUs.", "sort_order": 2},
		{"icon": "maintenance", "title": "Service in KSA", "description": "Commissioning, spares and on-site support after the line is running.", "sort_order": 3},
		{"icon": "training", "title": "TITAN training", "description": "One operating concept across REA JET ink, paint and laser — operators train once.", "sort_order": 4},
	]


def ksa_section(image: str, image_alt: str, sort_order: int) -> dict:
	return {
		"section_type": "Industry Solution",
		"heading": "Specified and installed in Saudi Arabia",
		"body": (
			"Printechs surveys the pack, speed and code, then installs REA JET in Riyadh, "
			"Jeddah and Dammam — including encoder, photocell and TITAN messages. We do "
			"not quote small-character CIJ (SC 2.0) on these pages."
		),
		"image": image,
		"image_alt": image_alt,
		"sort_order": sort_order,
	}


def video_section(*, heading, body, video_url, image, image_alt, sort_order):
	"""Official film in a content section — never set Website Product.video_url.

	Do not set link_href here. The API promotes a section video to the hero
	when the section link points at this product.
	"""
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
