"use client";

import { useState } from "react";
import type { VisualStoryItem } from "@/types/content";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";

type ProductVisualStoryProps = {
  heading: string;
  items: VisualStoryItem[];
};

export function ProductVisualStory({ heading, items }: ProductVisualStoryProps) {
  const [activeId, setActiveId] = useState(items[0]?.id ?? "");
  const activeItem = items.find((item) => item.id === activeId) ?? items[0];

  if (!activeItem) return null;

  return (
    <div>
      <ProductSectionHeader eyebrow="In action" title={heading} />
      <div className="mt-8 overflow-hidden rounded-sm border border-line bg-white shadow-soft">
        <ImageFrame
          src={activeItem.image.src}
          alt={activeItem.image.alt}
          spec={IMAGE_SPECS.industry}
          fill
          className="aspect-[21/9] sm:aspect-[2.4/1]"
          imageClassName="object-cover"
          sizes="100vw"
          showSizeLabel={false}
        />
        {activeItem.caption ? (
          <p className="border-t border-line bg-mist px-5 py-3 text-sm text-slate">
            {activeItem.caption}
          </p>
        ) : null}
      </div>
      {items.length > 1 ? (
        <div className="mt-4 flex flex-wrap gap-2">
          {items.map((item) => {
            const isActive = item.id === activeId;
            return (
              <button
                key={item.id}
                type="button"
                onClick={() => setActiveId(item.id)}
                className={`rounded-sm border px-4 py-2 text-sm font-semibold transition duration-300 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal ${
                  isActive
                    ? "border-signal bg-signal/10 text-signal-deep"
                    : "border-line bg-white text-slate hover:border-line-strong hover:text-ink"
                }`}
              >
                {item.label}
              </button>
            );
          })}
        </div>
      ) : null}
    </div>
  );
}
