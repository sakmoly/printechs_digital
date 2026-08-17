import type { Industry, Product, SolutionPageContent } from "@/types/content";
import { getSolutionPage } from "@/data/solution-pages";
import { getProductBySlug } from "@/data/products";
import { industries } from "@/data/industries";

export type ResolvedSolutionCategory = {
  category: SolutionPageContent["productCategories"][number];
  products: Product[];
};

export type ResolvedSolutionPage = {
  page: SolutionPageContent;
  categories: ResolvedSolutionCategory[];
  linkedIndustries: Industry[];
};

export function resolveSolutionPage(slug: string): ResolvedSolutionPage | undefined {
  const page = getSolutionPage(slug);
  if (!page) return undefined;

  const categories = page.productCategories.map((category) => ({
    category,
    products: category.productSlugs
      .map((productSlug) => getProductBySlug(productSlug))
      .filter((item): item is Product => item !== undefined),
  }));

  const linkedIndustries = (page.industrySlugs ?? [])
    .map((industrySlug) => industries.find((item) => item.slug === industrySlug))
    .filter((item): item is Industry => item !== undefined);

  return { page, categories, linkedIndustries };
}
