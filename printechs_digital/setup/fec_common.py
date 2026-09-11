# Copyright (c) 2026, Printechs and contributors
"""Shared helpers and unique media for FEC / Firich POS fills."""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
BRAND_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/brands")
TMP_DIR = Path("/tmp/fec-pos")
LIBRARY = SITE_FILES / "library" / "fec"
BRAND = "FEC"
OFFICIAL_SITE = "https://www.fecpos.com/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0"

# Official FEC cutouts / family shots — one URL per unique local file.
OFFICIAL_IMAGES = {
	"logo": "https://m.fecpos.com:29021/designguide/fec-logo.png",
	"hub-banner": "https://www.fecpos.com/proimages/Web_Data/Index_Banner/Web_bk_1500x690.jpg",
	"family-xpos": "https://m.fecpos.com:29021/officalweb-middle-elementzone/XPOSp.png",
	"family-xppc": "https://www.fecpos.com/proimages/Web_Data/product/01-XPPC/webicon/xppciconES.png",
	"family-xelf": "https://www.fecpos.com/proimages/pic/xelf2.png",
	"family-kp": "https://www.fecpos.com/proimages/Web_Data/Index-pic/KPL.png",
	"family-monitor": "https://www.fecpos.com/proimages/Web_Data/Index-pic/moniter750.png",
	"family-print": "https://www.fecpos.com/proimages/productlist/1200840.png",
	"xp-4765w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/XPOSPLUS/XP-4765W/new/XPOS_PLUS_ASM-20230530.532.png",
	"xp-4765w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/XPOSPLUS/XP-4765W/new/XPOS_PLUS_ASM-20230530.533.png",
	"xp-4765w-c": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/XPOSPLUS/XP-4765W/new/XPOS_PLUS_ASM-20230530.534.png",
	"xp-3765w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/XPOSPLUS/XP-3765W/231214.520.png",
	"xp-3765w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/XPOSPLUS/XP-3765W/231214.273.png",
	"xp-3765w-c": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/XPOSPLUS/XP-3765W/231214.271.png",
	"xp-4765-a": "https://www.fecpos.com/proimages/pb/product-detail/01-XPOS/XPOS_PLUS_ASM-20230530.723.png",
	"xp-4765-b": "https://www.fecpos.com/proimages/pb/product-detail/01-XPOS/XPOS_PLUS_ASM-20230530.720.png",
	"xp-3765-a": "https://www.fecpos.com/proimages/pb/productlist/231214.218.png",
	"xp-3765-b": "https://www.fecpos.com/proimages/pb/productlist/231214.215.png",
	"st-1130w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/ST-1130W/ST-1130W_B1.png",
	"st-1130w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/03-POS_System/ST-1130W/ST-1130W_B2.png",
	"xelf-ii-a": "https://www.fecpos.com/proimages/pb/Xelf2/0213.903.png",
	"xelf-ii-b": "https://www.fecpos.com/proimages/pb/Xelf2/0213.920.png",
	"xelf-ii-c": "https://www.fecpos.com/proimages/pb/Xelf2/0213.923.png",
	"pp-9745w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/01-XPPC/PP-9745W/ppic/0620_g3_io.294.png",
	"pp-9745w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/01-XPPC/PP-9745W/ppic/0620_g3_io.295.png",
	"pp-9735w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/05-Panel_PC/PP-9735W/2.png",
	"pp-9735w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/05-Panel_PC/PP-9735W/3.png",
	"pp-9815w-a": "https://www.fecpos.com/proimages/pb/product-detail/10-XPPC/x004.png",
	"pp-9815w-b": "https://www.fecpos.com/proimages/pb/product-detail/10-XPPC/x001.png",
	"kp-9795w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/11-KP/new/pic-n/15/151-abA.png",
	"kp-9795w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/11-KP/new/pic-n/15/153-abA.png",
	"kp-9155w-a": "https://www.fecpos.com/proimages/pb/KP/150-abA.png",
	"xc-574-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/04-BOX_System/XC-574/XC575F1.png",
	"xc-574-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/04-BOX_System/XC-574/XC575F2.png",
	"xc-373-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/04-BOX_System/XC-373/001.png",
	"xc-373-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/04-BOX_System/XC-373/002.png",
	"ld-9043w-a": "https://www.fecpos.com/proimages/pb/Web_Data/product/06-Monitors/LD-9043W/LD-9043W_1.png",
	"ld-9043w-b": "https://www.fecpos.com/proimages/pb/Web_Data/product/06-Monitors/LD-9043W/LD-9043W_2.png",
	"tp-100-a": "https://www.fecpos.com/proimages/pb/product-detail/08-Peripherals/TP-100/TP-100_B1.png",
	"tp-100-b": "https://www.fecpos.com/proimages/pb/product-detail/08-Peripherals/TP-100/TP-100_B2.png",
	"msr": "https://www.fecpos.com/proimages/product-detail/01-XPOS/MSR/MSR_B1.png",
}

# Unique lifestyle scenes (Unsplash). Do not reuse industry-retail.jpg.
APP_IMAGES = {
	"fashion": "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=1600&q=80",
	"grocery": "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=1600&q=80",
	"pharmacy": "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=1600&q=80",
	"beauty": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?auto=format&fit=crop&w=1600&q=80",
	"hospitality": "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1600&q=80",
	"qsr": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1600&q=80",
	"kitchen": "https://images.unsplash.com/photo-1556911220-bff31c812dba?auto=format&fit=crop&w=1600&q=80",
	"selfservice": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1600&q=80",
	"electronics": "https://images.unsplash.com/photo-1498049794561-7780e7231661?auto=format&fit=crop&w=1600&q=80",
	"enterprise": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1600&q=80",
}

KSA_BODY = (
	"Printechs supplies and supports FEC POS hardware across Saudi Arabia, including Riyadh, "
	"Jeddah and Dammam — specification, peripheral integration, Modern POS / ERPNext connection "
	"and after-sales service. FEC POS Solutions from Printechs Saudi Arabia."
)


def site_file(filename: str) -> str:
	return f"/files/{filename}"


def download(url: str, dest: Path) -> Path:
	dest.parent.mkdir(parents=True, exist_ok=True)
	if dest.exists() and dest.stat().st_size > 4000:
		return dest
	req = Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
	with urlopen(req, timeout=45) as response:
		data = response.read()
	if len(data) < 800:
		frappe.throw(f"Download too small ({len(data)} bytes): {url}")
	dest.write_bytes(data)
	return dest


def open_image(path: Path) -> Image.Image:
	im = Image.open(path)
	if im.mode in {"P", "LA"}:
		im = im.convert("RGBA")
	return im


def make_card(src: Path, dest_name: str, background=(255, 255, 255)) -> str:
	dest = SITE_FILES / dest_name
	im = open_image(src).convert("RGBA")
	scale = min(1040 / im.width, 1040 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), background)
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new.split()[-1] if new.mode == "RGBA" else None)
	canvas.save(dest, "JPEG", quality=92, optimize=True)
	return site_file(dest_name)


def save_jpeg(src: Path, dest_name: str, max_edge: int = 1800) -> str:
	dest = SITE_FILES / dest_name
	im = open_image(src).convert("RGB")
	w, h = im.size
	if max(w, h) > max_edge:
		scale = max_edge / max(w, h)
		im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
	im.save(dest, "JPEG", quality=90, optimize=True)
	return site_file(dest_name)


def save_app_scene(src: Path, dest_name: str, size: tuple[int, int] = (1600, 1200)) -> str:
	im = open_image(src).convert("RGB")
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
	candidates = [
		TMP_DIR / "logo-cands" / "fec-logo.png",
		TMP_DIR / "fec-logo-src.png",
	]
	src = next((path for path in candidates if path.exists() and path.stat().st_size > 1000), None)
	if src is None:
		src = download(OFFICIAL_IMAGES["logo"], TMP_DIR / "fec-logo-src.png")
	im = open_image(src).convert("RGBA")
	bbox = im.getbbox()
	if bbox:
		im = im.crop(bbox)
	canvas = Image.new("RGBA", (400, 160), (255, 255, 255, 0))
	scale = min(360 / im.width, 120 / im.height)
	new = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.Resampling.LANCZOS)
	canvas.paste(new, ((400 - new.width) // 2, (160 - new.height) // 2), new)
	for dest in (SITE_FILES / "brand-fec.png", BRAND_DIR / "brand-fec.png"):
		dest.parent.mkdir(parents=True, exist_ok=True)
		canvas.save(dest, "PNG")
	return site_file("brand-fec.png")


def prepare_media() -> dict[str, str]:
	SITE_FILES.mkdir(parents=True, exist_ok=True)
	TMP_DIR.mkdir(parents=True, exist_ok=True)
	(LIBRARY / "products").mkdir(parents=True, exist_ok=True)
	(LIBRARY / "applications").mkdir(parents=True, exist_ok=True)

	raw: dict[str, Path] = {}
	for key, url in OFFICIAL_IMAGES.items():
		if key == "logo":
			continue
		ext = Path(url.split("?", 1)[0]).suffix.lower() or ".png"
		if ext not in {".png", ".jpg", ".jpeg", ".webp"}:
			ext = ".png"
		try:
			raw[key] = download(url, TMP_DIR / f"{key}{ext}")
		except Exception as exc:
			# Family banners on m.fecpos.com:29021 can fail; fall back later.
			print(f"Skip official {key}: {exc}")

	apps: dict[str, str] = {}
	for key, url in APP_IMAGES.items():
		src = download(url, TMP_DIR / f"app-{key}.jpg")
		filename = f"fec-app-{key}.jpg"
		apps[key] = save_app_scene(src, filename)
		(LIBRARY / "applications" / filename).write_bytes((SITE_FILES / filename).read_bytes())

	def card(key: str, dest: str) -> str:
		if key not in raw:
			frappe.throw(f"Missing FEC source image for card {dest} ({key})")
		path = make_card(raw[key], dest)
		(LIBRARY / "products" / dest).write_bytes((SITE_FILES / dest).read_bytes())
		return path

	def scene(key: str, dest: str) -> str:
		if key not in raw:
			frappe.throw(f"Missing FEC source image for scene {dest} ({key})")
		path = save_jpeg(raw[key], dest)
		return path

	# Family cards prefer official family artwork; fall back to a unique product angle.
	family_map = {
		"hub": ("family-xpos", "xp-4765w-b", "hub-banner"),
		"xpos": ("family-xpos", "xp-4765w-b"),
		"xppc": ("family-xppc", "pp-9745w-b"),
		"xelf": ("family-xelf", "xelf-ii-a"),
		"kp": ("family-kp", "kp-9795w-a"),
		"xcomp": ("xc-574-a",),
		"monitor": ("family-monitor", "ld-9043w-a"),
		"peripherals": ("family-print", "tp-100-a"),
	}
	cards: dict[str, str] = {}
	for name, keys in family_map.items():
		src_key = next((k for k in keys if k in raw), None)
		if not src_key:
			frappe.throw(f"No source image available for family card {name}")
		cards[name] = card(src_key, f"fec-{name}-card.jpg")

	sku_cards = {
		"xp-4765w": "xp-4765w-a",
		"xp-3765w": "xp-3765w-a",
		"xp-4765": "xp-4765-a",
		"xp-3765": "xp-3765-a",
		"st-1130w": "st-1130w-a",
		"xelf-ii": "xelf-ii-a",
		"pp-9745w": "pp-9745w-a",
		"pp-9735w": "pp-9735w-a",
		"pp-9815w": "pp-9815w-a",
		"kp-9795w": "kp-9795w-a",
		"kp-9155w": "kp-9155w-a",
		"xc-574": "xc-574-a",
		"xc-373": "xc-373-a",
		"ld-9043w": "ld-9043w-a",
		"tp-100": "tp-100-a",
	}
	for name, key in sku_cards.items():
		cards[name] = card(key, f"fec-{name}-card.jpg")

	angles = {}
	for key in raw:
		angles[key] = scene(key, f"fec-{key}.jpg")

	return {
		**cards,
		**{f"app_{k}": v for k, v in apps.items()},
		**{f"src_{k}": v for k, v in angles.items()},
		"logo": install_logo(),
	}


def app_row(media: dict[str, str], key: str, title: str, description: str, alt: str, industry: str, sort: int) -> dict:
	return {
		"title": title,
		"description": description,
		"image": media[f"app_{key}"],
		"image_alt": alt,
		"industry_link": industry,
		"sort_order": sort,
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


def q_select(group: str, label: str, choices: list[str], *, required=1, sort=1) -> dict:
	return {
		"group_label": group,
		"label": label,
		"option_type": "Select",
		"choices": "\n".join(choices),
		"required": required,
		"sort_order": sort,
	}


def q_check(group: str, label: str, choices: list[str], *, required=0, sort=1) -> dict:
	return {
		"group_label": group,
		"label": label,
		"option_type": "Checkbox",
		"choices": "\n".join(choices),
		"required": required,
		"sort_order": sort,
	}


def xpos_quote_options() -> list[dict]:
	return [
		q_select("Platform", "Processor", [
			"Intel Celeron G6900",
			"Intel Core i3-12100",
			"Intel Core i3-12100TE",
			"Intel Core i5-12400",
			"Intel Core i5-12500TE",
			"Intel Core i7-12700",
			"Confirm during survey",
		], sort=1),
		q_select("Platform", "Memory", ["8 GB DDR4", "16 GB DDR4", "32 GB DDR4"], sort=2),
		q_select("Platform", "Storage", ["256 GB M.2 PCIe", "512 GB M.2 PCIe", "1 TB M.2 PCIe"], required=0, sort=3),
		q_select("Software", "Operating system", [
			"Windows 10 IoT Enterprise",
			"Windows 11 IoT Enterprise",
			"No OS (hardware only)",
		], sort=4),
		q_check("Options", "Optional modules", [
			"RFID reader",
			"2D barcode scanner",
			"Camera and LED module",
			"Wi-Fi and Bluetooth",
			"Customer display",
		], sort=5),
	]


def panel_h610_quote_options() -> list[dict]:
	return [
		q_select("Platform", "Processor", [
			"Intel Core i3-12100",
			"Intel Core i5-12400",
			"Intel Core i7-12700",
			"Confirm during survey",
		], sort=1),
		q_select("Platform", "Memory", ["8 GB DDR4", "16 GB DDR4", "32 GB DDR4"], sort=2),
		q_select("Platform", "Storage", ["256 GB SSD", "512 GB SSD"], sort=3),
		q_select("Software", "Operating system", [
			"Windows 10 IoT Enterprise",
			"Windows 11 IoT Enterprise",
			"No OS (hardware only)",
		], sort=4),
	]


def support_items() -> list[dict]:
	return [
		{"icon": "install", "title": "Deployment", "description": "Counter, kiosk or kitchen survey, mounting and I/O planning in Riyadh, Jeddah and Dammam.", "sort_order": 1},
		{"icon": "integration", "title": "POS integration", "description": "Modern POS, ERPNext, scanners, printers, payment terminals and ESL where the project needs them.", "sort_order": 2},
		{"icon": "maintenance", "title": "Saudi support", "description": "Spares, warranty handling and on-site service after go-live.", "sort_order": 3},
		{"icon": "training", "title": "Training", "description": "Operator and supervisor training for checkout, kiosk or kitchen workflows.", "sort_order": 4},
	]


def get_or_create(slug: str, display_name: str, hero: str, subcategory: str):
	existing = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = slug
	doc.website_product_name = display_name
	doc.display_name = display_name
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "POS Hardware"
	doc.subcategory = subcategory
	doc.short_description = f"{display_name} from FEC, supplied by Printechs Saudi Arabia."
	doc.long_description = f"<p>{display_name} from FEC, supplied by Printechs Saudi Arabia.</p>"
	doc.hero_image = hero
	return doc


def apply_identity(doc, *, slug, display_name, subcategory, category_label, on_list=True, featured=0, is_hub=0, configure=0):
	if not frappe.db.exists("Brand", BRAND):
		brand = frappe.new_doc("Brand")
		brand.brand = BRAND
		brand.flags.ignore_permissions = True
		brand.insert()
	doc.display_name = display_name
	doc.website_product_name = display_name
	doc.slug = slug
	doc.brand = BRAND
	doc.brand_name = "FEC"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.page_mode = "Full"
	doc.category = "POS Hardware"
	doc.subcategory = subcategory
	doc.category_label = category_label
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.configure_on_quote = 1 if configure else 0
	doc.featured = featured
	doc.show_on_products_list = 1 if on_list else 0
	doc.show_on_software_list = 0
	doc.card_brand_label = "FEC"
	doc.show_item_code_on_website = 0
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{slug}/quote"
	doc.final_cta_secondary_label = "Talk to a POS Hardware Specialist"
	doc.final_cta_secondary_href = "/contact"
	doc.canonical_path = f"/products/{slug}"
	doc.index_page = 1
	doc.published = 1
	doc.is_hub = is_hub
	doc.video_url = ""


def save_product(doc):
	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	frappe.db.commit()
	print(f"Filled {doc.name} → /products/{doc.slug}")
	return doc.name


def update_website_brand(logo: str):
	name = frappe.db.get_value("Website Brand", {"slug": "fec"}, "name")
	doc = frappe.get_doc("Website Brand", name) if name else frappe.new_doc("Website Brand")
	if not frappe.db.exists("Brand", BRAND):
		frappe.throw("ERP Brand FEC was not found")
	doc.brand = BRAND
	doc.display_name = "FEC"
	doc.slug = "fec"
	doc.logo = logo
	doc.summary = (
		"FEC POS Solutions from Printechs Saudi Arabia — POS terminals, panel PCs, "
		"self-service kiosks, kitchen displays, box PCs, touch monitors and peripherals."
	)
	doc.sort_order = 13
	doc.official_website = OFFICIAL_SITE
	doc.show_in_footer = 0
	doc.published = 1
	doc.meta_title = "FEC POS Systems, Self-Service Kiosks & Commercial Touch Solutions | Printechs"
	doc.meta_description = (
		"FEC POS systems in Saudi Arabia from Printechs: XPOS Plus terminals, XPPC panel PCs, "
		"XELF II kiosks, KP kitchen displays, XCOMP box PCs, XMonitor and POS peripherals."
	)
	doc.flags.ignore_permissions = True
	if name:
		doc.save()
	else:
		doc.insert()
	frappe.db.commit()
	print(f"Website Brand FEC → /brands/fec ({doc.name})")
	return doc.name
