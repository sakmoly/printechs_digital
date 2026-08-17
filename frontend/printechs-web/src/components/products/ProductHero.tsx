import type { ProductPageContent } from "@/types/content";
import type { Brand } from "@/types/content";
import { Container } from "@/components/ui/Container";
import { Breadcrumb, type Crumb } from "@/components/ui/Breadcrumb";
import { Button } from "@/components/ui/Button";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildProductDemoUrl, buildProductQuoteUrl } from "@/lib/product-quote";
import { ProductIcon, trustChipIcons } from "@/components/products/ProductIcon";
import {
  productHeadingClass,
  productPageTheme,
} from "@/lib/product-page-theme";

const typeLabels: Record<ProductPageContent["productType"], string> = {
  industrial: "Industrial",
  retail_hardware: "Retail",
  software: "Software",
  generic: "Product",
};

const heroImageSpec = (productType: ProductPageContent["productType"]) =>
  productType === "software" ? IMAGE_SPECS.software : IMAGE_SPECS.product;

type ProductHeroProps = {
  page: ProductPageContent;
  brand?: Brand;
  crumbs: Crumb[];
};

export function ProductHero({ page, brand, crumbs }: ProductHeroProps) {
  const imageSpec = heroImageSpec(page.productType);
  const quoteUrl = buildProductQuoteUrl(page);
  const demoUrl = buildProductDemoUrl(page);
  const categoryLabel =
    page.categoryLabel ??
    page.subcategory?.toUpperCase() ??
    page.category.toUpperCase();

  return (
    <section className="border-b border-line bg-white">
      <Container className="py-12 sm:py-14 lg:py-16">
        <Breadcrumb items={crumbs} />

        <div className="grid items-center gap-10 lg:grid-cols-[minmax(0,1.05fr)_minmax(0,0.95fr)] lg:gap-12">
          <div>
            {brand ? (
              <div className="mb-5 inline-flex rounded-md border border-line bg-white px-4 py-3 shadow-soft">
                <ImageFrame
                  src={brand.logo.src}
                  alt={brand.logo.alt}
                  spec={IMAGE_SPECS.brandLogo}
                  width={140}
                  height={48}
                  showSizeLabel={false}
                  className="flex h-10 w-32 items-center justify-center"
                  imageClassName="max-h-9 w-auto max-w-full object-contain"
                />
              </div>
            ) : null}

            <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
              {categoryLabel}
            </p>
            <h1
              className={`mt-3 font-display text-4xl font-semibold tracking-tight sm:text-5xl lg:text-[3.35rem] lg:leading-[1.06] ${productHeadingClass("display")}`}
            >
              {page.displayName}
            </h1>
            {page.tagline ? (
              <p
                className={`mt-4 max-w-xl text-lg font-semibold leading-snug ${productPageTheme.blueHeadings ? "text-product-icon/85" : "text-ink"}`}
              >
                {page.tagline}
              </p>
            ) : null}
            <p className="mt-3 max-w-xl text-base leading-relaxed text-slate">
              {page.shortDescription}
            </p>

            <div className="mt-6 flex flex-wrap gap-2">
              <span className="rounded-sm border border-line bg-white px-2.5 py-1 text-[0.7rem] font-semibold uppercase tracking-[0.14em] text-slate">
                {typeLabels[page.productType]}
              </span>
              {page.itemCode ? (
                <span className="rounded-sm border border-line bg-white px-2.5 py-1 text-[0.7rem] font-semibold uppercase tracking-[0.14em] text-slate">
                  Item {page.itemCode}
                </span>
              ) : null}
            </div>

            <div className="mt-8 flex flex-wrap gap-3">
              <Button href={quoteUrl} variant="primary">
                Request Quote →
              </Button>
              {page.primaryDownload ? (
                <Button href={page.primaryDownload.href} variant="ghost">
                  ↓ Download Datasheet
                </Button>
              ) : null}
              {page.showDemoCta !== false &&
              (page.productType === "software" || page.showDemoCta) ? (
                <Button href={demoUrl} variant="ghost">
                  Book a Demo
                </Button>
              ) : null}
            </div>

            {page.heroTrustChips?.length ? (
              <ul className="mt-8 flex flex-wrap gap-x-6 gap-y-3">
                {page.heroTrustChips.map((chip) => {
                  const iconKey = trustChipIcons[chip];
                  return (
                    <li
                      key={chip}
                      className="flex items-center gap-2.5 text-sm font-medium text-slate"
                    >
                      {iconKey ? (
                        <span className="inline-flex h-8 w-8 items-center justify-center rounded-full bg-product-icon/10 text-product-icon">
                          <ProductIcon name={iconKey} size="sm" />
                        </span>
                      ) : (
                        <span className="h-1.5 w-1.5 rounded-full bg-product-icon" />
                      )}
                      {chip}
                    </li>
                  );
                })}
              </ul>
            ) : null}
          </div>

          <div className="relative flex items-center justify-center">
            <div className="relative w-full max-w-lg rounded-md border border-line bg-white p-6 shadow-soft sm:p-8">
              <ImageFrame
                src={page.heroImage.src}
                alt={page.heroImage.alt}
                spec={imageSpec}
                fill
                priority
                className={
                  page.productType === "software"
                    ? "aspect-[16/10]"
                    : "aspect-square"
                }
                imageClassName="object-contain p-4"
                sizes="(max-width: 1024px) 100vw, 42vw"
                showSizeLabel={false}
              />
            </div>
            {page.gallery?.length ? (
              <div className="absolute -bottom-3 -right-2 hidden w-28 overflow-hidden rounded-md border border-line bg-white shadow-soft sm:block lg:-right-6 lg:w-32">
                <ImageFrame
                  src={page.gallery[0].src}
                  alt={page.gallery[0].alt}
                  spec={imageSpec}
                  fill
                  className="aspect-square"
                  imageClassName="object-contain p-2"
                  sizes="128px"
                  showSizeLabel={false}
                />
              </div>
            ) : null}
          </div>
        </div>
      </Container>
    </section>
  );
}
