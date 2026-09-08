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
		"Plan production, manage Bills of Materials, calculate material requirements, issue Work Orders "
		"and track shop-floor operations against live stock and cost.\n\n"
		"This is the core Manufacturing module. Industry-specific factory stories stay in the "
		"Manufacturing section further down this page."
	),
	"People & Projects": (
		"Manage the employee lifecycle, attendance, leave and payroll, then post salary to Finance. "
		"Projects, timesheets and expenses use the same people.\n\n"
		"This is the HR and Project Management module — Frappe HR and ERPNext Projects on one platform."
	),
}

MODULES = [
	{
		"card_heading": "Inventory",
		"slug": "inventory",
		"display_name": "Inventory Management",
		"subcategory": "Inventory & Stock",
		"tagline": "Real-time stock control across every warehouse",
		"hero_image": "software-warehouse-management-system.jpg",
		"hero_alt": "ERPNext inventory across warehouses with live stock, batches and valuation",
		"short": (
			"Manage stock, warehouses, batches, serial numbers, replenishment and inventory valuation "
			"from one integrated ERP platform."
		),
		"long": (
			"<p>ERPNext Inventory gives operations and finance the same live stock position. Receipts, "
			"transfers, deliveries and manufacturing consumption post to one item master and warehouse "
			"structure — so sales, purchasing and accounts are not working from a second spreadsheet.</p>"
			"<p>Standard ERPNext Inventory covers stock, warehouses, serials, batches, valuation, transfers, "
			"reconciliation and reorder. Bin-level putaway, directed picking and handheld warehouse execution "
			"sit on Printechs WMS and post back to this same inventory.</p>"
		),
		"benefits": [
			(
				"inventory",
				"Multi-warehouse inventory",
				"Track stock across branches, stores, central warehouses and transit locations with real-time visibility.",
			),
			(
				"scan",
				"Serial and batch traceability",
				"Track serial numbers, batches, expiry dates, supplier history and customer delivery through the inventory lifecycle.",
			),
			(
				"store",
				"Automatic stock replenishment",
				"Set reorder levels and quantities by warehouse and raise Material Requests when stock reaches the minimum.",
			),
			(
				"report",
				"Accurate valuation",
				"Stock movements update quantity and value so warehouse balances stay aligned with Finance.",
			),
		],
		"specs": [
			("inventory", "Multi-warehouse", "Branches, stores, central and transit"),
			("scan", "Serial & batch", "Serials, batches and expiry"),
			("store", "Auto replenishment", "Reorder rules and Material Requests"),
			("report", "Reconciliation", "Stock count with controlled posting"),
			("print", "Multiple UOM", "Piece, box, carton, kg, litre"),
			("device", "Barcode", "Receive, transfer and count"),
			("loyalty", "Item variants", "Size, colour, style as SKUs"),
			("lines", "Dimensions", "Extra stock dimensions for reporting"),
			("cloud", "Valuation", "FIFO and moving average"),
			("integration", "Connected ERP", "Purchase, sales, manufacturing, accounts"),
		],
		"sections": [
			(
				"Multi-warehouse inventory",
				"Track stock across branches, stores, central warehouses and transit locations with real-time visibility. "
				"Each warehouse keeps its own quantity and valuation, so retail, distribution and manufacturing teams "
				"see what is actually available to sell or consume.\n\n"
				"Opening balances and warehouse mapping are set once, then receipts, issues and transfers stay on "
				"the same structure sales and purchasing already use.",
			),
			(
				"Serial and batch traceability",
				"Track individual serial numbers, batches, expiry dates, supplier history and customer delivery "
				"throughout the complete inventory lifecycle. That supports recalls, warranty and regulated goods "
				"in industrial, pharmaceutical, electronics and distribution operations.\n\n"
				"Use batch and expiry where the item is lot-controlled. Use serial numbers where each unit must stay unique.",
			),
			(
				"Automatic stock replenishment",
				"Define reorder levels and reorder quantities by warehouse and automatically generate Material Requests "
				"when stock reaches minimum levels. Reorder rules sit on the Item, so replenishment follows how you "
				"actually buy and stock each SKU.\n\n"
				"Purchasing sees the request in time to raise a purchase order instead of discovering the shortage at the counter.",
			),
			(
				"Stock count and reconciliation",
				"Compare physical inventory against system stock and post controlled inventory adjustments while "
				"maintaining accurate stock valuation. ERPNext Stock Reconciliation is the counted, auditable posting "
				"— not an informal spreadsheet adjustment.\n\n"
				"Warehouse and finance see the same quantity and value after the count.",
			),
			(
				"Units, barcodes and item variants",
				"Purchase, store and sell products using different units such as Piece, Box, Carton, Kg or Litre "
				"with automatic conversion factors. Item barcodes speed receiving, transfers, stock counting and "
				"transaction processing.\n\n"
				"Item Variants keep size, colour, style and other attributes as independent SKUs — which matters "
				"for fashion and apparel as well as any business with option-level stock.",
			),
			(
				"Transfers, valuation and where WMS starts",
				"Internal transfers and material requests move stock between warehouses without breaking sales "
				"availability. Valuation methods such as FIFO or moving average stay on the same movement that "
				"updates quantity. Advanced inventory dimensions can add reporting detail beyond warehouse, batch "
				"and serial.\n\n"
				"ERPNext Inventory is stock, warehouses, batches, serials, valuation, transfers, reconciliation "
				"and reorder. Printechs WMS adds bin and location management, carton control, directed putaway, "
				"picking, cycle count and handheld scanning — and still posts back to this inventory.",
			),
		],
	},
	{
		"card_heading": "Sales & Purchase",
		"slug": "sales-purchase",
		"display_name": "Sales & Purchase Management",
		"subcategory": "Sales & Procurement",
		"tagline": "Manage the complete order-to-cash and procure-to-pay process",
		"hero_image": "software-modern-pos.jpg",
		"hero_alt": "ERPNext sales and purchase documents from order to invoice and payment",
		"short": (
			"Manage quotations, sales orders, purchase orders, deliveries, receipts, invoices, payments "
			"and supplier transactions from one integrated ERP platform."
		),
		"long": (
			"<p>ERPNext Sales and Purchase is the commercial process, not only invoice entry. The same item, "
			"party and price master carries a customer from quotation to payment, and a supplier from material "
			"request to payment, without retyping the order into a second system.</p>"
			"<p>CRM can start the sales cycle as a lead or opportunity. From there this page covers selling and "
			"buying documents. Sales and purchase transactions are fully integrated with ERPNext Inventory and "
			"Accounting.</p>"
		),
		"benefits": [
			(
				"checkout",
				"Order-to-cash",
				"Lead or opportunity, quotation, sales order, delivery, invoice and payment stay on one flow.",
			),
			(
				"inventory",
				"Procure-to-pay",
				"Material request, RFQ, supplier quotation, purchase order, receipt, invoice and payment stay linked.",
			),
			(
				"report",
				"Pricing and credit control",
				"Price lists, customer credit limits and payment terms sit on the same party master.",
			),
			(
				"integration",
				"Connected inventory and accounts",
				"Sales and purchase transactions are fully integrated with ERPNext Inventory and Accounting.",
			),
		],
		"specs": [
			("checkout", "Sales cycle", "Quote → order → delivery → invoice → payment"),
			("inventory", "Purchase cycle", "RFQ → PO → receipt → invoice → payment"),
			("report", "Pricing", "Customer, supplier and qty-based lists"),
			("store", "Credit control", "Limits, terms and due dates"),
			("scan", "RFQ & compare", "Supplier quotations before the PO"),
			("cloud", "Fulfilment", "Ordered, delivered, billed, pending"),
			("loyalty", "Returns", "Customer and supplier returns"),
			("shield", "Approvals", "Material request and PO workflows"),
			("print", "Partials", "Partial delivery and receipt"),
			("device", "Multi-currency", "Customer and supplier currencies"),
			("lines", "Landed cost", "Freight and import costs on purchases"),
			("integration", "Connected ERP", "Inventory and accounting"),
		],
		"sections": [
			(
				"Sales management",
				"ERPNext manages the complete sales cycle, not invoicing alone:\n\n"
				"Lead / Opportunity → Quotation → Sales Order → Delivery Note → Sales Invoice → Payment\n\n"
				"A lead or opportunity in CRM can start the process. This page is the commercial documents that "
				"follow — quotation through payment — on one customer, item and tax master.",
			),
			(
				"Purchase management",
				"The buying cycle is equally complete:\n\n"
				"Material Request → Request for Quotation → Supplier Quotation → Purchase Order → "
				"Purchase Receipt → Purchase Invoice → Payment\n\n"
				"Three-way match keeps supplier bills aligned with what was ordered and received, so finance "
				"is not paying from an unmatched spreadsheet.",
			),
			(
				"Customer and supplier pricing",
				"Maintain customer-specific, supplier-specific, quantity-based and promotional pricing using "
				"centralized Price Lists and Item Prices.\n\n"
				"Sales and procurement stop keeping separate Excel price books. The price that appears on the "
				"quotation is the price that can flow to the order and the invoice.",
			),
			(
				"Credit control and payment terms",
				"Define customer credit limits, payment terms and due dates to maintain better control over "
				"receivables and sales exposure. That matters for Saudi B2B companies that sell on credit.\n\n"
				"Limits and terms sit on the customer record used by quotation, sales order and invoice.",
			),
			(
				"Supplier RFQ and quotation management",
				"Send Requests for Quotation to multiple suppliers, capture supplier quotations and compare "
				"pricing before placing the Purchase Order.\n\n"
				"Buyers see competing quotes in the same process that later becomes the PO, receipt and bill.",
			),
			(
				"Order fulfilment and partials",
				"Track ordered, delivered, billed and pending quantities in real time for every Sales Order "
				"and Purchase Order.\n\n"
				"Handle partial customer deliveries and partial supplier receipts while tracking pending "
				"quantities against the original order — typical for distribution and trading.",
			),
			(
				"Sales and purchase returns",
				"Process customer returns and supplier returns while automatically updating stock, outstanding "
				"amounts and accounting records.\n\n"
				"Returns are explicit documents, not a hidden adjustment inside generic transaction management.",
			),
			(
				"Purchase approval workflows",
				"Configure approval levels for Material Requests, Purchase Orders and other purchasing "
				"transactions based on company policies and authorization limits.\n\n"
				"That is how purchasing stays controlled as volume and value grow.",
			),
			(
				"Multi-currency and landed cost",
				"Create customer and supplier transactions in multiple currencies while ERPNext maintains "
				"company currency values and exchange-rate impact. That is common for Saudi companies that "
				"buy internationally.\n\n"
				"Landed cost is a purchase capability: allocate freight, customs, transportation and other "
				"import costs to received inventory for more accurate product valuation. It is not a sales feature.",
			),
			(
				"Inventory and accounting integration",
				"Sales and purchase transactions are fully integrated with ERPNext Inventory and Accounting. "
				"Deliveries and receipts update stock; invoices and payments update receivables, payables and "
				"the ledger.\n\n"
				"Warehouses, batches, serials and valuation are covered on the Inventory page. This page stays "
				"on the commercial documents that drive those postings.",
			),
		],
	},
	{
		"card_heading": "Manufacturing",
		"slug": "manufacturing-module",
		"display_name": "Manufacturing Software",
		"subcategory": "Manufacturing",
		"tagline": "Plan. Produce. Control. Improve.",
		"hero_image": "software-warehouse-management-system.jpg",
		"hero_alt": "ERPNext manufacturing from production planning to finished goods",
		"short": (
			"Run your complete manufacturing operation from material planning to finished goods. "
			"Plan production, manage Bills of Materials, calculate material requirements, schedule "
			"workstations, issue Work Orders, track shop-floor operations, inspect quality and "
			"calculate manufacturing cost from one integrated ERP platform."
		),
		"long": (
			"<p>Whether you manufacture made-to-stock products, produce against customer orders, "
			"assemble multi-level products or outsource part of production, ERPNext gives production, "
			"inventory, purchasing and finance one connected system.</p>"
			"<p>From production planning through shop-floor execution, material consumption and "
			"finished-goods receipt, information flows through one integrated ERP — not a separate "
			"planning spreadsheet next to the factory.</p>"
		),
		"benefits": [
			(
				"report",
				"Plan from real demand",
				"Turn sales orders or forecasts into production plans, material requirements and Work Orders.",
			),
			(
				"print",
				"Control the shop floor",
				"Work Orders, Job Cards, workstations and quality inspections track what the factory actually did.",
			),
			(
				"inventory",
				"See materials in production",
				"Separate raw material, WIP and finished goods so planners know what is available to make and ship.",
			),
			(
				"integration",
				"Know what it really cost",
				"Compare expected BOM cost with actual consumption, operations, scrap and finished-goods receipt.",
			),
		],
		"specs": [
			("report", "Production planning", "Sales orders, multi-item plans, shortages"),
			("print", "Bill of Materials", "Materials, operations, scrap and cost"),
			("lines", "Multi-level BOM", "Components and sub-assemblies"),
			("device", "Routing", "Operations, sequence and workstations"),
			("store", "Work Orders", "What, how much, where and when"),
			("scan", "Job Cards", "Shop-floor time, qty and scrap"),
			("shield", "Quality", "In-process, incoming and outgoing"),
			("cloud", "Capacity", "Workstation hours and load"),
			("inventory", "Subcontracting", "Supply materials, receive processed goods"),
			("zatca", "Costing", "Expected versus actual production cost"),
			("loyalty", "Make-to-order", "From sales order to delivery"),
			("integration", "Connected ERP", "Sales, purchase, stock, accounts"),
		],
		"sections": [
			(
				"Complete manufacturing control from one system",
				"ERPNext connects the complete manufacturing lifecycle:\n\n"
				"Customer Demand / Forecast → Production Planning → Material Requirement Planning → "
				"Purchase / Material Availability → Bill of Materials → Work Order → "
				"Material Transfer to Production → Operations & Job Cards → Quality Inspection → "
				"Finished Goods → Inventory & Accounting\n\n"
				"Production, stores and finance work from the same documents instead of reconciling three lists at month end.",
			),
			(
				"Production planning and material requirements",
				"Turn demand into an actionable plan. Create Production Plans from Sales Orders or internal "
				"requirements, then calculate what must be manufactured and what must be purchased — including "
				"multi-level BOM items and sub-assemblies.\n\n"
				"Plans can generate Work Orders for production and Material Requests for shortages, and let "
				"planners review required versus available materials across several demands.",
			),
			(
				"Bills of Materials and multi-level products",
				"A BOM is the manufacturing recipe: raw materials, components, sub-assemblies, operations, "
				"workstations, scrap, quantities and operating cost. ERPNext uses it for planning, material "
				"requirements and expected product cost.\n\n"
				"Multi-level BOMs support Raw Materials → Components → Sub-Assemblies → Finished Product, "
				"so a machine can have its own motor, panel and frame assemblies — each with its own BOM. "
				"Planning can treat a sub-assembly as manufactured, subcontracted or purchased.",
			),
			(
				"Routing, operations and workstations",
				"Define how a product moves through the factory — for example Cutting → Machining → Welding → "
				"Assembly → Painting → Inspection → Packing. Each operation can have a default workstation, "
				"standard time and cost.\n\n"
				"A workstation may be a machine, line, cell or department, with working hours, capacity and "
				"operating cost. That information feeds Job Cards, scheduling and capacity planning.",
			),
			(
				"Work Orders and material to production",
				"A Work Order tells the floor what to make, how much, which materials and operations to use, "
				"and which warehouses to pull from and receive into — including source, WIP, finished goods "
				"and scrap warehouses. It can be created from a Production Plan or directly.\n\n"
				"Typical material flow: Raw Material Warehouse → Material Transfer for Manufacture → "
				"Work-In-Progress → Production → Finished Goods Warehouse. Transfers can be against the "
				"Work Order or, depending on setup, against Job Cards.",
			),
			(
				"Job Cards, WIP and actual consumption",
				"When a Work Order has operations, Job Cards track the operation, workstation, employee, "
				"planned and completed quantity, start and finish time, scrap and quality. Supervisors "
				"follow progress against the Work Order instead of a whiteboard.\n\n"
				"WIP warehouses separate raw material, production and finished goods. Actual consumption "
				"can be recorded — including continuous consumption — so you see material variance, "
				"wastage and efficiency, not only theoretical BOM quantities.",
			),
			(
				"Quality, scrap and finished goods",
				"Quality Inspection can run during production from Job Cards, using templates for weight, "
				"dimension, finish, colour, strength or visual checks — numeric, value or formula based. "
				"Incoming, outgoing and in-process inspections are supported.\n\n"
				"Job Cards can record scrap and process loss so inventory matches the floor. When production "
				"completes, finished goods are received and become available for sales and distribution.",
			),
			(
				"Capacity, scheduling, costing and downtime",
				"Capacity planning uses workstation hours, holidays, overtime and existing jobs to show "
				"whether the factory can meet the plan. Operations can be scheduled from planned start date, "
				"operation time and workstation availability.\n\n"
				"Costing brings together raw materials, components, sub-assemblies, workstation and operation "
				"cost, scrap and actual consumption so you can compare expected versus actual manufacturing "
				"cost. Downtime entries record machine unavailability — failure, maintenance, material "
				"shortage, setup or operator — for bottleneck analysis.",
			),
			(
				"Subcontracting and traceability",
				"When part of production is outsourced, ERPNext can supply raw materials to a subcontractor "
				"and receive processed goods back: Purchase / Subcontract Order → materials supplied → "
				"supplier processing → subcontracting receipt.\n\n"
				"Batch and serial control stays with Inventory. Manufacturing can carry purchased material "
				"through production to a finished-goods batch or serial and then to the customer — useful "
				"for food, pharma, cosmetics, electronics and industrial products. Detail on batches and "
				"serials is on the Inventory page.",
			),
			(
				"Make-to-order, make-to-stock and connected ERP",
				"Make-to-order: Customer Enquiry → Quotation → Sales Order → Production Plan → material "
				"requirement → Work Order → production → finished goods → delivery → sales invoice.\n\n"
				"Make-to-stock: demand or stock requirement → Production Plan → material planning → "
				"Work Orders → manufacturing → finished goods inventory → later sales orders.\n\n"
				"Sales can drive demand. Purchase covers shortages. Inventory holds raw material, WIP and "
				"finished goods. Quality inspects incoming, in-process and outgoing items. Accounting "
				"receives valuation and manufacturing postings.",
			),
		],
	},
	{
		"card_heading": "People & Projects",
		"slug": "hr-project-management",
		"display_name": "HR & Project Management",
		"subcategory": "HR, Payroll & Projects",
		"tagline": "Manage Your Workforce. Run Payroll. Deliver Projects.",
		"hero_image": "software-erpnext.jpg",
		"hero_alt": "ERPNext HR, payroll, leave and project timesheets",
		"short": (
			"Manage the complete employee lifecycle, attendance, leave, payroll, expenses, performance "
			"and project operations from one integrated platform. ERPNext with Frappe HR connects "
			"employees, HR processes, payroll, projects, timesheets, expenses and accounting."
		),
		"long": (
			"<p>From recruitment and onboarding through attendance, leave, payroll and employee "
			"separation, Frappe HR keeps workforce information in one place — with approvals and "
			"day-to-day HR services employees can use themselves.</p>"
			"<p>ERPNext Projects then use those same people for tasks, timesheets, expenses and "
			"billing, so HR, project managers and finance are not reconciling three lists at month end.</p>"
		),
		"benefits": [
			(
				"loyalty",
				"One employee record",
				"Profiles, organisation structure, documents and career history stay on a single master.",
			),
			(
				"report",
				"Time that feeds payroll",
				"Attendance, shifts, leave and check-in become the working days salary actually uses.",
			),
			(
				"zatca",
				"Payroll on the ledger",
				"Salary structures, slips and salary expense post to Finance after review.",
			),
			(
				"cloud",
				"Projects on the same people",
				"Tasks, timesheets, expenses and billing sit on the workforce you already pay.",
			),
		],
		"specs": [
			("loyalty", "Employee master", "Profile, department, grade and documents"),
			("report", "Recruitment", "Staffing plan to job offer to employee"),
			("print", "Onboarding", "Assigned joining activities across teams"),
			("scan", "Attendance", "Present, absent, leave and half day"),
			("device", "Check-in", "Mobile check-in with geolocation"),
			("cloud", "Shifts", "General, night, factory and store"),
			("report", "Leave", "Types, policies, balances and holidays"),
			("zatca", "Expenses", "Claims, advances and approvals"),
			("shield", "Performance", "Cycles, KRAs and appraisals"),
			("zatca", "Payroll", "Components, structures, slips, posting"),
			("device", "Self-service", "Leave, expenses, profile and salary"),
			("integration", "Projects", "Tasks, timesheets, cost and billing"),
		],
		"sections": [
			(
				"Employee master and organisation structure",
				"Build a central employee database with the structure of the business: employee ID, "
				"employment type, department, branch, designation, grade, reporting manager, joining "
				"date, status, company, previous experience, contacts, emergency contacts and documents.\n\n"
				"Frappe HR organisation masters include Employment Type, Branch, Department, Designation "
				"and Grade — so HR, payroll and projects refer to the same people.",
			),
			(
				"Recruitment, onboarding and career movement",
				"Hiring can run inside HR: Staffing Requirement → Job Opening → Job Applicant → "
				"Interview → Job Offer → Employee. That includes staffing plans, interview rounds and "
				"feedback, offer tracking and conversion to an employee record.\n\n"
				"Onboarding activities — documents, orientation, IT accounts, laptop, email, department "
				"introduction, policy acknowledgement, training, ID and probation — can be assigned "
				"across teams and tracked in one place. Transfers, promotions and changes to department, "
				"branch, designation, grade or manager keep a career history on the same employee.",
			),
			(
				"Attendance, check-in and shifts",
				"Daily attendance can record Present, Absent, On Leave or Half Day, including shift-based "
				"attendance, late or missing review, monthly attendance reports and attendance-linked payroll.\n\n"
				"Employees can check in and check out from supported Frappe HR interfaces, including "
				"mobile with geolocation — useful for sales, service engineers, field and site staff, "
				"multi-branch and remote teams. Shifts (general, morning, evening, night, rotational, "
				"store or factory) then drive both attendance and payroll.",
			),
			(
				"Leave, holidays, expenses and advances",
				"Replace leave spreadsheets with leave types, policies, allocation, applications, "
				"approvals, balances and leave without pay — annual, sick, emergency, unpaid, "
				"compensatory, maternity or company-specific. Holiday Lists can differ for head office, "
				"branches, factories, stores or regions.\n\n"
				"Expense claims cover travel, transport, accommodation, meals, fuel, telephone, client "
				"entertainment, office purchases and project expenses, with multi-level approval into "
				"Accounting. Employee advances for travel, projects, site work or purchases can be "
				"settled against those claims.",
			),
			(
				"Performance, separation and HR visibility",
				"Appraisal cycles, templates, goals and Key Result Areas support self-appraisal, manager "
				"evaluation and a performance history instead of a side spreadsheet.\n\n"
				"Separation covers resignation, exit interview, asset return, document and department "
				"clearance, final settlement and status update so HR, Finance, IT and operations finish "
				"the same checklist. Reports include employee information, department headcount, "
				"attendance, leave balance and usage, salary register, expenses, performance and recruitment.",
			),
			(
				"Salary components, structures and assignment",
				"Configure earnings — basic, housing, transport, telephone, food, overtime, bonus, "
				"commission and other allowances — and deductions such as absence, unpaid leave, loans "
				"and advances. Components can use conditions and formulas.\n\n"
				"Reusable Salary Structures (management, sales, technician, retail, factory) standardise "
				"earnings and deductions by group. Assign a structure to each employee with effective "
				"date, base amount and payroll frequency so compensation changes have a controlled history.",
			),
			(
				"Payroll processing and accounting",
				"Working days can come from Attendance or Leave Applications — present, absence, leave, "
				"leave without pay, working days and holidays. Payroll Entry generates Salary Slips in "
				"bulk by company, branch, department, designation or frequency.\n\n"
				"Typical flow: Attendance & Leave → Salary Structure → Additional Salary / Adjustments → "
				"Payroll Entry → Salary Slips → Accounting Entry → Salary Payment. Additional salary "
				"covers bonus, commission, overtime, incentives, arrears and one-time items. Each slip "
				"shows earnings, deductions, gross, working days, LWP, additional salary and net pay. "
				"Salary expense then posts as payable / payroll liability, payment and general ledger.",
			),
			(
				"Employee self-service and approval workflows",
				"Employees can apply for leave, review balances, check in, view their profile, submit "
				"expense claims and advances, review salary information and take part in appraisals — "
				"including from the Frappe HR mobile app for leave, attendance and profile.\n\n"
				"Configurable approvals cover leave, expenses, advances, recruitment, salary changes and "
				"other HR documents, so management has an auditable path instead of email threads.",
			),
			(
				"Project planning, tasks and templates",
				"ERPNext Projects hold customer, project type, dates, estimated cost, status, manager "
				"and team. Tasks break the work down: owner, status, priority, dates, dependencies, "
				"progress and department, with Gantt visualisation where you need it.\n\n"
				"Project templates standardise repeated work — ERP implementations, equipment "
				"installations, maintenance contracts, construction, consulting, software development "
				"or retail rollouts — so the next project starts from a known task structure.",
			),
			(
				"Timesheets, project cost and one connected platform",
				"Employees record time against Project → Task → Activity, with activity type, hours, "
				"billable hours, billing rate and costing rate. Project cost can include estimated cost, "
				"timesheet cost, expense claims, purchase invoices, billed amount and revenue — so you "
				"can see Sales Revenue minus time, expenses and material cost.\n\n"
				"Billable timesheets suit consulting, software, engineering, support and installation. "
				"The same chain then runs through the ERP: Employees → Attendance & Leave → Payroll → "
				"Projects & Tasks → Timesheets → Expenses → Customer Billing → Accounting.",
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


def fill_erpnext_inventory():
	"""Update Inventory page copy only. Does not rewrite other core-module pages."""
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
	spec = next(row for row in MODULES if row["slug"] == "inventory")
	_fill_module(parent_name, spec, images)

	doc = frappe.get_doc("Website Product", {"slug": "inventory"})
	doc.category_label = "ERPNext Core Module"
	doc.hero_trust_chips = (
		"Multi-Warehouse Inventory\nSerial & Batch Tracking\nAutomatic Replenishment\nReal-Time Valuation"
	)
	doc.hero_secondary_cta_label = "Explore ERPNext"
	doc.hero_secondary_cta_href = "/software/erpnext#modules"
	doc.meta_title = "ERPNext Inventory Management Software Saudi Arabia | Printechs"
	doc.meta_description = (
		"ERPNext inventory management: multi-warehouse stock, serial and batch tracking, "
		"automatic replenishment, stock reconciliation, multiple UOM, barcodes and item variants "
		"connected to sales, purchasing, manufacturing and finance."
	)
	doc.final_cta_heading = "See live stock across every warehouse"
	doc.final_cta_description = (
		"Walk through multi-warehouse inventory, serial and batch tracking, reorder rules "
		"and valuation against your items and locations."
	)
	related = [
		{
			"display_name_override": "Sales",
			"summary_override": "Availability, delivery and invoices",
			"href": "/software/erpnext/sales-purchase",
			"sort_order": 1,
		},
		{
			"display_name_override": "Purchase",
			"summary_override": "Receipts and supplier stock",
			"href": "/software/erpnext/sales-purchase",
			"sort_order": 2,
		},
		{
			"display_name_override": "Manufacturing",
			"summary_override": "Material issue and finished goods",
			"href": "/software/erpnext/manufacturing-module",
			"sort_order": 3,
		},
		{
			"related_website_product": frappe.db.get_value("Website Product", {"slug": "finance"}, "name"),
			"display_name_override": "Finance",
			"summary_override": "Stock valuation and the ledger",
			"href": "/software/erpnext/finance",
			"sort_order": 4,
		},
	]
	wms_name = published_name("warehouse-management-system")
	if wms_name:
		related.append(
			{
				"related_website_product": wms_name,
				"display_name_override": "Printechs WMS",
				"summary_override": "Bins, putaway, picking and handheld execution",
				"href": "/software/warehouse-management-system",
				"sort_order": 5,
			}
		)
	doc.set("related_products", related)
	doc.flags.ignore_permissions = True
	doc.save()
	return {"slug": "inventory", "canonical_path": doc.canonical_path}


def fill_erpnext_sales_purchase():
	"""Update Sales & Purchase page copy only. Does not rewrite other core-module pages."""
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
	spec = next(row for row in MODULES if row["slug"] == "sales-purchase")
	_fill_module(parent_name, spec, images)

	doc = frappe.get_doc("Website Product", {"slug": "sales-purchase"})
	doc.category_label = "ERPNext Core Module"
	doc.hero_trust_chips = (
		"Order-to-Cash\nProcure-to-Pay\nCredit Control\nSupplier RFQ"
	)
	doc.hero_secondary_cta_label = "Explore ERPNext"
	doc.hero_secondary_cta_href = "/software/erpnext#modules"
	doc.meta_title = "ERPNext Sales & Purchase Software Saudi Arabia | Printechs"
	doc.meta_description = (
		"ERPNext sales and purchase: quotations, sales orders, purchase orders, deliveries, "
		"receipts, invoices, credit control, supplier RFQ, returns, approvals, multi-currency "
		"and landed cost — integrated with inventory and accounting."
	)
	doc.final_cta_heading = "See order-to-cash and procure-to-pay in one system"
	doc.final_cta_description = (
		"Walk through quotations, sales orders, purchase orders, credit limits, RFQ comparison "
		"and landed cost against your items and parties."
	)
	doc.set(
		"related_products",
		[
			{
				"display_name_override": "Inventory",
				"summary_override": "Deliveries, receipts and stock",
				"href": "/software/erpnext/inventory",
				"sort_order": 1,
			},
			{
				"related_website_product": frappe.db.get_value("Website Product", {"slug": "finance"}, "name"),
				"display_name_override": "Finance",
				"summary_override": "Receivables, payables and the ledger",
				"href": "/software/erpnext/finance",
				"sort_order": 2,
			},
			{
				"display_name_override": "Manufacturing",
				"summary_override": "Material demand from orders",
				"href": "/software/erpnext/manufacturing-module",
				"sort_order": 3,
			},
			{
				"related_website_product": parent_name,
				"display_name_override": "ERPNext",
				"summary_override": "Full platform and industry solutions",
				"href": "/software/erpnext",
				"sort_order": 4,
			},
		],
	)
	doc.flags.ignore_permissions = True
	doc.save()
	return {"slug": "sales-purchase", "canonical_path": doc.canonical_path}


def fill_erpnext_manufacturing():
	"""Update Manufacturing page copy only. Does not rewrite other core-module pages."""
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
	spec = next(row for row in MODULES if row["slug"] == "manufacturing-module")
	_fill_module(parent_name, spec, images)

	doc = frappe.get_doc("Website Product", {"slug": "manufacturing-module"})
	doc.category_label = "ERPNext Core Module"
	doc.story_heading = "Complete manufacturing control from one system"
	doc.hero_trust_chips = (
		"Production Planning\nMulti-level BOM\nShop-Floor Control\nManufacturing Costing"
	)
	doc.hero_primary_cta_label = "Schedule a Demo"
	doc.hero_primary_cta_href = "/request-demo"
	doc.hero_secondary_cta_label = "Talk to Our ERPNext Manufacturing Team"
	doc.hero_secondary_cta_href = "/contact"
	doc.meta_title = "ERPNext Manufacturing Software Saudi Arabia | Printechs"
	doc.meta_description = (
		"ERPNext manufacturing software: production planning, BOM, Work Orders, Job Cards, "
		"quality, subcontracting, costing and shop-floor control — connected to sales, "
		"purchase, inventory and accounting in Saudi Arabia."
	)
	doc.final_cta_heading = "Run your factory with better visibility"
	doc.final_cta_description = (
		"Connect sales demand, materials, purchasing, production, quality, inventory and "
		"accounting. Plan what to manufacture, know what materials you need, track what "
		"the factory produced, and measure what it actually cost."
	)
	doc.final_cta_primary_label = "Schedule an ERPNext Manufacturing Demo"
	doc.final_cta_primary_href = "/request-demo"
	doc.final_cta_secondary_label = "Talk to Our Manufacturing ERP Team"
	doc.final_cta_secondary_href = "/contact"
	doc.audience_heading = "Designed for different manufacturing industries"
	doc.implementation_heading = "Why ERPNext Manufacturing with Printechs?"
	doc.implementation_cta_label = "Talk to Our Manufacturing ERP Team"
	doc.implementation_cta_href = "/contact"
	doc.process_heading = "The manufacturing lifecycle"
	doc.process_subheading = (
		"From customer demand through shop-floor execution to inventory and accounting."
	)
	doc.integration_heading = "Manufacturing does not operate in isolation"
	doc.set(
		"page_section_order",
		[
			{"section": section, "sort_order": idx}
			for idx, section in enumerate(
				[
					"overview",
					"process_steps",
					"benefits",
					"icon_specifications",
					"content_sections",
					"applications",
					"related_products",
					"support",
				],
				start=1,
			)
		],
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "Demand",
				"title": "Customer Demand / Forecast → Production Planning",
				"description": "Sales Orders or internal requirements become a production plan.",
				"sort_order": 1,
			},
			{
				"group_title": "Materials",
				"title": "MRP → Purchase / Availability → Bill of Materials",
				"description": "Required finished goods, sub-assemblies and raw materials are calculated before production starts.",
				"sort_order": 2,
			},
			{
				"group_title": "Execution",
				"title": "Work Order → Material Transfer → Job Cards → Quality",
				"description": "The floor is told what to make, materials move to WIP, operations are tracked and inspected.",
				"sort_order": 3,
			},
			{
				"group_title": "Output",
				"title": "Finished Goods → Inventory & Accounting",
				"description": "Completed production updates stock availability and manufacturing cost in the same ERP.",
				"sort_order": 4,
			},
		],
	)
	doc.set(
		"audience_items",
		[
			{"title": "Food & Beverage", "description": "Recipes/BOM, batch production, raw-material control and traceability.", "sort_order": 1},
			{"title": "Pharmaceutical & Cosmetics", "description": "Batch management, quality inspections, controlled materials and expiry.", "sort_order": 2},
			{"title": "Plastics", "description": "Raw-material consumption, machines, operations, scrap and finished products.", "sort_order": 3},
			{"title": "Metal Fabrication", "description": "Cutting, machining, welding, finishing, assembly and subcontracting.", "sort_order": 4},
			{"title": "Electrical & Electronics", "description": "Multi-level BOM, component management, assembly, serials and quality.", "sort_order": 5},
			{"title": "Machinery & Equipment", "description": "Complex BOMs, sub-assemblies, Work Orders and operation-level tracking.", "sort_order": 6},
			{"title": "Packaging", "description": "Production planning, material consumption, workstation scheduling and waste control.", "sort_order": 7},
			{"title": "Building Materials", "description": "Bulk material planning, production control, quality and inventory integration.", "sort_order": 8},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "Manufacturing process study", "description": "Map how planning, stores and the shop floor work today.", "sort_order": 1},
			{"icon": "print", "title": "BOM and routing setup", "description": "Migrate BOMs, operations and workstations that match real products.", "sort_order": 2},
			{"icon": "report", "title": "Production planning", "description": "Configure plans, material requests and Work Order generation.", "sort_order": 3},
			{"icon": "device", "title": "Shop-floor processes", "description": "Job Cards, quality, scrap and barcode where the team needs them.", "sort_order": 4},
			{"icon": "inventory", "title": "Warehouse integration", "description": "Raw material, WIP and finished-goods warehouses on one stock.", "sort_order": 5},
			{"icon": "cloud", "title": "Reports and dashboards", "description": "Work Order, Job Card, quality and downtime visibility for managers.", "sort_order": 6},
			{"icon": "training", "title": "Training", "description": "Role-based sessions for planners, stores and operators.", "sort_order": 7},
			{"icon": "maintenance", "title": "Post-go-live support", "description": "Local Saudi implementation support after the first production cycles.", "sort_order": 8},
		],
	)
	doc.set(
		"related_products",
		[
			{
				"display_name_override": "Sales",
				"summary_override": "Sales Orders that drive production",
				"href": "/software/erpnext/sales-purchase",
				"sort_order": 1,
			},
			{
				"display_name_override": "Purchase",
				"summary_override": "Material Requests for shortages",
				"href": "/software/erpnext/sales-purchase",
				"sort_order": 2,
			},
			{
				"display_name_override": "Inventory",
				"summary_override": "Raw material, WIP and finished goods",
				"href": "/software/erpnext/inventory",
				"sort_order": 3,
			},
			{
				"related_website_product": frappe.db.get_value("Website Product", {"slug": "finance"}, "name"),
				"display_name_override": "Finance",
				"summary_override": "Manufacturing cost and valuation",
				"href": "/software/erpnext/finance",
				"sort_order": 4,
			},
		],
	)
	doc.flags.ignore_permissions = True
	doc.save()
	_wire_parent_cards(parent_name, {"Manufacturing": "/software/erpnext/manufacturing-module"})
	return {"slug": "manufacturing-module", "canonical_path": doc.canonical_path}


HR_PROJECT_PATH = "/software/erpnext/hr-project-management"


def _relink_people_projects_urls():
	"""Point existing Desk links at the renamed HR & Project Management slug."""
	old = "/software/erpnext/people-projects"
	for doctype, field in (
		("Website Product Related", "href"),
		("Website Product Connection Item", "href"),
		("Website Product Content Section", "link_href"),
	):
		if not frappe.db.exists("DocType", doctype):
			continue
		for name in frappe.get_all(doctype, filters={field: old}, pluck="name"):
			frappe.db.set_value(doctype, name, field, HR_PROJECT_PATH, update_modified=False)


def fill_erpnext_hr_project_management():
	"""Update HR & Project Management copy only. Does not rewrite other core-module pages."""
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
	spec = next(row for row in MODULES if row["slug"] == "hr-project-management")
	_fill_module(parent_name, spec, images)

	doc = frappe.get_doc("Website Product", {"slug": "hr-project-management"})
	doc.category_label = "ERPNext Core Module"
	doc.story_heading = "Complete HR management"
	doc.hero_trust_chips = "Employee Lifecycle\nPayroll\nTimesheets\nConnected Accounting"
	doc.hero_primary_cta_label = "Schedule a Demo"
	doc.hero_primary_cta_href = "/request-demo"
	doc.hero_secondary_cta_label = "Talk to Our ERPNext Team"
	doc.hero_secondary_cta_href = "/contact"
	doc.meta_title = "ERPNext HR & Project Management Software Saudi Arabia | Printechs"
	doc.meta_description = (
		"ERPNext with Frappe HR: employee lifecycle, attendance, leave, payroll, expenses, "
		"performance, projects, timesheets and costing — connected to accounting in Saudi Arabia."
	)
	doc.final_cta_heading = "Manage your workforce and projects from one platform"
	doc.final_cta_description = (
		"Bring employees, attendance, leave, payroll, projects, timesheets, expenses and "
		"accounting together with ERPNext."
	)
	doc.final_cta_primary_label = "Schedule an ERPNext Demo"
	doc.final_cta_primary_href = "/request-demo"
	doc.final_cta_secondary_label = "Talk to Our ERPNext Team"
	doc.final_cta_secondary_href = "/contact"
	doc.audience_heading = "Built for service, project and multi-site teams"
	doc.implementation_heading = "Why Printechs?"
	doc.implementation_cta_label = "Talk to Our ERPNext Team"
	doc.implementation_cta_href = "/contact"
	doc.process_heading = "One platform for people, payroll and projects"
	doc.process_subheading = (
		"Employees, time, pay and project cost stay on the same records — not in separate systems."
	)
	doc.integration_heading = "People, payroll and projects stay connected"
	doc.set(
		"page_section_order",
		[
			{"section": section, "sort_order": idx}
			for idx, section in enumerate(
				[
					"overview",
					"process_steps",
					"benefits",
					"icon_specifications",
					"content_sections",
					"applications",
					"related_products",
					"support",
				],
				start=1,
			)
		],
	)
	doc.set(
		"process_steps",
		[
			{
				"group_title": "People",
				"title": "Recruitment → Employee → Onboarding",
				"description": "Staffing plans and job offers become an employee record with structured joining activities.",
				"sort_order": 1,
			},
			{
				"group_title": "Time",
				"title": "Attendance, shifts and leave",
				"description": "Daily attendance, check-in, holiday calendars and leave approvals replace paper forms.",
				"sort_order": 2,
			},
			{
				"group_title": "Pay",
				"title": "Salary structure → Payroll Entry → Accounting",
				"description": "Working days, additional salary and slips post salary expense to the same ledger.",
				"sort_order": 3,
			},
			{
				"group_title": "Delivery",
				"title": "Projects → Timesheets → Expenses → Billing",
				"description": "The same employees record time and cost so project profitability is visible to finance.",
				"sort_order": 4,
			},
		],
	)
	doc.set(
		"audience_items",
		[
			{"title": "Consulting", "description": "Billable timesheets, project expenses and customer invoices on one record.", "sort_order": 1},
			{"title": "Software development", "description": "Tasks, templates and billable hours for implementation and product work.", "sort_order": 2},
			{"title": "Engineering & technical support", "description": "Field check-in, site expenses and time against service projects.", "sort_order": 3},
			{"title": "Installation & field service", "description": "Project templates, travel advances and timesheets for site delivery.", "sort_order": 4},
			{"title": "Construction & site work", "description": "Project cost, purchases, expenses and team attendance in one place.", "sort_order": 5},
			{"title": "Multi-branch retail", "description": "Shifts, holiday calendars, leave and payroll by branch and store.", "sort_order": 6},
			{"title": "Factory & shift operations", "description": "Shift attendance, overtime components and factory salary structures.", "sort_order": 7},
			{"title": "Professional services", "description": "Retainers, billable time and project profitability next to payroll.", "sort_order": 8},
		],
	)
	doc.set(
		"support_items",
		[
			{"icon": "install", "title": "HR process study", "description": "Map how hiring, leave, attendance and payroll work today.", "sort_order": 1},
			{"icon": "print", "title": "Employee data migration", "description": "Bring employee masters, structures and history into Frappe HR.", "sort_order": 2},
			{"icon": "loyalty", "title": "Organisation structure", "description": "Departments, branches, designations, grades and reporting lines.", "sort_order": 3},
			{"icon": "report", "title": "Leave, attendance and shifts", "description": "Leave types, holiday lists, check-in and shift schedules.", "sort_order": 4},
			{"icon": "zatca", "title": "Payroll and salary structures", "description": "Components, structures, assignment and accounting postings.", "sort_order": 5},
			{"icon": "cloud", "title": "Project setup and costing", "description": "Templates, timesheets, expenses and project profitability.", "sort_order": 6},
			{"icon": "shield", "title": "Approval workflows", "description": "Leave, expenses, advances, recruitment and salary changes.", "sort_order": 7},
			{"icon": "training", "title": "Training and Saudi support", "description": "Local implementation, training and post-go-live support in Saudi Arabia.", "sort_order": 8},
		],
	)
	doc.set(
		"related_products",
		[
			{
				"related_website_product": frappe.db.get_value("Website Product", {"slug": "finance"}, "name"),
				"display_name_override": "Finance",
				"summary_override": "Payroll liabilities and salary posting",
				"href": "/software/erpnext/finance",
				"sort_order": 1,
			},
			{
				"display_name_override": "Sales",
				"summary_override": "Billable projects and customer invoices",
				"href": "/software/erpnext/sales-purchase",
				"sort_order": 2,
			},
			{
				"related_website_product": parent_name,
				"display_name_override": "ERPNext",
				"summary_override": "Full platform and industry solutions",
				"href": "/software/erpnext",
				"sort_order": 3,
			},
		],
	)
	doc.flags.ignore_permissions = True
	doc.save()
	_wire_parent_cards(parent_name, {"People & Projects": HR_PROJECT_PATH})
	_relink_people_projects_urls()
	return {"slug": "hr-project-management", "canonical_path": doc.canonical_path}
