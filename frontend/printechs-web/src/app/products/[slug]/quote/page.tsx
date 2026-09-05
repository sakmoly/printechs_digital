import Link from "next/link";
import { notFound } from "next/navigation";
import { Container } from "@/components/ui/Container";
import { Breadcrumb } from "@/components/ui/Breadcrumb";
import { Section } from "@/components/ui/Section";
import { QuoteRequestForm } from "@/components/forms/QuoteRequestForm";
import { buildMetadata } from "@/lib/seo";
import { productHeadingClass } from "@/lib/product-page-theme";
import type { QuoteConfiguration } from "@/types/quote-config";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type Props = { params: { slug: string } };

async function fetchQuoteConfiguration(slug: string): Promise<QuoteConfiguration | null> {
  const url = new URL(
    "/api/method/printechs_digital.api.quote.get_quote_configuration",
    process.env.ERPNEXT_URL || process.env.NEXT_PUBLIC_ERPNEXT_URL || "https://printechs.com",
  );
  url.searchParams.set("slug", slug);

  try {
    const response = await fetch(url.toString(), {
      headers: { Accept: "application/json" },
      next: { revalidate: 60 },
    });
    if (!response.ok) return null;
    const payload = (await response.json()) as { message?: QuoteConfiguration };
    return payload.message ?? null;
  } catch {
    return null;
  }
}

export async function generateMetadata({ params }: Props) {
  const configuration = await fetchQuoteConfiguration(params.slug);
  const name = configuration?.product || "Product";
  return buildMetadata({
    title: `Request Quote — ${name} | Printechs`,
    description: `Request a quote for ${name} from Printechs.`,
    canonicalPath: `/products/${params.slug}/quote`,
    indexPage: false,
  });
}

export default async function ProductQuotePage({ params }: Props) {
  const configuration = await fetchQuoteConfiguration(params.slug);
  if (!configuration) notFound();

  const productHref = configuration.sourceUrl || `/products/${params.slug}`;

  return (
    <>
      <section className="border-b border-line bg-white">
        <Container className="pt-10 pb-8 sm:pt-12 sm:pb-9">
          <Breadcrumb
            className="mb-5"
            items={[
              { label: "Home", href: "/" },
              { label: "Products", href: "/products" },
              { label: configuration.product, href: productHref },
              { label: "Request Quote" },
            ]}
          />
          <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
            Request Quote
          </p>
          <h1
            className={`mt-3 font-display text-4xl font-semibold tracking-tight sm:text-5xl ${productHeadingClass("display")}`}
          >
            {configuration.product}
          </h1>
          <p className="mt-3 max-w-2xl text-base leading-relaxed text-slate">
            {configuration.configureOnQuote
              ? "Choose the configuration you need. A Printechs specialist will reply with pricing and availability."
              : "Tell us about your requirement. A Printechs specialist will reply with pricing and availability."}
          </p>
          <p className="mt-5">
            <Link
              href={productHref}
              className="text-sm font-semibold text-product-icon underline-offset-4 hover:underline"
            >
              ← Back to product
            </Link>
          </p>
        </Container>
      </section>
      <Section tone="white" pad="compact">
        <div className="mx-auto max-w-3xl">
          <QuoteRequestForm configuration={configuration} />
        </div>
      </Section>
    </>
  );
}
