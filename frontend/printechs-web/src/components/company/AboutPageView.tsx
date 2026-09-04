import Link from "next/link";
import type { AboutPageContent } from "@/types/content";
import { PageIntro } from "@/components/ui/PageIntro";
import { Section } from "@/components/ui/Section";
import { Button } from "@/components/ui/Button";
import { CTA } from "@/components/ui/CTA";

const coreAreas = [
  {
    title: "Industrial Automation",
    summary: "Coding, marking, labeling, traceability and production identification.",
    href: "/solutions/coding-marking",
  },
  {
    title: "Retail Technology",
    summary: "POS, Auto-ID, mobility, barcode, ESL and weighing systems.",
    href: "/solutions/retail-automation",
  },
  {
    title: "Business Software",
    summary: "ERPNext, POS, WMS, BI, integration and custom development.",
    href: "/software",
  },
];

const locations = ["Riyadh", "Jeddah", "Dammam"];

const supportItems = [
  "Application consultation",
  "Installation and commissioning",
  "Integration and training",
  "Preventive maintenance",
  "Technical support and spare parts",
];

export function AboutPageView({ content }: { content: AboutPageContent }) {
  const [leadParagraph, ...bodyParagraphs] = content.paragraphs;

  return (
    <>
      <PageIntro
        title={content.title}
        description={content.tagline}
        crumbs={[
          { label: "Home", href: "/" },
          { label: "Company", href: "/company" },
          { label: "About" },
        ]}
      />

      <Section tone="white" pad="compact">
        <ul className="grid gap-4 md:grid-cols-3">
          {coreAreas.map((area) => (
            <li
              key={area.title}
              className="rounded-sm border border-line bg-mist p-5 sm:p-6"
            >
              <h2 className="font-display text-lg font-semibold tracking-tight text-ink">
                {area.title}
              </h2>
              <p className="mt-2 text-sm leading-relaxed text-slate">{area.summary}</p>
              <Link
                href={area.href}
                className="mt-4 inline-flex text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
              >
                Explore
              </Link>
            </li>
          ))}
        </ul>
      </Section>

      <Section tone="white">
        <div className="grid gap-10 lg:grid-cols-12 lg:gap-12">
          <div className="lg:col-span-8">
            {leadParagraph ? (
              <p className="text-lg leading-relaxed text-ink sm:text-xl">{leadParagraph}</p>
            ) : null}
            <div className="mt-6 space-y-5">
              {bodyParagraphs.map((paragraph) => (
                <p
                  key={paragraph.slice(0, 48)}
                  className="text-base leading-relaxed text-slate sm:text-[1.05rem]"
                >
                  {paragraph}
                </p>
              ))}
            </div>
          </div>

          <aside className="lg:col-span-4">
            <div className="space-y-4 lg:sticky lg:top-24">
              <div className="rounded-sm border border-line bg-mist p-5">
                <p className="text-[0.7rem] font-semibold uppercase tracking-[0.2em] text-signal-deep">
                  Established
                </p>
                <p className="mt-2 font-display text-3xl font-semibold tracking-tight text-ink">
                  Since 2002
                </p>
                <p className="mt-2 text-sm leading-relaxed text-slate">
                  Supporting businesses across Saudi Arabia with reliable technology and local
                  delivery.
                </p>
              </div>

              <div className="rounded-sm border border-line bg-white p-5 shadow-soft">
                <p className="text-[0.7rem] font-semibold uppercase tracking-[0.2em] text-signal-deep">
                  Locations
                </p>
                <ul className="mt-3 space-y-2 text-sm font-semibold text-ink">
                  {locations.map((city) => (
                    <li key={city} className="flex items-center gap-2">
                      <span className="h-1.5 w-1.5 rounded-full bg-signal" />
                      {city}
                    </li>
                  ))}
                </ul>
              </div>

              <div className="rounded-sm border border-line bg-white p-5 shadow-soft">
                <p className="text-[0.7rem] font-semibold uppercase tracking-[0.2em] text-signal-deep">
                  Lifecycle support
                </p>
                <ul className="mt-3 space-y-2 text-sm leading-relaxed text-slate">
                  {supportItems.map((item) => (
                    <li key={item} className="flex gap-2">
                      <span className="mt-2 h-1 w-1 shrink-0 rounded-full bg-signal" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="flex flex-wrap gap-3">
                <Button href="/contact" variant="primary">
                  Contact Us
                </Button>
                <Button href="/solutions" variant="ghost">
                  Explore Solutions
                </Button>
                {content.profileDownload ? (
                  <a
                    href={content.profileDownload.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex min-h-11 items-center justify-center rounded-sm border border-ink/12 bg-transparent px-5 py-2.5 text-sm font-semibold tracking-wide text-ink shadow-soft transition duration-300 ease-premium hover:border-ink/30 hover:bg-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal focus-visible:ring-offset-2"
                  >
                    {content.profileDownload.label}
                  </a>
                ) : null}
              </div>
            </div>
          </aside>
        </div>

        {content.closingLine ? (
          <div className="mt-12 rounded-sm bg-ink px-6 py-8 sm:px-8 sm:py-10">
            <p className="max-w-4xl font-display text-2xl font-semibold tracking-tight text-paper sm:text-3xl">
              {content.closingLine}
            </p>
          </div>
        ) : null}
      </Section>

      <Section tone="muted">
        <CTA
          title="Talk to a Printechs specialist"
          description="Request a quote, book a demo, or plan a site visit with our team in Saudi Arabia."
          primaryLabel="Contact Us"
          primaryHref="/contact"
          secondaryLabel="Explore Solutions"
          secondaryHref="/solutions"
        />
      </Section>
    </>
  );
}
