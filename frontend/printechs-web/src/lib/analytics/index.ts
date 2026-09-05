export { analyticsConfig, isValidClarityId, isValidGtmId } from "@/lib/analytics/config";
export { captureAttributionFromUrl, getLeadAttribution, getUtmParams } from "@/lib/analytics/attribution";
export {
  trackDemoClick,
  trackDownload,
  trackEmailClick,
  trackEvent,
  trackFormError,
  trackFormStart,
  trackFormSuccess,
  trackOutboundClick,
  trackPageView,
  trackPhoneClick,
  trackProductView,
  trackQuoteClick,
  trackVideoEvent,
  trackWhatsAppClick,
} from "@/lib/analytics/events";
export { getPageLocation, getPageTitle } from "@/lib/analytics/page-location";
export { deriveBusinessSegment } from "@/lib/analytics/segments";
export type {
  AnalyticsEventName,
  AnalyticsParams,
  LeadAttribution,
  ProductAnalyticsContext,
} from "@/lib/analytics/types";
