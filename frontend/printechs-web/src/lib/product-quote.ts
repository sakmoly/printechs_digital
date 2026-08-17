import type { ProductPageContent } from "@/types/content";

/** Build Request Quote URL with product context (Phase F3). */
export function buildProductQuoteUrl(page: ProductPageContent): string {
  const params = new URLSearchParams({
    product: page.displayName,
    brand: page.brand,
    category: page.category,
    url: page.canonicalPath,
  });

  if (page.itemCode) {
    params.set("code", page.itemCode);
  }

  return `/request-quote?${params.toString()}`;
}

export function buildProductDemoUrl(page: ProductPageContent): string {
  const params = new URLSearchParams({
    product: page.displayName,
    url: page.canonicalPath,
  });

  return `/request-demo?${params.toString()}`;
}
