# Copyright (c) 2026, Printechs and contributors
"""Create or update the API & System Integration Website Product.

Content follows docs/Page.md: software, machines, devices and cloud —
not API terminology alone.
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
SLUG = "api-integration"
PATH = "/software/api-integration"

SECTION_ORDER = [
	"benefits",
	"overview",
	"product_tour",
	"applications",
	"key_features",
	"content_sections",
	"process_steps",
	"capability_modules",
	"icon_specifications",
	"localization",
	"ecosystem",
	"related_products",
	"support",
	"faqs",
]

IMAGES = {
	"software-api-integration.jpg": (
		"https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=2000&q=80"
	),
	"api-erp.jpg": (
		"https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=2000&q=80"
	),
	"api-pos.jpg": (
		"https://images.unsplash.com/photo-1556740758-90de374c12ad?auto=format&fit=crop&w=2000&q=80"
	),
	"api-machine.jpg": (
		"https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=2000&q=80"
	),
	"api-warehouse.jpg": (
		"https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=2000&q=80"
	),
	"api-autoid.jpg": (
		"https://images.unsplash.com/photo-1616401784845-180882ba9ba8?auto=format&fit=crop&w=2000&q=80"
	),
	"api-cloud.jpg": (
		"https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2000&q=80"
	),
	"api-code.jpg": (
		"https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=2000&q=80"
	),
	"api-hmi.jpg": (
		"https://images.unsplash.com/photo-1581092162384-8987c1d64718?auto=format&fit=crop&w=2000&q=80"
	),
	"api-retail.jpg": (
		"https://images.unsplash.com/photo-1534723452862-4c874018d66d?auto=format&fit=crop&w=2000&q=80"
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
	doc.website_product_name = "API Integration"
	doc.display_name = "API & System Integration"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Integration Software"
	doc.short_description = (
		"Custom APIs, middleware and device interfaces that connect ERP, POS, "
		"warehouse systems, machines and cloud services."
	)
	doc.long_description = "<p>API & System Integration</p>"
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Network integration layer connecting business systems and operational devices"
	)
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_api_integration():
	m = media()
	hero = m["software-api-integration.jpg"]
	doc = get_or_create(hero)
	erp = m["api-erp.jpg"]
	pos = m["api-pos.jpg"]
	machine = m["api-machine.jpg"]
	warehouse = m["api-warehouse.jpg"]
	autoid = m["api-autoid.jpg"]
	cloud = m["api-cloud.jpg"]
	code = m["api-code.jpg"]
	hmi = m["api-hmi.jpg"]
	retail = m["api-retail.jpg"]

	erpnext_image = "/files/software-erpnext.jpg"
	pos_image = "/files/software-modern-pos.jpg"
	wms_image = "/files/software-warehouse-management-system.jpg"
	zatca_image = "/files/software-zatca-integration.jpg"
	ecom_image = "/files/software-e-commerce-solutions.jpg"

	doc.website_product_name = "API Integration"
	doc.display_name = "API & System Integration"
	doc.slug = SLUG
	doc.product_type = "Software"
	doc.division = "Software"
	if frappe.db.exists("Brand", "Printechs"):
		doc.brand = "Printechs"
	doc.category = "Integration Software"
	doc.subcategory = "API & Middleware"
	doc.category_label = "SOFTWARE ↔ MACHINE"
	doc.tagline = (
		"Connect software, machines and devices that already have a way to communicate"
	)
	doc.short_description = (
		"Printechs builds the APIs, middleware and device interfaces that let ERP, POS, "
		"warehouse systems, industrial equipment and cloud services exchange data automatically."
	)
	doc.long_description = (
		"<p>Businesses often run applications, machines and devices that were never designed "
		"to talk to each other. Staff re-key the same order, weight or barcode into a second "
		"system — and the two books drift apart.</p>"
		"<p>Printechs bridges those systems. We develop a secure integration layer so information "
		"moves automatically between ERP, POS, warehouse, e-commerce, mobile apps, industrial "
		"equipment and third-party services.</p>"
		"<p>The work is not limited to REST APIs. If a system or machine exposes an API, "
		"database, SDK, file exchange, TCP/IP, serial or industrial protocol, we can evaluate "
		"how to connect it — from the shop floor back to the ERP dashboard.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Server and network fabric representing the Printechs integration layer"
	)
	doc.hero_trust_chips = (
		"Software ↔ Software\nSoftware ↔ Machine\nMachine ↔ Cloud\nERP ↔ Devices"
	)
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Discuss Your Integration"
	doc.hero_primary_cta_href = "/contact"
	doc.hero_secondary_cta_label = "Request a Technical Consultation"
	doc.hero_secondary_cta_href = "/request-quote"
	doc.show_demo_cta = 1
	doc.show_quote_in_hero = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.featured = 0
	doc.index_page = 1
	doc.collapsible_full_specs = 1
	doc.enable_product_tour = 0
	doc.story_heading = "Your business systems should work together"
	doc.visual_story_heading = "From business software to the shop floor"
	doc.card_title = "API Integration"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"APIs, middleware and device interfaces that connect ERP, machines and the shop floor."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Have two systems that don't talk to each other?"
	doc.final_cta_description = (
		"Whether you need to connect two applications, synchronise ERP with an external "
		"platform, integrate a warehouse device or send a production order to a machine — "
		"tell us what needs to connect. We'll design the bridge."
	)
	doc.final_cta_primary_label = "Discuss Your Integration"
	doc.final_cta_primary_href = "/contact"
	doc.final_cta_secondary_label = "Send Us Your Requirement"
	doc.final_cta_secondary_href = "/request-quote"
	doc.meta_title = "API & System Integration Saudi Arabia | ERP, Machines & IoT | Printechs"
	doc.meta_description = (
		"Connect ERP, POS, e-commerce, warehouse systems, RFID, barcode devices, "
		"weighing scales and industrial machines. Printechs provides custom API, "
		"middleware and system integration in Saudi Arabia."
	)
	doc.implementation_heading = "End-to-end integration services"
	doc.implementation_cta_label = "Discuss Your Integration"
	doc.implementation_cta_href = "/contact"
	doc.published = 1

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(SECTION_ORDER, start=1)],
	)

	doc.connection_heading = "From business software to the shop floor. Connected."
	doc.connection_center_label = "Printechs Integration Layer — API · Middleware · Device interface"
	doc.set(
		"connection_items",
		[
			{"title": "ERP / Business systems", "href": "/software/erpnext", "sort_order": 1},
			{"title": "POS", "href": "/software/modern-pos", "sort_order": 2},
			{"title": "E-commerce", "href": "/software/e-commerce-solutions", "sort_order": 3},
			{"title": "Warehouse", "href": "/software/warehouse-management-system", "sort_order": 4},
			{"title": "RFID & barcode", "sort_order": 5},
			{"title": "Industrial machines", "sort_order": 6},
			{"title": "Printers & scales", "sort_order": 7},
			{"title": "Mobile & cloud", "sort_order": 8},
		],
	)

	doc.set(
		"benefits",
		[
			{
				"icon": "integration",
				"title": "Software expertise",
				"description": "ERP, POS, APIs, databases and cloud applications — on the same stack we implement.",
				"sort_order": 1,
			},
			{
				"icon": "store",
				"title": "Retail technology",
				"description": "POS, scanners, weighing scales, printers and RFID that we already supply in store.",
				"sort_order": 2,
			},
			{
				"icon": "inventory",
				"title": "Warehouse technology",
				"description": "Mobile computers, barcode, RFID and inventory workflows tied to ERPNext / WMS.",
				"sort_order": 3,
			},
			{
				"icon": "print",
				"title": "Industrial technology",
				"description": "Coding equipment, production systems, machine protocols and shop-floor automation.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Integration layer",
				"image": hero,
				"image_alt": "Network fabric that carries traffic between applications and devices",
				"caption": "A middleware layer so systems do not have to speak the same language.",
				"sort_order": 1,
			},
			{
				"label": "ERP & dashboards",
				"image": erp,
				"image_alt": "Business dashboard receiving live data from connected operations",
				"caption": "Orders, stock and machine results land in the ERP the finance team already uses.",
				"sort_order": 2,
			},
			{
				"label": "Shop floor",
				"image": machine,
				"image_alt": "Engineer at a production station with a laptop connected to the line",
				"caption": "A production order can leave ERP and reach the machine — then come back.",
				"sort_order": 3,
			},
			{
				"label": "Warehouse & Auto-ID",
				"image": warehouse,
				"image_alt": "Warehouse pick faces and carton locations that post into ERP",
				"caption": "Scans and RFID reads become stock transactions, not spreadsheet rows.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"applications",
		[
			{
				"title": "ERP & business applications",
				"description": "ERPNext, SAP, Oracle, Dynamics, Odoo, accounting and CRM — connected to the rest of the operation.",
				"image": erp,
				"image_alt": "ERP dashboard used as the business system of record",
				"industry_link": "retail",
				"sort_order": 1,
			},
			{
				"title": "POS & retail systems",
				"description": "Tills, loyalty, e-wallets, promotions, central returns, payments and the web store.",
				"image": pos,
				"image_alt": "Retail POS counter connected to central inventory and payments",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Industrial machines & production",
				"description": "Coding printers, PLCs, sensors, checkweighers, vision and packaging equipment — via API, TCP/IP, serial or SDK.",
				"image": machine,
				"image_alt": "Production station where the line and the business system share data",
				"industry_link": "packaging",
				"sort_order": 3,
			},
			{
				"title": "Barcode, RFID & Auto-ID",
				"description": "Handhelds, fixed scanners, RFID gates and label printers posting warehouse and store movements live.",
				"image": autoid,
				"image_alt": "Warehouse aisle where barcode and RFID activity can post to ERP",
				"industry_link": "warehouse-logistics",
				"sort_order": 4,
			},
			{
				"title": "Weighing & printing equipment",
				"description": "Retail and industrial scales, label printers and inkjet — a weight or label request becomes an ERP transaction.",
				"image": retail,
				"image_alt": "Retail aisle where scale, label and price data should stay in one system",
				"industry_link": "food-beverage",
				"sort_order": 5,
			},
			{
				"title": "Cloud & third-party platforms",
				"description": "E-commerce, payment gateways, shipping, SMS / WhatsApp, mobile apps and government platforms.",
				"image": cloud,
				"image_alt": "Connected cities at night — cloud and partner platforms",
				"industry_link": "warehouse-logistics",
				"sort_order": 6,
			},
		],
	)

	doc.key_features_heading = "Integration scenarios we can build"
	doc.set(
		"key_features",
		[
			{
				"title": "Manufacturing",
				"icon": "print",
				"description": (
					"ERP creates a production order → product, batch and quantity go to the coding "
					"printer or PLC → the machine runs → quantity and status return to ERP."
				),
				"sort_order": 1,
			},
			{
				"title": "Warehouse",
				"icon": "inventory",
				"description": (
					"ERP creates a pick → the handheld receives it → the operator scans → "
					"stock updates in ERP immediately."
				),
				"sort_order": 2,
			},
			{
				"title": "Retail",
				"icon": "checkout",
				"description": (
					"POS completes the sale → central inventory moves → loyalty or e-wallet "
					"updates → management sees the same ticket in ERP."
				),
				"sort_order": 3,
			},
			{
				"title": "RFID",
				"icon": "scan",
				"description": (
					"An RFID portal reads tags leaving a warehouse or store → middleware "
					"validates them → ERP posts the stock transaction."
				),
				"sort_order": 4,
			},
			{
				"title": "Weighing scale",
				"icon": "store",
				"description": (
					"Item and price master come from ERP → the scale receives them → weight "
					"and the ticket post back as a business transaction."
				),
				"sort_order": 5,
			},
			{
				"title": "E-commerce",
				"icon": "cloud",
				"description": (
					"The web order arrives → ERP creates the sales order → the warehouse ships "
					"→ status writes back to the storefront and the customer."
				),
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "From ERP to the machine — and back again",
				"body": (
					"Printechs integration is not limited to exchanging files between two applications.\n\n"
					"A production order created in the ERP can be sent to a machine. The machine "
					"executes the operation and can return quantity, status, batch, alarms or other "
					"shop-floor data so ERP updates without a second keyboard.\n\n"
					"ERP production order → product / batch / quantity → integration gateway → "
					"printer, PLC or line → result back → ERP updated."
				),
				"image": hmi,
				"image_alt": "Machine HMI that can receive an ERP order and return production status",
				"link_label": "See coding & marking",
				"link_href": "/solutions/coding-marking",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "If it can communicate, we can evaluate the bridge",
				"body": (
					"We do not promise every machine on earth. We can integrate virtually any "
					"system or equipment that provides an accessible communication interface — "
					"API, database, SDK, network protocol, file exchange or industrial bus.\n\n"
					"Typical interfaces: REST, SOAP, webhooks, JSON, XML, CSV, SQL, TCP/IP, "
					"RS-232 / RS-485, MQTT, OPC UA, Modbus and manufacturer SDKs. Middleware "
					"translates when the two sides do not already share a perfect API."
				),
				"image": code,
				"image_alt": "Custom API and middleware code that translates between systems",
				"link_label": "Talk to an integration engineer",
				"link_href": "/contact",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Integration solutions for Saudi Arabia",
				"body": (
					"Printechs helps Saudi operations connect internal systems with operational "
					"and regulatory platforms — where the interface exists and the process is clear.\n\n"
					"Typical work includes ZATCA e-invoicing, e-commerce and payment gateways, "
					"logistics providers, ERPNext with POS and WMS, and shop-floor equipment. "
					"SFDA or other government links are scoped when the official interface is available."
				),
				"image": pos,
				"image_alt": "Saudi retail counter where POS, payments and ERP should stay in sync",
				"link_label": "See ZATCA Integration",
				"link_href": "/software/zatca-integration",
				"sort_order": 3,
			},
		],
	)

	doc.process_heading = "How we build an integration"
	doc.process_subheading = (
		"Customers trust the work more when they can see the project approach — "
		"from the first site survey to monitoring after go-live."
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "01 Understand",
				"title": "Map the process, not only the endpoints",
				"description": (
					"We study the existing applications, equipment and the business transaction "
					"you need to stop re-typing."
				),
				"sort_order": 1,
			},
			{
				"group_title": "02 Connect",
				"title": "Identify how each side can talk",
				"description": (
					"APIs, SDKs, databases, file drops or machine protocols — we list what is "
					"actually available before we promise a design."
				),
				"sort_order": 2,
			},
			{
				"group_title": "03 Develop",
				"title": "Build the connector or middleware",
				"description": (
					"A custom REST API, webhook, device service or industrial gateway — "
					"whichever side cannot already speak the other language."
				),
				"sort_order": 3,
			},
			{
				"group_title": "04 Test",
				"title": "Prove the transaction end to end",
				"description": (
					"We validate the happy path, errors, retries, security and load before "
					"the integration touches live stock or invoices."
				),
				"sort_order": 4,
			},
			{
				"group_title": "05 Deploy",
				"title": "On-premise, cloud or hybrid",
				"description": (
					"The integration runs where the machines and the ERP already live — "
					"in your plant, in the cloud, or split between both."
				),
				"sort_order": 5,
			},
			{
				"group_title": "06 Support",
				"title": "Watch the pipe after go-live",
				"description": (
					"Logging, error tracking, retries and health checks — then support from "
					"Riyadh, Jeddah and Dammam as the operation grows."
				),
				"sort_order": 6,
			},
		],
	)

	capability_rows = []
	modules = [
		(
			"Integration consulting",
			"training",
			[
				"Study systems, processes and communication constraints before design",
				"Scope what can be connected now versus what needs a hardware or vendor change",
			],
		),
		(
			"API development",
			"integration",
			[
				"Custom REST APIs, webhooks and authenticated interfaces",
				"JSON / XML contracts that both sides can version and monitor",
			],
		),
		(
			"Middleware development",
			"cloud",
			[
				"A translation layer when two systems cannot connect directly",
				"Queues, retries and mapping so a failed call does not lose the business event",
			],
		),
		(
			"Device & machine integration",
			"device",
			[
				"Scanners, RFID, printers, scales, PLCs and coding equipment",
				"TCP/IP, serial, MQTT, OPC UA, Modbus or the manufacturer SDK",
			],
		),
		(
			"Data synchronization",
			"inventory",
			[
				"Real-time or scheduled sync between applications and databases",
				"Items, prices, stock, orders and shipment status kept on one ledger",
			],
		),
		(
			"Monitoring & support",
			"report",
			[
				"Logging, error tracking and integration health",
				"Retry policies and on-call support after go-live",
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
		"icon_specifications",
		[
			{
				"icon": "integration",
				"title": "REST & SOAP",
				"description": "Documented HTTP APIs with auth, versioning and webhooks",
				"sort_order": 1,
			},
			{
				"icon": "cloud",
				"title": "JSON · XML · CSV",
				"description": "Payloads and file exchange when a live API is not available",
				"sort_order": 2,
			},
			{
				"icon": "report",
				"title": "SQL databases",
				"description": "Read or write the tables the existing application already owns",
				"sort_order": 3,
			},
			{
				"icon": "connectivity",
				"title": "TCP/IP & serial",
				"description": "RS-232 / RS-485 and sockets for printers, scales and controllers",
				"sort_order": 4,
			},
			{
				"icon": "print",
				"title": "Industrial protocols",
				"description": "MQTT, OPC UA and Modbus into ERP transactions",
				"sort_order": 5,
			},
			{
				"icon": "device",
				"title": "Manufacturer SDKs",
				"description": "Vendor libraries when the device has no public API",
				"sort_order": 6,
			},
		],
	)

	doc.localization_heading = "Integration solutions for Saudi Arabia"
	doc.localization_body = (
		"Printechs designs integrations for Saudi retail, warehouse and manufacturing "
		"operations — connecting the systems you already run with the platforms your "
		"customers, couriers and regulators require, when those interfaces are available."
	)
	doc.localization_chips = (
		"ZATCA e-invoicing\n"
		"E-commerce & payments\n"
		"Logistics providers\n"
		"ERPNext · POS · WMS\n"
		"Retail & warehouse devices\n"
		"Manufacturing equipment\n"
		"SFDA / government APIs (when published)"
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "training",
				"title": "Integration consulting",
				"description": "We study your systems, processes and communication requirements first.",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "API & middleware",
				"description": "Custom APIs and a translation layer when the two sides cannot connect directly.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Device & machine work",
				"description": "Scanners, RFID, printers, scales, PLCs and coding equipment on the same project.",
				"sort_order": 3,
			},
			{
				"icon": "maintenance",
				"title": "Monitor and support",
				"description": "Logging, retries and support from Riyadh, Jeddah and Dammam after go-live.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Is this only REST API development?",
				"answer": (
					"No. REST is one interface. We also build middleware, webhooks, database sync "
					"and device or machine connectors — including TCP/IP, serial and industrial protocols."
				),
				"sort_order": 1,
			},
			{
				"question": "Can you connect a production machine to ERPNext?",
				"answer": (
					"If the machine exposes an API, SDK, network socket, serial port or industrial "
					"protocol, we can evaluate a gateway that sends the ERP order out and writes "
					"quantity or status back. We do not claim every legacy machine can be connected."
				),
				"sort_order": 2,
			},
			{
				"question": "Why Printechs instead of a pure software house?",
				"answer": (
					"We work both sides of the cable — ERP and POS software, and the scanners, "
					"scales, printers, RFID and coding equipment on the floor. That is how we "
					"design a complete process, not only an API specification."
				),
				"sort_order": 3,
			},
			{
				"question": "Do you integrate ZATCA and shipping platforms?",
				"answer": (
					"Yes, where the official interface exists. ZATCA Phase 2 invoices, payment "
					"gateways and logistics providers such as Aramex are typical Saudi scopes. "
					"Government platforms are quoted when the published API is available."
				),
				"sort_order": 4,
			},
			{
				"question": "Where does the integration run?",
				"answer": (
					"On-premise next to the machines, in the cloud next to ERP, or hybrid. "
					"We choose the topology that matches latency, security and the plant network."
				),
				"sort_order": 5,
			},
		],
	)

	related = []
	for sort, slug, label, summary, href, image in (
		(1, "erpnext", "ERPNext", "The business system most integrations post into", "/software/erpnext", erpnext_image),
		(2, "modern-pos", "Modern POS", "Store tickets that should hit the same stock book", "/software/modern-pos", pos_image),
		(3, "warehouse-management-system", "Warehouse Management", "Scans and picks that need a live ERP post", "/software/warehouse-management-system", wms_image),
		(4, "zatca-integration", "ZATCA Integration", "Phase 2 invoices from any connected channel", "/software/zatca-integration", zatca_image),
		(5, "e-commerce-solutions", "E-Commerce Solutions", "Web orders that write back as ERP sales orders", "/software/e-commerce-solutions", ecom_image),
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
