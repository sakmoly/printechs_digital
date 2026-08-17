import type { SolutionPageContent } from "@/types/content";
import { Container } from "@/components/ui/Container";
import { Breadcrumb, type Crumb } from "@/components/ui/Breadcrumb";
import { Button } from "@/components/ui/Button";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { buildSolutionQuoteUrl } from "@/lib/solution-quote";
import { ProductIcon, trustChipIcons } from "@/components/products/ProductIcon";
import { productHeadingClass } from "@/lib/product-page-theme";

type SolutionHeroProps = {
  page: SolutionPageContent;
  crumbs: Crumb[];
};

export function SolutionHero({ page, crumbs }: SolutionHeroProps) {
  const quoteUrl = buildSolutionQuoteUrl(page);

  return (
    <section className="border-b border-line bg-white">
      <Container className="py-12 sm:py-14 lg:py-16">
        <Breadcrumb items={crumbs} />

        <div className="grid items-center gap-10 lg:grid-cols-[minmax(0,1.05fr)_minmax(0,0.95fr)] lg:gap-12">
          <div>
            <p className="text-[0.72rem] font-bold uppercase tracking-[0.24em] text-product-icon">
              {page.categoryLabel ?? "SOLUTION"}
            </p>
            <h1
              className={`mt-3 font-display text-4xl font-semibold tracking-tight sm:text-5xl lg:text-[3.35rem] lg:leading-[1.06] ${productHeadingClass("display")}`}
            >
              {page.displayName}
            </h1>
            {page.tagline ? (
              <p className="mt-4 max-w-xl text-lg font-semibold leading-snug text-product-icon/85">
                {page.tagline}
              </p>
            ) : null}
            <p className="mt-3 max-w-xl text-base leading-relaxed text-slate">
              {page.shortDescription}
            </p>

            <div className="mt-8 flex flex-wrap gap-3">
              <Button href={quoteUrl} variant="primary">
                Request Quote →
              </Button>
              <Button href="/contact" variant="ghost">
                Talk to a Specialist
              </Button>
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
            <div className="relative w-full max-w-lg overflow-hidden rounded-md border border-line bg-white shadow-soft">
              <ImageFrame
                src={page.heroImage.src}
                alt={page.heroImage.alt}
                spec={IMAGE_SPECS.solution}
                fill
                priority
                className="aspect-[16/10]"
                imageClassName="object-cover"
                sizes="(max-width: 1024px) 100vw, 42vw"
                showSizeLabel={false}
              />
            </div>
          </div>
        </div>
      </Container>
    </section>
  );
}
