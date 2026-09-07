"use client";

import Link from "next/link";
import { useEffect, useState } from "react";
import { siteConfig } from "@/config/site";
import { Container } from "@/components/ui/Container";
import { BrandLogo } from "@/components/ui/BrandLogo";
import {
  HeaderActionButton,
  WhatsAppIcon,
} from "@/components/navigation/HeaderActionButton";
import type { HeaderContactActions } from "@/lib/header-contact";

const navLinkClass =
  "relative whitespace-nowrap text-sm font-medium text-white/85 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal after:absolute after:-bottom-1 after:left-0 after:h-px after:w-0 after:bg-accent after:transition-all after:duration-300 hover:after:w-full";

const mobileNavLinkClass =
  "rounded-sm px-2 py-3.5 text-base text-white/90 hover:bg-white/5 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal";

function NavItem({
  href,
  label,
  mobile = false,
  onNavigate,
}: {
  href: string;
  label: string;
  mobile?: boolean;
  onNavigate?: () => void;
}) {
  const className = mobile ? mobileNavLinkClass : navLinkClass;

  if (href.startsWith("mailto:") || href.startsWith("tel:")) {
    return (
      <a href={href} className={className} onClick={onNavigate}>
        {label}
      </a>
    );
  }

  return (
    <Link href={href} className={className} onClick={onNavigate}>
      {label}
    </Link>
  );
}

function HeaderWhatsAppButton({
  contact,
  className = "",
  fullWidth = false,
}: {
  contact: HeaderContactActions;
  className?: string;
  fullWidth?: boolean;
}) {
  const widthClass = fullWidth ? "w-full" : "";

  if (!contact.whatsapp) return null;

  return (
    <div className={className}>
      <HeaderActionButton
        href={contact.whatsapp.href}
        variant="whatsapp"
        size="compact"
        external
        className={widthClass}
      >
        <WhatsAppIcon className="h-3.5 w-3.5" />
        {contact.whatsapp.label}
      </HeaderActionButton>
    </div>
  );
}

export function SiteHeader({ contact }: { contact: HeaderContactActions }) {
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
            <NavItem key={item.href} href={item.href} label={item.label} />
          ))}
        </nav>

        <div className="hidden shrink-0 lg:block">
          <HeaderWhatsAppButton contact={contact} />
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
              <NavItem
                key={item.href}
                href={item.href}
                label={item.label}
                mobile
                onNavigate={() => setOpen(false)}
              />
            ))}
            <div className="pt-3">
              <HeaderWhatsAppButton contact={contact} fullWidth />
            </div>
          </Container>
        </div>
      ) : null}
    </header>
  );
}
