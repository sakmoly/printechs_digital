"use client";

import type { LeadContext } from "@/types/lead";
import { TextArea, TextInput } from "@/components/forms/FormField";
import { LeadFormSuccess, SubmitButton, useLeadForm } from "@/components/forms/LeadForm";

type DemoRequestFormProps = {
  context?: LeadContext;
};

export function DemoRequestForm({ context }: DemoRequestFormProps) {
  const { submit, errors, submitting, result, formError } = useLeadForm({
    type: "demo",
    initialContext: context,
  });

  if (result) {
    return (
      <LeadFormSuccess
        title="Demo request received"
        description="Thank you. Our software team will contact you to schedule a demonstration tailored to your retail or enterprise environment."
        reference={result.reference}
      />
    );
  }

  return (
    <form
      className="space-y-5"
      noValidate
      onSubmit={(event) => {
        event.preventDefault();
        void submit(new FormData(event.currentTarget));
      }}
    >
      {context?.product ? (
        <div className="rounded-sm border border-line bg-mist p-5">
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
            Software interest
          </p>
          <p className="mt-2 font-display text-lg font-semibold text-ink">{context.product}</p>
        </div>
      ) : null}

      <div className="grid gap-5 sm:grid-cols-2">
        <TextInput label="Full name" name="name" autoComplete="name" required error={errors.name} />
        <TextInput
          label="Company"
          name="company"
          autoComplete="organization"
          required
          error={errors.company}
        />
        <TextInput
          label="Work email"
          name="email"
          type="email"
          autoComplete="email"
          required
          error={errors.email}
        />
        <TextInput
          label="Phone / WhatsApp"
          name="phone"
          type="tel"
          autoComplete="tel"
          required
          error={errors.phone}
        />
      </div>

      <TextInput
        label="Preferred demo time"
        name="preferredTime"
        error={errors.preferredTime}
        hint="Optional — your timezone, preferred days, or availability."
        placeholder="e.g. Sun–Thu, 10:00–14:00 AST"
      />

      <TextArea
        label="What would you like to see?"
        name="message"
        error={errors.message}
        placeholder="Store count, POS setup, ERP integration, ZATCA, WMS, or other topics…"
      />

      {context?.productSlug ? (
        <input type="hidden" name="productSlug" value={context.productSlug} />
      ) : null}
      {context?.product ? <input type="hidden" name="product" value={context.product} /> : null}
      {context?.sourceUrl ? (
        <input type="hidden" name="sourceUrl" value={context.sourceUrl} />
      ) : null}

      {formError ? (
        <p className="text-sm font-medium text-accent" role="alert">
          {formError}
        </p>
      ) : null}

      <SubmitButton label="Request demo" submitting={submitting} />
    </form>
  );
}
