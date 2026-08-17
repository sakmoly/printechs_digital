import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { buildMetadata } from "@/lib/seo";

type Props = {
  searchParams: Record<string, string | string[] | undefined>;
};

export const metadata = buildMetadata({
  title: "Request Quote | Printechs",
  description: "Request a quote for Printechs products and solutions.",
});

function param(value: string | string[] | undefined): string | undefined {
  return Array.isArray(value) ? value[0] : value;
}

export default function Page({ searchParams }: Props) {
  const product = param(searchParams.product);
  const code = param(searchParams.code);
  const brand = param(searchParams.brand);
  const category = param(searchParams.category);
  const sourceUrl = param(searchParams.url);

  const hasContext = Boolean(product || code || brand || category);

  return (
    <>
      <PageIntro
        title="Request Quote"
        description={
          hasContext
            ? "Quote request with product context — form integration pending."
            : "Lead capture interface foundation — mockup only."
        }
        crumbs={[{ label: "Home", href: "/" }, { label: "Request Quote" }]}
      />
      <Section tone="white">
        {hasContext ? (
          <div className="max-w-xl rounded-sm border border-line bg-mist p-6 text-sm text-slate">
            <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
              Product context
            </p>
            <dl className="mt-4 space-y-3">
              {product ? (
                <div>
                  <dt className="font-medium text-ink">Product</dt>
                  <dd>{product}</dd>
                </div>
              ) : null}
              {code ? (
                <div>
                  <dt className="font-medium text-ink">Product code</dt>
                  <dd>{code}</dd>
                </div>
              ) : null}
              {brand ? (
                <div>
                  <dt className="font-medium text-ink">Brand</dt>
                  <dd>{brand}</dd>
                </div>
              ) : null}
              {category ? (
                <div>
                  <dt className="font-medium text-ink">Category</dt>
                  <dd>{category}</dd>
                </div>
              ) : null}
              {sourceUrl ? (
                <div>
                  <dt className="font-medium text-ink">Source page</dt>
                  <dd>{sourceUrl}</dd>
                </div>
              ) : null}
            </dl>
          </div>
        ) : (
          <p className="max-w-2xl text-base leading-relaxed text-slate">
            This route is part of the information architecture foundation. Full quote
            form will connect to ERPNext in a later phase.
          </p>
        )}
        <div className="mt-8">
          <Button href="/" variant="ghost">
            Back to homepage
          </Button>
        </div>
      </Section>
    </>
  );
}
