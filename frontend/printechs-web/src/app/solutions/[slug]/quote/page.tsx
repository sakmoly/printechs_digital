import Link from "next/link";
import { notFound } from "next/navigation";
import { getSolutionQuoteContext, listSolutionQuoteSlugs } from "@/lib/solution-quote-context";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { QuoteRequestForm } from "@/components/forms/QuoteRequestForm";
import { buildMetadata } from "@/lib/seo";

type Props = { params: { slug: string } };

export function generateStaticParams() {
  return listSolutionQuoteSlugs().map((slug) => ({ slug }));
}

export function generateMetadata({ params }: Props) {
  const quoteContext = getSolutionQuoteContext(params.slug);
  if (!quoteContext) {
    return buildMetadata({
      title: "Request Quote | Printechs",
      description: "Request a quote from Printechs.",
    });
  }

  return buildMetadata({
    title: `Request Quote — ${quoteContext.displayName} | Printechs`,
    description: `Request a quote for ${quoteContext.displayName} solutions from Printechs.`,
    canonicalPath: `/solutions/${params.slug}/quote`,
  });
}

export default function SolutionQuotePage({ params }: Props) {
  const quoteContext = getSolutionQuoteContext(params.slug);
  if (!quoteContext) notFound();

  return (
    <>
      <PageIntro
        title="Request Quote"
        description={`Tell us about your ${quoteContext.displayName} requirements. A Printechs specialist will recommend the right products and integration approach.`}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Solutions", href: "/solutions" },
          { label: quoteContext.displayName, href: quoteContext.sourceUrl },
          { label: "Request Quote" },
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
          <QuoteRequestForm context={quoteContext.leadContext} />
        </div>
      </Section>
    </>
  );
}
