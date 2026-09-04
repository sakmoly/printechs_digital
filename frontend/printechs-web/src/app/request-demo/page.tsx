import Link from "next/link";
import { DemoRequestForm } from "@/components/forms/DemoRequestForm";
import { Container } from "@/components/ui/Container";
import { Breadcrumb } from "@/components/ui/Breadcrumb";
import { Section } from "@/components/ui/Section";
import { fetchDemoConfiguration, slugFromSourceUrl } from "@/lib/form-configuration";
import { buildMetadata } from "@/lib/seo";
import { productHeadingClass } from "@/lib/product-page-theme";
import type { LeadContext } from "@/types/lead";

type Props = {
  searchParams: Record<string, string | string[] | undefined>;
};

export const dynamic = "force-dynamic";

export const metadata = buildMetadata({
  title: "Request Demo | Printechs",
  description: "Book a software demonstration with Printechs.",
  canonicalPath: "/request-demo",
});

function param(value: string | string[] | undefined): string | undefined {
  return Array.isArray(value) ? value[0] : value;
}

export default async function Page({ searchParams }: Props) {
  const product = param(searchParams.product);
  const sourceUrl = param(searchParams.url);
  const slug = slugFromSourceUrl(sourceUrl);
  const configuration = slug ? await fetchDemoConfiguration(slug) : null;

  const context: LeadContext = {
    product: configuration?.product || product,
    productSlug: configuration?.productSlug || slug,
    brand: configuration?.brand,
    category: configuration?.category,
    code: configuration?.code,
    sourceUrl: configuration?.sourceUrl || sourceUrl,
  };

  const hasContext = Boolean(context.product || context.sourceUrl);
  const backHref = context.sourceUrl;
  const backLabel = context.product || "product";

  return (
    <>
      <section className="border-b border-line bg-white">
        <Container className="pt-10 pb-8 sm:pt-12 sm:pb-9">
          <Breadcrumb
            className="mb-5"
            items={[{ label: "Home", href: "/" }, { label: "Request Demo" }]}
          />
          <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
            Request Demo
          </p>
          <h1
            className={`mt-3 font-display text-4xl font-semibold tracking-tight sm:text-5xl ${productHeadingClass("display")}`}
          >
            {hasContext ? context.product : "Book a demonstration"}
          </h1>
          <p className="mt-3 max-w-2xl text-base leading-relaxed text-slate">
            {hasContext
              ? configuration?.configureOnQuote
                ? "Tell us about your environment so we can tailor the demonstration. A Printechs software specialist will contact you to schedule the session."
                : `Schedule a demonstration of ${context.product} with a Printechs software specialist.`
              : "Tell us which software you want to explore and we will arrange a tailored demonstration."}
          </p>
          {backHref ? (
            <p className="mt-5">
              <Link
                href={backHref}
                className="text-sm font-semibold text-product-icon underline-offset-4 hover:underline"
              >
                ← Back to {backLabel}
              </Link>
            </p>
          ) : null}
        </Container>
      </section>
      <Section tone="white" pad="compact">
        <div className="mx-auto max-w-3xl">
          <DemoRequestForm
            context={hasContext ? context : undefined}
            configuration={configuration ?? undefined}
          />
        </div>
      </Section>
    </>
  );
}
