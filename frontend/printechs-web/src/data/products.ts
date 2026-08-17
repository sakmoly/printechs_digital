import type { Product } from "@/types/content";

const productImage = (label: string) => ({
  src: `/images/placeholders/product.svg`,
  alt: `${label} visual`,
  width: 1200,
  height: 1200,
});

export const products: Product[] = [
  {
    id: "prod-hitachi-ux-d161",
    slug: "hitachi-ux-d161",
    name: "UX-D161W",
    brand: "Hitachi",
    summary: "Continuous inkjet coder designed for high-speed industrial production lines.",
    category: "Coding & Marking",
    division: "industrial",
    image: productImage("Hitachi UX-D161W"),
    relatedIndustrySlugs: ["dairy", "food-beverage", "packaging"],
    relatedSolutionSlugs: ["coding-marking", "traceability"],
    seo: {
      title: "Hitachi UX-D161W | Printechs",
      description: "Discover Hitachi UX-D161W continuous inkjet coding solutions from Printechs.",
      canonicalPath: "/products/hitachi-ux-d161",
    },
  },
  {
    id: "prod-hitachi-ux-d160",
    slug: "hitachi-ux-d160",
    name: "UX-D160W",
    brand: "Hitachi",
    summary: "Reliable industrial coding platform for demanding manufacturing environments.",
    category: "Coding & Marking",
    division: "industrial",
    image: productImage("Hitachi UX-D160W"),
    relatedIndustrySlugs: ["pharmaceutical", "plastic", "steel"],
    relatedSolutionSlugs: ["coding-marking"],
    seo: {
      title: "Hitachi UX-D160W | Printechs",
      description: "Explore Hitachi UX-D160W industrial coding technology with Printechs.",
      canonicalPath: "/products/hitachi-ux-d160",
    },
  },
  {
    id: "prod-rea-jet",
    slug: "rea-jet-coding-systems",
    name: "Coding Systems",
    brand: "REA JET",
    summary: "High-resolution and large-character coding systems for industrial packaging.",
    category: "Coding & Marking",
    division: "industrial",
    image: productImage("REA JET"),
    relatedIndustrySlugs: ["pipe", "packaging", "steel"],
    relatedSolutionSlugs: ["coding-marking", "traceability"],
    seo: {
      title: "REA JET | Printechs",
      description: "REA JET industrial coding systems supplied and supported by Printechs.",
      canonicalPath: "/products/rea-jet-coding-systems",
    },
  },
  {
    id: "prod-datalogic-memor-12",
    slug: "datalogic-memor-12",
    name: "Memor 12",
    brand: "Datalogic",
    summary:
      "Full-touch mobile computer for retail floor and warehouse mobility workflows.",
    category: "Barcode & Mobility",
    division: "retail",
    image: productImage("Datalogic Memor 12"),
    relatedIndustrySlugs: ["retail", "warehouse-logistics", "fashion"],
    relatedSolutionSlugs: ["barcode-mobility", "warehouse-automation"],
    seo: {
      title: "Datalogic Memor 12 | Printechs",
      description:
        "Datalogic Memor 12 mobile computer for retail and warehouse — supplied by Printechs.",
      canonicalPath: "/products/datalogic-memor-12",
    },
  },
  {
    id: "prod-datalogic",
    slug: "datalogic-barcode-solutions",
    name: "Scanning & Data Capture",
    brand: "Datalogic",
    summary:
      "Barcode scanners and data capture devices for retail, warehouse, and industrial use.",
    category: "Barcode & Mobility",
    division: "retail",
    image: productImage("Datalogic"),
    relatedIndustrySlugs: ["retail", "warehouse-logistics"],
    relatedSolutionSlugs: ["barcode-mobility", "warehouse-automation"],
    seo: {
      title: "Datalogic AutoID Solutions | Printechs",
      description: "Datalogic scanning and data capture solutions from Printechs.",
      canonicalPath: "/products/datalogic-barcode-solutions",
    },
  },
  {
    id: "prod-zebra",
    slug: "zebra-mobility",
    name: "Mobility & Printing",
    brand: "Zebra",
    summary: "Enterprise mobile computers and printers for connected operations.",
    category: "Barcode & Mobility",
    division: "retail",
    image: productImage("Zebra"),
    relatedIndustrySlugs: ["retail", "warehouse-logistics", "fashion"],
    relatedSolutionSlugs: ["barcode-mobility", "warehouse-automation"],
    seo: {
      title: "Zebra AutoID Solutions | Printechs",
      description: "Zebra enterprise mobility and printing solutions with Printechs expertise.",
      canonicalPath: "/products/zebra-mobility",
    },
  },
  {
    id: "prod-avery-berkel",
    slug: "avery-berkel-weighing",
    name: "Scale",
    brand: "Avery Berkel",
    summary: "Retail and food weighing solutions built for accuracy and uptime.",
    category: "Weighing",
    division: "retail",
    image: productImage("Avery Berkel"),
    relatedIndustrySlugs: ["retail", "food-beverage", "bakery"],
    relatedSolutionSlugs: ["retail-automation"],
    seo: {
      title: "Avery Berkel Scale | Printechs",
      description: "Avery Berkel scale and weighing solutions available through Printechs.",
      canonicalPath: "/products/avery-berkel-weighing",
    },
  },
  {
    id: "prod-autoid-solutions",
    slug: "autoid-solutions",
    name: "AutoID Solutions",
    brand: "Datalogic / Zebra",
    summary:
      "Scanning, printing, and mobile computing for accurate retail, warehouse, and industrial operations.",
    category: "Barcode & Mobility",
    division: "retail",
    image: productImage("AutoID Solutions"),
    hubProductSlugs: ["datalogic-barcode-solutions", "zebra-mobility"],
    relatedIndustrySlugs: ["retail", "warehouse-logistics"],
    relatedSolutionSlugs: ["barcode-mobility", "warehouse-automation"],
    seo: {
      title: "AutoID Solutions | Datalogic & Zebra | Printechs",
      description:
        "Explore Datalogic and Zebra AutoID solutions supplied and supported by Printechs.",
      canonicalPath: "/products/autoid-solutions",
    },
  },
];

const FEATURED_PRODUCT_SLUGS = [
  "hitachi-ux-d161",
  "avery-berkel-weighing",
  "rea-jet-coding-systems",
  "autoid-solutions",
] as const;

export function getFeaturedProducts(limit = 4): Product[] {
  return FEATURED_PRODUCT_SLUGS.slice(0, limit)
    .map((slug) => products.find((item) => item.slug === slug))
    .filter((item): item is Product => item !== undefined);
}

export function getProductBySlug(slug: string): Product | undefined {
  return products.find((item) => item.slug === slug);
}

export function getProductHubChildren(hub: Product): Product[] {
  if (!hub.hubProductSlugs?.length) return [];

  return hub.hubProductSlugs
    .map((slug) => getProductBySlug(slug))
    .filter((item): item is Product => item !== undefined);
}
