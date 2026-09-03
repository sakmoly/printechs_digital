# ERPNext ↔ Frontend Field Map

**Status:** Approved — maps **Website Product** DocType (not legacy Website Item)  
**Companion doc:** [WEBSITE_PRODUCT_DOCTYPE.md](./WEBSITE_PRODUCT_DOCTYPE.md)  
**Frontend types:** `frontend/printechs-web/src/types/content.ts` → `ProductPageContent`  
**Frontend loader (swap point):** `frontend/printechs-web/src/lib/product-service.ts` → `resolveProductPage(slug)`  
**Live template reference:** [Hitachi UX-D161W](https://printechs.com/newwebsite/products/hitachi-ux-d161)

> **Note:** Legacy **Website Item** (Webshop) remains for the old Frappe shop. **Website Product** is a separate DocType in `printechs_digital`, created from Item via **Digital Website → Create Website Product**. Optional `website_item_reference` field stores the legacy link for migration only.

---

## 1. Architecture overview

```text
┌─────────────────────────┐
│  ERPNext                │
│  Website Product        │──┐
│  (+ child tables)       │  │
│  optional → Item        │  │  GET /api/method/printechs_digital.api.website.get_product?slug=
└─────────────────────────┘  │
                             ▼
┌─────────────────────────┐
│  JSON response          │  Must match ProductPageContent (+ resolved brand)
│  (camelCase keys)       │
└─────────────────────────┘
                             ▼
┌─────────────────────────┐
│  resolveProductPage()   │  Replace mock lookup; keep UI unchanged
└─────────────────────────┘
                             ▼
┌─────────────────────────┐
│  ProductPageView        │  Same template for industrial, retail, software
└─────────────────────────┘
```

**Quote / demo (already live on frontend):**

```text
/products/{slug}/quote  →  loads context via slug → itemCode for ERP Lead
/products/{slug}/demo   →  only if productType=software OR showDemoCta=1
```

---

## 2. Control fields (routing & page behaviour)

These ERPNext fields decide **where** and **how** a record appears. Add to **Website Product** main DocType.

| ERPNext field | Type | Frontend / URL effect |
|---------------|------|------------------------|
| `slug` | Data | URL key: `/products/{slug}` or `/software/{slug}` |
| `published` | Check | `0` → API returns 404; not on listings |
| `product_type` | Select | Maps to `productType` — see §3 |
| `division` | Select | Listing filter: Industrial / Retail / Software |
| `page_mode` | Select | `full` · `minimal` · `external` — see §4 |
| `is_hub` | Check | Hub layout (e.g. AutoID); uses `hub_products` |
| `show_on_products_list` | Check | Include on `/products` catalogue |
| `show_on_software_list` | Check | Include on `/software` catalogue |
| `featured` | Check | Homepage featured products (with `featured_sort_order`) |
| `featured_sort_order` | Int | Lower = higher on homepage |
| `software_demo_enabled` | Check | Allow `/products/{slug}/demo` (default 1 for Software) |

**Canonical URL rule (API builds this):**

| Condition | `canonicalPath` |
|-----------|-----------------|
| `product_type` = Software | `/software/{slug}` |
| `is_hub` = 1 | `/products/{slug}` |
| Otherwise | `/products/{slug}` |

**Breadcrumb root:**

| `product_type` | `breadcrumbRoot` |
|----------------|------------------|
| Software | `{ label: "Software", href: "/software" }` |
| Other | `{ label: "Products", href: "/products" }` |

---

## 3. `product_type` enum mapping

| ERPNext `product_type` | Frontend `productType` | Typical use |
|------------------------|------------------------|-------------|
| `Industrial` | `industrial` | Hitachi, REA JET |
| `Retail Hardware` | `retail_hardware` | Datalogic, scales |
| `Software` | `software` | Modern POS, ERPNext |
| `Generic` | `generic` | Hubs, misc. |

API must emit **lowercase snake** values exactly as above.

---

## 4. `page_mode` behaviour

| ERPNext `page_mode` | Frontend behaviour |
|---------------------|-------------------|
| **`full`** | Return complete `ProductPageContent`; render `ProductPageView` |
| **`minimal`** | Return short payload; frontend renders minimal stub (summary + CTAs) until full content ready |
| **`external`** | Listing card only; `href` = `external_url`; no detail page |

**Minimal mode API minimum fields:**

```json
{
  "slug": "erpnext",
  "productType": "software",
  "pageMode": "minimal",
  "displayName": "ERPNext",
  "brand": "Printechs",
  "category": "ERP & Business Automation",
  "shortDescription": "...",
  "longDescription": "...",
  "heroImage": { "src": "...", "alt": "..." },
  "canonicalPath": "/software/erpnext",
  "breadcrumbRoot": { "label": "Software", "href": "/software" },
  "seo": { "title": "...", "description": "...", "canonicalPath": "/software/erpnext" }
}
```

---

## 5. Main DocType → `ProductPageContent` field map

| ERPNext field | Frontend property | Transform / notes |
|---------------|-------------------|-------------------|
| `slug` | `slug` | As stored |
| `product_type` | `productType` | See §3 |
| `display_name` | `displayName` | Hero H1 |
| `item` → `item_code` | `itemCode` | From linked Item; omit if empty |
| `brand` / `brand_name` | `brand` | Display string |
| Website Brand.`slug` | `brandSlug` | For logo lookup |
| `category` | `category` | |
| `subcategory` | `subcategory` | Optional |
| `category_label` | `categoryLabel` | Hero eyebrow (uppercase on UI) |
| `tagline` | `tagline` | |
| `short_description` | `shortDescription` | Hero paragraph |
| `long_description` | `longDescription` | HTML/plain → split on `\n\n` for paragraphs |
| `hero_image` | `heroImage.src` | Absolute URL: `/files/...` |
| `hero_image_alt` | `heroImage.alt` | |
| — | `heroImage.width` | Default `1200` |
| — | `heroImage.height` | Default `1200` |
| `gallery_image_1…3` | `gallery[]` | Array of `{ src, alt }` |
| `video_url` | `videoUrl` | Optional YouTube/hosted URL |
| `hero_trust_chips` | `heroTrustChips` | Split lines → string array |
| `primary_download_label` + `primary_download_file` | `primaryDownload` | `{ label, href, type: "datasheet" }` |
| `show_demo_cta` or `software_demo_enabled` | `showDemoCta` | Boolean |
| `story_heading` | `storyHeading` | Overview section title |
| `collapsible_full_specs` | `collapsibleFullSpecs` | Default `true` |
| `final_cta_heading` | `finalCta.heading` | |
| `final_cta_description` | `finalCta.description` | |
| `meta_title` | `seo.title` | Fallback: `{displayName} \| Printechs` |
| `meta_description` | `seo.description` | Fallback: `short_description` |
| `index_page` | `seo.indexPage` | Default `true` |
| — | `seo.canonicalPath` | Same as `canonicalPath` |
| — | `canonicalPath` | See §2 |
| — | `breadcrumbRoot` | See §2 |
| `card_title` | *(listing only)* | Catalogue card title; API list endpoint |
| `card_brand_label` | *(listing only)* | Card eyebrow |
| `card_summary` | *(listing only)* | Falls back to `short_description` |
| `card_image` | *(listing only)* | Falls back to `hero_image` |

**Fields used internally but not on full page UI today:** `features[]`, `keySpecifications[]`, `trustIndicators[]`, `applications[]`, `supportServices[]` — may be omitted from API or kept for future SEO/PDF export.

---

## 6. Child tables → nested JSON

### 6.1 `benefits` → `keyValueCards[]`

| ERPNext (Website Product Benefit) | Frontend |
|-----------------------------------|----------|
| `icon` | `icon` (ProductIconKey) |
| `title` | `title` |
| `description` | `description` |
| `sort_order` | Array sort |

**Section hidden if:** array empty.

---

### 6.2 Visual story → `visualStory`

| ERPNext | Frontend |
|---------|----------|
| `visual_story_heading` | `visualStory.heading` |
| `visual_story_items[].label` | `items[].label` |
| `visual_story_items[].image` | `items[].image.src` |
| `visual_story_items[].image_alt` | `items[].image.alt` |
| `visual_story_items[].caption` | `items[].caption` |
| `visual_story_items[].name` or row index | `items[].id` |

**Section hidden if:** no items.

---

### 6.3 `icon_specifications` → `iconSpecifications[]`

| ERPNext (Website Product Icon Spec) | Frontend |
|-------------------------------------|----------|
| `icon` | `icon` |
| `title` | `title` |
| `description` | `description` |

---

### 6.4 `full_specifications` → `fullSpecifications[]`

| ERPNext (Website Product Spec Group) | Frontend |
|--------------------------------------|----------|
| `group_title` | `title` |
| Child `spec_items[].label` | `items[].label` |
| Child `spec_items[].value` | `items[].value` |

---

### 6.5 `applications` → `applicationCards[]`

| ERPNext (Website Product Application) | Frontend |
|---------------------------------------|----------|
| `title` | `title` |
| `description` | `description` |
| `image` | `image.src` |
| `image_alt` | `image.alt` |
| `industry_link` → Website Industry.`slug` | `href` = `/industries/{slug}` |

**Alternative:** main field `industry_slugs` (Table MultiSelect) → `industrySlugs[]` for resolver only (frontend can auto-build cards from Industry master — Phase B2).

---

### 6.6 Ecosystem → `ecosystemItems[]`

Prefer single child table **`ecosystem_items`** (merged accessories + compatible).

| ERPNext (Website Product Ecosystem Item) | Frontend |
|------------------------------------------|----------|
| `related_website_product` → slug | `slug` |
| `display_name_override` or linked `display_name` | `name` |
| `summary_override` or linked summary | `summary` |
| — | `href` = `/products/{slug}` or `/software/{slug}` per linked record type |
| Linked `hero_image` | `image` |

**Legacy split (if kept):** `accessories[]` + `compatibleHardware[]` — frontend merges into `ecosystemItems`.

---

### 6.7 `support_items` → `supportServiceItems[]`

| ERPNext | Frontend |
|---------|----------|
| `icon` | `icon` |
| `title` | `title` |
| `description` | `description` |

---

### 6.8 Software-only → `capabilityModules[]` / `softwareCapabilities[]`

| ERPNext child (optional Phase B1) | Frontend |
|-----------------------------------|----------|
| Website Product Capability Module | `capabilityModules[]` `{ icon, title, items[] }` |
| Website Product Capability Line | `items[]` under module |
| Simple text lines child table | `softwareCapabilities[]` string array |

Use **modules** for Modern POS-style pages; **capabilities** for simple bullet grids.

---

### 6.9 `downloads` → `downloads[]`

| ERPNext | Frontend |
|---------|----------|
| `label` | `label` |
| `file` | `href` |
| `download_type` | `type`: `datasheet` \| `brochure` \| `manual` \| `other` |

---

### 6.10 `package_contents` → `packageContents[]`

| ERPNext (Website Product Package Line) | Frontend |
|----------------------------------------|----------|
| `item_description` | string in array |

---

### 6.11 `related_products` → `relatedProducts[]`

| ERPNext | Frontend |
|---------|----------|
| `related_website_product` | `slug`, `name`, `summary`, `href`, `image` (same as ecosystem) |

---

### 6.12 Hub products → `hubProductSlugs` (listing API only)

| ERPNext | Frontend catalogue `Product` type |
|---------|-----------------------------------|
| `is_hub` = 1 | `hubProductSlugs: string[]` from `hub_products` links |

Detail hub page: frontend custom route `/products/autoid-solutions` **or** generic hub template driven by `is_hub` (future).

---

## 7. Icon select → `ProductIconKey`

ERPNext Select values must match exactly (lowercase):

```text
speed, lines, shield, integration, battery, scan, android, checkout,
inventory, store, loyalty, install, consumables, maintenance, training,
display, connectivity, durability, zatca, cloud, report, device, rugged, print
```

Invalid icon → omit icon; card still renders.

---

## 8. API endpoints & response shapes

### 8.1 Single product (detail page)

```http
GET /api/method/printechs_digital.api.website.get_product?slug=hitachi-ux-d161
```

**Response:**

```json
{
  "page": { /* ProductPageContent — full §5–§6 */ },
  "brand": {
    "slug": "hitachi",
    "name": "Hitachi",
    "logo": { "src": "/files/brand-hitachi.png", "alt": "Hitachi" }
  },
  "linkedIndustries": [
    { "slug": "dairy", "name": "Dairy", "summary": "...", "image": { "src": "...", "alt": "..." } }
  ]
}
```

Maps directly to frontend `ResolvedProductPage`:

```typescript
// frontend/printechs-web/src/lib/product-service.ts
export type ResolvedProductPage = {
  page: ProductPageContent;
  brand?: Brand;
  linkedIndustries: Industry[];
};
```

---

### 8.2 Product catalogue (listings)

```http
GET /api/method/printechs_digital.api.website.list_products?division=Industrial&brand=Hitachi
```

**Response item (maps to frontend `Product`):**

```json
{
  "id": "prod-hitachi-ux-d161",
  "slug": "hitachi-ux-d161",
  "name": "UX-D161W",
  "brand": "Hitachi",
  "summary": "Continuous inkjet coder...",
  "category": "Coding & Marking",
  "division": "industrial",
  "image": { "src": "...", "alt": "..." },
  "hubProductSlugs": null,
  "seo": { "title": "...", "description": "...", "canonicalPath": "/products/hitachi-ux-d161" }
}
```

| ERPNext filter | Query param |
|----------------|-------------|
| `show_on_products_list` = 1 | Default for `/products` |
| `show_on_software_list` = 1 | `/software` listing |
| `division` | `division=Industrial|Retail|Software` |
| `brand` | `brand=Hitachi` |
| `published` = 1 | Always required |

---

### 8.3 Featured products (homepage)

```http
GET /api/method/printechs_digital.api.website.get_featured_products
```

Returns max 4 where `featured` = 1, ordered by `featured_sort_order`.

---

### 8.4 Quote context (for ERP Lead — optional dedicated endpoint)

```http
GET /api/method/printechs_digital.api.website.get_quote_context?slug=hitachi-ux-d161
```

**Response (maps to `LeadContext`):**

```json
{
  "productSlug": "hitachi-ux-d161",
  "product": "Hitachi UX-D161W",
  "code": "IND.SYS.HIJ.1995",
  "brand": "Hitachi",
  "category": "Coding & Marking",
  "sourceUrl": "/products/hitachi-ux-d161",
  "websiteProduct": "WP-2026-00001",
  "item": "IND.SYS.HIJ.1995"
}
```

Frontend already submits `productSlug` + `code` to `/api/leads`; ERPNext Lead hook should resolve **Item** from `code` or Website Product link.

---

## 9. Software vs hardware — same DocType, different flags

| Aspect | Industrial / Retail | Software |
|--------|---------------------|----------|
| ERPNext `product_type` | Industrial / Retail Hardware | Software |
| Item link | **Recommended** | Usually **empty** |
| Detail URL | `/products/{slug}` | `/software/{slug}` |
| Listing | `/products` | `/software` |
| Demo route | Only if `show_demo_cta` | `/products/{slug}/demo` if `software_demo_enabled` |
| Typical extra sections | iconSpecifications, fullSpecifications, packageContents | capabilityModules, softwareCapabilities |
| Hero image ratio | 1:1 (1200×1200) | 16:10 (1600×1000) optional |

**Both use the same `ProductPageView` component** — sections show/hide by data.

---

## 10. Frontend loader strategy (when you go live)

```typescript
// product-service.ts — target implementation
export async function resolveProductPage(slug: string) {
  // 1. Try ERPNext API
  const fromErp = await fetchProductFromErp(slug);
  if (fromErp) return fromErp;

  // 2. Fallback to mock during migration
  return resolveProductPageMock(slug);
}
```

Migrate slug-by-slug; remove mock entry when ERP record is published.

---

## 11. ERPNext implementation checklist

- [ ] Create DocTypes per [WEBSITE_PRODUCT_DOCTYPE.md](./WEBSITE_PRODUCT_DOCTYPE.md)
- [ ] Add `page_mode`, `show_on_products_list`, `show_on_software_list`, `software_demo_enabled`
- [ ] Whitelist `get_product`, `list_products`, `get_featured_products` (guest read, published only)
- [ ] Image fields return full `/files/...` URLs (or CDN base from site config)
- [ ] Import **Hitachi UX-D161W** as validation record
- [ ] Compare API JSON to mock: `product-pages.ts` → `hitachi-ux-d161`
- [ ] Wire Lead creation from `/api/leads` → ERPNext (Phase B3)
- [ ] Purchase role permissions on Website Product only

---

## 12. Example: Hitachi UX-D161W key mappings

| ERPNext | Frontend (current mock) |
|---------|-------------------------|
| `slug` = `hitachi-ux-d161` | `slug` |
| `item` → `IND.SYS.HIJ.1995` | `itemCode` |
| `display_name` = `Hitachi UX-D161W` | `displayName` |
| `product_type` = Industrial | `productType: "industrial"` |
| `category_label` = `CONTINUOUS INKJET PRINTER` | `categoryLabel` |
| 4 × benefits child rows | `keyValueCards[4]` |
| 4 × visual story items | `visualStory.items[4]` |
| 6 × icon specifications | `iconSpecifications[6]` |
| 5 × spec groups | `fullSpecifications[5]` |
| 4 × application cards | `applicationCards[4]` |
| 2 × ecosystem items | `ecosystemItems[2]` |
| Quote URL | `/products/hitachi-ux-d161/quote` |

---

## 13. Related documents

| Document | Path |
|----------|------|
| DocType field spec | `docs/WEBSITE_PRODUCT_DOCTYPE.md` |
| TypeScript contract | `frontend/printechs-web/src/types/content.ts` |
| Mock data (migration source) | `frontend/printechs-web/src/data/product-pages.ts` |
| Quote context helper | `frontend/printechs-web/src/lib/product-quote-context.ts` |
| Lead submission shape | `frontend/printechs-web/src/types/lead.ts` |

---

*Document version: 1.0 — aligned with Option A product-scoped quote/demo and software `page_mode` design.*
