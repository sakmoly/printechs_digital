# Copyright (c) 2026, Printechs and contributors
"""Create or update the Warehouse Management System Website Product."""

from pathlib import Path
from shutil import copy2

import frappe

SOFTWARE_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/software")
INDUSTRY_DIR = Path("/home/erpnext/frappe-bench/frontend/printechs-web/public/images/industries")
SITE_FILES = Path("/home/erpnext/frappe-bench/sites/site1.local/public/files")


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
		"Control inventory movement, picking accuracy and warehouse throughput."
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


def fill_wms():
	doc = get_or_create_wms()

	hero = copy_software_image("software-warehouse-management-system.jpg")
	mobile_image = copy_software_image("software-mobile-applications.jpg")
	erpnext_image = copy_software_image("software-erpnext.jpg")
	pos_image = copy_software_image("software-modern-pos.jpg")
	warehouse_industry = copy_industry_image("industry-warehouse-logistics.jpg")

	doc.website_product_name = "Warehouse Management System"
	doc.display_name = "Warehouse Management System"
	doc.slug = "warehouse-management-system"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.brand = "Printechs"
	doc.category = "Warehouse Software"
	doc.subcategory = "Warehouse Management"
	doc.category_label = "WAREHOUSE EXECUTION SOFTWARE"
	doc.tagline = "Control inventory movement, picking accuracy and warehouse throughput"
	doc.short_description = (
		"Cloud-ready WMS for distribution and multi-site warehousing — inbound, put-away, "
		"picking, packing, and ERP-connected stock visibility."
	)
	doc.long_description = (
		"<p>Printechs Warehouse Management System connects receiving, storage, and dispatch "
		"in one operational view. Warehouse teams scan, pick, and ship from handheld devices "
		"while supervisors track inventory accuracy, order status, and labour in real time.</p>"
		"<p>Built for Saudi distribution centres and retail replenishment operations, the "
		"platform integrates with ERPNext, barcode printers, mobile computers, and store "
		"systems — so stock movements stay accurate from the dock to the sales floor.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Warehouse management picking list with scanner, label printer and dashboard"
	)
	doc.hero_trust_chips = "Inbound / outbound\nInventory visibility\nMobile workflows"
	doc.show_demo_cta = 1
	doc.show_on_products_list = 0
	doc.show_on_software_list = 1
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "Warehouse execution, visible from dock to dispatch"
	doc.visual_story_heading = "See WMS in action"
	doc.card_title = "Warehouse Management System"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Control inventory movement, picking accuracy and warehouse throughput."
	)
	doc.card_image = hero
	doc.final_cta_heading = "See WMS in your warehouse environment"
	doc.final_cta_description = (
		"Book a demo with Printechs to explore receiving, picking, ERP integration, "
		"and mobile workflows for your distribution operation."
	)
	doc.meta_title = "Warehouse Management System | Printechs Software"
	doc.meta_description = "Warehouse management software from Printechs."
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "inventory",
				"title": "Inventory visibility",
				"description": "Real-time stock by location, lot, and status across warehouses and stores.",
				"sort_order": 1,
			},
			{
				"icon": "scan",
				"title": "Picking accuracy",
				"description": "Directed picking on handhelds with barcode confirmation and exception handling.",
				"sort_order": 2,
			},
			{
				"icon": "store",
				"title": "Inbound & outbound",
				"description": "ASN receiving, put-away, packing, and dispatch in one warehouse workflow.",
				"sort_order": 3,
			},
			{
				"icon": "android",
				"title": "Mobile workflows",
				"description": "Android handhelds for receiving, counts, transfers, and floor replenishment.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"visual_story_items",
		[
			{
				"label": "Receiving",
				"image": warehouse_industry,
				"image_alt": "Warehouse receiving with pallets and racking",
				"caption": "Scan inbound ASNs and put stock away to directed locations.",
				"sort_order": 1,
			},
			{
				"label": "Picking",
				"image": mobile_image,
				"image_alt": "Mobile warehouse picking with handheld scanner",
				"caption": "Wave and order picking on mobile computers with barcode confirmation.",
				"sort_order": 2,
			},
			{
				"label": "Dispatch",
				"image": hero,
				"image_alt": "Warehouse dashboard with picking list and label printer",
				"caption": "Pack, label, and ship with live order status for supervisors.",
				"sort_order": 3,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{
				"icon": "cloud",
				"title": "Deployment",
				"description": "Cloud SaaS or on-premise · multi-warehouse support",
				"sort_order": 1,
			},
			{
				"icon": "integration",
				"title": "ERP integration",
				"description": "ERPNext native · real-time stock and order sync",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Device support",
				"description": "Android handhelds, barcode scanners, and label printers",
				"sort_order": 3,
			},
			{
				"icon": "scan",
				"title": "Identification",
				"description": "1D/2D barcode and location-level tracking",
				"sort_order": 4,
			},
			{
				"icon": "report",
				"title": "Languages",
				"description": "English and Arabic interface support",
				"sort_order": 5,
			},
			{
				"icon": "connectivity",
				"title": "Offline mode",
				"description": "Continue receiving and picking when connectivity drops",
				"sort_order": 6,
			},
		],
	)

	capability_rows = []
	modules = [
		("Inbound", "inventory", [
			"ASN and purchase-order receiving",
			"Quality hold and put-away rules",
			"Location-directed storage",
		]),
		("Inventory", "scan", [
			"Real-time stock by bin and lot",
			"Cycle counts and adjustments",
			"Inter-warehouse transfers",
		]),
		("Outbound", "store", [
			"Wave, cluster, and order picking",
			"Packing and shipping confirmation",
			"Store replenishment orders",
		]),
		("Labour", "android", [
			"Task assignment on handhelds",
			"Picker productivity tracking",
			"Exception and short-pick handling",
		]),
		("Labels", "print", [
			"Location and item barcode labels",
			"Shipping and carton labels",
			"Zebra printer connectivity",
		]),
		("Integrations", "integration", [
			"ERPNext inventory and sales sync",
			"POS and e-commerce order flow",
			"API layer for 3PL and carriers",
		]),
	]
	sort_order = 1
	for title, icon, items in modules:
		for item_text in items:
			capability_rows.append({
				"module_title": title,
				"icon": icon,
				"item_text": item_text,
				"sort_order": sort_order,
			})
			sort_order += 1
	doc.set("capability_items", capability_rows)

	doc.set(
		"applications",
		[
			{
				"title": "Distribution centres",
				"description": "High-volume inbound, picking, and dispatch with handheld workflows.",
				"image": warehouse_industry,
				"image_alt": "Warehouse logistics with conveyor, forklift and pallet racking",
				"industry_link": "warehouse-logistics",
				"sort_order": 1,
			},
			{
				"title": "Retail replenishment",
				"description": "Store allocation and multi-location stock for retail chains.",
				"image": copy_industry_image("industry-retail.jpg"),
				"image_alt": "Retail warehouse replenishment",
				"industry_link": "retail",
				"sort_order": 2,
			},
			{
				"title": "Food & beverage",
				"description": "Lot tracking, FEFO picking, and cold-chain warehouse control.",
				"image": copy_industry_image("industry-food-beverage.jpg"),
				"image_alt": "Food and beverage warehouse operations",
				"industry_link": "food-beverage",
				"sort_order": 3,
			},
			{
				"title": "Pharmaceutical",
				"description": "Batch traceability and controlled-item handling in the warehouse.",
				"image": copy_industry_image("industry-pharmaceutical.jpg"),
				"image_alt": "Pharmaceutical warehouse operations",
				"industry_link": "pharmaceutical",
				"sort_order": 4,
			},
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
				"summary_override": "Floor picking & counts",
				"href": "/products/datalogic-memor-17" if memor_name else "#",
				"image": "/files/Memor17_front.jpg" if (SITE_FILES / "Memor17_front.jpg").exists() else None,
				"sort_order": 1,
			},
			{
				"related_website_product": zebra_name,
				"display_name_override": "Label Printer",
				"summary_override": "Location & shipping labels",
				"href": "/products/zebra-zt421" if zebra_name else "#",
				"image": "/files/ZT421.jpg" if (SITE_FILES / "ZT421.jpg").exists() else None,
				"sort_order": 2,
			},
			{
				"display_name_override": "Barcode Scanner",
				"summary_override": "Receiving & verification",
				"href": "#",
				"image": "/files/Mobile Computers.jpg" if (SITE_FILES / "Mobile Computers.jpg").exists() else hero,
				"sort_order": 3,
			},
			{
				"display_name_override": "ERPNext",
				"summary_override": "Inventory & orders",
				"href": "/software/erpnext",
				"image": erpnext_image,
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Discovery & rollout",
				"description": "Process mapping, location design, and warehouse go-live support.",
				"sort_order": 1,
			},
			{
				"icon": "device",
				"title": "Device staging",
				"description": "Handheld, scanner, and printer configuration for the floor.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "ERP integration",
				"description": "ERPNext setup, data migration, and API connectivity.",
				"sort_order": 3,
			},
			{
				"icon": "training",
				"title": "Ongoing support",
				"description": "Operator training, help desk, and continuous improvement.",
				"sort_order": 4,
			},
		],
	)

	doc.set("downloads", [])
	doc.set("package_contents", [])
	doc.set("full_specifications", [])

	pos_name = published_name("modern-pos")
	doc.set(
		"related_products",
		[
			{
				"related_website_product": pos_name,
				"display_name_override": "Modern POS",
				"summary_override": "Store checkout connected to warehouse stock",
				"href": "/software/modern-pos",
				"image": pos_image,
				"sort_order": 1,
			},
			{
				"display_name_override": "ERPNext",
				"summary_override": "Integrated ERP for finance, inventory, and operations",
				"href": "/software/erpnext",
				"image": erpnext_image,
				"sort_order": 2,
			},
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	frappe.db.commit()
	return doc.name
