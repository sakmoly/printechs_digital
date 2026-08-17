import Link from "next/link";
import type { Industry } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { Button } from "@/components/ui/Button";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function IndustriesSection({ items }: { items: Industry[] }) {
  return (
    <Section tone="white">
      <div className="mb-10 flex flex-col gap-6 md:mb-12 md:flex-row md:items-end md:justify-between">
        <Heading
          eyebrow="Industries"
          title="Industries we serve"
          description="From dairy and packaging to retail and logistics — technology mapped to the realities of each sector."
          className="mb-0"
        />
        <Button href="/industries" variant="ghost" className="shrink-0">
          View all industries
        </Button>
      </div>

      <ul className="grid grid-cols-2 gap-3 sm:gap-4 lg:grid-cols-4">
        {items.map((item) => (
          <li key={item.id}>
            <Link
              href={`/industries/${item.slug}`}
              className="group block rounded-sm bg-mist focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              <ImageFrame
                src={item.image.src}
                alt={item.image.alt}
                spec={IMAGE_SPECS.industry}
                fill
                className="aspect-[3/2] rounded-sm"
                imageClassName="media-zoom object-cover"
                sizes="(max-width: 1024px) 50vw, 25vw"
                overlay={
                  <>
                    <div className="absolute inset-0 bg-gradient-to-t from-ink/75 via-ink/20 to-transparent" />
                    <span className="absolute inset-x-0 bottom-0 p-4 font-display text-base font-semibold text-paper sm:text-lg">
                      {item.name}
                    </span>
                  </>
                }
              />
            </Link>
          </li>
        ))}
      </ul>
    </Section>
  );
}
