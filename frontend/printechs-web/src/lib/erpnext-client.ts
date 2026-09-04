import type { Brand, Product, ProductPageContent } from "@/types/content";
import { getBrandBySlug } from "@/data/brands";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

const DEFAULT_PUBLIC_URL = "https://printechs.com";

function getConfiguredPublicUrl(): string {
  return (
    process.env.NEXT_PUBLIC_ERPNEXT_URL ||
    process.env.ERPNEXT_URL ||
    DEFAULT_PUBLIC_URL
  ).replace(/\/$/, "");
}

/** Public URL for /files assets and absolute links rendered in HTML. */
export function getErpnextBaseUrl(): string {
  return getConfiguredPublicUrl();
}

/** Server-side API base URL. Override with BUILD_ERPNEXT_URL during next build if needed. */
export function getErpnextApiBaseUrl(): string {
  if (process.env.BUILD_ERPNEXT_URL) {
    return process.env.BUILD_ERPNEXT_URL.replace(/\/$/, "");
  }

  return getConfiguredPublicUrl();
}

type FrappeResponse<T> = {
  message?: T;
  exc?: string;
};

export async function erpnextMethod<T>(
  method: string,
  params: Record<string, string | number | undefined> = {},
  revalidate = REVALIDATE_SECONDS,
): Promise<T | null> {
  const url = new URL(`/api/method/${method}`, `${getErpnextApiBaseUrl()}/`);

  Object.entries(params).forEach(([key, value]) => {
    if (value !== undefined && value !== null && value !== "") {
      url.searchParams.set(key, String(value));
    }
  });

  try {
    const response = await fetch(url.toString(), {
      next: { revalidate },
      headers: { Accept: "application/json" },
    });

    if (!response.ok) {
      return null;
    }

    const payload = (await response.json()) as FrappeResponse<T>;
    if (payload.exc || payload.message === undefined) {
      return null;
    }

    return payload.message;
  } catch {
    return null;
  }
}

export function resolvePublicAssetUrl(src?: string | null): string | undefined {
  if (!src) return undefined;
  if (src.startsWith("/images/")) return src;

  const httpsSrc = src.replace(/^http:\/\//i, "https://");
  if (httpsSrc.startsWith("https://")) return httpsSrc;

  const base = getErpnextBaseUrl();
  return `${base}${src.startsWith("/") ? src : `/${src}`}`;
}

export function normalizeMediaAsset<T extends { src: string }>(asset: T): T {
  return {
    ...asset,
    src: resolvePublicAssetUrl(asset.src) ?? asset.src,
  };
}

export function normalizeProductPage(page: ProductPageContent): ProductPageContent {
  return {
    ...page,
    heroImage: normalizeMediaAsset(page.heroImage),
    gallery: page.gallery?.map(normalizeMediaAsset),
    primaryDownload: page.primaryDownload
      ? {
          ...page.primaryDownload,
          href: resolvePublicAssetUrl(page.primaryDownload.href) ?? page.primaryDownload.href,
        }
      : undefined,
    visualStory: page.visualStory
      ? {
          ...page.visualStory,
          items: page.visualStory.items.map((item) => ({
            ...item,
            image: normalizeMediaAsset(item.image),
          })),
        }
      : undefined,
    applicationCards: page.applicationCards?.map((card) => ({
      ...card,
      image: normalizeMediaAsset(card.image),
    })),
    ecosystemItems: page.ecosystemItems?.map((item) => ({
      ...item,
      image: item.image ? normalizeMediaAsset(item.image) : undefined,
    })),
    relatedProducts: page.relatedProducts?.map((item) => ({
      ...item,
      image: item.image ? normalizeMediaAsset(item.image) : undefined,
    })),
    contentSections: page.contentSections?.map((section) => ({
      ...section,
      image: section.image ? normalizeMediaAsset(section.image) : undefined,
    })),
    productTour: page.productTour
      ? {
          ...page.productTour,
          sections: page.productTour.sections.map((section) => ({
            ...section,
            image: section.image ? normalizeMediaAsset(section.image) : undefined,
          })),
        }
      : undefined,
    downloads: page.downloads?.map((item) => ({
      ...item,
      href: resolvePublicAssetUrl(item.href) ?? item.href,
    })),
  };
}

export function normalizeBrand(brand?: Brand | null): Brand | undefined {
  if (!brand) return undefined;

  if (brand.logo?.src && !brand.logo.src.includes("/images/brands/")) {
    return {
      ...brand,
      logo: normalizeMediaAsset(brand.logo),
    };
  }

  const mockBrand = brand.slug ? getBrandBySlug(brand.slug) : undefined;
  if (mockBrand) return mockBrand;

  if (!brand.logo?.src) return undefined;

  return {
    ...brand,
    logo: normalizeMediaAsset(brand.logo),
  };
}

export function normalizeCatalogProduct(product: Product): Product {
  return {
    ...product,
    image: normalizeMediaAsset(product.image),
  };
}
