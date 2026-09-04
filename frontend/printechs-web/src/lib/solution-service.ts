import { cache } from "react";
import type { FeaturedSolution, Industry, Product, Solution, SolutionPageContent } from "@/types/content";
import { getSolutionPage } from "@/data/solution-pages";
import { getProductBySlug } from "@/data/products";
import { featuredSolutions as mockFeaturedSolutions } from "@/data/featured-solutions";
import { industries } from "@/data/industries";
import { solutions as mockSolutions } from "@/data/solutions";
import { erpnextMethod, normalizeMediaAsset } from "@/lib/erpnext-client";

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

function normalizeSolution(solution: Solution): Solution {
  return {
    ...solution,
    image: normalizeMediaAsset(solution.image),
  };
}

function normalizeFeatured(item: FeaturedSolution): FeaturedSolution {
  return {
    ...item,
    image: normalizeMediaAsset(item.image),
  };
}

export const fetchSolutions = cache(async (): Promise<Solution[]> => {
  const fromErp =
    (await erpnextMethod<Solution[]>("printechs_digital.api.website.list_solutions", {
      limit: 50,
    })) ?? [];

  if (fromErp.length) {
    return fromErp.map(normalizeSolution);
  }

  return mockSolutions;
});

export const fetchFeaturedSolutions = cache(async (limit = 4): Promise<FeaturedSolution[]> => {
  const fromErp =
    (await erpnextMethod<FeaturedSolution[]>("printechs_digital.api.website.get_featured_solutions", {
      limit,
    })) ?? [];

  if (fromErp.length) {
    return fromErp.slice(0, limit).map(normalizeFeatured);
  }

  return mockFeaturedSolutions.slice(0, limit);
});

export async function fetchSolution(slug: string): Promise<Solution | undefined> {
  const fromErp = await erpnextMethod<Solution>("printechs_digital.api.website.get_solution", {
    slug,
  });

  if (fromErp?.slug) {
    return normalizeSolution(fromErp);
  }

  return mockSolutions.find((item) => item.slug === slug);
}

export async function fetchSolutionSlugs(): Promise<string[]> {
  const fromErp = await erpnextMethod<string[]>("printechs_digital.api.website.get_solution_slugs");
  if (fromErp?.length) {
    return fromErp;
  }
  return mockSolutions.map((item) => item.slug);
}
