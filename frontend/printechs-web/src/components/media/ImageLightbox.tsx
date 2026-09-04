"use client";

import Image from "next/image";
import { useCallback, useEffect, useRef } from "react";
import { withBasePath } from "@/lib/paths";

export type LightboxSlide = {
  id: string;
  src: string;
  alt: string;
  title: string;
};

type ImageLightboxProps = {
  slides: LightboxSlide[];
  activeIndex: number;
  onClose: () => void;
  onNavigate: (index: number) => void;
};

export function ImageLightbox({
  slides,
  activeIndex,
  onClose,
  onNavigate,
}: ImageLightboxProps) {
  const closeButtonRef = useRef<HTMLButtonElement>(null);
  const slide = slides[activeIndex];
  const hasMultiple = slides.length > 1;

  const goPrev = useCallback(() => {
    onNavigate((activeIndex - 1 + slides.length) % slides.length);
  }, [activeIndex, onNavigate, slides.length]);

  const goNext = useCallback(() => {
    onNavigate((activeIndex + 1) % slides.length);
  }, [activeIndex, onNavigate, slides.length]);

  useEffect(() => {
    closeButtonRef.current?.focus();
    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";

    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key === "Escape") {
        onClose();
      } else if (event.key === "ArrowLeft" && hasMultiple) {
        goPrev();
      } else if (event.key === "ArrowRight" && hasMultiple) {
        goNext();
      }
    };

    window.addEventListener("keydown", onKeyDown);
    return () => {
      document.body.style.overflow = previousOverflow;
      window.removeEventListener("keydown", onKeyDown);
    };
  }, [goNext, goPrev, hasMultiple, onClose]);

  if (!slide) return null;

  return (
    <div
      className="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6"
      role="dialog"
      aria-modal="true"
      aria-label={slide.title}
    >
      <button
        type="button"
        className="absolute inset-0 bg-ink/80 backdrop-blur-[2px]"
        aria-label="Close image viewer"
        onClick={onClose}
      />

      <div className="relative z-10 flex w-full max-w-5xl flex-col overflow-hidden rounded-md border border-line bg-white shadow-soft">
        <div className="flex items-center justify-between gap-4 border-b border-line px-4 py-3 sm:px-5">
          <p className="min-w-0 truncate text-sm font-semibold text-ink">{slide.title}</p>
          <button
            ref={closeButtonRef}
            type="button"
            onClick={onClose}
            className="inline-flex h-9 w-9 shrink-0 items-center justify-center rounded-sm border border-line text-slate transition hover:border-line-strong hover:text-ink focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            aria-label="Close"
          >
            <span aria-hidden="true" className="text-lg leading-none">
              ×
            </span>
          </button>
        </div>

        <div className="relative aspect-[16/10] w-full bg-mist">
          <Image
            src={withBasePath(slide.src)}
            alt={slide.alt}
            fill
            className="object-contain object-center"
            sizes="(max-width: 1024px) 100vw, 80rem"
            priority
          />
        </div>

        {hasMultiple ? (
          <div className="flex items-center justify-between gap-3 border-t border-line px-4 py-3 sm:px-5">
            <button
              type="button"
              onClick={goPrev}
              className="rounded-sm border border-line px-3 py-2 text-sm font-semibold text-slate transition hover:border-line-strong hover:text-ink focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              Previous
            </button>
            <p className="text-xs font-medium text-slate">
              {activeIndex + 1} / {slides.length}
            </p>
            <button
              type="button"
              onClick={goNext}
              className="rounded-sm border border-line px-3 py-2 text-sm font-semibold text-slate transition hover:border-line-strong hover:text-ink focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              Next
            </button>
          </div>
        ) : null}
      </div>
    </div>
  );
}
