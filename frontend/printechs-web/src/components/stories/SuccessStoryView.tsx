import Link from "next/link";
import type { SuccessStory } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { Container } from "@/components/ui/Container";
import { Breadcrumb } from "@/components/ui/Breadcrumb";
import { ImageFrame } from "@/components/media/ImageFrame";
import { PosterVideo } from "@/components/media/PosterVideo";
import { IMAGE_SPECS } from "@/lib/image-specs";

function storyParagraphs(story: string) {
  return story
    .split(/\n\n+/)
    .map((paragraph) => paragraph.trim())
    .filter(Boolean);
}

export function SuccessStoryView({ story }: { story: SuccessStory }) {
  const paragraphs = storyParagraphs(story.story || story.summary || "");
  const lead = paragraphs[0];
  const rest = paragraphs.slice(1);
  const heroSrc = story.image?.src;
  const gallery = (story.gallery ?? []).filter((image) => image.src !== heroSrc);
  const videos = story.videos ?? [];
  const facts = [
    story.customer ? { label: "Customer", value: story.customer } : null,
    story.location ? { label: "Location", value: story.location } : null,
    story.brand ? { label: "Brand", value: story.brand } : null,
    story.industry ? { label: "Industry", value: story.industry } : null,
    story.productName ? { label: "Product", value: story.productName } : null,
  ].filter((item): item is { label: string; value: string } => Boolean(item));

  return (
    <>
      <article className="border-b border-line bg-white">
        <Container className="py-7 sm:py-9">
          <Breadcrumb
            className="mb-4"
            items={[
              { label: "Home", href: "/" },
              { label: "Success Stories", href: "/success-stories" },
              { label: story.title },
            ]}
          />

          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
            {[story.brand, story.industry].filter(Boolean).join(" · ")}
          </p>
          <h1 className="mt-2 max-w-3xl font-display text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
            {story.title}
          </h1>

          <div className="mt-8 grid items-start gap-10 lg:grid-cols-[minmax(0,1.15fr)_minmax(17rem,0.85fr)] lg:gap-14">
            <div>
              {lead ? (
                <p className="text-lg font-medium leading-relaxed text-ink sm:text-xl sm:leading-relaxed">
                  {lead}
                </p>
              ) : null}
              {rest.length ? (
                <div className="mt-5 max-w-xl space-y-4 text-base leading-relaxed text-slate">
                  {rest.map((paragraph) => (
                    <p key={paragraph.slice(0, 48)}>{paragraph}</p>
                  ))}
                </div>
              ) : null}

              <div className="mt-8 flex flex-wrap gap-3">
                {story.productSlug ? (
                  <Button href={`/products/${story.productSlug}`} variant="primary">
                    View product
                  </Button>
                ) : null}
                {story.brandSlug ? (
                  <Button
                    href={`/success-stories?brand=${story.brandSlug}`}
                    variant="ghost"
                  >
                    More {story.brand} stories
                  </Button>
                ) : (
                  <Button href="/success-stories" variant="ghost">
                    All success stories
                  </Button>
                )}
              </div>
            </div>

            <aside className="space-y-4">
              {videos[0] ? (
                <PosterVideo
                  type={videos[0].type}
                  source={videos[0].source}
                  title={videos[0].title}
                  poster={videos[0].poster || heroSrc}
                  className="overflow-hidden rounded-sm border border-line shadow-soft"
                />
              ) : story.image ? (
                <div className="overflow-hidden rounded-sm border border-line bg-mist shadow-soft">
                  <ImageFrame
                    src={story.image.src}
                    alt={story.image.alt}
                    spec={IMAGE_SPECS.product}
                    fill
                    className="aspect-square"
                    imageClassName="object-contain p-8"
                    sizes="(max-width: 1024px) 100vw, 28rem"
                  />
                </div>
              ) : null}

              {facts.length ? (
                <dl className="rounded-sm border border-line bg-mist/70 px-5 py-4">
                  {facts.map((fact) => (
                    <div
                      key={fact.label}
                      className="flex justify-between gap-4 border-b border-line/70 py-2.5 last:border-b-0 last:pb-0 first:pt-0"
                    >
                      <dt className="text-[0.7rem] font-semibold uppercase tracking-[0.14em] text-slate">
                        {fact.label}
                      </dt>
                      <dd className="text-right text-sm font-semibold text-ink">
                        {fact.value}
                      </dd>
                    </div>
                  ))}
                </dl>
              ) : null}
            </aside>
          </div>
        </Container>
      </article>

      {videos.length > 1 ? (
        <Section tone="muted" pad="compact">
          <h2 className="mb-5 font-display text-2xl font-semibold tracking-tight text-ink">
            Installation videos
          </h2>
          <div className="grid gap-5 lg:grid-cols-2">
            {videos.slice(1).map((video) => (
              <PosterVideo
                key={`${video.type}-${video.source}`}
                type={video.type}
                source={video.source}
                title={video.title}
                poster={video.poster}
                className="overflow-hidden rounded-sm border border-line"
              />
            ))}
          </div>
        </Section>
      ) : null}

      {gallery.length ? (
        <Section tone="muted" pad="compact">
          <h2 className="mb-5 font-display text-2xl font-semibold tracking-tight text-ink">
            From the installation
          </h2>
          <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
            {gallery.map((image) => (
              <ImageFrame
                key={image.src}
                src={image.src}
                alt={image.alt}
                spec={IMAGE_SPECS.caseStudy}
                fill
                className="aspect-[4/3] overflow-hidden rounded-sm border border-line bg-mist"
                imageClassName="object-cover"
                sizes="(max-width: 768px) 100vw, 33vw"
              />
            ))}
          </div>
        </Section>
      ) : null}

      {story.related?.length ? (
        <Section tone="white" pad="compact">
          <div className="mb-6 flex items-end justify-between gap-4">
            <h2 className="font-display text-2xl font-semibold tracking-tight text-ink">
              More success stories
            </h2>
            <Link
              href="/success-stories"
              className="text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
            >
              View all
            </Link>
          </div>
          <FeatureGrid columns={3}>
            {story.related.map((item) => (
              <Card
                key={item.id}
                href={item.href}
                title={item.title}
                description={item.summary}
                meta={[item.brand, item.industry].filter(Boolean).join(" · ")}
                cta="Read story"
                className="border border-line bg-white p-3 shadow-soft"
                media={
                  <ImageFrame
                    src={item.image.src}
                    alt={item.image.alt}
                    spec={IMAGE_SPECS.caseStudy}
                    fill
                    className="aspect-[16/10] bg-mist"
                    imageClassName="object-contain p-4"
                    sizes="(max-width: 768px) 100vw, 33vw"
                  />
                }
              />
            ))}
          </FeatureGrid>
        </Section>
      ) : null}

      <Section tone="ink" pad="compact">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h2 className="font-display text-2xl font-semibold tracking-tight text-paper">
              Planning a similar installation?
            </h2>
            <p className="mt-2 max-w-xl text-base text-paper/70">
              Printechs can specify, install and support the same setup on your
              line.
            </p>
          </div>
          <Button href="/contact" variant="on-dark">
            Talk to a Specialist
          </Button>
        </div>
      </Section>
    </>
  );
}
