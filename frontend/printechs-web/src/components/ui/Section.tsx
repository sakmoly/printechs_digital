import type { ReactNode } from "react";
import { Container } from "./Container";

type SectionProps = {
  children: ReactNode;
  className?: string;
  id?: string;
  tone?: "default" | "muted" | "ink" | "white";
  flush?: boolean;
};

const toneClass: Record<NonNullable<SectionProps["tone"]>, string> = {
  default: "bg-paper text-ink",
  white: "bg-white text-ink",
  muted: "bg-mist text-ink",
  ink: "bg-ink text-paper",
};

export function Section({
  children,
  className = "",
  id,
  tone = "default",
  flush = false,
}: SectionProps) {
  return (
    <section
      id={id}
      className={`section-pad ${toneClass[tone]} ${className}`}
    >
      {flush ? children : <Container>{children}</Container>}
    </section>
  );
}
