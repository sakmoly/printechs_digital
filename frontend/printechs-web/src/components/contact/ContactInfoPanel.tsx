import Link from "next/link";
import type { ContactSpecialistPanel } from "@/types/content";

function phoneHref(phone: string) {
  const first = phone.split("|")[0]?.trim() ?? phone.trim();
  return `tel:${first.replace(/\s/g, "")}`;
}

function WhatsAppIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden className="h-5 w-5 shrink-0 fill-current">
      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.435 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413Z" />
    </svg>
  );
}

export function ContactInfoPanel({ specialist }: { specialist: ContactSpecialistPanel }) {
  const { pricing, whatsapp } = specialist;

  return (
    <aside className="rounded-sm border border-line bg-mist p-6 lg:p-8">
      <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
        {specialist.eyebrow}
      </p>
      <h2 className="mt-2 font-display text-2xl font-semibold text-ink">{specialist.title}</h2>
      <p className="mt-3 text-sm leading-relaxed text-slate">{specialist.description}</p>

      <dl className="mt-8 space-y-5 text-sm">
        <div>
          <dt className="font-semibold text-ink">Email</dt>
          <dd className="mt-1">
            <Link
              href={`mailto:${specialist.email}`}
              className="text-signal-deep underline-offset-4 hover:underline"
            >
              {specialist.email}
            </Link>
          </dd>
        </div>
        <div>
          <dt className="font-semibold text-ink">Phone</dt>
          <dd className="mt-1">
            <Link
              href={phoneHref(specialist.phone)}
              className="text-signal-deep underline-offset-4 hover:underline"
            >
              {specialist.phone}
            </Link>
          </dd>
        </div>
        <div>
          <dt className="font-semibold text-ink">Location</dt>
          <dd className="mt-1 text-slate">{specialist.location}</dd>
        </div>
        <div>
          <dt className="font-semibold text-ink">Office hours</dt>
          <dd className="mt-1 text-slate">{specialist.officeHours}</dd>
        </div>
      </dl>

      {whatsapp ? (
        <div className="mt-8">
          <a
            href={whatsapp.href}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex min-h-11 w-full items-center justify-center gap-2 rounded-sm bg-[#25D366] px-5 py-2.5 text-sm font-semibold tracking-wide text-white shadow-soft transition duration-300 ease-premium hover:bg-[#20bd5a] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#25D366] focus-visible:ring-offset-2"
          >
            <WhatsAppIcon />
            {whatsapp.label}
          </a>
        </div>
      ) : null}

      <div className="mt-8 border-t border-line pt-6">
        <p className="text-sm font-semibold text-ink">{pricing.title}</p>
        <p className="mt-2 text-sm text-slate">
          Use{" "}
          <Link
            href={pricing.linkHref}
            className="font-semibold text-signal-deep hover:underline"
          >
            {pricing.linkLabel}
          </Link>{" "}
          {pricing.description}
        </p>
      </div>
    </aside>
  );
}
