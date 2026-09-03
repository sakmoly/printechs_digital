# Website Product — ERPNext DocType Specification

**Status:** Approved approach — separate DocType (coexists with legacy Website Item)  
**App:** `printechs_digital`  
**Site:** `demo` (development) → production when approved  
**Maintained by:** Printechs **Purchase** role  
**Frontend reference:** `ProductPageContent` in `frontend/printechs-web/src/types/content.ts`  
**Live template:** [Hitachi UX-D161W](https://printechs.com/newwebsite/products/hitachi-ux-d161)

---

## 0. Why a new DocType (not extend Website Item)

| Concern | Decision |
|---------|----------|
| Current Frappe shop uses **Website Item** (Webshop app) | **Leave unchanged** — old site keeps working |
| New Next.js site needs rich structured sections | **Website Product** — matches `ProductPageContent` |
| Risk of breaking existing website | **No custom fields on Website Item** |
| Purchase team workflow | **Item → Create Website Product** button (separate from “View Website Item”) |
| Quote integration | Website Product links to same **Item** (`item_code`) |
| Migration | Optional one-time copy from Website Item via `website_item_reference` |

**Item form buttons (both can appear):**

| Button | App | Purpose |
|--------|-----|---------|
| Publish in Website / View Website Item | Webshop | Legacy Frappe shop |
| **Create Website Product / View Website Product** | printechs_digital | New Next.js site (`/newwebsite`) |

**Implementation:** `printechs_digital/public/js/item.js` + `make_website_product()` in `website_product.py`.

---

## 1. Purpose

Enable Purchase team members to create and maintain up to **~100 marketing product pages** across Industrial, Retail, and Software divisions **without developer involvement**, while keeping ERP **Item** master data separate from website marketing content.

**Design principle:** One Website Product record = one public URL (`/products/{slug}`). Empty optional sections are hidden on the website (same behaviour as the Hitachi page today).

---

## 2. Why not use standard Item?

| Standard Item | Website Product |
|---------------|-----------------|
| Inventory, pricing, suppliers | Marketing copy, hero, specs, applications |
| Used by sales/purchase/stock | Used by public website |
| Wrong shape for rich page sections | Matches approved product page template |

**Optional link:** Website Product → Item (for item code on quotes, e.g. `IND.SYS.HIJ.1995`).

---

## 3. DocTypes overview

| DocType | Type | Purpose |
|---------|------|---------|
| **Website Product** | Main | Full product marketing page |
| **Website Product Benefit** | Child table | Hero benefit icon cards |
| **Website Product Visual Story Item** | Child table | “In action” gallery tabs |
| **Website Product Icon Spec** | Child table | Technical highlight icons |
| **Website Product Spec Group** | Child table | Full specifications (group header) |
| **Website Product Spec Item** | Child table | Spec rows within a group |
| **Website Product Application** | Child table | Application industry cards |
| **Website Product Ecosystem Item** | Child table | Compatible products / accessories |
| **Website Product Support Item** | Child table | Services & support cards |
| **Website Product Download** | Child table | Datasheets, brochures |
| **Website Product Package Line** | Child table | What’s included list |
| **Website Product Related** | Child table | Related products |
| **Website Brand** | Main | Brand name, slug, logo (separate spec — Phase B1) |

**Phase B1 scope:** Website Product + child tables only.  
**Phase B2:** Website Brand, Website Solution, Website Industry, Website Software (same pattern).

---

## 4. Website Product — main fields

### 4.1 Identity & publishing

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `name` | Data | Auto | ERPNext doc name; suggest `{brand}-{model}` |
| `website_product_name` | Data | Yes | Internal title for Purchase team |
| `slug` | Data | Yes | URL segment, unique, lowercase-hyphen (e.g. `hitachi-ux-d161`) |
| `published` | Check | Yes | Default 0; only published records appear on API |
| `featured` | Check | No | Include in homepage featured products (max 4 controlled in frontend or sort order) |
| `featured_sort_order` | Int | No | Lower = higher priority on homepage |
| `product_type` | Select | Yes | `Industrial` · `Retail Hardware` · `Software` · `Generic` |
| `division` | Select | Yes | `Industrial` · `Retail` · `Software` |
| `is_hub` | Check | No | Category hub page (e.g. AutoID Solutions) |
| `hub_products` | Table MultiSelect | No | Links to other Website Product records when `is_hub` = 1 |

### 4.2 ERP link (optional)

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `item` | Link → Item | No | Optional ERP item for quote integration |
| `item_code` | Data | Read only | Fetched from Item; shown on product page |
| `show_item_code_on_website` | Check | No | Default 1 for industrial products |

### 4.3 Brand & category

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `brand` | Link → Website Brand | Yes | Or Data if Brand DocType delayed |
| `brand_name` | Data | Read only | Display name |
| `category` | Data | Yes | e.g. `Coding & Marking` |
| `subcategory` | Data | No | e.g. `Continuous Inkjet` |
| `category_label` | Data | No | Hero eyebrow, ALL CAPS style (e.g. `CONTINUOUS INKJET PRINTER`) |

### 4.4 Hero section

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `display_name` | Data | Yes | Public H1 (e.g. `Hitachi UX-D161W`) |
| `tagline` | Data | No | Short line under title |
| `short_description` | Text | Yes | Hero paragraph (~2 lines) |
| `hero_image` | Attach Image | Yes | 1200×1200 recommended |
| `hero_image_alt` | Data | Yes | Accessibility |
| `gallery_image_1` … `gallery_image_3` | Attach Image | No | Optional hero thumbnails |
| `hero_trust_chips` | Small Text | No | One chip per line (max 5) |
| `primary_download_label` | Data | No | e.g. `Download Datasheet` |
| `primary_download_file` | Attach | No | PDF |
| `show_demo_cta` | Check | No | Software products only |

### 4.5 Product overview

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `story_heading` | Data | No | Default: `Built for production line coding` |
| `long_description` | Text Editor | Yes | Supports paragraphs; `\n\n` = new paragraph on website |
| `show_printechs_support_line` | Check | No | Default 1 — “Supplied and supported by Printechs…” |

### 4.6 Child tables (sections)

| Table field | Child DocType | Maps to frontend section |
|-------------|---------------|--------------------------|
| `benefits` | Website Product Benefit | Benefit icon cards below hero |
| `visual_story_items` | Website Product Visual Story Item | “In action” gallery |
| `visual_story_heading` | Data (main) | e.g. `See the print quality` |
| `icon_specifications` | Website Product Icon Spec | Technical highlights grid |
| `full_specifications` | Website Product Spec Group + Spec Item | Collapsible full specs |
| `collapsible_full_specs` | Check (main) | Default 1 |
| `applications` | Website Product Application | Application cards |
| `ecosystem_items` | Website Product Ecosystem Item | Compatible products strip |
| `support_items` | Website Product Support Item | Services & support |
| `downloads` | Website Product Download | Resources section |
| `package_contents` | Website Product Package Line | What’s included |
| `related_products` | Website Product Related | You may also consider |

**Rule:** If a child table is empty, that website section is **not rendered**.

### 4.7 Final CTA & SEO

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `final_cta_heading` | Data | No | Default from template |
| `final_cta_description` | Text | No | |
| `meta_title` | Data | No | Falls back to `{display_name} \| Printechs` |
| `meta_description` | Text | No | Falls back to `short_description` |
| `canonical_path` | Data | Read only | Auto: `/products/{slug}` |
| `index_page` | Check | No | Default 1; allow noindex for drafts |

### 4.8 Listing / catalogue card (homepage & grids)

| Field | Field type | Required | Notes |
|-------|------------|----------|-------|
| `card_title` | Data | No | Short title on cards (e.g. `UX-Series`, `Scale`); falls back to `display_name` |
| `card_brand_label` | Data | No | Eyebrow on card (e.g. `Datalogic / Zebra` for hubs) |
| `card_summary` | Text | No | Falls back to `short_description` |
| `card_image` | Attach Image | No | Falls back to `hero_image` |

---

## 5. Child table field definitions

### Website Product Benefit

| Field | Type | Required |
|-------|------|----------|
| `icon` | Select | No — see icon list §8 |
| `title` | Data | Yes |
| `description` | Text | Yes |
| `sort_order` | Int | No |

### Website Product Visual Story Item

| Field | Type | Required |
|-------|------|----------|
| `label` | Data | Yes — tab button text |
| `image` | Attach Image | Yes |
| `image_alt` | Data | Yes |
| `caption` | Text | No |
| `sort_order` | Int | No |

### Website Product Icon Spec

| Field | Type | Required |
|-------|------|----------|
| `icon` | Select | No |
| `title` | Data | Yes |
| `description` | Text | Yes |
| `sort_order` | Int | No |

### Website Product Spec Group

| Field | Type | Required |
|-------|------|----------|
| `group_title` | Data | Yes |
| `sort_order` | Int | No |
| `spec_items` | Table → Website Product Spec Item | Yes |

### Website Product Spec Item

| Field | Type | Required |
|-------|------|----------|
| `label` | Data | Yes |
| `value` | Data | Yes |

### Website Product Application

| Field | Type | Required |
|-------|------|----------|
| `title` | Data | Yes |
| `description` | Text | Yes |
| `image` | Attach Image | Yes |
| `image_alt` | Data | Yes |
| `industry_link` | Link → Website Industry | No — Phase B2 |
| `sort_order` | Int | No |

### Website Product Ecosystem Item

| Field | Type | Required |
|-------|------|----------|
| `related_website_product` | Link → Website Product | Yes |
| `display_name_override` | Data | No |
| `summary_override` | Text | No |
| `sort_order` | Int | No |

### Website Product Support Item

| Field | Type | Required |
|-------|------|----------|
| `icon` | Select | No |
| `title` | Data | Yes |
| `description` | Text | Yes |
| `sort_order` | Int | No |

### Website Product Download

| Field | Type | Required |
|-------|------|----------|
| `label` | Data | Yes |
| `file` | Attach | Yes |
| `download_type` | Select | No — `Datasheet` · `Brochure` · `Manual` · `Other` |

### Website Product Package Line

| Field | Type | Required |
|-------|------|----------|
| `item_description` | Data | Yes |
| `sort_order` | Int | No |

### Website Product Related

| Field | Type | Required |
|-------|------|----------|
| `related_website_product` | Link → Website Product | Yes |
| `sort_order` | Int | No |

---

## 6. Permissions — Purchase role

| Permission | Purchase | System Manager | Website Manager (optional) |
|------------|----------|----------------|----------------------------|
| Create / edit Website Product | Yes | Yes | Yes |
| Publish / unpublish | Yes | Yes | Yes |
| Delete | No (or Manager only) | Yes | Yes |
| Edit Item master | No | Yes | No |
| Upload attachments | Yes | Yes | Yes |

**Recommended:** Create role **Website Editor** cloned from Purchase with Website Product permissions only, assigned to Purchase team members.

**Workflow (optional Phase B1.5):**

- Draft → Pending Review → Published  
- Purchase saves drafts; Manager publishes (if required)

---

## 7. Public API (Phase B1 — read only)

**Endpoint (whitelisted, guest allowed for published):**

```
GET /api/method/printechs_digital.api.website.get_product?slug=hitachi-ux-d161
GET /api/method/printechs_digital.api.website.list_products?division=Industrial&limit=100
GET /api/method/printechs_digital.api.website.get_featured_products
```

**Response shape:** Must map 1:1 to frontend `ProductPageContent` (see `src/types/content.ts`).

**Rules:**

- Return `404` if not published
- Never expose cost price, supplier, stock from linked Item
- Image URLs as absolute paths to Frappe `/files/...` or CDN
- Cache: 60–300 seconds on API; Next.js ISR on frontend

**Quote integration (Phase B3):**

```
GET /api/method/printechs_digital.api.website.get_quote_context?slug=hitachi-ux-d161
```

Returns: `display_name`, `item_code`, `brand`, `category`, `source_url` for Request Quote form.

---

## 8. Icon select options (shared across child tables)

Match frontend `ProductIconKey`:

```
speed, lines, shield, integration, battery, scan, android, checkout,
inventory, store, loyalty, install, consumables, maintenance, training,
display, connectivity, durability, zatca, cloud, report, device, rugged, print
```

Purchase team picks from dropdown; frontend renders SVG.

---

## 9. Hub products (e.g. AutoID Solutions)

When `is_hub` = 1:

- `display_name` = `AutoID Solutions`
- `card_brand_label` = `Datalogic / Zebra`
- `hub_products` = links to Datalogic + Zebra Website Product records
- Website renders hub template (`/products/autoid-solutions`) instead of standard product layout
- `item` link optional (usually blank for hubs)

---

## 10. Software products

**Option A (recommended):** Same **Website Product** DocType with `product_type` = `Software` and `division` = `Software`.  
**Option B:** Separate **Website Software** DocType — only if fields diverge significantly.

Modern POS page already uses `ProductPageView` with `productType: "software"`. Same DocType works with conditional sections (`capability_modules`, `software_capabilities`, `show_demo_cta`).

---

## 11. Data entry workflow for Purchase team

1. Create **Website Product** → enter `display_name`, `slug`, `brand`, `division`
2. Optionally link **Item** for quote code
3. Upload **hero_image** + fill hero text
4. Add **benefits** child rows (typically 4)
5. Add **visual story** tabs if available
6. Write **long_description**
7. Add **icon specifications** (typically 6)
8. Add **full specifications** groups
9. Add **applications**, **ecosystem**, **support**, **downloads**, **package**
10. Link **related products**
11. Fill **SEO** fields
12. Set **published** = 1

**Estimated time per product:** 30–60 min once datasheets/images are ready.

---

## 12. Migration plan (~100 products)

| Step | Action |
|------|--------|
| 1 | Approve this DocType spec |
| 2 | Implement DocTypes on `demo` |
| 3 | Import **Hitachi UX-D161W** from mock data as validation |
| 4 | Purchase team enters next 5–10 pilot products |
| 5 | Switch frontend `fetchProductPage()` from mock → API for pilot slugs |
| 6 | Bulk import remaining catalogue (CSV or copy from approved datasheets) |
| 7 | Remove mock entries from `product-pages.ts` as each slug goes live on API |

---

## 13. Implementation phases (backend)

| Phase | Deliverable | Depends on |
|-------|-------------|------------|
| **B1a** | Website Product DocType + child tables | This spec approved |
| **B1b** | Public read API + image URLs | B1a |
| **B1c** | Purchase role permissions + desk list views | B1a |
| **B2** | Website Brand, Industry, Solution DocTypes | B1 stable |
| **B3** | Quote form → ERPNext Lead with item context | Contact form design |
| **B4** | Search index across website content | B1 + B2 |

**Do not start B1a until:** Hitachi product page design is signed off (you indicated ~1–2 more review cycles).

---

## 14. Frontend impact (no UI redesign)

Only change data loading in `src/lib/product-service.ts`:

```text
Today:  getProductPage(slug) from product-pages.ts
Later:  GET /api/method/...get_product?slug=...
```

`ProductPageView` and all section components stay unchanged.

---

## 15. Open questions for Printechs approval

Please confirm:

1. **Item link** — Should every industrial product require an Item link, or optional?
2. **Publish workflow** — Can Purchase publish directly, or needs Manager approval?
3. **Software products** — Same DocType (Option A) or separate Website Software?
4. **Featured homepage** — Manual checkbox + sort order, or separate “Featured Products” list DocType?
5. **Hub pages** — Will there be more hubs besides AutoID (e.g. weighing brands)?
6. **Attachments** — Store PDFs in ERPNext only, or also sync to public file storage?

---

## 16. Sign-off

| Role | Name | Date | Approved |
|------|------|------|----------|
| Purchase / Content | | | ☐ |
| Management | | | ☐ |
| Development | | | ☐ |

Once signed off, development starts with **B1a on `demo` site only** — no production changes.

---

*Document version: 1.0 — generated from Hitachi UX-D161W template and `ProductPageContent` interface.*
