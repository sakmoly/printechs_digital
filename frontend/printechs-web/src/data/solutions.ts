import type { Solution } from "@/types/content";

const image = (name: string) => ({
  src: "/images/placeholders/solution.svg",
  alt: `${name} solution placeholder`,
  width: 800,
  height: 500,
});

export const solutions: Solution[] = [
  {
    id: "sol-coding",
    slug: "coding-marking",
    name: "Coding & Marking",
    summary: "Industrial coding systems that keep production lines compliant and readable.",
    image: image("Coding & Marking"),
    relatedProductSlugs: ["hitachi-ux-d161", "hitachi-ux-d160", "rea-jet-coding-systems"],
    seo: {
      title: "Coding & Marking Solutions | Printechs",
      description: "Industrial coding and marking solutions from Printechs.",
      canonicalPath: "/solutions/coding-marking",
    },
  },
  {
    id: "sol-traceability",
    slug: "traceability",
    name: "Traceability",
    summary: "End-to-end identification strategies for product and batch visibility.",
    image: image("Traceability"),
    seo: {
      title: "Traceability Solutions | Printechs",
      description: "Traceability solutions from Printechs.",
      canonicalPath: "/solutions/traceability",
    },
  },
  {
    id: "sol-barcode",
    slug: "barcode-mobility",
    name: "Barcode & Mobility",
    summary: "Scanning, printing and mobile computing for accurate operations.",
    image: image("Barcode & Mobility"),
    relatedProductSlugs: ["autoid-solutions", "datalogic-barcode-solutions", "zebra-mobility"],
    seo: {
      title: "Barcode & Mobility | Printechs",
      description: "Barcode and mobility solutions from Printechs.",
      canonicalPath: "/solutions/barcode-mobility",
    },
  },
  {
    id: "sol-retail",
    slug: "retail-automation",
    name: "Retail Automation",
    summary: "Connected store technology that improves speed, accuracy and experience.",
    image: image("Retail Automation"),
    seo: {
      title: "Retail Automation | Printechs",
      description: "Retail automation solutions from Printechs.",
      canonicalPath: "/solutions/retail-automation",
    },
  },
  {
    id: "sol-wh",
    slug: "warehouse-automation",
    name: "Warehouse Automation",
    summary: "Hardware and software designed for efficient warehouse execution.",
    image: image("Warehouse Automation"),
    relatedSoftwareSlugs: ["warehouse-management-system"],
    seo: {
      title: "Warehouse Automation | Printechs",
      description: "Warehouse automation solutions from Printechs.",
      canonicalPath: "/solutions/warehouse-automation",
    },
  },
  {
    id: "sol-pos",
    slug: "pos-retail-software",
    name: "POS & Retail Software",
    summary: "Software platforms that power modern retail selling and operations.",
    image: image("POS & Retail Software"),
    relatedSoftwareSlugs: ["modern-pos", "printechs-loyalty-management-system"],
    seo: {
      title: "POS & Retail Software | Printechs",
      description: "POS and retail software solutions from Printechs.",
      canonicalPath: "/solutions/pos-retail-software",
    },
  },
  {
    id: "sol-erp",
    slug: "erp-business-automation",
    name: "ERP & Business Automation",
    summary: "Business systems that unify finance, inventory and service delivery.",
    image: image("ERP & Business Automation"),
    relatedSoftwareSlugs: ["erpnext", "zatca-integration"],
    seo: {
      title: "ERP & Business Automation | Printechs",
      description: "ERP and business automation from Printechs.",
      canonicalPath: "/solutions/erp-business-automation",
    },
  },
  {
    id: "sol-rfid",
    slug: "rfid",
    name: "RFID",
    summary: "RFID identification for inventory visibility and process control.",
    image: image("RFID"),
    seo: {
      title: "RFID Solutions | Printechs",
      description: "RFID solutions from Printechs.",
      canonicalPath: "/solutions/rfid",
    },
  },
  {
    id: "sol-esl",
    slug: "electronic-shelf-labels",
    name: "Electronic Shelf Labels",
    summary: "Dynamic pricing displays for accurate and efficient store operations.",
    image: image("Electronic Shelf Labels"),
    seo: {
      title: "Electronic Shelf Labels | Printechs",
      description: "Electronic shelf label solutions from Printechs.",
      canonicalPath: "/solutions/electronic-shelf-labels",
    },
  },
  {
    id: "sol-integration",
    slug: "system-integration",
    name: "System Integration",
    summary: "Connecting hardware, software and operational processes into one stack.",
    image: image("System Integration"),
    relatedSoftwareSlugs: ["api-integration"],
    seo: {
      title: "System Integration | Printechs",
      description: "System integration services from Printechs.",
      canonicalPath: "/solutions/system-integration",
    },
  },
];

export function getFeaturedSolutions(limit = 4): Solution[] {
  return solutions.slice(0, limit);
}
