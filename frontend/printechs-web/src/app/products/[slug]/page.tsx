import { notFound } from "next/navigation";
import { products, getProductBySlug } from "@/data/products";
import { resolveProductPage } from "@/lib/product-service";
import { ProductPageView } from "@/components/products/ProductPageView";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { buildMetadata } from "@/lib/seo";

type Props = { params: { slug: string } };

export function generateStaticParams() {
  return products.map((product) => ({ slug: product.slug }));
}

export function generateMetadata({ params }: Props) {
  const resolved = resolveProductPage(params.slug);
  const product = getProductBySlug(params.slug);

  if (resolved) {
    return buildMetadata({
      ...resolved.page.seo,
      title: `${resolved.page.displayName} | Printechs`,
      description: resolved.page.shortDescription,
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

export default function ProductDetailPage({ params }: Props) {
  const resolved = resolveProductPage(params.slug);
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
            <Button href="/request-quote" variant="primary">
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
