"use client";

import Image from "next/image";
import { useMemo, useState } from "react";
import { ImageLightbox, type LightboxSlide } from "@/components/media/ImageLightbox";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { Button } from "@/components/ui/Button";
import type { ProductTour, ProductTourSection } from "@/types/content";

type ProductTourSectionsProps = {
  tour: ProductTour;
  demoHref: string;
  quoteHref: string;
  productName?: string;
};

function ScreenshotPlaceholder() {
  return (
    <div className="flex aspect-[16/10] w-full items-center justify-center rounded-md border border-line bg-mist px-6 text-center">
      <p className="text-sm font-medium text-slate">Screenshot coming soon</p>
    </div>
  );
}

function resolveImageSrc(section: ProductTourSection): string | null {
  const src = section.image?.src;
  if (!src) return null;
  return src;
}

type TourScreenshotProps = {
  section: ProductTourSection;
  priority?: boolean;
  onOpenLightbox: () => void;
  onImageError: (sectionId: string) => void;
};

function TourScreenshot({
  section,
  priority = false,
  onOpenLightbox,
  onImageError,
}: TourScreenshotProps) {
  const [failed, setFailed] = useState(false);
  const src = resolveImageSrc(section);

  if (!src || failed) {
    return <ScreenshotPlaceholder />;
  }

  return (
    <button
      type="button"
      onClick={onOpenLightbox}
      className="group relative block w-full overflow-hidden rounded-md border border-line bg-white text-left shadow-soft transition duration-300 hover:border-line-strong focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2"
      aria-label={`View larger ${section.title} screenshot`}
    >
      <div className="relative aspect-[16/10] w-full bg-mist">
        <Image
          src={src}
          alt={section.image?.alt || section.title}
          fill
          priority={priority}
          loading={priority ? undefined : "lazy"}
          className="object-contain object-center p-3 transition duration-300 group-hover:scale-[1.01] motion-reduce:transition-none motion-reduce:group-hover:scale-100"
          sizes="(max-width: 1024px) 100vw, 44rem"
          onError={() => {
            setFailed(true);
            onImageError(section.id);
          }}
        />
      </div>
    </button>
  );
}

function TourSectionBlock({
  section,
  index,
  onOpenLightbox,
  onImageError,
}: {
  section: ProductTourSection;
  index: number;
  onOpenLightbox: () => void;
  onImageError: (sectionId: string) => void;
}) {
  const imageOnRight = index % 2 === 1;

  return (
    <article className="grid items-center gap-8 lg:grid-cols-2 lg:gap-12">
      <div className={imageOnRight ? "lg:order-2" : ""}>
        <TourScreenshot
          section={section}
          priority={index === 0}
          onOpenLightbox={onOpenLightbox}
          onImageError={onImageError}
        />
      </div>
      <div className={imageOnRight ? "lg:order-1" : ""}>
        <ProductSectionHeader eyebrow={section.eyebrow} title={section.title} />
        <p className="mt-5 max-w-xl text-base leading-relaxed text-slate">{section.description}</p>
        {section.features.length ? (
          <ul className="mt-5 max-w-xl space-y-2.5">
            {section.features.map((feature) => (
              <li key={feature} className="flex gap-2.5 text-base leading-relaxed text-slate">
                <span
                  className="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-signal"
                  aria-hidden="true"
                />
                <span>{feature}</span>
              </li>
            ))}
          </ul>
        ) : null}
      </div>
    </article>
  );
}

export function ProductTourSections({
  tour,
  demoHref,
  quoteHref,
  productName,
}: ProductTourSectionsProps) {
  const [lightboxOpen, setLightboxOpen] = useState(false);
  const [lightboxIndex, setLightboxIndex] = useState(0);
  const [imageFailures, setImageFailures] = useState<Record<string, boolean>>({});

  const lightboxSlides = useMemo<LightboxSlide[]>(
    () =>
      tour.sections
        .filter((section) => !imageFailures[section.id] && resolveImageSrc(section))
        .map((section) => ({
          id: section.id,
          src: resolveImageSrc(section) || "",
          alt: section.image?.alt || section.title,
          title: section.title,
        })),
    [imageFailures, tour.sections],
  );

  const openLightbox = (sectionId: string) => {
    if (imageFailures[sectionId]) return;
    const index = lightboxSlides.findIndex((slide) => slide.id === sectionId);
    if (index < 0) return;
    setLightboxIndex(index);
    setLightboxOpen(true);
  };

  return (
    <div>
      <ProductSectionHeader
        eyebrow="Product tour"
        title={tour.heading}
        description={tour.subheading}
      />

      <div className="mt-10 space-y-12 lg:space-y-16">
        {tour.sections.map((section, index) => (
          <TourSectionBlock
            key={section.id}
            section={section}
            index={index}
            onOpenLightbox={() => openLightbox(section.id)}
            onImageError={(sectionId) =>
              setImageFailures((current) => ({ ...current, [sectionId]: true }))
            }
          />
        ))}
      </div>

      <div className="mt-12 rounded-sm border border-line bg-mist/50 px-5 py-6 sm:px-6">
        <p className="text-base font-semibold text-ink">
          Want to see {productName ?? "this product"} with your workflow?
        </p>
        <div className="mt-4 flex flex-wrap gap-3">
          <Button href={demoHref} variant="primary">
            Book a Demo
          </Button>
          <Button href={quoteHref} variant="ghost">
            Request a Quote
          </Button>
        </div>
      </div>

      {lightboxOpen && lightboxSlides.length > 0 ? (
        <ImageLightbox
          slides={lightboxSlides}
          activeIndex={lightboxIndex}
          onClose={() => setLightboxOpen(false)}
          onNavigate={setLightboxIndex}
        />
      ) : null}
    </div>
  );
}
