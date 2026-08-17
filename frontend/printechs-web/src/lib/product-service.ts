import type { Brand, Industry, ProductPageContent } from "@/types/content";
import { getProductPage } from "@/data/product-pages";
import { getBrandBySlug } from "@/data/brands";
import { industries } from "@/data/industries";

export type ResolvedProductPage = {
  page: ProductPageContent;
  brand?: Brand;
  linkedIndustries: Industry[];
};

/**
 * Product page resolver — swap mock loader for ERPNext API without changing UI.
 */
export function resolveProductPage(slug: string): ResolvedProductPage | undefined {
  const page = getProductPage(slug);
  if (!page) return undefined;

  const brand = page.brandSlug ? getBrandBySlug(page.brandSlug) : undefined;

  const linkedIndustries = (page.industrySlugs ?? [])
    .map((industrySlug) => industries.find((item) => item.slug === industrySlug))
    .filter((item): item is Industry => item !== undefined);

  return { page, brand, linkedIndustries };
}

/** Future: async ERPNext fetch replaces resolveProductPage mock lookup. */
export async function fetchProductPage(
  slug: string,
): Promise<ResolvedProductPage | undefined> {
  return resolveProductPage(slug);
}
