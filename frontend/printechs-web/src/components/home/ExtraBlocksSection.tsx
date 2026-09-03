import Link from "next/link";
import type { HomepageExtraBlock } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

export function ExtraBlocksSection({ blocks }: { blocks: HomepageExtraBlock[] }) {
  if (!blocks.length) return null;

  return (
    <>
      {blocks.map((block, index) => (
        <Section key={block.id} tone={index % 2 === 0 ? "white" : "muted"}>
          <div className={block.image ? "grid gap-8 lg:grid-cols-2 lg:items-center" : "max-w-3xl"}>
            <div>
              <h2 className="font-display text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
                {block.heading}
              </h2>
              <p className="mt-4 whitespace-pre-line text-base leading-relaxed text-slate sm:text-lg">
                {block.body}
              </p>
              {block.linkHref && block.linkLabel ? (
                <Link
                  href={block.linkHref}
                  className="mt-6 inline-flex text-sm font-semibold text-signal-deep underline-offset-4 transition hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
                >
                  {block.linkLabel}
                </Link>
              ) : null}
            </div>
            {block.image ? (
              <ImageFrame
                src={block.image.src}
                alt={block.image.alt}
                spec={IMAGE_SPECS.caseStudy}
                fill
                className="aspect-[16/9]"
                imageClassName="object-cover"
                sizes="(max-width: 1024px) 100vw, 50vw"
              />
            ) : null}
          </div>
        </Section>
      ))}
    </>
  );
}
