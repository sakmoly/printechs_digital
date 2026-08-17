import Link from "next/link";
import { Button } from "./Button";
import { Heading } from "./Heading";

type CTAProps = {
  title?: string;
  description?: string;
  primaryLabel?: string;
  primaryHref?: string;
  secondaryLabel?: string;
  secondaryHref?: string;
};

export function CTA({
  title = "Talk to a Printechs specialist",
  description = "Request a quote, book a demo, or plan a site visit with our team in Saudi Arabia.",
  primaryLabel = "Request Quote",
  primaryHref = "/request-quote",
  secondaryLabel = "Request Demo",
  secondaryHref = "/request-demo",
}: CTAProps) {
  return (
    <div className="relative overflow-hidden rounded-sm bg-steel px-6 py-12 sm:px-10 lg:px-14 lg:py-16">
      <div className="pointer-events-none absolute -right-16 top-0 h-64 w-64 rounded-full bg-signal/10 blur-3xl" />
      <div className="relative">
        <Heading
          title={title}
          description={description}
          tone="light"
          align="left"
          className="mb-8"
        />
        <div className="flex flex-wrap items-center gap-3">
          <Button href={primaryHref} variant="primary">
            {primaryLabel}
          </Button>
          <Button href={secondaryHref} variant="secondary">
            {secondaryLabel}
          </Button>
          <Link
            href="/contact"
            className="ml-1 text-sm font-semibold text-paper/75 underline-offset-4 transition hover:text-paper hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal"
          >
            Contact Printechs
          </Link>
        </div>
      </div>
    </div>
  );
}
