import { notFound } from "next/navigation";
import { fetchProductsByBrand } from "@/lib/catalog-service";
import { fetchBrand, fetchBrandSlugs } from "@/lib/brand-service";
import { fetchSuccessStories } from "@/lib/success-story-service";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { Container } from "@/components/ui/Container";
import { Breadcrumb } from "@/components/ui/Breadcrumb";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildMetadata } from "@/lib/seo";

export const revalidate = 60;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchBrandSlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const brand = await fetchBrand(params.slug);
  if (!brand) {
    return buildMetadata({
      title: "Brand | Printechs",
      description: "Brand information from Printechs.",
    });
  }
  return buildMetadata(brand.seo);
}

export default async function BrandDetailPage({ params }: Props) {
  const brand = await fetchBrand(params.slug);
  if (!brand) notFound();

  const brandProducts = await fetchProductsByBrand(brand.name);
  const brandStories = await fetchSuccessStories({ brand: brand.slug });

  return (
    <>
      <section className="border-b border-ink/10 bg-mist py-5 sm:py-6">
        <Container>
          <Breadcrumb
            items={[
              { label: "Home", href: "/" },
              { label: "Brands", href: "/brands" },
              { label: brand.name },
            ]}
          />
          <h1 className="sr-only">{brand.name}</h1>
          <div className="flex flex-col gap-4 sm:flex-row sm:items-start sm:justify-between">
            <div className="min-w-0">
              <ImageFrame
                src={brand.logo.src}
                alt=""
                spec={IMAGE_SPECS.brandLogo}
                width={220}
                height={72}
                showSizeLabel={false}
                className="flex h-16 w-52 items-center justify-start"
                imageClassName="max-h-14 w-auto max-w-full object-contain object-left"
              />
              {brand.summary ? (
                <p className="mt-3 max-w-xl text-sm leading-relaxed text-slate sm:text-base">
                  {brand.summary}
                </p>
              ) : null}
            </div>
            <div className="flex flex-wrap gap-3">
              {brandStories.stories.length ? (
                <Button href={`/success-stories?brand=${brand.slug}`} variant="ghost">
                  Success Stories
                </Button>
              ) : null}
              <Button href="/contact" variant="primary" className="shrink-0 self-start">
                Talk to a Specialist
              </Button>
            </div>
          </div>
        </Container>
      </section>

      <Section tone="white" pad="compact">
        <h2 className="mb-6 font-display text-2xl font-semibold tracking-tight text-ink">
          Products
        </h2>

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
                    imageClassName="object-contain p-6"
                    sizes="(max-width: 768px) 100vw, 33vw"
                  />
                }
              />
            ))}
          </FeatureGrid>
        ) : (
          <div className="rounded-sm border border-line bg-mist p-8">
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
