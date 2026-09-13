import type { SolutionPageContent } from "@/types/content";

const solutionImage = (filename: string, alt: string) => ({
  src: `/images/solutions/${filename}`,
  alt,
  width: 1600,
  height: 1000,
});

const fileImage = (filename: string, alt: string, width = 1200, height = 1200) => ({
  src: `/files/${filename}`,
  alt,
  width,
  height,
});

const industryImage = (filename: string, alt: string) => ({
  src: `/images/industries/${filename}`,
  alt,
  width: 1200,
  height: 800,
});

export const solutionPages: Record<string, SolutionPageContent> = {
  "coding-marking": {
    slug: "coding-marking",
    displayName: "Coding & Marking",
    categoryLabel: "INDUSTRIAL SOLUTION",
    tagline: "Hitachi, REA and laser marking for KSA production lines",
    shortDescription:
      "Industrial coding and marking for products, packaging and production lines — Hitachi continuous inkjet, REA JET inkjet, REA LASER, UKCM laser and thermal inkjet.",
    longDescription:
      "Printechs specifies coding and marking for manufacturers across Saudi Arabia. Hitachi CIJ covers high-speed bottles, cans and film. REA JET covers large-character, high-resolution and spray marking. REA LASER and UKCM cover CO2, fiber and UV laser marks. Thermal inkjet covers cartons and cases.\n\nSelect a technology below to open the product page, or contact Printechs for a line assessment. This page is the coding range — we match the printhead, ink or laser to the pack when you enquire.",
    heroImage: solutionImage(
      "featured-production-coding-marking.jpg",
      "Industrial coding and marking system on a production line",
    ),
    heroTrustChips: [
      "Hitachi CIJ partner",
      "REA JET & REA LASER",
      "UKCM laser marking",
    ],
    keyValueCards: [
      {
        icon: "speed",
        title: "Line-speed performance",
        description:
          "Coding systems built for high-throughput production without compromising print quality.",
      },
      {
        icon: "shield",
        title: "Compliance ready",
        description:
          "Dates, batch codes, barcodes and Data Matrix for regulatory and traceability requirements.",
      },
      {
        icon: "print",
        title: "Inkjet and laser",
        description:
          "CIJ, TIJ, large-character and laser marking — matched to substrate and line speed.",
      },
      {
        icon: "integration",
        title: "Full lifecycle support",
        description:
          "Specification, installation, consumables, training and ongoing service from Printechs.",
      },
    ],
    visualStory: {
      heading: "Marking across production environments",
      items: [
        {
          id: "cij",
          label: "Continuous inkjet",
          image: fileImage(
            "hitachi-ux2-product.jpg",
            "Hitachi UX2 continuous inkjet coder",
            1600,
            1000,
          ),
          caption: "High-speed lot, expiry and time codes on bottles, cans and film.",
        },
        {
          id: "large-character",
          label: "Large-character inkjet",
          image: fileImage(
            "rea-jet-dod-2-product.jpg",
            "REA JET DOD 2.0 large-character coder",
            1600,
            1000,
          ),
          caption: "Case, carton and pallet marks from REA JET drop-on-demand systems.",
        },
        {
          id: "laser",
          label: "Laser marking",
          image: fileImage(
            "ukcm-fiber-laser-card.jpg",
            "UKCM fiber laser marking system",
            1600,
            1000,
          ),
          caption: "Permanent fiber, CO2 and UV laser marks from REA LASER and UKCM.",
        },
      ],
    },
    storyHeading: "Built for Saudi manufacturing lines",
    productCategories: [
      {
        slug: "hitachi-cij",
        title: "Hitachi Continuous Inkjet",
        shortTitle: "Hitachi CIJ",
        description:
          "Non-contact CIJ for high-speed lines — bottles, cans, pouches and flexible film.",
        image: fileImage("uxd161.jpg", "Hitachi UX-D161W continuous inkjet"),
        productSlugs: [
          "hitachi-ux-d161",
          "hitachi-ux-d160",
          "hitachi-ux2-d160",
          "hitachi-ux2-d150",
          "hitachi-ux-d151",
        ],
      },
      {
        slug: "rea-jet-inkjet",
        title: "REA JET Inkjet & Marking",
        shortTitle: "REA JET",
        description:
          "Large-character, high-resolution, piezo, spray marking and code verification.",
        image: fileImage("rea-jet-hub-product.jpg", "REA JET coding systems"),
        productSlugs: [
          "rea-jet-coding-systems",
          "rea-jet-dod-2",
          "rea-jet-hr-2",
          "rea-jet-gk-2",
          "rea-jet-up",
          "rea-jet-spray-mark",
          "rea-jet-code-verification",
        ],
      },
      {
        slug: "laser-marking",
        title: "Laser Marking",
        shortTitle: "REA & UKCM Laser",
        description:
          "CO2, fiber and UV laser marking for permanent codes on plastic, metal and film.",
        image: fileImage("rea-jet-cl-card.jpg", "REA LASER CL CO2 laser marker"),
        productSlugs: [
          "rea-jet-cl",
          "rea-jet-fl",
          "ukcm-laser",
          "ukcm-fiber-laser",
          "ukcm-co2-laser",
          "ukcm-uv-laser",
        ],
      },
      {
        slug: "thermal-inkjet",
        title: "Thermal Inkjet (TIJ)",
        shortTitle: "TIJ Printers",
        description:
          "Cartridge TIJ for cartons, cases and secondary packs — ANSER and UKCM.",
        image: fileImage("anser-a1-card.jpg", "ANSER A1 thermal inkjet printer"),
        productSlugs: [
          "anser-a1",
          "anser-sph-smart-printhead",
          "ukcm-kt7",
          "ukcm-kt10",
          "ukcm-hand-coder",
        ],
      },
    ],
    applicationCards: [
      {
        title: "Dairy",
        description: "Date and batch coding on bottles and pouches at line speed.",
        image: industryImage("industry-dairy.jpg", "Dairy production coding"),
        href: "/industries/dairy",
      },
      {
        title: "Food & Beverage",
        description: "Expiry marking on bottles, cans and flexible packaging.",
        image: industryImage(
          "industry-food-beverage.jpg",
          "Food and beverage production",
        ),
        href: "/industries/food-beverage",
      },
      {
        title: "Pharmaceutical",
        description: "Traceability codes for regulated packaging environments.",
        image: industryImage(
          "industry-pharmaceutical.jpg",
          "Pharmaceutical packaging",
        ),
        href: "/industries/pharmaceutical",
      },
      {
        title: "Packaging",
        description: "Secondary packaging and carton coding for logistics.",
        image: industryImage("industry-packaging.jpg", "Packaging production"),
        href: "/industries/packaging",
      },
    ],
    industrySlugs: ["dairy", "food-beverage", "pharmaceutical", "packaging"],
    supportServiceItems: [
      {
        icon: "install",
        title: "Line assessment",
        description: "Site survey, substrate testing and integration planning.",
      },
      {
        icon: "maintenance",
        title: "Service & maintenance",
        description: "Preventive plans and emergency support across KSA.",
      },
      {
        icon: "training",
        title: "Operator training",
        description: "Hands-on training for production and maintenance teams.",
      },
      {
        icon: "integration",
        title: "Plant integration",
        description: "Connectivity with MES, ERP and line control systems.",
      },
    ],
    finalCta: {
      heading: "Need to code your production line?",
      description:
        "Talk to Printechs coding and marking specialists for specification, product selection and deployment support across Saudi Arabia.",
    },
    seo: {
      title: "Coding & Marking Solutions | Printechs",
      description:
        "Hitachi CIJ, REA JET, REA LASER and UKCM laser marking for production lines in Saudi Arabia.",
      canonicalPath: "/solutions/coding-marking",
    },
    canonicalPath: "/solutions/coding-marking",
  },
  "retail-automation": {
    slug: "retail-automation",
    displayName: "Retail Automation",
    categoryLabel: "RETAIL SOLUTION",
    tagline: "Shelf, till and entrance working as one store",
    shortDescription:
      "Electronic shelf labels, POS, weighing, scanning and loss prevention for retailers in Saudi Arabia — from the aisle to checkout.",
    longDescription:
      "A store needs a price, a scan and a stock figure that match — on the shelf, at the fresh counter and at the till.\n\nPrintechs specifies Vusion ESL, FEC POS, Avery Berkel and CAS scales, Datalogic scanning and Nedap RF EAS for chains and independents in Riyadh, Jeddah and Dammam. Select a technology below, or contact us for a store survey. We match the bay, the counter and the lane when you enquire.",
    heroImage: fileImage(
      "featured-connected-retail.png",
      "Retail checkout with POS terminal, scanner and customer display",
      1600,
      1000,
    ),
    heroTrustChips: [
      "Vusion ESL partner",
      "FEC POS & Datalogic",
      "Nedap RF EAS",
    ],
    keyValueCards: [
      {
        icon: "store",
        title: "One identity on the floor",
        description:
          "Price, barcode and stock that stay in step from planogram to till.",
      },
      {
        icon: "checkout",
        title: "Faster, cleaner checkout",
        description:
          "POS, scanners and self-service that keep the queue moving.",
      },
      {
        icon: "scan",
        title: "Shelf to scan path",
        description:
          "ESL, handhelds and fixed scanners that read the same item identity.",
      },
      {
        icon: "shield",
        title: "Protected exits",
        description:
          "RF EAS at the entrance and the lane without a heavy hall.",
      },
    ],
    visualStory: {
      heading: "How a connected store looks",
      items: [
        {
          id: "aisle",
          label: "Aisle pricing",
          image: fileImage(
            "vus-app-supermarket-aisle.jpg",
            "Supermarket aisle with electronic shelf labels",
            1600,
            1000,
          ),
          caption: "A price on every facing that matches the till — updated from the office.",
        },
        {
          id: "checkout",
          label: "Checkout and self-service",
          image: fileImage(
            "nedap-app-self-checkout.jpg",
            "Self-checkout lanes with EAS pedestals in a grocery store",
            1600,
            1000,
          ),
          caption: "Staffed and self-checkout lanes with a scan and an exit that agree.",
        },
        {
          id: "fresh",
          label: "Fresh counters",
          image: fileImage(
            "ab-app-supermarket-fresh.jpg",
            "Fresh produce bay in a supermarket",
            1600,
            1000,
          ),
          caption: "Weigh, label and scan at the counter before the bag leaves the bay.",
        },
      ],
    },
    storyHeading: "Built for Saudi retail floors",
    productCategories: [
      {
        slug: "electronic-shelf-labels",
        title: "Electronic Shelf Labels",
        shortTitle: "Vusion ESL",
        description:
          "Central price updates, four-colour labels and smart-shelf sensing — grocery, fresh and specialty.",
        image: fileImage(
          "vus-app-smart-rail.jpg",
          "Electronic shelf labels on a grocery rail",
        ),
        productSlugs: [
          "vusion-esl",
          "vusion-v300",
          "vusion-v300-waterproof",
          "vusion-v300-freezer",
          "vusion-edgesense",
          "vusion-vusioncloud",
          "vusion-retail-media",
        ],
      },
      {
        slug: "checkout-pos",
        title: "Checkout & POS",
        shortTitle: "POS & Kiosks",
        description:
          "All-in-one terminals, self-service kiosks, price checkers and receipt printers for the lane.",
        image: fileImage(
          "fec-xpos-card.jpg",
          "FEC XPOS Plus all-in-one POS terminals",
        ),
        productSlugs: [
          "fec-pos-systems",
          "fec-xp-4765w",
          "fec-xelf-ii",
          "fec-st-1130w",
          "datalogic-smart-portal",
          "fec-tp-100",
        ],
      },
      {
        slug: "weighing",
        title: "Weighing & Fresh Counters",
        shortTitle: "Scales",
        description:
          "Retail scales and label printers for produce, bakery, deli and service counters.",
        image: fileImage(
          "cas-app-bakery-deli.jpg",
          "Bakery and deli counter ready for retail weighing",
        ),
        productSlugs: [
          "avery-berkel",
          "avery-berkel-xti400",
          "cas-cl-5500d",
          "cas-cl-5500h",
          "cas-cl-5200p",
          "cas-cn1",
        ],
      },
      {
        slug: "scanning",
        title: "Scanning & Self-Shopping",
        shortTitle: "Scanners",
        description:
          "Bi-optic checkout scanners, handhelds and personal shoppers for the aisle and the till.",
        image: fileImage(
          "datalogic-gryphon-4600-retail-pos.jpg",
          "Handheld barcode scanner at a retail counter",
        ),
        productSlugs: [
          "datalogic-magellan-9900i",
          "datalogic-magellan-3610vsi",
          "datalogic-gryphon-i-gd4690",
          "datalogic-joya-smart",
        ],
      },
      {
        slug: "loss-prevention",
        title: "RFID & Loss Prevention",
        shortTitle: "Nedap EAS",
        description:
          "RF EAS pedestals, checkout antennas and labels for fashion, grocery and specialty stores.",
        image: fileImage(
          "nedap-app-fashion-mall.jpg",
          "RF EAS pedestals at a fashion store entrance",
        ),
        productSlugs: [
          "nedap-rf-eas",
          "nedap-i45",
          "nedap-i37",
          "nedap-i15-go",
          "nedap-checkout-antenna",
          "nedap-rf-eas-labels",
        ],
      },
    ],
    applicationCards: [
      {
        title: "Retail",
        description: "Aisle, fresh counter and checkout for grocery and general merchandise.",
        image: industryImage("industry-retail.jpg", "Retail store operations"),
        href: "/industries/retail",
      },
      {
        title: "Fashion",
        description: "Ticketing, rails and entrance protection for apparel floors.",
        image: industryImage("industry-fashion.jpg", "Fashion retail floor"),
        href: "/industries/fashion",
      },
      {
        title: "Warehouse & Logistics",
        description: "Receiving, restock and back-of-store identity that matches the hall.",
        image: industryImage(
          "industry-warehouse-logistics.jpg",
          "Warehouse and store back-of-house",
        ),
        href: "/industries/warehouse-logistics",
      },
    ],
    industrySlugs: ["retail", "fashion", "warehouse-logistics"],
    supportServiceItems: [
      {
        icon: "install",
        title: "Store assessment",
        description: "Site survey, aisle plan and checkout layout before you buy.",
      },
      {
        icon: "maintenance",
        title: "Service & maintenance",
        description: "Preventive plans and emergency support across KSA.",
      },
      {
        icon: "training",
        title: "Operator training",
        description: "Hands-on training for store, fresh-counter and IT teams.",
      },
      {
        icon: "integration",
        title: "POS and ERP integration",
        description: "Price, scan and stock connected to the systems you already run.",
      },
    ],
    finalCta: {
      heading: "Ready to connect the store?",
      description:
        "Talk to Printechs retail specialists for specification, product selection and rollout support across Saudi Arabia.",
    },
    seo: {
      title: "Retail Automation Solutions | Printechs",
      description:
        "ESL, POS, weighing, scanning and RF EAS for retailers in Saudi Arabia.",
      canonicalPath: "/solutions/retail-automation",
    },
    canonicalPath: "/solutions/retail-automation",
  },
  "warehouse-automation": {
    slug: "warehouse-automation",
    displayName: "Warehouse Automation",
    categoryLabel: "INDUSTRIAL SOLUTION",
    tagline: "Aisle, dock and RFID inventory in one DC",
    shortDescription:
      "Mobile computers, fixed scanners, label printers and RFID inventory systems for distribution centres in Saudi Arabia.",
    longDescription:
      "A DC needs a location, a licence plate and a scan that follow the pallet from inbound to pick to the dock. RFID inventory adds a count that does not depend on line-of-sight — handheld sleds in the aisle, fixed readers at the door, and encode printers at the pack bench.\n\nPrintechs specifies Datalogic and Zebra mobility, industrial scanning, ship-station printing and Zebra RFID inventory for distribution centres in Riyadh, Jeddah and Dammam. Warehouse software is specified separately when you need WMS on the same flow. Select a technology below, or contact us for a site survey.",
    heroImage: fileImage(
      "featured-warehouse-automation.jpg",
      "High-bay warehouse aisle with a roller conveyor between pallet racks",
      1600,
      1000,
    ),
    heroTrustChips: [
      "Datalogic mobility",
      "Zebra RFID inventory",
      "Printechs Saudi Arabia",
    ],
    keyValueCards: [
      {
        icon: "inventory",
        title: "Known stock, known location",
        description:
          "A scan or an RFID read that matches the bin, the tote and the ASN.",
      },
      {
        icon: "scan",
        title: "Aisle and dock coverage",
        description:
          "Handhelds, wearables and fixed imagers for receive, pick and ship.",
      },
      {
        icon: "print",
        title: "Labels that leave with the load",
        description:
          "Licence plates and shippers that grade after the pack station.",
      },
      {
        icon: "integration",
        title: "Tied to the WMS",
        description:
          "Hardware specified to the warehouse system you already run — or to Printechs WMS.",
      },
    ],
    visualStory: {
      heading: "How a connected DC looks",
      items: [
        {
          id: "aisle",
          label: "Aisle inventory",
          image: fileImage(
            "featured-enterprise-warehouse.png",
            "Warehouse handheld confirming a carton barcode and location",
            1600,
            1000,
          ),
          caption: "Receive, count and pick with the same identity the dock printed.",
        },
        {
          id: "ship-station",
          label: "Ship-station labels",
          image: fileImage(
            "zebra-zt421-warehouse.png",
            "Zebra ZT421 printing a shipping label at a warehouse pack station",
            1600,
            1000,
          ),
          caption: "A licence plate and a shipper that leave with the pallet.",
        },
        {
          id: "rfid",
          label: "RFID inventory",
          image: fileImage(
            "featured-rfid.jpg",
            "RFID inventory portal around a garment rail",
            1600,
            1000,
          ),
          caption:
            "Bulk counts without line-of-sight — handheld, wearable and dock-door RFID.",
        },
      ],
    },
    storyHeading: "Built for Saudi distribution centres",
    productCategories: [
      {
        slug: "mobile-computers",
        title: "Mobile Computers & Wearables",
        shortTitle: "Mobility",
        description:
          "Gun-grip, wearable and tablet computers for inbound, count, pick and putaway.",
        image: fileImage(
          "datalogic-codiscan-2.jpg",
          "Wearable scanner on a warehouse pick",
        ),
        productSlugs: [
          "datalogic-memor-12",
          "datalogic-memor-17",
          "datalogic-skorpio-x40-x45",
          "datalogic-falcon-x60-x65",
          "datalogic-codiscan",
          "zebra-tc53e-tc58e",
          "zebra-tc73-tc78",
          "zebra-ws501",
        ],
      },
      {
        slug: "industrial-scanning",
        title: "Industrial & Fixed Scanning",
        shortTitle: "Fixed Scan",
        description:
          "Conveyor imagers and rugged handhelds for the pack line and the dock.",
        image: fileImage(
          "datalogic-matrix-320-operation.jpg",
          "Fixed imager reading cartons on a conveyor",
        ),
        productSlugs: [
          "datalogic-matrix-320",
          "datalogic-powerscan-9600",
          "zebra-ds3600-series",
        ],
      },
      {
        slug: "label-printing",
        title: "Label & Ship-Station Printing",
        shortTitle: "Label Print",
        description:
          "Industrial, desktop and mobile printers for licence plates and shippers.",
        image: fileImage(
          "zebra-zt421-card.jpg",
          "Zebra ZT421 industrial label printer",
        ),
        productSlugs: [
          "zebra-zt421",
          "zebra-zt411",
          "zebra-zt610-zt620",
          "zebra-zd621",
          "zebra-zq630-plus",
          "zebra-zq521",
        ],
      },
      {
        slug: "rfid-inventory",
        title: "RFID Inventory System",
        shortTitle: "RFID Inventory",
        description:
          "Handheld sleds, dock-door readers, RFID encode printers and wearable verify — Zebra UHF inventory for the DC and back-of-store.",
        image: fileImage(
          "zebra-rfd90.png",
          "Zebra RFD90 rugged UHF RFID sled",
        ),
        productSlugs: [
          "zebra-rfd90",
          "zebra-fxr90",
          "zebra-zd621r",
          "zebra-zq630-rfid-plus",
          "zebra-ws50-rfid",
          "zebra-rfd40",
        ],
      },
    ],
    applicationCards: [
      {
        title: "Warehouse & Logistics",
        description: "Racking, aisle mobility, fulfilment and outbound freight.",
        image: industryImage(
          "industry-warehouse-logistics.jpg",
          "Warehouse and logistics operations",
        ),
        href: "/industries/warehouse-logistics",
      },
      {
        title: "Retail",
        description: "Back-of-store receiving and replenishment that match the hall.",
        image: industryImage("industry-retail.jpg", "Retail back-of-store operations"),
        href: "/industries/retail",
      },
      {
        title: "Packaging",
        description: "Carton identity that follows the pack into the warehouse.",
        image: industryImage("industry-packaging.jpg", "Packaging and case identity"),
        href: "/industries/packaging",
      },
    ],
    industrySlugs: ["warehouse-logistics", "retail", "packaging"],
    supportServiceItems: [
      {
        icon: "install",
        title: "DC assessment",
        description: "Site survey of aisles, docks and pack stations before you buy.",
      },
      {
        icon: "maintenance",
        title: "Service & maintenance",
        description: "Preventive plans and emergency support across KSA.",
      },
      {
        icon: "training",
        title: "Operator training",
        description: "Hands-on training for warehouse, IT and shift leads.",
      },
      {
        icon: "integration",
        title: "WMS integration",
        description: "Hardware specified to your warehouse system or Printechs WMS.",
      },
    ],
    finalCta: {
      heading: "Ready to specify the DC?",
      description:
        "Talk to Printechs warehouse specialists for mobility, RFID inventory, printing and rollout support across Saudi Arabia.",
    },
    seo: {
      title: "Warehouse Automation Solutions | Printechs",
      description:
        "Warehouse mobility, industrial scanning, label printing and Zebra RFID inventory systems for DCs in Saudi Arabia.",
      canonicalPath: "/solutions/warehouse-automation",
    },
    canonicalPath: "/solutions/warehouse-automation",
  },
  "erp-business-automation": {
    slug: "erp-business-automation",
    displayName: "ERP & Business Automation",
    categoryLabel: "BUSINESS SOFTWARE",
    tagline: "Finance, stock, POS and warehouse in one picture",
    shortDescription:
      "ERPNext, Modern POS, warehouse management and ZATCA e-invoicing — so finance, inventory and the store share the same numbers.",
    longDescription:
      "A business needs one stock figure, one invoice and one location that match — in the office, at the till and in the DC.\n\nPrintechs implements ERPNext, Modern POS, warehouse management and ZATCA integration for companies in Riyadh, Jeddah and Dammam. This page is the software suite. Select a system below, or contact us for a process review. Hardware for the store and the warehouse is specified on the retail and warehouse solution pages.",
    heroImage: fileImage(
      "featured-erp-business-automation.jpg",
      "Office laptop showing a business operations dashboard",
      1600,
      1000,
    ),
    heroTrustChips: [
      "ERPNext partner",
      "ZATCA e-invoicing",
      "Printechs Saudi Arabia",
    ],
    keyValueCards: [
      {
        icon: "integration",
        title: "One set of numbers",
        description:
          "Finance, inventory and sales post to the same company books.",
      },
      {
        icon: "inventory",
        title: "Stock you can trust",
        description:
          "Warehouse, store and purchase share the same item identity.",
      },
      {
        icon: "zatca",
        title: "Saudi e-invoicing",
        description:
          "ZATCA clearance on the invoice before it leaves the system.",
      },
      {
        icon: "cloud",
        title: "Cloud or on your servers",
        description:
          "Deployed and supported in Saudi Arabia, in Arabic and English.",
      },
    ],
    visualStory: {
      heading: "What the suite looks like day to day",
      items: [
        {
          id: "erp",
          label: "Company dashboard",
          image: fileImage(
            "software-erpnext.jpg",
            "ERPNext dashboard with sales, stock and cash in Saudi Riyal",
            1600,
            1000,
          ),
          caption: "Sales, receivables, payables and stock on one screen for the owner and the finance team.",
        },
        {
          id: "pos",
          label: "Store checkout",
          image: fileImage(
            "software-modern-pos.jpg",
            "Modern POS at a fashion retail checkout",
            1600,
            1000,
          ),
          caption: "The till posts the sale, the stock and the ZATCA invoice in the same flow.",
        },
        {
          id: "wms",
          label: "Warehouse execution",
          image: fileImage(
            "software-warehouse-management-system.jpg",
            "Warehouse dashboard with pick list, scanner and label printer",
            1600,
            1000,
          ),
          caption: "Receive, pick and ship against the same stock the office already sees.",
        },
      ],
    },
    storyHeading: "Built for Saudi companies",
    productCategories: [],
    applicationsEyebrow: "Software",
    applicationsTitle: "Choose the system you need",
    applicationCards: [
      {
        title: "ERPNext",
        description:
          "Finance, inventory, buying, selling and projects for the whole company.",
        image: fileImage(
          "software-erpnext.jpg",
          "ERPNext company dashboard",
          1600,
          1000,
        ),
        href: "/software/erpnext",
      },
      {
        title: "Modern POS",
        description:
          "Checkout, returns and ZATCA invoices that post back to ERP.",
        image: fileImage(
          "software-modern-pos.jpg",
          "Modern POS checkout in a fashion store",
          1600,
          1000,
        ),
        href: "/software/modern-pos",
      },
      {
        title: "Warehouse Management",
        description:
          "Inbound, pick and ship on the same stock file as ERPNext.",
        image: fileImage(
          "software-warehouse-management-system.jpg",
          "Warehouse management pick station and dashboard",
          1600,
          1000,
        ),
        href: "/software/warehouse-management-system",
      },
      {
        title: "ZATCA Integration",
        description:
          "E-invoice clearance and reporting for Phase 2 in Saudi Arabia.",
        image: fileImage(
          "software-zatca-integration.jpg",
          "ZATCA e-invoicing dashboard and tax invoice",
          1600,
          1000,
        ),
        href: "/software/zatca-integration",
      },
      {
        title: "Healthcare ERP",
        description:
          "Patient, pharmacy and billing on the same ERPNext backbone.",
        image: fileImage(
          "HealthCare2.png",
          "Healthcare team using a hospital information system",
          1600,
          1000,
        ),
        href: "/software/erpnext/healthcare",
      },
    ],
    industrySlugs: ["retail", "warehouse-logistics", "fashion"],
    supportServiceItems: [
      {
        icon: "install",
        title: "Discovery and implementation",
        description: "Process review, chart of accounts and a staged go-live.",
      },
      {
        icon: "training",
        title: "User training",
        description: "Hands-on training in Arabic and English for finance and operations.",
      },
      {
        icon: "integration",
        title: "POS, WMS and ZATCA",
        description: "The till, the DC and the invoice connected to one company.",
      },
      {
        icon: "report",
        title: "Reporting and go-live",
        description: "Owner dashboards, stock reports and hypercare after cutover.",
      },
    ],
    finalCta: {
      heading: "Ready to unify the business?",
      description:
        "Talk to Printechs software specialists for ERP assessment, POS, WMS and ZATCA rollout across Saudi Arabia.",
    },
    seo: {
      title: "ERP & Business Automation | Printechs",
      description:
        "ERPNext, Modern POS, warehouse management and ZATCA e-invoicing for companies in Saudi Arabia.",
      canonicalPath: "/solutions/erp-business-automation",
    },
    canonicalPath: "/solutions/erp-business-automation",
  },
};

export function getSolutionPage(slug: string): SolutionPageContent | undefined {
  return solutionPages[slug];
}
