import Link from "next/link";
import { siteConfig } from "@/config/site";
import { Container } from "@/components/ui/Container";
import { BrandLogo } from "@/components/ui/BrandLogo";
import { fetchBrands } from "@/lib/brand-service";

function brandColumnCount(linkCount: number) {
  if (linkCount > 12) {
    return 3;
  }

  if (linkCount > 5) {
    return 2;
  }

  return 1;
}

function splitIntoColumns<T>(items: T[], columnCount: number): T[][] {
  const perColumn = Math.ceil(items.length / columnCount);

  return Array.from({ length: columnCount }, (_, index) =>
    items.slice(index * perColumn, (index + 1) * perColumn)
  );
}

export async function SiteFooter() {
  const brands = await fetchBrands();
  const brandLinks = [
    { label: "All Brands", href: "/brands" },
    ...brands.map((brand) => ({
      label: brand.name,
      href: `/brands/${brand.slug}`,
    })),
  ];
  const columns = brandColumnCount(brandLinks.length);
  const brandLinkColumns = splitIntoColumns(brandLinks, columns);
  const staticColumns = siteConfig.footer.columns.filter(
    (column) => column.title !== "Brands"
  );

  const footerGridClass =
    columns === 3
      ? "grid gap-10 py-14 sm:grid-cols-2 lg:grid-cols-7"
      : columns === 2
        ? "grid gap-10 py-14 sm:grid-cols-2 lg:grid-cols-6"
        : "grid gap-10 py-14 sm:grid-cols-2 lg:grid-cols-5";

  return (
    <footer className="border-t border-paper/10 bg-ink text-paper">
      <Container className={footerGridClass}>
        <div className="sm:col-span-2 lg:col-span-1">
          <BrandLogo size="footer" />
          <p className="mt-4 max-w-xs text-sm leading-relaxed text-paper/68">
            {siteConfig.description}
          </p>
          <Link
            href="/contact"
            className="mt-5 inline-flex text-sm font-semibold text-signal-bright underline-offset-4 hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
          >
            Contact
          </Link>
        </div>

        {staticColumns.slice(0, 2).map((column) => (
          <FooterColumn key={column.title} title={column.title} links={column.links} />
        ))}

        <div
          className={
            columns === 3
              ? "lg:col-span-3"
              : columns === 2
                ? "lg:col-span-2"
                : undefined
          }
        >
          <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-bright">
            Brands
          </p>
          <div
            className={`mt-4 grid gap-x-8 ${
              columns === 3
                ? "grid-cols-2 sm:grid-cols-3"
                : columns === 2
                  ? "grid-cols-2"
                  : "grid-cols-1"
            }`}
          >
            {brandLinkColumns.map((columnLinks) => (
              <ul key={columnLinks[0]?.href ?? "empty"} className="space-y-3">
                {columnLinks.map((link) => (
                  <li key={link.href}>
                    <Link
                      href={link.href}
                      className="text-sm text-paper/70 transition hover:text-paper focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
                    >
                      {link.label}
                    </Link>
                  </li>
                ))}
              </ul>
            ))}
          </div>
        </div>

        {staticColumns.slice(2).map((column) => (
          <FooterColumn key={column.title} title={column.title} links={column.links} />
        ))}
      </Container>

      <Container className="flex flex-col gap-2 border-t border-paper/10 py-6 text-xs text-paper/45 sm:flex-row sm:items-center sm:justify-between">
        <p>
          © {new Date().getFullYear()} {siteConfig.legalName}. All rights
          reserved.
        </p>
        <p>Demo preview environment</p>
      </Container>
    </footer>
  );
}

function FooterColumn({
  title,
  links,
}: {
  title: string;
  links: readonly { label: string; href: string }[];
}) {
  return (
    <div>
      <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-bright">
        {title}
      </p>
      <ul className="mt-4 space-y-3">
        {links.map((link) => (
          <li key={link.href}>
            <Link
              href={link.href}
              className="text-sm text-paper/70 transition hover:text-paper focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
            >
              {link.label}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
