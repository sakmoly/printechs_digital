import type { HeroContent } from "@/types/content";
import { Container } from "@/components/ui/Container";
import { Button } from "@/components/ui/Button";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { withBasePath } from "@/lib/paths";

const defaultChips = ["Industrial", "Retail", "Software", "Saudi Arabia"];

export function HomeHero({ content }: { content: HeroContent }) {
  const chips = content.chips?.length ? content.chips : defaultChips;
  return (
    <section className="relative isolate overflow-hidden bg-ink text-paper">
      <div className="absolute inset-0">
        {content.media.kind === "image" ? (
          <div className="hero-media-pan absolute inset-0">
            <ImageFrame
              src={content.media.src}
              alt={content.media.alt ?? ""}
              spec={IMAGE_SPECS.hero}
              fill
              priority
              className="h-full w-full"
              imageClassName="object-cover object-[72%_center] sm:object-[68%_center] lg:object-right"
              sizes="100vw"
            />
          </div>
        ) : null}

        {content.media.kind === "hosted-video" ? (
          <video
            className="h-full w-full object-cover"
            autoPlay
            muted
            loop
            playsInline
            poster={
              content.media.poster
                ? withBasePath(content.media.poster)
                : undefined
            }
          >
            <source src={withBasePath(content.media.src)} />
          </video>
        ) : null}

        {/* Darken only the left band so hero photography stays visible on the right */}
        <div className="absolute inset-0 bg-gradient-to-r from-ink/92 via-ink/45 to-transparent" />
        <div className="absolute inset-0 bg-gradient-to-t from-ink/75 via-ink/10 to-transparent" />
      </div>

      <Container className="relative flex min-h-[82vh] flex-col justify-end pb-10 pt-24 sm:min-h-[86vh] sm:pb-12 lg:pb-14 lg:pt-28">
        <div className="max-w-xl animate-fade-up lg:max-w-2xl">
          <p className="mb-5 text-[0.7rem] font-semibold uppercase tracking-[0.22em] text-signal-bright">
            {content.eyebrow || "Printechs"}
          </p>
          <h1 className="font-display text-balance text-4xl font-semibold leading-[1.05] tracking-tight sm:text-5xl lg:text-6xl xl:text-[4.25rem]">
            {content.headline}
          </h1>
          <p className="mt-6 max-w-xl text-base leading-relaxed text-paper/78 sm:text-lg lg:text-xl">
            {content.supportingText}
          </p>
          <div className="mt-9 flex flex-wrap gap-3">
            <Button href={content.primaryCta.href} variant="primary">
              {content.primaryCta.label}
            </Button>
            <Button href={content.secondaryCta.href} variant="secondary">
              {content.secondaryCta.label}
            </Button>
          </div>
        </div>

        {chips.length ? (
          <ul className="mt-10 flex flex-wrap gap-x-8 gap-y-3 border-t border-paper/15 pt-5 text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-paper/65 animate-fade-up animation-delay-150 sm:mt-12">
            {chips.map((item) => (
              <li key={item}>{item}</li>
            ))}
          </ul>
        ) : null}
      </Container>
    </section>
  );
}
