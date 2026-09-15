import type { SoftwareSolution } from "@/types/content";

const softwareImageFile = (filename: string, alt: string) => ({
  src: `/images/software/${filename}`,
  alt,
  width: 1600,
  height: 1000,
});

export const softwareSolutions: SoftwareSolution[] = [
  {
    id: "sw-modern-pos",
    slug: "modern-pos",
    name: "Modern POS",
    summary: "A contemporary point-of-sale platform for multi-store retail operations.",
    highlights: ["Omnichannel ready", "Store operations", "Loyalty ready"],
    image: softwareImageFile(
      "software-modern-pos.jpg",
      "Modern POS checkout with scanner, terminal and payment system",
    ),
    relatedIndustrySlugs: ["retail", "fashion", "food-beverage"],
    seo: {
      title: "Modern POS | Printechs Software",
      description: "Modern POS software solutions from Printechs.",
      canonicalPath: "/software/modern-pos",
    },
  },
  {
    id: "sw-wms",
    slug: "warehouse-management-system",
    name: "Warehouse Management System",
    summary: "Control inventory movement, picking accuracy and warehouse throughput.",
    highlights: ["Inbound / outbound", "Inventory visibility", "Mobile workflows"],
    image: softwareImageFile(
      "software-warehouse-management-system.jpg",
      "Warehouse management picking list with scanner, label printer and dashboard",
    ),
    relatedIndustrySlugs: ["warehouse-logistics", "retail"],
    seo: {
      title: "Warehouse Management System | Printechs Software",
      description: "Warehouse management software from Printechs.",
      canonicalPath: "/software/warehouse-management-system",
    },
  },
  {
    id: "sw-erpnext",
    slug: "erpnext",
    name: "ERPNext",
    summary: "Integrated ERP for finance, inventory, manufacturing and service operations.",
    highlights: ["Unified operations", "Local expertise", "Scalable deployment"],
    image: softwareImageFile(
      "software-erpnext.jpg",
      "ERPNext business dashboard with sales, inventory and finance metrics",
    ),
    relatedIndustrySlugs: ["retail", "manufacturing", "warehouse-logistics"],
    seo: {
      title: "ERPNext | Printechs Software",
      description: "ERPNext implementation and support with Printechs.",
      canonicalPath: "/software/erpnext",
    },
  },
  {
    id: "sw-zatca",
    slug: "zatca-integration",
    name: "ZATCA Integration",
    summary: "e-Invoicing compliance integration aligned with Saudi ZATCA requirements.",
    highlights: ["Compliance workflows", "ERP connectivity", "Audit readiness"],
    image: softwareImageFile(
      "software-zatca-integration.jpg",
      "ZATCA e-invoicing compliance dashboard across desktop, laptop and mobile",
    ),
    relatedIndustrySlugs: ["retail", "food-beverage"],
    seo: {
      title: "ZATCA Integration | Printechs Software",
      description: "ZATCA e-invoicing integration services from Printechs.",
      canonicalPath: "/software/zatca-integration",
    },
  },
  {
    id: "sw-plms",
    slug: "printechs-loyalty-management-system",
    name: "Printechs Loyalty Management System",
    summary: "Loyalty and customer engagement platform designed for retail growth.",
    highlights: ["Campaigns", "Member insights", "POS integration"],
    image: softwareImageFile(
      "software-printechs-loyalty-management-system.jpg",
      "Printechs loyalty management dashboard with member points and campaigns",
    ),
    relatedIndustrySlugs: ["retail", "fashion"],
    seo: {
      title: "Printechs Loyalty Management System",
      description: "Loyalty management software from Printechs.",
      canonicalPath: "/software/printechs-loyalty-management-system",
    },
  },
  {
    id: "sw-mobile",
    slug: "mobile-applications",
    name: "Mobile Applications",
    summary: "Custom and packaged mobile apps for field, warehouse and retail teams.",
    highlights: ["Field operations", "Offline capable", "Device integration"],
    image: softwareImageFile(
      "software-mobile-applications.jpg",
      "Mobile warehouse application with handheld scanner and label printer",
    ),
    seo: {
      title: "Mobile Applications | Printechs Software",
      description: "Mobile application development with Printechs.",
      canonicalPath: "/software/mobile-applications",
    },
  },
  {
    id: "sw-van-sales",
    slug: "van-sales",
    name: "VAN Sales",
    summary:
      "Mobile field sales, van inventory, delivery, invoices, collections and printing — on ERPNext.",
    highlights: ["ERPNext van warehouse", "Offline ready", "ZATCA integrated"],
    image: softwareImageFile(
      "software-van-sales.jpg",
      "Sales van at a customer location while the representative delivers cartons",
    ),
    relatedIndustrySlugs: ["retail", "food-beverage", "warehouse-logistics"],
    seo: {
      title: "Van Sales Software Saudi Arabia | ERPNext & ZATCA | Printechs",
      description:
        "Van Sales software for Saudi Arabia integrated with ERPNext and ZATCA. Manage van stock, orders, delivery, invoices, payments, offline sales, barcode scanning and mobile printing.",
      canonicalPath: "/software/van-sales",
    },
  },
  {
    id: "sw-ecommerce",
    slug: "e-commerce-solutions",
    name: "E-Commerce Solutions",
    summary: "ERPNext-connected web store and mobile apps with Aramex delivery and live tracking.",
    highlights: ["ERPNext catalogue & stock", "Aramex live tracking", "Android and iOS apps"],
    image: softwareImageFile(
      "software-e-commerce-solutions.jpg",
      "ShoeArena ERPNext e-commerce storefront built by Printechs",
    ),
    relatedIndustrySlugs: ["retail", "fashion"],
    seo: {
      title: "E-Commerce Solutions | Printechs Software",
      description: "E-commerce software solutions from Printechs.",
      canonicalPath: "/software/e-commerce-solutions",
    },
  },
  {
    id: "sw-api",
    slug: "api-integration",
    name: "API Integration",
    summary: "APIs, middleware and device interfaces that connect ERP, machines and the shop floor.",
    highlights: ["Software ↔ Machine", "Middleware", "Saudi platforms"],
    image: softwareImageFile(
      "software-api-integration.jpg",
      "Printechs integration layer connecting ERP, machines and devices",
    ),
    relatedIndustrySlugs: ["retail", "warehouse-logistics", "packaging"],
    seo: {
      title: "API & System Integration Saudi Arabia | ERP, Machines & IoT | Printechs",
      description:
        "Connect ERP, POS, e-commerce, warehouse systems, RFID, barcode devices, weighing scales and industrial machines.",
      canonicalPath: "/software/api-integration",
    },
  },
  {
    id: "sw-custom",
    slug: "custom-software-development",
    name: "Custom Software Development",
    summary: "Van sales, shelf labels, scales, mobile inventory and price checkers — built around your workflow.",
    highlights: ["Van sales", "Device integration", "ERP / POS connected"],
    image: softwareImageFile(
      "software-custom-software-development.jpg",
      "Field team using a custom handheld application at a delivery van",
    ),
    relatedIndustrySlugs: ["retail", "fashion", "warehouse-logistics", "food-beverage"],
    seo: {
      title: "Custom Software Development Saudi Arabia | Mobile, ERP & Device Integration | Printechs",
      description:
        "Custom software for van sales, mobile inventory, shelf-label printing, platform scales and price checkers.",
      canonicalPath: "/software/custom-software-development",
    },
  },
];

export function getFeaturedSoftware(limit = 6): SoftwareSolution[] {
  return softwareSolutions.slice(0, limit);
}

export function getSoftwareBySlug(slug: string): SoftwareSolution | undefined {
  return softwareSolutions.find((item) => item.slug === slug);
}
