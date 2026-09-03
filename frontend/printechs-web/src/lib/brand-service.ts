import type { Brand } from "@/types/content";
import { brands, getBrandBySlug } from "@/data/brands";
import { erpnextMethod, normalizeMediaAsset } from "@/lib/erpnext-client";

export function normalizeWebsiteBrand(brand: Brand): Brand {
  return {
    ...brand,
    logo: normalizeMediaAsset(brand.logo),
  };
}

export async function fetchBrands(): Promise<Brand[]> {
  const fromErp =
    (await erpnextMethod<Brand[]>("printechs_digital.api.website.list_brands", {
      limit: 50,
    })) ?? [];

  if (fromErp.length) {
    return fromErp.map(normalizeWebsiteBrand);
  }

  return brands;
}

export async function fetchBrand(slug: string): Promise<Brand | undefined> {
  const fromErp = await erpnextMethod<Brand>("printechs_digital.api.website.get_brand", {
    slug,
  });

  if (fromErp?.slug) {
    return normalizeWebsiteBrand(fromErp);
  }

  return getBrandBySlug(slug);
}

export async function fetchBrandSlugs(): Promise<string[]> {
  const slugs =
    (await erpnextMethod<string[]>("printechs_digital.api.website.get_brand_slugs")) ?? [];
  const mockSlugs = brands.map((brand) => brand.slug);
  return Array.from(new Set([...slugs, ...mockSlugs]));
}
