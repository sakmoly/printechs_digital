import Link from "next/link";
import type { BusinessDivision } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function DivisionsSection({
  divisions,
}: {
  divisions: BusinessDivision[];
}) {
  return (
    <Section tone="white">
      <Heading
        eyebrow="Capabilities"
        title="Three divisions. One technology partner."
        description="Industrial systems, retail technology and enterprise software — each with a clear focus and deep delivery expertise."
      />
      <div className="grid gap-5 lg:grid-cols-3">
        {divisions.map((division) => (
          <article
            key={division.id}
            className="group flex h-full flex-col overflow-hidden rounded-sm bg-paper shadow-soft transition duration-500 ease-premium hover:-translate-y-1 hover:shadow-lift"
          >
            <ImageFrame
              src={division.image.src}
              alt={division.image.alt}
              spec={IMAGE_SPECS.division}
              fill
              className="aspect-[4/3]"
              imageClassName="media-zoom object-cover"
              sizes="(max-width: 1024px) 100vw, 33vw"
              overlay={
                <div className="absolute inset-0 bg-gradient-to-t from-ink/55 via-transparent to-transparent" />
              }
            />
            <div className="flex flex-1 flex-col p-6 sm:p-7">
              <h3 className="font-display text-2xl font-semibold tracking-tight text-ink">
                {division.title}
              </h3>
              <p className="mt-3 text-sm leading-relaxed text-slate">
                {division.summary}
              </p>
              <ul className="mt-5 space-y-2 border-t border-line pt-5 text-sm text-ink/80">
                {division.items.slice(0, 5).map((item) => (
                  <li key={item} className="flex gap-2">
                    <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-signal" />
                    <span>{item}</span>
                  </li>
                ))}
              </ul>
              <Link
                href={division.href}
                className="mt-6 inline-flex text-sm font-semibold text-signal-deep underline-offset-4 transition hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
              >
                Explore {division.title}
              </Link>
            </div>
          </article>
        ))}
      </div>
    </Section>
  );
}
