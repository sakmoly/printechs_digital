"use client";

import { useState } from "react";
import type { ProductSpecGroup } from "@/types/content";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { productPageTheme } from "@/lib/product-page-theme";

type ProductFullSpecsProps = {
  groups: ProductSpecGroup[];
  defaultExpanded?: boolean;
};

export function ProductFullSpecs({
  groups,
  defaultExpanded = false,
}: ProductFullSpecsProps) {
  const [expanded, setExpanded] = useState(defaultExpanded);

  return (
    <div>
      <div className="flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
        <ProductSectionHeader
          eyebrow="Full specifications"
          title="Detailed technical specifications"
        />
        <button
          type="button"
          onClick={() => setExpanded((value) => !value)}
          className={`text-sm font-semibold underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal ${productPageTheme.blueHeadings ? "text-product-icon" : "text-signal-deep"}`}
        >
          {expanded ? "Hide full specifications" : "View full specifications →"}
        </button>
      </div>
      {expanded ? (
        <div className="mt-8 grid gap-5 lg:grid-cols-2">
          {groups.map((group) => (
            <div
              key={group.title}
              className="overflow-hidden rounded-sm border border-line bg-white"
            >
              <div className="border-b border-line bg-mist px-5 py-3">
                <h3 className="font-display text-lg font-semibold text-ink">
                  {group.title}
                </h3>
              </div>
              <dl className="divide-y divide-line">
                {group.items.map((item) => (
                  <div
                    key={item.label}
                    className="grid grid-cols-[minmax(0,1fr)_minmax(0,1.1fr)] gap-4 px-5 py-3 text-sm"
                  >
                    <dt className="font-medium text-slate">{item.label}</dt>
                    <dd className="text-ink">{item.value}</dd>
                  </div>
                ))}
              </dl>
            </div>
          ))}
        </div>
      ) : null}
    </div>
  );
}
