# Copyright (c) 2026, Printechs and contributors
"""Create the nested Healthcare ERP page and refresh the ERPNext industry teaser."""

import frappe

from printechs_digital.setup.fill_erpnext import (
	copy_industry_image,
	copy_software_image,
	published_name,
)

HEALTHCARE_PATH = "/software/erpnext/healthcare"

PARENT_TEASER = (
	"Printechs Healthcare ERP connects patient care with the hospital operations behind it — "
	"appointments, EMR, pharmacy, laboratory, billing, inventory, HR and accounting on one platform.\n\n"
	"Patients can book on the web or mobile and review results in the app, so the journey stays "
	"paperless from registration through follow-up."
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
	"related_products",
	"support",
	"faqs",
]


def get_or_create_healthcare():
	name = frappe.db.get_value("Website Product", {"slug": "healthcare"}, "name")
	if name:
		return frappe.get_doc("Website Product", name)

	doc = frappe.new_doc("Website Product")
	doc.website_product_name = "Printechs Healthcare ERP"
	doc.display_name = "Healthcare ERP"
	doc.slug = "healthcare"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.category = "ERP Software"
	doc.short_description = (
		"Automate hospitals, clinics and medical centers with connected patients, "
		"appointments, EMR, pharmacy, laboratory, billing and finance."
	)
	doc.long_description = "<p>Healthcare ERP</p>"
	doc.hero_image = copy_industry_image("industry-pharmaceutical.jpg")
	doc.hero_image_alt = "Healthcare operations for hospitals and clinics in Saudi Arabia"
	doc.published = 0
	doc.flags.ignore_permissions = True
	doc.insert()
	return doc


def _link_parent_healthcare_section(parent_name: str):
	parent = frappe.get_doc("Website Product", parent_name)
	updated = False
	for row in parent.get("content_sections") or []:
		if (row.get("section_type") or "") != "Industry Solution":
			continue
		if (row.heading or "").strip().lower() != "healthcare":
			continue
		row.body = PARENT_TEASER
		row.link_label = "Explore Healthcare ERP"
		row.link_href = HEALTHCARE_PATH
		updated = True
		break
	if updated:
		parent.flags.ignore_permissions = True
		parent.flags.ignore_validate = True
		parent.save()


def fill_erpnext_healthcare():
	parent_name = published_name("erpnext") or frappe.db.get_value(
		"Website Product", {"slug": "erpnext"}, "name"
	)
	if not parent_name:
		frappe.throw("ERPNext Website Product must exist before creating Healthcare")

	hero = copy_industry_image("industry-pharmaceutical.jpg")
	dashboard = copy_software_image("software-erpnext.jpg")
	mobile = copy_software_image("software-mobile-applications.jpg")
	inventory = copy_software_image("software-warehouse-management-system.jpg")
	finance_img = copy_software_image("software-zatca-integration.jpg")

	doc = get_or_create_healthcare()
	doc.website_product_name = "Printechs Healthcare ERP"
	doc.display_name = "Healthcare ERP"
	doc.slug = "healthcare"
	doc.product_type = "Software"
	doc.division = "Software"
	doc.parent_software = parent_name
	doc.brand = "Printechs"
	doc.category = "ERP Software"
	doc.subcategory = "Industry Solutions"
	doc.category_label = "ERPNext Healthcare Solutions"
	doc.tagline = "Automate your hospital. Connect every department."
	doc.short_description = (
		"Bring patient care, appointments, doctors, pharmacy, laboratory, billing, "
		"inventory, HR and finance together on one integrated healthcare management platform."
	)
	doc.long_description = (
		"Hospitals and clinics often run separate systems for appointments, patient "
		"information, billing, pharmacy, inventory, accounting and HR. The result is "
		"duplicate data entry, disconnected departments and limited management visibility.\n\n"
		"Printechs Healthcare ERP — powered by ERPNext — connects these processes in one "
		"platform. Receptionists, doctors, nurses, pharmacists, laboratory teams, accountants "
		"and management see the information that belongs to their role.\n\n"
		"The same record stays paperless from registration to follow-up. Patients can book "
		"online or from a mobile app and review laboratory and clinical results in that app "
		"instead of collecting printed reports at the counter."
	)
	doc.hero_image = hero
	doc.hero_image_alt = (
		"Healthcare ERP for hospitals and clinics — patient, pharmacy and operations in one system"
	)
	doc.hero_trust_chips = "Patients & EMR\nPharmacy & Laboratory\nPaperless Patient App\nMulti-Branch Control"
	doc.use_custom_hero_ctas = 1
	doc.hero_primary_cta_label = "Request a Demo"
	doc.hero_primary_cta_href = "/request-demo"
	doc.hero_secondary_cta_label = "Talk to Our ERP Team"
	doc.hero_secondary_cta_href = "/contact"
	doc.show_demo_cta = 0
	doc.show_quote_in_hero = 0
	doc.show_on_products_list = 0
	doc.show_on_software_list = 0
	doc.show_item_code_on_website = 0
	doc.collapsible_full_specs = 1
	doc.story_heading = "One platform for clinical and business operations"
	doc.card_title = "Healthcare"
	doc.card_brand_label = "Printechs"
	doc.card_summary = (
		"Patients, appointments, EMR, pharmacy, laboratory, billing and finance on one ERP."
	)
	doc.card_image = hero
	doc.final_cta_heading = "Ready to digitize your hospital or clinic?"
	doc.final_cta_description = (
		"Connect patient care with the business operations behind it. Printechs can configure "
		"an integrated healthcare platform for hospitals, clinics, medical centers and groups."
	)
	doc.final_cta_primary_label = "Request a Healthcare ERP Demo"
	doc.final_cta_primary_href = "/request-demo"
	doc.final_cta_secondary_label = "Discuss Your Requirements"
	doc.final_cta_secondary_href = "/contact"
	doc.meta_title = (
		"Healthcare ERP Saudi Arabia | Hospital & Clinic Management Software | Printechs"
	)
	doc.meta_description = (
		"Automate hospitals, clinics and medical centers with Printechs Healthcare ERP. "
		"Manage patients, appointments, doctors, EMR, pharmacy, laboratory, billing, "
		"inventory, HR, accounting and multi-branch operations from one integrated platform."
	)
	doc.canonical_path = HEALTHCARE_PATH
	doc.index_page = 1
	doc.published = 1
	doc.enable_product_tour = 0

	doc.set(
		"page_section_order",
		[{"section": section, "sort_order": idx} for idx, section in enumerate(SECTION_ORDER, start=1)],
	)

	doc.connection_heading = "Healthcare + ERP on one stack"
	doc.connection_center_label = "One connected Healthcare ERP"
	doc.set(
		"connection_items",
		[
			{"title": "Patients", "sort_order": 1},
			{"title": "Appointments", "sort_order": 2},
			{"title": "EMR / Doctors", "sort_order": 3},
			{"title": "Pharmacy", "sort_order": 4},
			{"title": "Laboratory", "sort_order": 5},
			{"title": "Procedures", "sort_order": 6},
			{"title": "Inpatient", "sort_order": 7},
			{"title": "Billing", "sort_order": 8},
			{"title": "Inventory & Purchase", "href": "/software/erpnext/inventory", "sort_order": 9},
			{"title": "HR & Payroll", "href": "/software/erpnext/hr-project-management", "sort_order": 10},
			{"title": "Accounting", "href": "/software/erpnext/finance", "sort_order": 11},
			{"title": "Mobile & APIs", "sort_order": 12},
		],
	)

	doc.process_heading = "From appointment to payment — one connected workflow"
	doc.process_subheading = (
		"Clinical steps stay on the same record as inventory, procurement, accounting, "
		"HR, payroll, assets and reporting. Patients can start and finish that journey "
		"without paper files."
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "Arrival",
				"title": "Registration → Appointment booking → Check-in & queue",
				"description": "Patients register once, book at reception, online or on mobile, then check in without a paper slip.",
				"sort_order": 1,
			},
			{
				"group_title": "Care",
				"title": "Vitals → Doctor consultation → Prescription / lab / procedure",
				"description": "The encounter captures complaints, diagnosis, notes, medication, investigations and follow-up on the same patient.",
				"sort_order": 2,
			},
			{
				"group_title": "Fulfilment",
				"title": "Pharmacy / laboratory / treatment → Billing & payment",
				"description": "Dispensing, results and chargeable services create the invoice — then payment and the ledger, not a second billing system.",
				"sort_order": 3,
			},
			{
				"group_title": "Continue",
				"title": "Follow-up appointment + results on the patient app",
				"description": "Book the next visit and let patients see laboratory and clinical results on mobile instead of collecting printed reports.",
				"sort_order": 4,
			},
			{
				"group_title": "Automation",
				"title": "Appointments, billing, inventory, procurement and finance",
				"description": "Reminders, invoices, reorder levels, purchase requests and accounting post from the same healthcare transactions.",
				"sort_order": 5,
			},
		],
	)

	doc.key_features_heading = "Clinical care connected to hospital operations"
	doc.set(
		"key_features",
		[
			{
				"icon": "loyalty",
				"title": "One patient record",
				"description": "Registration, history, vitals, diagnoses, prescriptions, labs, procedures, appointments, billing and documents on a single profile.",
				"sort_order": 1,
			},
			{
				"icon": "report",
				"title": "Smart appointment scheduling",
				"description": "Doctor and department calendars, time slots, walk-ins, reschedule and cancel — with overlapping bookings prevented.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "Digital consultation and EMR",
				"description": "Doctors document complaints, symptoms, vitals, diagnosis, medication, investigations and follow-up at the point of care.",
				"sort_order": 3,
			},
			{
				"icon": "inventory",
				"title": "Pharmacy on live stock",
				"description": "Prescriptions connect to batch, expiry, multi-location pharmacy stock, dispensing, sales and purchase.",
				"sort_order": 4,
			},
			{
				"icon": "print",
				"title": "Laboratory and procedures",
				"description": "Investigation requests, templates, results and chargeable procedures stay on the patient and the invoice.",
				"sort_order": 5,
			},
			{
				"icon": "zatca",
				"title": "Billing into accounting",
				"description": "Consultation, lab, procedure and pharmacy charges become patient invoices, payments and receivables.",
				"sort_order": 6,
			},
			{
				"icon": "cloud",
				"title": "Paperless patient access",
				"description": "Patients book online or on mobile and open their results in the app — less paper at reception and in the file room.",
				"sort_order": 7,
			},
			{
				"icon": "store",
				"title": "Multi-branch healthcare groups",
				"description": "Run Riyadh, Jeddah, Dammam and other sites with central visibility of visits, pharmacy, inventory and profit.",
				"sort_order": 8,
			},
		],
	)

	doc.set(
		"benefits",
		[
			{
				"icon": "integration",
				"title": "Clinical and business on one system",
				"description": "Appointments, EMR, pharmacy, inventory, HR and finance share the same records.",
				"sort_order": 1,
			},
			{
				"icon": "speed",
				"title": "Less waiting, better scheduling",
				"description": "Available slots, queues and reminders improve the patient experience.",
				"sort_order": 2,
			},
			{
				"icon": "device",
				"title": "A paperless patient journey",
				"description": "Book online or on mobile and review results in the app instead of printed files.",
				"sort_order": 3,
			},
			{
				"icon": "inventory",
				"title": "Know what was prescribed and dispensed",
				"description": "See remaining pharmacy stock and what must be purchased, with expiry in view.",
				"sort_order": 4,
			},
			{
				"icon": "report",
				"title": "From service to financial reporting",
				"description": "Chargeable care posts to invoices and the ledger without re-keying.",
				"sort_order": 5,
			},
			{
				"icon": "store",
				"title": "Central control across branches",
				"description": "Revenue, doctors, inventory and receivables by clinic or medical center.",
				"sort_order": 6,
			},
		],
	)

	doc.set(
		"icon_specifications",
		[
			{"icon": "loyalty", "title": "Patients", "description": "One connected clinical record", "sort_order": 1},
			{"icon": "report", "title": "Appointments", "description": "Doctors, slots and queues", "sort_order": 2},
			{"icon": "device", "title": "EMR", "description": "Encounter, diagnosis, notes", "sort_order": 3},
			{"icon": "inventory", "title": "Pharmacy", "description": "Batch, expiry, dispensing", "sort_order": 4},
			{"icon": "print", "title": "Laboratory", "description": "Requests, results, history", "sort_order": 5},
			{"icon": "scan", "title": "Procedures", "description": "Treatment and billing", "sort_order": 6},
			{"icon": "store", "title": "Inpatient", "description": "Wards, beds and discharge", "sort_order": 7},
			{"icon": "zatca", "title": "Billing", "description": "Invoice to the ledger", "sort_order": 8},
			{"icon": "cloud", "title": "Inventory", "description": "Medicines and supplies", "sort_order": 9},
			{"icon": "shield", "title": "HR & payroll", "description": "Clinical workforce", "sort_order": 10},
			{"icon": "integration", "title": "Accounting", "description": "AR, AP and statements", "sort_order": 11},
			{"icon": "android", "title": "Patient app", "description": "Book and view results", "sort_order": 12},
		],
	)

	doc.set(
		"content_sections",
		[
			{
				"section_type": "Industry Solution",
				"heading": "Complete patient management",
				"body": (
					"One patient. One connected record. Maintain a central profile through the "
					"whole journey: registration and unique ID, personal and contact details, "
					"medical history, previous consultations, vitals, diagnoses, prescriptions, "
					"laboratory investigations, procedures, appointment and billing history, "
					"documents and follow-up.\n\n"
					"Practitioners open previous conditions and treatment without searching "
					"across files or separate applications. That record is also what the "
					"patient app uses when results are published."
				),
				"image": dashboard,
				"image_alt": "Central patient profile with clinical and administrative history",
				"sort_order": 1,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Smart appointment and doctor scheduling",
				"body": (
					"Less waiting. Better scheduling. Better patient experience. Manage doctor "
					"availability, department calendars, appointment types, consultation duration "
					"and available slots. Prevent overlapping bookings, reschedule or cancel, "
					"take walk-ins and track referral and appointment status.\n\n"
					"Patients can book at reception, online or on their mobile. SMS or email "
					"reminders and a confirmation-to-follow-up sequence reduce no-shows. "
					"Appointment invoicing can be automated when you configure it."
				),
				"image": mobile,
				"image_alt": "Patient booking appointments online or from a mobile application",
				"sort_order": 2,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Digital consultation and clinical records",
				"body": (
					"Give doctors the information they need at the point of care. The encounter "
					"can capture chief complaints, symptoms, vitals, diagnosis, observations, "
					"medical notes, medication with dosage and duration, laboratory investigations, "
					"clinical procedures and follow-up instructions.\n\n"
					"The path on screen is Patient → Diagnosis → Prescription → Lab → Follow-up — "
					"on the same record pharmacy, laboratory and billing will use next."
				),
				"image": dashboard,
				"image_alt": "Doctor encounter with diagnosis, prescription and follow-up",
				"sort_order": 3,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Integrated pharmacy and medication inventory",
				"body": (
					"Know what was prescribed, what was dispensed, what remains in stock and what "
					"needs to be purchased. Connect prescriptions to medicines, batch numbers, "
					"expiry, purchase and receipt, pharmacy stock, multiple locations, transfers, "
					"reorder levels, suppliers, purchase orders, dispensing, sales, returns and "
					"valuation.\n\n"
					"Pharmacy is not a side list. It sits on ERPNext inventory and accounting, "
					"so stock and cost stay visible to procurement and finance."
				),
				"image": inventory,
				"image_alt": "Pharmacy stock with batch, expiry and dispensing",
				"sort_order": 4,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Laboratory, procedures and inpatient care",
				"body": (
					"Digitize the lab from investigation request to result entry: catalogues, "
					"templates, patient-linked tests, sample workflow, result entry, billing and "
					"historical results on the clinical record. Patients can open those results "
					"in the mobile app when you publish them.\n\n"
					"Chargeable procedures — minor and diagnostic work, treatment sessions, "
					"physiotherapy and rehabilitation — keep the patient, practitioner, clinical "
					"notes and invoice together. Hospitals can extend the same platform to "
					"admission, wards, rooms, beds, movement, treatment and discharge."
				),
				"image": hero,
				"image_alt": "Laboratory results and hospital service units on one record",
				"sort_order": 5,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Healthcare billing connected to accounting",
				"body": (
					"Clinical activity should not end in another disconnected billing system. "
					"Consultation, laboratory, procedure, pharmacy and other medical services "
					"become patient invoices, payments, receivables, discounts, taxes and "
					"credit control — then accounting entries and financial reports.\n\n"
					"From patient service to financial reporting without duplicate data entry. "
					"Appointment invoicing can run automatically; ERPNext supplies the sales "
					"invoice and ledger underneath."
				),
				"image": finance_img,
				"image_alt": "Healthcare invoices and receivables in the same accounts as the hospital",
				"sort_order": 6,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Medical inventory, procurement and assets",
				"body": (
					"Hospitals consume thousands of medicines, consumables and surgical supplies. "
					"Manage multiple warehouses, pharmacy inventory, batch and serial tracking, "
					"expiry, transfers, replenishment, purchase requests and orders, suppliers, "
					"valuation and consumption reporting.\n\n"
					"Purchasing follows Request → Approval → RFQ → Purchase Order → Receipt → "
					"Supplier Invoice → Payment. Capital equipment — MRI, X-ray, ultrasound, "
					"monitors, laboratory devices, IT and vehicles — can carry location, "
					"department, depreciation, maintenance and disposal on the same ERP."
				),
				"image": inventory,
				"image_alt": "Medical supplies, pharmacy warehouses and hospital equipment",
				"sort_order": 7,
			},
			{
				"section_type": "Industry Solution",
				"heading": "Healthcare HR, payroll and complete finance",
				"body": (
					"Clinical operations and workforce management share the same organisation "
					"structure. Manage doctors, nurses, technicians, pharmacists and "
					"administrative staff — records, attendance, shifts, leave, payroll, "
					"recruitment, expenses and performance — then post salary to the ledger.\n\n"
					"ERPNext is the financial backbone: general ledger, receivables and payables, "
					"bank and cash, cost centres, budgeting, fixed assets, department "
					"profitability, patient receivables, supplier liabilities and statements."
				),
				"image": finance_img,
				"image_alt": "Healthcare payroll and financial statements on ERPNext",
				"sort_order": 8,
			},
			{
				"section_type": "Industry Solution",
				"heading": "A paperless process patients can finish on mobile",
				"body": (
					"The proposition is one connected healthcare ERP: Patient Care (appointments, "
					"EMR, doctors, laboratory, pharmacy, procedures, inpatient), Hospital "
					"Operations (inventory, procurement, assets, HR, payroll) and Business "
					"Management (billing, accounting, analytics, multi-branch).\n\n"
					"Make that journey paperless. Patients book online or on their mobile, "
					"receive reminders, and open laboratory and clinical results inside the "
					"application. Reception, clinicians and accounts work from the same digital "
					"record instead of printed files moving between departments."
				),
				"image": mobile,
				"image_alt": "Patient mobile app for booking appointments and viewing results",
				"sort_order": 9,
			},
			{
				"section_type": "Industry Solution",
				"heading": "The right information for every user",
				"body": (
					"Reception works with patients, appointments, check-in and payments. Doctors "
					"open history, encounters, diagnosis, prescription and investigations. Nurses "
					"record vitals and clinical activities. Laboratory handles requests and "
					"results. Pharmacy dispenses against prescriptions and stock.\n\n"
					"Accounts see billing, payments, receivables and financials. Management uses "
					"dashboards, KPIs, approvals and profitability. HR runs employees, attendance, "
					"leave and payroll. Technical naming of the Frappe healthcare app stays in "
					"implementation — the page is Printechs Healthcare ERP powered by ERPNext."
				),
				"image": dashboard,
				"image_alt": "Role-based healthcare and ERP workspaces",
				"sort_order": 10,
			},
		],
	)

	doc.localization_heading = "One system for multiple clinics and medical centers"
	doc.localization_body = (
		"Saudi healthcare groups can run head office with clinics in Riyadh, Jeddah, Dammam "
		"and other branches on one platform. Monitor revenue, appointments, doctor "
		"performance, patient visits, pharmacy sales, inventory, purchases, expenses, "
		"receivables and profitability from centralized dashboards. Arabic and English "
		"documents, VAT and ZATCA e-invoicing workflows can sit on the same ERPNext finance "
		"backbone used by the rest of the organisation."
	)
	doc.localization_chips = (
		"Riyadh · Jeddah · Dammam\nArabic / English\nVAT & ZATCA workflows\nCentral dashboards"
	)

	doc.reports_heading = "Healthcare analytics when management needs them"
	doc.reports_image = dashboard
	doc.reports_image_alt = "Healthcare appointments, revenue, pharmacy and inventory reports"
	doc.set(
		"report_items",
		[
			{"title": title, "sort_order": idx}
			for idx, title in enumerate(
				[
					"Today's appointments",
					"Completed consultations",
					"Waiting patients",
					"New patients",
					"Daily and monthly revenue",
					"Pharmacy sales",
					"Appointments by department",
					"Patients by doctor",
					"Doctor utilization",
					"Lab tests and procedures",
					"Outstanding receivables",
					"Branch profitability",
					"Low-stock medicines",
					"Expiring batches",
				],
				start=1,
			)
		],
	)

	doc.dashboard_heading = "Turn operational data into management decisions"
	doc.dashboard_body = (
		"Bring today's appointments, waiting patients, revenue and pharmacy sales together "
		"with department load, doctor utilization, cancellation rate, lab and procedure "
		"volume, receivables, branch profitability, low-stock medicines, expiring batches "
		"and purchase requirements — clinical, operational and financial data on one dashboard."
	)
	doc.dashboard_image = dashboard
	doc.dashboard_image_alt = "Healthcare ERP dashboard with appointments, revenue and inventory KPIs"

	doc.audience_heading = "Built for different healthcare organisations"
	doc.set(
		"audience_items",
		[
			{"title": "Hospitals", "description": "Integrated clinical, inpatient and enterprise operations.", "sort_order": 1},
			{"title": "Multi-specialty clinics", "description": "Doctors, departments, appointments, billing and pharmacy.", "sort_order": 2},
			{"title": "Medical centers", "description": "Centralized patient and administrative management.", "sort_order": 3},
			{"title": "Dental clinics", "description": "Appointments, procedures, patient records and billing.", "sort_order": 4},
			{"title": "Physiotherapy & rehabilitation", "description": "Treatment sessions, practitioners and patient history.", "sort_order": 5},
			{"title": "Diagnostic centers & laboratories", "description": "Investigation workflow and result management, including patient-app results.", "sort_order": 6},
			{"title": "Day surgery centers", "description": "Procedures, supplies, billing and patient records.", "sort_order": 7},
			{"title": "Healthcare groups", "description": "Central control across multiple branches and legal entities.", "sort_order": 8},
		],
	)

	doc.integration_heading = "Healthcare sits on the same ERP as the rest of the business"
	related = [
		{
			"related_website_product": frappe.db.get_value("Website Product", {"slug": "finance"}, "name"),
			"display_name_override": "Finance",
			"summary_override": "Patient invoices, receivables and the ledger",
			"href": "/software/erpnext/finance",
			"sort_order": 1,
		},
		{
			"display_name_override": "Inventory",
			"summary_override": "Pharmacy, consumables and warehouses",
			"href": "/software/erpnext/inventory",
			"sort_order": 2,
		},
		{
			"display_name_override": "HR & Payroll",
			"summary_override": "Doctors, nurses, shifts and salary",
			"href": "/software/erpnext/hr-project-management",
			"sort_order": 3,
		},
		{
			"related_website_product": parent_name,
			"display_name_override": "ERPNext",
			"summary_override": "The ERP platform under Healthcare",
			"href": "/software/erpnext",
			"sort_order": 4,
		},
	]
	doc.set("related_products", related)

	doc.implementation_heading = "Why Printechs for Healthcare ERP?"
	doc.implementation_cta_label = "Discuss Your Requirements"
	doc.implementation_cta_href = "/contact"
	doc.set(
		"support_items",
		[
			{
				"icon": "integration",
				"title": "Healthcare + ERP",
				"description": "Clinical workflows with finance, procurement, inventory, HR and assets.",
				"sort_order": 1,
			},
			{
				"icon": "print",
				"title": "Customizable",
				"description": "Adapt workflows, forms, reports and approvals to how your facility works.",
				"sort_order": 2,
			},
			{
				"icon": "cloud",
				"title": "Cloud or private deployment",
				"description": "Deploy to the organisation's infrastructure strategy.",
				"sort_order": 3,
			},
			{
				"icon": "store",
				"title": "Multi-branch ready",
				"description": "Centralize hospitals, clinics and medical centers.",
				"sort_order": 4,
			},
			{
				"icon": "connectivity",
				"title": "Integration ready",
				"description": "Connect payment, communication or other healthcare systems through APIs.",
				"sort_order": 5,
			},
			{
				"icon": "device",
				"title": "Paperless patient app",
				"description": "Online and mobile booking plus results the patient can open on their phone.",
				"sort_order": 6,
			},
			{
				"icon": "training",
				"title": "Saudi Arabia support",
				"description": "Implementation, customization, training and support from Printechs.",
				"sort_order": 7,
			},
			{
				"icon": "maintenance",
				"title": "Post-go-live care",
				"description": "Hypercare after the first clinics go live on the connected record.",
				"sort_order": 8,
			},
		],
	)

	doc.set(
		"faq_items",
		[
			{
				"question": "Is this only patient registration software?",
				"answer": (
					"<p>No. Printechs Healthcare ERP connects patient care with hospital operations "
					"and business management: appointments, EMR, pharmacy, laboratory, procedures, "
					"inpatient, inventory, procurement, assets, HR, billing and accounting.</p>"
				),
				"sort_order": 1,
			},
			{
				"question": "Can patients book online or on mobile?",
				"answer": (
					"<p>Yes. Patients can book at reception, online or from a mobile application. "
					"Reminders and follow-up appointments stay on the same schedule doctors and "
					"reception already use.</p>"
				),
				"sort_order": 2,
			},
			{
				"question": "Can patients see laboratory results in the mobile app?",
				"answer": (
					"<p>Yes. When results are published to the patient record they can be opened "
					"in the mobile application, so the journey can stay paperless instead of "
					"printed reports collected at the counter.</p>"
				),
				"sort_order": 3,
			},
			{
				"question": "Does a clinic need inpatient features?",
				"answer": (
					"<p>No. Clinics can start with patients, appointments, EMR, pharmacy, laboratory "
					"and billing. Hospitals add admission, wards, beds, movement and discharge when "
					"they need them.</p>"
				),
				"sort_order": 4,
			},
			{
				"question": "How does pharmacy stay accurate?",
				"answer": (
					"<p>Prescriptions connect to ERPNext inventory: batch, expiry, locations, "
					"dispensing, purchase and valuation. You can see what was prescribed, what was "
					"dispensed and what must be reordered.</p>"
				),
				"sort_order": 5,
			},
			{
				"question": "Can we run several branches in Saudi Arabia?",
				"answer": (
					"<p>Yes. Head office can monitor clinics and medical centers — for example in "
					"Riyadh, Jeddah and Dammam — for revenue, appointments, pharmacy, inventory and "
					"profitability.</p>"
				),
				"sort_order": 6,
			},
			{
				"question": "What is the product called?",
				"answer": (
					"<p>On this site it is Printechs Healthcare ERP powered by ERPNext. Implementation "
					"uses the current ERPNext healthcare application architecture; naming of that "
					"app can change without changing what your teams use every day.</p>"
				),
				"sort_order": 7,
			},
		],
	)

	doc.set("visual_story_items", [])
	doc.set("capability_items", [])

	doc.flags.ignore_permissions = True
	doc.save()
	_link_parent_healthcare_section(parent_name)
	return {"slug": "healthcare", "canonical_path": doc.canonical_path}
