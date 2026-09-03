import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";
import { fetchSolutions } from "@/lib/solution-service";

export const revalidate = 60;

export const metadata = buildMetadata({
  title: "Solutions | Printechs",
  description: "Solution areas spanning industrial, retail and software.",
  canonicalPath: "/solutions",
});

export default async function SolutionsPage() {
  const solutions = await fetchSolutions();

  return (
    <>
      <PageIntro
        title="Solutions"
        description="Industrial coding, retail technology and enterprise software — organised by the operational outcome you need."
        crumbs={[{ label: "Home", href: "/" }, { label: "Solutions" }]}
      />
      <Section tone="white">
        <FeatureGrid columns={3}>
          {solutions.map((item) => (
            <Card
              key={item.id}
              href={item.href || `/solutions/${item.slug}`}
              title={item.name}
              description={item.summary}
              cta="Explore solution"
              ctaArrow
              media={
                <ImageFrame
                  src={item.image.src}
                  alt={item.image.alt}
                  spec={IMAGE_SPECS.solution}
                  fill
                  className="aspect-[16/10]"
                  imageClassName="media-zoom-subtle object-cover"
                  sizes="(max-width: 1024px) 100vw, 33vw"
                />
              }
            />
          ))}
        </FeatureGrid>
      </Section>
    </>
  );
}
