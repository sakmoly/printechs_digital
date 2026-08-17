import type { SolutionPageContent } from "@/types/content";

export function buildSolutionQuoteUrl(page: SolutionPageContent): string {
  const params = new URLSearchParams({
    product: page.displayName,
    category: page.displayName,
    url: page.canonicalPath,
  });

  return `/request-quote?${params.toString()}`;
}
