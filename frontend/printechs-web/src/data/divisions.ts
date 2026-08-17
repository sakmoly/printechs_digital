import type { BusinessDivision } from "@/types/content";

export const businessDivisions: BusinessDivision[] = [
  {
    id: "industrial",
    title: "Industrial Solutions",
    summary:
      "Coding, marking, traceability and identification systems engineered for production environments.",
    href: "/solutions/coding-marking",
    items: ["Coding & Marking", "Traceability", "RFID", "System Integration"],
    image: {
      src: "/images/divisions/division-industrial.jpg",
      alt: "Hitachi industrial coding and marking system on a production line",
      width: 1200,
      height: 900,
    },
  },
  {
    id: "retail",
    title: "Retail Solutions",
    summary:
      "Store automation, barcode mobility and weighing technology for modern retail operations.",
    href: "/solutions/retail-automation",
    items: [
      "Barcode & Mobility",
      "Electronic Shelf Labels",
      "Weighing",
      "Retail Hardware",
    ],
    image: {
      src: "/images/divisions/division-retail.jpg",
      alt: "Retail POS, barcode scanner and weighing system in a grocery store",
      width: 1200,
      height: 900,
    },
  },
  {
    id: "software",
    title: "Software Solutions",
    summary:
      "Enterprise platforms that connect operations, compliance and growth across the business.",
    href: "/software",
    items: [
      "Modern POS",
      "ERPNext",
      "Warehouse Management",
      "ZATCA Integration",
      "Loyalty",
    ],
    image: {
      src: "/images/divisions/division-software.jpg",
      alt: "Enterprise software dashboards across desktop, POS, mobile and tablet",
      width: 1200,
      height: 900,
    },
  },
];
