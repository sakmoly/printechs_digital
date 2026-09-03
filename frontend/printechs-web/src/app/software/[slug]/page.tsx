import { notFound } from "next/navigation";
import { softwareSolutions, getSoftwareBySlug } from "@/data/software";
import { fetchProductPage } from "@/lib/product-service";
import { fetchPublishedProductSlugs } from "@/lib/catalog-service";
import { ProductPageView } from "@/components/products/ProductPageView";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { buildMetadata } from "@/lib/seo";
import { buildProductDemoPath, buildProductQuotePath } from "@/lib/product-quote-context";

export const revalidate = 60;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchPublishedProductSlugs();
  const softwareSlugs = softwareSolutions.map((item) => item.slug);
  return Array.from(new Set([...slugs, ...softwareSlugs])).map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const resolved = await fetchProductPage(params.slug);
  const software = getSoftwareBySlug(params.slug);

  if (resolved) {
    return buildMetadata({
      ...resolved.page.seo,
      title:
        resolved.page.seo?.title ||
        `${resolved.page.displayName} | Printechs Software`,
      description:
        resolved.page.seo?.description || resolved.page.shortDescription,
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

export default async function SoftwareDetailPage({ params }: Props) {
  const resolved = await fetchProductPage(params.slug);
  if (resolved) {
    return <ProductPageView {...resolved} />;
  }

  const software = getSoftwareBySlug(params.slug);
  if (!software) notFound();

  return (
    <>
      <PageIntro
        title={software.name}
        description={software.summary}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Software", href: "/software" },
          { label: software.name },
        ]}
      />
      <Section tone="white">
        <div className="max-w-3xl">
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-signal-deep">
            {software.highlights.slice(0, 2).join(" · ") || "Printechs Software"}
          </p>
          <p className="mt-4 text-base leading-relaxed text-slate">
            Full software detail for {software.name} will be published soon. Contact
            Printechs for demos, deployment planning, and integration support.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button href={buildProductQuotePath(software.slug)} variant="primary">
              Request Quote
            </Button>
            <Button href={buildProductDemoPath(software.slug)} variant="secondary">
              Request Demo
            </Button>
          </div>
        </div>
      </Section>
    </>
  );
}
