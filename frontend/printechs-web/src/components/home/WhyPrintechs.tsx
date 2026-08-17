import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";

const points = [
  {
    title: "Industrial depth",
    body: "Coding, marking and identification expertise built around production realities.",
  },
  {
    title: "Retail systems",
    body: "Hardware and software that keep stores accurate, connected and serviceable.",
  },
  {
    title: "Enterprise software",
    body: "POS, ERP, WMS, loyalty and compliance platforms with local delivery support.",
  },
  {
    title: "Saudi focus",
    body: "Built for B2B customers operating across the Kingdom’s industrial and retail economy.",
  },
];

export function WhyPrintechs() {
  return (
    <Section tone="muted">
      <Heading
        eyebrow="Why Printechs"
        title="A partner for technology that has to work"
        description="Premium systems, practical delivery and long-term support — without marketplace clutter."
      />
      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {points.map((point, index) => (
          <article
            key={point.title}
            className="rounded-sm border border-line bg-white p-6 shadow-soft"
          >
            <p className="font-display text-sm font-semibold text-signal-deep">
              0{index + 1}
            </p>
            <h3 className="mt-4 font-display text-lg font-semibold text-ink">
              {point.title}
            </h3>
            <p className="mt-2 text-sm leading-relaxed text-slate">{point.body}</p>
          </article>
        ))}
      </div>
    </Section>
  );
}
