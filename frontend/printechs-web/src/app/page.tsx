import { HomeHero } from "@/components/hero/HomeHero";
import { DivisionsSection } from "@/components/home/DivisionsSection";
import { FeaturedSolutions } from "@/components/home/FeaturedSolutions";
import { FeaturedProducts } from "@/components/home/FeaturedProducts";
import { SoftwareSection } from "@/components/home/SoftwareSection";
import { IndustriesSection } from "@/components/home/IndustriesSection";
import { WhyPrintechs } from "@/components/home/WhyPrintechs";
import { VideoSection } from "@/components/home/VideoSection";
import { BrandsSection } from "@/components/home/BrandsSection";
import { CaseStudiesSection } from "@/components/home/CaseStudiesSection";
import { ExtraBlocksSection } from "@/components/home/ExtraBlocksSection";
import { HomeCTA } from "@/components/home/HomeCTA";
import { homeHero, businessDivisions, videos } from "@/data";
import { fetchFeaturedProducts, fetchFeaturedSoftware } from "@/lib/catalog-service";
import { fetchBrands } from "@/lib/brand-service";
import { fetchHomepage } from "@/lib/home-service";
import { fetchIndustries } from "@/lib/industry-service";
import { fetchFeaturedSolutions } from "@/lib/solution-service";
import { fetchFeaturedSuccessStories } from "@/lib/success-story-service";

export const revalidate = 60;

export default async function HomePage() {
  const [featuredProducts, featuredSoftware, brands, homepage] = await Promise.all([
    fetchFeaturedProducts(4),
    fetchFeaturedSoftware(6),
    fetchBrands(),
    fetchHomepage(),
  ]);

  const hero = homepage?.hero ?? homeHero;
  const why = homepage ? homepage.why : undefined;
  const video = homepage ? homepage.video : videos[0];
  const storiesHeading = homepage ? homepage.stories : undefined;
  const cta = homepage ? homepage.cta : undefined;
  const divisionsHeading = homepage ? homepage.divisions : undefined;
  const featuredHeading = homepage ? homepage.featuredSolutions : undefined;
  const industriesHeading = homepage ? homepage.industries : undefined;
  const extraBlocks = homepage?.extraBlocks ?? [];

  const [successStories, featuredSolutions, homeIndustries] = await Promise.all([
    storiesHeading === null
      ? Promise.resolve([])
      : fetchFeaturedSuccessStories(storiesHeading?.limit ?? 2),
    featuredHeading === null
      ? Promise.resolve([])
      : fetchFeaturedSolutions(featuredHeading?.limit ?? 4),
    industriesHeading === null
      ? Promise.resolve([])
      : fetchIndustries({ home: true, limit: industriesHeading?.limit ?? 12 }),
  ]);

  const divisions =
    divisionsHeading === null
      ? []
      : divisionsHeading?.items?.length
        ? divisionsHeading.items
        : businessDivisions;

  return (
    <>
      <HomeHero content={hero} />
      <DivisionsSection divisions={divisions} heading={divisionsHeading} />
      <FeaturedSolutions items={featuredSolutions} heading={featuredHeading} />
      <FeaturedProducts items={featuredProducts} />
      <SoftwareSection items={featuredSoftware} />
      <IndustriesSection items={homeIndustries} heading={industriesHeading} />
      {why !== null ? <WhyPrintechs content={why} /> : null}
      {video ? <VideoSection video={video} eyebrow={video.eyebrow} /> : null}
      <BrandsSection brands={brands} />
      {successStories.length ? (
        <CaseStudiesSection items={successStories} heading={storiesHeading} />
      ) : null}
      <ExtraBlocksSection blocks={extraBlocks} />
      {cta !== null ? <HomeCTA content={cta} /> : null}
    </>
  );
}
