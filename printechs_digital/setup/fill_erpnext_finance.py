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

FINANCE_SECTION_ORDER = [
	"overview",
	"key_features",
	"process_steps",
	"localization",
	"reports",
	"dashboard",
	"benefits",
	"applications",
	"related_products",
	"support",
	"faqs",
]


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
		"Connect accounting, receivables, payables, banking, VAT, ZATCA e-invoicing "
		"and financial reporting with Sales, Purchasing, Inventory and Payroll."
	)
	doc.long_description = "<p>ERPNext Finance</p>"
	doc.hero_image = copy_software_image("software-erpnext.jpg")
	doc.hero_image_alt = "ERPNext Finance dashboard showing receivables, payables and financial reports"
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

	doc = get_or_create_finance()
	doc.website_product_name = "ERPNext Finance"
	doc.display_name = "Finance & Accounting"
	doc.slug = "finance"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.parent_software = parent_name
	doc.brand = "Printechs"
	doc.category = "ERP Software"
	doc.subcategory = "Finance & Accounting"
	doc.category_label = "ERPNEXT FINANCE"
	doc.tagline = "One financial system connected to your entire business"
	doc.short_description = (
		"Connect accounting, receivables, payables, banking, VAT, ZATCA e-invoicing "
		"and financial reporting directly with Sales, Purchasing, Inventory, Payroll "
		"and other ERPNext operations."
	)
	doc.long_description = (
		"<p>Every commercial transaction in ERPNext can flow into Finance without duplicate "
		"data entry. Sales invoices update receivables, purchase invoices update payables, "
		"stock transactions affect inventory valuation, payroll creates salary liabilities, "
		"and payments update bank and cash balances.</p>"
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"ERPNext Finance dashboard showing receivables, payables and financial reports"
	)
	doc.hero_trust_chips = "General Ledger\nReceivables & Payables\nVAT & ZATCA\nReal-Time Reporting"
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Book a Consultation"
	doc.hero_primary_cta_href = "/contact"
	doc.hero_secondary_cta_label = "Explore ERPNext"
	doc.hero_secondary_cta_href = "/software/erpnext#modules"
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 0
	doc.show_on_products_list = 0
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "Complete financial control in one system"
	doc.card_title = "Finance"
	doc.card_brand_label = "ERPNext"
	doc.card_summary = "Ledger, receivables, payables, VAT, ZATCA and management reports."
	doc.card_image = hero
	doc.final_cta_heading = "Ready to modernize your financial operations?"
	doc.final_cta_description = (
		"See how ERPNext Finance can connect accounting with sales, purchasing, inventory "
		"and your wider business operations."
	)
	doc.final_cta_primary_label = "Book a Consultation"
	doc.final_cta_primary_href = "/contact"
	doc.final_cta_secondary_label = "Explore ERPNext"
	doc.final_cta_secondary_href = "/software/erpnext#modules"
	doc.meta_title = "ERPNext Finance & Accounting | Printechs"
	doc.meta_description = (
		"ERPNext Finance with Printechs: one financial system connected to sales, purchasing, "
		"inventory and payroll, with VAT, ZATCA workflows and real-time reporting in Saudi Arabia."
	)
	doc.canonical_path = FINANCE_PATH
	doc.index_page = 1
	doc.published = 1
	doc.enable_product_tour = 0

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(FINANCE_SECTION_ORDER, start=1)],
	)

	doc.key_features_heading = "Key features of ERPNext Finance"
	doc.set(
		"key_features",
		[
			{
				"icon": "report",
				"title": "General Ledger",
				"description": "Maintain a centralized chart of accounts with automatic postings from business transactions across your organization.",
				"sort_order": 1,
			},
			{
				"icon": "checkout",
				"title": "Accounts Receivable",
				"description": "Track customer invoices, outstanding balances, ageing and collections with real-time visibility.",
				"sort_order": 2,
			},
			{
				"icon": "store",
				"title": "Accounts Payable",
				"description": "Monitor supplier invoices, payment schedules, ageing and liabilities from one workspace.",
				"sort_order": 3,
			},
			{
				"icon": "cloud",
				"title": "Bank & Cash Management",
				"description": "Manage bank accounts, cash accounts, payment entries, bank transactions and reconciliation.",
				"sort_order": 4,
			},
			{
				"icon": "zatca",
				"title": "VAT & ZATCA E-Invoicing",
				"description": "Support Saudi VAT requirements and connect business invoicing processes with ZATCA Phase 2 workflows.",
				"sort_order": 5,
			},
			{
				"icon": "integration",
				"title": "Cost Centers & Accounting Dimensions",
				"description": "Analyze income and expenses by branch, department, project, store, business unit or other management dimensions.",
				"sort_order": 6,
			},
			{
				"icon": "lines",
				"title": "Budgeting",
				"description": "Create budgets and compare actual expenditure against approved financial targets.",
				"sort_order": 7,
			},
			{
				"icon": "device",
				"title": "Financial Statements",
				"description": "Generate Profit & Loss, Balance Sheet, Cash Flow, General Ledger and other management reports in real time.",
				"sort_order": 8,
			},
		],
	)

	doc.connection_heading = "Every operational document can post to Finance"
	doc.connection_center_label = "One General Ledger"
	doc.set(
		"connection_items",
		[
			{"title": "Sales → Finance", "href": "/software/erpnext/sales-purchase", "sort_order": 1},
			{"title": "Purchase → Finance", "href": "/software/erpnext/sales-purchase", "sort_order": 2},
			{"title": "Inventory → Finance", "href": "/software/erpnext/inventory", "sort_order": 3},
			{"title": "Payroll → Finance", "href": "/software/erpnext/people-projects", "sort_order": 4},
			{"title": "Assets → Finance", "href": "/software/erpnext", "sort_order": 5},
		],
	)

	doc.process_heading = "How Finance works across ERPNext"
	doc.process_subheading = "Finance is connected to the transaction — not entered afterwards."
	doc.set(
		"process_steps",
		[
			{
				"group_title": "Sales",
				"title": "Quotation → Sales Order → Delivery → Invoice → Receivable",
				"description": "The same customer, item and tax master used by sales posts the receivable when the invoice is submitted.",
				"sort_order": 1,
			},
			{
				"group_title": "Procurement",
				"title": "Material Request → Purchase Order → Receipt → Invoice → Payable",
				"description": "Supplier bills match what was ordered and received, then update payables without re-keying.",
				"sort_order": 2,
			},
			{
				"group_title": "Inventory",
				"title": "Receipt / Issue / Transfer → Stock Valuation → Financial Impact",
				"description": "Stock movements update quantity and value so warehouse balances stay aligned with the ledger.",
				"sort_order": 3,
			},
			{
				"group_title": "Payroll",
				"title": "Salary Processing → Payroll Liability → Payment",
				"description": "Reviewed payroll posts salary liabilities and payments into the same accounts finance already uses.",
				"sort_order": 4,
			},
			{
				"group_title": "Assets",
				"title": "Asset Purchase → Depreciation → Financial Statements",
				"description": "Capital purchases and depreciation feed the statements instead of a separate fixed-asset workbook.",
				"sort_order": 5,
			},
		],
	)

	doc.localization_heading = "ERPNext Finance for Saudi Arabia"
	doc.localization_body = (
		"Configure ERPNext for Saudi business requirements including VAT, electronic invoicing "
		"workflows, Arabic/English business documents, company branches and financial reporting. "
		"Printechs can also customize workflows, integrations and print formats according to "
		"your operational requirements."
	)
	doc.localization_chips = "Saudi VAT\nZATCA Integration\nArabic / English Documents\nMulti-Branch Operations"

	doc.reports_heading = "Financial information when management needs it"
	doc.reports_image = hero
	doc.reports_image_alt = "ERPNext financial reports including P&L, balance sheet and ageing"
	doc.set(
		"report_items",
		[
			{"title": title, "sort_order": idx}
			for idx, title in enumerate(
				[
					"Profit & Loss",
					"Balance Sheet",
					"Cash Flow",
					"Accounts Receivable",
					"Accounts Payable",
					"Customer Ageing",
					"Supplier Ageing",
					"General Ledger",
					"Trial Balance",
					"Budget Variance",
					"Cost Center Analysis",
				],
				start=1,
			)
		],
	)

	doc.dashboard_heading = "From transactions to management insight"
	doc.dashboard_body = (
		"ERPNext dashboards allow finance teams and management to monitor cash position, "
		"outstanding receivables, liabilities, revenue, expenses and other business KPIs "
		"without waiting for manually prepared spreadsheets."
	)
	doc.dashboard_image = hero
	doc.dashboard_image_alt = "ERPNext Finance dashboard with cash, receivables and KPI cards"

	doc.set(
		"benefits",
		[
			{
				"icon": "integration",
				"title": "Single source of financial truth",
				"description": "Transactions across departments feed one accounting system.",
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Faster month-end reporting",
				"description": "Reduce manual consolidation and spreadsheet preparation.",
				"sort_order": 2,
			},
			{
				"icon": "report",
				"title": "Better cash-flow visibility",
				"description": "Monitor customer collections, supplier obligations and bank balances.",
				"sort_order": 3,
			},
			{
				"icon": "shield",
				"title": "Stronger financial controls",
				"description": "Approval workflows, permissions and audit trails improve accountability.",
				"sort_order": 4,
			},
			{
				"icon": "cloud",
				"title": "Real-time profitability",
				"description": "Review financial performance while transactions are happening.",
				"sort_order": 5,
			},
			{
				"icon": "store",
				"title": "Scalable multi-company management",
				"description": "Manage multiple companies, branches and accounting structures.",
				"sort_order": 6,
			},
		],
	)

	doc.audience_heading = "Built for growing and complex businesses"
	doc.set(
		"audience_items",
		[
			{"title": "Trading & Distribution", "description": "High invoice volume, landed costs and multi-warehouse stock.", "sort_order": 1},
			{"title": "Retail", "description": "Store sales, VAT and cash that must post cleanly into the ledger.", "sort_order": 2},
			{"title": "Manufacturing", "description": "Material consumption and finished goods that affect costing.", "sort_order": 3},
			{"title": "Services", "description": "Project billing, retainers and timesheet-based invoices.", "sort_order": 4},
			{"title": "Construction & Projects", "description": "Cost centres, billing and WIP visibility by project.", "sort_order": 5},
			{"title": "Multi-Branch Enterprises", "description": "Shared chart of accounts with branch and company reporting.", "sort_order": 6},
		],
	)

	doc.integration_heading = "Finance connects with every ERPNext module"
	related = [
		{"display_name_override": "Sales", "summary_override": "Quotes, orders and invoices", "href": "/software/erpnext/sales-purchase", "sort_order": 1},
		{"display_name_override": "Purchasing", "summary_override": "Orders, receipts and supplier bills", "href": "/software/erpnext/sales-purchase", "sort_order": 2},
		{"display_name_override": "Inventory", "summary_override": "Stock valuation and movements", "href": "/software/erpnext/inventory", "sort_order": 3},
		{"display_name_override": "Manufacturing", "summary_override": "Material issue and finished goods", "href": "/software/erpnext/manufacturing-module", "sort_order": 4},
		{"display_name_override": "HR & Payroll", "summary_override": "Salary liabilities and payments", "href": "/software/erpnext/people-projects", "sort_order": 5},
		{"display_name_override": "Assets", "summary_override": "Purchase, depreciation and books", "href": "/software/erpnext", "sort_order": 6},
		{"display_name_override": "Projects", "summary_override": "Timesheets, billing and cost", "href": "/software/erpnext/people-projects", "sort_order": 7},
		{"display_name_override": "CRM", "summary_override": "Customers and opportunities", "href": "/software/erpnext/sales-purchase", "sort_order": 8},
	]
	zatca_name = published_name("zatca-integration")
	if zatca_name:
		related.append(
			{
				"related_website_product": zatca_name,
				"display_name_override": "ZATCA Integration",
				"summary_override": "Phase 2 e-invoicing from ERP documents",
				"href": "/software/zatca-integration",
				"sort_order": 9,
			}
		)
	doc.set("related_products", related)

	doc.implementation_heading = "More than software — ERPNext implemented around your business"
	doc.implementation_cta_label = "Discuss Your ERP Requirements"
	doc.implementation_cta_href = "/contact"
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Business process study", "description": "Map how finance, sales and warehouse work today before documents go live.", "sort_order": 1},
			{"icon": "cloud", "title": "ERPNext configuration", "description": "Chart of accounts, taxes, roles, dimensions and period close.", "sort_order": 2},
			{"icon": "zatca", "title": "Saudi localization", "description": "VAT, print formats, Arabic/English documents and ZATCA workflows.", "sort_order": 3},
			{"icon": "integration", "title": "Custom development", "description": "Reports, print formats and workflow changes that match your controls.", "sort_order": 4},
			{"icon": "scan", "title": "Data migration", "description": "Opening balances, parties and outstanding invoices moved with a controlled cutover.", "sort_order": 5},
			{"icon": "connectivity", "title": "API & third-party integration", "description": "Banks, POS, WMS and other systems posting into controlled ERPNext documents.", "sort_order": 6},
			{"icon": "training", "title": "Training", "description": "Role-based sessions for the people who will post, approve and close.", "sort_order": 7},
			{"icon": "maintenance", "title": "Post-go-live support", "description": "Hypercare and ongoing help after the first month-end in the new books.", "sort_order": 8},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Can ERPNext manage multiple companies?",
				"answer": "<p>Yes. ERPNext supports multiple companies with a shared or separate chart of accounts, so group and statutory views can live in one system.</p>",
				"sort_order": 1,
			},
			{
				"question": "Does ERPNext support Saudi VAT?",
				"answer": "<p>Yes. Printechs configures VAT templates on items and invoices so tax is calculated at posting time, then trains finance on the reports used for filing.</p>",
				"sort_order": 2,
			},
			{
				"question": "Can ERPNext integrate with ZATCA?",
				"answer": "<p>Printechs connects ERPNext sales documents to ZATCA Phase 2 workflows so e-invoices follow the same invoice your team already posts. Scope is agreed during implementation rather than assumed as a generic one-click certification.</p>",
				"sort_order": 3,
			},
			{
				"question": "Can Finance integrate with Sales and Inventory?",
				"answer": "<p>Yes. That is the point of the module. Sales invoices, purchase invoices and stock movements post into the same ledger instead of being re-entered afterwards.</p>",
				"sort_order": 4,
			},
			{
				"question": "Can we use different cost centers or branches?",
				"answer": "<p>Yes. Cost centres and accounting dimensions let you analyse income and expenses by branch, department, project, store or business unit.</p>",
				"sort_order": 5,
			},
			{
				"question": "Can management view financial reports in real time?",
				"answer": "<p>Yes. Profit and Loss, Balance Sheet, ageing and other reports run from posted documents, so managers do not wait for a monthly spreadsheet rebuild.</p>",
				"sort_order": 6,
			},
			{
				"question": "Can Printechs customize financial reports?",
				"answer": "<p>Yes. We set the report pack your finance and management team will actually use, including print formats and filters by company or cost centre.</p>",
				"sort_order": 7,
			},
		],
	)

	doc.set("content_sections", [])
	doc.set("icon_specifications", [])
	doc.set("visual_story_items", [])
	doc.set("capability_items", [])

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
