import type { Product } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function FeaturedProducts({ items }: { items: Product[] }) {
  return (
    <Section tone="white">
      <Heading
        eyebrow="Products"
        title="Featured products"
        description="Selected technologies for demanding industrial and retail environments."
      />
      <FeatureGrid columns={4}>
        {items.map((item) => (
          <Card
            key={item.id}
            href={`/products/${item.slug}`}
            title={item.name}
            description={item.summary}
            meta={item.brand}
            cta="View product"
            media={
              <ImageFrame
                src={item.image.src}
                alt={item.image.alt}
                spec={IMAGE_SPECS.product}
                fill
                className="aspect-square bg-mist"
                imageClassName="media-zoom object-cover p-6"
                sizes="(max-width: 768px) 100vw, 25vw"
              />
            }
          />
        ))}
      </FeatureGrid>
    </Section>
  );
}
