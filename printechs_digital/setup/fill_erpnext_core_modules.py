# Copyright (c) 2026, Printechs and contributors
"""Create nested ERPNext core-module pages and wire card Learn more links (no summary-page links)."""

import frappe

from printechs_digital.setup.fill_erpnext import copy_software_image, published_name

PARENT_TEASERS = {
	"Finance": (
		"ERPNext Finance is the ledger behind every sale, purchase, payroll run and stock movement. "
		"Accounts, VAT and ZATCA e-invoicing stay connected to the same documents your operations team already uses.\n\n"
		"The full Finance module page covers the chart of accounts, receivables, payables, period close, "
		"banking and Saudi reporting."
	),
	"Inventory": (
		"Inventory in ERPNext tracks stock across warehouses, bins and companies with serial, batch and valuation methods "
		"that match how you buy and sell.\n\n"
		"Reorder rules, stock reconciliation and transfers stay visible to purchasing, sales and finance — "
		"so warehouse balances match the ledger."
	),
	"Sales & Purchase": (
		"Quotations, sales orders, delivery notes and invoices share one item and pricing master with purchase orders "
		"and supplier bills.\n\n"
		"Credit limits, pricing rules and landing costs are enforced in the same system that posts to stock and accounts, "
		"so sales and procurement do not drift apart."
	),
	"Manufacturing": (
		"The Manufacturing module plans BOMs, work orders, material consumption and finished goods against live stock "
		"and costing.\n\n"
		"Use this when you need the standard ERPNext production cycle. Industry-specific factory rollouts stay in the "
		"Manufacturing section further down this page."
	),
	"People & Projects": (
		"HR and Payroll manage the employee master, attendance, leave, salary structures and payslips, then post "
		"payroll to Finance. Projects connect timesheets and billing to the same people records.\n\n"
		"Printechs sets role permissions, approval flows and Saudi payroll components so HR, finance and project "
		"managers work from one workforce record."
	),
}

MODULES = [
	{
		"card_heading": "Inventory",
		"slug": "inventory",
		"display_name": "Inventory",
		"subcategory": "Inventory & Stock",
		"tagline": "Live stock that matches sales, purchasing and the ledger",
		"hero_image": "software-warehouse-management-system.jpg",
		"hero_alt": "Multi-warehouse inventory and stock valuation in ERPNext",
		"short": (
			"ERPNext Inventory tracks stock across warehouses and companies with serial, batch, valuation and "
			"reorder rules connected to sales, purchasing and finance."
		),
		"long": (
			"<p>Inventory in ERPNext is not a separate stock app. Receipts, deliveries, transfers and manufacturing "
			"consumption post to the same item master and warehouses that sales and purchasing already use.</p>"
			"<p>Printechs configures warehouses, valuation methods, serial and batch tracking and reorder rules for "
			"Saudi multi-location operations, then trains store and warehouse teams on the daily movements that keep "
			"the ledger honest.</p>"
		),
		"benefits": [
			("inventory", "Multi-warehouse", "Stock and valuation by warehouse, bin and company."),
			("scan", "Traceability", "Serial, batch and lot tracking from receipt to delivery."),
			("report", "Reorder control", "Reorder rules and reconciliation instead of surprise stockouts."),
			("integration", "Connected books", "Movements post to Finance and feed sales availability."),
		],
		"specs": [
			("inventory", "Locations", "Warehouses, bins, companies"),
			("scan", "Tracking", "Serial, batch, lot"),
			("report", "Valuation", "FIFO, moving average"),
			("store", "Replenish", "Reorder rules and requests"),
			("print", "Moves", "Receipts, transfers, deliveries"),
			("cloud", "Visibility", "Live available-to-promise"),
		],
		"sections": [
			(
				"Warehouses and valuation",
				"Set up warehouses and valuation methods that match how you actually hold stock — stores, plants, "
				"transit and consignment. ERPNext keeps quantities and value in the same movement.\n\n"
				"Printechs maps your current locations and opening balances so go-live does not start with a second set of books.",
			),
			(
				"Serial, batch and lot tracking",
				"Serial and batch numbers travel with receipts, deliveries, returns and manufacturing consumption. "
				"That is the foundation for recalls, expiry and warranty work.\n\n"
				"Use batch where the item is lot-controlled; use serial where each unit must stay unique.",
			),
			(
				"Reorder and reconciliation",
				"Reorder levels raise material requests before the shelf is empty. Stock reconciliation corrects counts "
				"with a controlled posting to the ledger.\n\n"
				"Warehouse and finance see the same adjustment instead of a spreadsheet that never gets booked.",
			),
			(
				"Transfers and availability",
				"Internal transfers and material requests move stock between locations without breaking sales availability. "
				"Reserved and projected qty stay visible to the counter and the planner.\n\n"
				"When WMS is in use, warehouse-floor tasks still post back to this same inventory.",
			),
		],
	},
	{
		"card_heading": "Sales & Purchase",
		"slug": "sales-purchase",
		"display_name": "Sales & Purchase",
		"subcategory": "Sales & Procurement",
		"tagline": "One item and price master from quote to supplier bill",
		"hero_image": "software-modern-pos.jpg",
		"hero_alt": "ERPNext sales orders, invoices and purchase workflows",
		"short": (
			"Quotations, sales orders, invoices, purchase orders and supplier bills share one item, pricing and party "
			"master — with credit limits and landing costs posted to stock and accounts."
		),
		"long": (
			"<p>Sales and purchasing in ERPNext are two sides of the same document flow. The item you quote is the item "
			"you buy, receive and invoice. Pricing rules, taxes and credit limits apply once.</p>"
			"<p>Printechs sets selling and buying cycles for Saudi companies — including POS and e-commerce postings — "
			"so finance is not re-keying the same order into a second system.</p>"
		),
		"benefits": [
			("checkout", "Quote to cash", "Quotation, order, delivery and invoice on one flow."),
			("inventory", "Procure to pay", "Purchase order, receipt and supplier bill stay linked."),
			("report", "Pricing control", "Price lists, rules and credit limits on the party master."),
			("zatca", "Tax on the document", "VAT calculated at posting, ready for ZATCA from sales invoices."),
		],
		"specs": [
			("checkout", "Selling", "Quotes, orders, invoices"),
			("inventory", "Buying", "RFQ, PO, receipts, bills"),
			("report", "Pricing", "Price lists and rules"),
			("store", "Credit", "Limits and payment terms"),
			("cloud", "Landed cost", "Freight and charges on stock"),
			("zatca", "Tax", "VAT templates on documents"),
		],
		"sections": [
			(
				"Quotations, orders and invoices",
				"A quotation becomes an order, then a delivery and an invoice without retyping items. Customer credit "
				"and payment terms are checked on the same party record.\n\n"
				"Sales teams see reserved stock; finance sees the invoice that will hit receivables.",
			),
			(
				"Purchase orders and supplier bills",
				"Material requests and purchase orders use the same items and warehouses. Receipts update stock; "
				"supplier bills match what was ordered and received.\n\n"
				"Three-way match reduces the bills that land in finance with no warehouse confirmation.",
			),
			(
				"Pricing, credit and landing costs",
				"Price lists and pricing rules keep list, contract and promotional prices consistent. Credit limits "
				"stop overselling. Landed costs put freight and charges onto stock value.\n\n"
				"Sales and procurement stop maintaining separate Excel price books.",
			),
			(
				"From stores and channels",
				"Modern POS, van sales and e-commerce can post into this same selling cycle so store invoices and "
				"central orders share items, taxes and customers.\n\n"
				"Sales Posting is available as a dedicated Printechs application when you need a controlled daily "
				"consolidation from many stores.",
			),
		],
	},
	{
		"card_heading": "Manufacturing",
		"slug": "manufacturing-module",
		"display_name": "Manufacturing",
		"subcategory": "Manufacturing",
		"tagline": "BOMs, work orders and finished goods on live stock",
		"hero_image": "software-warehouse-management-system.jpg",
		"hero_alt": "ERPNext manufacturing with BOMs, work orders and material planning",
		"short": (
			"ERPNext Manufacturing plans BOMs, work orders, material consumption and finished goods against live "
			"inventory and costing — the standard production cycle inside the ERP."
		),
		"long": (
			"<p>This page is the ERPNext Manufacturing <em>module</em>: bills of materials, work orders, job cards, "
			"material consumption and finished-goods receipt. It is the production engine inside the same stock and "
			"ledger as the rest of ERPNext.</p>"
			"<p>Industry programmes — factory layout, quality gates and sector workflows — are covered on the "
			"Manufacturing industry block on the main ERPNext page. Printechs implements both when you need them.</p>"
		),
		"benefits": [
			("print", "BOM control", "Multi-level BOMs and operations for repeatable builds."),
			("inventory", "Material issue", "Consumption and finished goods post to live stock."),
			("report", "Work orders", "Plan, release and close production against demand."),
			("integration", "Costed output", "Material and operations feed inventory valuation and finance."),
		],
		"specs": [
			("print", "BOM", "Items, operations, scrap"),
			("inventory", "Materials", "Issue and finished goods"),
			("report", "Work orders", "Plan, release, close"),
			("device", "Job cards", "Shop-floor time and qty"),
			("cloud", "MRP", "Material planning from demand"),
			("store", "Subcontract", "Send and receive work"),
		],
		"sections": [
			(
				"Bills of materials and operations",
				"A BOM lists what goes into a finished item and, when needed, the operations to make it. Nested BOMs "
				"support assemblies and sub-assemblies.\n\n"
				"Printechs helps you start with the SKUs that drive volume, not every possible variant on day one.",
			),
			(
				"Work orders and job cards",
				"Work orders reserve or issue material and track produced qty. Job cards record time and output on "
				"the shop floor when you need that detail.\n\n"
				"Planners see open work; warehouse sees what to issue; finance sees the costed receipt.",
			),
			(
				"Material consumption and finished goods",
				"Issued components reduce stock; finished goods increase it at a cost that includes material and, "
				"where configured, operations.\n\n"
				"That is how manufacturing stays on the same inventory and ledger as purchasing and sales.",
			),
			(
				"Planning and subcontracting",
				"Production planning and material requests pull from sales orders and reorder rules. Subcontracting "
				"sends material to a supplier and receives finished items back into stock.\n\n"
				"Use the industry Manufacturing section on the ERPNext page when you need a full vertical rollout, "
				"not only this core module.",
			),
		],
	},
	{
		"card_heading": "People & Projects",
		"slug": "people-projects",
		"display_name": "People & Projects",
		"subcategory": "HR, Payroll & Projects",
		"tagline": "Employees, payroll and project time on one record",
		"hero_image": "software-erpnext.jpg",
		"hero_alt": "ERPNext HR, payroll, leave and project timesheets",
		"short": (
			"ERPNext HR and Payroll manage employees, attendance, leave and salary structures, then post payroll to "
			"Finance. Projects connect timesheets and billing to the same people."
		),
		"long": (
			"<p>People data should not live in a spreadsheet next to the ERP. ERPNext keeps the employee master, "
			"leave, attendance and payroll in the same system that already holds cost centres and the ledger.</p>"
			"<p>Projects use those people for timesheets and billing. Printechs configures Saudi payroll components, "
			"roles and approvals so HR and finance close the month from one workforce record.</p>"
		),
		"benefits": [
			("loyalty", "Employee master", "One profile for role, department, bank and statutory IDs."),
			("report", "Attendance and leave", "Policies and approvals that feed payroll."),
			("zatca", "Payroll to ledger", "Salary structures post to Finance after review."),
			("cloud", "Projects", "Timesheets and billing against the same employees."),
		],
		"specs": [
			("loyalty", "HR", "Employee, department, grade"),
			("report", "Leave", "Types, balances, approvals"),
			("device", "Attendance", "Manual, timesheet, devices"),
			("zatca", "Payroll", "Structures, slips, posting"),
			("cloud", "Projects", "Tasks, time, billing"),
			("store", "Access", "Roles and approvals"),
		],
		"sections": [
			(
				"Employee master and organisation",
				"The employee record holds role, department, reporting manager, bank details and statutory identifiers. "
				"Changes flow to payroll, projects and permissions.\n\n"
				"HR stops maintaining a second list that never matches finance.",
			),
			(
				"Attendance and leave",
				"Leave types and policies can vary by grade or department. Attendance can be entered in ERPNext or "
				"brought in from devices. Approvals stay in the system.\n\n"
				"Approved leave and attendance are the inputs payroll should use — not a side spreadsheet.",
			),
			(
				"Salary structures and payroll",
				"Earnings and deductions are defined as components — fixed, formula or attendance-based. Payroll is "
				"generated, reviewed and posted to the ledger.\n\n"
				"Printechs configures Saudi statutory items with your finance team and runs parallel cycles before go-live.",
			),
			(
				"Projects, timesheets and billing",
				"Projects and timesheets use the same employees. Billable time can become invoices without retyping "
				"names and rates.\n\n"
				"Managers see utilisation; finance sees the revenue and cost in the same period.",
			),
		],
	},
]


def _get_or_create(slug: str, display_name: str, hero: str, alt: str):
	name = frappe.db.get_value("Website Product", {"slug": slug}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = f"ERPNext {display_name}"
	doc.display_name = display_name
	doc.slug = slug
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "ERP Software"
	doc.short_description = display_name
	doc.long_description = f"<p>ERPNext {display_name}</p>"
	doc.hero_image = hero
	doc.hero_image_alt = alt
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def _fill_module(parent_name: str, spec: dict, images: dict):
	hero = images[spec["hero_image"]]
	doc = _get_or_create(spec["slug"], spec["display_name"], hero, spec["hero_alt"])
	path = f"/software/erpnext/{spec['slug']}"

	doc.website_product_name = f"ERPNext {spec['display_name']}"
	doc.display_name = spec["display_name"]
	doc.slug = spec["slug"]
	doc.product_type = "Software"
	doc.division = "Software"
	doc.parent_software = parent_name
	doc.brand = "Printechs"
	doc.category = "ERP Software"
	doc.subcategory = spec["subcategory"]
	doc.category_label = "ERPNEXT CORE MODULE"
	doc.tagline = spec["tagline"]
	doc.short_description = spec["short"]
	doc.long_description = spec["long"]
	doc.hero_image = hero
	doc.hero_image_alt = spec["hero_alt"]
	doc.hero_trust_chips = "ERPNext core module\nSaudi implementation\nConnected to Finance"
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Book a Consultation"
	doc.hero_primary_cta_href = "/contact"
	doc.hero_secondary_cta_label = "Back to ERPNext"
	doc.hero_secondary_cta_href = "/software/erpnext"
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 0
	doc.show_on_products_list = 0
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = spec["tagline"]
	doc.card_title = spec["display_name"]
	doc.card_brand_label = "ERPNext"
	doc.card_summary = spec["short"][:140]
	doc.card_image = hero
	doc.final_cta_heading = f"See {spec['display_name']} in your operation"
	doc.final_cta_description = (
		"Printechs can walk through this ERPNext module against your documents, roles and Saudi requirements."
	)
	doc.meta_title = f"ERPNext {spec['display_name']} | Printechs"
	doc.meta_description = spec["short"][:160]
	doc.canonical_path = path
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{"icon": icon, "title": title, "description": desc, "sort_order": idx}
			for idx, (icon, title, desc) in enumerate(spec["benefits"], start=1)
		],
	)
	doc.set(
		"icon_specifications",
		[
			{"icon": icon, "title": title, "description": desc, "sort_order": idx}
			for idx, (icon, title, desc) in enumerate(spec["specs"], start=1)
		],
	)

	alts = {
		"software-erpnext.jpg": images["software-erpnext.jpg"],
		"software-warehouse-management-system.jpg": images["software-warehouse-management-system.jpg"],
		"software-modern-pos.jpg": images["software-modern-pos.jpg"],
		"software-zatca-integration.jpg": images["software-zatca-integration.jpg"],
	}
	image_cycle = list(alts.values())
	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": heading,
				"body": body,
				"image": image_cycle[idx % len(image_cycle)],
				"image_alt": heading,
				"sort_order": idx + 1,
			}
			for idx, (heading, body) in enumerate(spec["sections"])
		],
	)
	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Process design",
				"description": "Map how your team works today before documents go live.",
				"sort_order": 1,
			},
			{
				"icon": "training",
				"title": "Training",
				"description": "Role-based sessions for the people who will post every day.",
				"sort_order": 2,
			},
			{
				"icon": "integration",
				"title": "Connected ERP",
				"description": "Keep this module on the same items, parties and ledger as the rest of ERPNext.",
				"sort_order": 3,
			},
		],
	)
	doc.set(
		"related_products",
		[
			{
				"related_website_product": parent_name,
				"display_name_override": "ERPNext",
				"summary_override": "Full platform and industry solutions",
				"href": "/software/erpnext",
				"sort_order": 1,
			}
		],
	)

	doc.flags.ignore_permissions = True
	doc.save()
	return path


def _wire_parent_cards(parent_name: str, heading_to_path: dict[str, str]):
	parent = frappe.get_doc("Website Product", parent_name)
	changed = False
	for row in parent.get("content_sections") or []:
		if (row.get("section_type") or "") != "Core Module":
			continue
		heading = (row.heading or "").strip()
		if heading in PARENT_TEASERS:
			row.body = PARENT_TEASERS[heading]
			changed = True
		if heading in heading_to_path:
			row.link_href = heading_to_path[heading]
			row.link_label = ""
			changed = True
		elif heading == "Finance":
			row.link_href = "/software/erpnext/finance"
			row.link_label = ""
			changed = True
	if changed:
		parent.flags.ignore_permissions = True
		parent.flags.ignore_validate = True
		parent.save()


def fill_erpnext_core_modules():
	parent_name = published_name("erpnext") or frappe.db.get_value(
		"Website Product", {"slug": "erpnext"}, "name"
	)
	if not parent_name:
		frappe.throw("ERPNext Website Product must exist first")

	images = {
		filename: copy_software_image(filename)
		for filename in (
			"software-erpnext.jpg",
			"software-warehouse-management-system.jpg",
			"software-modern-pos.jpg",
			"software-zatca-integration.jpg",
		)
	}

	heading_to_path = {"Finance": "/software/erpnext/finance"}
	for spec in MODULES:
		heading_to_path[spec["card_heading"]] = _fill_module(parent_name, spec, images)

	_wire_parent_cards(parent_name, heading_to_path)
	return heading_to_path
