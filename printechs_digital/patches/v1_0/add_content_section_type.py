# Copyright (c) 2026, Printechs and contributors

import frappe

CORE_MODULES = [
	{
		"heading": "Finance",
		"image": "/files/software-erpnext.jpg",
		"image_alt": "ERPNext finance dashboard with receivables, payables and reports",
		"body": (
			"ERPNext Finance is the ledger behind every sale, purchase, payroll run and stock movement. "
			"Accounts, VAT and ZATCA e-invoicing stay connected to the same documents your operations team already uses.\n\n"
			"Printechs configures the chart of accounts, tax templates and Saudi reporting so finance sees live numbers "
			"instead of waiting for month-end spreadsheets."
		),
		"sort_order": 1,
	},
	{
		"heading": "Inventory",
		"image": "/files/software-warehouse-management-system.jpg",
		"image_alt": "Multi-warehouse inventory and stock valuation in ERPNext",
		"body": (
			"Inventory in ERPNext tracks stock across warehouses, bins and companies with serial, batch and valuation methods "
			"that match how you buy and sell.\n\n"
			"Reorder rules, stock reconciliation and transfers stay visible to purchasing, sales and finance — "
			"so warehouse balances match the ledger."
		),
		"sort_order": 2,
	},
	{
		"heading": "Sales & Purchase",
		"image": "/files/SalesPosting.png",
		"image_alt": "ERPNext sales orders, invoices and purchase workflows",
		"body": (
			"Quotations, sales orders, delivery notes and invoices share one item and pricing master with purchase orders "
			"and supplier bills.\n\n"
			"Credit limits, pricing rules and landing costs are enforced in the same system that posts to stock and accounts, "
			"so sales and procurement do not drift apart."
		),
		"sort_order": 3,
	},
	{
		"heading": "Manufacturing",
		"image": "/files/Manufaruting.png",
		"image_alt": "ERPNext manufacturing with BOMs, work orders and material planning",
		"body": (
			"The Manufacturing module plans BOMs, work orders, material consumption and finished goods against live stock "
			"and costing.\n\n"
			"Use this when you need the standard ERPNext production cycle. For a full industry rollout — factory workflows, "
			"quality and procurement design — see the Manufacturing industry section below."
		),
		"sort_order": 4,
	},
	{
		"heading": "People & Projects",
		"image": "/files/HealthCare.png",
		"image_alt": "ERPNext HR, payroll, leave and project timesheets",
		"body": (
			"HR and Payroll manage the employee master, attendance, leave, salary structures and payslips, then post "
			"payroll to Finance. Projects connect timesheets and billing to the same people records.\n\n"
			"Printechs sets role permissions, approval flows and Saudi payroll components so HR, finance and project "
			"managers work from one workforce record."
		),
		"sort_order": 5,
	},
	{
		"heading": "Integrations",
		"image": "/files/POS_Integeration.png",
		"image_alt": "ERPNext integrations with Modern POS, WMS and external APIs",
		"body": (
			"ERPNext stays the system of record while Printechs connects store, warehouse and compliance systems around it.\n\n"
			"Modern POS, Warehouse Management, ZATCA e-invoicing, banks and e-commerce post into controlled ERPNext "
			"workflows instead of sitting in separate tools."
		),
		"sort_order": 6,
	},
]


def execute():
	if not frappe.db.exists("DocType", "Website Product Content Section"):
		return

	frappe.reload_doc("Printechs Digital", "doctype", "website_product_content_section")
	frappe.db.updatedb("Website Product Content Section")

	if frappe.db.has_column("Website Product Content Section", "section_type"):
		frappe.db.sql(
			"""
			UPDATE `tabWebsite Product Content Section`
			SET section_type = 'Industry Solution'
			WHERE ifnull(section_type, '') = ''
			"""
		)

	_seed_erpnext_core_modules()
	frappe.db.commit()


def _seed_erpnext_core_modules():
	name = frappe.db.get_value("Website Product", {"slug": "erpnext"}, "name")
	if not name:
		return

	doc = frappe.get_doc("Website Product", name)
	existing = {
		(row.heading or "").strip().lower()
		for row in doc.get("content_sections") or []
		if (row.get("section_type") or "") == "Core Module"
	}
	if existing:
		return

	for row in CORE_MODULES:
		if row["heading"].strip().lower() in existing:
			continue
		doc.append(
			"content_sections",
			{
				"section_type": "Core Module",
				"heading": row["heading"],
				"body": row["body"],
				"image": row["image"],
				"image_alt": row["image_alt"],
				"sort_order": row["sort_order"],
			},
		)

	doc.flags.ignore_validate = True
	doc.save(ignore_permissions=True)
