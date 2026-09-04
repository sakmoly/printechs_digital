import type { HomepageStories, SuccessStory } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

const fallbackHeading: HomepageStories = {
  eyebrow: "Case studies",
  title: "Technology deployed where performance matters",
  description: "Selected project stories from industrial and retail environments.",
  limit: 2,
};

export function CaseStudiesSection({
  items,
  heading,
}: {
  items: SuccessStory[];
  heading?: HomepageStories | null;
}) {
  if (!items.length) {
    return null;
  }

  const intro = heading ?? fallbackHeading;

  return (
    <Section tone="muted">
      <Heading
        eyebrow={intro.eyebrow}
        title={intro.title}
        description={intro.description}
      />
      <FeatureGrid columns={2}>
        {items.map((item) => (
          <Card
            key={item.id}
            href={item.href}
            title={item.title}
            description={item.summary}
            meta={item.customer || item.industry}
            cta="Read story"
            media={
              <ImageFrame
                src={item.image.src}
                alt={item.image.alt}
                spec={IMAGE_SPECS.caseStudy}
                fill
                className="aspect-[21/9]"
                imageClassName="media-zoom object-cover"
                sizes="(max-width: 768px) 100vw, 50vw"
              />
            }
          />
        ))}
      </FeatureGrid>
    </Section>
  );
}
