import type { ResolvedSolutionCategory } from "@/lib/solution-service";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";
import { Card } from "@/components/ui/Card";
import { FeatureGrid } from "@/components/ui/FeatureGrid";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";

type SolutionCategoryProductsProps = {
  categories: ResolvedSolutionCategory[];
};

export function SolutionCategoryProducts({
  categories,
}: SolutionCategoryProductsProps) {
  return (
    <div className="space-y-16">
      {categories.map(({ category, products }) => (
        <section
          key={category.slug}
          id={category.slug}
          className="scroll-mt-28"
        >
          <ProductSectionHeader
            eyebrow="Products"
            title={category.title}
            description={category.description}
          />
          {products.length > 0 ? (
            <div className="mt-8">
              <FeatureGrid columns={products.length > 2 ? 3 : 2}>
              {products.map((product) => (
                <Card
                  key={product.slug}
                  href={`/products/${product.slug}`}
                  title={product.name}
                  description={product.summary}
                  meta={product.brand}
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
            </div>
          ) : (
            <p className="mt-6 text-base text-slate">
              Product listings for this category will be published soon. Contact
              Printechs for specifications and availability.
            </p>
          )}
        </section>
      ))}
    </div>
  );
}
