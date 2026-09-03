import Link from "next/link";
import type { SuccessStory } from "@/types/content";

export function SuccessStoryAccordion({ stories }: { stories: SuccessStory[] }) {
  return (
    <div className="divide-y divide-line border-y border-line">
      {stories.map((story) => {
        const meta = [story.brand, story.industry, story.location]
          .filter(Boolean)
          .join(" · ");

        return (
          <details key={story.id} name="success-stories" className="group">
            <summary className="cursor-pointer list-none py-5 marker:content-none focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal">
              <span className="flex items-start justify-between gap-4">
                <span>
                  {meta ? (
                    <span className="mb-1 block text-[0.7rem] font-semibold uppercase tracking-[0.16em] text-signal-deep">
                      {meta}
                    </span>
                  ) : null}
                  <span className="block font-display text-xl font-semibold tracking-tight text-ink">
                    {story.title}
                  </span>
                </span>
                <span
                  aria-hidden="true"
                  className="mt-1 shrink-0 text-lg text-slate group-open:hidden"
                >
                  +
                </span>
                <span
                  aria-hidden="true"
                  className="mt-1 hidden shrink-0 text-lg text-slate group-open:inline"
                >
                  −
                </span>
              </span>
            </summary>

            <div className="pb-6">
              {story.customer ? (
                <p className="text-sm font-medium text-ink">{story.customer}</p>
              ) : null}
              <p className="mt-2 max-w-3xl text-base leading-relaxed text-slate">
                {story.summary}
              </p>
              <div className="mt-4 flex flex-wrap gap-x-5 gap-y-2">
                <Link
                  href={story.href}
                  className="text-sm font-semibold text-signal-deep underline-offset-4 hover:underline"
                >
                  Read full story
                </Link>
                {story.productSlug ? (
                  <Link
                    href={`/products/${story.productSlug}`}
                    className="text-sm font-semibold text-ink underline-offset-4 hover:underline"
                  >
                    View product
                  </Link>
                ) : null}
              </div>
            </div>
          </details>
        );
      })}
    </div>
  );
}
