import Link from "next/link";
import type { EventAlbum } from "@/types/content";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

function formatEventDate(value?: string) {
  if (!value) return null;
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleDateString("en-GB", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

function FilterChip({
  href,
  label,
  active,
}: {
  href: string;
  label: string;
  active: boolean;
}) {
  return (
    <Link
      href={href}
      className={
        active
          ? "rounded-sm bg-signal px-3 py-1.5 text-sm font-semibold text-white"
          : "rounded-sm border border-line bg-white px-3 py-1.5 text-sm font-semibold text-slate hover:border-line-strong hover:text-ink"
      }
    >
      {label}
    </Link>
  );
}

export function EventsPageView({
  albums,
  eventTypes,
  activeType,
}: {
  albums: EventAlbum[];
  eventTypes: string[];
  activeType?: string;
}) {
  return (
    <>
      <PageIntro
        title="Events & Exhibitions"
        description="Exhibitions, trade shows, team gatherings, and community events from Printechs across Saudi Arabia."
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Company", href: "/company" },
          { label: "Events" },
        ]}
      />

      <Section tone="white" pad="compact">
        {eventTypes.length > 1 ? (
          <div className="mb-8 flex flex-wrap gap-2">
            <FilterChip href="/company/events" label="All events" active={!activeType} />
            {eventTypes.map((type) => (
              <FilterChip
                key={type}
                href={`/company/events?type=${encodeURIComponent(type)}`}
                label={type}
                active={activeType === type}
              />
            ))}
          </div>
        ) : null}

        {albums.length > 0 ? (
          <FeatureGrid columns={3}>
            {albums.map((album) => (
              <Card
                key={album.id}
                href={album.href}
                title={album.title}
                description={album.summary}
                meta={[album.eventType, formatEventDate(album.eventDate), album.location]
                  .filter(Boolean)
                  .join(" · ")}
                cta="View photos"
                media={
                  <ImageFrame
                    src={album.image.src}
                    alt={album.image.alt}
                    spec={IMAGE_SPECS.caseStudy}
                    fill
                    className="aspect-[21/9]"
                    imageClassName="media-zoom object-cover"
                    sizes="(max-width: 768px) 100vw, 33vw"
                  />
                }
              />
            ))}
          </FeatureGrid>
        ) : (
          <div className="rounded-sm border border-line bg-mist p-8">
            <p className="text-base text-slate">
              Event albums will appear here as photos are published from exhibitions,
              Iftar gatherings, and trade shows.
            </p>
          </div>
        )}
      </Section>
    </>
  );
}

export function EventAlbumView({ album }: { album: EventAlbum }) {
  const photos = album.gallery?.length
    ? [album.image, ...album.gallery.filter((photo) => photo.src !== album.image.src)]
    : [album.image];
  const formattedDate = formatEventDate(album.eventDate);

  return (
    <>
      <section className="border-b border-ink/10 bg-mist py-6 sm:py-8">
        <div className="mx-auto max-w-content px-gutter">
          <nav className="mb-3 text-sm text-slate">
            <Link href="/" className="hover:text-ink">
              Home
            </Link>
            <span className="mx-2">/</span>
            <Link href="/company" className="hover:text-ink">
              Company
            </Link>
            <span className="mx-2">/</span>
            <Link href="/company/events" className="hover:text-ink">
              Events
            </Link>
            <span className="mx-2">/</span>
            <span className="text-ink">{album.title}</span>
          </nav>
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
            {album.eventType}
          </p>
          <h1 className="mt-2 font-display text-3xl font-semibold tracking-tight text-ink sm:text-4xl">
            {album.title}
          </h1>
          <p className="mt-2 max-w-2xl text-sm leading-relaxed text-slate sm:text-base">
            {[formattedDate, album.location].filter(Boolean).join(" · ")}
          </p>
          {album.summary ? (
            <p className="mt-3 max-w-3xl text-base leading-relaxed text-slate">{album.summary}</p>
          ) : null}
        </div>
      </section>

      <Section tone="white">
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {photos.map((photo, index) => (
            <figure
              key={`${photo.src}-${index}`}
              className="overflow-hidden rounded-sm border border-line bg-mist"
            >
              <ImageFrame
                src={photo.src}
                alt={photo.alt}
                spec={IMAGE_SPECS.caseStudy}
                fill
                className="aspect-[4/3]"
                imageClassName="object-cover"
                sizes="(max-width: 768px) 100vw, 33vw"
              />
            </figure>
          ))}
        </div>

        {album.description ? (
          <div className="prose prose-slate mt-10 max-w-3xl whitespace-pre-line text-base leading-relaxed">
            {album.description}
          </div>
        ) : null}
      </Section>
    </>
  );
}
