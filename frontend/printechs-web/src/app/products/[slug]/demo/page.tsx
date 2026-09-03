import Link from "next/link";
import { notFound } from "next/navigation";
import {
  fetchProductQuoteContext,
  getDemoProductSlugsAsync,
  productSupportsDemoAsync,
} from "@/lib/product-quote-context";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { DemoRequestForm } from "@/components/forms/DemoRequestForm";
import { buildMetadata } from "@/lib/seo";

export const revalidate = 60;

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

export default async function ProductDemoPage({ params }: Props) {
  if (!(await productSupportsDemoAsync(params.slug))) notFound();

  const quoteContext = await fetchProductQuoteContext(params.slug);
  if (!quoteContext) notFound();

  return (
    <>
      <PageIntro
        title="Request Demo"
        description={`Schedule a demonstration of ${quoteContext.displayName} with a Printechs software specialist.`}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Products", href: "/products" },
          { label: quoteContext.displayName, href: quoteContext.sourceUrl },
          { label: "Request Demo" },
        ]}
      />
      <Section tone="white">
        <div className="mx-auto max-w-3xl">
          <p className="mb-6 text-sm text-slate">
            <Link
              href={quoteContext.sourceUrl}
              className="font-semibold text-signal-deep underline-offset-4 hover:underline"
            >
              ← Back to {quoteContext.displayName}
            </Link>
          </p>
          <DemoRequestForm context={quoteContext.leadContext} />
        </div>
      </Section>
    </>
  );
}
