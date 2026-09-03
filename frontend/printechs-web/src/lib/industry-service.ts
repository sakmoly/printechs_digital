import type { Industry } from "@/types/content";
import { industries as mockIndustries } from "@/data/industries";
import { erpnextMethod, normalizeMediaAsset } from "@/lib/erpnext-client";

function normalizeIndustry(industry: Industry): Industry {
  return {
    ...industry,
    image: normalizeMediaAsset(industry.image),
  };
}

export async function fetchIndustries(options: { home?: boolean; limit?: number } = {}): Promise<Industry[]> {
  const fromErp =
    (await erpnextMethod<Industry[]>("printechs_digital.api.website.list_industries", {
      home: options.home ? 1 : 0,
      limit: options.limit ?? 50,
    })) ?? [];

  if (fromErp.length) {
    return fromErp.map(normalizeIndustry);
  }

  return options.home ? mockIndustries.slice(0, options.limit ?? 12) : mockIndustries;
}

export async function fetchIndustry(slug: string): Promise<Industry | undefined> {
  const fromErp = await erpnextMethod<Industry>("printechs_digital.api.website.get_industry", {
    slug,
  });

  if (fromErp?.slug) {
    return normalizeIndustry(fromErp);
  }

  return mockIndustries.find((item) => item.slug === slug);
}

export async function fetchIndustrySlugs(): Promise<string[]> {
  const fromErp = await erpnextMethod<string[]>("printechs_digital.api.website.get_industry_slugs");
  if (fromErp?.length) {
    return fromErp;
  }
  return mockIndustries.map((item) => item.slug);
}
