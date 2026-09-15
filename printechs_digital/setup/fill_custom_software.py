# Copyright (c) 2026, Printechs and contributors
"""Create or update Custom Software Development.

Content follows docs/Printechs_Custom_Software_Development_Page_Content_Plan.docx.
Features are described as capabilities Printechs can develop — not a fixed SKU list.
"""

from io import BytesIO
from pathlib import Path
from urllib.request import Request, urlopen

from PIL import Image

import frappe


SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")
SOFTWARE_DIRS = (
	Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/software"),
	Path("/home/erpnext/frappe-bench/apps/printechs_digital/frontend/printechs-web/public/images/software"),
)
UA = "Mozilla/5.0 (compatible; Printechs/1.0)"
SLUG = "custom-software-development"
VAN_SALES = "/software/van-sales"

SECTION_ORDER = [
	"benefits",
	"overview",
	"product_tour",
	"applications",
	"key_features",
	"content_sections",
	"icon_specifications",
	"localization",
	"process_steps",
	"ecosystem",
	"related_products",
	"support",
	"faqs",
]

IMAGES = {
	"software-custom-software-development.jpg": (
		"https://images.pexels.com/photos/6169668/pexels-photo-6169668.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"custom-van-load.jpg": (
		"https://images.pexels.com/photos/6169056/pexels-photo-6169056.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"custom-van-stock.jpg": (
		"https://images.unsplash.com/photo-1580674285054-bed31e145f59?auto=format&fit=crop&w=2000&q=80"
	),
	"custom-shelf.jpg": (
		"https://images.unsplash.com/photo-1445205170230-053b83016050?auto=format&fit=crop&w=2000&q=80"
	),
	"custom-supermarket.jpg": (
		"https://images.unsplash.com/photo-1578916171728-46686eac8d58?auto=format&fit=crop&w=2000&q=80"
	),
	"custom-scale.jpg": (
		"https://images.unsplash.com/photo-1488459716781-31db52582fe9?auto=format&fit=crop&w=2000&q=80"
	),
	"custom-seafood.jpg": (
		"https://images.unsplash.com/photo-1615141982883-c7ad0e69fd62?auto=format&fit=crop&w=2000&q=80"
	),
	"custom-inventory.jpg": (
		"https://images.pexels.com/photos/4484078/pexels-photo-4484078.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"custom-warehouse.jpg": (
		"https://images.pexels.com/photos/4483610/pexels-photo-4483610.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"custom-van-route.jpg": (
		"https://images.pexels.com/photos/4391470/pexels-photo-4391470.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
}


def _save_wide(im: Image.Image, filename: str) -> str:
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
	target = SITE_FILES / filename
	im.save(target, "JPEG", quality=90, optimize=True)
	for folder in SOFTWARE_DIRS:
		folder.mkdir(parents=True, exist_ok=True)
		im.save(folder / filename, "JPEG", quality=90, optimize=True)
	return f"/files/{filename}"


def download_wide(filename: str, url: str) -> str:
	target = SITE_FILES / filename
	if target.exists():
		return f"/files/{filename}"
	request = Request(url, headers={"User-Agent": UA})
	with urlopen(request, timeout=45) as response:
		data = response.read()
	if len(data) < 2000:
		frappe.throw(f"Download too small ({len(data)} bytes): {url}")
	im = Image.open(BytesIO(data)).convert("RGB")
	return _save_wide(im, filename)


def media() -> dict[str, str]:
	return {name: download_wide(name, url) for name, url in IMAGES.items()}


def published_name(slug: str) -> str | None:
	return frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")


def get_or_create(hero: str):
	name = frappe.db.get_value("Website Product", {"slug": SLUG}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "Custom Software Development"
	doc.display_name = "Custom Software Development"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Custom Software"
	doc.short_description = (
		"Purpose-built applications that connect people, ERP/POS, handhelds, printers and scales."
	)
	doc.long_description = "<p>Custom Software Development</p>"
	doc.hero_image = hero
	doc.hero_image_alt = "Field team loading a delivery van with a handheld application"
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_custom_software():
	m = media()
	hero = m["software-custom-software-development.jpg"]
	doc = get_or_create(hero)
	van_load = m["custom-van-load.jpg"]
	van_stock = m["custom-van-stock.jpg"]
	shelf = m["custom-shelf.jpg"]
	supermarket = m["custom-supermarket.jpg"]
	scale = m["custom-scale.jpg"]
	seafood = m["custom-seafood.jpg"]
	inventory = m["custom-inventory.jpg"]
	warehouse = m["custom-warehouse.jpg"]
	van_route = m["custom-van-route.jpg"]

	erpnext_image = "/files/software-erpnext.jpg"
	pos_image = "/files/software-modern-pos.jpg"
	wms_image = "/files/software-warehouse-management-system.jpg"
	api_image = "/files/software-api-integration.jpg"
	mobile_image = "/files/software-mobile-applications.jpg"

	doc.website_product_name = "Custom Software Development"
	doc.display_name = "Custom Software Development"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	if frappe.db.exists("Brand", "Printechs"):
		doc.brand = "Printechs"
	doc.category = "Custom Software"
	doc.subcategory = "Operational Applications"
	doc.category_label = "CUSTOM SOFTWARE DEVELOPMENT"
	doc.tagline = "Software that fits the way your business really works"
	doc.short_description = (
		"Printechs designs custom applications around your workflow — van sales, shelf-label "
		"printing, platform scales, mobile inventory and in-store price checkers — connected "
		"to the ERP, POS and devices you already use."
	)
	doc.long_description = (
		"<p>Printechs does not only write software. We build applications that connect people, "
		"ERP or POS systems, enterprise handhelds, mobile printers, platform scales and "
		"shop-floor operations.</p>"
		"<p>Some operational problems cannot be solved by installing another standard package. "
		"A field team needs offline invoices. A store team needs to reprint a hundred shelf "
		"labels on the floor. A cold store needs the weight from the scale — not a number "
		"typed later at a desktop.</p>"
		"<p>We develop the missing workflow and integrate it through the interfaces your "
		"system or device already provides: APIs, web services, databases, SDKs, serial or "
		"TCP/IP. The aim is not to replace a working system. It is to connect the work your "
		"staff already do.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Delivery van and field team using a handheld while loading cartons — custom operational software"
	)
	doc.hero_trust_chips = (
		"Van sales & field sales\n"
		"Shelf-label printing\n"
		"Platform scale integration\n"
		"Mobile inventory\n"
		"Price checker & promotion"
	)
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Discuss Your Software Requirement"
	doc.hero_primary_cta_href = "/contact"
	doc.hero_secondary_cta_label = "See Our Custom Solutions"
	doc.hero_secondary_cta_href = "#applications"
	doc.show_demo_cta = 1
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.index_page = 1
	doc.collapsible_full_specs = 1
	doc.enable_product_tour = 0
	doc.story_heading = "Custom software built around your operation"
	doc.visual_story_heading = "From mobile users to shop-floor devices"
	doc.card_title = "Custom Software Development"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Van sales, shelf labels, scales, mobile inventory and price checkers — built around your workflow."
	)
	doc.card_image = hero
	doc.final_cta_heading = (
		"Have an operational problem that standard software does not solve?"
	)
	doc.final_cta_description = (
		"Tell Printechs what your staff currently do manually, which system you already use "
		"and which device or machine is involved. We can study the workflow and design a "
		"custom application or integration around it."
	)
	doc.final_cta_primary_label = "Discuss Your Requirement"
	doc.final_cta_primary_href = "/contact"
	doc.final_cta_secondary_label = "Request a Workflow Assessment"
	doc.final_cta_secondary_href = "/request-quote"
	doc.meta_title = (
		"Custom Software Development Saudi Arabia | Mobile, ERP & Device Integration | Printechs"
	)
	doc.meta_description = (
		"Custom software development in Saudi Arabia for van sales, mobile inventory, "
		"shelf label printing, platform scale integration, price checkers and "
		"ERP/POS-connected operational applications."
	)
	doc.implementation_heading = "Software + devices + operations — one partner"
	doc.implementation_cta_label = "Discuss Your Requirement"
	doc.implementation_cta_href = "/contact"
	doc.published = 1

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(SECTION_ORDER, start=1)],
	)

	doc.connection_heading = "Built around your existing ERP, POS and devices"
	doc.connection_center_label = (
		"Printechs custom application — people · ERP/POS · handhelds · printers · scales"
	)
	doc.set(
		"connection_items",
		[
			{"title": "ERP / POS", "href": "/software/erpnext", "sort_order": 1},
			{"title": "REST API", "href": "/software/api-integration", "sort_order": 2},
			{"title": "Web services", "sort_order": 3},
			{"title": "SQL / database", "sort_order": 4},
			{"title": "Barcode & RFID", "sort_order": 5},
			{"title": "Mobile printers", "sort_order": 6},
			{"title": "Electronic scales", "sort_order": 7},
			{"title": "Enterprise Android", "sort_order": 8},
		],
	)

	doc.set(
		"benefits",
		[
			{
				"icon": "device",
				"title": "Enterprise mobility",
				"description": "Rugged handhelds and mobile apps for store, warehouse and field users.",
				"sort_order": 1,
			},
			{
				"icon": "print",
				"title": "Printing & Auto-ID",
				"description": "Barcode scanning, shelf and carton labels, RFID and item identification.",
				"sort_order": 2,
			},
			{
				"icon": "inventory",
				"title": "Weighing integration",
				"description": "Capture operational weight from a connected platform scale where the interface exists.",
				"sort_order": 3,
			},
			{
				"icon": "store",
				"title": "Retail self-service",
				"description": "Price-check and customer-facing kiosk applications on devices such as the Zebra CC6000.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Field & van sales",
				"image": hero,
				"image_alt": "Sales team at a delivery van using a handheld while loading cartons",
				"caption": "Take ERP customers, prices and van stock onto the road — including offline.",
				"sort_order": 1,
			},
			{
				"label": "Shop-floor labels",
				"image": shelf,
				"image_alt": "Fashion retail rail where shelf and garment prices must match POS",
				"caption": "Scan, confirm the ERP/POS price and print the new shelf label on the floor.",
				"sort_order": 2,
			},
			{
				"label": "Scale receiving",
				"image": scale,
				"image_alt": "Fresh produce counter with a hanging scale used for operational weight",
				"caption": "Read the stable weight from the scale — then print the carton barcode.",
				"sort_order": 3,
			},
			{
				"label": "Warehouse mobility",
				"image": inventory,
				"image_alt": "Warehouse operator with a tablet in the aisle for receive, transfer and count",
				"caption": "The transaction is captured where the carton actually moves.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"applications",
		[
			{
				"title": "Van sales & field sales",
				"description": "Orders, invoices, collections, van stock and offline field operations.",
				"image": van_route,
				"image_alt": "Small delivery van used for field sales and route distribution",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Mobile shelf-label printing",
				"description": "Scan a product, verify or update the price and print the new shelf label immediately.",
				"image": supermarket,
				"image_alt": "Supermarket aisle where hundreds of shelf labels may need a same-day price change",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Platform scale integration",
				"description": "Capture actual shipment weight from the scale and create the barcode label.",
				"image": scale,
				"image_alt": "Weighing at a fresh-food counter connected to the receiving application",
				"industry_link": "food-beverage",
				"sort_order": 3,
			},
			{
				"title": "Mobile inventory operations",
				"description": "Receive, transfer, count, audit and move stock on enterprise handhelds.",
				"image": warehouse,
				"image_alt": "Warehouse racking where operators can scan product and location barcodes",
				"industry_link": "warehouse-logistics",
				"sort_order": 4,
			},
			{
				"title": "Price checker & digital promotion",
				"description": "Customer self-service price lookup from ERP/POS, with idle-screen advertising.",
				"image": shelf,
				"image_alt": "Fashion store floor where a kiosk can show price and campaign content",
				"industry_link": "fashion",
				"sort_order": 5,
			},
		],
	)

	doc.key_features_heading = "Operational applications we can build"
	doc.set(
		"key_features",
		[
			{
				"title": "Van sales & field sales",
				"icon": "device",
				"description": (
					"A salesperson starts the day with customer, price and van-stock data. "
					"At the customer they create the sale, record payment and share the invoice. "
					"Online it posts to ERP immediately; offline it queues and syncs later."
				),
				"sort_order": 1,
			},
			{
				"title": "Mobile shelf-label printing",
				"icon": "print",
				"description": (
					"Scan the barcode → retrieve description and ERP/POS price → confirm or "
					"select the authorised promotion → print on a paired mobile printer → "
					"replace the label on the shelf. The same flow restores the regular price."
				),
				"sort_order": 2,
			},
			{
				"title": "Platform scale receiving",
				"icon": "inventory",
				"description": (
					"Place the carton on the scale → the application reads the stable weight → "
					"the operator selects item, supplier, batch or PO → a barcode label prints → "
					"receiving posts to ERP/WMS. Designed around serial, TCP/IP or the vendor SDK."
				),
				"sort_order": 3,
			},
			{
				"title": "Mobile inventory & warehouse",
				"icon": "scan",
				"description": (
					"Receive, putaway, transfer, pick, pack, cycle count and audit on a rugged "
					"handheld — at the location, not later at a desktop. Offline where required."
				),
				"sort_order": 4,
			},
			{
				"title": "Price checker & promotion kiosk",
				"icon": "store",
				"description": (
					"Idle screen shows campaign artwork. The shopper scans a barcode. The kiosk "
					"reads ERP/POS and shows name, regular and offer price. After a timeout it "
					"returns to advertising. Typical hardware: Zebra CC6000."
				),
				"sort_order": 5,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Take your ERP to the road",
				"body": (
					"Printechs can develop a van-sales application for distributors, wholesalers "
					"and mobile sales teams. It can integrate with ERPNext or another ERP through "
					"APIs, web services, staging tables or an approved database interface.\n\n"
					"Typical capabilities include customer and item sync, van stock, quotations "
					"and invoices, credit and collections, returns, routes, GPS where required, "
					"and offline capture with later synchronisation."
				),
				"image": van_stock,
				"image_alt": "Loaded delivery van where van stock, invoices and collections should stay in ERP",
				"link_label": "Explore Printechs Van Sales",
				"link_href": VAN_SALES,
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Change shelf prices in minutes — from the shop floor",
				"body": (
					"During promotions and large price revisions, store teams often need to change "
					"hundreds of shelf labels quickly. Printechs can build a mobile application "
					"for rugged Datalogic or Zebra devices that scans the product, retrieves the "
					"current ERP/POS price, confirms the authorised price and prints the new "
					"label on a paired mobile printer.\n\n"
					"Barcode-driven selection reduces typing. Central templates and permissions "
					"keep store-specific and offer prices under control."
				),
				"image": supermarket,
				"image_alt": "Supermarket shelves where price labels must match the till",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Capture weight directly from the scale — no manual entry",
				"body": (
					"For meat, seafood, food distribution and cold stores, Printechs can connect "
					"custom software to an electronic platform scale. The carton goes on the "
					"scale; the application reads the stable weight; the operator selects item "
					"and batch; a barcode label prints; stock posts to ERP/WMS.\n\n"
					"Gross, tare and net weight, lot, expiry, supplier, PO, carton ID, destination "
					"and operator can be captured when the process needs them. The interface "
					"follows what the scale actually offers — serial/RS-232, TCP/IP, vendor "
					"protocol or SDK."
				),
				"image": seafood,
				"image_alt": "Seafood on ice — a typical weight-based receiving line for scale integration",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Put warehouse transactions in the operator's hands",
				"body": (
					"Printechs develops mobile warehouse and inventory applications for rugged "
					"handhelds. Instead of paper or a later desktop booking, staff scan product "
					"and location where the physical movement happens.\n\n"
					"Functions that can be included: goods receipt, putaway, transfers, pick and "
					"pack, physical and cycle count, audit, item and bin lookup, label reprint, "
					"batch or serial capture, and real-time or offline sync with ERP or WMS."
				),
				"image": inventory,
				"image_alt": "Operator in the warehouse aisle capturing receive, transfer or count on a handheld",
				"link_label": "See Warehouse Management",
				"link_href": "/software/warehouse-management-system",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "One device for price checking and digital advertising",
				"body": (
					"Printechs can develop a customer-facing price-checker application for "
					"interactive kiosks such as the Zebra CC6000. The shopper scans an item; "
					"the screen shows the latest ERP/POS price and configured product details.\n\n"
					"When idle, the same screen can show promotional images and campaign artwork. "
					"Optional functions include item image, member price, stock or aisle hints, "
					"Arabic and English, loyalty lookup and a call-for-assistance workflow — "
					"configured to the retailer."
				),
				"image": shelf,
				"image_alt": "Fashion store aisle where a price-checker kiosk can show price and campaign content",
				"sort_order": 5,
			},
		],
	)

	doc.process_heading = "How we design a custom application"
	doc.process_subheading = (
		"The exact screens and device list depend on your ERP, the handheld or scale "
		"interface, and the workflow we survey on site."
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "01 Understand",
				"title": "Watch the work your staff already do",
				"description": (
					"We map the manual steps, the system you already use and the device or "
					"machine in the path — before we propose screens."
				),
				"sort_order": 1,
			},
			{
				"group_title": "02 Connect",
				"title": "Use the interfaces that already exist",
				"description": (
					"APIs, web services, staging tables, databases, SDKs, serial or TCP/IP — "
					"we design around what the ERP and the device can actually expose."
				),
				"sort_order": 2,
			},
			{
				"group_title": "03 Develop",
				"title": "Build the missing operational workflow",
				"description": (
					"A mobile app, kiosk, scale service or van-sales client — configured for "
					"your prices, permissions, label formats and offline rules."
				),
				"sort_order": 3,
			},
			{
				"group_title": "04 Support",
				"title": "Go live with the hardware you already run",
				"description": (
					"Printechs supplies and supports the handhelds, printers, scales and kiosks "
					"from Riyadh, Jeddah and Dammam — the same team that wrote the application."
				),
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "integration",
				"title": "ERP / POS",
				"description": "ERPNext or the platform you already run — via the published interface",
				"sort_order": 1,
			},
			{
				"icon": "cloud",
				"title": "REST & web services",
				"description": "APIs, SOAP and webhooks when the vendor provides them",
				"sort_order": 2,
			},
			{
				"icon": "report",
				"title": "SQL / staging",
				"description": "Database or staging-table integration when a live API is not available",
				"sort_order": 3,
			},
			{
				"icon": "scan",
				"title": "Barcode & RFID",
				"description": "Handheld, fixed and portal identification in store and warehouse",
				"sort_order": 4,
			},
			{
				"icon": "print",
				"title": "Mobile printers",
				"description": "Shelf, carton and invoice labels printed next to the work",
				"sort_order": 5,
			},
			{
				"icon": "device",
				"title": "Enterprise Android",
				"description": "Datalogic, Zebra and kiosk devices we already supply in Saudi Arabia",
				"sort_order": 6,
			},
		],
	)

	doc.localization_heading = "Industries where these applications are used"
	doc.localization_body = (
		"The five solution families are easiest to picture in the operations Printechs "
		"already supports across Saudi Arabia — retail floors, distribution vans, "
		"weight-based warehouses and manufacturing stores."
	)
	doc.localization_chips = (
		"Fashion & apparel\n"
		"Supermarkets & hypermarkets\n"
		"Perfume & cosmetics\n"
		"Food distribution\n"
		"Meat & seafood warehouses\n"
		"Cold storage\n"
		"Wholesale & distribution\n"
		"Pharmaceutical distribution\n"
		"Manufacturing stores"
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "integration",
				"title": "Business software",
				"description": "ERP, POS, WMS, databases, APIs and custom workflows on one project.",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Enterprise mobility",
				"description": "Rugged handhelds and mobile applications for store, warehouse and field users.",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "Printing & Auto-ID",
				"description": "Barcode, shelf and carton labels, RFID and item identification.",
				"sort_order": 3,
			},
			{
				"icon": "store",
				"title": "Retail self-service",
				"description": "Price-checking and customer-facing kiosk applications, including Zebra CC6000.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Is this a fixed product, or do you design around our workflow?",
				"answer": (
					"These are solution families Printechs can develop. The exact screens, "
					"devices and fields depend on your ERP, the handheld or scale interface, "
					"and the process we survey. We use wording such as can develop and can be "
					"configured on purpose — it is not a boxed SKU."
				),
				"sort_order": 1,
			},
			{
				"question": "Do the applications only work with ERPNext?",
				"answer": (
					"No. We can integrate with the ERP, POS, WMS or legacy application you "
					"already use, subject to the interfaces that system makes available — "
					"REST/SOAP, web services, webhooks, staging tables, databases or SDKs."
				),
				"sort_order": 2,
			},
			{
				"question": "Can van sales work without a continuous internet connection?",
				"answer": (
					"Yes. A van-sales application can capture transactions offline and "
					"synchronise with the central system when connectivity returns. See also "
					"Printechs Van Sales."
				),
				"sort_order": 3,
			},
			{
				"question": "Which devices do you build for?",
				"answer": (
					"Typical projects use rugged Datalogic or Zebra handhelds, mobile printers, "
					"electronic platform scales and kiosks such as the Zebra CC6000. We design "
					"for the device you already own when the SDK or protocol is available."
				),
				"sort_order": 4,
			},
			{
				"question": "Why Printechs instead of a software house that only writes apps?",
				"answer": (
					"We work across enterprise software, retail technology, Auto-ID, warehouse "
					"mobility, weighing and industrial equipment. That lets us design the "
					"complete flow — the screen, the scan, the label and the ERP posting."
				),
				"sort_order": 5,
			},
		],
	)

	related = []
	for sort, slug, label, summary, href, image in (
		(1, "api-integration", "API Integration", "Connect the custom app to ERP, devices and partners", "/software/api-integration", api_image),
		(2, "erpnext", "ERPNext", "The business system many of these apps post into", "/software/erpnext", erpnext_image),
		(3, "modern-pos", "Modern POS", "Store prices the shelf-label and kiosk apps should match", "/software/modern-pos", pos_image),
		(4, "warehouse-management-system", "Warehouse Management", "Desktop WMS the handheld inventory app can extend", "/software/warehouse-management-system", wms_image),
		(5, "mobile-applications", "Mobile Applications", "Packaged and custom mobile apps for the floor", "/software/mobile-applications", mobile_image),
		(6, "van-sales", "Van Sales", "Field sales, van stock and collections on the road", VAN_SALES, hero),
	):
		name = published_name(slug)
		if not name:
			continue
		related.append(
			{
				"related_website_product": name,
				"display_name_override": label,
				"summary_override": summary,
				"href": href,
				"image": image,
				"sort_order": sort,
			}
		)
	doc.set("ecosystem_items", related)
	doc.set("related_products", related)

	doc.set("downloads", [])
	doc.set("package_contents", [])
	doc.set("full_specifications", [])

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
