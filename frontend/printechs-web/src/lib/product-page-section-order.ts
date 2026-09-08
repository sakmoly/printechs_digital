export const DEFAULT_PRODUCT_PAGE_SECTION_ORDER = [
  "benefits",
  "overview",
  "product_tour",
  "icon_specifications",
  "capability_modules",
  "software_capabilities",
  "applications",
  "content_sections",
  "ecosystem",
  "support",
  "downloads",
  "related_products",
  "faqs",
  "key_features",
  "process_steps",
  "localization",
  "reports",
  "dashboard",
] as const;

export type ProductPageSectionKey = (typeof DEFAULT_PRODUCT_PAGE_SECTION_ORDER)[number];

export const PRODUCT_PAGE_SECTION_LABELS: Record<ProductPageSectionKey, string> = {
  benefits: "Benefits",
  overview: "Product Overview",
  product_tour: "Product Tour / Visual Story",
  icon_specifications: "Technical Highlights",
  capability_modules: "Platform Modules",
  software_capabilities: "Software Capabilities",
  applications: "Applications",
  content_sections: "Content Sections",
  ecosystem: "Ecosystem",
  support: "Support & Services",
  downloads: "Downloads & Package",
  related_products: "Related Products",
  faqs: "FAQ",
  key_features: "Key Features",
  process_steps: "Process / Workflow",
  localization: "Localization",
  reports: "Reports",
  dashboard: "Management Dashboard",
};

const SECTION_KEY_SET = new Set<string>(DEFAULT_PRODUCT_PAGE_SECTION_ORDER);

export function resolveProductPageSectionOrder(
  order: string[] | undefined,
): ProductPageSectionKey[] {
  const configured = (order ?? [])
    .filter((key): key is ProductPageSectionKey => SECTION_KEY_SET.has(key));

  if (configured.length) {
    return configured;
  }

  return [...DEFAULT_PRODUCT_PAGE_SECTION_ORDER];
}
