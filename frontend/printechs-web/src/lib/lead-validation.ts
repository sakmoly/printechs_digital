import type { LeadSubmission, LeadType } from "@/types/lead";

const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export type LeadValidationResult =
  | { ok: true; data: LeadSubmission }
  | { ok: false; errors: Record<string, string> };

function clean(value: unknown): string {
  return typeof value === "string" ? value.trim() : "";
}

export function validateLeadPayload(body: unknown): LeadValidationResult {
  const errors: Record<string, string> = {};
  const input = (body ?? {}) as Record<string, unknown>;
  const contextInput = (input.context ?? {}) as Record<string, unknown>;

  const type = clean(input.type) as LeadType;
  if (!["quote", "contact", "demo"].includes(type)) {
    errors.type = "Invalid request type.";
  }

  const name = clean(input.name);
  const company = clean(input.company);
  const email = clean(input.email);
  const phone = clean(input.phone);
  const message = clean(input.message);

  if (!name) errors.name = "Name is required.";
  if (!company) errors.company = "Company is required.";
  if (!email) errors.email = "Email is required.";
  else if (!emailPattern.test(email)) errors.email = "Enter a valid email address.";
  if (!phone) errors.phone = "Phone is required.";

  if (type === "contact" && !message) {
    errors.message = "Please tell us how we can help.";
  }

  if (Object.keys(errors).length > 0) {
    return { ok: false, errors };
  }

  return {
    ok: true,
    data: {
      type,
      name,
      company,
      email,
      phone,
      message: message || undefined,
      context: {
        productSlug: clean(contextInput.productSlug) || undefined,
        solutionSlug: clean(contextInput.solutionSlug) || undefined,
        product: clean(contextInput.product) || undefined,
        code: clean(contextInput.code) || undefined,
        brand: clean(contextInput.brand) || undefined,
        category: clean(contextInput.category) || undefined,
        sourceUrl: clean(contextInput.sourceUrl) || undefined,
        preferredTime: clean(contextInput.preferredTime) || undefined,
        inquiryType: clean(contextInput.inquiryType) || undefined,
      },
    },
  };
}
