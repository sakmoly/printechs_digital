# Copyright (c) 2026, Printechs and contributors
"""CAS application image library, brochure tidy-up, and official spec corrections."""

from pathlib import Path
from shutil import copy2

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
ASSETS_DIR = Path(
	"/home/erpnext/.cursor/projects/home-erpnext-frappe-bench-apps-printechs-digital/assets"
)
LIBRARY = SITE_FILES / "library"

CAS_APP_KEYS = (
	"supermarket-fresh",
	"butchery",
	"bakery-deli",
	"seafood",
	"hanging-meat",
	"wet-well",
	"gourmet-deli",
	"cheese",
	"bakery-premium",
	"produce",
	"grocery-aisle",
	"compact-butcher",
	"specialty",
	"deli-bench",
	"bakery-small",
	"prepack",
	"service-island",
	"fish-market",
	"olive-bar",
	"ksa-fresh",
)

CAS_SOCIAL_KEYS = ("butcher", "bakery", "seafood", "produce")

# slug → (scene, title, description, alt, industry)
CAS_APPLICATIONS = {
	"cas-cl-5500d": [
		("supermarket-fresh", "Grocery & supermarkets", "Pole-type labelling for produce, deli and fresh-food islands.", "Supermarket fresh-food hall", "retail"),
		("butchery", "Butcher & fresh meat", "Weight, price and barcode labels at the meat counter.", "Premium butcher counter", "food-beverage"),
		("bakery-deli", "Bakery & deli", "Fast PLU recall and receipt printing on a busy counter.", "Bakery and deli display", "bakery"),
		("seafood", "Seafood & specialty counters", "Dual-range weighing for light fillets and heavier whole fish.", "Seafood on ice", "food-beverage"),
	],
	"cas-cl-5500h": [
		("hanging-meat", "Butcher & meat counters", "Hanging form keeps the platter off a wet or crowded worktop.", "Hanging meat display", "food-beverage"),
		("fish-market", "Seafood departments", "Suspended pan over ice — the right hanging scale for wet counters.", "Fish market hanging scale", "food-beverage"),
		("wet-well", "Wet food sections", "Overhead weighing where a bench platter would stay wet all day.", "Wet supermarket well", "food-beverage"),
		("service-island", "Supermarkets", "Same CL-5500 labelling, hanging over a service island.", "Supermarket service island", "retail"),
	],
	"cas-cn1": [
		("ksa-fresh", "Grocery & supermarkets", "7-inch colour display for networked fresh-food departments.", "Modern supermarket hall", "retail"),
		("gourmet-deli", "Butcher & fresh meat", "Colour PLUs and barcodes on a staffed meat counter.", "Gourmet deli counter", "food-beverage"),
		("bakery-premium", "Deli & bakery", "Vivid product pictures on the 7-inch customer screen.", "Premium bakery", "bakery"),
		("produce", "Seafood & produce counters", "Colour UI for mixed fresh departments on the CAS Network.", "Fresh produce display", "food-beverage"),
	],
	"cas-cl-5200p": [
		("grocery-aisle", "Grocery & supermarkets", "Popular pole CL-5200 for everyday fresh-food labelling.", "Supermarket grocery aisle", "retail"),
		("cheese", "Deli & cheese counters", "72 speed keys and a raised display for staffed deli service.", "Cheese and deli counter", "food-beverage"),
		("bakery-small", "Bakery counters", "Ingredients and nutrition on thermal labels.", "Neighbourhood bakery", "bakery"),
		("specialty", "Specialty retail", "Ethernet master/slave for small multi-scale shops.", "Specialty grocery", "retail"),
	],
	"cas-cl-5200b": [
		("deli-bench", "Grocery & supermarkets", "Low-height bench scale where a pole will not fit the glass.", "Deli service bench", "retail"),
		("compact-butcher", "Butcher shops", "54 speed keys on a compact stainless platter.", "Compact butcher counter", "food-beverage"),
		("olive-bar", "Deli & specialty", "Label packed olives, salads and counter specials from the bench.", "Olive and specialty bar", "food-beverage"),
		("prepack", "Back-room pre-pack", "Batch labels from a bench station in the prep room.", "Food pre-pack room", "packaging"),
	],
}

BROCHURE_MAP = {
	"cas-cl-5200b": ("CL5200-en.pdf", "cas-cl-5200-brochure.pdf", "CL-5200 Brochure"),
	"cas-cl-5200p": ("CL5200-en.pdf", "cas-cl-5200-brochure.pdf", "CL-5200 Brochure"),
	"cas-cl-5500d": ("brochure-cl-5500d.pdf", "cas-cl-5500d-brochure.pdf", "CL-5500D Brochure"),
	"cas-cl-5500h": ("File-1597168228.pdf", "cas-cl-5500h-brochure.pdf", "CL-5500H Brochure"),
	"cas-cn1": ("bXin04WDlsflm1FL8s8FgIe7RS1Ul2o8FufRxuuT.pdf", "cas-cn1-brochure.pdf", "CN1 Brochure"),
}


def site_file(filename: str) -> str:
	return f"/files/{filename}"


def _cover_jpeg(src: Path, dest: Path, size: tuple[int, int]) -> None:
	im = Image.open(src).convert("RGB")
	tw, th = size
	scale = max(tw / im.width, th / im.height)
	nw, nh = max(1, int(im.width * scale)), max(1, int(im.height * scale))
	im = im.resize((nw, nh), Image.Resampling.LANCZOS)
	left, top = (nw - tw) // 2, (nh - th) // 2
	im = im.crop((left, top, left + tw, top + th))
	dest.parent.mkdir(parents=True, exist_ok=True)
	im.save(dest, "JPEG", quality=90, optimize=True)


def install_cas_library() -> dict[str, str]:
	"""Copy generated CAS scenes into /files and /files/library/cas/."""
	app_dir = LIBRARY / "cas" / "applications"
	social_dir = LIBRARY / "cas" / "social"
	brochure_dir = LIBRARY / "cas" / "brochures"
	app_dir.mkdir(parents=True, exist_ok=True)
	social_dir.mkdir(parents=True, exist_ok=True)
	brochure_dir.mkdir(parents=True, exist_ok=True)

	media: dict[str, str] = {}
	missing = []
	for key in CAS_APP_KEYS:
		name = f"cas-app-{key}.jpg"
		src = ASSETS_DIR / name
		if not src.exists():
			src = SITE_FILES / name
		if not src.exists():
			missing.append(name)
			continue
		_cover_jpeg(src, SITE_FILES / name, (1600, 1200))
		copy2(SITE_FILES / name, app_dir / name)
		media[key] = site_file(name)

	for key in CAS_SOCIAL_KEYS:
		name = f"cas-social-{key}.jpg"
		src = ASSETS_DIR / name
		if src.exists():
			_cover_jpeg(src, SITE_FILES / name, (1200, 1200))
			copy2(SITE_FILES / name, social_dir / name)

	for old, new, _label in BROCHURE_MAP.values():
		src = SITE_FILES / old
		if src.exists():
			copy2(src, SITE_FILES / new)
			copy2(src, brochure_dir / new)

	# Keep Avery Berkel scenes in the same library tree for social / reuse.
	ab_dir = LIBRARY / "avery-berkel" / "applications"
	ab_dir.mkdir(parents=True, exist_ok=True)
	for src in SITE_FILES.glob("ab-app-*.jpg"):
		if src.is_file() and "library" not in str(src):
			copy2(src, ab_dir / src.name)

	if missing:
		frappe.throw(f"Missing CAS application images: {', '.join(missing)}")
	return media


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


def specs_for(slug: str):
	from printechs_digital.api.website import _resolve_product_slug

	slug = _resolve_product_slug(slug)
	if slug == "cas-cl-5500d":
		return [
			("Model configuration", [
				("Model", "CAS CL-5500D"),
				("Form factor", "Pole type — label and receipt printing"),
				("Capacity (this page)", "15/30 kg dual range × 5/10 g"),
				("Family capacities", "3/6 kg × 1/2 g and 6/15 kg × 2/5 g also available"),
				("Speed keys", "144 PLU (72 keys × 2 via double-click)"),
				("Display", "Graphic LCD 32 × 202 plus numeric LCD 4/5/6/6"),
			]),
			("Printing", [
				("Printer", "Built-in thermal label and receipt/ticket"),
				("Print speed", "Up to 100 mm/s"),
				("Resolution", "202 dpi"),
				("Label size", "Width 40–60 mm; length 30–200 mm"),
				("Formats", "40 fixed plus up to 20 custom (CL-Works)"),
				("Media", "Quick-change cartridge; continuous ticket supported"),
			]),
			("Data & networking", [
				("PLU capacity", "8,000 PLUs"),
				("Ingredients", "1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP; master/slave; floating clerk"),
				("Software", "CAS CL-Works Pro (also CL-5000 / CL-5000J)"),
			]),
			("Connectivity", [
				("Interfaces", "USB, LAN, RJ11, RS-232C, PS/2"),
				("Wireless", "Optional wireless bridge card"),
				("Power", "AC 100–240 V, 50/60 Hz"),
			]),
			("Physical", [
				("Platter", "Stainless steel, approx. 380 × 270 mm"),
				("Dimensions (W × D × H)", "Approx. 396 × 464 × 612 mm"),
				("Product weight", "Approx. 12.6 kg"),
				("Operating temperature", "−10 °C to 40 °C"),
				("Item code", "RET.SYS.CAS.3035"),
			]),
		]
	if slug == "cas-cl-5500h":
		return [
			("Model configuration", [
				("Model", "CAS CL-5500H"),
				("Form factor", "Hanging / overhead — not a bench platter"),
				("Capacity (this page)", "15/30 kg dual range × 5/10 g"),
				("Speed keys", "144 PLU (72 keys × 2)"),
				("Display", "Dual LCD — operator and customer"),
			]),
			("Printing", [
				("Print technology", "High-speed thermal"),
				("Print speed", "Up to 100 mm/s"),
				("Resolution", "202 dpi"),
				("Label width / length", "40–60 mm / 30–200 mm"),
				("Formats", "50 standard; up to 20 custom"),
				("Barcodes", "UPC-A, EAN-13, Code 128, Code 93, Codabar and more"),
			]),
			("Data & software", [
				("PLU capacity", "4,000 PLUs"),
				("Software", "CAS CL-Works Pro"),
				("Compatibility", "Same menu system as CL-5000 / CL series"),
				("Firmware", "Flash ROM for upgrades"),
			]),
			("Connectivity", [
				("Ethernet", "100 Base-T TCP/IP"),
				("Other", "RS-232C, USB, PS/2 keyboard"),
				("Wireless", "Optional IEEE 802.11 kit"),
			]),
			("Physical", [
				("Dimensions (W × D × H)", "420 × 281 × 706 mm"),
				("Product weight", "14.2 kg"),
				("Power", "AC 100–240 V, 50/60 Hz"),
				("Operating temperature", "−10 °C to 40 °C"),
				("Item code", "RET.SYS.CAS.3036"),
			]),
		]
	if slug == "cas-cn1":
		return [
			("Model configuration", [
				("Model", "CAS CN1"),
				("Series", "CN — CAS Network"),
				("Form factor", "Pole type with 7-inch colour display"),
				("Capacity (this page)", "15/30 kg dual range × 5/10 g"),
				("Family capacities", "6/15 kg × 2/5 g also available"),
				("Keys", "72 PLU keys plus 36 function keys"),
				("Display", "7-inch colour, 800 × 480, 16.7 million colours"),
			]),
			("Printing", [
				("Printer", "Built-in thermal label printer"),
				("Print speed", "Up to 100 mm/s"),
				("Resolution", "202 dpi"),
				("Label size", "Width 40–60 mm; length 30–290 mm"),
				("Barcodes", "UPC, EAN-13, Code 128, GS1 DataBar, QR"),
			]),
			("Data & networking", [
				("PLU capacity", "Up to 10,000 PLUs"),
				("Ingredients", "Up to 1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP; remote control and firmware update"),
				("Compatibility", "Compatible with CAS CL series and CL-Works Pro"),
			]),
			("Connectivity", [
				("Interfaces", "USB, LAN, RJ11, RS-232C"),
				("Wireless", "Optional"),
				("Power", "AC 100–240 V, 50/60 Hz"),
			]),
			("Physical", [
				("Platter", "Stainless steel, approx. 380 × 250 mm"),
				("Body", "Dark grey retail housing"),
				("Item code", "RET.SYS.CAS.3677"),
			]),
		]
	if slug == "cas-cl-5200p":
		return [
			("Model configuration", [
				("Model", "CAS CL-5200P"),
				("Form factor", "Pole type"),
				("Capacity (this page)", "15/30 kg dual range × 5/10 g"),
				("Family capacities", "6/15 kg × 2/5 g also available"),
				("Speed keys", "72 keys (144 PLU via double-click)"),
				("Display", "Combined wide graphic LCD, 208 × 48"),
			]),
			("Printing", [
				("Printer", "Built-in thermal label printer"),
				("Print speed", "Up to 100 mm/s"),
				("Resolution", "202 dpi"),
				("Label size", "Width 40–60 mm; length 30–120 mm"),
				("Formats", "45 fixed plus up to 20 custom"),
				("Media", "Easy-loading label cartridge"),
			]),
			("Data & networking", [
				("PLU capacity", "6,000 PLUs (official CL-5200 specification)"),
				("Ingredients", "1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP; compatible with other CAS CL scales"),
				("Software", "CAS CL-Works Pro (shared with CL-5500 / CL-5000)"),
			]),
			("Connectivity", [
				("Interfaces", "USB, LAN, RJ11, RS-232C"),
				("Power", "AC 100–240 V, 50/60 Hz"),
			]),
			("Physical", [
				("Platter", "Stainless steel, approx. 380 × 250 mm"),
				("Dimensions (W × D × H)", "Approx. 410 × 500 × 536 mm"),
				("Product weight", "Approx. 7.7 kg"),
				("Operating temperature", "−10 °C to 40 °C"),
				("Item code", "RET.SYS.CAS.1247"),
			]),
		]
	if slug == "cas-cl-5200b":
		return [
			("Model configuration", [
				("Model", "CAS CL-5200B"),
				("Form factor", "Bench type — no raised pole"),
				("Capacity (this page)", "15/30 kg dual range × 5/10 g"),
				("Family capacities", "6/15 kg × 2/5 g also available"),
				("Speed keys", "54 keys (108 PLU via double-click)"),
				("Display", "Combined wide graphic LCD, 208 × 48"),
			]),
			("Printing", [
				("Printer", "Built-in thermal label printer"),
				("Print speed", "Up to 100 mm/s"),
				("Resolution", "202 dpi"),
				("Label size", "Width 40–60 mm; length 30–120 mm"),
				("Formats", "45 fixed plus up to 20 custom"),
				("Media", "Easy-loading label cartridge"),
			]),
			("Data & networking", [
				("PLU capacity", "6,000 PLUs (official CL-5200 specification)"),
				("Ingredients", "1,000 ingredient records"),
				("Networking", "Ethernet TCP/IP; optional wireless"),
				("Software", "CAS CL-Works Pro"),
			]),
			("Connectivity", [
				("Interfaces", "USB, LAN, RJ11, RS-232C"),
				("Power", "AC 100–240 V, 50/60 Hz"),
			]),
			("Physical", [
				("Platter", "Stainless steel, approx. 380 × 250 mm"),
				("Dimensions (W × D × H)", "Approx. 409 × 441 × 180 mm"),
				("Product weight", "Approx. 7.0 kg"),
				("Operating temperature", "−10 °C to 40 °C"),
				("Item code", "RET.SYS.CAS.1246"),
			]),
		]
	raise ValueError(f"No CAS specs for {slug}")


def apply_cas_page(doc, media: dict[str, str]):
	from printechs_digital.api.website import _resolve_product_slug

	slug = _resolve_product_slug(doc.slug)
	rows = CAS_APPLICATIONS.get(slug)
	if not rows:
		return
	doc.set("applications", [
		{
			"title": title,
			"description": description,
			"image": media[key],
			"image_alt": alt,
			"industry_link": industry,
			"sort_order": i,
		}
		for i, (key, title, description, alt, industry) in enumerate(rows, start=1)
	])
	set_specs(doc, specs_for(slug))
	old, new, label = BROCHURE_MAP[slug]
	path = site_file(new) if (SITE_FILES / new).exists() else site_file(old)
	doc.primary_download_label = label
	doc.primary_download_file = path
	doc.set("downloads", [{"label": label, "file": path, "download_type": "Brochure", "sort_order": 1}])
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1


def _ensure_file_folder(path_parts: tuple[str, ...]) -> str:
	parent = "Home"
	for part in path_parts:
		name = f"{parent}/{part}"
		if not frappe.db.exists("File", name):
			folder = frappe.get_doc(
				{"doctype": "File", "file_name": part, "is_folder": 1, "folder": parent}
			)
			folder.flags.ignore_permissions = True
			folder.insert()
		parent = name
	return parent


def _register_existing_file(folder: str, filename: str, file_url: str) -> None:
	if frappe.db.exists("File", {"file_url": file_url, "folder": folder}):
		return
	disk = Path(frappe.get_site_path("public", "files")) / file_url.replace("/files/", "", 1)
	if not disk.exists():
		return
	suffix = filename.rsplit(".", 1)[-1].lower()
	file_type = {"jpg": "Image", "jpeg": "Image", "png": "Image", "pdf": "PDF"}.get(suffix, "")
	doc = frappe.new_doc("File")
	doc.name = frappe.generate_hash(length=10)
	doc.file_name = filename
	doc.file_url = file_url
	doc.folder = folder
	doc.is_private = 0
	doc.file_size = disk.stat().st_size
	doc.file_type = file_type
	doc.db_insert()


def register_library_in_desk() -> int:
	"""Expose /files library assets in Desk File Manager without re-uploading."""
	app_folder = _ensure_file_folder(("Library", "CAS", "Applications"))
	social_folder = _ensure_file_folder(("Library", "CAS", "Social"))
	brochure_folder = _ensure_file_folder(("Library", "CAS", "Brochures"))
	ab_folder = _ensure_file_folder(("Library", "Avery Berkel", "Applications"))
	count = 0
	for key in CAS_APP_KEYS:
		name = f"cas-app-{key}.jpg"
		_register_existing_file(app_folder, name, site_file(name))
		count += 1
	for key in CAS_SOCIAL_KEYS:
		name = f"cas-social-{key}.jpg"
		_register_existing_file(social_folder, name, site_file(name))
		count += 1
	seen_brochures: set[str] = set()
	for _old, new, _label in BROCHURE_MAP.values():
		if new in seen_brochures:
			continue
		seen_brochures.add(new)
		_register_existing_file(brochure_folder, new, site_file(new))
		count += 1
	for src in SITE_FILES.glob("ab-app-*.jpg"):
		if src.is_file():
			_register_existing_file(ab_folder, src.name, site_file(src.name))
			count += 1
	return count


def update_cas_library_and_pages():
	media = install_cas_library()
	register_library_in_desk()
	updated = []
	for slug in CAS_APPLICATIONS:
		name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
		if not name:
			continue
		doc = frappe.get_doc("Website Product", name)
		apply_cas_page(doc, media)
		doc.flags.ignore_permissions = True
		doc.save()
		updated.append(slug)
	frappe.db.commit()
	print(f"Updated {len(updated)} CAS pages; library at /files/library/cas/")
	return updated
