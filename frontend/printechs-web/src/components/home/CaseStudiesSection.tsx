import type { CaseStudy } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function CaseStudiesSection({ items }: { items: CaseStudy[] }) {
  return (
    <Section tone="muted">
      <Heading
        eyebrow="Case studies"
        title="Technology deployed where performance matters"
        description="Selected project stories from industrial and retail environments."
      />
      <FeatureGrid columns={2}>
        {items.map((item) => (
          <Card
            key={item.id}
            href="/resources/case-studies"
            title={item.title}
            description={item.summary}
            meta={item.customer}
            cta="Read case study"
            media={
              <ImageFrame
                src={item.image.src}
                alt={item.image.alt}
                spec={IMAGE_SPECS.caseStudy}
                fill
                className="aspect-video"
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
