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
import { HomeCTA } from "@/components/home/HomeCTA";
import {
  homeHero,
  businessDivisions,
  featuredSolutions,
  getFeaturedProducts,
  getFeaturedSoftware,
  getFeaturedIndustries,
  brands,
  caseStudies,
  videos,
} from "@/data";

export default function HomePage() {
  return (
    <>
      <HomeHero content={homeHero} />
      <DivisionsSection divisions={businessDivisions} />
      <FeaturedSolutions items={featuredSolutions} />
      <FeaturedProducts items={getFeaturedProducts(4)} />
      <SoftwareSection items={getFeaturedSoftware(6)} />
      <IndustriesSection items={getFeaturedIndustries(12)} />
      <WhyPrintechs />
      <VideoSection video={videos[0]} />
      <BrandsSection brands={brands} />
      <CaseStudiesSection items={caseStudies} />
      <HomeCTA />
    </>
  );
}
