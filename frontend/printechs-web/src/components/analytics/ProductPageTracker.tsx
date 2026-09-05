"use client";

import { useEffect, useRef } from "react";
import type { ProductPageContent } from "@/types/content";
import { trackProductView } from "@/lib/analytics/events";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";
import { deriveBusinessSegment } from "@/lib/analytics/segments";

type ProductPageTrackerProps = {
  page: ProductPageContent;
};

export function ProductPageTracker({ page }: ProductPageTrackerProps) {
  const trackedSlug = useRef<string | null>(null);

  useEffect(() => {
    if (trackedSlug.current === page.slug) return;
    trackedSlug.current = page.slug;

    trackProductView({
      product_name: page.displayName,
      product_brand: page.brand || undefined,
      product_category: page.category,
      product_slug: page.slug,
      business_segment: deriveBusinessSegment(page),
      page_title: getPageTitle(),
      page_location: getPageLocation(window.location.pathname, window.location.search),
    });
  }, [page]);

  return null;
}
