import type { Industry } from "@/types/content";

const industryImageFile = (filename: string, alt: string) => ({
  src: `/images/industries/${filename}`,
  alt,
  width: 1200,
  height: 800,
});

export const industries: Industry[] = [
  {
    id: "ind-dairy",
    slug: "dairy",
    name: "Dairy",
    summary: "Coding, traceability and packaging identification for dairy producers.",
    image: industryImageFile(
      "industry-dairy.jpg",
      "Dairy production line with coded milk bottles on a conveyor",
    ),
    relatedProductSlugs: ["hitachi-ux-d161"],
    relatedSoftwareSlugs: ["erpnext", "warehouse-management-system"],
    relatedSolutionSlugs: ["coding-marking", "traceability"],
    seo: {
      title: "Dairy Industry Solutions | Printechs",
      description: "Technology solutions for dairy producers from Printechs.",
      canonicalPath: "/industries/dairy",
    },
  },
  {
    id: "ind-fnb",
    slug: "food-beverage",
    name: "Food & Beverage",
    summary: "Line coding, labelling and retail systems for F&B operations.",
    image: industryImageFile(
      "industry-food-beverage.jpg",
      "Food and beverage production line with coded meal containers and bottles",
    ),
    relatedSolutionSlugs: ["coding-marking", "retail-automation"],
    seo: {
      title: "Food & Beverage Solutions | Printechs",
      description: "Food and beverage technology solutions from Printechs.",
      canonicalPath: "/industries/food-beverage",
    },
  },
  {
    id: "ind-bakery",
    slug: "bakery",
    name: "Bakery",
    summary: "Weighing, coding and store technology for bakery brands.",
    image: industryImageFile(
      "industry-bakery.jpg",
      "Bakery production line with coded bread packaging on a conveyor",
    ),
    seo: {
      title: "Bakery Solutions | Printechs",
      description: "Bakery industry solutions from Printechs.",
      canonicalPath: "/industries/bakery",
    },
  },
  {
    id: "ind-egg",
    slug: "egg-poultry",
    name: "Egg / Poultry",
    summary: "Marking and traceability systems for egg and poultry producers.",
    image: industryImageFile(
      "industry-egg-poultry.jpg",
      "Egg packaging line with traceability coding on cartons and shells",
    ),
    seo: {
      title: "Egg & Poultry Solutions | Printechs",
      description: "Egg and poultry technology solutions from Printechs.",
      canonicalPath: "/industries/egg-poultry",
    },
  },
  {
    id: "ind-pharma",
    slug: "pharmaceutical",
    name: "Pharmaceutical",
    summary: "Compliant coding and identification for pharmaceutical packaging.",
    image: industryImageFile(
      "industry-pharmaceutical.jpg",
      "Pharmaceutical packaging line with batch-coded product boxes",
    ),
    relatedSolutionSlugs: ["coding-marking", "traceability"],
    seo: {
      title: "Pharmaceutical Solutions | Printechs",
      description: "Pharmaceutical coding and traceability with Printechs.",
      canonicalPath: "/industries/pharmaceutical",
    },
  },
  {
    id: "ind-pipe",
    slug: "pipe",
    name: "Pipe",
    summary: "Large character and industrial coding for pipe manufacturers.",
    image: industryImageFile(
      "industry-pipe.jpg",
      "Industrial pipe with batch number and size marking",
    ),
    seo: {
      title: "Pipe Industry Solutions | Printechs",
      description: "Pipe industry coding solutions from Printechs.",
      canonicalPath: "/industries/pipe",
    },
  },
  {
    id: "ind-plastic",
    slug: "plastic",
    name: "Plastic",
    summary: "Durable coding systems for plastic manufacturing environments.",
    image: industryImageFile(
      "industry-plastic.jpg",
      "Plastic bottles on a production line with lot and expiry coding",
    ),
    seo: {
      title: "Plastic Industry Solutions | Printechs",
      description: "Plastic industry technology from Printechs.",
      canonicalPath: "/industries/plastic",
    },
  },
  {
    id: "ind-steel",
    slug: "steel",
    name: "Steel",
    summary: "Rugged identification and marking for steel and metals.",
    image: industryImageFile(
      "industry-steel.jpg",
      "Steel coil with batch number, production date and QR code marking",
    ),
    seo: {
      title: "Steel Industry Solutions | Printechs",
      description: "Steel industry marking solutions from Printechs.",
      canonicalPath: "/industries/steel",
    },
  },
  {
    id: "ind-packaging",
    slug: "packaging",
    name: "Packaging",
    summary: "Coding, inspection readiness and packaging line technology.",
    image: industryImageFile(
      "industry-packaging.jpg",
      "Automated packaging line with cartons and pouches on a conveyor",
    ),
    seo: {
      title: "Packaging Solutions | Printechs",
      description: "Packaging industry solutions from Printechs.",
      canonicalPath: "/industries/packaging",
    },
  },
  {
    id: "ind-retail",
    slug: "retail",
    name: "Retail",
    summary: "Store hardware, POS software and retail automation platforms.",
    image: industryImageFile(
      "industry-retail.jpg",
      "Retail checkout scanning product with lot and expiry traceability data",
    ),
    relatedSoftwareSlugs: ["modern-pos", "printechs-loyalty-management-system"],
    relatedSolutionSlugs: ["retail-automation", "pos-retail-software"],
    seo: {
      title: "Retail Solutions | Printechs",
      description: "Retail technology and software from Printechs.",
      canonicalPath: "/industries/retail",
    },
  },
  {
    id: "ind-fashion",
    slug: "fashion",
    name: "Fashion",
    summary: "Labelling, mobility and store systems for fashion retail.",
    image: industryImageFile(
      "industry-fashion.jpg",
      "Fashion retail checkout with modern POS terminal and store display",
    ),
    seo: {
      title: "Fashion Retail Solutions | Printechs",
      description: "Fashion retail technology from Printechs.",
      canonicalPath: "/industries/fashion",
    },
  },
  {
    id: "ind-warehouse",
    slug: "warehouse-logistics",
    name: "Warehouse & Logistics",
    summary: "Barcode mobility, WMS and automation for distribution centres.",
    image: industryImageFile(
      "industry-warehouse-logistics.jpg",
      "Warehouse logistics with conveyor, forklift and pallet racking",
    ),
    relatedSoftwareSlugs: ["warehouse-management-system"],
    relatedSolutionSlugs: ["warehouse-automation", "barcode-mobility"],
    seo: {
      title: "Warehouse & Logistics Solutions | Printechs",
      description: "Warehouse and logistics technology from Printechs.",
      canonicalPath: "/industries/warehouse-logistics",
    },
  },
];

export function getFeaturedIndustries(limit = 8): Industry[] {
  return industries.slice(0, limit);
}
