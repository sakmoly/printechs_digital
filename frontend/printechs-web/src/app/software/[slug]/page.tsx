import { notFound } from "next/navigation";
import { softwareSolutions, getSoftwareBySlug } from "@/data/software";
import { resolveProductPage } from "@/lib/product-service";
import { ProductPageView } from "@/components/products/ProductPageView";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { buildMetadata } from "@/lib/seo";

type Props = { params: { slug: string } };

export function generateStaticParams() {
  return softwareSolutions.map((item) => ({ slug: item.slug }));
}

export function generateMetadata({ params }: Props) {
  const resolved = resolveProductPage(params.slug);
  const software = getSoftwareBySlug(params.slug);

  if (resolved) {
    return buildMetadata({
      ...resolved.page.seo,
      title: `${resolved.page.displayName} | Printechs Software`,
      description: resolved.page.shortDescription,
    });
  }

  if (!software) {
    return buildMetadata({
      title: "Software | Printechs",
      description: "Software solutions from Printechs.",
    });
  }

  return buildMetadata({
    ...software.seo,
    title: `${software.name} | Printechs Software`,
    description: software.summary,
  });
}

export default function SoftwareDetailPage({ params }: Props) {
  const resolved = resolveProductPage(params.slug);
  if (resolved) {
    return <ProductPageView {...resolved} />;
  }

  const software = getSoftwareBySlug(params.slug);
  if (!software) notFound();

  const title = software.name;

  return (
    <>
      <PageIntro
        title={title}
        description={software.summary}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Software", href: "/software" },
          { label: title },
        ]}
      />
      <Section tone="white">
        <div className="max-w-3xl">
          <p className="mt-4 text-base leading-relaxed text-slate">
            Full detail for {title} will be published soon. Contact Printechs for
            demos, integration scope, and deployment planning.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button href="/request-quote" variant="primary">
              Request Quote
            </Button>
            <Button href="/request-demo" variant="ghost">
              Schedule Demo
            </Button>
          </div>
        </div>
      </Section>
    </>
  );
}
