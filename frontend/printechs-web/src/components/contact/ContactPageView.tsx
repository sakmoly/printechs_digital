import type { ContactPageContent } from "@/types/content";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { ContactForm } from "@/components/forms/ContactForm";
import { ContactInfoPanel } from "@/components/contact/ContactInfoPanel";
import { ContactOfficeBlock } from "@/components/contact/ContactOfficeBlock";

export function ContactPageView({ content }: { content: ContactPageContent }) {
  return (
    <>
      <PageIntro
        title={content.title}
        description={content.tagline}
        crumbs={[{ label: "Home", href: "/" }, { label: "Contact" }]}
      />

      <Section tone="muted" pad="compact">
        <div className="space-y-12">
          {content.offices.map((office, index) => (
            <ContactOfficeBlock key={office.city} office={office} reverse={index % 2 === 1} />
          ))}
        </div>
      </Section>

      <Section tone="white" id="message">
        <div className="grid gap-10 lg:grid-cols-12 lg:gap-12">
          <div className="lg:col-span-7">
            <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
              {content.form.eyebrow}
            </p>
            <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight text-ink">
              {content.form.title}
            </h2>
            <p className="mt-4 max-w-2xl text-base leading-relaxed text-slate">
              {content.form.description}
            </p>
            <div className="mt-8 rounded-sm border border-line bg-mist p-6 sm:p-8">
              <ContactForm />
            </div>
          </div>

          <div className="lg:col-span-5">
            <ContactInfoPanel specialist={content.specialist} />
          </div>
        </div>
      </Section>
    </>
  );
}
