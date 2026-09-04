import { notFound } from "next/navigation";
import { getProductBySlug } from "@/data/products";
import { fetchProductPage } from "@/lib/product-service";
import { fetchPublishedProductSlugs } from "@/lib/catalog-service";
import { ProductPageView } from "@/components/products/ProductPageView";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { buildMetadata } from "@/lib/seo";
import { buildProductQuotePath } from "@/lib/product-quote-context";

import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchPublishedProductSlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const resolved = await fetchProductPage(params.slug);
  const product = getProductBySlug(params.slug);

  if (resolved) {
    return buildMetadata({
      ...resolved.page.seo,
      title: resolved.page.seo?.title || `${resolved.page.displayName} | Printechs`,
      description:
        resolved.page.seo?.description || resolved.page.shortDescription,
    });
  }

  if (!product) {
    return buildMetadata({
      title: "Product | Printechs",
      description: "Product information from Printechs.",
    });
  }

  return buildMetadata({
    ...product.seo,
    title: `${product.name} | Printechs`,
    description: product.summary,
  });
}

export default async function ProductDetailPage({ params }: Props) {
  const resolved = await fetchProductPage(params.slug);
  if (resolved) {
    return <ProductPageView {...resolved} />;
  }

  const product = getProductBySlug(params.slug);
  if (!product) notFound();

  return (
    <>
      <PageIntro
        title={product.name}
        description={product.summary}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Products", href: "/products" },
          { label: product.name },
        ]}
      />
      <Section tone="white">
        <div className="max-w-3xl">
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-signal-deep">
            {product.brand} · {product.category}
          </p>
          <p className="mt-4 text-base leading-relaxed text-slate">
            Full product detail for {product.name} will be published soon. Contact
            Printechs for specifications, availability, and integration support.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button href={buildProductQuotePath(product.slug)} variant="primary">
              Request Quote
            </Button>
            <Button href="/contact" variant="ghost">
              Contact Printechs
            </Button>
          </div>
        </div>
      </Section>
    </>
  );
}
