import type { ReactNode } from "react";
import { Container } from "./Container";

type SectionProps = {
  children: ReactNode;
  className?: string;
  id?: string;
  tone?: "default" | "muted" | "ink" | "white";
  flush?: boolean;
  /** default = homepage spacing; compact = tighter rhythm for long detail pages */
  pad?: "default" | "compact";
};

const toneClass: Record<NonNullable<SectionProps["tone"]>, string> = {
  default: "bg-paper text-ink",
  white: "bg-white text-ink",
  muted: "bg-mist text-ink",
  ink: "bg-ink text-paper",
};

const padClass = {
  default: "section-pad",
  compact: "section-pad-compact",
};

export function Section({
  children,
  className = "",
  id,
  tone = "default",
  flush = false,
  pad = "default",
}: SectionProps) {
  return (
    <section
      id={id}
      className={`${padClass[pad]} ${toneClass[tone]} ${className}`}
    >
      {flush ? children : <Container>{children}</Container>}
    </section>
  );
}
