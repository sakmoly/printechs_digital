import type { SolutionPageContent } from "@/types/content";

const solutionImage = (filename: string, alt: string) => ({
  src: `/images/solutions/${filename}`,
  alt,
  width: 1600,
  height: 1000,
});

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

export const solutionPages: Record<string, SolutionPageContent> = {
  "coding-marking": {
    slug: "coding-marking",
    displayName: "Coding & Marking",
    categoryLabel: "INDUSTRIAL SOLUTION",
    tagline: "Reliable marking systems aligned with KSA production demands",
    shortDescription:
      "Industrial coding and marking for products, packaging and production lines — from continuous inkjet to large-character systems.",
    longDescription:
      "Printechs delivers coding and marking solutions for manufacturers across Saudi Arabia. Whether you need high-speed CIJ printing on bottling lines, large-character marking on cartons, or traceability codes for compliance — we supply, integrate, and support the full stack.\n\nSelect a technology category below to explore compatible products, or contact Printechs for line assessment and specification support.",
    heroImage: solutionImage(
      "featured-production-coding-marking.jpg",
      "Industrial coding and marking system on a production line",
    ),
    heroTrustChips: [
      "KSA production expertise",
      "Hitachi & REA JET partner",
      "Printechs Saudi Arabia",
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
        title: "Multiple technologies",
        description:
          "CIJ, large-character and integrated marking — matched to your substrate and line speed.",
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
          id: "dates",
          label: "Production dates",
          image: industryImage(
            "industry-dairy.jpg",
            "Date coding on dairy production line",
          ),
          caption: "High-contrast date and time codes on fast-moving lines.",
        },
        {
          id: "batch",
          label: "Batch & lot codes",
          image: industryImage(
            "industry-packaging.jpg",
            "Batch coding on packaging line",
          ),
          caption: "Lot traceability on cartons, pouches and secondary packaging.",
        },
        {
          id: "barcode",
          label: "Barcodes & Data Matrix",
          image: industryImage(
            "industry-food-beverage.jpg",
            "Barcode marking on beverage packaging",
          ),
          caption: "1D and 2D codes for supply chain visibility.",
        },
      ],
    },
    storyHeading: "Built for Saudi manufacturing lines",
    productCategories: [
      {
        slug: "continuous-inkjet",
        title: "Continuous Inkjet (CIJ)",
        shortTitle: "CIJ Printers",
        description:
          "Non-contact inkjet printing for high-speed lines — ideal for bottles, cans, pouches and flexible film.",
        image: productImage("Hitachi UX-D161W"),
        productSlugs: ["hitachi-ux-d161", "hitachi-ux-d160"],
      },
      {
        slug: "large-character",
        title: "Large Character & Case Coding",
        shortTitle: "REA JET Systems",
        description:
          "High-resolution and large-character coding for cartons, cases, pallets and industrial packaging.",
        image: productImage("REA JET"),
        productSlugs: ["rea-jet-coding-systems"],
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
        "Industrial coding and marking solutions from Printechs — CIJ, large-character and production line marking.",
      canonicalPath: "/solutions/coding-marking",
    },
    canonicalPath: "/solutions/coding-marking",
  },
};

export function getSolutionPage(slug: string): SolutionPageContent | undefined {
  return solutionPages[slug];
}
