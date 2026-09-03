import type {
  BusinessDivision,
  HomepageContent,
  HomepageExtraBlock,
  HeroContent,
  Video,
} from "@/types/content";
import { erpnextMethod, normalizeMediaAsset, resolvePublicAssetUrl } from "@/lib/erpnext-client";

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

export async function fetchHomepage(): Promise<HomepageContent | null> {
  const fromErp = await erpnextMethod<HomepageContent | null>(
    "printechs_digital.api.website.get_homepage",
  );

  if (!fromErp?.hero?.headline) {
    return null;
  }

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
