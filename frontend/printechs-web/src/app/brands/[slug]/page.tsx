import Link from "next/link";
import { notFound } from "next/navigation";
import {
  brands,
  getBrandBySlug,
  getProductsByBrandName,
} from "@/data";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";

type Props = { params: { slug: string } };

export function generateStaticParams() {
  return brands.map((brand) => ({ slug: brand.slug }));
}

export function generateMetadata({ params }: Props) {
  const brand = getBrandBySlug(params.slug);
  if (!brand) {
    return buildMetadata({
      title: "Brand | Printechs",
      description: "Brand information from Printechs.",
    });
  }
  return buildMetadata(brand.seo);
}

export default function BrandDetailPage({ params }: Props) {
  const brand = getBrandBySlug(params.slug);
  if (!brand) notFound();

  const brandProducts = getProductsByBrandName(brand.name);

  return (
    <>
      <PageIntro
        title={brand.name}
        description={brand.summary}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Brands", href: "/brands" },
          { label: brand.name },
        ]}
      />

      <Section tone="white">
        <div className="flex flex-col gap-8 lg:flex-row lg:items-center lg:justify-between">
          <ImageFrame
            src={brand.logo.src}
            alt={brand.logo.alt}
            spec={IMAGE_SPECS.brandLogo}
            width={240}
            height={80}
            showSizeLabel={false}
            className="flex h-24 w-full max-w-sm items-center justify-center rounded-sm border border-line bg-white px-8"
            imageClassName="max-h-14 w-auto max-w-full object-contain object-center"
          />
          <div className="flex flex-wrap gap-3">
            <Button href="/request-quote" variant="primary">
              Request Quote
            </Button>
            <Button href="/contact" variant="ghost">
              Talk to a Specialist
            </Button>
            <Button href="/brands" variant="ghost">
              All Brands
            </Button>
          </div>
        </div>
      </Section>

      <Section tone="muted">
        <div className="mb-8 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <p className="text-[0.7rem] font-semibold uppercase tracking-[0.18em] text-signal-deep">
              Products
            </p>
            <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight text-ink">
              {brand.name} products
            </h2>
          </div>
          <Link
            href="/products"
            className="text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
          >
            View all products
          </Link>
        </div>

        {brandProducts.length > 0 ? (
          <FeatureGrid columns={3}>
            {brandProducts.map((product) => (
              <Card
                key={product.id}
                href={`/products/${product.slug}`}
                title={product.name}
                description={product.summary}
                meta={product.category}
                cta="View product"
                media={
                  <ImageFrame
                    src={product.image.src}
                    alt={product.image.alt}
                    spec={IMAGE_SPECS.product}
                    fill
                    className="aspect-square bg-mist"
                    imageClassName="object-cover p-6"
                    sizes="(max-width: 768px) 100vw, 33vw"
                  />
                }
              />
            ))}
          </FeatureGrid>
        ) : (
          <div className="rounded-sm border border-line bg-white p-8">
            <p className="text-base text-slate">
              Product details for {brand.name} will appear here as the catalogue
              is expanded. Contact Printechs for current availability and
              recommendations.
            </p>
            <div className="mt-6">
              <Button href="/contact" variant="ghost">
                Contact Printechs
              </Button>
            </div>
          </div>
        )}
      </Section>
    </>
  );
}
