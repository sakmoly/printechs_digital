"use client";

import { useEffect, useState } from "react";
import type { LeadContext } from "@/types/lead";
import { SelectInput, TextArea, TextInput } from "@/components/forms/FormField";
import { LeadFormSuccess, SubmitButton, useLeadForm } from "@/components/forms/LeadForm";
import { buildWhatsAppQuoteLink } from "@/lib/whatsapp-quote";

const contactMethodOptions = [
  { value: "email", label: "Email" },
  { value: "whatsapp", label: "WhatsApp" },
];

type FollowUpDetails = {
  method: string;
  name: string;
  company: string;
  phone: string;
  email: string;
  message: string;
};

type GeneralQuoteRequestFormProps = {
  context?: LeadContext;
  printechsWhatsAppHref?: string | null;
};

export function GeneralQuoteRequestForm({
  context,
  printechsWhatsAppHref,
}: GeneralQuoteRequestFormProps) {
  const { submit, errors, submitting, result, formError } = useLeadForm({
    type: "quote",
    initialContext: context,
  });
  const [followUp, setFollowUp] = useState<FollowUpDetails | null>(null);
  const [whatsappOpened, setWhatsappOpened] = useState(false);

  const whatsappLink =
    followUp?.method === "whatsapp" && printechsWhatsAppHref
      ? buildWhatsAppQuoteLink(printechsWhatsAppHref, followUp)
      : null;

  useEffect(() => {
    if (!result || !whatsappLink || whatsappOpened) {
      return;
    }

    setWhatsappOpened(true);
    window.location.assign(whatsappLink);
  }, [result, whatsappLink, whatsappOpened]);

  if (result) {
    const viaWhatsApp = followUp?.method === "whatsapp" && Boolean(whatsappLink);

    return (
      <LeadFormSuccess
        title="Quote request received"
        description={
          viaWhatsApp
            ? "Your request is saved in our system. WhatsApp is opening with your details — tap Send to deliver the message to Printechs."
            : `Thank you. A confirmation email was sent to ${followUp?.email || "your inbox"}. Our team will respond with your quote during business hours.`
        }
        reference={result.reference}
      />
    );
  }

  const productName = context?.product;

  return (
    <form
      className="overflow-hidden rounded-sm border border-line bg-white shadow-soft"
      noValidate
      data-analytics-form="quote"
      onSubmit={(event) => {
        event.preventDefault();
        const formData = new FormData(event.currentTarget);
        setFollowUp({
          method: String(formData.get("preferredContactMethod") ?? "email"),
          name: String(formData.get("name") ?? ""),
          company: String(formData.get("company") ?? ""),
          phone: String(formData.get("phone") ?? ""),
          email: String(formData.get("email") ?? ""),
          message: String(formData.get("message") ?? ""),
        });
        setWhatsappOpened(false);
        void submit(formData);
      }}
    >
      {productName ? (
        <div className="flex items-start gap-4 border-b border-line bg-mist px-6 py-5 sm:px-8">
          <span className="mt-1 hidden h-10 w-1 shrink-0 rounded-full bg-signal sm:block" />
          <div>
            <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
              Product context
            </p>
            <p className="mt-2 font-display text-xl font-semibold tracking-tight text-ink">
              {productName}
            </p>
            <p className="mt-1 text-sm text-slate">
              {[context?.brand, context?.category, context?.code].filter(Boolean).join(" · ")}
            </p>
          </div>
        </div>
      ) : null}

      <div className="space-y-6 px-6 py-7 sm:px-8 sm:py-8">
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

        <SelectInput
          label="Preferred contact method"
          name="preferredContactMethod"
          options={contactMethodOptions}
          defaultValue="email"
          required
          error={errors.preferredContactMethod}
          hint="WhatsApp opens automatically after submit so you can send your request to our team."
        />

        <TextArea
          label="What do you need a quote for?"
          name="message"
          required
          error={errors.message}
          placeholder="Products, quantities, location, timeline, or any project details…"
        />

        {context?.product ? <input type="hidden" name="product" value={context.product} /> : null}
        {context?.code ? <input type="hidden" name="code" value={context.code} /> : null}
        {context?.brand ? <input type="hidden" name="brand" value={context.brand} /> : null}
        {context?.category ? <input type="hidden" name="category" value={context.category} /> : null}
        {context?.sourceUrl ? (
          <input type="hidden" name="sourceUrl" value={context.sourceUrl} />
        ) : null}

        {formError ? (
          <p className="text-sm font-medium text-accent" role="alert">
            {formError}
          </p>
        ) : null}

        <div className="flex flex-wrap items-center gap-4 border-t border-line pt-6">
          <SubmitButton label="Submit quote request" submitting={submitting} />
          <p className="text-sm text-slate">No prices on the website — we reply with a formal quote.</p>
        </div>
      </div>
    </form>
  );
}
