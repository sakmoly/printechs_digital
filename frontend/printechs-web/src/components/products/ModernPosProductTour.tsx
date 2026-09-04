"use client";

import Image from "next/image";
import { useMemo, useState } from "react";
import { ImageLightbox, type LightboxSlide } from "@/components/media/ImageLightbox";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { Button } from "@/components/ui/Button";
import {
  MODERN_POS_PRODUCT_TOUR_TABS,
  MODERN_POS_TOUR_HEADING,
  MODERN_POS_TOUR_SUBHEADING,
  type ModernPosTourTab,
} from "@/data/modern-pos-product-tour";
import { withBasePath } from "@/lib/paths";

type ModernPosProductTourProps = {
  demoHref: string;
  quoteHref: string;
};

function ScreenshotPlaceholder() {
  return (
    <div className="flex aspect-[16/10] w-full items-center justify-center rounded-md border border-line bg-mist px-6 text-center">
      <p className="text-sm font-medium text-slate">Modern POS screenshot coming soon</p>
    </div>
  );
}

type TourScreenshotProps = {
  tab: ModernPosTourTab;
  priority?: boolean;
  onOpenLightbox: () => void;
  onImageError: (tabId: string) => void;
};

function TourScreenshot({ tab, priority = false, onOpenLightbox, onImageError }: TourScreenshotProps) {
  const [failed, setFailed] = useState(false);

  if (failed) {
    return <ScreenshotPlaceholder />;
  }

  return (
    <button
      type="button"
      onClick={onOpenLightbox}
      className="group relative block w-full overflow-hidden rounded-md border border-line bg-white text-left shadow-soft transition duration-300 hover:border-line-strong focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2"
      aria-label={`View larger ${tab.title} screenshot`}
    >
      <div className="relative aspect-[16/10] w-full bg-mist">
        <Image
          src={withBasePath(tab.imageSrc)}
          alt={tab.imageAlt}
          fill
          priority={priority}
          loading={priority ? undefined : "lazy"}
          className="object-contain object-center p-3 transition duration-300 group-hover:scale-[1.01] motion-reduce:transition-none motion-reduce:group-hover:scale-100"
          sizes="(max-width: 1024px) 100vw, 44rem"
          onError={() => {
            setFailed(true);
            onImageError(tab.id);
          }}
        />
      </div>
    </button>
  );
}

function TourSection({
  tab,
  index,
  onOpenLightbox,
  onImageError,
}: {
  tab: ModernPosTourTab;
  index: number;
  onOpenLightbox: () => void;
  onImageError: (tabId: string) => void;
}) {
  const imageOnRight = index % 2 === 1;

  return (
    <article className="grid items-center gap-8 lg:grid-cols-2 lg:gap-12">
      <div className={imageOnRight ? "lg:order-2" : ""}>
        <TourScreenshot
          tab={tab}
          priority={index === 0}
          onOpenLightbox={onOpenLightbox}
          onImageError={onImageError}
        />
      </div>
      <div className={imageOnRight ? "lg:order-1" : ""}>
        <ProductSectionHeader eyebrow={tab.label} title={tab.title} />
        <p className="mt-5 max-w-xl text-base leading-relaxed text-slate">{tab.description}</p>
        <ul className="mt-5 max-w-xl space-y-2.5">
          {tab.features.map((feature) => (
            <li key={feature} className="flex gap-2.5 text-base leading-relaxed text-slate">
              <span className="mt-2.5 h-1.5 w-1.5 shrink-0 rounded-full bg-signal" aria-hidden="true" />
              <span>{feature}</span>
            </li>
          ))}
        </ul>
      </div>
    </article>
  );
}

export function ModernPosProductTour({ demoHref, quoteHref }: ModernPosProductTourProps) {
  const sections = MODERN_POS_PRODUCT_TOUR_TABS;
  const [lightboxOpen, setLightboxOpen] = useState(false);
  const [lightboxIndex, setLightboxIndex] = useState(0);
  const [imageFailures, setImageFailures] = useState<Record<string, boolean>>({});

  const lightboxSlides = useMemo<LightboxSlide[]>(
    () =>
      sections
        .filter((tab) => !imageFailures[tab.id])
        .map((tab) => ({
          id: tab.id,
          src: tab.imageSrc,
          alt: tab.imageAlt,
          title: tab.title,
        })),
    [imageFailures, sections],
  );

  const openLightbox = (tabId: string) => {
    if (imageFailures[tabId]) return;
    const index = lightboxSlides.findIndex((slide) => slide.id === tabId);
    if (index < 0) return;
    setLightboxIndex(index);
    setLightboxOpen(true);
  };

  return (
    <div>
      <ProductSectionHeader
        eyebrow="Product tour"
        title={MODERN_POS_TOUR_HEADING}
        description={MODERN_POS_TOUR_SUBHEADING}
      />

      <div className="mt-10 space-y-12 lg:space-y-16">
        {sections.map((tab, index) => (
          <TourSection
            key={tab.id}
            tab={tab}
            index={index}
            onOpenLightbox={() => openLightbox(tab.id)}
            onImageError={(tabId) =>
              setImageFailures((current) => ({ ...current, [tabId]: true }))
            }
          />
        ))}
      </div>

      <div className="mt-12 rounded-sm border border-line bg-mist/50 px-5 py-6 sm:px-6">
        <p className="text-base font-semibold text-ink">
          Want to see Modern POS with your retail workflow?
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
