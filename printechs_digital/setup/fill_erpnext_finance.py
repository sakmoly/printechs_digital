# Copyright (c) 2026, Printechs and contributors
"""Create the nested ERPNext Finance page and link it from the parent ERPNext page."""

import frappe

from printechs_digital.setup.fill_erpnext import copy_software_image, published_name

FINANCE_PATH = "/software/erpnext/finance"

PARENT_TEASER = (
	"ERPNext Finance is the ledger behind every sale, purchase, payroll run and stock movement. "
	"Accounts, VAT and ZATCA e-invoicing stay connected to the same documents your operations team already uses.\n\n"
	"The full Finance module page covers the chart of accounts, receivables, payables, period close, "
	"banking and Saudi reporting."
)


def get_or_create_finance():
	name = frappe.db.get_value("Website Product", {"slug": "finance"}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "ERPNext Finance"
	doc.display_name = "Finance"
	doc.slug = "finance"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "ERP Software"
	doc.short_description = (
		"Accounting, VAT, ZATCA e-invoicing, receivables, payables and management reports "
		"on the same ledger as your ERPNext operations."
	)
	doc.long_description = "<p>ERPNext Finance</p>"
	doc.hero_image = copy_software_image("software-erpnext.jpg")
	doc.hero_image_alt = "ERPNext finance dashboard with receivables, payables and reports"
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def fill_erpnext_finance():
	parent_name = published_name("erpnext") or frappe.db.get_value(
		"Website Product", {"slug": "erpnext"}, "name"
	)
	if not parent_name:
		frappe.throw("ERPNext Website Product must exist before creating Finance")

	hero = copy_software_image("software-erpnext.jpg")
	zatca = copy_software_image("software-zatca-integration.jpg")
	pos = copy_software_image("software-modern-pos.jpg")
	wms = copy_software_image("software-warehouse-management-system.jpg")

	doc = get_or_create_finance()
	doc.website_product_name = "ERPNext Finance"
	doc.display_name = "Finance"
	doc.slug = "finance"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.parent_software = parent_name
	doc.brand = "Printechs"
	doc.category = "ERP Software"
	doc.subcategory = "Finance & Accounting"
	doc.category_label = "ERPNEXT CORE MODULE"
	doc.tagline = "One ledger for operations, tax and management reporting"
	doc.short_description = (
		"ERPNext Finance connects the general ledger, receivables, payables, VAT, ZATCA e-invoicing "
		"and management reports to the same sales, purchase, stock and payroll documents your teams already post."
	)
	doc.long_description = (
		"<p>Finance in ERPNext is not a standalone accounts package. Every invoice, payment, stock movement "
		"and payroll entry can post to the same chart of accounts, so the numbers operations see match "
		"the numbers finance signs off.</p>"
		"<p>Printechs implements ERPNext Finance for Saudi companies: chart of accounts, tax templates, "
		"ZATCA Phase 2, period close, role-based approvals and reports your management team will actually use. "
		"This page covers the Finance module in depth. Industry rollouts — fashion, manufacturing, healthcare — "
		"stay on the main ERPNext page.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = "ERPNext finance dashboard with receivables, payables and reports"
	doc.hero_trust_chips = "General ledger\nVAT & ZATCA Phase 2\nSaudi implementation"
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
	doc.story_heading = "Finance that stays connected to the business"
	doc.card_title = "Finance"
	doc.card_brand_label = "ERPNext"
	doc.card_summary = "Ledger, VAT, ZATCA, receivables, payables and management reports."
	doc.card_image = hero
	doc.final_cta_heading = "See ERPNext Finance in your books"
	doc.final_cta_description = (
		"Printechs can walk through your chart of accounts, tax setup, ZATCA flow and the reports "
		"your finance team needs before go-live."
	)
	doc.meta_title = "ERPNext Finance | Printechs"
	doc.meta_description = (
		"ERPNext Finance with Printechs: general ledger, receivables, payables, VAT, "
		"ZATCA e-invoicing and management reports for Saudi operations."
	)
	doc.canonical_path = FINANCE_PATH
	doc.index_page = 1
	doc.published = 1

	doc.set(
		"benefits",
		[
			{
				"icon": "report",
				"title": "One ledger",
				"description": "Sales, purchasing, stock and payroll post into the same accounts.",
				"sort_order": 1,
			},
			{
				"icon": "zatca",
				"title": "Saudi tax ready",
				"description": "VAT templates and ZATCA Phase 2 e-invoicing from ERP documents.",
				"sort_order": 2,
			},
			{
				"icon": "cloud",
				"title": "Live visibility",
				"description": "Receivables, payables, cash and P&L without waiting for month-end files.",
				"sort_order": 3,
			},
			{
				"icon": "integration",
				"title": "Controlled close",
				"description": "Period close, cost centres and approvals instead of spreadsheet journals.",
				"sort_order": 4,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "report", "title": "Ledger", "description": "Multi-company chart of accounts", "sort_order": 1},
			{"icon": "zatca", "title": "Compliance", "description": "VAT and ZATCA Phase 2", "sort_order": 2},
			{"icon": "checkout", "title": "AR / AP", "description": "Invoices, payments, credit control", "sort_order": 3},
			{"icon": "cloud", "title": "Close", "description": "Period lock and cost centres", "sort_order": 4},
			{"icon": "store", "title": "Banking", "description": "Payments, receipts, reconciliation", "sort_order": 5},
			{"icon": "device", "title": "Reports", "description": "P&L, balance sheet, cash flow", "sort_order": 6},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "General ledger and chart of accounts",
				"body": (
					"The chart of accounts is the structure finance uses every day. ERPNext supports multi-company "
					"ledgers, cost centres and account types so statutory books and management views can share one tree.\n\n"
					"Printechs maps your existing Tally, Excel or legacy ERP accounts into ERPNext, then trains the "
					"team on journals, opening balances and how operational documents post automatically — so most "
					"entries never start as a manual voucher."
				),
				"image": hero,
				"image_alt": "ERPNext chart of accounts and general ledger",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Receivables and payables",
				"body": (
					"Customer invoices, credit notes, payment entries and outstanding statements live next to supplier "
					"bills, purchase invoices and payment runs. Credit limits and payment terms are enforced on the "
					"same party master sales and purchasing already use.\n\n"
					"Finance sees ageing, advances and unallocated payments without exporting a second system. "
					"Collections and supplier payment lists stay auditable."
				),
				"image": pos,
				"image_alt": "ERPNext receivables and payables workflows",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "VAT and ZATCA e-invoicing",
				"body": (
					"Tax templates sit on items and invoices so VAT is calculated at posting time, not rebuilt at "
					"month end. For Saudi operations, Printechs configures ZATCA Phase 2 so compliant e-invoices "
					"are generated from the same ERPNext sales documents.\n\n"
					"Finance can review tax reports, clearance status and rejected invoices in one place. "
					"Detailed ZATCA integration is also covered on the dedicated ZATCA software page."
				),
				"image": zatca,
				"image_alt": "ZATCA e-invoicing and VAT reporting from ERPNext Finance",
				"link_label": "Explore ZATCA Integration",
				"link_href": "/software/zatca-integration",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Budgets, costing and period close",
				"body": (
					"Budgets can be set by cost centre and account so overspend is visible before the board pack. "
					"Stock valuation, landed costs and manufacturing consumption feed the same costing that finance "
					"uses for margins.\n\n"
					"Period closing locks posted months, keeps opening balances clean and reduces the late journals "
					"that usually appear after a spreadsheet close."
				),
				"image": wms,
				"image_alt": "ERPNext budgets, costing and period close",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Banking, payments and cash",
				"body": (
					"Payment entries, receipts, internal transfers and bank reconciliation keep cash in the ledger "
					"instead of a parallel Excel cash book. Mode of payment and bank accounts can match how you "
					"actually collect in stores, online or from the field.\n\n"
					"When Modern POS or van sales post into ERPNext, Finance still sees controlled summaries rather "
					"than a pile of unmanaged cash entries."
				),
				"image": pos,
				"image_alt": "ERPNext banking, payments and cash reconciliation",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Management and statutory reports",
				"body": (
					"Profit and loss, balance sheet, cash flow, trial balance, tax reports and receivable ageing "
					"are available from the same posted documents. Filters by company, cost centre and date range "
					"replace monthly rebuilds of the same workbook.\n\n"
					"Printechs sets the report pack your CFO and auditors asked for, then trains users on how to "
					"re-run it after go-live."
				),
				"image": hero,
				"image_alt": "ERPNext financial and management reports",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"support_items",
		[
			{
				"icon": "install",
				"title": "Chart of accounts design",
				"description": "Map statutory and management accounts before opening balances are loaded.",
				"sort_order": 1,
			},
			{
				"icon": "zatca",
				"title": "Tax and ZATCA setup",
				"description": "VAT templates, e-invoice flow and validation with your finance team.",
				"sort_order": 2,
			},
			{
				"icon": "training",
				"title": "Close and reporting",
				"description": "Period close, roles and the monthly report pack your team will own.",
				"sort_order": 3,
			},
		],
	)

	related = [
		{
			"related_website_product": parent_name,
			"display_name_override": "ERPNext",
			"summary_override": "Full platform and industry solutions",
			"href": "/software/erpnext",
			"sort_order": 1,
		}
	]
	zatca_name = published_name("zatca-integration")
	if zatca_name:
		related.append(
			{
				"related_website_product": zatca_name,
				"display_name_override": "ZATCA Integration",
				"summary_override": "Phase 2 e-invoicing from ERP documents",
				"href": "/software/zatca-integration",
				"sort_order": 2,
			}
		)
	doc.set("related_products", related)

	doc.flags.ignore_permissions = True
	doc.save()
	_link_parent_finance_section(parent_name)
	return doc


def _link_parent_finance_section(parent_name: str):
	parent = frappe.get_doc("Website Product", parent_name)
	updated = False
	for row in parent.get("content_sections") or []:
		if (row.get("section_type") or "") != "Core Module":
			continue
		if (row.heading or "").strip().lower() != "finance":
			continue
		row.body = PARENT_TEASER
		row.link_label = ""
		row.link_href = FINANCE_PATH
		updated = True
		break
	if updated:
		parent.flags.ignore_permissions = True
		parent.flags.ignore_validate = True
		parent.save()
