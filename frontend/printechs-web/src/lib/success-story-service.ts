import { cache } from "react";
import type { SuccessStory, SuccessStoryList } from "@/types/content";
import { erpnextMethod, normalizeMediaAsset } from "@/lib/erpnext-client";

function normalizeStory(story: SuccessStory): SuccessStory {
  return {
    ...story,
    image: normalizeMediaAsset(story.image),
    gallery: story.gallery?.map(normalizeMediaAsset),
    videos: story.videos?.map((video) => ({
      ...video,
      poster: video.poster
        ? (normalizeMediaAsset({ src: video.poster, alt: video.title }).src ?? video.poster)
        : video.poster,
    })),
    related: story.related?.map(normalizeStory),
  };
}

export const fetchSuccessStories = cache(async (filters: {
  product?: string;
  brand?: string;
  industry?: string;
} = {}): Promise<SuccessStoryList> => {
  const fromErp = await erpnextMethod<SuccessStoryList>(
    "printechs_digital.api.website.list_success_stories",
    {
      product: filters.product,
      brand: filters.brand,
      industry: filters.industry,
      limit: 50,
    },
  );

  if (!fromErp) {
    return { stories: [], brands: [], industries: [] };
  }

  return {
    stories: (fromErp.stories ?? []).map(normalizeStory),
    brands: fromErp.brands ?? [],
    industries: fromErp.industries ?? [],
  };
});

export async function fetchSuccessStory(slug: string): Promise<SuccessStory | undefined> {
  const fromErp = await erpnextMethod<SuccessStory>(
    "printechs_digital.api.website.get_success_story",
    { slug },
  );

  if (!fromErp?.slug) {
    return undefined;
  }

  return normalizeStory(fromErp);
}

export const fetchFeaturedSuccessStories = cache(async (limit = 2): Promise<SuccessStory[]> => {
  const fromErp = await erpnextMethod<SuccessStory[]>(
    "printechs_digital.api.website.get_featured_success_stories",
    { limit },
  );

  return (fromErp ?? []).map(normalizeStory);
});

export async function fetchSuccessStorySlugs(): Promise<string[]> {
  return (
    (await erpnextMethod<string[]>("printechs_digital.api.website.get_success_story_slugs")) ?? []
  );
}
