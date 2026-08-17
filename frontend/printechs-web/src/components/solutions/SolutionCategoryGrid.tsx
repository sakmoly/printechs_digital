import Link from "next/link";
import type { SolutionPageContent } from "@/types/content";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";

type SolutionCategoryGridProps = {
  categories: SolutionPageContent["productCategories"];
};

export function SolutionCategoryGrid({ categories }: SolutionCategoryGridProps) {
  return (
    <div>
      <ProductSectionHeader
        eyebrow="Technologies"
        title="Choose your marking technology"
        description="Select a category to view compatible products. Printechs will help you match the right system to your line speed, substrate and compliance requirements."
      />
      <ul className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {categories.map((category) => (
          <li key={category.slug}>
            <Link
              href={`#${category.slug}`}
              className="group block overflow-hidden rounded-md border border-line bg-white shadow-soft transition duration-300 hover:-translate-y-0.5 hover:border-product-icon/30 hover:shadow-lift focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              <ImageFrame
                src={category.image.src}
                alt={category.image.alt}
                spec={IMAGE_SPECS.product}
                fill
                className="aspect-[4/3] bg-mist"
                imageClassName="object-contain p-6 transition duration-500 group-hover:scale-[1.02]"
                sizes="(max-width: 768px) 100vw, 33vw"
                showSizeLabel={false}
              />
              <div className="bg-product-icon px-4 py-3 text-center">
                <p className="font-display text-sm font-semibold text-white sm:text-base">
                  {category.shortTitle ?? category.title}
                </p>
              </div>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
