import Link from "next/link";
import { notFound } from "next/navigation";
import {
  fetchProductQuoteContext,
  getDemoProductSlugsAsync,
  productSupportsDemoAsync,
} from "@/lib/product-quote-context";
import { fetchDemoConfiguration } from "@/lib/form-configuration";
import { Container } from "@/components/ui/Container";
import { Breadcrumb } from "@/components/ui/Breadcrumb";
import { Section } from "@/components/ui/Section";
import { DemoRequestForm } from "@/components/forms/DemoRequestForm";
import { buildMetadata } from "@/lib/seo";
import { productHeadingClass } from "@/lib/product-page-theme";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await getDemoProductSlugsAsync();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const quoteContext = await fetchProductQuoteContext(params.slug);
  if (!quoteContext) {
    return buildMetadata({
      title: "Request Demo | Printechs",
      description: "Book a software demonstration with Printechs.",
    });
  }

  return buildMetadata({
    title: `Request Demo — ${quoteContext.displayName} | Printechs`,
    description: `Schedule a demonstration of ${quoteContext.displayName} with Printechs.`,
    canonicalPath: `/products/${params.slug}/demo`,
  });
}

function demoCrumbs(displayName: string, sourceUrl: string) {
  const isSoftware = sourceUrl.startsWith("/software/");
  return [
    { label: "Home", href: "/" },
    isSoftware
      ? { label: "Software", href: "/software" }
      : { label: "Products", href: "/products" },
    { label: displayName, href: sourceUrl },
    { label: "Request Demo" },
  ];
}

export default async function ProductDemoPage({ params }: Props) {
  if (!(await productSupportsDemoAsync(params.slug))) notFound();

  const quoteContext = await fetchProductQuoteContext(params.slug);
  if (!quoteContext) notFound();

  const configuration = await fetchDemoConfiguration(params.slug);
  const productHref = quoteContext.sourceUrl;

  return (
    <>
      <section className="border-b border-line bg-white">
        <Container className="pt-10 pb-8 sm:pt-12 sm:pb-9">
          <Breadcrumb
            className="mb-5"
            items={demoCrumbs(quoteContext.displayName, productHref)}
          />
          <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
            Request Demo
          </p>
          <h1
            className={`mt-3 font-display text-4xl font-semibold tracking-tight sm:text-5xl ${productHeadingClass("display")}`}
          >
            {quoteContext.displayName}
          </h1>
          <p className="mt-3 max-w-2xl text-base leading-relaxed text-slate">
            {configuration?.configureOnQuote
              ? "Tell us about your environment so we can tailor the demonstration. A Printechs software specialist will contact you to schedule the session."
              : "Schedule a live demonstration with a Printechs software specialist."}
          </p>
          <p className="mt-5">
            <Link
              href={productHref}
              className="text-sm font-semibold text-product-icon underline-offset-4 hover:underline"
            >
              ← Back to {quoteContext.displayName}
            </Link>
          </p>
        </Container>
      </section>
      <Section tone="white" pad="compact">
        <div className="mx-auto max-w-3xl">
          <DemoRequestForm
            context={quoteContext.leadContext}
            configuration={configuration ?? undefined}
          />
        </div>
      </Section>
    </>
  );
}
