"use client";

import { analyticsConfig } from "@/lib/analytics/config";
import { getUtmParams } from "@/lib/analytics/attribution";
import { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";
import type { AnalyticsEventName, AnalyticsParams } from "@/lib/analytics/types";

declare global {
  interface Window {
    dataLayer?: Record<string, unknown>[];
  }
}

function pushDataLayer(payload: Record<string, unknown>) {
  if (typeof window === "undefined") return;
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push(payload);
}

function sanitizeParams(params: AnalyticsParams): Record<string, string | number | boolean> {
  const clean: Record<string, string | number | boolean> = {};
  for (const [key, value] of Object.entries(params)) {
    if (value === undefined || value === null || value === "") continue;
    clean[key] = value;
  }
  return clean;
}

export function trackEvent(event: AnalyticsEventName, params: AnalyticsParams = {}) {
  const page_location =
    typeof params.page_location === "string"
      ? params.page_location
      : typeof window !== "undefined"
        ? getPageLocation(window.location.pathname, window.location.search)
        : undefined;

  const payload = sanitizeParams({
    event,
    page_title: params.page_title ?? (typeof window !== "undefined" ? getPageTitle() : undefined),
    page_location,
    ...getUtmParams(),
    ...params,
  });

  pushDataLayer(payload);

  if (analyticsConfig.debug && typeof console !== "undefined") {
    // eslint-disable-next-line no-console -- intentional debug output when NEXT_PUBLIC_ANALYTICS_DEBUG=true
    console.info("[Analytics]", payload);
  }
}

export function trackPageView(pathname: string, search = "") {
  trackEvent("page_view", {
    page_location: getPageLocation(pathname, search),
    page_title: typeof document !== "undefined" ? document.title : undefined,
  });
}

export function trackProductView(params: AnalyticsParams) {
  trackEvent("product_view", params);
}

export function trackQuoteClick(params: AnalyticsParams) {
  trackEvent("request_quote_click", params);
}

export function trackDemoClick(params: AnalyticsParams) {
  trackEvent("demo_request_click", params);
}

export function trackWhatsAppClick(params: AnalyticsParams) {
  trackEvent("whatsapp_click", params);
}

export function trackPhoneClick(params: AnalyticsParams) {
  trackEvent("phone_click", params);
}

export function trackEmailClick(params: AnalyticsParams) {
  trackEvent("email_click", params);
}

export function trackFormStart(formName: string, params: AnalyticsParams = {}) {
  trackEvent("form_start", { form_name: formName, ...params });
}

export function trackFormSuccess(formName: string, params: AnalyticsParams = {}) {
  trackEvent("form_submit_success", { form_name: formName, ...params });
}

export function trackFormError(formName: string, params: AnalyticsParams = {}) {
  trackEvent("form_submit_error", { form_name: formName, ...params });
}

export function trackVideoEvent(
  milestone: Extract<
    AnalyticsEventName,
    "video_start" | "video_25_percent" | "video_50_percent" | "video_75_percent" | "video_complete"
  >,
  params: AnalyticsParams,
) {
  trackEvent(milestone, params);
}

export function trackDownload(params: AnalyticsParams) {
  trackEvent("file_download", params);
}

export function trackOutboundClick(params: AnalyticsParams) {
  trackEvent("outbound_click", params);
}
