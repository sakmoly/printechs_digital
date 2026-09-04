import Link from "next/link";
import type { SoftwareSolution } from "@/types/content";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { Card } from "@/components/ui/Card";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function SoftwarePageView({ items }: { items: SoftwareSolution[] }) {
  return (
    <>
      <PageIntro
        title="Software Solutions"
        description="Modern POS, ERPNext, WMS, ZATCA compliance, loyalty, and custom platforms — delivered as a dedicated software practice."
        crumbs={[{ label: "Home", href: "/" }, { label: "Software" }]}
      />

      <Section tone="white">
        <FeatureGrid columns={3}>
          {items.map((item) => (
            <Card
              key={item.id}
              href={`/software/${item.slug}`}
              title={item.name}
              description={item.summary}
              meta={item.highlights.slice(0, 2).join(" · ")}
              cta="View software"
              media={
                <ImageFrame
                  src={item.image.src}
                  alt={item.image.alt}
                  spec={IMAGE_SPECS.software}
                  fill
                  className="aspect-[16/10]"
                  imageClassName="media-zoom object-cover"
                  sizes="(max-width: 768px) 100vw, 33vw"
                />
              }
            />
          ))}
        </FeatureGrid>

        <p className="mt-10 text-sm text-slate">
          Need integration between POS, ERP, and warehouse systems?{" "}
          <Link
            href="/contact"
            className="font-semibold text-signal-deep underline-offset-4 hover:underline"
          >
            Contact Printechs
          </Link>{" "}
          for deployment planning and support.
        </p>
      </Section>
    </>
  );
}
