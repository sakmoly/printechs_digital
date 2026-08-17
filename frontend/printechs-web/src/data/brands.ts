import type { Brand, Product } from "@/types/content";
import { products } from "./products";

const brandLogo = (filename: string, alt: string) => ({
  src: `/images/brands/${filename}`,
  alt,
  width: 400,
  height: 160,
});

export const brands: Brand[] = [
  {
    id: "brand-hitachi",
    slug: "hitachi",
    name: "Hitachi",
    summary:
      "Industrial continuous inkjet coding technology for high-speed production lines.",
    logo: brandLogo("brand-hitachi.png", "Hitachi"),
    seo: {
      title: "Hitachi | Printechs Brands",
      description: "Hitachi coding technology supplied and supported by Printechs.",
      canonicalPath: "/brands/hitachi",
    },
  },
  {
    id: "brand-rea-jet",
    slug: "rea-jet",
    name: "REA JET",
    summary: "Industrial coding and marking systems for packaging and manufacturing.",
    logo: brandLogo("brand-rea-jet.png", "REA JET"),
    seo: {
      title: "REA JET | Printechs Brands",
      description: "REA JET coding solutions with Printechs.",
      canonicalPath: "/brands/rea-jet",
    },
  },
  {
    id: "brand-datalogic",
    slug: "datalogic",
    name: "Datalogic",
    summary: "Barcode scanning and data capture for retail, warehouse and industry.",
    logo: brandLogo("brand-datalogic.png", "Datalogic"),
    seo: {
      title: "Datalogic | Printechs Brands",
      description: "Datalogic barcode and mobility solutions with Printechs.",
      canonicalPath: "/brands/datalogic",
    },
  },
  {
    id: "brand-zebra",
    slug: "zebra",
    name: "Zebra",
    summary: "Enterprise mobility, printing and identification technology.",
    logo: brandLogo("brand-zebra.png", "Zebra"),
    seo: {
      title: "Zebra | Printechs Brands",
      description: "Zebra enterprise mobility solutions with Printechs.",
      canonicalPath: "/brands/zebra",
    },
  },
  {
    id: "brand-avery",
    slug: "avery-berkel",
    name: "Avery Berkel",
    summary: "Retail and food weighing systems built for accuracy and uptime.",
    logo: brandLogo("brand-avery-berkel.png", "Avery Berkel"),
    seo: {
      title: "Avery Berkel | Printechs Brands",
      description: "Avery Berkel weighing solutions with Printechs.",
      canonicalPath: "/brands/avery-berkel",
    },
  },
  {
    id: "brand-cas",
    slug: "cas",
    name: "CAS",
    summary: "Weighing and retail scale technology for store and food operations.",
    logo: brandLogo("brand-cas.png", "CAS"),
    seo: {
      title: "CAS | Printechs Brands",
      description: "CAS weighing solutions with Printechs.",
      canonicalPath: "/brands/cas",
    },
  },
];

export function getBrandBySlug(slug: string): Brand | undefined {
  return brands.find((brand) => brand.slug === slug);
}

export function getProductsByBrandName(brandName: string): Product[] {
  return products.filter(
    (product) =>
      !product.hubProductSlugs &&
      product.brand.toLowerCase() === brandName.toLowerCase()
  );
}
