# Copyright (c) 2026, Printechs and contributors
"""Shared helpers for Avery Berkel Website Product fills."""

from pathlib import Path
from shutil import copy2
from urllib.request import Request, urlopen

from PIL import Image, ImageDraw

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
TMP_DIR = Path("/tmp/avery-berkel")
ASSETS_DIR = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
BRAND = "AVERY BERKEL"

# Unique 4:3 application scenes (not the shared industry-retail / food / bakery stock).
APP_SCENE_KEYS = (
	"butchery",
	"deli",
	"bakery",
	"supermarket-fresh",
	"seafood",
	"grocery",
	"cheese",
	"wet-counter",
	"produce",
	"prepack",
	"pos",
	"nutrition-label",
	"service-island",
	"speciality",
	"bakery-pack",
	"fish-market",
	"compact-counter",
	"premium-deli",
	"zero-waste",
	"bakery-pos",
	"supermarket-aisle",
	"meat-prep",
	"ksa-fresh",
	"label-print",
	"hanging-fish",
	"fruit-display",
	"packed-meat",
	"self-scan",
	"olive-bar",
	"bakery-shelf",
)

# slug → (scene_key, title, description, image_alt)
APPLICATIONS_BY_SLUG: dict[str, list[tuple[str, str, str, str]]] = {
	"avery-berkel": [
		("supermarket-fresh", "Supermarket fresh food", "Meat, deli, cheese and produce counters with networked prices.", "Supermarket fresh-food department"),
		("butchery", "Butchery and deli", "Service weighing with labels customers can scan at checkout.", "Butchery counter"),
		("bakery", "Bakery and pre-pack", "XTs600 / XTi600 terminals when weight is fixed or from another platform.", "Bakery counter"),
	],
	"avery-berkel-xs-series": [
		("meat-prep", "Butchery", "Fast PLU keys on a compact or tower scale.", "Butcher preparing meat"),
		("deli", "Grocery and deli", "Price computing and barcode labels for checkout.", "Delicatessen counter"),
		("seafood", "Seafood", "Specify hanging Xs500 instead of a bench pan.", "Seafood on ice"),
	],
	"avery-berkel-xts-series": [
		("service-island", "Supermarket counters", "Colour PLUs and customer-facing promotions.", "Supermarket service island"),
		("hanging-fish", "Seafood", "XTs500 hanging configuration.", "Hanging fish display"),
		("bakery-pack", "Pre-pack / EPOS", "XTs600 when weight is not on this device.", "Bakery packing table"),
	],
	"avery-berkel-xti-series": [
		("premium-deli", "Premium deli / butcher", "XTi400 or XTi420 for eye-level service and dual media.", "Premium deli counter"),
		("produce", "Produce self-service", "XTi300 in fruit and vegetable aisles.", "Produce department"),
		("bakery-pos", "Bakery terminal", "XTi600 when items are fixed-price or pre-weighed.", "Bakery point of sale"),
	],
	"avery-berkel-xs100": [
		("compact-counter", "Butcher shops", "Fast keys and labels on a short counter.", "Compact butcher counter"),
		("olive-bar", "Delicatessens", "Cheese and prepared-food PLUs with barcode labels.", "Olive and deli bar"),
		("bakery", "Bakeries", "Service weighing where a monobloc fits the glass counter.", "Bakery display"),
	],
	"avery-berkel-xs200": [
		("supermarket-aisle", "Supermarkets", "Customer-readable totals on a service island.", "Supermarket aisle"),
		("butchery", "Butcheries", "Keys stay low; the shopper sees the price.", "Butchery counter"),
		("grocery", "Grocery service", "Networked PLUs with a visible customer display.", "Grocery service counter"),
	],
	"avery-berkel-xs400": [
		("premium-deli", "Premium butcheries", "Clear workspace around the platter.", "Premium open counter"),
		("cheese", "Cheese and deli", "Eye-level totals on a tight island.", "Artisan cheese counter"),
		("ksa-fresh", "Supermarket service", "Reduced footprint versus a deep monobloc.", "Modern fresh-food hall"),
	],
	"avery-berkel-xs500": [
		("fish-market", "Fish markets", "Hang the pan over ice or a well.", "Fish market stall"),
		("wet-counter", "Supermarket seafood", "Same Xs labels as the meat counter, different form.", "Wet-food supermarket well"),
		("hanging-fish", "Wet food sections", "Where a bench platter would stay wet all day.", "Hanging seafood display"),
	],
	"avery-berkel-xts100": [
		("compact-counter", "Compact butcher counters", "Touch PLUs without a tower.", "Compact glass counter"),
		("supermarket-fresh", "Supermarkets", "Colour products on a short run.", "Fresh-food supermarket"),
		("speciality", "Delis", "Promotions on the 7-inch customer display.", "Specialty food shop"),
	],
	"avery-berkel-xts200": [
		("service-island", "Supermarket islands", "Shoppers see the total and the offer.", "Service island"),
		("pos", "Service counters", "Promotions without a second screen SKU.", "Retail service checkout"),
		("olive-bar", "Delis", "Colour PLUs plus a raised customer face.", "Deli olive bar"),
	],
	"avery-berkel-xts400": [
		("ksa-fresh", "Premium food counters", "Presentation and a clear work area.", "Luxury fresh-food hall"),
		("supermarket-aisle", "Supermarkets", "Tower XTs without a second printer.", "Supermarket aisle"),
		("cheese", "Cheese / deli", "Eye-level colour PLUs.", "Cheese counter"),
	],
	"avery-berkel-xts420": [
		("pos", "Combined weigh / POS", "Label the pack and print the ticket.", "Weigh and receipt counter"),
		("packed-meat", "High-volume counters", "No media change mid-rush.", "Packed meat trays"),
		("meat-prep", "Fresh food", "Two label sizes permanently loaded.", "Meat preparation"),
	],
	"avery-berkel-xts500": [
		("seafood", "Seafood counters", "The featured hanging touchscale.", "Seafood on ice"),
		("hanging-fish", "Wet supermarket sections", "Protect the electronics above the well.", "Hanging fish"),
		("speciality", "Specialist fish shops", "Colour PLUs for mixed catch.", "Specialty food shop"),
	],
	"avery-berkel-xts600": [
		("bakery", "Bakeries", "Fixed-price packs and counter labels.", "Bakery counter"),
		("bakery-pack", "Pre-pack rooms", "Print without a weigh platter on this device.", "Bakery packing"),
		("bakery-shelf", "EPOS", "Receipt workstation on the XT network.", "Packaged bakery shelf"),
	],
	"avery-berkel-xts700": [
		("nutrition-label", "Dual-label packs", "Brand/price plus ingredients.", "Nutrition and price labels"),
		("prepack", "Pre-pack rooms", "Two sizes loaded all shift.", "Food pre-pack room"),
		("label-print", "Allergen labels", "Larger format without stopping the host scale.", "Thermal label printing"),
	],
	"avery-berkel-xti100": [
		("compact-counter", "Compact premium counters", "XTi screen without a column.", "Compact premium counter"),
		("ksa-fresh", "Supermarkets", "Colour PLUs on a short run.", "Modern supermarket hall"),
		("speciality", "Speciality food", "Large touch, small height.", "Specialty food shop"),
	],
	"avery-berkel-xti200": [
		("supermarket-fresh", "Supermarket counters", "Featured everyday XTi.", "Fresh-food supermarket"),
		("service-island", "Speciality food", "Promotions on the raised display.", "Service island"),
		("prepack", "Pre-pack", "Same station for service and batch labels.", "Pre-pack room"),
	],
	"avery-berkel-xti300": [
		("produce", "Fruit and vegetables", "The defining XTi300 department.", "Produce department"),
		("zero-waste", "Zero-waste", "Customers buy only what they need.", "Zero-waste grocery"),
		("self-scan", "Self-scan stores", "Labels ready for SCO or handheld checkout.", "Self-scan checkout"),
	],
	"avery-berkel-xti400": [
		("premium-deli", "Supermarket deli", "Featured attended tower.", "Premium deli"),
		("meat-prep", "Butchery", "Eye contact, clear platter.", "Meat preparation"),
		("cheese", "Cheese counters", "Premium presentation.", "Cheese counter"),
	],
	"avery-berkel-xti420": [
		("pos", "Weigh + POS counters", "The demonstration workstation.", "Weigh and POS counter"),
		("packed-meat", "Supermarkets", "Label the pack, print the ticket.", "Packed meat trays"),
		("butchery", "Butcheries", "Two media, one conversation.", "Butchery counter"),
	],
	"avery-berkel-xti600": [
		("bakery-pos", "Bakeries", "Featured printing/EPOS application.", "Bakery checkout"),
		("bakery-shelf", "Pre-pack", "Labels without a platter on this device.", "Bakery packaged goods"),
		("bakery-pack", "Food EPOS", "Receipts on the XTi network.", "Bakery packing table"),
	],
}


def site_file(filename: str) -> str:
	return f"/files/{filename}"


_PDF_HEADERS = {
	"User-Agent": (
		"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
		"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
	)
}

# Official Avery-branded family PDFs (brochure + datasheet) for customer download.
BROCHURE_SOURCES = {
	"xs_brochure": {
		"filename": "avery-berkel-xs-brochure.pdf",
		"label": "Avery Berkel Xs Series Brochure",
		"download_type": "Brochure",
		"tmp": "xs-brochure.pdf",
		"urls": [
			"https://southcoastsystems.co.uk/wp-content/uploads/2022/11/XS_ENGLISH.pdf",
			"https://allprep.wdyuk.co.uk/media/wysiwyg/1749135369_XS%20Product%20Brochure.pdf",
		],
	},
	"xt_brochure": {
		"filename": "avery-berkel-xt-brochure.pdf",
		"label": "Avery Berkel XT Series Brochure",
		"download_type": "Brochure",
		"tmp": "xt-brochure.pdf",
		"urls": [
			"https://rmspos.co.uk/wp-content/uploads/2025/05/Avery_Berkel_XT_Series_Datasheet_RMS.pdf",
			"https://rmspos.co.uk/wp-content/uploads/2026/05/Avery_XT_Series_Datasheet_RMS.pdf",
		],
	},
	"xt_datasheet": {
		"filename": "avery-berkel-xt-datasheet.pdf",
		"label": "Avery Berkel XT Technical Specification",
		"download_type": "Datasheet",
		"tmp": "xt-datasheet.pdf",
		"urls": [
			"https://www.ourweigh.co.uk/user/Avery%20Berkel%20XT%20Series%20Technical%20Specifications.pdf",
			"https://allprep.wdyuk.co.uk/media/wysiwyg/1747143416_XT%20Technical%20Specs.pdf",
			"https://www.averyberkel.com/api/files/file/ABR35-000556-AH-XT-Tech-Spec-English.pdf",
		],
	},
}


def _ensure_pdf(key: str) -> str:
	meta = BROCHURE_SOURCES[key]
	dest = SITE_FILES / meta["filename"]
	if dest.exists() and dest.stat().st_size > 20000:
		return site_file(meta["filename"])
	tmp = TMP_DIR / meta["tmp"]
	if tmp.exists() and tmp.stat().st_size > 20000:
		copy2(tmp, dest)
		return site_file(meta["filename"])
	for url in meta["urls"]:
		try:
			request = Request(url, headers=_PDF_HEADERS)
			with urlopen(request, timeout=45) as response, dest.open("wb") as handle:
				handle.write(response.read())
			if dest.exists() and dest.stat().st_size > 20000:
				return site_file(meta["filename"])
		except Exception:
			continue
	frappe.throw(f"Could not install Avery Berkel PDF: {meta['filename']}")


def install_brochures() -> dict[str, str]:
	return {key: _ensure_pdf(key) for key in BROCHURE_SOURCES}


def _download_row(key: str, files: dict[str, str], sort_order: int) -> dict:
	meta = BROCHURE_SOURCES[key]
	return {
		"label": meta["label"],
		"file": files[key],
		"download_type": meta["download_type"],
		"sort_order": sort_order,
	}


def brochure_keys_for(slug: str) -> list[str]:
	if slug == "avery-berkel":
		return ["xs_brochure", "xt_brochure", "xt_datasheet"]
	if slug.startswith("avery-berkel-xs"):
		return ["xs_brochure"]
	return ["xt_brochure", "xt_datasheet"]


def apply_brochures(doc, slug: str, files: dict[str, str] | None = None):
	files = files or install_brochures()
	keys = brochure_keys_for(slug)
	doc.set("downloads", [_download_row(key, files, i) for i, key in enumerate(keys, start=1)])
	primary = keys[0]
	doc.primary_download_label = BROCHURE_SOURCES[primary]["label"]
	doc.primary_download_file = files[primary]


def update_avery_berkel_brochures():
	"""Attach family brochures so customers can download them from every page."""
	files = install_brochures()
	updated = []
	for name in frappe.get_all("Website Product", filters={"slug": ["like", "avery-berkel%"]}, pluck="name"):
		doc = frappe.get_doc("Website Product", name)
		apply_brochures(doc, doc.slug, files)
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(doc.slug)
	frappe.db.commit()
	print(f"Attached brochures on {len(updated)} Avery Berkel pages")
	return updated


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


def save_jpeg(src: Path, dest_name: str, max_edge: int = 1800) -> str:
	dest = SITE_FILES / dest_name
	im = Image.open(src).convert("RGB")
	w, h = im.size
	if max(w, h) > max_edge:
		scale = max_edge / max(w, h)
		im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
	im.save(dest, "JPEG", quality=90, optimize=True)
	return site_file(dest_name)


def wipe_ccm_logos(src: Path, dest_name: str) -> str:
	"""Remove CCM / XT watermarks from the top-left of distributor photos."""
	im = Image.open(src).convert("RGB")
	w, h = im.size
	draw = ImageDraw.Draw(im)
	draw.rectangle((0, 0, int(w * 0.44), int(h * 0.34)), fill=(248, 248, 248))
	dest = SITE_FILES / dest_name
	im.save(dest, "JPEG", quality=92, optimize=True)
	return dest_name


def _scene_media_key(scene_key: str) -> str:
	return f"app_{scene_key.replace('-', '_')}"


def save_app_scene(src: Path, dest_name: str, size: tuple[int, int] = (1600, 1200)) -> str:
	"""Cover-crop a lifestyle photo to 4:3 for Application cards."""
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


def install_application_scenes() -> dict[str, str]:
	"""Copy unique application scenes into /files. Sources may live in Cursor assets or site files."""
	media: dict[str, str] = {}
	missing: list[str] = []
	for key in APP_SCENE_KEYS:
		filename = f"ab-app-{key}.jpg"
		candidates = [ASSETS_DIR / filename, SITE_FILES / filename]
		src = next((path for path in candidates if path.exists()), None)
		if not src:
			missing.append(filename)
			continue
		media[_scene_media_key(key)] = save_app_scene(src, filename)
	if missing:
		frappe.throw(f"Missing Avery Berkel application scenes: {', '.join(missing)}")
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
			"image": media[_scene_media_key(key)],
			"image_alt": alt,
			"industry_link": "retail",
			"sort_order": i,
		})
	return out


def crop_to(src: Path, dest_name: str, box: tuple[float, float, float, float]) -> str:
	im = Image.open(src).convert("RGB")
	w, h = im.size
	l, t, r, b = box
	cropped = im.crop((int(w * l), int(h * t), int(w * r), int(h * b)))
	dest = SITE_FILES / dest_name
	cropped.save(dest, "JPEG", quality=92, optimize=True)
	return dest_name


def prepare_media() -> dict[str, str]:
	"""Build unique HQ files. Industry stock may be shared; product photos are unique."""
	erp = {
		"xs100": SITE_FILES / "XS100-01-scaled.webp",
		"xs200": SITE_FILES / "XS200-01-scaled.webp",
		"xs400": SITE_FILES / "XS400-01-scaled.webp",
		"xs500": SITE_FILES / "XS500-01.webp",
		"xts100": SITE_FILES / "XTs100_01-scaled.webp",
		"xts200": SITE_FILES / "XTs200-7-7-01-scaled.webp",
		"xts400": SITE_FILES / "XTs400-7-10_01-scaled.webp",
		"xts500": SITE_FILES / "XTs500-01-1-scaled.webp",
		"xti100": SITE_FILES / "XTi100-01-1-scaled.webp",
		"xti200": SITE_FILES / "XTi200-01.webp",
		"xti300": SITE_FILES / "XTx300-01-scaled.webp",
		"xti400": SITE_FILES / "XTi400-01-scaled.webp",
		"xti600": SITE_FILES / "XTi600-01-scaled.webp",
	}
	for key, path in erp.items():
		if not path.exists():
			frappe.throw(f"Missing Avery Berkel source image: {path}")

	# Official brochure / datasheet crops (unique filenames)
	save_jpeg(TMP_DIR / "xs-brochure-p2-0.png", "ab-hub-lifestyle.jpg")
	save_jpeg(TMP_DIR / "xs-brochure-p3-0.png", "ab-xs-series-scene.jpg")
	save_jpeg(TMP_DIR / "xs-brochure-p3-1.png", "ab-xs200-scene.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p3-0.png", "ab-xts-series-pair.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p7-0.png", "ab-xti420-hero.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p8-0.png", "ab-xti-series-counter.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p4-1.png", "ab-xts700-cassette.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p4-2.png", "ab-xts700-label.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p5-0.png", "ab-xti200-advert.jpg")
	save_jpeg(TMP_DIR / "xt-datasheet-p7-2.png", "ab-xts500-angle.jpg")

	wipe_ccm_logos(TMP_DIR / "dist/xts420-full.jpg", "ab-xts420-src.jpg")
	wipe_ccm_logos(TMP_DIR / "dist/xts600-full.jpg", "ab-xts600-src.jpg")

	cards = {
		"xs100": make_card(erp["xs100"], "ab-xs100-card.jpg"),
		"xs200": make_card(erp["xs200"], "ab-xs200-card.jpg"),
		"xs400": make_card(erp["xs400"], "ab-xs400-card.jpg"),
		"xs500": make_card(erp["xs500"], "ab-xs500-card.jpg"),
		"xts100": make_card(erp["xts100"], "ab-xts100-card.jpg"),
		"xts200": make_card(erp["xts200"], "ab-xts200-card.jpg"),
		"xts400": make_card(erp["xts400"], "ab-xts400-card.jpg"),
		"xts420": make_card(SITE_FILES / "ab-xts420-src.jpg", "ab-xts420-card.jpg"),
		"xts500": make_card(erp["xts500"], "ab-xts500-card.jpg"),
		"xts600": make_card(SITE_FILES / "ab-xts600-src.jpg", "ab-xts600-card.jpg"),
		"xts700": make_card(SITE_FILES / "ab-xts700-cassette.jpg", "ab-xts700-card.jpg"),
		"xti100": make_card(erp["xti100"], "ab-xti100-card.jpg"),
		"xti200": make_card(erp["xti200"], "ab-xti200-card.jpg"),
		"xti300": make_card(erp["xti300"], "ab-xti300-card.jpg"),
		"xti400": make_card(erp["xti400"], "ab-xti400-card.jpg"),
		"xti420": make_card(SITE_FILES / "ab-xti420-hero.jpg", "ab-xti420-card.jpg"),
		"xti600": make_card(erp["xti600"], "ab-xti600-card.jpg"),
		"hub": make_card(SITE_FILES / "ab-hub-lifestyle.jpg", "ab-hub-card.jpg"),
		"xs-series": make_card(SITE_FILES / "ab-xs-series-scene.jpg", "ab-xs-series-card.jpg"),
		"xts-series": make_card(SITE_FILES / "ab-xts-series-pair.jpg", "ab-xts-series-card.jpg"),
		"xti-series": make_card(SITE_FILES / "ab-xti-series-counter.jpg", "ab-xti-series-card.jpg"),
	}

	return {
		**cards,
		**install_application_scenes(),
		"hub_scene": site_file("ab-hub-lifestyle.jpg"),
		"xs_series_scene": site_file("ab-xs-series-scene.jpg"),
		"xs200_scene": site_file("ab-xs200-scene.jpg"),
		"xts_series_pair": site_file("ab-xts-series-pair.jpg"),
		"xti420_hero": site_file("ab-xti420-hero.jpg"),
		"xti_series_counter": site_file("ab-xti-series-counter.jpg"),
		"xts700_label": site_file("ab-xts700-label.jpg"),
		"xti200_advert": site_file("ab-xti200-advert.jpg"),
		"xts500_angle": site_file("ab-xts500-angle.jpg"),
		"retail": site_file("industry-retail.jpg"),
		"food": site_file("industry-food-beverage.jpg"),
		"bakery": site_file("industry-bakery.jpg"),
	}


def update_avery_berkel_application_images():
	"""Replace Application-section images only — does not rebuild product copy."""
	media = install_application_scenes()
	updated = []
	for slug in APPLICATIONS_BY_SLUG:
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		doc.set("applications", scene_apps(media, slug))
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(slug)
	frappe.db.commit()
	print(f"Updated applications on {len(updated)} Avery Berkel pages")
	return updated


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


def update_avery_berkel_hero_ctas():
	"""Hardware pages: Request a Quote only. Book a Demo is for software."""
	updated = []
	for name in frappe.get_all("Website Product", filters={"slug": ["like", "avery-berkel%"]}, pluck="name"):
		doc = frappe.get_doc("Website Product", name)
		doc.show_demo_cta = 0
		doc.show_quote_in_hero = 1
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(doc.slug)
	frappe.db.commit()
	print(f"Quote-only hero on {len(updated)} Avery Berkel pages")
	return updated


def update_avery_berkel_full_specs():
	"""Replace Full Specifications with model-accurate technical tables."""
	from printechs_digital.setup.avery_berkel_specs import SPECS_BY_SLUG, specs_for

	updated = []
	for slug in SPECS_BY_SLUG:
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		set_specs(doc, specs_for(slug))
		doc.collapsible_full_specs = 0
		if slug == "avery-berkel-xts500":
			for row in doc.benefits:
				if row.title == "ValuMax":
					row.title = "Hanging seafood head"
					row.icon = "inventory"
					row.description = "Suspended pan and elevated 7-inch touch — ValuMax is not specified on XTs500."
			for row in doc.icon_specifications:
				if "ValuMax" in (row.title or "") or "ValuMax" in (row.description or ""):
					row.title = "Print"
					row.icon = "print"
					row.description = "Cassette thermal"
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(slug)
	frappe.db.commit()
	print(f"Updated full specifications on {len(updated)} Avery Berkel pages")
	return updated


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
	doc.category = "Retail Systems"
	doc.subcategory = subcategory
	doc.short_description = f"{display_name} retail weighing scale."
	doc.long_description = f"<p>{display_name} retail weighing scale.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, item, subcategory, category_label, on_list=True, featured=0):
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	if item and frappe.db.exists("Item", item) and not doc.item:
		other = frappe.db.get_value("Website Product", {"item": item}, "name")
		if not other or other == doc.name:
			doc.item = item
	if frappe.db.exists("Brand", BRAND):
		doc.brand = BRAND
	doc.brand_name = "Avery Berkel"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.page_mode = "Full"
	doc.category = "Retail Systems"
	doc.subcategory = subcategory
	doc.category_label = category_label
	doc.collapsible_full_specs = 0
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 0
	doc.featured = featured
	doc.show_on_products_list = 1 if on_list else 0
	doc.show_on_software_list = 0
	doc.card_brand_label = "Avery Berkel"
	doc.show_item_code_on_website = 1 if doc.item else 0
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to Our Team"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1
	doc.video_url = ""


def support_items(install, device, maintenance, training):
	return [
		{"icon": "install", "title": "Deployment", "description": install, "sort_order": 1},
		{"icon": "device", "title": "Labels & media", "description": device, "sort_order": 2},
		{"icon": "maintenance", "title": "Service", "description": maintenance, "sort_order": 3},
		{"icon": "training", "title": "Training", "description": training, "sort_order": 4},
	]


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
