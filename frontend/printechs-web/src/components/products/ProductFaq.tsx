import type { ProductFaqItem } from "@/types/content";
import { ProductSectionHeader } from "@/components/products/ProductSectionHeader";

type ProductFaqProps = {
  items: ProductFaqItem[];
};

export function ProductFaq({ items }: ProductFaqProps) {
  return (
    <div>
      <ProductSectionHeader
        eyebrow="FAQ"
        title="Frequently asked questions"
      />
      <div className="mt-6 divide-y divide-line border-y border-line">
        {items.map((item) => (
          <details key={item.question} className="group py-4">
            <summary className="cursor-pointer list-none text-base font-semibold text-ink marker:content-none focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal">
              <span className="flex items-start justify-between gap-4">
                {item.question}
                <span aria-hidden="true" className="text-slate group-open:hidden">
                  +
                </span>
                <span aria-hidden="true" className="hidden text-slate group-open:inline">
                  −
                </span>
              </span>
            </summary>
            <p className="mt-3 max-w-3xl text-base leading-relaxed text-slate">
              {item.answer}
            </p>
          </details>
        ))}
      </div>
    </div>
  );
}
