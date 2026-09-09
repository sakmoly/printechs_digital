# Copyright (c) 2026, Printechs and contributors
"""Create or update the Warehouse Management System Website Product."""

from pathlib import Path
from shutil import copy2

import frappe
from frappe.utils import cstr

SOFTWARE_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/software")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")

WMS_PATH = "/software/warehouse-management-system"
WMS_VIDEO = "https://youtu.be/4ykPZF4wSsw"

PARENT_TEASER = (
	"Printechs WMS adds carton, location and bin execution on top of ERPNext inventory — "
	"ASN receiving, putaway, picking, transfers, cycle counts and in-transit control.\n\n"
	"Warehouse teams scan on the floor while ERPNext keeps warehouse-level quantity, "
	"valuation and financial postings."
)

SECTION_ORDER = [
	"overview",
	"process_steps",
	"key_features",
	"benefits",
	"icon_specifications",
	"content_sections",
	"localization",
	"reports",
	"dashboard",
	"applications",
	"ecosystem",
	"related_products",
	"support",
	"faqs",
]


def copy_image(source_dir: Path, filename: str) -> str:
	source = source_dir / filename
	target = SITE_FILES / filename
	if source.exists() and not target.exists():
		copy2(source, target)
	return f"/files/{filename}"


def copy_software_image(filename: str) -> str:
	return copy_image(SOFTWARE_DIR, filename)


def copy_industry_image(filename: str) -> str:
	return copy_image(INDUSTRY_DIR, filename)


def published_name(slug: str) -> str | None:
	return frappe.db.get_value("Website Product", {"slug": slug, "published": 1}, "name")


def get_or_create_wms():
	name = frappe.db.get_value(
		"Website Product", {"slug": "warehouse-management-system"}, "name"
	)
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "Warehouse Management System"
	doc.display_name = "Warehouse Management System"
	doc.slug = "warehouse-management-system"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "Warehouse Software"
	doc.short_description = (
		"Manage receiving, cartons, locations, putaway, picking, transfers and cycle counts."
	)
	doc.long_description = "<p>Warehouse Management System</p>"
	doc.hero_image = copy_software_image("software-warehouse-management-system.jpg")
	doc.hero_image_alt = (
		"Warehouse management picking list with scanner, label printer and dashboard"
	)
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def _link_parent_wms_section():
	parent_name = published_name("erpnext") or frappe.db.get_value(
		"Website Product", {"slug": "erpnext"}, "name"
	)
	if not parent_name:
		return
	parent = frappe.get_doc("Website Product", parent_name)
	updated = False
	for row in parent.get("content_sections") or []:
		heading = (row.heading or "").strip().lower()
		if heading != "warehouse management system":
			continue
		row.body = PARENT_TEASER
		row.link_label = "Explore Warehouse Management System"
		row.link_href = WMS_PATH
		updated = True
		break
	if updated:
		parent.flags.ignore_permissions = True
		parent.save()


def fill_wms():
	doc = get_or_create_wms()

	hero = copy_software_image("software-warehouse-management-system.jpg")
	mobile_image = copy_software_image("software-mobile-applications.jpg")
	erpnext_image = copy_software_image("software-erpnext.jpg")
	pos_image = copy_software_image("software-modern-pos.jpg")
	warehouse_industry = copy_industry_image("industry-warehouse-logistics.jpg")
	video_url = cstr(getattr(doc, "video_url", None)).strip() or WMS_VIDEO

	doc.website_product_name = "Warehouse Management System"
	doc.display_name = "Warehouse Management System"
	doc.slug = "warehouse-management-system"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.brand = "Printechs"
	doc.category = "Warehouse Software"
	doc.subcategory = "Warehouse Management"
	doc.category_label = "SMARTER WAREHOUSE OPERATIONS"
	doc.tagline = "Complete inventory control"
	doc.short_description = (
		"Manage receiving, cartons, locations, putaway, picking, transfers, replenishment, "
		"cycle counts and stock movements from one connected warehouse platform."
	)
	doc.long_description = (
		"Knowing how much stock is available is not enough. Warehouse teams also need to know "
		"where it is, which carton and bin hold it, who moved it, where it came from, where it "
		"is going, whether it has been received, put away or picked, whether it is in transit, "
		"and whether the physical quantity matches ERP inventory.\n\n"
		"Printechs WMS gives warehouse teams real-time control over physical inventory — from "
		"the moment goods arrive until they are picked, transferred or dispatched. It connects "
		"warehouse employees, barcode scanning, cartons, storage locations and ERP transactions "
		"into one controlled warehouse process.\n\n"
		"Integrated with ERPNext, Printechs WMS adds detailed warehouse execution at carton, "
		"location and bin level while ERPNext continues to manage enterprise inventory, "
		"valuation and financial transactions."
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Warehouse management picking list with scanner, label printer and dashboard"
	)
	doc.video_url = video_url
	doc.hero_trust_chips = "Carton Control\nLocation & Bin\nMobile Scanning\nERPNext Connected"
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Request a Demo"
	doc.hero_primary_cta_href = "/request-demo"
	doc.hero_secondary_cta_label = "Explore Printechs WMS"
	doc.hero_secondary_cta_href = "#overview"
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 0
	doc.show_quote_in_product_tour = 0
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.enable_product_tour = 0
	doc.story_heading = "From warehouse stock to exact physical location"
	doc.visual_story_heading = "See WMS in action"
	doc.card_title = "Warehouse Management System"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Carton, location and bin execution connected to ERPNext inventory."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Take control of every carton, location and stock movement"
	doc.final_cta_description = (
		"Transform warehouse operations with barcode-driven receiving, putaway, picking, "
		"transfers, cycle counting and ERP integration. From the receiving dock to the final "
		"location — every movement under control."
	)
	doc.final_cta_primary_label = "Request a WMS Demo"
	doc.final_cta_primary_href = "/request-demo"
	doc.final_cta_secondary_label = "Talk to Our Warehouse Solutions Team"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = "Warehouse Management System | Printechs WMS"
	doc.meta_description = (
		"Printechs WMS controls receiving, cartons, locations, putaway, picking, transfers "
		"and cycle counts — connected to ERPNext inventory, valuation and finance."
	)
	doc.canonical_path = WMS_PATH
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(SECTION_ORDER, start=1)],
	)

	doc.connection_heading = "One connected flow from receiving to dispatch"
	doc.connection_center_label = "Printechs WMS"
	doc.set(
		"connection_items",
		[
			{"title": "ASN", "sort_order": 1},
			{"title": "Receiving", "sort_order": 2},
			{"title": "Putaway", "sort_order": 3},
			{"title": "Locations & Bins", "sort_order": 4},
			{"title": "Picking", "sort_order": 5},
			{"title": "Transfers", "sort_order": 6},
			{"title": "Cycle Count", "sort_order": 7},
			{"title": "ERPNext", "href": "/software/erpnext", "sort_order": 8},
		],
	)

	doc.process_heading = "One connected flow from receiving to dispatch"
	doc.process_subheading = (
		"Printechs WMS controls inventory through a structured warehouse workflow — "
		"from expected inbound cartons to ERP reconciliation."
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "Inbound",
				"title": "Advance Shipping Notice → Warehouse receiving → Purchase Receipt",
				"description": (
					"Expected goods and cartons are prepared before arrival. Staff scan and verify "
					"incoming cartons, then confirmed receiving posts into ERPNext."
				),
				"sort_order": 1,
			},
			{
				"group_title": "Putaway",
				"title": "Staging → Directed putaway → Warehouse storage",
				"description": (
					"Received cartons sit in inbound or quality staging until the system directs "
					"them to the right warehouse, location and bin."
				),
				"sort_order": 2,
			},
			{
				"group_title": "Outbound",
				"title": "Picking → Transfer or dispatch → Destination receiving",
				"description": (
					"Operators collect stock from the correct locations. Cartons move to another "
					"warehouse or leave as a dispatch, then the destination confirms what arrived."
				),
				"sort_order": 3,
			},
			{
				"group_title": "Control",
				"title": "Cycle count → ERP reconciliation",
				"description": (
					"Physical stock is counted at location level. Approved variances post as "
					"stock adjustments while warehouse-level control stays in WMS."
				),
				"sort_order": 4,
			},
		],
	)

	doc.key_features_heading = "Warehouse execution at carton, location and bin level"
	doc.set(
		"key_features",
		[
			{
				"icon": "inventory",
				"title": "Advance Shipping Notice",
				"description": "See expected suppliers, cartons, items and quantities before the truck arrives.",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Carton-wise receiving",
				"description": "Capture carton ID, barcode, item, quantity and warehouse as goods physically arrive.",
				"sort_order": 2,
			},
			{
				"icon": "store",
				"title": "Smart putaway",
				"description": "Scan the carton, confirm contents, scan the location and update WMS stock.",
				"sort_order": 3,
			},
			{
				"icon": "cloud",
				"title": "Location and bin control",
				"description": "Identify stock as warehouse + zone/aisle + rack + level + bin + carton + item.",
				"sort_order": 4,
			},
			{
				"icon": "android",
				"title": "Mobile picking",
				"description": "Material Requests become handheld tasks with location, carton and remaining quantity.",
				"sort_order": 5,
			},
			{
				"icon": "connectivity",
				"title": "Transfers and transit",
				"description": "Move complete cartons, keep stock in transit visible, and confirm destination receipt.",
				"sort_order": 6,
			},
			{
				"icon": "report",
				"title": "Cycle count with approval",
				"description": "Count on the floor, review variance, then post only approved adjustments to ERP.",
				"sort_order": 7,
			},
			{
				"icon": "integration",
				"title": "ERPNext connected",
				"description": "ERP warehouse quantity should equal the sum of WMS carton and location quantities.",
				"sort_order": 8,
			},
		],
	)

	doc.set(
		"benefits",
		[
			{
				"icon": "scan",
				"title": "Improved inventory accuracy",
				"description": "Keep system stock aligned with physical carton and location quantities.",
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Faster receiving and putaway",
				"description": "Barcode ASN receiving and directed putaway reduce misplaced inventory.",
				"sort_order": 2,
			},
			{
				"icon": "android",
				"title": "Faster picking",
				"description": "Send operators to the correct carton and location from the handheld.",
				"sort_order": 3,
			},
			{
				"icon": "inventory",
				"title": "Carton traceability",
				"description": "Follow a carton from receiving through storage, pick, transit and destination.",
				"sort_order": 4,
			},
			{
				"icon": "integration",
				"title": "Less duplicate entry",
				"description": "Confirmed warehouse work creates the ERPNext receipts, transfers and adjustments.",
				"sort_order": 5,
			},
			{
				"icon": "report",
				"title": "Better stock visibility",
				"description": "See inventory by warehouse, location, carton and in-transit status.",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "inventory", "title": "ASN", "description": "Expected cartons before arrival", "sort_order": 1},
			{"icon": "scan", "title": "Receiving", "description": "Carton, item and quantity", "sort_order": 2},
			{"icon": "store", "title": "Putaway", "description": "Directed location confirmation", "sort_order": 3},
			{"icon": "cloud", "title": "Locations", "description": "Zone, rack, level and bin", "sort_order": 4},
			{"icon": "android", "title": "Picking", "description": "Handheld tasks from ERP", "sort_order": 5},
			{"icon": "connectivity", "title": "Transfers", "description": "Carton move and transit", "sort_order": 6},
			{"icon": "report", "title": "Cycle count", "description": "Preview then approve", "sort_order": 7},
			{"icon": "integration", "title": "ERPNext", "description": "Quantity, valuation, finance", "sort_order": 8},
			{"icon": "device", "title": "Desktop WMS", "description": "Tasks, review and reports", "sort_order": 9},
			{"icon": "rugged", "title": "Mobile WMS", "description": "Scan where stock is handled", "sort_order": 10},
			{"icon": "print", "title": "Barcodes", "description": "Item, carton, location, task", "sort_order": 11},
			{"icon": "shield", "title": "Roles", "description": "Operator to finance control", "sort_order": 12},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Prepare the warehouse before goods arrive",
				"body": (
					"Printechs WMS supports an Advance Shipping Notice so warehouse users can see "
					"expected inbound inventory before physical receiving begins. An ASN can carry "
					"supplier, purchase reference, expected items and quantities, carton IDs, arrival "
					"information, receiving warehouse and status.\n\n"
					"Prepare labour and space, compare expected versus received cartons, and keep "
					"carton-level inbound visibility instead of discovering shortages at the dock."
				),
				"image": warehouse_industry,
				"image_alt": "Inbound warehouse receiving dock with expected cartons",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Receive inventory the way it physically arrives",
				"body": (
					"Goods usually arrive packed inside cartons, not as a single item total. During "
					"receiving, users can capture ASN, carton ID, barcode, item, quantity, UOM, "
					"warehouse, date, user and status — so WMS knows which carton holds each quantity.\n\n"
					"When receiving is confirmed, the workflow can create the ERPNext Purchase Receipt. "
					"ASN created → cartons received → quantities verified → receiving confirmed → "
					"Purchase Receipt → ERPNext inventory updated, without re-keying the dock."
				),
				"image": hero,
				"image_alt": "Carton-wise warehouse receiving with barcode scanning",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Staging and smart putaway",
				"body": (
					"Incoming stock may not move straight from the truck to a permanent bin. Use "
					"receiving, quality, putaway-pending, transfer and dispatch staging so inventory "
					"that has entered the building stays visible before it reaches its final location.\n\n"
					"Putaway on the handheld: scan carton, view contents, identify destination, scan "
					"the warehouse location, confirm, and update WMS stock. That reduces misplaced "
					"inventory and keeps carton traceability for faster picking later."
				),
				"image": warehouse_industry,
				"image_alt": "Directed putaway from staging into warehouse racking",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Know exactly where every item is stored",
				"body": (
					"Divide a warehouse into zone, aisle, rack, level and bin — for example A1-R01-L3-B1. "
					"Inventory is then warehouse + location + carton + item + quantity, which is far more "
					"useful than a single warehouse total.\n\n"
					"Each carton keeps its own identity: current location, contents, receiving or transfer "
					"reference, status and movement history. Status can move from received and waiting "
					"for putaway through stored, allocated, picked, in transit, received at destination "
					"and closed."
				),
				"image": hero,
				"image_alt": "Warehouse location and bin labels for carton storage",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "WMS stock balance and a movement ledger",
				"body": (
					"Printechs WMS holds stock at physical-location level, independent of a simple ERP "
					"warehouse total. Users can see company, warehouse, zone, location, carton, item "
					"and quantity. If ERP shows 120 PCS, WMS can show 40, 30 and 50 PCS across three "
					"cartons — and the total should still be 120.\n\n"
					"Every physical movement should write a ledger row: date, item, quantity, carton, "
					"source and destination warehouse and location, movement type, reference and user. "
					"Typical types include receiving, putaway, picking, relocation, transfer, cycle-count "
					"adjustment, opening stock and correction."
				),
				"image": erpnext_image,
				"image_alt": "WMS stock balance by location and carton versus ERP quantity",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Turn stock requirements into mobile picking tasks",
				"body": (
					"Material Requests and other ERPNext requirements become warehouse picking tasks. "
					"The operator opens the task, goes to the location, scans location and carton or "
					"item, confirms quantity and completes the pick. WMS can then generate the transfer "
					"or issue transaction.\n\n"
					"The handheld can show task number, item, required quantity, warehouse, location, "
					"carton, picked quantity and remaining quantity — less searching, less paperwork."
				),
				"image": mobile_image,
				"image_alt": "Android handheld picking task with location and carton",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Move cartons, keep in-transit stock visible",
				"body": (
					"Transfer a carton as one warehouse unit: scan carton, validate contents, select "
					"destination, create the transfer, then let the destination scan and complete it. "
					"All item quantities inside the carton move with it.\n\n"
					"For distant warehouses, WMS can follow ERPNext Add to Transit so stock does not "
					"look available at the destination while it is still travelling. Management can see "
					"transfer reference, cartons, items, dispatch date and receiving status."
				),
				"image": warehouse_industry,
				"image_alt": "Carton transfer between warehouses with in-transit control",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Relocate stock without losing traceability",
				"body": (
					"Layouts change for space, fast movers, consolidation or picking efficiency. "
					"Relocation is scan source location, scan carton, scan destination, confirm — "
					"then WMS stock updates.\n\n"
					"ERP financial quantity stays the same because inventory only changed physical "
					"location inside the warehouse."
				),
				"image": hero,
				"image_alt": "Location-to-location warehouse relocation with barcode scanning",
				"sort_order": 8,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Count on the floor, approve before ERP changes",
				"body": (
					"Cycle counts can run by warehouse, zone, location, item, category, selected task "
					"or ad-hoc work — without waiting for an annual stocktake. Mobile users receive "
					"the task, scan location and item or carton, enter the physical quantity and submit.\n\n"
					"Management reviews system versus actual quantity and the variance. Only approved "
					"adjustments post to ERP. A count of 98 against a system 100 is a −2 PCS variance "
					"until someone authorises it."
				),
				"image": mobile_image,
				"image_alt": "Mobile cycle count at a warehouse location",
				"sort_order": 9,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Bring existing inventory under WMS control",
				"body": (
					"At go-live, ERP warehouse totals need physical cartons and locations. Read ERP "
					"stock, count the warehouse, assign locations and cartons, review the WMS opening "
					"balance, then confirm opening stock.\n\n"
					"That opening balance is the foundation every later receipt, putaway, pick and "
					"count will reconcile against."
				),
				"image": erpnext_image,
				"image_alt": "Opening stock mapped from ERPNext into WMS locations",
				"sort_order": 10,
			},
			{
				"section_type": "Industry Solution",
				"heading": "ERPNext financial control with warehouse execution",
				"body": (
					"ERPNext manages purchasing, Purchase Receipt, warehouse-level quantity, valuation, "
					"Stock Entry, Material Request, accounting and enterprise reporting. Printechs WMS "
					"manages cartons, locations, putaway, picking, relocation, mobile tasks, cycle-count "
					"capture and physical traceability.\n\n"
					"The control rule is simple: ERPNext warehouse quantity should equal the sum of all "
					"Printechs WMS carton and location quantities for the same item and warehouse. For "
					"WMS-managed warehouses, receiving, putaway, relocation, picking, transfer and "
					"counting should pass through WMS so users cannot bypass the floor process."
				),
				"image": erpnext_image,
				"image_alt": "ERPNext inventory connected to Printechs WMS execution",
				"sort_order": 11,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Mobile, barcode and task-based warehouse work",
				"body": (
					"Operators work on industrial Android computers — Datalogic, Zebra and other "
					"rugged terminals — at the point inventory is handled. Barcodes can identify item, "
					"carton, location, transfer, ASN, picking task and count task.\n\n"
					"Supervisors distribute work as tasks: receive ASN, put away carton, pick Material "
					"Request, transfer, receive transfer, relocate, count location. Each task can carry "
					"assignee, warehouse, status, required action and completion time. Replenishment "
					"rules can also turn store sales velocity and min/max into Material Requests for "
					"the central warehouse to pick."
				),
				"image": mobile_image,
				"image_alt": "Industrial Android mobile computer for warehouse scanning",
				"sort_order": 12,
			},
		],
	)

	doc.localization_heading = "Desktop WMS, mobile WMS and ERPNext on one platform"
	doc.localization_body = (
		"Desktop WMS is for configuration, ASN management, task control, receiving review, "
		"stock inquiry, cycle-count review, transfers, reporting and management. Mobile WMS "
		"is for barcode scanning on the floor: receiving, putaway, picking, relocation, "
		"transfers and cycle count. ERPNext remains the system for purchasing, valuation, "
		"accounting, Material Requests, Stock Entries and Purchase Receipts.\n\n"
		"Stock inquiry finds an item, barcode, carton, warehouse or location in seconds and "
		"returns available quantity, location, carton and status. Role-based access keeps "
		"operators on the floor, supervisors on tasks, inventory controllers on variances "
		"and finance on approved postings."
	)
	doc.localization_chips = (
		"Desktop + mobile + ERP\nBarcode-driven\nRole-based access\nFull audit trail"
	)

	doc.reports_heading = "Turn warehouse activity into actionable information"
	doc.reports_image = hero
	doc.reports_image_alt = "Warehouse stock, inbound, movement and cycle-count reports"
	doc.set(
		"report_items",
		[
			{"title": title, "sort_order": idx}
			for idx, title in enumerate(
				[
					"WMS stock balance",
					"Stock by warehouse, location and carton",
					"Carton contents",
					"Stock in transit",
					"ASN status and expected vs received",
					"Putaway pending",
					"WMS stock ledger",
					"Location and carton movement",
					"Warehouse transfer history",
					"Cycle-count variance",
					"Adjustment history",
					"Tasks and productivity by user",
				],
				start=1,
			)
		],
	)

	doc.dashboard_heading = "See the status of your warehouse in real time"
	doc.dashboard_body = (
		"Give management today's receiving, ASN pending, cartons received, putaway pending, "
		"picking tasks, transfers, stock in transit, cycle counts, count variances, warehouse "
		"stock, location occupancy and user productivity — operational KPIs across the floor."
	)
	doc.dashboard_image = hero
	doc.dashboard_image_alt = "Printechs WMS dashboard with receiving, picking and transit KPIs"

	doc.audience_heading = "Built for businesses that need better warehouse control"
	doc.set(
		"audience_items",
		[
			{"title": "Fashion & apparel", "description": "Carton and style-level warehouse control for wholesale and retail.", "sort_order": 1},
			{"title": "Retail and multi-store", "description": "Central warehouse picking and store replenishment from live stock.", "sort_order": 2},
			{"title": "FMCG and food distribution", "description": "Inbound cartons, locations and transfers for high-volume SKUs.", "sort_order": 3},
			{"title": "Electronics and spare parts", "description": "Bin-level accuracy for mixed cartons and service parts.", "sort_order": 4},
			{"title": "Pharmaceutical and cosmetics", "description": "Traceable receiving, locations and count control for regulated goods.", "sort_order": 5},
			{"title": "E-commerce and wholesale", "description": "Directed picking, carton dispatch and destination receiving.", "sort_order": 6},
			{"title": "Industrial distribution", "description": "Multi-warehouse transfers with in-transit visibility.", "sort_order": 7},
			{"title": "Third-party warehousing", "description": "Task-based receiving, putaway and picking for 3PL operations.", "sort_order": 8},
		],
	)

	memor_name = published_name("datalogic-memor-17")
	zebra_name = published_name("zebra-zt421")
	doc.set(
		"ecosystem_items",
		[
			{
				"related_website_product": memor_name,
				"display_name_override": "Handheld Computer",
				"summary_override": "Floor receiving, putaway and picks",
				"href": "/products/datalogic-memor-17" if memor_name else "/products",
				"image": "/files/Memor17_front.jpg" if (SITE_FILES / "Memor17_front.jpg").exists() else None,
				"sort_order": 1,
			},
			{
				"related_website_product": zebra_name,
				"display_name_override": "Label Printer",
				"summary_override": "Location, carton and shipping labels",
				"href": "/products/zebra-zt421" if zebra_name else "/products",
				"image": "/files/ZT421.jpg" if (SITE_FILES / "ZT421.jpg").exists() else None,
				"sort_order": 2,
			},
			{
				"display_name_override": "Barcode Scanner",
				"summary_override": "Item, carton and location identification",
				"href": "/products",
				"image": "/files/Mobile Computers.jpg" if (SITE_FILES / "Mobile Computers.jpg").exists() else hero,
				"sort_order": 3,
			},
			{
				"display_name_override": "ERPNext",
				"summary_override": "Inventory, valuation and finance",
				"href": "/software/erpnext",
				"image": erpnext_image,
				"sort_order": 4,
			},
		],
	)

	pos_name = published_name("modern-pos")
	erpnext_name = published_name("erpnext")
	doc.set(
		"related_products",
		[
			{
				"related_website_product": erpnext_name,
				"display_name_override": "ERPNext",
				"summary_override": "Purchasing, warehouse quantity, valuation and accounting",
				"href": "/software/erpnext",
				"image": erpnext_image,
				"sort_order": 1,
			},
			{
				"related_website_product": pos_name,
				"display_name_override": "Modern POS",
				"summary_override": "Store sales that can drive warehouse replenishment",
				"href": "/software/modern-pos",
				"image": pos_image,
				"sort_order": 2,
			},
		],
	)

	doc.implementation_heading = "Why Printechs WMS?"
	doc.implementation_cta_label = "Talk to Our Warehouse Solutions Team"
	doc.implementation_cta_href = "/contact"
	doc.set(
		"support_items",
		[
			{
				"icon": "inventory",
				"title": "More than warehouse stock",
				"description": "ERP says how much you have. WMS shows where it is and how it moved.",
				"sort_order": 1,
			},
			{
				"icon": "install",
				"title": "Opening stock and go-live",
				"description": "Map ERP balances into cartons and locations before live transactions start.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Device staging",
				"description": "Android handhelds, scanners and printers configured for the floor.",
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "ERPNext integration",
				"description": "Receipts, Material Requests, transfers and approved adjustments stay connected.",
				"sort_order": 4,
			},
			{
				"icon": "shield",
				"title": "User control and audit",
				"description": "Know who moved which carton, from where to where, and when.",
				"sort_order": 5,
			},
			{
				"icon": "training",
				"title": "Saudi implementation",
				"description": "Process design, training and support from Printechs.",
				"sort_order": 6,
			},
		],
	)

	doc.set("downloads", [])
	doc.set("package_contents", [])
	doc.set("full_specifications", [])
	doc.set("capability_items", [])
	doc.set("visual_story_items", [])

	doc.set(
		"faq_items",
		[
			{
				"question": "How is Printechs WMS different from ERPNext stock?",
				"answer": (
					"<p>ERPNext tells you how much inventory a warehouse holds and posts valuation "
					"and finance. Printechs WMS adds carton, location and bin execution — receiving, "
					"putaway, picking, transfers and counts — so physical stock stays aligned with ERP.</p>"
				),
				"sort_order": 1,
			},
			{
				"question": "Does WMS replace ERPNext inventory?",
				"answer": (
					"<p>No. For the same item and warehouse, ERPNext warehouse quantity should equal "
					"the sum of WMS carton and location quantities. ERP keeps purchasing, valuation "
					"and accounting; WMS keeps the floor process.</p>"
				),
				"sort_order": 2,
			},
			{
				"question": "Can we receive by carton against an ASN?",
				"answer": (
					"<p>Yes. An Advance Shipping Notice can show expected cartons and items. Staff "
					"scan carton ID, item and quantity, then confirmed receiving can create the "
					"ERPNext Purchase Receipt.</p>"
				),
				"sort_order": 3,
			},
			{
				"question": "What happens to stock while it travels between warehouses?",
				"answer": (
					"<p>WMS can follow ERPNext Add to Transit. Stock leaves the source, stays visible "
					"as in transit, and only becomes available at the destination after carton "
					"receiving is confirmed.</p>"
				),
				"sort_order": 4,
			},
			{
				"question": "Do cycle counts change ERP stock immediately?",
				"answer": (
					"<p>No. Operators capture the physical quantity. Management reviews the variance "
					"and only approved adjustments post to ERPNext.</p>"
				),
				"sort_order": 5,
			},
			{
				"question": "Which devices does the mobile WMS use?",
				"answer": (
					"<p>Industrial Android mobile computers and barcode scanners, including Datalogic "
					"and Zebra terminals, so operators work at the location where inventory is handled.</p>"
				),
				"sort_order": 6,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	_link_parent_wms_section()
	frappe.db.commit()
	return doc.name
