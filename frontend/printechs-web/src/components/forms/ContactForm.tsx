"use client";

import { SelectInput, TextArea, TextInput } from "@/components/forms/FormField";
import { LeadFormSuccess, SubmitButton, useLeadForm } from "@/components/forms/LeadForm";

const inquiryOptions = [
  { value: "general", label: "General enquiry" },
  { value: "sales", label: "Sales & products" },
  { value: "support", label: "Support & service" },
  { value: "software", label: "Software & integration" },
  { value: "partnership", label: "Partnership" },
];

export function ContactForm() {
  const { submit, errors, submitting, result, formError } = useLeadForm({ type: "contact" });

  if (result) {
    return (
      <LeadFormSuccess
        title="Message sent"
        description="Thank you for contacting Printechs. A specialist will respond to your enquiry as soon as possible."
        reference={result.reference}
      />
    );
  }

  return (
    <form
      className="space-y-5"
      noValidate
      data-analytics-form="contact"
      onSubmit={(event) => {
        event.preventDefault();
        void submit(new FormData(event.currentTarget));
      }}
    >
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
        label="Enquiry type"
        name="inquiryType"
        options={inquiryOptions}
        defaultValue="general"
        error={errors.inquiryType}
      />

      <TextArea
        label="How can we help?"
        name="message"
        required
        error={errors.message}
        placeholder="Describe your requirement, location, and preferred contact method…"
      />

      {formError ? (
        <p className="text-sm font-medium text-accent" role="alert">
          {formError}
        </p>
      ) : null}

      <SubmitButton label="Send message" submitting={submitting} />
    </form>
  );
}
