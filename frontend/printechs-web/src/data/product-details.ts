import type { ProductDetailContent } from "@/types/content";
import { productPages } from "@/data/product-pages";

export const productDetails: Record<string, ProductDetailContent> = {
  "hitachi-ux-d161": {
    displayName: "Hitachi UX-D161W",
    itemCode: "IND.SYS.HIJ.1995",
    tagline: "Dynamic Smart Bottle industrial inkjet printer",
    overview:
      "High-performance continuous inkjet printer for production line marking on metal, plastic, film, and packaging — with wireless connectivity and easy maintenance.",
    description:
      "The Hitachi UX-D161W is an industrial continuous inkjet (CIJ) printer designed for demanding manufacturing environments. Using a non-contact printing method, it applies codes, dates, and batch data to products moving on production lines at high speed.\n\nBuilt for reliability in harsh conditions, the UX-D161W combines advanced ink delivery, automatic nozzle cleaning, and remote monitoring capability. Printechs supplies, installs, and supports Hitachi UX systems across Saudi Arabia with local expertise and service coverage.",
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
    specGroups: [
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
    packageContents: [
      "UX-D161W printer main unit",
      "2 L starter ink smart bottle",
      "Mounting kit",
      "Power and interface cabling",
    ],
    relatedProductSlugs: ["hitachi-ux-d160", "rea-jet-coding-systems"],
  },
  "hitachi-ux-d160": {
    displayName: "Hitachi UX-D160W",
    itemCode: "IND.SYS.HIJ.1994",
    tagline: "Industrial inkjet printer with wireless connectivity",
    overview:
      "Higher functionality and easier installation for a variety of printing needs — built for speed, flexibility, and durability on production lines.",
    description:
      "The Hitachi UX-D160W delivers continuous inkjet marking for metals, plastics, films, papers, and packaging substrates. Its non-contact printing method, robust construction, and intuitive interface make it a proven choice for industrial coding applications.\n\nPrintechs provides UX-D160W supply, integration, and ongoing support for manufacturers across the Kingdom.",
    features: [
      "Continuous inkjet non-contact printing",
      "Wireless 802.11ac connectivity",
      "600 dpi high-resolution output",
      "IP65-rated stainless steel enclosure",
      "Touchscreen interface",
      "Automatic nozzle cleaning",
      "Multi-language operator support",
      "Remote monitoring ready",
    ],
    specGroups: [
      {
        title: "Printing performance",
        items: [
          { label: "Print resolution", value: "600 dpi" },
          { label: "Print speed", value: "5 m/s" },
          { label: "Character height", value: "1–12 mm" },
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
          { label: "Ink capacity", value: "2 L" },
          { label: "Drying time", value: "0.3–3 seconds" },
        ],
      },
    ],
    packageContents: [
      "UX-D160W printer main unit",
      "2 L starter ink pack",
      "Mounting kit",
    ],
    relatedProductSlugs: ["hitachi-ux-d161", "rea-jet-coding-systems"],
  },
};

export function getProductDetail(slug: string): ProductDetailContent | undefined {
  const page = productPages[slug];
  if (!page) return productDetails[slug];

  return {
    displayName: page.displayName,
    itemCode: page.itemCode,
    tagline: page.tagline,
    overview: page.shortDescription,
    description: page.longDescription,
    features: page.features,
    specGroups: page.fullSpecifications ?? [],
    packageContents: page.packageContents,
    relatedProductSlugs: page.relatedProducts?.map((item) => item.slug),
  };
}
