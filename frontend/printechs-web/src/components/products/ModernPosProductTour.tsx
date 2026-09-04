"use client";

import Image from "next/image";
import { useCallback, useMemo, useState } from "react";
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
    <div className="flex aspect-[16/10] w-full flex-col items-center justify-center rounded-sm border border-dashed border-line bg-mist px-6 text-center">
      <p className="text-sm font-semibold text-ink">Modern POS Screenshot Coming Soon</p>
      <p className="mt-2 max-w-xs text-xs leading-relaxed text-slate">
        Upload WebP screenshots to{" "}
        <span className="font-mono text-[0.68rem]">public/images/software/modern-pos/screens/</span>
      </p>
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
      className="group relative block w-full overflow-hidden rounded-sm border border-line bg-white text-left shadow-soft transition duration-300 hover:border-line-strong focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2"
      aria-label={`View larger ${tab.title} screenshot`}
    >
      <div className="flex items-center gap-2 border-b border-line bg-mist/80 px-3 py-2">
        <span className="h-2.5 w-2.5 rounded-full bg-line-strong/70" aria-hidden="true" />
        <span className="h-2.5 w-2.5 rounded-full bg-line-strong/50" aria-hidden="true" />
        <span className="h-2.5 w-2.5 rounded-full bg-line-strong/35" aria-hidden="true" />
        <span className="ml-2 truncate text-[0.65rem] font-medium uppercase tracking-[0.12em] text-slate">
          Modern POS · {tab.label}
        </span>
      </div>
      <div className="relative aspect-[16/10] w-full bg-white">
        <Image
          src={withBasePath(tab.imageSrc)}
          alt={tab.imageAlt}
          fill
          priority={priority}
          loading={priority ? undefined : "lazy"}
          className="object-contain object-top p-2 transition duration-300 group-hover:scale-[1.01] motion-reduce:transition-none motion-reduce:group-hover:scale-100"
          sizes="(max-width: 1024px) 100vw, 60rem"
          onError={() => {
            setFailed(true);
            onImageError(tab.id);
          }}
        />
      </div>
      <p className="border-t border-line bg-white px-3 py-2 text-xs text-slate opacity-0 transition group-hover:opacity-100 motion-reduce:opacity-100">
        Click to enlarge
      </p>
    </button>
  );
}

function TourPanelContent({ tab }: { tab: ModernPosTourTab }) {
  return (
    <div className="motion-reduce:transition-none">
      <h3 className="font-display text-2xl font-semibold tracking-tight text-ink">{tab.title}</h3>
      <p className="mt-3 text-base leading-relaxed text-slate">{tab.description}</p>
      <ul className="mt-5 space-y-2.5">
        {tab.features.map((feature) => (
          <li key={feature} className="flex gap-2.5 text-sm leading-relaxed text-slate">
            <span
              className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-signal"
              aria-hidden="true"
            />
            <span>{feature}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function ModernPosProductTour({ demoHref, quoteHref }: ModernPosProductTourProps) {
  const tabs = MODERN_POS_PRODUCT_TOUR_TABS;
  const [activeId, setActiveId] = useState(tabs[0]?.id ?? "");
  const [displayId, setDisplayId] = useState(tabs[0]?.id ?? "");
  const [fading, setFading] = useState(false);
  const [lightboxOpen, setLightboxOpen] = useState(false);
  const [lightboxIndex, setLightboxIndex] = useState(0);
  const [imageFailures, setImageFailures] = useState<Record<string, boolean>>({});

  const activeTab = tabs.find((tab) => tab.id === displayId) ?? tabs[0];
  const activeIndex = tabs.findIndex((tab) => tab.id === activeId);

  const lightboxSlides = useMemo<LightboxSlide[]>(
    () =>
      tabs
        .filter((tab) => !imageFailures[tab.id])
        .map((tab) => ({
          id: tab.id,
          src: tab.imageSrc,
          alt: tab.imageAlt,
          title: tab.title,
        })),
    [imageFailures, tabs],
  );

  const selectTab = useCallback(
    (id: string) => {
      if (id === activeId) return;

      const reducedMotion =
        typeof window !== "undefined" &&
        window.matchMedia("(prefers-reduced-motion: reduce)").matches;

      if (reducedMotion) {
        setActiveId(id);
        setDisplayId(id);
        return;
      }

      setFading(true);
      window.setTimeout(() => {
        setActiveId(id);
        setDisplayId(id);
        setFading(false);
      }, 180);
    },
    [activeId],
  );

  const openLightbox = () => {
    if (imageFailures[activeTab.id]) return;
    const index = lightboxSlides.findIndex((slide) => slide.id === activeTab.id);
    if (index < 0) return;
    setLightboxIndex(index);
    setLightboxOpen(true);
  };

  if (!activeTab) return null;

  return (
    <div>
      <ProductSectionHeader
        eyebrow="Product tour"
        title={MODERN_POS_TOUR_HEADING}
        description={MODERN_POS_TOUR_SUBHEADING}
      />

      <div className="mt-6 -mx-4 overflow-x-auto px-4 pb-1 sm:mx-0 sm:px-0">
        <div
          role="tablist"
          aria-label="Modern POS product tour"
          className="flex min-w-max gap-2 sm:flex-wrap"
        >
          {tabs.map((tab) => {
            const selected = tab.id === activeId;
            return (
              <button
                key={tab.id}
                type="button"
                role="tab"
                id={`modern-pos-tab-${tab.id}`}
                aria-selected={selected}
                aria-controls={`modern-pos-panel-${tab.id}`}
                onClick={() => selectTab(tab.id)}
                className={`shrink-0 rounded-sm border px-4 py-2 text-sm font-semibold transition duration-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal motion-reduce:transition-none ${
                  selected
                    ? "border-signal bg-signal/10 text-signal-deep"
                    : "border-line bg-white text-slate hover:border-line-strong hover:text-ink"
                }`}
              >
                {tab.label}
              </button>
            );
          })}
        </div>
      </div>

      <div
        className={`mt-8 grid items-start gap-8 transition-opacity duration-300 motion-reduce:transition-none lg:grid-cols-[minmax(0,1.75fr)_minmax(0,1fr)] lg:gap-12 ${
          fading ? "opacity-0" : "opacity-100"
        }`}
      >
        <div
          role="tabpanel"
          id={`modern-pos-panel-${activeTab.id}`}
          aria-labelledby={`modern-pos-tab-${activeTab.id}`}
          className="min-w-0"
        >
          <TourScreenshot
            tab={activeTab}
            priority={activeIndex === 0}
            onOpenLightbox={openLightbox}
            onImageError={(tabId) =>
              setImageFailures((current) => ({ ...current, [tabId]: true }))
            }
          />
        </div>

        <div className="min-w-0 lg:pt-2">
          <TourPanelContent tab={activeTab} />
        </div>
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
