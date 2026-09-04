"use client";

import type { LeadContext } from "@/types/lead";
import type { QuoteConfiguration } from "@/types/quote-config";
import { Button } from "@/components/ui/Button";
import {
  QuoteConfigurationFields,
  formatQuoteConfiguration,
} from "@/components/forms/QuoteConfigurationFields";
import { useLeadForm } from "@/components/forms/LeadForm";

const fieldClass =
  "mt-2 w-full rounded-sm border border-line bg-white px-4 py-2.5 text-sm text-ink shadow-sm transition placeholder:text-slate/70 focus-visible:border-product-icon focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-product-icon/20";

type DemoRequestFormProps = {
  context?: LeadContext;
  configuration?: QuoteConfiguration;
};

export function DemoRequestForm({ context, configuration }: DemoRequestFormProps) {
  const leadContext: LeadContext = {
    ...(context ?? {}),
    generateLead: configuration?.generateLead ?? context?.generateLead,
  };

  const { submit, errors, submitting, result, formError, setFormError } = useLeadForm({
    type: "demo",
    initialContext: leadContext,
  });

  const productName = configuration?.product || context?.product;
  const brand = configuration?.brand || context?.brand;
  const category = configuration?.category || context?.category;
  const showQuestionnaire = Boolean(
    configuration?.configureOnQuote && configuration.quoteOptions.length,
  );
  const backHref = configuration?.sourceUrl || context?.sourceUrl;

  if (result) {
    return (
      <div className="overflow-hidden rounded-sm border border-product-icon/15 bg-white shadow-soft">
        <div className="border-b border-line bg-paper px-6 py-5 sm:px-8">
          <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
            Request received
          </p>
          <h2 className="mt-3 font-display text-2xl font-semibold tracking-tight text-ink">
            Demo request received
          </h2>
          <p className="mt-3 max-w-xl text-base leading-relaxed text-slate">
            Thank you. Our software team will contact you to schedule a demonstration tailored
            to your business environment.
          </p>
        </div>
        <div className="flex flex-wrap gap-3 px-6 py-6 sm:px-8">
          {backHref ? (
            <Button href={backHref} variant="primary">
              Back to {productName || "product"}
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
          setFormError(`Please choose: ${missing.map((option) => option.label).join(", ")}`);
          return;
        }

        const configText = formatQuoteConfiguration(data);
        data.set("message", String(data.get("message") ?? "").trim());
        if (configText) {
          data.set("configuration", configText);
        }
        const preferredTime = String(data.get("preferredTime") ?? "").trim();
        if (preferredTime) {
          data.set("preferredTime", preferredTime);
        }

        void submit(data);
      }}
    >
      {productName ? (
        <div className="flex items-start gap-4 border-b border-line bg-paper px-6 py-5 sm:px-8">
          <span className="mt-1 hidden h-10 w-1 shrink-0 rounded-full bg-product-icon sm:block" />
          <div>
            <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
              Software demo
            </p>
            <p className="mt-2 font-display text-xl font-semibold tracking-tight text-ink">
              {productName}
            </p>
            <p className="mt-1 text-sm text-slate">
              {[brand, category].filter(Boolean).join(" · ")}
            </p>
          </div>
        </div>
      ) : null}

      <div className="space-y-8 px-6 py-7 sm:px-8 sm:py-8">
        {showQuestionnaire ? (
          <>
            <QuoteConfigurationFields
              options={configuration!.quoteOptions}
              sectionTitle="Tell us about your environment"
              sectionDescription="Help us tailor the demonstration to your business. Required fields are marked."
            />
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
                Full name
                {errors.name ? null : <span className="text-product-icon"> *</span>}
              </span>
              <input
                name="name"
                required
                autoComplete="name"
                className={fieldClass}
                aria-invalid={Boolean(errors.name)}
              />
              {errors.name ? (
                <p className="mt-1.5 text-xs font-medium text-accent" role="alert">
                  {errors.name}
                </p>
              ) : null}
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Company <span className="text-product-icon"> *</span>
              </span>
              <input
                name="company"
                required
                autoComplete="organization"
                className={fieldClass}
                aria-invalid={Boolean(errors.company)}
              />
              {errors.company ? (
                <p className="mt-1.5 text-xs font-medium text-accent" role="alert">
                  {errors.company}
                </p>
              ) : null}
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Work email <span className="text-product-icon"> *</span>
              </span>
              <input
                name="email"
                type="email"
                required
                autoComplete="email"
                className={fieldClass}
                aria-invalid={Boolean(errors.email)}
              />
              {errors.email ? (
                <p className="mt-1.5 text-xs font-medium text-accent" role="alert">
                  {errors.email}
                </p>
              ) : null}
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">
                Phone / WhatsApp <span className="text-product-icon"> *</span>
              </span>
              <input
                name="phone"
                type="tel"
                required
                autoComplete="tel"
                className={fieldClass}
                aria-invalid={Boolean(errors.phone)}
              />
              {errors.phone ? (
                <p className="mt-1.5 text-xs font-medium text-accent" role="alert">
                  {errors.phone}
                </p>
              ) : null}
            </label>
          </div>
        </section>

        <section>
          <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
            Demo preferences
          </p>
          <div className="mt-5 space-y-5">
            <label className="block">
              <span className="text-sm font-semibold text-ink">Preferred demo time</span>
              <input
                name="preferredTime"
                placeholder="e.g. Sun–Thu, 10:00–14:00 AST"
                className={fieldClass}
              />
              <p className="mt-1.5 text-xs text-slate">
                Optional — your timezone, preferred days, or availability.
              </p>
            </label>
            <label className="block">
              <span className="text-sm font-semibold text-ink">What would you like to see?</span>
              <textarea
                name="message"
                rows={4}
                placeholder="Store count, POS setup, ERP integration, ZATCA, WMS, or other topics…"
                className={`${fieldClass} min-h-[120px] resize-y`}
              />
            </label>
          </div>
        </section>

        {context?.productSlug ? (
          <input type="hidden" name="productSlug" value={context.productSlug} />
        ) : null}
        {productName ? <input type="hidden" name="product" value={productName} /> : null}
        {backHref ? <input type="hidden" name="sourceUrl" value={backHref} /> : null}

        {formError ? (
          <p className="text-sm font-medium text-accent" role="alert">
            {formError}
          </p>
        ) : null}

        <div className="flex flex-wrap items-center gap-4 border-t border-line pt-6">
          <button
            type="submit"
            disabled={submitting}
            className="inline-flex min-h-11 items-center justify-center rounded-sm bg-signal px-6 py-2.5 text-sm font-semibold tracking-wide text-white shadow-soft transition duration-300 ease-premium hover:bg-signal-bright focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {submitting ? "Submitting…" : "Request demo"}
          </button>
          <p className="text-sm text-slate">
            A Printechs specialist will contact you to confirm the session.
          </p>
        </div>
      </div>
    </form>
  );
}
