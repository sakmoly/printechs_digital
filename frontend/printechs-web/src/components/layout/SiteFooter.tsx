import Link from "next/link";
import { siteConfig } from "@/config/site";
import { Container } from "@/components/ui/Container";
import { BrandLogo } from "@/components/ui/BrandLogo";

export function SiteFooter() {
  return (
    <footer className="border-t border-paper/10 bg-ink text-paper">
      <Container className="grid gap-10 py-14 sm:grid-cols-2 lg:grid-cols-5">
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

        {siteConfig.footer.columns.map((column) => (
          <div key={column.title}>
            <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-bright">
              {column.title}
            </p>
            <ul className="mt-4 space-y-3">
              {column.links.map((link) => (
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
