# Copyright (c) 2026, Printechs and contributors
"""Shorten long product slugs and refresh CAS CL-5200 product photography."""

from pathlib import Path
from shutil import copy2

from PIL import Image

import frappe

from printechs_digital.api.website import PRODUCT_SLUG_ALIASES

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
LIBRARY = SITE_FILES / "library" / "cas" / "products"
OFFICIAL = Path("/tmp/cas-official")


def site_file(filename: str) -> str:
	return f"/files/{filename}"


def make_card(src: Path, dest_name: str) -> str:
	dest = SITE_FILES / dest_name
	im = Image.open(src).convert("RGBA")
	scale = min(1040 / im.width, 1040 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	dest.parent.mkdir(parents=True, exist_ok=True)
	canvas.save(dest, "JPEG", quality=92, optimize=True)
	LIBRARY.mkdir(parents=True, exist_ok=True)
	copy2(dest, LIBRARY / dest_name)
	return site_file(dest_name)


def make_wide(src: Path, dest_name: str, size: tuple[int, int] = (1600, 1000)) -> str:
	im = Image.open(src).convert("RGBA")
	tw, th = size
	scale = min(tw / im.width, th / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", size, (255, 255, 255))
	canvas.paste(new.convert("RGB"), ((tw - new.width) // 2, (th - new.height) // 2), new)
	dest = SITE_FILES / dest_name
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	LIBRARY.mkdir(parents=True, exist_ok=True)
	copy2(dest, LIBRARY / dest_name)
	return site_file(dest_name)


def install_cl5200_photos() -> dict[str, str]:
	bench = OFFICIAL / "CAS-CL5200-B-Scale.png"
	pole = OFFICIAL / "CAS-CL5200-P-Scale.png"
	cartridge = OFFICIAL / "CAS-CL5200-cartridge.png"
	missing = [str(p) for p in (bench, pole, cartridge) if not p.exists()]
	if missing:
		frappe.throw(f"Missing official CAS photos: {', '.join(missing)}")
	return {
		"bench": make_card(bench, "cas-cl-5200b.jpg"),
		"pole": make_card(pole, "cas-cl-5200p.jpg"),
		"cartridge": make_wide(cartridge, "cas-cl-5200-cartridge.jpg"),
	}


def _rewrite_text(value: str | None) -> str | None:
	if not value:
		return value
	lines = []
	for line in value.splitlines():
		stripped = line.strip()
		lines.append(PRODUCT_SLUG_ALIASES.get(stripped, stripped))
	return "\n".join(lines)


def _rewrite_related_hrefs():
	for name in frappe.get_all("Website Product Related", pluck="name"):
		row = frappe.get_doc("Website Product Related", name)
		href = row.href or ""
		new_href = href
		for old, new in PRODUCT_SLUG_ALIASES.items():
			new_href = new_href.replace(f"/products/{old}", f"/products/{new}")
		if new_href != href:
			row.href = new_href
			row.flags.ignore_permissions = True
			row.save()


def apply_cl5200_photos(photos: dict[str, str]):
	bench_name = frappe.db.get_value("Website Product", {"item": "RET.SYS.CAS.1246"}, "name")
	pole_name = frappe.db.get_value("Website Product", {"item": "RET.SYS.CAS.1247"}, "name")
	if bench_name:
		doc = frappe.get_doc("Website Product", bench_name)
		doc.hero_image = photos["bench"]
		doc.hero_image_alt = "CAS CL-5200B bench-type label printing scale"
		doc.card_image = photos["bench"]
		doc.set(
			"visual_story_items",
			[
				{
					"label": "Bench counter scale",
					"image": photos["bench"],
					"image_alt": "CAS CL-5200B bench label printing scale",
					"caption": "Official CL-5200B bench layout for delis, butcher counters, and specialty retail.",
					"sort_order": 1,
				},
				{
					"label": "Easy label cartridge",
					"image": photos["cartridge"],
					"image_alt": "CAS CL-5200 easy-loading label cartridge",
					"caption": "Quick-change thermal cartridge — the same printer used on CL-5200B and CL-5200P.",
					"sort_order": 2,
				},
				{
					"label": "Pole model also available",
					"image": photos["pole"],
					"image_alt": "CAS CL-5200P pole label printing scale",
					"caption": "Need a raised display? The CL-5200P adds a pole and 72 speed keys.",
					"sort_order": 3,
				},
			],
		)
		doc.flags.ignore_permissions = True
		doc.save()
	if pole_name:
		doc = frappe.get_doc("Website Product", pole_name)
		doc.hero_image = photos["pole"]
		doc.hero_image_alt = "CAS CL-5200P pole-type label printing scale"
		doc.card_image = photos["pole"]
		story = list(doc.visual_story_items or [])
		for row in story:
			if "bench" in (row.label or "").lower() or (row.image or "").endswith("CAS-CL5200B.png"):
				row.image = photos["bench"]
				row.image_alt = "CAS CL-5200B bench label printing scale"
		if not story:
			story = [
				{
					"label": "Pole-type retail scale",
					"image": photos["pole"],
					"image_alt": "CAS CL-5200P pole label printing scale",
					"caption": "Raised display for busy grocery and fresh-food counters.",
					"sort_order": 1,
				},
				{
					"label": "Bench model also available",
					"image": photos["bench"],
					"image_alt": "CAS CL-5200B bench label printing scale",
					"caption": "The CL-5200B keeps the same printer in a compact bench body.",
					"sort_order": 2,
				},
			]
		doc.set("visual_story_items", story)
		doc.flags.ignore_permissions = True
		doc.save()


def shorten_product_slugs():
	photos = install_cl5200_photos()
	updated = []
	for old, new in PRODUCT_SLUG_ALIASES.items():
		if old == "people-projects":
			continue
		name = frappe.db.get_value("Website Product", {"slug": old}, "name")
		if not name:
			# already shortened
			name = frappe.db.get_value("Website Product", {"slug": new}, "name")
			if not name:
				continue
		doc = frappe.get_doc("Website Product", name)
		doc.slug = new
		if doc.final_cta_primary_href:
			doc.final_cta_primary_href = doc.final_cta_primary_href.replace(f"/products/{old}", f"/products/{new}")
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(f"{old} → {new}")

	apply_cl5200_photos(photos)
	_rewrite_related_hrefs()
	from printechs_digital.setup.link_cas_related_products import link_cas_related_products

	link_cas_related_products()

	for doctype, field in (
		("Website Industry", "related_product_slugs"),
		("Website Solution", "related_product_slugs"),
	):
		for name in frappe.get_all(doctype, pluck="name"):
			doc = frappe.get_doc(doctype, name)
			value = getattr(doc, field, None)
			rewritten = _rewrite_text(value)
			if rewritten != value:
				setattr(doc, field, rewritten)
				doc.flags.ignore_permissions = True
				doc.save()

	fix_cl5200_page_images()
	frappe.db.commit()
	print("Shortened slugs:", updated)
	return updated


def fix_cl5200_page_images():
	"""Replace leftover marketing graphics on CL-5200 content sections and stories."""
	bench = site_file("cas-cl-5200b.jpg")
	pole = site_file("cas-cl-5200p.jpg")
	cartridge = site_file("cas-cl-5200-cartridge.jpg")
	replacements = {
		"RET.SYS.CAS.1246": {
			"Bench format when space is tight": (bench, "CAS CL-5200B bench scale"),
			"CL-Works Pro and flexible networking": (cartridge, "CAS CL-5200 label cartridge"),
		},
		"RET.SYS.CAS.1247": {
			"A proven CL-series workhorse": (pole, "CAS CL-5200P label printing scale"),
			"Pole or bench to suit your counter": (bench, "CAS CL-5200B bench scale"),
		},
	}
	for name, mapping in replacements.items():
		if not frappe.db.exists("Website Product", name):
			continue
		doc = frappe.get_doc("Website Product", name)
		for row in doc.content_sections or []:
			if row.heading in mapping:
				row.image, row.image_alt = mapping[row.heading]
		for row in doc.visual_story_items or []:
			if "pole-type" in (row.label or "").lower() or (row.image or "").endswith("CL5200.jpg"):
				row.image = pole
				row.image_alt = "CAS CL-5200P pole label printing scale"
			if (row.image or "").endswith("CAS-CL5200B.png") or (row.image or "").endswith("CAS-CL5200B.jpg"):
				row.image = bench
				row.image_alt = "CAS CL-5200B bench label printing scale"
		doc.flags.ignore_permissions = True
		doc.save()
	frappe.db.commit()
	return ["RET.SYS.CAS.1246", "RET.SYS.CAS.1247"]
