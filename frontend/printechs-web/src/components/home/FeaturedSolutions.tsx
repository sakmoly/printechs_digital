import type { FeaturedSolution, HomepageSectionHeading } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function FeaturedSolutions({
  items,
  heading,
}: {
  items: FeaturedSolution[];
  heading?: HomepageSectionHeading | null;
}) {
  if (!items.length) return null;

  return (
    <Section tone="muted">
      <Heading
        eyebrow={heading?.eyebrow ?? "Featured solutions"}
        title={heading?.title ?? "Technology built for real operations"}
        description={
          heading?.description ??
          "From production floors to retail stores and enterprise systems, our solutions help businesses improve accuracy, visibility and operational control."
        }
      />
      <FeatureGrid columns={4}>
        {items.map((item) => (
          <Card
            key={item.id}
            href={item.href}
            title={item.title}
            description={item.description}
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
                sizes="(max-width: 768px) 100vw, 25vw"
              />
            }
          />
        ))}
      </FeatureGrid>
    </Section>
  );
}
