# Copyright (c) 2026, Printechs and contributors
"""Create or update the VAN Sales Website Product.

URL: https://printechs.com/software/van-sales
GPS / location tracking is optional only — not advertised as a standard feature.
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
SLUG = "van-sales"
PATH = "/software/van-sales"

SECTION_ORDER = [
	"benefits",
	"overview",
	"product_tour",
	"process_steps",
	"key_features",
	"content_sections",
	"capability_modules",
	"applications",
	"icon_specifications",
	"localization",
	"reports",
	"dashboard",
	"ecosystem",
	"related_products",
	"support",
	"faqs",
]

# Unique operational photographs — none reused from other software pages.
IMAGES = {
	"software-van-sales.jpg": (
		"https://images.pexels.com/photos/5025669/pexels-photo-5025669.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-stock.jpg": (
		"https://images.pexels.com/photos/6169662/pexels-photo-6169662.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-load.jpg": (
		"https://images.pexels.com/photos/4391476/pexels-photo-4391476.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-warehouse.jpg": (
		"https://images.pexels.com/photos/4481258/pexels-photo-4481258.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-retail.jpg": (
		"https://images.pexels.com/photos/264636/pexels-photo-264636.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-mobile.jpg": (
		"https://images.pexels.com/photos/6169659/pexels-photo-6169659.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-produce.jpg": (
		"https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=2000&q=80"
	),
	"van-bakery.jpg": (
		"https://images.pexels.com/photos/205961/pexels-photo-205961.jpeg?auto=compress&cs=tinysrgb&w=2000"
	),
	"van-salon.jpg": (
		"https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=2000&q=80"
	),
	"van-parts.jpg": (
		"https://images.pexels.com/photos/162553/keys-workshop-mechanic-tools-162553.jpeg?auto=compress&cs=tinysrgb&w=2000"
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
	doc.website_product_name = "VAN Sales"
	doc.display_name = "Van Sales Software for Mobile Sales, Delivery & Collection"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Field Sales Software"
	doc.short_description = (
		"Mobile field sales, delivery, invoicing and collection — connected to ERPNext."
	)
	doc.long_description = "<p>VAN Sales</p>"
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Sales van parked at a customer location while the representative delivers cartons"
	)
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_van_sales():
	m = media()
	hero = m["software-van-sales.jpg"]
	doc = get_or_create(hero)
	stock = m["van-stock.jpg"]
	load = m["van-load.jpg"]
	warehouse = m["van-warehouse.jpg"]
	retail = m["van-retail.jpg"]
	mobile = m["van-mobile.jpg"]
	produce = m["van-produce.jpg"]
	bakery = m["van-bakery.jpg"]
	salon = m["van-salon.jpg"]
	parts = m["van-parts.jpg"]

	erpnext_image = "/files/software-erpnext.jpg"
	zatca_image = "/files/software-zatca-integration.jpg"
	wms_image = "/files/software-warehouse-management-system.jpg"
	custom_image = "/files/software-custom-software-development.jpg"
	mobile_image = "/files/software-mobile-applications.jpg"
	api_image = "/files/software-api-integration.jpg"

	doc.website_product_name = "VAN Sales"
	doc.display_name = "Van Sales Software for Mobile Sales, Delivery & Collection"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	if frappe.db.exists("Brand", "Printechs"):
		doc.brand = "Printechs"
	doc.category = "Field Sales Software"
	doc.subcategory = "Distribution"
	doc.category_label = "VAN SALES SOFTWARE SAUDI ARABIA"
	doc.tagline = (
		"Mobile sales, delivery, invoicing and collection — fully integrated with ERPNext"
	)
	doc.short_description = (
		"Take customer, product, pricing and van stock on the road. Sell, deliver, "
		"invoice, collect and print from one mobile application connected to ERPNext."
	)
	doc.long_description = (
		"<p>Take your sales operation beyond the office with <strong>Printechs VAN Sales</strong>, "
		"a mobile field-sales and distribution application for companies that run sales vans, "
		"delivery vehicles and field teams.</p>"
		"<p>The application connects directly with <strong>ERPNext</strong>. Each sales van can "
		"be managed as an individual warehouse, so stock loaded into the vehicle stays under "
		"central control. Sales representatives carry customer, product, pricing and stock "
		"information with them — and can keep working when mobile internet is unavailable.</p>"
		"<p>From taking an order and delivering product to generating the invoice, collecting "
		"payment and printing at the customer location, the field transaction stays on one "
		"device. Invoices follow the company's configured <strong>ZATCA</strong> e-invoicing "
		"workflow in ERPNext before the printed copy is handed over.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"White delivery van at a customer street while the salesperson carries cartons from the vehicle"
	)
	doc.hero_trust_chips = "ERP Connected\nMobile\nOffline Ready\nZATCA Integrated"
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Request a VAN Sales Demo"
	doc.hero_primary_cta_href = "/products/van-sales/demo"
	doc.hero_secondary_cta_label = "Discuss Your Distribution Workflow"
	doc.hero_secondary_cta_href = "/contact"
	doc.show_demo_cta = 1
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.index_page = 1
	doc.collapsible_full_specs = 1
	doc.enable_product_tour = 0
	doc.story_heading = "One mobile application for the complete van sales cycle"
	doc.visual_story_heading = "From van stock to the customer counter"
	doc.card_title = "VAN Sales"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Mobile field sales, van inventory, delivery, invoices, collections and printing — on ERPNext."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Take your ERPNext sales operation to the road"
	doc.final_cta_description = (
		"Give the team the ability to sell, deliver, invoice, collect and print from anywhere — "
		"while ERPNext stays at the centre of the business. Whether you operate five vans or a "
		"nationwide fleet, Printechs configures the workflow around your products, customers "
		"and warehouse structure."
	)
	doc.final_cta_primary_label = "Request a VAN Sales Demo"
	doc.final_cta_primary_href = "/products/van-sales/demo"
	doc.final_cta_secondary_label = "Talk to Printechs"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Van Sales Software Saudi Arabia | ERPNext & ZATCA | Printechs"
	doc.meta_description = (
		"Van Sales software for Saudi Arabia integrated with ERPNext and ZATCA. "
		"Manage van stock, orders, delivery, invoices, payments, offline sales, "
		"barcode scanning and mobile printing."
	)
	doc.implementation_heading = "Built around your distribution process"
	doc.implementation_cta_label = "Discuss Your Distribution Workflow"
	doc.implementation_cta_href = "/contact"
	doc.published = 1

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(SECTION_ORDER, start=1)],
	)

	doc.connection_heading = "Your ERPNext sales operation on the road"
	doc.connection_center_label = (
		"Van → Mobile device → ERPNext → ZATCA → Printed invoice → Collection"
	)
	doc.set(
		"connection_items",
		[
			{"title": "ERPNext master data", "href": "/software/erpnext", "sort_order": 1},
			{"title": "Van warehouse", "sort_order": 2},
			{"title": "Mobile VAN Sales app", "sort_order": 3},
			{"title": "Order · delivery · invoice", "sort_order": 4},
			{"title": "ZATCA via ERPNext", "href": "/software/zatca-integration", "sort_order": 5},
			{"title": "Mobile print", "sort_order": 6},
			{"title": "Payment collection", "sort_order": 7},
			{"title": "ERPNext accounts", "href": "/software/erpnext", "sort_order": 8},
		],
	)

	doc.set(
		"benefits",
		[
			{
				"icon": "integration",
				"title": "ERPNext integrated",
				"description": "Customers, items, prices, stock and invoices stay on the same ERP ledger the office already runs.",
				"sort_order": 1,
			},
			{
				"icon": "inventory",
				"title": "Van-level inventory",
				"description": "Each vehicle is an ERPNext warehouse — load, sell, return and reconcile from that stock book.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Online and offline",
				"description": "No internet? Keep working. Connection restored? Synchronise pending transactions with ERPNext.",
				"sort_order": 3,
			},
			{
				"icon": "print",
				"title": "Invoice, ZATCA, print",
				"description": "Field invoices post to ERPNext, follow the configured ZATCA workflow, then print at the customer.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Synchronise the van",
				"image": mobile,
				"image_alt": "Field user checking a tablet beside cartons loaded in the sales van",
				"caption": "Start the day with synchronised customers, products, prices and van inventory.",
				"sort_order": 1,
			},
			{
				"label": "Visit the customer",
				"image": retail,
				"image_alt": "Retail produce aisle — a typical direct-store-delivery customer location",
				"caption": "Search the customer, review the account and take the order at the store.",
				"sort_order": 2,
			},
			{
				"label": "Sell from van stock",
				"image": stock,
				"image_alt": "Open sales van packed with cartons ready for delivery",
				"caption": "Scan or search products and issue quantity from that van's ERPNext warehouse.",
				"sort_order": 3,
			},
			{
				"label": "Load and reconcile",
				"image": load,
				"image_alt": "Operator placing a carton into the van during morning load",
				"caption": "Stock transferred from the central warehouse becomes that vehicle's available inventory.",
				"sort_order": 4,
			},
		],
	)

	doc.process_heading = "Typical daily workflow"
	doc.process_subheading = (
		"Designed around the working day of a field salesperson — from morning load "
		"to invoice, collection and the ERPNext update."
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "01 Load",
				"title": "Transfer stock to the van warehouse",
				"description": (
					"ERPNext moves inventory from the central warehouse into VAN-001, VAN-002 "
					"and the rest of the fleet."
				),
				"sort_order": 1,
			},
			{
				"group_title": "02 Sync",
				"title": "Synchronise the mobile device",
				"description": (
					"Customers, items, barcodes, prices, tax and van stock download to the handheld."
				),
				"sort_order": 2,
			},
			{
				"group_title": "03 Sell",
				"title": "Visit, order or sell direct",
				"description": (
					"Take an order, deliver against an existing order, or complete a direct van sale."
				),
				"sort_order": 3,
			},
			{
				"group_title": "04 Invoice",
				"title": "Generate the invoice through ERPNext / ZATCA",
				"description": (
					"The mobile sale posts to ERPNext. The invoice follows the configured "
					"ZATCA e-invoicing workflow. The response returns to the device."
				),
				"sort_order": 4,
			},
			{
				"group_title": "05 Print",
				"title": "Print and collect at the customer",
				"description": (
					"A paired mobile printer produces the customer invoice. Payment is recorded "
					"on the same device."
				),
				"sort_order": 5,
			},
			{
				"group_title": "06 Update",
				"title": "Synchronise back to ERPNext",
				"description": (
					"Orders, invoices, payments, returns and stock movements update the central books."
				),
				"sort_order": 6,
			},
		],
	)

	doc.key_features_heading = "Core VAN Sales capabilities"
	doc.set(
		"key_features",
		[
			{
				"title": "ERPNext master-data synchronisation",
				"icon": "integration",
				"description": (
					"Customers, items, barcodes, UOMs, price lists, tax rules, van stock and "
					"salesperson assignment download from ERPNext so the field team works from "
					"centrally controlled information."
				),
				"sort_order": 1,
			},
			{
				"title": "Each van is an ERPNext warehouse",
				"icon": "inventory",
				"description": (
					"VAN-001, VAN-002 and the rest of the fleet keep their own stock book. "
					"Load, sell, return and remaining quantity stay visible to the office."
				),
				"sort_order": 2,
			},
			{
				"title": "Work online or offline",
				"icon": "cloud",
				"description": (
					"Search customers, scan products, check van stock, take orders, prepare "
					"deliveries and record collections without a live connection. Pending "
					"transactions synchronise when the network returns."
				),
				"sort_order": 3,
			},
			{
				"title": "Orders, delivery and direct van sales",
				"icon": "store",
				"description": (
					"Order today and deliver later, sell immediately from van stock, deliver "
					"against an existing sales order, or process a partial quantity — configured "
					"to the distribution model."
				),
				"sort_order": 4,
			},
			{
				"title": "Mobile invoice, ZATCA and print",
				"icon": "print",
				"description": (
					"The invoice posts to ERPNext, follows the company's ZATCA workflow, returns "
					"to the application and prints on a paired mobile printer at the customer."
				),
				"sort_order": 5,
			},
			{
				"title": "Payment collection and barcode scanning",
				"icon": "scan",
				"description": (
					"Record cash or credit collections against the invoice and identify products "
					"with the scanner on a Datalogic or Zebra enterprise handheld."
				),
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Core Module",
				"heading": "Each van becomes a warehouse in ERPNext",
				"body": (
					"Stock transferred from the central warehouse into VAN-001, VAN-002 or VAN-003 "
					"becomes that vehicle's available inventory.\n\n"
					"Management keeps control of stock loaded into each vehicle, products sold "
					"from each van, remaining quantity, transfers, salesperson responsibility, "
					"returned products and daily van reconciliation — even while goods are "
					"physically moving across the fleet."
				),
				"image": stock,
				"image_alt": "Loaded van warehouse — cartons assigned to one sales vehicle",
				"sort_order": 1,
			},
			{
				"section_type": "Core Module",
				"heading": "No internet? Keep working. Internet restored? Synchronise.",
				"body": (
					"Required information is stored on the device so authorised users can search "
					"customers, scan products, view prices, check van stock, take orders, prepare "
					"deliveries, generate sales and record collections without a live ERP link.\n\n"
					"When a connection is available, orders, invoices, payments, stock movement "
					"and master-data updates can communicate with ERPNext immediately. "
					"Synchronisation status shows whether a transaction has reached ERPNext or "
					"is still pending."
				),
				"image": mobile,
				"image_alt": "Salesperson using a tablet beside van cartons while working in the field",
				"sort_order": 2,
			},
			{
				"section_type": "Core Module",
				"heading": "Mobile sale → ERPNext → ZATCA → printed invoice",
				"body": (
					"For Saudi operations, VAN Sales works with the company's ERPNext ZATCA "
					"e-invoicing integration.\n\n"
					"The transaction is transmitted to ERPNext. ERPNext generates and processes "
					"the electronic invoice. The invoice follows the configured ZATCA-compliant "
					"workflow. The response returns to the application. The salesperson then "
					"prints the customer invoice in the field.\n\n"
					"The exact reporting or clearance process depends on invoice type, taxpayer "
					"requirements and the configured e-invoicing environment."
				),
				"image": warehouse,
				"image_alt": "Central warehouse team staging stock that will become van inventory and invoices",
				"link_label": "See ZATCA Integration",
				"link_href": "/software/zatca-integration",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Print the invoice. Collect the payment. Leave the location.",
				"body": (
					"A compatible mobile printer produces a professional customer invoice at the "
					"counter — no pre-printed stationery and no return to the office.\n\n"
					"Field collections record customer, invoice reference, amount, method, date, "
					"salesperson, reference number and remarks, then synchronise with ERPNext so "
					"accounts sees cash and credit collections the same day."
				),
				"image": load,
				"image_alt": "Carton leaving the van at the customer — the moment of delivery, invoice and collection",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Built around the way your vans already operate",
				"body": (
					"Every distribution business works slightly differently. Some take orders "
					"today and deliver tomorrow. Others sell directly from van stock, deliver "
					"against pre-booked sales orders, collect cash at delivery, extend credit, "
					"run fixed routes, require batch and expiry control, or work where "
					"connectivity is limited.\n\n"
					"Printechs configures and extends VAN Sales around those requirements while "
					"ERPNext remains the central business platform. Tell us how your vans operate "
					"— we will design the workflow around your business."
				),
				"image": hero,
				"image_alt": "Sales van on a residential route — the daily field-sales operation VAN Sales is built for",
				"link_label": "Discuss Your Distribution Workflow",
				"link_href": "/contact",
				"sort_order": 5,
			},
		],
	)

	capability_rows = []
	modules = [
		(
			"Core features",
			"integration",
			[
				"ERPNext integration and automatic transaction synchronisation",
				"Van as an ERPNext warehouse with van-stock synchronisation",
				"Customer, item, barcode, price and tax synchronisation",
				"Online and offline operation",
				"Customer order taking and sales-order synchronisation",
				"Delivery workflow and direct van sales",
				"Mobile sales invoice and ZATCA integration through ERPNext",
				"Payment collection and mobile invoice printing",
			],
		),
		(
			"Recommended next features",
			"inventory",
			[
				"Customer outstanding, credit-limit control and sales history",
				"Product returns and credit-note / sales-return workflow",
				"Batch, expiry and multi-UOM selling units",
				"Van loading, replenishment and daily van reconciliation",
				"Promotion and salesperson discount limits",
				"Sales dashboard and proof of delivery",
			],
		),
		(
			"Optional enhancements",
			"device",
			[
				"GPS location tracking can be added where required — it is not a standard feature",
				"Customer check-in / check-out and visit planning",
				"Route and territory management; route optimisation as a separate scope",
				"Digital signature and delivery photographs",
				"New customer registration submitted to ERPNext for approval",
				"Sales targets and salesperson performance indicators",
			],
		),
	]
	sort_order = 1
	for title, icon, items in modules:
		for item_text in items:
			capability_rows.append(
				{
					"module_title": title,
					"icon": icon,
					"item_text": item_text,
					"sort_order": sort_order,
				}
			)
			sort_order += 1
	doc.set("capability_items", capability_rows)

	doc.set(
		"applications",
		[
			{
				"title": "FMCG",
				"description": "High-volume store visits, van inventory, direct sales and collections.",
				"image": retail,
				"image_alt": "Supermarket produce display — a typical FMCG van-sales customer",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "Food & beverage distribution",
				"description": "Take orders, deliver products and invoice customers from the vehicle.",
				"image": produce,
				"image_alt": "Fresh produce display supplied by food-distribution vans",
				"industry_link": "food-beverage",
				"sort_order": 2,
			},
			{
				"title": "Dairy distribution",
				"description": "Frequent route-based deliveries and mobile invoicing for dairy routes.",
				"image": warehouse,
				"image_alt": "Warehouse staging for high-frequency dairy and cold-chain van loads",
				"industry_link": "dairy",
				"sort_order": 3,
			},
			{
				"title": "Bakery distribution",
				"description": "Daily delivery routes and direct invoicing to stores and customers.",
				"image": bakery,
				"image_alt": "Bakery counter stocked for the morning van-delivery run",
				"industry_link": "bakery",
				"sort_order": 4,
			},
			{
				"title": "Meat & seafood distribution",
				"description": "Product sales, customer deliveries and collections from distribution vehicles.",
				"image": load,
				"image_alt": "Cartons leaving the van for a food-service or retail delivery",
				"industry_link": "food-beverage",
				"sort_order": 5,
			},
			{
				"title": "Pharmaceutical distribution",
				"description": "Controlled field sales and collections with centrally synchronised data.",
				"image": mobile,
				"image_alt": "Field user confirming product and quantity on a handheld before delivery",
				"industry_link": "pharmaceutical",
				"sort_order": 6,
			},
			{
				"title": "Cosmetics & beauty distribution",
				"description": "Visit salons, retailers and beauty outlets with complete product and customer information.",
				"image": salon,
				"image_alt": "Beauty salon floor visited by cosmetics field-sales representatives",
				"industry_link": "fashion",
				"sort_order": 7,
			},
			{
				"title": "Wholesale & spare-parts distribution",
				"description": "Mobile order taking, van stock, delivery, invoicing and account information on the road.",
				"image": parts,
				"image_alt": "Spare-parts workshop tools — typical stock carried by a parts sales van",
				"industry_link": "warehouse-logistics",
				"sort_order": 8,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "integration",
				"title": "ERPNext connected",
				"description": "Customers, items, prices, stock and invoices on one ledger",
				"sort_order": 1,
			},
			{
				"icon": "inventory",
				"title": "Van warehouse",
				"description": "Each vehicle is a stock location the office can reconcile",
				"sort_order": 2,
			},
			{
				"icon": "cloud",
				"title": "Offline ready",
				"description": "Capture the sale; synchronise when the network returns",
				"sort_order": 3,
			},
			{
				"icon": "scan",
				"title": "Barcode scanning",
				"description": "Identify items on Datalogic or Zebra enterprise handhelds",
				"sort_order": 4,
			},
			{
				"icon": "print",
				"title": "Mobile printing",
				"description": "Invoice or receipt at the customer from a paired printer",
				"sort_order": 5,
			},
			{
				"icon": "checkout",
				"title": "ZATCA via ERPNext",
				"description": "Field invoices follow the company's e-invoicing workflow",
				"sort_order": 6,
			},
		],
	)

	doc.localization_heading = "Van Sales software for Saudi distribution"
	doc.localization_body = (
		"Printechs VAN Sales is built for field sales and direct-store-delivery teams "
		"operating across Saudi Arabia — with ERPNext at the centre and ZATCA e-invoicing "
		"on the invoice path. The same stack supports Arabic and English device and "
		"document requirements where the project needs them."
	)
	doc.localization_chips = (
		"Van Sales Software Saudi Arabia\n"
		"ERPNext Van Sales\n"
		"Offline Van Sales Software\n"
		"ZATCA Van Sales Software\n"
		"Direct Store Delivery\n"
		"Mobile Invoice Printing\n"
		"Van Inventory Management\n"
		"Mobile Payment Collection"
	)

	doc.reports_heading = "Sales, inventory, collection and productivity in one place"
	doc.reports_image = warehouse
	doc.reports_image_alt = "Warehouse and van-load activity that feeds VAN Sales management reports"
	doc.set(
		"report_items",
		[
			{"title": title, "sort_order": idx}
			for idx, title in enumerate(
				[
					"Sales by van, salesperson, customer, item and territory",
					"Daily and monthly sales — cash versus credit",
					"Stock by van, movement and remaining balance",
					"Fast-moving, unsold and return stock",
					"Collection by salesperson and customer",
					"Daily cash collection and overdue receivables",
					"Customers assigned, visited and productive visits",
					"Orders taken, no-order visits and target achievement",
				],
				start=1,
			)
		],
	)

	doc.dashboard_heading = "Close the day with complete visibility of van activity"
	doc.dashboard_body = (
		"Opening van stock, stock loaded, sales quantity, returns, remaining stock, "
		"cash collected, credit sales, payments, cancelled transactions and stock "
		"differences — so management can reconcile the salesperson's day without "
		"waiting for paper to reach the office."
	)
	doc.dashboard_image = stock
	doc.dashboard_image_alt = "Van inventory ready for daily sales, returns and end-of-day reconciliation"

	doc.set(
		"support_items",
		[
			{
				"icon": "integration",
				"title": "ERPNext + ZATCA",
				"description": "The same ERP and e-invoicing stack the office already runs.",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Enterprise handhelds",
				"description": "Datalogic and Zebra Android devices with integrated barcode scanning.",
				"sort_order": 2,
			},
			{
				"icon": "print",
				"title": "Mobile printers",
				"description": "Invoice and receipt printing paired to the field application.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Expandable workflow",
				"description": "Add returns, credit control, visits, promotions and more as the fleet grows.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Does VAN Sales work without mobile internet?",
				"answer": (
					"Yes. Required customers, products, prices and van stock are stored on the "
					"device. Authorised users can take orders, prepare deliveries, generate "
					"sales and record collections offline. Pending transactions synchronise "
					"with ERPNext when connectivity returns."
				),
				"sort_order": 1,
			},
			{
				"question": "How does ZATCA e-invoicing work from the van?",
				"answer": (
					"The mobile invoice is transmitted to ERPNext. ERPNext generates and "
					"processes the electronic invoice through the configured ZATCA integration. "
					"The response returns to the application so the salesperson can print the "
					"customer invoice. The exact clearance or reporting step depends on invoice "
					"type and the taxpayer environment."
				),
				"sort_order": 2,
			},
			{
				"question": "Is each van really a warehouse in ERPNext?",
				"answer": (
					"Yes. Each vehicle can be configured as its own warehouse — for example "
					"VAN-001 Warehouse. Stock transferred from the central warehouse becomes "
					"that van's available inventory, and sales issue from that location."
				),
				"sort_order": 3,
			},
			{
				"question": "Do you include GPS location tracking?",
				"answer": (
					"No — not as a standard feature. GPS-based salesperson and vehicle tracking "
					"is an optional enhancement. It can be added where the company policy and "
					"applicable privacy requirements allow, and should not be assumed in a "
					"standard deployment."
				),
				"sort_order": 4,
			},
			{
				"question": "Which devices does VAN Sales run on?",
				"answer": (
					"The application is deployed on suitable Android devices, including rugged "
					"Datalogic or Zebra enterprise handhelds when the project needs integrated "
					"barcode scanning and field durability. A mobile printer can be paired for "
					"invoice and receipt printing."
				),
				"sort_order": 5,
			},
			{
				"question": "Can you match our order-today, deliver-tomorrow process?",
				"answer": (
					"Yes. VAN Sales can be configured for order taking followed by later "
					"delivery, immediate order and delivery, direct van sale, delivery against "
					"an existing sales order, and partial delivery. Printechs designs the "
					"workflow around how your vans already operate."
				),
				"sort_order": 6,
			},
		],
	)

	related = []
	for sort, slug, label, summary, href, image in (
		(1, "erpnext", "ERPNext", "The central ledger for customers, van stock, invoices and collections", "/software/erpnext", erpnext_image),
		(2, "zatca-integration", "ZATCA Integration", "E-invoicing workflow field invoices follow after they post to ERPNext", "/software/zatca-integration", zatca_image),
		(3, "warehouse-management-system", "Warehouse Management", "Central warehouse load and replenishment into each van", "/software/warehouse-management-system", wms_image),
		(4, "custom-software-development", "Custom Software", "Extend VAN Sales with returns, visits, promotions and device workflows", "/software/custom-software-development", custom_image),
		(5, "mobile-applications", "Mobile Applications", "Enterprise Android apps for field, warehouse and retail teams", "/software/mobile-applications", mobile_image),
		(6, "api-integration", "API Integration", "Connect VAN Sales to additional systems and devices", "/software/api-integration", api_image),
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
