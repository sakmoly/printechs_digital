# Copyright (c) 2026, Printechs and contributors
"""Fill the Dairy industry page with official Hitachi dairy print samples.

No product names, product links, or videos. Samples are unique to this page —
not the UX2 Hoover dairy shot or the margarine sample used on product pages.
"""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

from printechs_digital.setup.copy_website_asset import copy_public_image

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
PUBLIC_INDUSTRIES = Path(
	"/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries"
)

OFFICIAL_IMAGES = {
	"dairy-yoghurt-cup.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Dairy_Print-Sample-1.webp"
	),
	"dairy-uht-carton.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Dairy_Print-Sample-2.webp"
	),
	"dairy-spread-tub.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Dairy_Print-Sample-3.webp"
	),
	"dairy-fresh-film.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Dairy_Print-Sample-4.webp"
	),
	"dairy-cheese-sachet.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Dairy_print-Sample-5-.webp"
	),
}

OVERVIEW = """Dairy lines need a lot, expiry and time code that stays readable after cold fill, condensation and wipe-down — on cups, cartons, tubs, film and sachets.

Printechs surveys the pack and the hall, then specifies coding for dairy producers in Riyadh, Jeddah and Dammam. The same duty applies whichever industrial inkjet or thermal system sits on the line.

This page is the dairy application, not a product list. We match ink, throw and photocell to the pack when you enquire."""


def download_wide(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"})
		with urlopen(request, timeout=40) as response:
			data = response.read()
		im = Image.open(BytesIO(data)).convert("RGB")
		target_ratio = 16 / 10
		width, height = im.size
		if width / height > target_ratio:
			new_w = int(height * target_ratio)
			left = (width - new_w) // 2
			im = im.crop((left, 0, left + new_w, height))
		else:
			new_h = int(width / target_ratio)
			top = (height - new_h) // 2
			im = im.crop((0, top, width, top + new_h))
		im = im.resize((1600, 1000), Image.Resampling.LANCZOS)
		im.save(target, "JPEG", quality=90, optimize=True)
		public = PUBLIC_INDUSTRIES / filename
		public.parent.mkdir(parents=True, exist_ok=True)
		im.save(public, "JPEG", quality=90, optimize=True)
	return f"/files/{filename}"


def media() -> dict[str, str]:
	return {name: download_wide(name, url) for name, url in OFFICIAL_IMAGES.items()}


def fill_dairy_industry():
	name = frappe.db.get_value("Website Industry", {"slug": "dairy"}, "name")
	if not name:
		frappe.throw("Website Industry dairy is missing")

	m = media()
	doc = frappe.get_doc("Website Industry", name)
	doc.published = 1
	doc.show_on_home = 1
	doc.industry_name = "Dairy"
	doc.summary = (
		"Lot, expiry and time codes on yoghurt cups, UHT cartons, spread tubs, "
		"fresh-cheese film and sachets — for dairy halls in Saudi Arabia."
	)
	doc.overview = OVERVIEW
	doc.image = copy_public_image("industries/industry-dairy.jpg")
	doc.image_alt = "Dairy production line with coded milk bottles on a conveyor"
	doc.related_product_slugs = ""
	doc.related_software_slugs = ""
	doc.related_solution_slugs = "coding-marking\ntraceability"
	doc.meta_title = "Dairy Industry Solutions | Printechs"
	doc.meta_description = (
		"Dairy coding samples for cups, cartons, tubs, film and sachets. "
		"Printechs specifies readable lot and expiry marks for dairy lines in Saudi Arabia."
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Yoghurt and cultured cups",
				"body": (
					"Lot and time on the cup wall, next to the nutrition panel, after fill and seal.\n\n"
					"White PP and condensation in a wet hall need an ink that keys to the pot "
					"and stays readable in the cold chain — not a smear after wipe-down."
				),
				"image": m["dairy-yoghurt-cup.jpg"],
				"image_alt": "Lot and time code on a yoghurt cup",
				"image_side": "Left",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "UHT and fresh milk cartons",
				"body": (
					"Best-before and lot on the gable or top panel, at filler speed.\n\n"
					"Carton board takes a sharp code if throw and photocell are set for the "
					"peak. The mark has to survive packing into the crate and the chill store."
				),
				"image": m["dairy-uht-carton.jpg"],
				"image_alt": "Best-before and lot code on a UHT milk carton",
				"image_side": "Right",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Spreads and tub lids",
				"body": (
					"Date and lot on the lid foil or the tub shoulder, after the lid is pressed.\n\n"
					"Gold and printed lids are low-contrast. The code still has to be obvious "
					"on the retail shelf and in the warehouse scan."
				),
				"image": m["dairy-spread-tub.jpg"],
				"image_alt": "Date and lot code on a dairy spread tub lid",
				"image_side": "Left",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Fresh cheese and film packs",
				"body": (
					"Lot and time on flexible film over a chilled pack — often next to a "
					"deli or sandwich line.\n\n"
					"Film stretch and moisture change the print window. We set the head to "
					"the web so the code does not walk off the seal."
				),
				"image": m["dairy-fresh-film.jpg"],
				"image_alt": "Lot and time code on a fresh dairy film pack",
				"image_side": "Right",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Sachets and grated-cheese pouches",
				"body": (
					"Date and lot on a small foil sachet, often on a vertical form-fill-seal.\n\n"
					"The print area is tight and the film is shiny. A compact, high-contrast "
					"code is what the retailer and the kitchen both need to read."
				),
				"image": m["dairy-cheese-sachet.jpg"],
				"image_alt": "Date and lot code on a grated-cheese sachet",
				"image_side": "Left",
				"sort_order": 5,
			},
		],
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": "dairy", "sections": len(doc.content_sections)}
