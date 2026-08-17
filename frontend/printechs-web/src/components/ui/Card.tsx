import Link from "next/link";
import type { ReactNode } from "react";

type CardProps = {
  href?: string;
  title: string;
  description: string;
  meta?: string;
  media?: ReactNode;
  cta?: string;
  /** Renders a trailing arrow with a subtle hover shift on linked cards. */
  ctaArrow?: boolean;
  className?: string;
};

export function Card({
  href,
  title,
  description,
  meta,
  media,
  cta = "Explore",
  ctaArrow = false,
  className = "",
}: CardProps) {
  const body = (
    <>
      {media ? (
        <div className="mb-5 overflow-hidden rounded-sm bg-mist">{media}</div>
      ) : null}
      <div className="flex flex-1 flex-col">
        <p className="mb-2 min-h-[1.125rem] text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
          {meta ?? "\u00A0"}
        </p>
        <h3 className="font-display text-xl font-semibold tracking-tight text-ink transition group-hover:text-signal-deep">
          {title}
        </h3>
        <p className="mt-2 flex-1 text-sm leading-relaxed text-slate">{description}</p>
        {href ? (
          <span className="mt-4 inline-flex items-center gap-1 text-sm font-semibold text-ink underline-offset-4 transition group-hover:text-signal-deep group-hover:underline">
            {cta}
            {ctaArrow ? (
              <span
                aria-hidden="true"
                className="transition-transform duration-300 ease-out group-hover:translate-x-1"
              >
                →
              </span>
            ) : null}
          </span>
        ) : null}
      </div>
    </>
  );

  const shared = `group flex h-full flex-col rounded-sm ${className}`;

  if (href) {
    return (
      <Link
        href={href}
        className={`${shared} focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal`}
      >
        {body}
      </Link>
    );
  }

  return <div className={shared}>{body}</div>;
}
