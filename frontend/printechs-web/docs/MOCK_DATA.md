# Mock Data

Location: `src/data/`

| Dataset | File | Purpose |
|---------|------|---------|
| Hero | `hero.ts` | Homepage hero copy + media config |
| Divisions | `divisions.ts` | Industrial / Retail / Software |
| Products | `products.ts` | Representative physical products |
| Software | `software.ts` | Dedicated software catalogue |
| Industries | `industries.ts` | Industry landing records |
| Solutions | `solutions.ts` | Solution records |
| Brands | `brands.ts` | Partner brands |
| Case studies | `case-studies.ts` | Outcome stories |
| Videos | `videos.ts` | YouTube / hosted video records |

Types live in `src/types/content.ts`.

Rules:

- No pricing fields
- No stock / valuation / supplier / customer financial data
- Content stays outside presentational components
- Future ERPNext responses should map 1:1 onto these interfaces
