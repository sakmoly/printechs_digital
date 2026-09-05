export type AnalyticsEventName =
  | "page_view"
  | "product_view"
  | "request_quote_click"
  | "demo_request_click"
  | "form_start"
  | "form_submit_success"
  | "form_submit_error"
  | "whatsapp_click"
  | "phone_click"
  | "email_click"
  | "video_start"
  | "video_25_percent"
  | "video_50_percent"
  | "video_75_percent"
  | "video_complete"
  | "file_download"
  | "outbound_click"
  | "site_search";

export type AnalyticsParams = Record<string, string | number | boolean | undefined>;

export type LeadAttribution = {
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
  utm_content?: string;
  utm_term?: string;
  landing_page?: string;
  referrer?: string;
  first_visit_at?: string;
};

export type ProductAnalyticsContext = {
  product_name?: string;
  product_brand?: string;
  product_category?: string;
  product_slug?: string;
  business_segment?: string;
  page_title?: string;
  page_location?: string;
};
