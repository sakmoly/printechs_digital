import Link from "next/link";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";

const companyLinks = [
  {
    title: "About Printechs",
    description:
      "Our story, divisions, and lifecycle support across industrial, retail, and software.",
    href: "/company/about",
    cta: "About us",
  },
  {
    title: "Events & Exhibitions",
    description:
      "Photos from trade shows, exhibitions, Iftar gatherings, and team events.",
    href: "/company/events",
    cta: "View events",
  },
  {
    title: "Brand Partners",
    description:
      "Authorized distribution and support for leading global technology brands.",
    href: "/brands",
    cta: "View brands",
  },
  {
    title: "Contact",
    description: "Offices in Riyadh, Jeddah, and Dammam — talk to a specialist.",
    href: "/contact",
    cta: "Contact us",
  },
];

export function CompanyPageView() {
  return (
    <>
      <PageIntro
        title="Company"
        description="Printechs is a Saudi technology partner for industrial coding, retail systems, and enterprise software — established in 2002."
        crumbs={[{ label: "Home", href: "/" }, { label: "Company" }]}
      />

      <Section tone="white">
        <div className="grid gap-4 md:grid-cols-2">
          {companyLinks.map((item) => (
            <article
              key={item.href}
              className="flex h-full flex-col rounded-sm border border-line bg-mist p-6 sm:p-7"
            >
              <h2 className="font-display text-xl font-semibold tracking-tight text-ink">
                {item.title}
              </h2>
              <p className="mt-3 flex-1 text-sm leading-relaxed text-slate sm:text-base">
                {item.description}
              </p>
              <Link
                href={item.href}
                className="mt-5 inline-flex text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
              >
                {item.cta}
              </Link>
            </article>
          ))}
        </div>

        <div className="mt-10 flex flex-wrap gap-3">
          <Button href="/request-quote" variant="primary">
            Request Quote
          </Button>
          <Button href="/success-stories" variant="ghost">
            Success Stories
          </Button>
        </div>
      </Section>
    </>
  );
}
