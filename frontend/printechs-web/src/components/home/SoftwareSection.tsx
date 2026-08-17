import Link from "next/link";
import type { SoftwareSolution } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { Button } from "@/components/ui/Button";
import { Container } from "@/components/ui/Container";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function SoftwareSection({ items }: { items: SoftwareSolution[] }) {
  return (
    <Section tone="ink" flush>
      <Container>
        <div className="flex flex-col gap-8 lg:flex-row lg:items-end lg:justify-between">
          <Heading
            eyebrow="Software"
            title="Software solutions that stand on their own"
            description="Modern POS, ERPNext, WMS, loyalty, ZATCA and custom platforms — delivered as a dedicated software practice, not buried under retail hardware."
            tone="light"
            className="mb-0"
          />
          <Button href="/software" variant="secondary" className="shrink-0">
            View all software
          </Button>
        </div>

        <div className="mt-12 grid gap-4 sm:grid-cols-2 xl:grid-cols-3">
          {items.map((item) => (
            <Link
              key={item.id}
              href={`/software/${item.slug}`}
              className="group overflow-hidden rounded-sm border border-paper/10 bg-steel/60 transition duration-300 ease-premium hover:border-signal/50 hover:bg-steel focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              <ImageFrame
                src={item.image.src}
                alt={item.image.alt}
                spec={IMAGE_SPECS.software}
                fill
                className="aspect-[16/10] border-b border-paper/10"
                imageClassName="media-zoom object-cover opacity-90"
                sizes="(max-width: 1280px) 50vw, 33vw"
                overlay={
                  <div className="absolute inset-0 bg-gradient-to-t from-ink/70 via-transparent to-transparent" />
                }
              />
              <div className="p-6">
                <h3 className="font-display text-xl font-semibold text-paper transition group-hover:text-signal-bright">
                  {item.name}
                </h3>
                <p className="mt-3 text-sm leading-relaxed text-paper/68">
                  {item.summary}
                </p>
                <ul className="mt-4 flex flex-wrap gap-2">
                  {item.highlights.slice(0, 3).map((highlight) => (
                    <li
                      key={highlight}
                      className="rounded-sm border border-paper/10 px-2 py-1 text-[0.7rem] uppercase tracking-wide text-paper/60"
                    >
                      {highlight}
                    </li>
                  ))}
                </ul>
              </div>
            </Link>
          ))}
        </div>
      </Container>
    </Section>
  );
}
