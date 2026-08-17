import type { ProductPageContent } from "@/types/content";

const productImage = (label: string) => ({
  src: "/images/placeholders/product.svg",
  alt: `${label} product visual`,
  width: 1200,
  height: 1200,
});

const industryImage = (filename: string, alt: string) => ({
  src: `/images/industries/${filename}`,
  alt,
  width: 1200,
  height: 800,
});

const softwareHeroImage = (filename: string, alt: string) => ({
  src: `/images/software/${filename}`,
  alt,
  width: 1600,
  height: 1000,
});

export const productPages: Record<string, ProductPageContent> = {
  "hitachi-ux-d161": {
    slug: "hitachi-ux-d161",
    productType: "industrial",
    displayName: "Hitachi UX-D161W",
    itemCode: "IND.SYS.HIJ.1995",
    brand: "Hitachi",
    brandSlug: "hitachi",
    category: "Coding & Marking",
    subcategory: "Continuous Inkjet",
    tagline: "Reliable coding for demanding production environments",
    shortDescription:
      "High-performance continuous inkjet printer for production line marking on metal, plastic, film, and packaging — with wireless connectivity and easy maintenance.",
    longDescription:
      "The Hitachi UX-D161W is an industrial continuous inkjet (CIJ) printer designed for demanding manufacturing environments. Using a non-contact printing method, it applies codes, dates, and batch data to products moving on production lines at high speed.\n\nBuilt for reliability in harsh conditions, the UX-D161W combines advanced ink delivery, automatic nozzle cleaning, and remote monitoring capability. Printechs supplies, installs, and supports Hitachi UX systems across Saudi Arabia with local expertise and service coverage.",
    heroImage: productImage("Hitachi UX-D161W"),
    categoryLabel: "CONTINUOUS INKJET PRINTER",
    heroTrustChips: ["IP65 rated", "Up to 600 dpi", "Printechs Saudi Arabia"],
    primaryDownload: {
      label: "Download Datasheet",
      href: "#",
      type: "datasheet",
    },
    showDemoCta: false,
    collapsibleFullSpecs: true,
    visualStory: {
      heading: "See the print quality",
      items: [
        {
          id: "dates",
          label: "Production dates",
          image: industryImage(
            "industry-dairy.jpg",
            "Production date codes on dairy bottles",
          ),
          caption: "Clear, high-contrast date codes on fast-moving dairy lines.",
        },
        {
          id: "expiry",
          label: "Expiry dates",
          image: industryImage(
            "industry-food-beverage.jpg",
            "Expiry date marking on beverage packaging",
          ),
          caption: "Legible expiry and best-before marking on bottles and packs.",
        },
        {
          id: "batch",
          label: "Batch codes",
          image: industryImage(
            "industry-packaging.jpg",
            "Batch codes on secondary packaging",
          ),
          caption: "Batch and lot traceability on cartons and flexible film.",
        },
        {
          id: "barcode",
          label: "Barcodes",
          image: industryImage(
            "industry-plastic.jpg",
            "Barcode printing on plastic containers",
          ),
          caption: "1D and 2D codes for supply chain traceability.",
        },
      ],
    },
    trustIndicators: [
      { label: "IP rating", value: "IP65" },
      { label: "Resolution", value: "Up to 600 dpi" },
      { label: "Compliance", value: "CE · FCC · ATEX Zone 2" },
      { label: "Support", value: "Printechs Saudi Arabia" },
    ],
    keyValueCards: [
      {
        icon: "speed",
        title: "High-speed coding",
        description:
          "Print at line speeds up to 5 m/s without compromising code quality on fast-moving conveyors.",
      },
      {
        icon: "lines",
        title: "Up to 6 print lines",
        description:
          "Flexible multi-line printing from a single printhead for dates, batch data, and logos.",
      },
      {
        icon: "shield",
        title: "Industrial reliability",
        description:
          "Stainless steel IP65 construction built for washdown and harsh production environments.",
      },
      {
        icon: "integration",
        title: "Flexible integration",
        description:
          "Wi-Fi 5 and Ethernet for remote monitoring, diagnostics, and plant system connectivity.",
      },
    ],
    iconSpecifications: [
      {
        icon: "print",
        title: "Print technology",
        description: "Continuous inkjet (CIJ) · up to 600 dpi · 1–12 mm character height",
      },
      {
        icon: "lines",
        title: "Print lines",
        description: "Up to 6 lines from a single printhead",
      },
      {
        icon: "display",
        title: "Touchscreen",
        description: "10.4\" colour LCD operator interface",
      },
      {
        icon: "connectivity",
        title: "Connectivity",
        description: "Ethernet · Wi-Fi 5 · USB 2.0 host/device",
      },
      {
        icon: "speed",
        title: "Applications",
        description: "Dates · lot · batch · barcode · Data Matrix",
      },
      {
        icon: "durability",
        title: "Suitable for",
        description: "Packaging · dairy · beverage · plastic · metal",
      },
    ],
    applicationCards: [
      {
        title: "Dairy",
        description: "Date and batch coding on bottles and pouches at high line speeds.",
        image: industryImage("industry-dairy.jpg", "Dairy production line coding"),
        href: "/industries/dairy",
      },
      {
        title: "Food & Beverage",
        description: "Expiry and production marking on bottles, cans, and flexible packaging.",
        image: industryImage(
          "industry-food-beverage.jpg",
          "Food and beverage packaging line",
        ),
        href: "/industries/food-beverage",
      },
      {
        title: "Pharmaceutical",
        description: "Traceability codes for regulated packaging and secondary cartons.",
        image: industryImage(
          "industry-pharmaceutical.jpg",
          "Pharmaceutical packaging line",
        ),
        href: "/industries/pharmaceutical",
      },
      {
        title: "Pipe & Plastic",
        description: "Durable marking on extruded products, pipes, and plastic containers.",
        image: industryImage("industry-plastic.jpg", "Plastic manufacturing line"),
        href: "/industries/plastic",
      },
    ],
    supportServiceItems: [
      {
        icon: "install",
        title: "Installation",
        description: "Site survey, mounting, commissioning, and line integration.",
      },
      {
        icon: "consumables",
        title: "Consumables",
        description: "Ink supply, smart bottle management, and spare parts.",
      },
      {
        icon: "maintenance",
        title: "Maintenance",
        description: "Preventive service plans and emergency response across KSA.",
      },
      {
        icon: "training",
        title: "Operator training",
        description: "Hands-on training for operators and maintenance teams.",
      },
    ],
    ecosystemItems: [
      {
        slug: "hitachi-ux-d160",
        name: "UX-D160W",
        summary: "Alternative UX platform",
        href: "/products/hitachi-ux-d160",
        image: productImage("Hitachi UX-D160W"),
      },
      {
        slug: "rea-jet-coding-systems",
        name: "REA JET Systems",
        summary: "Large-character coding",
        href: "/products/rea-jet-coding-systems",
        image: productImage("REA JET"),
      },
    ],
    storyHeading: "Built for production line coding",
    features: [
      "Industrial-grade continuous inkjet technology",
      "Wireless 802.11ac connectivity",
      "High-resolution printing up to 600 dpi",
      "Stainless steel construction with IP65-rated enclosure",
      "Touchscreen operator interface",
      "Automatic nozzle cleaning system",
      "Multi-language support",
      "Quick-drying solvent-based ink system",
      "Remote monitoring capability",
      "Flexible text printing — up to 6 lines from a single printhead",
    ],
    keySpecifications: [
      { label: "Print resolution", value: "Up to 600 dpi" },
      { label: "Print speed", value: "Up to 5 m/s" },
      { label: "Character height", value: "1–12 mm" },
      { label: "Print lines", value: "Up to 6 lines" },
      { label: "Ink capacity", value: "2 L smart bottle" },
      { label: "IP rating", value: "IP65" },
    ],
    fullSpecifications: [
      {
        title: "Printing performance",
        items: [
          { label: "Print resolution", value: "Up to 600 dpi" },
          { label: "Print speed", value: "Up to 5 m/s" },
          { label: "Character height", value: "1–12 mm" },
          { label: "Print lines", value: "Up to 6 lines" },
        ],
      },
      {
        title: "Connectivity",
        items: [
          { label: "Wireless", value: "Wi-Fi 5 (802.11ac)" },
          { label: "Ethernet", value: "10/100/1000BASE-T" },
          { label: "USB", value: "2.0 Host / Device" },
        ],
      },
      {
        title: "Ink system",
        items: [
          { label: "Ink type", value: "MEK-based / solvent" },
          { label: "Ink capacity", value: "2 L smart bottle" },
          { label: "Drying time", value: "0.3–3 seconds" },
        ],
      },
      {
        title: "Durability & environment",
        items: [
          { label: "IP rating", value: "IP65" },
          { label: "Operating temperature", value: "0–40 °C" },
          { label: "Construction", value: "Stainless steel" },
        ],
      },
      {
        title: "Compliance",
        items: [
          { label: "Safety", value: "CE, FCC, RoHS" },
          { label: "Explosion protection", value: "ATEX Zone 2" },
        ],
      },
    ],
    applications: [
      "Batch and lot coding on packaging lines",
      "Expiry date and best-before marking",
      "Secondary packaging and carton coding",
      "Metal, plastic, and film substrate marking",
      "High-speed beverage and dairy lines",
    ],
    industrySlugs: ["dairy", "food-beverage", "packaging", "pharmaceutical"],
    accessories: [
      {
        slug: "hitachi-ux-d160",
        name: "Hitachi UX-D160W",
        summary: "Alternative UX platform for varied printing needs",
        href: "/products/hitachi-ux-d160",
        image: productImage("Hitachi UX-D160W"),
      },
    ],
    compatibleHardware: [
      {
        slug: "rea-jet-coding-systems",
        name: "REA JET Coding Systems",
        summary: "Complementary large-character and high-resolution coding",
        href: "/products/rea-jet-coding-systems",
        image: productImage("REA JET"),
      },
    ],
    supportServices: [
      "Site survey and line integration planning",
      "Installation, commissioning, and operator training",
      "Preventive maintenance and emergency service",
      "Ink supply and consumables management",
      "Remote diagnostics and technical support",
    ],
    downloads: [
      {
        label: "UX-D161W Product Datasheet",
        href: "#",
        type: "datasheet",
      },
      {
        label: "Hitachi UX Series Brochure",
        href: "#",
        type: "brochure",
      },
    ],
    packageContents: [
      "UX-D161W printer main unit",
      "2 L starter ink smart bottle",
      "Mounting kit",
      "Power and interface cabling",
    ],
    relatedProducts: [
      {
        slug: "hitachi-ux-d160",
        name: "Hitachi UX-D160W",
        summary: "Industrial inkjet printer with wireless connectivity",
        href: "/products/hitachi-ux-d160",
        image: productImage("Hitachi UX-D160W"),
      },
      {
        slug: "rea-jet-coding-systems",
        name: "REA JET Coding Systems",
        summary: "High-resolution industrial coding systems",
        href: "/products/rea-jet-coding-systems",
        image: productImage("REA JET"),
      },
    ],
    finalCta: {
      heading: "Get pricing, availability, and integration advice",
      description:
        "Printechs supports Hitachi UX systems from specification through installation, training, and ongoing service across Saudi Arabia.",
    },
    seo: {
      title: "Hitachi UX-D161W | Printechs",
      description:
        "Discover Hitachi UX-D161W continuous inkjet coding solutions from Printechs.",
      canonicalPath: "/products/hitachi-ux-d161",
    },
    canonicalPath: "/products/hitachi-ux-d161",
    breadcrumbRoot: { label: "Products", href: "/products" },
  },

  "datalogic-memor-12": {
    slug: "datalogic-memor-12",
    productType: "retail_hardware",
    displayName: "Datalogic Memor 12",
    itemCode: "RTL.DEV.DLG.2841",
    brand: "Datalogic",
    brandSlug: "datalogic",
    category: "Barcode & Mobility",
    subcategory: "Mobile Computers",
    tagline: "Powerful performance. Pocket-sized. Built for the way you work.",
    shortDescription:
      "Enterprise-grade Android mobile computer with integrated scanning, long battery life, and durable design for store and warehouse workflows.",
    longDescription:
      "The Datalogic Memor 12 is a full-touch mobile computer built for retail floor operations, stock management, and warehouse picking. Its ergonomic design, powerful scanning engine, and enterprise Android platform help teams work faster with fewer errors.\n\nPrintechs supplies Memor 12 devices with staging, MDM configuration, and integration support for POS, WMS, and ERP environments across Saudi Arabia.",
    heroImage: productImage("Datalogic Memor 12"),
    categoryLabel: "MOBILE COMPUTER",
    heroTrustChips: [
      "Enterprise grade",
      "Global support",
      "2-Year warranty",
    ],
    primaryDownload: {
      label: "Download Datasheet",
      href: "#",
      type: "datasheet",
    },
    showDemoCta: false,
    collapsibleFullSpecs: true,
    visualStory: {
      heading: "Mobility in real operations",
      items: [
        {
          id: "retail",
          label: "Retail floor",
          image: industryImage(
            "industry-retail.jpg",
            "Mobile computer used in retail store",
          ),
          caption: "Price checks, shelf management, and assisted selling on the shop floor.",
        },
        {
          id: "warehouse",
          label: "Warehouse",
          image: industryImage(
            "industry-warehouse-logistics.jpg",
            "Warehouse picking with mobile computer",
          ),
          caption: "Receiving, picking, and inventory counts in warehouse operations.",
        },
        {
          id: "fashion",
          label: "Fashion",
          image: industryImage(
            "industry-fashion.jpg",
            "Fashion retail inventory with mobile device",
          ),
          caption: "Stock lookups and click-and-collect order fulfilment.",
        },
      ],
    },
    trustIndicators: [
      { label: "Platform", value: "Android Enterprise" },
      { label: "Scan engine", value: "1D / 2D imager" },
      { label: "Durability", value: "IP65 · 1.5 m drop" },
      { label: "Support", value: "Printechs Saudi Arabia" },
    ],
    keyValueCards: [
      {
        icon: "rugged",
        title: "Rugged mobility",
        description:
          "IP65 sealing and 1.5 m drop resistance for demanding store and warehouse use.",
      },
      {
        icon: "scan",
        title: "Fast. Accurate. Every time.",
        description:
          "Integrated 1D/2D imager reads damaged and high-density barcodes reliably.",
      },
      {
        icon: "battery",
        title: "All-day performance",
        description:
          "Removable 5000 mAh battery keeps teams productive through full shifts.",
      },
      {
        icon: "android",
        title: "Android platform",
        description:
          "Enterprise Android with MDM-ready deployment for retail and logistics apps.",
      },
    ],
    iconSpecifications: [
      {
        icon: "display",
        title: "Display",
        description: "5.7\" HD · glove touch",
      },
      {
        icon: "scan",
        title: "Scanning",
        description: "1D/2D imager",
      },
      {
        icon: "battery",
        title: "Battery",
        description: "5000 mAh removable",
      },
      {
        icon: "connectivity",
        title: "Connectivity",
        description: "Wi-Fi 6 · BT 5.1",
      },
      {
        icon: "durability",
        title: "Durability",
        description: "IP65 · 1.5 m drop",
      },
      {
        icon: "android",
        title: "Operating system",
        description: "Android Enterprise",
      },
    ],
    applicationCards: [
      {
        title: "Retail",
        description: "Shelf management, price verification, and assisted selling.",
        image: industryImage("industry-retail.jpg", "Retail store operations"),
        href: "/industries/retail",
      },
      {
        title: "Warehousing",
        description: "Receiving, put-away, picking, and cycle counting.",
        image: industryImage(
          "industry-warehouse-logistics.jpg",
          "Warehouse logistics",
        ),
        href: "/industries/warehouse-logistics",
      },
      {
        title: "Fashion",
        description: "Inventory lookups and click-and-collect fulfilment.",
        image: industryImage("industry-fashion.jpg", "Fashion retail"),
        href: "/industries/fashion",
      },
      {
        title: "Food & Beverage",
        description: "Stock checks and expiry management in fresh-food retail.",
        image: industryImage("industry-food-beverage.jpg", "Food retail"),
        href: "/industries/food-beverage",
      },
    ],
    supportServiceItems: [
      {
        icon: "install",
        title: "Device staging",
        description: "MDM configuration, app deployment, and rollout planning.",
      },
      {
        icon: "integration",
        title: "Integration",
        description: "Connect to POS, WMS, and ERP platforms.",
      },
      {
        icon: "maintenance",
        title: "Warranty & repair",
        description: "Swap-device programs and repair coordination.",
      },
      {
        icon: "training",
        title: "User training",
        description: "Operator training for store and warehouse teams.",
      },
    ],
    ecosystemItems: [
      {
        slug: "memor-12-cradle",
        name: "Single-Slot Cradle",
        summary: "Charging & sync",
        href: "#",
        image: productImage("Memor 12 cradle"),
      },
      {
        slug: "memor-12-strap",
        name: "Hand Strap & Boot",
        summary: "Drop protection",
        href: "#",
        image: productImage("Memor 12 accessories"),
      },
      {
        slug: "zebra-mobility",
        name: "Zebra Mobility",
        summary: "Alternative platforms",
        href: "/products/zebra-mobility",
        image: productImage("Zebra"),
      },
    ],
    storyHeading: "Mobility for connected store and warehouse teams",
    features: [
      "5.7\" full-touch display with glove support",
      "Integrated 1D/2D barcode imager",
      "Android 11 Enterprise platform",
      "Wi-Fi 6 and optional 4G/LTE",
      "IP65 sealing and 1.5 m drop resistance",
      "Removable battery for shift-long operation",
      "NFC for tap-to-pair accessories",
      "Push-to-talk ready for team communication",
      "Compatible with Datalogic cradles and chargers",
    ],
    keySpecifications: [
      { label: "Display", value: "5.7\" HD touchscreen" },
      { label: "Processor", value: "Qualcomm octa-core" },
      { label: "Memory", value: "4 GB RAM / 64 GB storage" },
      { label: "Scan engine", value: "1D/2D imager" },
      { label: "Wireless", value: "Wi-Fi 6 · Bluetooth 5.1" },
      { label: "Battery", value: "Removable · 5000 mAh" },
    ],
    fullSpecifications: [
      {
        title: "Display & input",
        items: [
          { label: "Display size", value: "5.7\"" },
          { label: "Resolution", value: "1280 × 720 HD" },
          { label: "Touch", value: "Multi-touch · glove capable" },
        ],
      },
      {
        title: "Scanning",
        items: [
          { label: "Engine", value: "1D/2D imager" },
          { label: "Symbologies", value: "All standard 1D/2D codes" },
          { label: "Read range", value: "Up to 40 cm (code dependent)" },
        ],
      },
      {
        title: "Connectivity",
        items: [
          { label: "WLAN", value: "Wi-Fi 6 (802.11ax)" },
          { label: "Cellular", value: "Optional 4G/LTE" },
          { label: "Bluetooth", value: "5.1 + NFC" },
        ],
      },
      {
        title: "Durability",
        items: [
          { label: "IP rating", value: "IP65" },
          { label: "Drop spec", value: "1.5 m to concrete" },
          { label: "Operating temp", value: "-10 °C to 50 °C" },
        ],
      },
    ],
    applications: [
      "In-store price verification and shelf management",
      "Inventory counts and stock replenishment",
      "Click-and-collect order picking",
      "Receiving and put-away in warehouses",
      "Last-mile delivery proof of delivery",
    ],
    industrySlugs: ["retail", "warehouse-logistics", "fashion", "food-beverage"],
    accessories: [
      {
        slug: "memor-12-cradle",
        name: "Memor 12 Single-Slot Cradle",
        summary: "Charging and data sync cradle for counter deployment",
        href: "#",
      },
      {
        slug: "memor-12-handstrap",
        name: "Hand Strap & Protective Boot",
        summary: "Ergonomic hand strap with drop protection",
        href: "#",
      },
    ],
    compatibleHardware: [
      {
        slug: "zebra-mobility",
        name: "Zebra Mobile Computers",
        summary: "Alternative enterprise mobility platforms",
        href: "/products/zebra-mobility",
        image: productImage("Zebra"),
      },
    ],
    supportServices: [
      "Device staging and MDM configuration",
      "Application deployment and testing",
      "Warranty and repair coordination",
      "Spare pool and swap-device programs",
      "Integration with POS and WMS platforms",
    ],
    downloads: [
      {
        label: "Memor 12 Product Datasheet",
        href: "#",
        type: "datasheet",
      },
      {
        label: "Datalogic Mobility Brochure",
        href: "#",
        type: "brochure",
      },
    ],
    relatedProducts: [
      {
        slug: "datalogic-barcode-solutions",
        name: "Datalogic Scanning Solutions",
        summary: "Barcode scanners and data capture devices",
        href: "/products/datalogic-barcode-solutions",
        image: productImage("Datalogic"),
      },
      {
        slug: "zebra-mobility",
        name: "Zebra Mobility & Printing",
        summary: "Enterprise mobile computers and printers",
        href: "/products/zebra-mobility",
        image: productImage("Zebra"),
      },
    ],
    finalCta: {
      heading: "Plan your mobile deployment with Printechs",
      description:
        "From device selection to MDM setup and WMS integration — Printechs helps retail and logistics teams deploy Datalogic mobility at scale.",
    },
    seo: {
      title: "Datalogic Memor 12 | Printechs",
      description:
        "Datalogic Memor 12 mobile computer for retail and warehouse operations — supplied by Printechs.",
      canonicalPath: "/products/datalogic-memor-12",
    },
    canonicalPath: "/products/datalogic-memor-12",
    breadcrumbRoot: { label: "Products", href: "/products" },
  },

  "modern-pos": {
    slug: "modern-pos",
    productType: "software",
    displayName: "Modern POS",
    brand: "Printechs",
    category: "Retail Software",
    subcategory: "Point of Sale",
    tagline: "A contemporary point-of-sale platform for multi-store retail",
    shortDescription:
      "Cloud-ready POS software for multi-store retail — unified checkout, inventory sync, loyalty, and ZATCA-compliant invoicing.",
    longDescription:
      "Modern POS is Printechs' retail point-of-sale platform designed for Saudi multi-store operations. It connects store checkout with back-office inventory, pricing, and customer engagement — giving retailers a single operational view across locations.\n\nBuilt for speed at the register and reliability at scale, Modern POS integrates with ERPNext, weighing scales, barcode scanners, payment terminals, and ZATCA e-invoicing requirements.",
    heroImage: softwareHeroImage(
      "software-modern-pos.jpg",
      "Modern POS checkout with scanner, terminal and payment system",
    ),
    categoryLabel: "RETAIL POINT OF SALE SOLUTION",
    heroTrustChips: [
      "ZATCA e-invoicing ready",
      "ERPNext connected",
      "Printechs Saudi Arabia",
    ],
    primaryDownload: {
      label: "Download Brochure",
      href: "#",
      type: "brochure",
    },
    showDemoCta: true,
    collapsibleFullSpecs: true,
    visualStory: {
      heading: "See Modern POS in action",
      items: [
        {
          id: "checkout",
          label: "Checkout",
          image: softwareHeroImage(
            "software-modern-pos.jpg",
            "Modern POS checkout screen",
          ),
          caption: "Fast register workflows with barcode, search, and weighed items.",
        },
        {
          id: "inventory",
          label: "Inventory",
          image: softwareHeroImage(
            "software-warehouse-management-system.jpg",
            "Inventory visibility dashboard",
          ),
          caption: "Real-time stock lookup across stores and warehouses.",
        },
        {
          id: "compliance",
          label: "ZATCA",
          image: softwareHeroImage(
            "software-zatca-integration.jpg",
            "ZATCA e-invoicing compliance",
          ),
          caption: "Automated ZATCA Phase 2 e-invoicing from the register.",
        },
      ],
    },
    trustIndicators: [
      { label: "Deployment", value: "Cloud or on-premise" },
      { label: "Compliance", value: "ZATCA e-invoicing ready" },
      { label: "Integration", value: "ERPNext · WMS · Loyalty" },
      { label: "Support", value: "Printechs Saudi Arabia" },
    ],
    keyValueCards: [
      {
        icon: "checkout",
        title: "Fast checkout",
        description:
          "Streamlined register workflows with barcode, search, and weighed-item support.",
      },
      {
        icon: "inventory",
        title: "Inventory control",
        description:
          "Real-time stock visibility across stores, warehouses, and back office.",
      },
      {
        icon: "store",
        title: "Multi-store management",
        description:
          "Centralised pricing, promotions, and reporting for every location.",
      },
      {
        icon: "loyalty",
        title: "Loyalty & promotions",
        description:
          "Member pricing, points, and campaign tools built into checkout.",
      },
    ],
    capabilityModules: [
      {
        icon: "checkout",
        title: "Sales",
        items: [
          "Quick billing and barcode scanning",
          "Multiple payment methods",
          "Returns, refunds, and void controls",
        ],
      },
      {
        icon: "inventory",
        title: "Inventory",
        items: [
          "Real-time stock lookup",
          "Inter-store transfers",
          "Weighed and variant items",
        ],
      },
      {
        icon: "loyalty",
        title: "Customers",
        items: [
          "Member profiles and loyalty points",
          "Campaign redemption at register",
          "Customer purchase history",
        ],
      },
      {
        icon: "store",
        title: "Promotions",
        items: [
          "Centralised offer management",
          "Mix-and-match deals",
          "Manager override controls",
        ],
      },
      {
        icon: "report",
        title: "Reports",
        items: [
          "End-of-day reconciliation",
          "Store-level KPI dashboards",
          "Cashier performance tracking",
        ],
      },
      {
        icon: "integration",
        title: "Integrations",
        items: [
          "ERPNext native sync",
          "E-commerce and API layer",
          "Payment terminal connectivity",
        ],
      },
    ],
    iconSpecifications: [
      {
        icon: "cloud",
        title: "Deployment",
        description: "Cloud SaaS or on-premise · unlimited registers per store",
      },
      {
        icon: "integration",
        title: "ERP integration",
        description: "ERPNext native · real-time sales and stock sync",
      },
      {
        icon: "zatca",
        title: "Compliance",
        description: "ZATCA Phase 2 e-invoicing · audit-ready workflows",
      },
      {
        icon: "device",
        title: "Device support",
        description: "Windows and Android POS terminals",
      },
      {
        icon: "report",
        title: "Languages",
        description: "English and Arabic interface support",
      },
      {
        icon: "connectivity",
        title: "Offline mode",
        description: "Continue selling when connectivity is interrupted",
      },
    ],
    applicationCards: [
      {
        title: "Grocery",
        description: "High-volume checkout with weighed items and promotions.",
        image: industryImage("industry-retail.jpg", "Grocery retail"),
        href: "/industries/retail",
      },
      {
        title: "Fashion retail",
        description: "Variant items, loyalty, and multi-store inventory control.",
        image: industryImage("industry-fashion.jpg", "Fashion retail store"),
        href: "/industries/fashion",
      },
      {
        title: "Specialty retail",
        description: "Deli, bakery, and fresh-food counters with scale integration.",
        image: industryImage("industry-bakery.jpg", "Specialty food retail"),
        href: "/industries/bakery",
      },
      {
        title: "Multi-store chains",
        description: "Centralised pricing, reporting, and franchise operations.",
        image: industryImage(
          "industry-food-beverage.jpg",
          "Multi-store food retail",
        ),
        href: "/industries/food-beverage",
      },
    ],
    supportServiceItems: [
      {
        icon: "install",
        title: "Discovery & rollout",
        description: "Process mapping, store deployment, and cashier training.",
      },
      {
        icon: "integration",
        title: "ERP integration",
        description: "ERPNext setup, data migration, and API connectivity.",
      },
      {
        icon: "zatca",
        title: "ZATCA compliance",
        description: "e-Invoicing configuration and compliance validation.",
      },
      {
        icon: "training",
        title: "Ongoing support",
        description: "Help desk, updates, and continuous improvement.",
      },
    ],
    ecosystemItems: [
      {
        slug: "pos-terminal",
        name: "POS Terminal",
        summary: "Checkout hardware",
        href: "#",
        image: productImage("POS terminal"),
      },
      {
        slug: "datalogic-memor-12",
        name: "Handheld Device",
        summary: "Floor inventory",
        href: "/products/datalogic-memor-12",
        image: productImage("Datalogic Memor 12"),
      },
      {
        slug: "avery-berkel-weighing",
        name: "Weighing Scale",
        summary: "Deli & fresh food",
        href: "/products/avery-berkel-weighing",
        image: productImage("Avery Berkel"),
      },
      {
        slug: "zebra-mobility",
        name: "Barcode Scanner",
        summary: "Retail scanning",
        href: "/products/zebra-mobility",
        image: productImage("Zebra"),
      },
    ],
    storyHeading: "Retail operations, unified at the register",
    features: [
      "Multi-store and multi-register support",
      "Barcode, search, and weighed-item sales",
      "Offline-capable store operation",
      "ZATCA Phase 2 e-invoicing integration",
      "ERPNext inventory and sales sync",
      "Member loyalty and promotions engine",
      "Role-based cashier and manager access",
      "End-of-day reporting and cash reconciliation",
      "Integration with Datalogic and Zebra scanners",
    ],
    keySpecifications: [
      { label: "Deployment", value: "Cloud SaaS or on-premise" },
      { label: "Registers", value: "Unlimited per store" },
      { label: "ERP integration", value: "ERPNext native" },
      { label: "Compliance", value: "ZATCA e-invoicing" },
      { label: "Hardware", value: "Windows · Android terminals" },
      { label: "Languages", value: "English · Arabic" },
    ],
    softwareCapabilities: [
      "Unified checkout for standard, weighed, and variant items",
      "Real-time stock lookup across stores and warehouses",
      "Customer loyalty points, tiers, and campaign redemption",
      "Manager overrides, discounts, and void controls",
      "Sales analytics dashboard with store-level KPIs",
      "API layer for e-commerce and third-party integrations",
      "Automated ZATCA invoice generation and submission",
      "Centralised user, role, and permission management",
    ],
    applications: [
      "Supermarkets and grocery chains",
      "Fashion and lifestyle retail",
      "Food service and quick-service restaurants",
      "Pharmacy and health retail",
      "Specialty retail with weighed products",
    ],
    industrySlugs: ["retail", "fashion", "food-beverage", "bakery"],
    compatibleHardware: [
      {
        slug: "datalogic-memor-12",
        name: "Datalogic Memor 12",
        summary: "Mobile computer for floor inventory and assisted selling",
        href: "/products/datalogic-memor-12",
        image: productImage("Datalogic Memor 12"),
      },
      {
        slug: "avery-berkel-weighing",
        name: "Avery Berkel Scales",
        summary: "Integrated weighing for deli and fresh-food counters",
        href: "/products/avery-berkel-weighing",
        image: productImage("Avery Berkel"),
      },
    ],
    supportServices: [
      "Discovery workshops and process mapping",
      "Store rollout and cashier training",
      "ERPNext integration and data migration",
      "ZATCA compliance configuration",
      "Ongoing support and feature updates",
    ],
    downloads: [
      {
        label: "Modern POS Product Overview",
        href: "#",
        type: "brochure",
      },
      {
        label: "Integration Capabilities Guide",
        href: "#",
        type: "other",
      },
    ],
    relatedProducts: [
      {
        slug: "erpnext",
        name: "ERPNext",
        summary: "Integrated ERP for finance, inventory, and operations",
        href: "/software/erpnext",
        image: softwareHeroImage(
          "software-erpnext.jpg",
          "ERPNext business dashboard",
        ),
      },
      {
        slug: "printechs-loyalty-management-system",
        name: "Printechs Loyalty Management",
        summary: "Customer loyalty and engagement platform",
        href: "/software/printechs-loyalty-management-system",
        image: softwareHeroImage(
          "software-printechs-loyalty-management-system.jpg",
          "Loyalty management dashboard",
        ),
      },
    ],
    finalCta: {
      heading: "See Modern POS in your store environment",
      description:
        "Book a demo with Printechs to explore checkout workflows, ERP integration, and ZATCA compliance for your retail operation.",
    },
    seo: {
      title: "Modern POS | Printechs Software",
      description: "Modern POS software solutions from Printechs.",
      canonicalPath: "/software/modern-pos",
    },
    canonicalPath: "/software/modern-pos",
    breadcrumbRoot: { label: "Software", href: "/software" },
  },
};

export function getProductPage(slug: string): ProductPageContent | undefined {
  return productPages[slug];
}

export function getAllProductPageSlugs(): string[] {
  return Object.keys(productPages);
}
