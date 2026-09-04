"use client";

import { useState } from "react";
import type { LeadSubmission, LeadSubmissionResult } from "@/types/lead";
import { apiPath } from "@/lib/api-path";
import { Button } from "@/components/ui/Button";

type UseLeadFormOptions = {
  type: LeadSubmission["type"];
  initialContext?: LeadSubmission["context"];
};

export function useLeadForm({ type, initialContext }: UseLeadFormOptions) {
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState<LeadSubmissionResult | null>(null);
  const [formError, setFormError] = useState<string | null>(null);

  async function submit(formData: FormData) {
    setSubmitting(true);
    setFormError(null);
    setErrors({});

    const configuration =
      String(formData.get("configuration") ?? "") || undefined;

    const payload: LeadSubmission = {
      type,
      name: String(formData.get("name") ?? ""),
      company: String(formData.get("company") ?? ""),
      email: String(formData.get("email") ?? ""),
      phone: String(formData.get("phone") ?? ""),
      message: String(formData.get("message") ?? "") || undefined,
      context: {
        ...initialContext,
        productSlug:
          String(formData.get("productSlug") ?? initialContext?.productSlug ?? "") ||
          undefined,
        solutionSlug:
          String(formData.get("solutionSlug") ?? initialContext?.solutionSlug ?? "") ||
          undefined,
        product: String(formData.get("product") ?? initialContext?.product ?? "") || undefined,
        code: String(formData.get("code") ?? initialContext?.code ?? "") || undefined,
        brand: String(formData.get("brand") ?? initialContext?.brand ?? "") || undefined,
        category: String(formData.get("category") ?? initialContext?.category ?? "") || undefined,
        sourceUrl:
          String(formData.get("sourceUrl") ?? initialContext?.sourceUrl ?? "") || undefined,
        preferredTime: String(formData.get("preferredTime") ?? "") || undefined,
        inquiryType: String(formData.get("inquiryType") ?? "") || undefined,
        preferredContactMethod:
          String(formData.get("preferredContactMethod") ?? "") || undefined,
        configuration,
      },
    };

    try {
      const response = await fetch(apiPath("/api/leads"), {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = (await response.json()) as
        | LeadSubmissionResult
        | { ok: false; errors?: Record<string, string>; message?: string };

      if (!response.ok) {
        if ("errors" in data && data.errors) {
          setErrors(data.errors);
        } else {
          setFormError(
            "message" in data && data.message
              ? data.message
              : "Something went wrong. Please try again.",
          );
        }
        return;
      }

      setResult(data as LeadSubmissionResult);
    } catch {
      setFormError("Unable to submit right now. Please try again or email us directly.");
    } finally {
      setSubmitting(false);
    }
  }

  return { submit, errors, submitting, result, formError, setFormError };
}

type LeadFormSuccessProps = {
  title: string;
  description: string;
  reference?: string;
  backHref?: string;
  backLabel?: string;
};

export function LeadFormSuccess({
  title,
  description,
  reference,
  backHref,
  backLabel,
}: LeadFormSuccessProps) {
  return (
    <div className="rounded-sm border border-signal/25 bg-signal/5 p-8">
      <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
        Request received
      </p>
      <h2 className="mt-2 font-display text-2xl font-semibold text-ink">{title}</h2>
      <p className="mt-3 max-w-xl text-base leading-relaxed text-slate">{description}</p>
      {reference ? (
        <p className="mt-4 text-sm text-slate">
          Reference: <span className="font-mono font-semibold text-ink">{reference}</span>
        </p>
      ) : null}
      <div className="mt-8 flex flex-wrap gap-3">
        {backHref ? (
          <Button href={backHref} variant="primary">
            Back to {backLabel || "product"}
          </Button>
        ) : (
          <Button href="/" variant="primary">
            Back to homepage
          </Button>
        )}
        <Button href="/contact" variant="ghost">
          Contact Printechs
        </Button>
      </div>
    </div>
  );
}

type SubmitButtonProps = {
  label: string;
  submitting: boolean;
};

export function SubmitButton({ label, submitting }: SubmitButtonProps) {
  return (
    <button
      type="submit"
      disabled={submitting}
      className="inline-flex min-h-11 items-center justify-center rounded-sm bg-signal px-6 py-2.5 text-sm font-semibold tracking-wide text-white shadow-soft transition duration-300 ease-premium hover:bg-signal-bright focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-60"
    >
      {submitting ? "Sending…" : label}
    </button>
  );
}
