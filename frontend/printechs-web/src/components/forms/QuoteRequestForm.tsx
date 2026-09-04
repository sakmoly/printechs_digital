"use client";

import { useState } from "react";
import type { LeadContext } from "@/types/lead";
import type { QuoteConfiguration } from "@/types/quote-config";
import { Button } from "@/components/ui/Button";
import {
  QuoteConfigurationFields,
  formatQuoteConfiguration,
} from "@/components/forms/QuoteConfigurationFields";

const fieldClass =
  "mt-2 w-full rounded-sm border border-line bg-white px-4 py-2.5 text-sm text-ink shadow-sm transition placeholder:text-slate/70 focus-visible:border-product-icon focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-product-icon/20";

type QuoteRequestFormProps = {
  configuration?: QuoteConfiguration;
  context?: LeadContext;
};

export function QuoteRequestForm({ configuration, context }: QuoteRequestFormProps) {
  const productName = configuration?.product || context?.product;
  const brand = configuration?.brand || context?.brand;
  const code = configuration?.code || context?.code;
  const category = configuration?.category || context?.category;
  const [submitting, setSubmitting] = useState(false);
  const [done, setDone] = useState(false);
  const [error, setError] = useState("");

  if (done) {
    return (
      <div className="rounded-sm border border-product-icon/15 bg-white p-8 shadow-soft">
        <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
          Request received
        </p>
        <h2 className="mt-3 font-display text-2xl font-semibold text-ink">
          Quote request received
        </h2>
        <p className="mt-3 max-w-xl text-base leading-relaxed text-slate">
          Our team will review the configuration and respond with pricing and availability.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Button href={configuration?.sourceUrl || "/products"} variant="primary">
            Back to product
          </Button>
          <Button href="/contact" variant="ghost">
            Contact Printechs
          </Button>
        </div>
      </div>
    );
  }

  return (
    <form
      className="overflow-hidden rounded-sm border border-line bg-white shadow-soft"
      noValidate
      onSubmit={(event) => {
        event.preventDefault();
        const form = event.currentTarget;
        const data = new FormData(form);
        const missing = (configuration?.quoteOptions ?? []).filter((option) => {
          if (!option.required) return false;
          const values = data.getAll(`config.${option.label}`).filter(Boolean);
          return values.length === 0;
        });
        if (missing.length) {
          setError(`Please choose: ${missing.map((option) => option.label).join(", ")}`);
          return;
        }

        const configText = formatQuoteConfiguration(data);
        const message = [data.get("message"), configText].filter(Boolean).join("\n\n");
        data.set("message", message);
        setError("");
        setSubmitting(true);
        void fetch("/newwebsite/api/leads", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            type: "quote",
            name: data.get("name"),
            company: data.get("company"),
            email: data.get("email"),
            phone: data.get("phone"),
            message,
            context: {
              ...context,
              productSlug: configuration?.productSlug || context?.productSlug,
              product: productName,
              code,
              brand,
              category,
              sourceUrl: configuration?.sourceUrl || context?.sourceUrl,
              configuration: configText,
              generateLead: configuration?.generateLead,
            },
          }),
        })
          .then(async (response) => {
            if (!response.ok) throw new Error("Could not submit quote request");
            setDone(true);
          })
          .catch(() => setError("Could not submit the quote request. Please try again or call Printechs."))
          .finally(() => setSubmitting(false));
      }}
    >
      {productName ? (
        <div className="flex items-start gap-4 border-b border-line bg-paper px-6 py-5 sm:px-8">
          <span className="mt-1 hidden h-10 w-1 shrink-0 rounded-full bg-product-icon sm:block" />
          <div>
            <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
              Product
            </p>
            <p className="mt-2 font-display text-xl font-semibold tracking-tight text-ink">
              {productName}
            </p>
            <p className="mt-1 text-sm text-slate">
              {[brand, category, code].filter(Boolean).join(" · ")}
            </p>
          </div>
        </div>
      ) : null}

      <div className="space-y-8 px-6 py-7 sm:px-8 sm:py-8">
        {configuration?.configureOnQuote ? (
          <>
            <QuoteConfigurationFields options={configuration.quoteOptions} />
            <hr className="border-line" />
          </>
        ) : null}

        <section>
          <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
            Your details
          </p>
          <div className="mt-5 grid gap-5 sm:grid-cols-2">
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Full name <span className="text-product-icon">*</span>
              </span>
              <input
                name="name"
                required
                autoComplete="name"
                className={fieldClass}
              />
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Company <span className="text-product-icon">*</span>
              </span>
              <input
                name="company"
                required
                autoComplete="organization"
                className={fieldClass}
              />
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Work email <span className="text-product-icon">*</span>
              </span>
              <input
                name="email"
                type="email"
                required
                autoComplete="email"
                className={fieldClass}
              />
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Phone / WhatsApp <span className="text-product-icon">*</span>
              </span>
              <input
                name="phone"
                type="tel"
                required
                autoComplete="tel"
                className={fieldClass}
              />
            </label>
          </div>
        </section>

        <label className="block">
          <span className="text-sm font-semibold text-ink">Project details</span>
          <textarea
            name="message"
            rows={4}
            placeholder="Quantity, site location, timeline…"
            className={`${fieldClass} min-h-[120px] resize-y`}
          />
        </label>

        {error ? (
          <p className="text-sm font-medium text-accent" role="alert">
            {error}
          </p>
        ) : null}

        <div className="flex flex-wrap items-center gap-4 border-t border-line pt-6">
          <button
            type="submit"
            disabled={submitting}
            className="inline-flex min-h-11 items-center justify-center rounded-sm bg-signal px-6 py-2.5 text-sm font-semibold tracking-wide text-white shadow-soft transition duration-300 ease-premium hover:bg-signal-bright focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {submitting ? "Submitting…" : "Submit quote request"}
          </button>
          <p className="text-sm text-slate">No prices on the website — we reply with a formal quote.</p>
        </div>
      </div>
    </form>
  );
}
