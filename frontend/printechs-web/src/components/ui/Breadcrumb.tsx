import Link from "next/link";

export type Crumb = { label: string; href?: string };

export function Breadcrumb({
  items,
  className = "mb-6",
}: {
  items: Crumb[];
  className?: string;
}) {
  return (
    <nav aria-label="Breadcrumb" className={className}>
      <ol className="flex flex-wrap items-center gap-2 text-sm text-slate">
        {items.map((item, index) => {
          const isLast = index === items.length - 1;
          return (
            <li key={`${item.label}-${index}`} className="flex items-center gap-2">
              {item.href && !isLast ? (
                <Link
                  href={item.href}
                  className="hover:text-ink focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
                >
                  {item.label}
                </Link>
              ) : (
                <span className={isLast ? "text-ink" : undefined} aria-current={isLast ? "page" : undefined}>
                  {item.label}
                </span>
              )}
              {!isLast ? <span aria-hidden="true">/</span> : null}
            </li>
          );
        })}
      </ol>
    </nav>
  );
}
