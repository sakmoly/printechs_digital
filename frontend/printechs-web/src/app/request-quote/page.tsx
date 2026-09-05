import { GeneralQuoteRequestForm } from "@/components/forms/GeneralQuoteRequestForm";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { buildMetadata } from "@/lib/seo";
import { fetchContactPage } from "@/lib/contact-service";
import type { LeadContext } from "@/types/lead";

type Props = {
  searchParams: Record<string, string | string[] | undefined>;
};

export const metadata = buildMetadata({
  title: "Request Quote | Printechs",
  description: "Request a quote for Printechs products and solutions.",
  indexPage: false,
});

function param(value: string | string[] | undefined): string | undefined {
  return Array.isArray(value) ? value[0] : value;
}

export default async function Page({ searchParams }: Props) {
  const contact = await fetchContactPage();
  const context: LeadContext = {
    product: param(searchParams.product),
    code: param(searchParams.code),
    brand: param(searchParams.brand),
    category: param(searchParams.category),
    sourceUrl: param(searchParams.url),
  };

  const hasContext = Boolean(
    context.product || context.code || context.brand || context.category,
  );

  return (
    <>
      <PageIntro
        title="Request Quote"
        description={
          hasContext
            ? "Tell us what you need and how you'd like us to follow up."
            : "Share your requirement and our team will respond with pricing and availability."
        }
        crumbs={[{ label: "Home", href: "/" }, { label: "Request Quote" }]}
      />
      <Section tone="white">
        <div className="max-w-3xl">
          <GeneralQuoteRequestForm
            context={hasContext ? context : undefined}
            printechsWhatsAppHref={contact.specialist.whatsapp?.href}
          />
        </div>
      </Section>
    </>
  );
}
