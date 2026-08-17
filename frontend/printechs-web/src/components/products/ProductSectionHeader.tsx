import {
  productEyebrowClass,
  productHeadingClass,
} from "@/lib/product-page-theme";

type ProductSectionHeaderProps = {
  eyebrow: string;
  title: string;
  description?: string;
  className?: string;
};

export function ProductSectionHeader({
  eyebrow,
  title,
  description,
  className = "",
}: ProductSectionHeaderProps) {
  return (
    <div className={className}>
      <p
        className={`text-[0.7rem] font-semibold uppercase tracking-[0.18em] ${productEyebrowClass()}`}
      >
        {eyebrow}
      </p>
      <h2
        className={`mt-2 font-display text-3xl font-semibold tracking-tight ${productHeadingClass("section")}`}
      >
        {title}
      </h2>
      {description ? (
        <p className="mt-3 max-w-3xl text-base leading-relaxed text-slate">
          {description}
        </p>
      ) : null}
    </div>
  );
}
