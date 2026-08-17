import type { FeaturedSolution } from "@/types/content";

/**
 * Homepage featured solutions — distinct from division category cards.
 * Drop images into frontend/printechs-web/public/images/solutions/
 * (1600 × 1000 / 16:10 recommended). JPG or PNG both work.
 */
const solutionImage = (filename: string, alt: string) => ({
  src: `/images/solutions/${filename}`,
  alt,
  width: 1600,
  height: 1000,
});

export const featuredSolutions: FeaturedSolution[] = [
  {
    id: "featured-production-coding",
    title: "Production Coding & Marking",
    description:
      "Reliable coding and marking for products, packaging and production lines.",
    href: "/solutions/coding-marking",
    image: solutionImage(
      "featured-production-coding-marking.jpg",
      "Industrial coding and marking system operating on a production line",
    ),
  },
  {
    id: "featured-product-traceability",
    title: "Product Traceability",
    description:
      "Connect products, batches and production data for greater visibility and control.",
    href: "/solutions/traceability",
    image: solutionImage(
      "featured-product-traceability.png",
      "Product barcode and traceability identification technology",
    ),
  },
  {
    id: "featured-connected-retail",
    title: "Connected Retail Operations",
    description:
      "Integrate POS, weighing, mobility and store technology into a smarter retail environment.",
    href: "/solutions/retail-automation",
    image: solutionImage(
      "featured-connected-retail.png",
      "Connected retail POS and store automation technology",
    ),
  },
  {
    id: "featured-enterprise-warehouse",
    title: "Enterprise & Warehouse Systems",
    description:
      "Connect ERP, warehouse, POS and compliance systems for better operational control.",
    href: "/software",
    image: solutionImage(
      "featured-enterprise-warehouse.png",
      "Enterprise ERP and warehouse management software systems",
    ),
  },
];
