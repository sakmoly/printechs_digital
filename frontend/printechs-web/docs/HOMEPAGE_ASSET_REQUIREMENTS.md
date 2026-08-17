# Homepage Asset Requirements

Media paths are configured in `src/data/*`. Replace files under `public/images/` without changing component code when possible.

| Section | Asset | Aspect | Recommended size | Current file | Notes |
|---------|-------|--------|------------------|--------------|-------|
| Hero | Cinematic still or loop | 16:9 | 1920×1080 | `placeholders/hero-industrial.svg` | Prefer muted hosted loop later |
| Divisions | Industrial panel | 4:3 | 1200×900 | `placeholders/division-industrial.svg` | Production / coding context |
| Divisions | Retail panel | 4:3 | 1200×900 | `placeholders/division-retail.svg` | Store / mobility context |
| Divisions | Software panel | 4:3 | 1200×900 | `placeholders/division-software.svg` | UI / platform context |
| Solutions | Card visuals ×4 | 16:10 | 1200×750 | `placeholders/solution.svg` | One per featured solution |
| Products | Product visuals ×4 | 1:1 | 1200×1200 | `placeholders/product.svg` | Exact model photos only |
| Software | UI screenshots ×6 | 16:10 | 1600×1000 | `placeholders/software.svg` | Clearly labelled per product |
| Industries | Card visuals ×12 | 3:2 | 1200×800 | `placeholders/industry.svg` | Sector photography |
| Partners | Brand logos ×6 | SVG | — | `placeholders/brand.svg` | Official artwork only |
| Case studies | Covers ×2 | 16:9 | 1600×900 | `placeholders/case-study.svg` | Anonymised story imagery |
| Video | Poster | 16:9 | 1920×1080 | `placeholders/video-poster.svg` | Used before player load |

## Replacement instructions

1. Drop the real file into the matching `public/images/...` folder.
2. Update the `src` in the relevant mock-data record.
3. Keep `alt` text accurate and non-promotional.
4. Do not substitute one product model for another.
