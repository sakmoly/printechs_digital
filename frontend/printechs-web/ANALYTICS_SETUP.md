# Printechs Website — Analytics & SEO Setup Guide

Use this checklist **after** the new site goes live at **https://printechs.com** (root, no `/newwebsite`).

The frontend code is ready. Tracking scripts load **only when environment variables are set**. Until then, the site behaves exactly as before (no GTM/Clarity in the page).

---

## 1. Production environment variables

Copy `.env.example` to `.env.production.local` (or your deployment secret store) and set:

```bash
# Canonical production URL (used for page_location, OG URLs, sitemap, canonical)
NEXT_PUBLIC_SITE_URL=https://printechs.com

# Root launch — leave empty (no /newwebsite prefix)
NEXT_PUBLIC_BASE_PATH=

# Allow Google to index public pages
NEXT_PUBLIC_ALLOW_INDEXING=true

# ERPNext API used by /api/leads (server-side)
ERPNEXT_URL=https://printechs.com

# --- Analytics (fill after creating accounts) ---
NEXT_PUBLIC_GTM_ID=GTM-XXXXXXX
NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX
NEXT_PUBLIC_CLARITY_PROJECT_ID=your_clarity_project_id
NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION=your_verification_token

# Debug logging in browser console (keep false in production)
NEXT_PUBLIC_ANALYTICS_DEBUG=false
```

Rebuild and restart the Next.js service after changing env vars.

---

## 2. Google Tag Manager (GTM)

1. Create a **Web** container at [tagmanager.google.com](https://tagmanager.google.com) for `printechs.com`.
2. Copy the container ID → `NEXT_PUBLIC_GTM_ID=GTM-XXXXXXX`.
3. **Do not** add a second gtag/GA4 script in the codebase — GA4 should be configured **inside GTM only**.

### Recommended GTM tags

| Tag | Type | Notes |
|-----|------|-------|
| GA4 Configuration | Google Analytics: GA4 Configuration | Measurement ID from step 3 |
| GA4 Event (optional) | GA4 Event | Map `dataLayer` custom events if needed |
| Microsoft Clarity (optional) | Custom HTML | Or load Clarity via env var (already implemented) |

### Recommended GTM triggers

- **All Pages** — GA4 Configuration (page views)
- **Custom Event** — event name equals each conversion event (see section 5)

### Mark as conversions in GA4

In GA4 → Admin → Events, mark as conversions:

- `form_submit_success`
- `whatsapp_click`
- `phone_click`
- `request_quote_click` (optional — or use form success only)
- `demo_request_click` (optional)

---

## 3. Google Analytics 4 (GA4)

1. Create a GA4 property for **Printechs — Website**.
2. Copy Measurement ID → `NEXT_PUBLIC_GA_MEASUREMENT_ID=G-XXXXXXXXXX`.
3. In GTM, add **GA4 Configuration** tag with this ID.
4. Enable **Enhanced measurement** (scrolls, outbound clicks) in GA4 — our custom events still provide richer product context.

### What GA4 will report (anonymous visitors)

- When they visited (date/time, sessions)
- Channel / source / medium / campaign (with UTMs)
- Country, city (where available), device
- Landing pages, page paths
- Custom events: product views, quote/demo clicks, WhatsApp, forms, videos, downloads

GA4 does **not** identify visitors by name/email — that is intentional (privacy). Identified leads come from ERPNext after form submit.

---

## 4. Microsoft Clarity

1. Create project at [clarity.microsoft.com](https://clarity.microsoft.com) for `printechs.com`.
2. Copy Project ID → `NEXT_PUBLIC_CLARITY_PROJECT_ID=...`
3. The site loads Clarity once via `MicrosoftClarity.tsx` (no duplicate on route changes).

Optional: enable **input masking** in Clarity settings for form fields.

---

## 5. Google Search Console

1. Add property `https://printechs.com`.
2. Choose **HTML tag** verification.
3. Copy the `content` value → `NEXT_PUBLIC_GOOGLE_SITE_VERIFICATION=...`
4. Rebuild/redeploy so the meta tag appears in `<head>`.
5. After launch, submit sitemap: `https://printechs.com/sitemap.xml`

---

## 6. Events reference (dataLayer)

All events push to `window.dataLayer` via `trackEvent()`. GTM/GA4 should listen to these.

| Event | When it fires | Key parameters |
|-------|---------------|----------------|
| `page_view` | Route change (SPA) | `page_location`, `page_title`, UTMs |
| `product_view` | Product/software page mount | `product_name`, `product_brand`, `product_category`, `product_slug`, `business_segment` |
| `request_quote_click` | Quote CTA click | `product_name`, `brand`, `category`, `button_location` |
| `demo_request_click` | Demo CTA click | `product_name`, `solution_name`, `button_location` |
| `form_start` | First focus in a tracked form | `form_name`, `product_name`, `product_category` |
| `form_submit_success` | API confirms success | `form_name`, `product_name` |
| `form_submit_error` | API error | `form_name` |
| `whatsapp_click` | WhatsApp link/button | `button_location`, `product_name`, `brand` |
| `phone_click` | `tel:` link | `button_location` |
| `email_click` | `mailto:` link | `button_location` |
| `video_start` / `video_25_percent` / … / `video_complete` | Hosted HTML5 video | `video_title`, `product_name`, `brand` |
| `file_download` | PDF/brochure link | `file_name`, `file_type`, `product_name` |
| `outbound_click` | External link | `destination_domain`, `link_text` |

**Not implemented:** `site_search` — no internal search UI exists on the site.

**Partial:** YouTube/Vimeo embed milestones — `video_start` fires on poster click; iframe progress requires GTM YouTube trigger or future enhancement.

---

## 7. UTM & lead attribution

On first visit, UTMs + landing page + referrer are stored in **sessionStorage** (`printechs_attribution_v1`).

On successful form submit, `context.attribution` is sent to `/api/leads` → ERPNext `submit_lead`.

### ERPNext backend

Custom fields on **Lead** (patch `add_lead_attribution_fields`) store website acquisition data:

| Lead field | Source |
|------------|--------|
| `web_utm_source` … `web_utm_term` | UTM parameters |
| `web_landing_page` | First landing URL in session |
| `web_referrer` | HTTP referrer |
| `web_first_visit_at` | First visit timestamp |
| `web_product_slug` | Product slug from form context |
| `web_source_url` | Page URL where form was submitted |

`printechs_digital.api.lead.submit_lead` saves these on Lead create/update (first-touch: empty fields only).

Run on each site after deploy: `bench --site YOUR_SITE migrate`

---

## 8. Campaign URL examples

Use these in email and ads after launch:

```
https://printechs.com/?utm_source=customer_email&utm_medium=email&utm_campaign=website_launch_2026

https://printechs.com/products/hitachi-ux-d161?utm_source=customer_email&utm_medium=email&utm_campaign=hitachi_launch&utm_content=hitachi_cij

https://printechs.com/software/modern-pos?utm_source=linkedin&utm_medium=paid_social&utm_campaign=modern_pos_2026

https://printechs.com/?utm_source=google&utm_medium=cpc&utm_campaign=hitachi_cij_saudi
```

---

## 9. Pre-launch technical test

After setting env vars and deploying to production:

| Check | How to verify |
|-------|----------------|
| GTM loads | View page source → GTM snippet; Tag Assistant |
| GA4 page views | GA4 Realtime report |
| SPA navigation | Click internal links → new page_view in dataLayer |
| Clarity | Clarity dashboard sessions |
| Search Console meta | View source → `google-site-verification` |
| WhatsApp / quote / demo | Click CTAs → dataLayer events (set `NEXT_PUBLIC_ANALYTICS_DEBUG=true` locally) |
| Form success | Submit test lead → `form_submit_success` only after API OK |
| UTM capture | Visit with `?utm_source=test` → check sessionStorage |
| Sitemap | Open `/sitemap.xml` — absolute `https://printechs.com/...` URLs |
| robots.txt | Open `/robots.txt` — `Allow: /` and sitemap line when indexing on |
| Canonical | View product page source → canonical = production URL |
| No duplicate GA | Only one GA4 config (via GTM), no extra gtag in HTML |
| Build | `npm run build` succeeds (Node ≥ 20 recommended) |

---

## 10. Cookie consent (future)

Analytics load immediately today. When you add a consent banner:

- Gate GTM/Clarity injection on consent in `layout.tsx` / `GoogleTagManager.tsx`
- Use GTM Consent Mode v2 for GA4

Document your legal basis (Saudi PDPL / marketing opt-in) with your compliance advisor.

---

## 11. Reporting funnel (GA4 + ERPNext)

```
Website visitors (GA4)
  → Product page views (product_view)
  → Engaged visitors (scroll, time on page)
  → Video viewers (video_* events)
  → WhatsApp / quote / demo clicks
  → Lead (form_submit_success + ERPNext Lead)
  → Quotation → Sale (ERPNext CRM)
```

Join GA4 campaign data with ERPNext leads using UTM fields on Lead once backend is wired.

---

## 12. Deployment reminder

Code lives in:

`apps/printechs_digital/frontend/printechs-web/`

Production server copy (if used):

`/home/erpnext/frappe-bench/frontend/printechs-web/`

Sync, set env, build with Node 20, restart `printechs-web` service. **Do not** enable tracking on `/newwebsite` demo unless testing — configure for root `printechs.com` at cutover.
