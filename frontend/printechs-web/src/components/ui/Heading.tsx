import type { ReactNode } from "react";

type HeadingProps = {
  eyebrow?: string;
  title: string;
  description?: string;
  align?: "left" | "center";
  tone?: "light" | "dark";
  children?: ReactNode;
  className?: string;
};

export function Heading({
  eyebrow,
  title,
  description,
  align = "left",
  tone = "dark",
  children,
  className = "",
}: HeadingProps) {
  const alignClass = align === "center" ? "mx-auto text-center items-center" : "";
  const titleColor = tone === "light" ? "text-paper" : "text-ink";
  const descColor = tone === "light" ? "text-paper/72" : "text-slate";
  const eyeColor = tone === "light" ? "text-signal-bright" : "text-signal-deep";

  return (
    <div className={`mb-10 flex max-w-3xl flex-col gap-4 md:mb-12 ${alignClass} ${className}`}>
      {eyebrow ? (
        <p className={`text-[0.7rem] font-semibold uppercase tracking-[0.2em] ${eyeColor}`}>
          {eyebrow}
        </p>
      ) : null}
      <h2
        className={`font-display text-balance text-3xl font-semibold tracking-tight sm:text-4xl lg:text-[2.75rem] lg:leading-[1.15] ${titleColor}`}
      >
        {title}
      </h2>
      {description ? (
        <p className={`max-w-2xl text-base leading-relaxed sm:text-lg ${descColor}`}>
          {description}
        </p>
      ) : null}
      {children}
    </div>
  );
}
