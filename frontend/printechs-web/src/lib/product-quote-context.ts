import { getProductBySlug, products } from "@/data/products";
import { getAllProductPageSlugs } from "@/data/product-pages";
import { fetchProductPage, resolveProductPage } from "@/lib/product-service";
import { fetchPublishedProductSlugs } from "@/lib/catalog-service";
import type { LeadContext } from "@/types/lead";
import type { ProductPageContent } from "@/types/content";

export type ProductQuoteContext = {
  slug: string;
  displayName: string;
  brand: string;
  category: string;
  sourceUrl: string;
  leadContext: LeadContext;
  page?: ProductPageContent;
};

function buildQuoteContextFromPage(
  slug: string,
  page: ProductPageContent,
): ProductQuoteContext {
  return {
    slug,
    displayName: page.displayName,
    brand: page.brand,
    category: page.category,
    sourceUrl: page.canonicalPath,
    page,
    leadContext: {
      productSlug: slug,
      product: page.displayName,
      code: page.itemCode,
      brand: page.brand,
      category: page.category,
      sourceUrl: page.canonicalPath,
    },
  };
}

export async function fetchProductQuoteContext(
  slug: string,
): Promise<ProductQuoteContext | undefined> {
  const resolved = await fetchProductPage(slug);
  if (resolved) {
    return buildQuoteContextFromPage(slug, resolved.page);
  }

  const product = getProductBySlug(slug);
  if (!product) return undefined;

  const displayName =
    product.name === product.brand || product.brand.includes("/")
      ? product.name
      : `${product.brand} ${product.name}`.trim();

  const sourceUrl = product.seo.canonicalPath;

  return {
    slug,
    displayName,
    brand: product.brand,
    category: product.category,
    sourceUrl,
    leadContext: {
      productSlug: slug,
      product: displayName,
      brand: product.brand,
      category: product.category,
      sourceUrl,
    },
  };
}

export function getProductQuoteContext(slug: string): ProductQuoteContext | undefined {
  const resolved = resolveProductPage(slug);
  if (resolved) {
    return buildQuoteContextFromPage(slug, resolved.page);
  }

  const product = getProductBySlug(slug);
  if (!product) return undefined;

  const displayName =
    product.name === product.brand || product.brand.includes("/")
      ? product.name
      : `${product.brand} ${product.name}`.trim();

  const sourceUrl = product.seo.canonicalPath;

  return {
    slug,
    displayName,
    brand: product.brand,
    category: product.category,
    sourceUrl,
    leadContext: {
      productSlug: slug,
      product: displayName,
      brand: product.brand,
      category: product.category,
      sourceUrl,
    },
  };
}

export async function productSupportsDemoAsync(slug: string): Promise<boolean> {
  const resolved = await fetchProductPage(slug);
  if (resolved) {
    const { page } = resolved;
    return page.productType === "software" || page.showDemoCta === true;
  }
  return false;
}

export function productSupportsDemo(slug: string): boolean {
  const resolved = resolveProductPage(slug);
  if (resolved) {
    const { page } = resolved;
    return page.productType === "software" || page.showDemoCta === true;
  }
  return false;
}

export function buildProductQuotePath(slug: string): string {
  return `/products/${slug}/quote`;
}

export function buildProductDemoPath(slug: string): string {
  return `/products/${slug}/demo`;
}

export function buildSolutionQuotePath(slug: string): string {
  return `/solutions/${slug}/quote`;
}

export function getAllProductSlugs(): string[] {
  return Array.from(
    new Set([...products.map((product) => product.slug), ...getAllProductPageSlugs()]),
  );
}

export async function getAllProductSlugsAsync(): Promise<string[]> {
  return fetchPublishedProductSlugs();
}

export function getDemoProductSlugs(): string[] {
  return getAllProductSlugs().filter((slug) => productSupportsDemo(slug));
}

export async function getDemoProductSlugsAsync(): Promise<string[]> {
  const slugs = await getAllProductSlugsAsync();
  const checks = await Promise.all(
    slugs.map(async (slug) => ((await productSupportsDemoAsync(slug)) ? slug : null)),
  );
  return checks.filter((slug): slug is string => slug !== null);
}
