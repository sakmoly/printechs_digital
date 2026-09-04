import { EventsPageView } from "@/components/company/EventsPageView";
import { buildMetadata } from "@/lib/seo";
import { fetchEventAlbums } from "@/lib/event-service";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type SearchParams = {
  type?: string;
};

export async function generateMetadata({ searchParams }: { searchParams: SearchParams }) {
  const suffix = searchParams.type ? ` — ${searchParams.type}` : "";
  return buildMetadata({
    title: `Events & Exhibitions${suffix} | Printechs`,
    description:
      "Photos from Printechs exhibitions, trade shows, Iftar gatherings, and team events across Saudi Arabia.",
    canonicalPath: "/company/events",
  });
}

export default async function EventsPage({ searchParams }: { searchParams: SearchParams }) {
  const { albums, eventTypes } = await fetchEventAlbums({
    eventType: searchParams.type,
  });

  return (
    <EventsPageView albums={albums} eventTypes={eventTypes} activeType={searchParams.type} />
  );
}
