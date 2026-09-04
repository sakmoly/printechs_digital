import { notFound } from "next/navigation";
import { EventAlbumView } from "@/components/company/EventsPageView";
import { buildMetadata } from "@/lib/seo";
import {
  fetchEventAlbum,
  fetchEventAlbumSlugs,
} from "@/lib/event-service";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

export const revalidate = REVALIDATE_SECONDS;

type Props = { params: { slug: string } };

export async function generateStaticParams() {
  const slugs = await fetchEventAlbumSlugs();
  return slugs.map((slug) => ({ slug }));
}

export async function generateMetadata({ params }: Props) {
  const album = await fetchEventAlbum(params.slug);
  if (!album) {
    return buildMetadata({
      title: "Event | Printechs",
      description: "Event photos from Printechs.",
    });
  }
  return buildMetadata(album.seo);
}

export default async function EventAlbumPage({ params }: Props) {
  const album = await fetchEventAlbum(params.slug);
  if (!album) notFound();

  return <EventAlbumView album={album} />;
}
