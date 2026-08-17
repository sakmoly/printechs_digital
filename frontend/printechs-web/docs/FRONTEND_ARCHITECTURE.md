# Frontend Architecture

Project: `frontend/printechs-web`

Stack:

- Next.js 14 (App Router)
- React 18
- TypeScript
- Tailwind CSS

## Goals

- Frontend-first mockup that can become the production Printechs website
- Typed content models ready for ERPNext API mapping
- Isolation from live Frappe sites (`site1.local` / existing `printechs_website`)

## Structure

```text
src/
  app/           # routes (App Router)
  components/    # UI + section components
  config/        # site navigation and globals
  data/          # typed mock content loaders
  lib/           # shared helpers (SEO, future API clients)
  types/         # content contracts
```

## Content transition plan

Today:

1. Pages import from `src/data/*`
2. Components accept typed props (`Product`, `SoftwareSolution`, etc.)

Later (backend phase):

1. Add API clients in `src/lib/api/`
2. Keep the same TypeScript interfaces
3. Replace data imports with fetchers that return the same shapes from `printechs_digital` on demo

## Non-goals (current phase)

- ERPNext DocTypes / APIs
- Pricing, cart, checkout
- Production Nginx / DNS cutover
- Full detail-page design beyond routing stubs
