"use client";

import { useMemo, useState } from "react";
import type { Product } from "@/types/content";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

type ProductsCatalogProps = {
  products: Product[];
  brands: string[];
};

const divisionFilters = [
  { value: "all", label: "All divisions" },
  { value: "industrial", label: "Industrial" },
  { value: "retail", label: "Retail" },
] as const;

export function ProductsCatalog({ products, brands }: ProductsCatalogProps) {
  const [division, setDivision] = useState<string>("all");
  const [brand, setBrand] = useState<string>("all");

  const filtered = useMemo(() => {
    return products.filter((item) => {
      if (division !== "all" && item.division !== division) return false;
      if (brand !== "all" && item.brand !== brand) return false;
      return true;
    });
  }, [products, division, brand]);

  const filterButtonClass = (active: boolean) =>
    `rounded-sm border px-4 py-2 text-sm font-semibold transition focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal ${
      active
        ? "border-signal bg-signal/10 text-signal-deep"
        : "border-line bg-white text-slate hover:border-line-strong hover:text-ink"
    }`;

  return (
    <>
      <div className="flex flex-col gap-4 border-b border-line pb-6 sm:flex-row sm:flex-wrap sm:items-center sm:justify-between">
        <div>
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
            Filter
          </p>
          <p className="mt-1 text-sm text-slate">
            {filtered.length} product{filtered.length === 1 ? "" : "s"}
          </p>
        </div>
        <div className="flex flex-col gap-3 sm:flex-row sm:flex-wrap">
          <div className="flex flex-wrap gap-2">
            {divisionFilters.map((option) => (
              <button
                key={option.value}
                type="button"
                onClick={() => setDivision(option.value)}
                className={filterButtonClass(division === option.value)}
              >
                {option.label}
              </button>
            ))}
          </div>
          <label className="flex items-center gap-2">
            <span className="sr-only">Filter by brand</span>
            <select
              value={brand}
              onChange={(event) => setBrand(event.target.value)}
              className="min-h-10 rounded-sm border border-line bg-white px-3 text-sm font-medium text-ink focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              <option value="all">All brands</option>
              {brands.map((name) => (
                <option key={name} value={name}>
                  {name}
                </option>
              ))}
            </select>
          </label>
        </div>
      </div>

      {filtered.length > 0 ? (
        <FeatureGrid columns={3} gap="md">
          {filtered.map((item) => (
            <Card
              key={item.id}
              href={`/products/${item.slug}`}
              title={item.name}
              description={item.summary}
              meta={`${item.brand} · ${item.category}`}
              cta="View product"
              media={
                <ImageFrame
                  src={item.image.src}
                  alt={item.image.alt}
                  spec={IMAGE_SPECS.product}
                  fill
                  className="aspect-square bg-mist"
                  imageClassName="media-zoom object-cover p-6"
                  sizes="(max-width: 768px) 100vw, 33vw"
                />
              }
            />
          ))}
        </FeatureGrid>
      ) : (
        <div className="rounded-sm border border-line bg-mist p-8 text-center">
          <p className="text-base text-slate">
            No products match the selected filters. Try another division or brand.
          </p>
        </div>
      )}
    </>
  );
}
