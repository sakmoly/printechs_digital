import type { LeadAttribution } from "@/lib/analytics/types";

const STORAGE_KEY = "printechs_attribution_v1";
const UTM_KEYS = [
  "utm_source",
  "utm_medium",
  "utm_campaign",
  "utm_content",
  "utm_term",
] as const;

type StoredAttribution = LeadAttribution;

function readStored(): StoredAttribution | null {
  if (typeof window === "undefined") return null;
  try {
    const raw = window.sessionStorage.getItem(STORAGE_KEY);
    return raw ? (JSON.parse(raw) as StoredAttribution) : null;
  } catch {
    return null;
  }
}

function writeStored(value: StoredAttribution) {
  if (typeof window === "undefined") return;
  try {
    window.sessionStorage.setItem(STORAGE_KEY, JSON.stringify(value));
  } catch {
    // Ignore quota errors.
  }
}

export function captureAttributionFromUrl(url: URL) {
  if (typeof window === "undefined") return;

  const existing = readStored() ?? {};
  const next: StoredAttribution = { ...existing };
  let changed = false;

  for (const key of UTM_KEYS) {
    const value = url.searchParams.get(key)?.trim();
    if (value) {
      next[key] = value;
      changed = true;
    }
  }

  if (!next.landing_page) {
    next.landing_page = `${url.pathname}${url.search}`;
    changed = true;
  }

  if (!next.referrer && document.referrer) {
    next.referrer = document.referrer;
    changed = true;
  }

  if (!next.first_visit_at) {
    next.first_visit_at = new Date().toISOString();
    changed = true;
  }

  if (changed) {
    writeStored(next);
  }
}

export function getLeadAttribution(): LeadAttribution {
  return readStored() ?? {};
}

export function getUtmParams(): LeadAttribution {
  const stored = readStored() ?? {};
  return {
    utm_source: stored.utm_source,
    utm_medium: stored.utm_medium,
    utm_campaign: stored.utm_campaign,
    utm_content: stored.utm_content,
    utm_term: stored.utm_term,
  };
}
