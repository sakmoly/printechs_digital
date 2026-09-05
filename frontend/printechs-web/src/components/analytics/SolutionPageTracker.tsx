"use client";

import { useEffect, useRef } from "react";
import { trackEvent } from "@/lib/analytics/events";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";

type SolutionPageTrackerProps = {
  slug: string;
  name: string;
  category?: string;
};

export function SolutionPageTracker({ slug, name, category }: SolutionPageTrackerProps) {
  const trackedSlug = useRef<string | null>(null);

  useEffect(() => {
    if (trackedSlug.current === slug) return;
    trackedSlug.current = slug;

    trackEvent("product_view", {
      product_name: name,
      product_slug: slug,
      product_category: category || "solution",
      business_segment: "software",
      page_title: getPageTitle(),
      page_location: getPageLocation(window.location.pathname, window.location.search),
    });
  }, [slug, name, category]);

  return null;
}
