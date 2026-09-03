import Link from "next/link";
import { siteConfig } from "@/config/site";

export function ContactInfoPanel() {
  return (
    <aside className="rounded-sm border border-line bg-mist p-6 lg:p-8">
      <p className="text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
        Printechs
      </p>
      <h2 className="mt-2 font-display text-2xl font-semibold text-ink">
        Talk to a specialist
      </h2>
      <p className="mt-3 text-sm leading-relaxed text-slate">
        Industrial coding, retail technology, and enterprise software across Saudi Arabia.
      </p>

      <dl className="mt-8 space-y-5 text-sm">
        <div>
          <dt className="font-semibold text-ink">Email</dt>
          <dd className="mt-1">
            <Link
              href={`mailto:${siteConfig.contactEmail}`}
              className="text-signal-deep underline-offset-4 hover:underline"
            >
              {siteConfig.contactEmail}
            </Link>
          </dd>
        </div>
        <div>
          <dt className="font-semibold text-ink">Phone</dt>
          <dd className="mt-1">
            <Link
              href={`tel:${siteConfig.contactPhone.replace(/\s/g, "")}`}
              className="text-signal-deep underline-offset-4 hover:underline"
            >
              {siteConfig.contactPhone}
            </Link>
          </dd>
        </div>
        <div>
          <dt className="font-semibold text-ink">Location</dt>
          <dd className="mt-1 text-slate">{siteConfig.contactLocation}</dd>
        </div>
        <div>
          <dt className="font-semibold text-ink">Office hours</dt>
          <dd className="mt-1 text-slate">{siteConfig.officeHours}</dd>
        </div>
      </dl>

      <div className="mt-8 border-t border-line pt-6">
        <p className="text-sm font-semibold text-ink">Looking for pricing?</p>
        <p className="mt-2 text-sm text-slate">
          Use{" "}
          <Link href="/products" className="font-semibold text-signal-deep hover:underline">
            Products
          </Link>{" "}
          to open a product and request a quote with the correct item context.
        </p>
      </div>
    </aside>
  );
}
