import type { Brand, Industry, ProductPageContent } from "@/types/content";
import { getProductPage } from "@/data/product-pages";
import { getBrandBySlug } from "@/data/brands";
import { industries } from "@/data/industries";
import { fetchBrand } from "@/lib/brand-service";
import { fetchSuccessStories } from "@/lib/success-story-service";
import {
  erpnextMethod,
  normalizeBrand,
  normalizeProductPage,
} from "@/lib/erpnext-client";

export type ResolvedProductPage = {
  page: ProductPageContent;
  brand?: Brand;
  linkedIndustries: Industry[];
  successStoriesHref?: string;
};

type ErpResolvedProductPage = {
  page: ProductPageContent;
  brand?: Brand | null;
  linkedIndustries?: Industry[];
  hasSuccessStories?: boolean;
};

function resolveProductPageMock(slug: string): ResolvedProductPage | undefined {
  const page = getProductPage(slug);
  if (!page) return undefined;

  const brand = page.brandSlug ? getBrandBySlug(page.brandSlug) : undefined;

  const linkedIndustries = (page.industrySlugs ?? [])
    .map((industrySlug) => industries.find((item) => item.slug === industrySlug))
    .filter((item): item is Industry => item !== undefined);

  return { page, brand, linkedIndustries };
}

/** @deprecated Use fetchProductPage in server components. */
export function resolveProductPage(slug: string): ResolvedProductPage | undefined {
  return resolveProductPageMock(slug);
}

export async function fetchProductPage(
  slug: string,
): Promise<ResolvedProductPage | undefined> {
  const fromErp = await erpnextMethod<ErpResolvedProductPage>(
    "printechs_digital.api.website.get_product",
    { slug },
  );

  if (fromErp?.page) {
    const page = normalizeProductPage(fromErp.page);
    const brand =
      (page.brandSlug ? await fetchBrand(page.brandSlug) : undefined) ??
      normalizeBrand(fromErp.brand ?? undefined) ??
      (page.brandSlug ? getBrandBySlug(page.brandSlug) : undefined);
    const linkedIndustries =
      fromErp.linkedIndustries ??
      (page.industrySlugs ?? [])
        .map((industrySlug) => industries.find((item) => item.slug === industrySlug))
        .filter((item): item is Industry => item !== undefined);

    return {
      page,
      brand,
      linkedIndustries,
      successStoriesHref: fromErp.hasSuccessStories
        ? `/success-stories?product=${page.slug}`
        : undefined,
    };
  }

  const mock = resolveProductPageMock(slug);
  if (!mock) {
    return undefined;
  }

  const brand = mock.page.brandSlug
    ? (await fetchBrand(mock.page.brandSlug)) ?? mock.brand
    : mock.brand;

  const stories = await fetchSuccessStories({ product: mock.page.slug });

  return {
    ...mock,
    brand,
    successStoriesHref: stories.stories.length
      ? `/success-stories?product=${mock.page.slug}`
      : undefined,
  };
}
