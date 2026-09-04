import type { QuoteConfiguration } from "@/types/quote-config";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

const erpBase =
  process.env.ERPNEXT_URL || process.env.NEXT_PUBLIC_ERPNEXT_URL || "https://printechs.com";

async function fetchConfiguration(
  method: string,
  slug: string,
): Promise<QuoteConfiguration | null> {
  const url = new URL(`/api/method/${method}`, erpBase);
  url.searchParams.set("slug", slug);

  try {
    const response = await fetch(url.toString(), {
      headers: { Accept: "application/json" },
      next: { revalidate: REVALIDATE_SECONDS },
    });
    if (!response.ok) return null;
    const payload = (await response.json()) as { message?: QuoteConfiguration };
    return payload.message ?? null;
  } catch {
    return null;
  }
}

export function fetchQuoteConfiguration(slug: string) {
  return fetchConfiguration("printechs_digital.api.quote.get_quote_configuration", slug);
}

export function fetchDemoConfiguration(slug: string) {
  return fetchConfiguration("printechs_digital.api.quote.get_demo_configuration", slug);
}

export function slugFromSourceUrl(url?: string): string | undefined {
  if (!url) return undefined;
  const match = url.match(/\/(?:products|software)\/([^/?#]+)/);
  return match?.[1];
}
