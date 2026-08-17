import { notFound } from "next/navigation";
import {
  getBrandBySlug,
  getProductBySlug,
  getProductHubChildren,
} from "@/data";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";

const HUB_SLUG = "autoid-solutions";

const brandSlugByProductBrand: Record<string, string> = {
  Datalogic: "datalogic",
  Zebra: "zebra",
};

export function generateMetadata() {
  const hub = getProductBySlug(HUB_SLUG);
  if (!hub) {
    return buildMetadata({
      title: "AutoID Solutions | Printechs",
      description: "AutoID solutions from Printechs.",
    });
  }
  return buildMetadata(hub.seo);
}

export default function AutoIdSolutionsPage() {
  const hub = getProductBySlug(HUB_SLUG);
  if (!hub) notFound();

  const brandProducts = getProductHubChildren(hub);

  return (
    <>
      <PageIntro
        title={hub.name}
        description="Printechs supplies AutoID technology from leading brands for scanning, printing, and mobile operations across retail, warehouse, and industrial environments."
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Products", href: "/products" },
          { label: hub.name },
        ]}
      />

      <Section tone="white">
        <div className="max-w-3xl">
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-signal-deep">
            {hub.brand}
          </p>
          <p className="mt-4 text-base leading-relaxed text-slate">{hub.summary}</p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button href="/request-quote" variant="primary">
              Request Quote
            </Button>
            <Button href="/contact" variant="ghost">
              Talk to a Specialist
            </Button>
          </div>
        </div>
      </Section>

      <Section tone="muted">
        <div className="mb-8">
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-signal-deep">
            Choose a brand
          </p>
          <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight text-ink">
            Explore by manufacturer
          </h2>
          <p className="mt-3 max-w-2xl text-base text-slate">
            Select Datalogic or Zebra to view brand-specific products, applications,
            and support from Printechs.
          </p>
        </div>

        <FeatureGrid columns={2}>
          {brandProducts.map((product) => {
            const brandSlug = brandSlugByProductBrand[product.brand];
            const brand = brandSlug ? getBrandBySlug(brandSlug) : undefined;

            return (
              <Card
                key={product.id}
                href={brand ? `/brands/${brand.slug}` : `/products/${product.slug}`}
                title={hub.name}
                description={product.summary}
                meta={product.brand}
                cta={`View ${product.brand}`}
                media={
                  <ImageFrame
                    src={brand?.logo.src ?? product.image.src}
                    alt={brand?.logo.alt ?? product.image.alt}
                    spec={IMAGE_SPECS.brandLogo}
                    fill
                    className="flex aspect-[16/10] items-center justify-center bg-white p-10"
                    imageClassName={
                      brand
                        ? "h-12 w-auto object-contain"
                        : "object-cover p-6"
                    }
                    sizes="(max-width: 768px) 100vw, 50vw"
                  />
                }
              />
            );
          })}
        </FeatureGrid>

        <div className="mt-10 rounded-sm border border-line bg-white p-6 sm:p-8">
          <p className="text-sm font-semibold uppercase tracking-[0.14em] text-signal-deep">
            Product detail pages
          </p>
          <div className="mt-4 flex flex-col gap-3 sm:flex-row sm:flex-wrap">
            {brandProducts.map((product) => (
              <Button
                key={product.id}
                href={`/products/${product.slug}`}
                variant="ghost"
              >
                {product.brand} catalogue
              </Button>
            ))}
          </div>
        </div>
      </Section>
    </>
  );
}
