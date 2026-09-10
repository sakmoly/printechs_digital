# Copyright (c) 2026, Printechs and contributors
"""Create and fill Website Product for Datalogic Matrix 320 Series (no ERP Item).

Official page:
https://www.datalogic.com/eng/retail-manufacturing-transportation-logistics/stationary-industrial-scanners/matrix-320-series-pd-895.html
Datasheets: DS-MATRIX320-2MP-EN Rev I 20240318; Matrix 320 5MP QRG 821012073 Rev D.

Stationary industrial 2D imager — not a handheld or POS scanner.
Liquid Lens electronic focus is specified on 2MP LQL models.
Premium / X extra processing is not standard on every Matrix 320.
UV illuminators are specialist (EN 62471 Risk Group 3) — not a default kit.
"""

from pathlib import Path
from shutil import copy2
from urllib.parse import quote
from urllib.request import Request, urlopen

from PIL import Image

import frappe

SLUG = "datalogic-matrix-320"
VIDEO_URL = "https://youtu.be/Pga2a2nEsx0"
FIVE_MP_VIDEO = "https://youtu.be/S69zP7Z8oco"
PREMIUM_VIDEO = "https://youtu.be/ryIL6VefDyo"
HANDS_FREE_VIDEO = "https://youtu.be/mWSe3HRKF64"
HIGH_SPEED_VIDEO = "https://youtu.be/geJZzG4DD90"
CMOUNT_VIDEO = "https://youtu.be/p8zuj2Ux_2o"
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
DATALOGIC_HOST = "https://www.datalogic.com"

OFFICIAL_IMAGES = {
	"datalogic-matrix-320-beauty.png": "/upload/products/unattendedscanningsystems/Matrix320Beauty.png",
	"datalogic-matrix-320-operation.jpg": "/upload/prod_line/Stationary Industrial Scanners/Matrix320/EMPOWER-YOUR-OPERATION_M320SERIES.jpg",
	"datalogic-matrix-320-applications.jpg": "/upload/prod_line/Stationary Industrial Scanners/Matrix320/EMPOWER-YOUR-APPLICATIONS_M320SERIES.jpg",
	"datalogic-matrix-320-installation.jpg": "/upload/prod_line/Stationary Industrial Scanners/Matrix320/EMPOWER-YOUR-INSTALLATION_M320SERIES.jpg",
}


def copy_public_image(filename: str) -> str:
	source = INDUSTRY_DIR / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def download_file(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if not target.exists():
		request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; Printechs/1.0)"})
		with urlopen(request, timeout=30) as response, target.open("wb") as handle:
			handle.write(response.read())
	return f"/files/{filename}"


def official_image(filename: str) -> str:
	target = SITE_FILES / filename
	if target.exists():
		return f"/files/{filename}"
	return download_file(filename, DATALOGIC_HOST + quote(OFFICIAL_IMAGES[filename], safe="/:+"))


def catalog_card_from_cutout(source_name: str, dest_name: str) -> str:
	"""Official beauty shot is 700 px; pad/scale to a 1200×1200 catalog card."""
	source = SITE_FILES / source_name
	dest = SITE_FILES / dest_name
	official_image(source_name)
	im = Image.open(source).convert("RGBA")
	scale = 900 / max(im.size)
	new = im.resize((int(im.width * scale), int(im.height * scale)), Image.Resampling.LANCZOS)
	canvas = Image.new("RGB", (1200, 1200), (255, 255, 255))
	x = (1200 - new.width) // 2
	y = (1200 - new.height) // 2
	canvas.paste(new.convert("RGB"), (x, y), new)
	canvas.save(dest, "JPEG", quality=90, optimize=True)
	return f"/files/{dest_name}"


def related_product_row(name: str, sort_order: int) -> dict | None:
	if not frappe.db.exists("Website Product", name):
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


def get_or_create():
	existing = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if existing:
		return frappe.get_doc("Website Product", existing)
	doc = frappe.new_doc("Website Product")
	doc.slug = SLUG
	doc.website_product_name = "Datalogic Matrix 320 Series"
	doc.display_name = "Datalogic Matrix 320 Series"
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.short_description = "Datalogic Matrix 320 stationary industrial 2D imager."
	doc.long_description = "<p>Datalogic Matrix 320 stationary industrial 2D imager.</p>"
	doc.hero_image = official_image("datalogic-matrix-320-beauty.png")
	return doc


def fill_datalogic_matrix_320():
	doc = get_or_create()

	hero = catalog_card_from_cutout(
		"datalogic-matrix-320-beauty.png", "datalogic-matrix-320-product.jpg"
	)
	operation = official_image("datalogic-matrix-320-operation.jpg")
	applications = official_image("datalogic-matrix-320-applications.jpg")
	installation = official_image("datalogic-matrix-320-installation.jpg")
	warehouse = copy_public_image("industry-warehouse-logistics.jpg")
	packaging = copy_public_image("industry-packaging.jpg")
	food = copy_public_image("industry-food-beverage.jpg")
	pharma = copy_public_image("industry-pharmaceutical.jpg")

	# Intentionally no Item — link later under ERP Item Link when you choose the SKU.
	doc.item = None
	doc.website_product_name = "Datalogic Matrix 320 Series"
	doc.display_name = "Datalogic Matrix 320 Series"
	doc.slug = SLUG
	doc.product_type = "Retail Hardware"
	doc.division = "Retail"
	doc.category = "Barcode & Mobility"
	doc.subcategory = "Stationary Industrial Scanners"
	doc.category_label = "STATIONARY 2D IMAGER"
	if frappe.db.exists("Brand", "Datalogic"):
		doc.brand = "Datalogic"
	doc.tagline = "Empower your traceability — 2 MP or 5 MP on the line"
	doc.short_description = (
		"Datalogic Matrix 320 is a fixed-mount industrial 2D imager for conveyors, packing "
		"benches and automated traceability. Choose 2 MP (1920 × 1080) or 5 MP (2560 × 1936), "
		"liquid-lens or C-Mount optics, and Gigabit Ethernet with PROFINET or EtherNet/IP."
	)
	doc.long_description = (
		"<p>Matrix 320 is Datalogic’s compact stationary 2D reader for manufacturing, "
		"in-plant logistics and distribution. It mounts over a conveyor, at a packing bench "
		"or on a machine — it is not a handheld gun and not a POS scanner.</p>"
		"<p>The 2 MP sensor (1920 × 1080, 16:9) gives the horizontal field of view of a typical "
		"3 MP part, at up to 60 frames/s. The 5 MP sensor (2560 × 1936) adds HDR, a wider "
		"application area and high intrinsic depth of field so one reader can take several "
		"labels or codes in one shot.</p>"
		"<p>2 MP Liquid Lens models (6 / 9 / 16 mm) change focus electronically — no opening "
		"the housing when the batch changes. 2 MP and 5 MP C-Mount bodies take Datalogic or "
		"third-party lenses. Illumination is modular: 14-LED HP or 36-LED VHP on 2 MP; 36-LED "
		"VHP or 72-LED UHP on 5 MP. Colour (red, white, blue; IR/UV on selected C-Mount kits) "
		"matches the mark and the material.</p>"
		"<p>Every series model has Time of Flight distance sensing and an orientation sensor. "
		"ToF trims photometry to the real working distance and can set a range limit so a "
		"hands-free bench does not fire on the wrong package. The orientation sensor stores "
		"mount pose and warns if the reader is knocked.</p>"
		"<p>Industrial I/O is onboard: Gigabit Ethernet (TCP/IP, FTP, PROFINET IO, EtherNet/IP, "
		"Modbus TCP), RS-232 / RS-422, ID-NET, two opto inputs and three outputs. Configure "
		"with X-PRESS or DL.CODE. Housing is IP65/IP67 on 24 VDC.</p>"
		"<p>Matrix 320 X keeps the same body and accessories on a newer platform. Premium "
		"quad-core models (1.6 GHz vs 0.9 GHz) are specified to double processing and halve "
		"decode time — they are not the default SKU. Printechs specifies Matrix 320 for "
		"Saudi Arabia plants and DCs; link the ERP Item on this page when you pick the optic.</p>"
	)

	doc.hero_image = hero
	doc.hero_image_alt = (
		"Datalogic Matrix 320 Series stationary industrial 2D barcode imager"
	)
	doc.video_url = VIDEO_URL
	doc.hero_trust_chips = (
		"2 MP or 5 MP fixed mount\n"
		"IP65 / IP67 · 24 VDC\n"
		"PROFINET · EtherNet/IP\n"
		"2-year factory warranty"
	)
	doc.story_heading = "Fixed-mount 2D reading for conveyors, benches and machines"
	doc.visual_story_heading = "Matrix 320 on the line and in the DC"
	doc.collapsible_full_specs = 1
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 1
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.card_title = "Matrix 320"
	doc.card_brand_label = "Datalogic"
	doc.card_summary = (
		"Stationary industrial 2D imager for conveyors and packing benches: 2 MP or 5 MP, "
		"liquid lens or C-Mount, ToF, IP65/IP67 and Gigabit fieldbus."
	)
	doc.card_image = hero

	doc.final_cta_heading = "Specify Matrix 320 for your conveyor or packing cell"
	doc.final_cta_description = (
		"Printechs can confirm 2 MP vs 5 MP, liquid lens vs C-Mount, 14/36/72-LED lighting "
		"and PROFINET or EtherNet/IP for plants in Saudi Arabia."
	)
	doc.final_cta_primary_label = "Request a Quote"
	doc.final_cta_primary_href = f"/products/{SLUG}/quote"
	doc.final_cta_secondary_label = "Talk to Our Industrial Team"
	doc.final_cta_secondary_href = "/contact"

	doc.meta_title = "Datalogic Matrix 320 Stationary Industrial Scanner | Printechs"
	doc.meta_description = (
		"Datalogic Matrix 320 fixed-mount 2D imager: 2 MP or 5 MP, liquid lens or C-Mount, "
		"IP65/IP67, PROFINET and EtherNet/IP. For conveyors and plants in Saudi Arabia."
	)
	doc.canonical_path = f"/products/{SLUG}"
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "2 MP or 5 MP on the line",
				"description": (
					"2 MP (1920 × 1080, 16:9, 60 fps) matches a typical 3 MP horizontal FoV. "
					"5 MP (2560 × 1936, HDR, 25 fps) covers a wider area and several codes in "
					"one frame."
				),
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "ToF and remote focus",
				"description": (
					"Time of Flight sets photometry to the real distance and can block stray "
					"reads. 2 MP liquid lenses (6 / 9 / 16 mm) refocus from DL.CODE when the "
					"batch changes."
				),
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Gigabit industrial I/O",
				"description": (
					"Onboard 10/100/1000 Ethernet with TCP/IP, FTP, PROFINET IO, EtherNet/IP "
					"and Modbus TCP, plus RS-232/422, ID-NET, two opto inputs and three outputs."
				),
				"sort_order": 3,
			},
			{
				"icon": "rugged",
				"title": "IP65 / IP67, 24 V plant power",
				"description": (
					"Aluminium body, sealed M12 power/I-O and X-coded Gigabit, 360° green/red "
					"read feedback and X-PRESS setup — built for the shop floor, not the till."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "ToF + orientation on every model",
				"image": operation,
				"image_alt": "Matrix 320 Time of Flight and orientation sensors on a fixed mount",
				"caption": "Distance sensing trims light; orientation stores mount pose.",
				"sort_order": 1,
			},
			{
				"label": "Modular optics and lighting",
				"image": applications,
				"image_alt": "Matrix 320 liquid-lens and C-Mount illuminator configurations",
				"caption": "14 / 36 / 72 LED, red, white, blue — or IR/UV on selected C-Mount kits.",
				"sort_order": 2,
			},
			{
				"label": "Install once, swap later",
				"image": installation,
				"image_alt": "Matrix 320 rotating connectors, brackets and 360° status LEDs",
				"caption": "0° or 90° connectors, X-PRESS and DL.CODE. Blue / green / red status.",
				"sort_order": 3,
			},
			{
				"label": "Conveyor and packing-bench work",
				"image": warehouse,
				"image_alt": "Warehouse conveyor and packing bench for Matrix 320 reading",
				"caption": "Inbound, print-and-apply, fulfilment and end-of-line traceability.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "scan",
				"title": "2 MP / 5 MP",
				"description": "1920×1080 @ 60 fps · 2560×1936 @ 25 fps",
				"sort_order": 1,
			},
			{
				"icon": "display",
				"title": "LQL or C-Mount",
				"description": "6/9/16 mm electronic focus · C-Mount 4–50 mm",
				"sort_order": 2,
			},
			{
				"icon": "connectivity",
				"title": "Gigabit + fieldbus",
				"description": "PROFINET · EtherNet/IP · Modbus TCP · ID-NET",
				"sort_order": 3,
			},
			{
				"icon": "rugged",
				"title": "IP65 / IP67",
				"description": "24 VDC · aluminium · sealed M12",
				"sort_order": 4,
			},
			{
				"icon": "device",
				"title": "ToF + pose",
				"description": "Distance sensor · orientation memory",
				"sort_order": 5,
			},
			{
				"icon": "shield",
				"title": "2-year warranty",
				"description": "Factory warranty · EASEOFCARE options",
				"sort_order": 6,
			},
		],
	)

	spec_rows = []
	groups = [
		(
			"Family & sensors",
			[
				("Family", "Matrix 320 stationary industrial 2D imager (not handheld / POS)"),
				("2 MP sensor", "1920 × 1080, 16:9, 1/3\" CMOS global shutter, 60 frames/s"),
				("5 MP sensor", "2560 × 1936 CMOS, 25 frames/s, HDR, high intrinsic DoF"),
				("2 MP FoV note", "16:9 horizontal FoV comparable to a typical 3 MP sensor"),
				("Platform", "Multicore image processing; 5 MP adds hardware acceleration"),
				("Standard CPU", "4 cores @ 900 MHz (2 MP datasheet)"),
				("Premium CPU", "4 cores @ 1600 MHz — double power / half decode time vs standard"),
				("X models", "Newer platform; same body, size and accessories as current 320"),
				("HDR", "Supported — improves contrast and can shorten exposure on fast lines"),
			],
		),
		(
			"Optics & illumination",
			[
				("2 MP liquid lens", "LQL 6 mm (48°), 9 mm (34°), 16 mm (20°) — electronic focus"),
				("2 MP LQL range", "6 mm: 50–550 mm; 9 mm: 35–1000 mm; 16 mm: 70–1500 mm"),
				("2 MP C-Mount", "4 / 6 / 8 / 12 / 16 / 25 / 35 mm Datalogic or third-party C-Mount"),
				("5 MP C-Mount", "8 / 12 / 16 / 25 / 35 / 50 mm (50° down to 8° aperture angle)"),
				("5 MP range (lens front)", "8 mm: 50 mm–∞; 12 mm: 100 mm–∞; 16–35 mm: 200 mm–∞; 50 mm: 400 mm–∞"),
				("2 MP lights", "14-LED High Power or 36-LED Very High Power; red / white / blue"),
				("5 MP lights", "36-LED VHP (white, blue, IR, UV) or 72-LED UHP (white or blue)"),
				("Aiming", "Laser cross (typical 14/36 LED); grid pattern or dual pointer on some kits"),
				("ToF", "Embedded Time of Flight on the series — auto photometry and range limits"),
				("Orientation", "Stores install pose; warns if the reader is moved"),
				("Filters", "Polarizer, ESD, band-pass and YAG-cut covers as accessories"),
				("UV caution", "UV kits are EN 62471 Risk Group 3 — skilled use and PPE only"),
			],
		),
		(
			"Decoding & software",
			[
				("1D / stacked", "Code 128/39/93, EAN/UPC, GS1 DataBar, PDF417, composites, Pharmacode"),
				("2D", "Data Matrix ECC 200 (incl. DPM), QR, Micro QR, Aztec, MaxiCode, DotCode"),
				("Postal", "Australia, RM4SCC, KIX, Japan, PLANET, POSTNET, Intelligent Mail, Swedish"),
				("Code quality", "ISO/IEC 15416, 15415, 16022/18004, AIM-DPM (ISO/IEC 29158)"),
				("Modes", "Continuous, One Shot, Phase Mode, PackTrack"),
				("Setup", "X-PRESS HMI (AIM, auto-setup, test) or DL.CODE over Ethernet/serial"),
				("Images", "FTP / SFTP image save and web Device Discovery (2 MP datasheet)"),
				("Feedback", "360° RGB (green good, red no-read, blue config) plus Green/Red Spot"),
			],
		),
		(
			"Interfaces & power",
			[
				("Ethernet", "10/100/1000 Mbit/s — TCP/IP, UDP, FTP; SFTP on 2 MP datasheet"),
				("Fieldbus", "PROFINET IO, EtherNet/IP, Modbus TCP; OPC UA on 2 MP datasheet"),
				("Serial", "Main RS-232 / RS-422 FD to 115.2 kbit/s; Aux RS-232"),
				("ID-NET", "Datalogic high-speed reader network; pass-through or master/slave"),
				("Connectors", "M12 17-pin power/COM/I-O; M12 X-coded Gigabit Ethernet"),
				("Inputs", "2 opto-coupled, polarity-insensitive; 30 VDC max, 10 mA"),
				("Outputs", "3× NPN/PNP/PP, short-circuit protected; first two opto-coupled on CBX"),
				("Supply", "24 VDC ± 10%"),
				("2 MP current", "14 LED: 0.42 A / 10 W max; 36 LED: 0.62 A / 15 W max"),
				("5 MP current", "No light 0.25 A pk; 36 LED 0.85 A pk; 72 LED 1.30 A pk"),
			],
		),
		(
			"Physical, environment & warranty",
			[
				("2 MP LQL 14 LED", "108.7 × 54 × 55.5 mm (0°); 380 g"),
				("2 MP LQL 36 LED", "115.5 × 126 × 70.3 mm (0°); 650 g"),
				("5 MP no light", "108.7 × 54 × 54.3 mm (0°); 300 g"),
				("5 MP 36 LED", "115.5 × 126 × 117.8 mm (0°); 900 g"),
				("5 MP 72 LED", "145 × 181 × 121.5 mm (0°); 1530 g"),
				("Housing", "Aluminium case, plastic window cover; sulfur-gas resistance on 2 MP"),
				("Sealing", "IP65 and IP67 with sealed IP67 cables and lens cover fitted"),
				("LQL operating", "0 to 45 °C (2 MP liquid lens)"),
				("C-Mount operating", "−10 to 50 °C typical; some 2/5 MP bodies 0 to 50 °C"),
				("Storage", "−20 to 70 °C"),
				("Humidity", "90% non-condensing (5 MP QRG)"),
				("Vibration / shock", "EN 60068-2-6 / -27 / -29 industrial ratings (see QRG)"),
				("Warranty", "2-year factory warranty (DS-MATRIX320-2MP-EN Rev I)"),
			],
		),
	]

	sort = 1
	for group_title, items in groups:
		for label, value in items:
			if len(value) > 140:
				frappe.throw(f"Spec value too long ({len(value)}): {label}")
			spec_rows.append(
				{
					"group_title": group_title,
					"label": label,
					"value": value,
					"sort_order": sort,
				}
			)
			sort += 1
	doc.set("full_specifications", spec_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Conveyor and automated warehouse reading",
				"description": (
					"Inbound, print-and-apply check, depalletising, pallet wrap and outbound "
					"— one or more Matrix 320 heads over the belt."
				),
				"image": warehouse,
				"image_alt": "Warehouse conveyor for Matrix 320 automated barcode reading",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Manufacturing WIP and DPM",
				"description": (
					"Component, WIP and end-of-line traceability including direct part marks "
					"on metal and plastic — C-Mount + colour lighting as required."
				),
				"image": packaging,
				"image_alt": "Manufacturing packaging line traceability with a fixed 2D imager",
				"industry_link": "packaging",
				"sort_order": 2,
			},
			{
				"title": "Food, beverage and secondary pack",
				"description": (
					"Secondary packaging, case codes and print-and-apply verification on "
					"food and beverage lines."
				),
				"image": food,
				"image_alt": "Food and beverage packaging line barcode verification",
				"industry_link": "food-beverage",
				"sort_order": 3,
			},
			{
				"title": "Pharma and UDI packs",
				"description": (
					"Label and 2D codes on cartons and devices. Code-quality metrics "
					"(ISO/IEC and AIM-DPM) are in the software feature set."
				),
				"image": pharma,
				"image_alt": "Pharmaceutical pack identification with a stationary imager",
				"industry_link": "pharmaceutical",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Empower your traceability — official Matrix 320 film",
				"body": (
					"Datalogic’s product film: Empower your Traceability, Boost your "
					"Productivity. Matrix 320 is the compact stationary 2D imager for shop "
					"floor, conveyor and packing-bench work — 2 MP or 5 MP."
				),
				"video_url": VIDEO_URL,
				"image": hero,
				"image_alt": "Datalogic Matrix 320 Series stationary industrial imager",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Matrix 320 5 MP — wider FoV, high DoF",
				"body": (
					"The 5 MP (2560 × 1936) body uses C-Mount lenses, HDR and either a 36-LED "
					"VHP or 72-LED UHP illuminator. Datalogic positions it for distribution, "
					"3PL, retail logistics and shop floors where one reader must cover a large "
					"area or several codes in a single frame.\n\n"
					"DoF is high and largely independent of the focus setting. Specify 5 MP "
					"when 2 MP liquid-lens FoV is not enough — not as a default upgrade."
				),
				"video_url": FIVE_MP_VIDEO,
				"image": applications,
				"image_alt": "Matrix 320 5MP wide-area industrial reading",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Liquid lens, C-Mount and lighting kits",
				"body": (
					"2 MP LQL models refocus 6, 9 or 16 mm electronically — useful when one "
					"object needs several focal planes. C-Mount (2 MP and 5 MP) takes Datalogic "
					"or third-party glass for odd distances and DPM.\n\n"
					"Buy a ready-assembled reader or build from body + lens + light + filter. "
					"UV illuminators are specialist (Risk Group 3) and need PPE; do not treat "
					"them as a standard warehouse kit."
				),
				"video_url": CMOUNT_VIDEO,
				"image": installation,
				"image_alt": "Matrix 320 C-Mount lens and modular illuminator",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "High-speed lines and Premium / X",
				"body": (
					"HDR and short exposure help on fast conveyors. Matrix 320 X keeps the "
					"same mechanics on a newer processor. Premium quad-core (1.6 GHz) is "
					"specified to capture and decode about twice as many images as standard "
					"— use it when multi-recipe or high fps is the constraint, not on every quote."
				),
				"video_url": HIGH_SPEED_VIDEO,
				"image": operation,
				"image_alt": "Matrix 320 reading codes on a high-speed conveyor",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Hands-free packing bench and e-commerce",
				"body": (
					"The same fixed reader can replace a handheld at a pack or sort station: "
					"cross or grid aiming on the goods, ToF range limits so the next carton "
					"is not scanned by accident, and flicker-free continuous light.\n\n"
					"Operators keep both hands on the order. Pair with CODiScan or Skorpio "
					"when the worker still needs a mobile scan further down the process."
				),
				"video_url": HANDS_FREE_VIDEO,
				"image": warehouse,
				"image_alt": "Matrix 320 hands-free packing bench scanning",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "X / Premium overview and Saudi Arabia support",
				"body": (
					"Watch Datalogic’s Matrix 320 X and Premium film for the platform story. "
					"Printechs sizes 2 MP vs 5 MP, LQL vs C-Mount, LED count/colour and "
					"PROFINET vs EtherNet/IP for plants and DCs in Riyadh, Jeddah and Dammam.\n\n"
					"ERP already has a generic Matrix 320 Item and a 710-430 LL16 white X SKU. "
					"Link the configuration you sell on this Website Product — the URL stays "
					"/products/datalogic-matrix-320. Factory warranty is 2 years; EASEOFCARE "
					"extends cover."
				),
				"video_url": PREMIUM_VIDEO,
				"image": hero,
				"image_alt": "Matrix 320 X and Premium stationary readers",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "scan",
				"title": "2 MP vs 5 MP",
				"description": "Confirm FoV, DoF and fps for the belt or bench before locking the sensor.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Optic & lighting",
				"description": "Liquid lens or C-Mount, 14/36/72 LEDs and colour (or IR) matched to the mark.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "PLC & host",
				"description": "PROFINET, EtherNet/IP, Modbus TCP, serial or ID-NET — plus CBX and cable length.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Application test, DL.CODE setup, EASEOFCARE and after-sales in KSA.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set(
		"package_contents",
		[
			{"item_description": "Matrix 320 reader body (2 MP or 5 MP — configuration dependent)", "sort_order": 1},
			{"item_description": "Liquid lens or C-Mount lens (kit dependent; C-Mount often ordered separately)", "sort_order": 2},
			{"item_description": "Internal illuminator 14 / 36 / 72 LED or no-light C-Mount body", "sort_order": 3},
			{"item_description": "Optional CBX connection box, M12 power and X-coded Ethernet cables", "sort_order": 4},
			{"item_description": "DL.CODE software and X-PRESS on-device setup (no extra licence listed)", "sort_order": 5},
		],
	)

	related = [
		row
		for row in (
			related_product_row("datalogic-powerscan-9600", 1),
			related_product_row("datalogic-skorpio-x40-x45", 2),
			related_product_row("datalogic-codiscan", 3),
		)
		if row
	]
	doc.set("related_products", related)
	doc.set("ecosystem_items", [])
	doc.set("capability_items", [])

	doc.set(
		"faq_items",
		[
			{
				"question": "What is the Datalogic Matrix 320?",
				"answer": (
					"A fixed-mount industrial 2D imager for conveyors, machines and packing "
					"benches. It is not a handheld scanner and not a retail checkout device."
				),
				"sort_order": 1,
			},
			{
				"question": "2 MP or 5 MP?",
				"answer": (
					"2 MP (1920 × 1080, 60 fps) is the compact workhorse, including liquid-lens "
					"models. 5 MP (2560 × 1936, 25 fps, HDR) is for wider FoV, multi-code frames "
					"and high DoF — C-Mount only on 5 MP."
				),
				"sort_order": 2,
			},
			{
				"question": "Does every Matrix 320 have a liquid lens?",
				"answer": (
					"No. Electronic focus (6 / 9 / 16 mm) is on 2 MP LQL models. 2 MP and 5 MP "
					"C-Mount bodies use manual C-Mount glass."
				),
				"sort_order": 3,
			},
			{
				"question": "What industrial protocols are onboard?",
				"answer": (
					"Gigabit Ethernet with TCP/IP, FTP, PROFINET IO, EtherNet/IP and Modbus TCP, "
					"plus RS-232/422 and ID-NET. OPC UA and SFTP are listed on the 2 MP datasheet."
				),
				"sort_order": 4,
			},
			{
				"question": "Are Premium and X the same as a standard Matrix 320?",
				"answer": (
					"X is a newer processing platform in the same housing. Premium adds a "
					"1.6 GHz quad-core versus 0.9 GHz standard and is specified for roughly "
					"2× images / half decode time. Quote them only when the application needs it."
				),
				"sort_order": 5,
			},
			{
				"question": "Is there an Item code in ERP yet?",
				"answer": (
					"This page is published without an Item link. ERP already has generic "
					"RET.SYS.DLG.3743 and 710-430 LL16 white X RET.SYS.DLG.4799, plus CBX/cables. "
					"Link the SKU you sell under ERP Item Link; the URL does not change."
				),
				"sort_order": 6,
			},
			{
				"question": "What is the warranty?",
				"answer": (
					"The official 2 MP datasheet specifies a 2-year factory warranty. EASEOFCARE "
					"3- or 5-year plans extend service."
				),
				"sort_order": 7,
			},
		],
	)

	doc.flags.ignore_permissions = True
	if doc.is_new():
		doc.insert()
	else:
		doc.save()
	frappe.db.commit()
	return doc.name
