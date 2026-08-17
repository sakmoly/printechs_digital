"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { siteConfig } from "@/config/site";
import { Container } from "@/components/ui/Container";
import { Button } from "@/components/ui/Button";
import { BrandLogo } from "@/components/ui/BrandLogo";

export function SiteHeader() {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 12);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [open]);

  return (
    <header
      className={`sticky top-0 z-50 border-b text-white transition duration-300 ease-premium ${
        scrolled || open
          ? "border-white/10 bg-ink shadow-soft"
          : "border-white/5 bg-ink"
      }`}
    >
      <Container className="flex h-16 items-center justify-between gap-4 !pl-4 sm:!pl-5 lg:h-[4.25rem] lg:!pl-6">
        <BrandLogo priority size="header" className="shrink-0" />

        <nav
          className="hidden flex-1 items-center justify-center gap-5 xl:gap-7 lg:flex"
          aria-label="Primary"
        >
          {siteConfig.navigation.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="relative whitespace-nowrap text-sm font-medium text-white/85 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal after:absolute after:-bottom-1 after:left-0 after:h-px after:w-0 after:bg-accent after:transition-all after:duration-300 hover:after:w-full"
            >
              {item.label}
            </Link>
          ))}
        </nav>

        <div className="hidden shrink-0 lg:block">
          <Button href={siteConfig.primaryCta.href} variant="primary">
            {siteConfig.primaryCta.label}
          </Button>
        </div>

        <button
          type="button"
          className="inline-flex min-h-11 min-w-11 items-center justify-center rounded-sm border border-white/25 px-3 text-sm font-medium text-white lg:hidden focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
          aria-expanded={open}
          aria-controls="mobile-nav"
          onClick={() => setOpen((value) => !value)}
        >
          <span className="sr-only">Toggle navigation</span>
          {open ? "Close" : "Menu"}
        </button>
      </Container>

      {open ? (
        <div id="mobile-nav" className="border-t border-white/10 bg-ink lg:hidden">
          <Container className="flex max-h-[calc(100vh-4rem)] flex-col gap-1 overflow-y-auto py-4">
            {siteConfig.navigation.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                className="rounded-sm px-2 py-3.5 text-base text-white/90 hover:bg-white/5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
                onClick={() => setOpen(false)}
              >
                {item.label}
              </Link>
            ))}
            <div className="pt-3">
              <Button
                href={siteConfig.primaryCta.href}
                variant="primary"
                className="w-full"
              >
                {siteConfig.primaryCta.label}
              </Button>
            </div>
          </Container>
        </div>
      ) : null}
    </header>
  );
}
