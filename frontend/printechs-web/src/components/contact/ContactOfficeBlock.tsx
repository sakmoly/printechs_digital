import Link from "next/link";
import type { ContactOffice } from "@/types/content";

function PhoneIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden className="h-5 w-5 shrink-0 text-signal-deep">
      <path
        fill="none"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.75"
        d="M8.5 4.5h-1A2.5 2.5 0 0 0 5 7v10a2.5 2.5 0 0 0 2.5 2.5h11A2.5 2.5 0 0 0 21 17V7a2.5 2.5 0 0 0-2.5-2.5h-1"
      />
      <path
        fill="none"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.75"
        d="M9 3h6v3H9z"
      />
    </svg>
  );
}

function EmailIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden className="h-5 w-5 shrink-0 text-accent">
      <path
        fill="none"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.75"
        d="M4 7.5A2.5 2.5 0 0 1 6.5 5h11A2.5 2.5 0 0 1 20 7.5v9A2.5 2.5 0 0 1 17.5 19h-11A2.5 2.5 0 0 1 4 16.5v-9Z"
      />
      <path
        fill="none"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.75"
        d="m5 7 7 5 7-5"
      />
    </svg>
  );
}

function LocationIcon() {
  return (
    <svg viewBox="0 0 24 24" aria-hidden className="h-5 w-5 shrink-0 text-signal-deep">
      <path
        fill="none"
        stroke="currentColor"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.75"
        d="M12 21s6-5.2 6-10a6 6 0 1 0-12 0c0 4.8 6 10 6 10Z"
      />
      <circle cx="12" cy="11" r="2.25" fill="none" stroke="currentColor" strokeWidth="1.75" />
    </svg>
  );
}

function phoneHref(phone: string) {
  const digits = phone.replace(/[^\d+]/g, "");
  const first = digits.split("|")[0]?.trim();
  return first ? `tel:${first.replace(/\s/g, "")}` : undefined;
}

export function ContactOfficeBlock({
  office,
  reverse = false,
}: {
  office: ContactOffice;
  reverse?: boolean;
}) {
  const tel = office.phone ? phoneHref(office.phone) : undefined;

  return (
    <div
      className={`grid gap-8 lg:grid-cols-2 lg:items-stretch lg:gap-10 ${
        reverse ? "lg:[&>*:first-child]:order-2" : ""
      }`}
    >
      <div className="rounded-sm border border-line bg-white p-6 shadow-sm sm:p-8">
        <h2 className="font-display text-2xl font-semibold tracking-tight text-ink sm:text-3xl">
          Connect With Printechs {office.city}.
        </h2>

        <dl className="mt-8 space-y-5 text-sm">
          {office.phone ? (
            <div className="flex gap-3">
              <dt className="sr-only">Phone</dt>
              <PhoneIcon />
              <dd>
                {tel ? (
                  <Link
                    href={tel}
                    className="text-slate underline-offset-4 hover:text-signal-deep hover:underline"
                  >
                    {office.phone}
                  </Link>
                ) : (
                  <span className="text-slate">{office.phone}</span>
                )}
              </dd>
            </div>
          ) : null}

          {office.email ? (
            <div className="flex gap-3">
              <dt className="sr-only">Email</dt>
              <EmailIcon />
              <dd>
                <Link
                  href={`mailto:${office.email}`}
                  className="text-slate underline-offset-4 hover:text-signal-deep hover:underline"
                >
                  {office.email}
                </Link>
              </dd>
            </div>
          ) : null}

          {office.address ? (
            <div className="flex gap-3">
              <dt className="sr-only">Address</dt>
              <LocationIcon />
              <dd className="leading-relaxed text-slate">{office.address}</dd>
            </div>
          ) : null}
        </dl>
      </div>

      {office.mapEmbedUrl ? (
        <div className="overflow-hidden rounded-sm border border-line bg-white shadow-sm">
          <iframe
            title={`Printechs ${office.city} location map`}
            src={office.mapEmbedUrl}
            className="aspect-[600/350] h-full min-h-[280px] w-full border-0"
            loading="lazy"
            referrerPolicy="no-referrer-when-downgrade"
            allowFullScreen
          />
        </div>
      ) : null}
    </div>
  );
}
