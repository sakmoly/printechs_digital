import type { SoftwareSolution } from "@/types/content";

const softwareImage = (name: string) => ({
  src: "/images/placeholders/software.svg",
  alt: `${name} software interface`,
  width: 1600,
  height: 1000,
});

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
    id: "sw-ecommerce",
    slug: "e-commerce-solutions",
    name: "E-Commerce Solutions",
    summary: "Digital commerce experiences connected to inventory and fulfilment.",
    highlights: ["Catalogue sync", "Order workflows", "Retail integration"],
    image: softwareImage("E-Commerce"),
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
    summary: "Secure system integration between ERP, POS, WMS and partner platforms.",
    highlights: ["API design", "Data sync", "Middleware"],
    image: softwareImage("API Integration"),
    seo: {
      title: "API Integration | Printechs Software",
      description: "API and systems integration services from Printechs.",
      canonicalPath: "/software/api-integration",
    },
  },
  {
    id: "sw-custom",
    slug: "custom-software-development",
    name: "Custom Software Development",
    summary: "Purpose-built applications for specialised operational requirements.",
    highlights: ["Discovery", "Delivery", "Long-term support"],
    image: softwareImage("Custom Software"),
    seo: {
      title: "Custom Software Development | Printechs",
      description: "Custom software development with Printechs.",
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
