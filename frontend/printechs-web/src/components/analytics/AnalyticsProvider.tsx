"use client";

import { useEffect, useRef } from "react";
import { usePathname, useSearchParams } from "next/navigation";
import { captureAttributionFromUrl } from "@/lib/analytics/attribution";
import {
  trackDemoClick,
  trackDownload,
  trackEmailClick,
  trackFormStart,
  trackOutboundClick,
  trackPageView,
  trackPhoneClick,
  trackQuoteClick,
  trackWhatsAppClick,
} from "@/lib/analytics/events";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";

function readDataset(anchor: HTMLElement, key: string): string | undefined {
  const value = anchor.dataset[key as keyof DOMStringMap];
  return value?.trim() || undefined;
}

function inferQuoteOrDemo(href: string): "quote" | "demo" | null {
  const lower = href.toLowerCase();
  if (lower.includes("/quote") || lower.includes("request-quote")) return "quote";
  if (lower.includes("/demo") || lower.includes("request-demo")) return "demo";
  return null;
}

function isExternalHref(href: string): boolean {
  if (!href.startsWith("http://") && !href.startsWith("https://")) return false;
  try {
    const url = new URL(href);
    const host = url.hostname.replace(/^www\./, "");
    return !["printechs.com", "demo.printechs.com", "localhost"].includes(host);
  } catch {
    return false;
  }
}

function isWhatsAppHref(href: string): boolean {
  const lower = href.toLowerCase();
  return lower.includes("wa.me/") || lower.includes("whatsapp.com");
}

function isDownloadHref(href: string): boolean {
  const lower = href.toLowerCase();
  return (
    lower.includes("/files/") &&
    (lower.endsWith(".pdf") ||
      lower.endsWith(".zip") ||
      lower.endsWith(".doc") ||
      lower.endsWith(".docx") ||
      lower.endsWith(".xlsx"))
  );
}

function fileTypeFromHref(href: string): string {
  const match = href.toLowerCase().match(/\.([a-z0-9]+)(?:\?|#|$)/);
  return match?.[1] || "file";
}

export function AnalyticsProvider({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const search = searchParams.toString();
  const searchSuffix = search ? `?${search}` : "";
  const lastTrackedPath = useRef<string | null>(null);

  useEffect(() => {
    if (typeof window === "undefined") return;
    captureAttributionFromUrl(new URL(window.location.href));
  }, []);

  useEffect(() => {
    const fullPath = `${pathname}${searchSuffix}`;
    if (lastTrackedPath.current === fullPath) return;
    lastTrackedPath.current = fullPath;
    trackPageView(pathname, searchSuffix);
  }, [pathname, searchSuffix]);

  useEffect(() => {
    function handleClick(event: MouseEvent) {
      const target = event.target as HTMLElement | null;
      const anchor = target?.closest("a") as HTMLAnchorElement | null;
      if (!anchor?.href) return;

      const href = anchor.getAttribute("href") || anchor.href;
      const pageTitle = getPageTitle();
      const pageLocation = getPageLocation(pathname, searchSuffix);
      const buttonLocation = readDataset(anchor, "analyticsLocation") || "unknown";
      const productName = readDataset(anchor, "analyticsProduct");
      const brand = readDataset(anchor, "analyticsBrand");
      const category = readDataset(anchor, "analyticsCategory");
      const explicitEvent = readDataset(anchor, "analyticsEvent");

      if (href.startsWith("tel:")) {
        trackPhoneClick({ page_title: pageTitle, page_location: pageLocation, button_location: buttonLocation });
        return;
      }

      if (href.startsWith("mailto:")) {
        trackEmailClick({ page_title: pageTitle, page_location: pageLocation, button_location: buttonLocation });
        return;
      }

      if (isWhatsAppHref(href) || explicitEvent === "whatsapp_click") {
        trackWhatsAppClick({
          page_title: pageTitle,
          page_location: pageLocation,
          button_location: buttonLocation,
          product_name: productName,
          brand,
        });
        return;
      }

      if (explicitEvent === "request_quote_click") {
        trackQuoteClick({
          page_title: pageTitle,
          page_location: pageLocation,
          button_location: buttonLocation,
          product_name: productName,
          brand,
          category,
        });
        return;
      }

      if (explicitEvent === "demo_request_click") {
        trackDemoClick({
          page_title: pageTitle,
          page_location: pageLocation,
          button_location: buttonLocation,
          product_name: productName,
          solution_name: readDataset(anchor, "analyticsSolution"),
        });
        return;
      }

      const inferred = inferQuoteOrDemo(href);
      if (inferred === "quote") {
        trackQuoteClick({
          page_title: pageTitle,
          page_location: pageLocation,
          button_location: buttonLocation,
          product_name: productName,
          brand,
          category,
        });
        return;
      }

      if (inferred === "demo") {
        trackDemoClick({
          page_title: pageTitle,
          page_location: pageLocation,
          button_location: buttonLocation,
          product_name: productName,
        });
        return;
      }

      if (isDownloadHref(href) || anchor.hasAttribute("download")) {
        const fileName = decodeURIComponent(href.split("/").pop()?.split("?")[0] || "download");
        trackDownload({
          file_name: fileName,
          file_type: fileTypeFromHref(href),
          product_name: productName,
          brand,
          page_location: pageLocation,
        });
        return;
      }

      if (isExternalHref(href) && !isWhatsAppHref(href)) {
        let destinationDomain = href;
        try {
          destinationDomain = new URL(href).hostname;
        } catch {
          // Keep raw href fallback.
        }
        trackOutboundClick({
          destination_domain: destinationDomain,
          link_text: anchor.textContent?.trim().slice(0, 120) || undefined,
          page_location: pageLocation,
        });
      }
    }

    document.addEventListener("click", handleClick, true);
    return () => document.removeEventListener("click", handleClick, true);
  }, [pathname, searchSuffix]);

  useEffect(() => {
    if (typeof window === "undefined") return;

    function handleFormFocusIn(event: FocusEvent) {
      const form = (event.target as HTMLElement | null)?.closest("form");
      if (!form || form.dataset.analyticsStarted === "true") return;
      form.dataset.analyticsStarted = "true";
      const formName = form.dataset.analyticsForm || form.getAttribute("name") || "unknown_form";
      trackFormStart(formName, {
        page_title: getPageTitle(),
        page_location: getPageLocation(pathname, searchSuffix),
        product_name: form.dataset.analyticsProduct,
        product_category: form.dataset.analyticsCategory,
      });
    }

    document.addEventListener("focusin", handleFormFocusIn, true);
    return () => document.removeEventListener("focusin", handleFormFocusIn, true);
  }, [pathname, searchSuffix]);

  return children;
}
