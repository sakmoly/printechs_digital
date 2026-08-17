import Link from "next/link";
import type { ReactNode } from "react";

type ButtonVariant = "primary" | "secondary" | "ghost" | "on-dark";

type ButtonProps = {
  href: string;
  children: ReactNode;
  variant?: ButtonVariant;
  className?: string;
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

export function Button({
  href,
  children,
  variant = "primary",
  className = "",
}: ButtonProps) {
  return (
    <Link
      href={href}
      className={`inline-flex min-h-11 items-center justify-center rounded-sm px-5 py-2.5 text-sm font-semibold tracking-wide transition duration-300 ease-premium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2 focus-visible:ring-offset-transparent ${variants[variant]} ${className}`}
    >
      {children}
    </Link>
  );
}
