import { cache } from "react";
import type {
  BusinessDivision,
  FeaturedSolution,
  HomepageBundle,
  HomepageContent,
  HomepageExtraBlock,
  HeroContent,
  Industry,
  Product,
  SoftwareSolution,
  SuccessStory,
  Video,
} from "@/types/content";
import { businessDivisions } from "@/data";
import { getFeaturedSoftware, softwareSolutions } from "@/data/software";
import { featuredSolutions as mockFeaturedSolutions } from "@/data/featured-solutions";
import { industries as mockIndustries } from "@/data/industries";
import { getFeaturedProducts } from "@/data/products";
import {
  erpnextMethod,
  normalizeCatalogProduct,
  normalizeMediaAsset,
  resolvePublicAssetUrl,
} from "@/lib/erpnext-client";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

function normalizeHero(hero: HeroContent): HeroContent {
  return {
    ...hero,
    media: {
      ...hero.media,
      src: resolvePublicAssetUrl(hero.media.src) ?? hero.media.src,
      poster: hero.media.poster
        ? resolvePublicAssetUrl(hero.media.poster) ?? hero.media.poster
        : hero.media.poster,
    },
  };
}

function normalizeVideo(video: Video & { eyebrow?: string }): Video & { eyebrow?: string } {
  return {
    ...video,
    video: {
      ...video.video,
      poster: video.video.poster
        ? resolvePublicAssetUrl(video.video.poster) ?? video.video.poster
        : video.video.poster,
      source:
        video.video.type === "hosted"
          ? resolvePublicAssetUrl(video.video.source) ?? video.video.source
          : video.video.source,
    },
  };
}

function normalizeDivision(division: BusinessDivision): BusinessDivision {
  return {
    ...division,
    image: normalizeMediaAsset(division.image),
  };
}

function normalizeExtraBlock(block: HomepageExtraBlock): HomepageExtraBlock {
  return {
    ...block,
    image: block.image ? normalizeMediaAsset(block.image) : block.image,
  };
}

function normalizeHomepage(fromErp: HomepageContent): HomepageContent {
  return {
    hero: normalizeHero(fromErp.hero),
    why: fromErp.why,
    video: fromErp.video ? normalizeVideo(fromErp.video) : null,
    stories: fromErp.stories,
    cta: fromErp.cta,
    divisions: fromErp.divisions
      ? {
          ...fromErp.divisions,
          items: (fromErp.divisions.items ?? []).map(normalizeDivision),
        }
      : fromErp.divisions,
    featuredSolutions: fromErp.featuredSolutions,
    industries: fromErp.industries,
    extraBlocks: (fromErp.extraBlocks ?? []).map(normalizeExtraBlock),
  };
}

function mergeFeaturedProducts(erpProducts: Product[], limit: number): Product[] {
  if (erpProducts.length >= limit) {
    return erpProducts.slice(0, limit).map(normalizeCatalogProduct);
  }

  const erpSlugs = new Set(erpProducts.map((product) => product.slug));
  const mockOnly = getFeaturedProducts(limit).filter((product) => !erpSlugs.has(product.slug));
  return [...erpProducts.map(normalizeCatalogProduct), ...mockOnly].slice(0, limit);
}

function mergeFeaturedSoftware(erpProducts: Product[], limit: number): SoftwareSolution[] {
  const erpAsSoftware: SoftwareSolution[] = erpProducts.map((product) => {
    const mock = softwareSolutions.find((item) => item.slug === product.slug);
    return {
      id: product.id,
      slug: product.slug,
      name: product.name,
      summary: product.summary,
      highlights: mock?.highlights ?? [],
      image: normalizeCatalogProduct(product).image,
      seo: product.seo,
      relatedIndustrySlugs: mock?.relatedIndustrySlugs,
    };
  });

  const erpSlugs = new Set(erpAsSoftware.map((item) => item.slug));
  const mockOnly = getFeaturedSoftware(limit).filter((item) => !erpSlugs.has(item.slug));
  return [...erpAsSoftware, ...mockOnly].slice(0, limit);
}

function mergeFeaturedSolutions(erpSolutions: FeaturedSolution[], limit: number): FeaturedSolution[] {
  if (erpSolutions.length) {
    return erpSolutions.slice(0, limit).map((item) => ({
      ...item,
      image: normalizeMediaAsset(item.image),
    }));
  }
  return mockFeaturedSolutions.slice(0, limit).map((item) => ({
    ...item,
    image: normalizeMediaAsset(item.image),
  }));
}

function mergeHomeIndustries(erpIndustries: Industry[], limit: number): Industry[] {
  if (erpIndustries.length) {
    return erpIndustries.slice(0, limit).map((item) => ({
      ...item,
      image: normalizeMediaAsset(item.image),
    }));
  }
  return mockIndustries.slice(0, limit).map((item) => ({
    ...item,
    image: normalizeMediaAsset(item.image),
  }));
}

function mergeSuccessStories(stories: SuccessStory[]): SuccessStory[] {
  return stories.map((story) => ({
    ...story,
    image: normalizeMediaAsset(story.image),
    gallery: story.gallery?.map(normalizeMediaAsset),
  }));
}

export async function fetchHomepage(): Promise<HomepageContent | null> {
  const fromErp = await erpnextMethod<HomepageContent | null>(
    "printechs_digital.api.website.get_homepage",
  );

  if (!fromErp?.hero?.headline) {
    return null;
  }

  return normalizeHomepage(fromErp);
}

export const fetchHomepageBundle = cache(async (): Promise<HomepageBundle> => {
  type RawHomepageBundle = Omit<HomepageBundle, "featuredSoftware"> & {
    featuredSoftware: Product[];
  };

  const fromErp = await erpnextMethod<RawHomepageBundle>(
    "printechs_digital.api.website.get_homepage_bundle",
    {},
    REVALIDATE_SECONDS,
  );

  const homepage = fromErp?.homepage?.hero?.headline
    ? normalizeHomepage(fromErp.homepage)
    : null;

  const featuredProductsLimit = 4;
  const featuredSoftwareLimit = 6;
  const featuredSolutionsLimit = homepage?.featuredSolutions?.limit ?? 4;
  const industriesLimit = homepage?.industries?.limit ?? 12;
  const storiesLimit = homepage?.stories?.limit ?? 2;

  return {
    homepage,
    featuredProducts: mergeFeaturedProducts(fromErp?.featuredProducts ?? [], featuredProductsLimit),
    featuredSoftware: mergeFeaturedSoftware(fromErp?.featuredSoftware ?? [], featuredSoftwareLimit),
    brands: (fromErp?.brands ?? []).map((brand) => ({
      ...brand,
      logo: normalizeMediaAsset(brand.logo),
    })),
    featuredSolutions:
      homepage?.featuredSolutions === null
        ? []
        : mergeFeaturedSolutions(fromErp?.featuredSolutions ?? [], featuredSolutionsLimit),
    industries:
      homepage?.industries === null
        ? []
        : mergeHomeIndustries(fromErp?.industries ?? [], industriesLimit),
    successStories:
      homepage?.stories === null
        ? []
        : mergeSuccessStories(fromErp?.successStories ?? []).slice(0, storiesLimit),
  };
});

export function getHomepageDivisions(
  homepage: HomepageContent | null,
): BusinessDivision[] {
  const divisionsHeading = homepage?.divisions;
  if (divisionsHeading === null) {
    return [];
  }
  if (divisionsHeading?.items?.length) {
    return divisionsHeading.items;
  }
  return businessDivisions;
}
