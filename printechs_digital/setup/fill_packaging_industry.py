# Copyright (c) 2026, Printechs and contributors
"""Fill the Packaging industry page with unique official photos and films.

Hero stays /files/industry-packaging.jpg. Section images are Hitachi Industrial
packaging print samples and vision hardware that are not used on product pages.
YouTube IDs are official REA JET / Hitachi films not assigned to any product.
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

# Official films not used on any Website Product page.
VIDEO_HR_FILM = "https://youtu.be/PL5O8y1vgTg"  # REA JET HR wet-on-wet
VIDEO_LATE_STAGE = "https://youtu.be/pUdlBKMGexg"  # REA late-stage customization
VIDEO_GS1 = "https://youtu.be/q6gXVJZsRkI"  # REA 2D codes in FMCG
VIDEO_VISION = "https://youtu.be/bbFoShNPK50"  # Hitachi vision on packaging codes

OFFICIAL_IMAGES = {
	"packaging-primary-code.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Packaging_Print-Sample-1.webp"
	),
	"packaging-film-carton.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Packaging_Print-Sample-2.webp"
	),
	"packaging-case-code.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/Packaging_Print-Sample-3.webp"
	),
	"packaging-vision-inspect.jpg": (
		"https://hitachi-industrial.eu/wp-content/uploads/2025/05/VISION-SYSTEM_COMPLETE-2-1.webp"
	),
}

OVERVIEW = """Printechs specifies and installs coding, marking, labelling and inspection for packaging lines in Saudi Arabia — primary packs, cartons, cases and shippers.

Hitachi continuous inkjet, REA JET high-resolution and large-character systems, Anser TIJ, Zebra industrial printers and REA VERIFIER work as one line: lot and expiry on the pack, GS1 on the case, and a grade on the code before it leaves the plant.

We survey substrate, speed and code, then install in Riyadh, Jeddah and Dammam with encoder, photocell and message setup. Consumables and spare parts are quoted with the machine — they are not mixed onto these pages."""


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


def fill_packaging_industry():
	name = frappe.db.get_value("Website Industry", {"slug": "packaging"}, "name")
	if not name:
		frappe.throw("Website Industry packaging is missing")

	m = media()
	doc = frappe.get_doc("Website Industry", name)
	doc.published = 1
	doc.show_on_home = 1
	doc.industry_name = "Packaging"
	doc.summary = (
		"Coding, marking, labelling and inspection for primary packs, cartons, "
		"cases and shippers — specified and supported in Saudi Arabia."
	)
	doc.overview = OVERVIEW
	doc.image = copy_public_image("industries/industry-packaging.jpg")
	doc.image_alt = "Automated packaging line with cartons and pouches on a conveyor"
	doc.related_product_slugs = "\n".join(
		[
			"hitachi-ux-d161",
			"hitachi-ux2-d160",
			"rea-jet-coding-systems",
			"rea-jet-hr-2",
			"rea-jet-dod-2",
			"rea-jet-gk-2",
			"rea-jet-code-verification",
			"anser-a1",
			"zebra-zt421",
		]
	)
	doc.related_solution_slugs = "coding-marking\ntraceability"
	doc.related_software_slugs = "warehouse-management-system"
	doc.meta_title = "Packaging Solutions | Printechs"
	doc.meta_description = (
		"Packaging line coding, marking, labelling and code inspection from Printechs "
		"in Saudi Arabia — Hitachi, REA JET, Anser and Zebra."
	)
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Primary pack codes that stay readable",
				"body": (
					"Lot, expiry and batch on bottles, pouches, cans and film — at line speed, "
					"without stopping the packer.\n\n"
					"Hitachi UX / UX2 continuous inkjet and REA JET HR cartridge systems cover "
					"absorbent and non-absorbent packs. Printechs matches ink, throw and "
					"photocell to the film or bottle so the code is still there at the DC."
				),
				"image": m["packaging-primary-code.jpg"],
				"image_alt": "Official Hitachi print sample on primary packaging",
				"video_url": VIDEO_HR_FILM,
				"link_label": "Hitachi UX-D161W",
				"link_href": "/products/hitachi-ux-d161",
				"image_side": "Left",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Late-stage marks on cartons and sleeves",
				"body": (
					"High-resolution text, logos and GS1 barcodes on folding cartons, sleeves "
					"and film — including late-stage customization after the brand artwork is printed.\n\n"
					"REA JET HR 2.0 and Anser A1 sit on the carton or flow-wrap. We install the "
					"heads, encoder and TITAN or Anser messages so changeovers stay on the HMI, "
					"not on a label stock change."
				),
				"image": m["packaging-film-carton.jpg"],
				"image_alt": "Official Hitachi coding sample on carton-style packaging",
				"video_url": VIDEO_LATE_STAGE,
				"link_label": "REA JET HR 2.0",
				"link_href": "/products/rea-jet-hr-2",
				"image_side": "Right",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Cases, pallets and shipper labels",
				"body": (
					"Secondary packaging needs a code the warehouse can scan: SSCC, product "
					"text and 2D on the case, plus a 4-inch shipper when the line feeds a DC.\n\n"
					"REA JET DOD 2.0 and GK 2.0 mark cases and pallets in large character. "
					"Zebra ZT421 prints the label when the pack-off needs thermal transfer "
					"instead of direct print."
				),
				"image": m["packaging-case-code.jpg"],
				"image_alt": "Official Hitachi coding sample for secondary packaging",
				"video_url": VIDEO_GS1,
				"link_label": "REA JET DOD 2.0",
				"link_href": "/products/rea-jet-dod-2",
				"image_side": "Left",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Inspect the code before it ships",
				"body": (
					"A mark that the camera cannot grade is a recall waiting to happen. "
					"Printechs adds inspection on the same line as the printer.\n\n"
					"REA VERIFIER grades 1D and 2D to ISO/IEC. Hitachi vision isolates "
					"dot-matrix CIJ characters on primary packs. Both stay unique to this "
					"page — the product films stay on their own SKUs."
				),
				"image": m["packaging-vision-inspect.jpg"],
				"image_alt": "Official Hitachi vision system for inkjet code inspection",
				"video_url": VIDEO_VISION,
				"link_label": "REA VERIFIER",
				"link_href": "/products/rea-jet-code-verification",
				"image_side": "Right",
				"sort_order": 4,
			},
		],
	)
	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return {"status": "updated", "slug": "packaging", "sections": len(doc.content_sections)}
