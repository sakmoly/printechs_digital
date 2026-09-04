import { HomeHero } from "@/components/hero/HomeHero";
import { DivisionsSection } from "@/components/home/DivisionsSection";
import { FeaturedSolutions } from "@/components/home/FeaturedSolutions";
import { FeaturedProducts } from "@/components/home/FeaturedProducts";
import { SoftwareSection } from "@/components/home/SoftwareSection";
import { IndustriesSection } from "@/components/home/IndustriesSection";
import { WhyPrintechs } from "@/components/home/WhyPrintechs";
import { CaseStudiesSection } from "@/components/home/CaseStudiesSection";
import { ExtraBlocksSection } from "@/components/home/ExtraBlocksSection";
import { HomeCTA } from "@/components/home/HomeCTA";
import { LazyBrandsSection, LazyVideoSection } from "@/components/home/LazyHomeSections";
import { homeHero, videos } from "@/data";
import { fetchHomepageBundle, getHomepageDivisions } from "@/lib/home-service";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

export default async function HomePage() {
  const bundle = await fetchHomepageBundle();

  const homepage = bundle.homepage;
  const hero = homepage?.hero ?? homeHero;
  const why = homepage ? homepage.why : undefined;
  const video = homepage ? homepage.video : videos[0];
  const storiesHeading = homepage ? homepage.stories : undefined;
  const cta = homepage ? homepage.cta : undefined;
  const divisionsHeading = homepage ? homepage.divisions : undefined;
  const featuredHeading = homepage ? homepage.featuredSolutions : undefined;
  const industriesHeading = homepage ? homepage.industries : undefined;
  const extraBlocks = homepage?.extraBlocks ?? [];
  const divisions = getHomepageDivisions(homepage);

  return (
    <>
      <HomeHero content={hero} />
      <DivisionsSection divisions={divisions} heading={divisionsHeading} />
      <FeaturedSolutions items={bundle.featuredSolutions} heading={featuredHeading} />
      <FeaturedProducts items={bundle.featuredProducts} />
      <SoftwareSection items={bundle.featuredSoftware} />
      <IndustriesSection items={bundle.industries} heading={industriesHeading} />
      {why !== null ? <WhyPrintechs content={why} /> : null}
      {video ? (
        <LazyVideoSection video={video} eyebrow={video.eyebrow} />
      ) : null}
      <LazyBrandsSection brands={bundle.brands} />
      {bundle.successStories.length ? (
        <CaseStudiesSection items={bundle.successStories} heading={storiesHeading} />
      ) : null}
      <ExtraBlocksSection blocks={extraBlocks} />
      {cta !== null ? <HomeCTA content={cta} /> : null}
    </>
  );
}
