import { getSolutionPage } from "@/data/solution-pages";
import { solutions } from "@/data/solutions";
import type { LeadContext } from "@/types/lead";

export type SolutionQuoteContext = {
  slug: string;
  displayName: string;
  sourceUrl: string;
  leadContext: LeadContext;
};

export function getSolutionQuoteContext(slug: string): SolutionQuoteContext | undefined {
  const page = getSolutionPage(slug);
  if (!page) return undefined;

  return {
    slug,
    displayName: page.displayName,
    sourceUrl: page.canonicalPath,
    leadContext: {
      solutionSlug: slug,
      product: page.displayName,
      category: page.displayName,
      sourceUrl: page.canonicalPath,
    },
  };
}

export function listSolutionQuoteSlugs(): string[] {
  return solutions
    .map((solution) => solution.slug)
    .filter((slug) => getSolutionPage(slug) !== undefined);
}
