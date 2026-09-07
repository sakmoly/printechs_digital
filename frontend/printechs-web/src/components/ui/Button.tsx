"use client";

import Link from "next/link";
import type { MouseEvent, ReactNode } from "react";

type ButtonVariant = "primary" | "secondary" | "ghost" | "on-dark";

type ButtonProps = {
  href: string;
  children: ReactNode;
  variant?: ButtonVariant;
  className?: string;
  analyticsEvent?: string;
  analyticsLocation?: string;
  analyticsProduct?: string;
  analyticsBrand?: string;
  analyticsCategory?: string;
  analyticsSolution?: string;
};

const variants: Record<ButtonVariant, string> = {
  primary:
    "bg-signal text-white hover:bg-signal-bright focus-visible:ring-signal shadow-soft",
  secondary:
    "border border-paper/35 bg-transparent text-paper hover:border-paper hover:bg-paper/10 focus-visible:ring-paper",
  "on-dark":
    "border border-paper/30 bg-paper text-ink hover:bg-white focus-visible:ring-paper",
  ghost:
    "border border-ink/12 bg-transparent text-ink hover:border-ink/30 hover:bg-white focus-visible:ring-signal",
};

function scrollToHash(href: string): void {
  const id = href.startsWith("#") ? href.slice(1) : href.split("#")[1];
  if (!id) return;

  const scroll = () => {
    const target = document.getElementById(decodeURIComponent(id));
    if (!target) return false;
    target.scrollIntoView({ behavior: "smooth", block: "start" });
    window.history.replaceState(null, "", `#${id}`);
    return true;
  };

  if (scroll()) return;

  let attempts = 0;
  const retry = window.setInterval(() => {
    attempts += 1;
    if (scroll() || attempts >= 15) {
      window.clearInterval(retry);
    }
  }, 100);
}

function handleHashClick(event: MouseEvent<HTMLAnchorElement>, href: string) {
  event.preventDefault();
  scrollToHash(href);
}

export function Button({
  href,
  children,
  variant = "primary",
  className = "",
  analyticsEvent,
  analyticsLocation,
  analyticsProduct,
  analyticsBrand,
  analyticsCategory,
  analyticsSolution,
}: ButtonProps) {
  const sharedProps = {
    "data-analytics-event": analyticsEvent,
    "data-analytics-location": analyticsLocation,
    "data-analytics-product": analyticsProduct,
    "data-analytics-brand": analyticsBrand,
    "data-analytics-category": analyticsCategory,
    "data-analytics-solution": analyticsSolution,
    className: `inline-flex min-h-11 items-center justify-center rounded-sm px-5 py-2.5 text-sm font-semibold tracking-wide transition duration-300 ease-premium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-transparent ${variants[variant]} ${className}`,
  };

  if (href.startsWith("#")) {
    return (
      <a href={href} onClick={(event) => handleHashClick(event, href)} {...sharedProps}>
        {children}
      </a>
    );
  }

  return (
    <Link href={href} {...sharedProps}>
      {children}
    </Link>
  );
}
