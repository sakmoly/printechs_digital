import { cache } from "react";
import type { EventAlbum, EventAlbumList, MediaAsset } from "@/types/content";
import { erpnextMethod, normalizeMediaAsset } from "@/lib/erpnext-client";
import { REVALIDATE_SECONDS } from "@/lib/revalidate";

function normalizeEventAlbum(album: EventAlbum): EventAlbum {
  return {
    ...album,
    image: normalizeMediaAsset(album.image),
    gallery: album.gallery?.map(normalizeMediaAsset),
  };
}

export const fetchEventAlbums = cache(async (filters: {
  eventType?: string;
} = {}): Promise<EventAlbumList> => {
  const fromErp = await erpnextMethod<EventAlbumList>(
    "printechs_digital.api.website.list_event_albums",
    {
      event_type: filters.eventType,
    },
    REVALIDATE_SECONDS,
  );

  if (!fromErp) {
    return { albums: [], eventTypes: [] };
  }

  return {
    albums: fromErp.albums.map(normalizeEventAlbum),
    eventTypes: fromErp.eventTypes,
  };
});

export async function fetchEventAlbum(slug: string): Promise<EventAlbum | undefined> {
  const fromErp = await erpnextMethod<EventAlbum>(
    "printechs_digital.api.website.get_event_album",
    { slug },
    REVALIDATE_SECONDS,
  );

  return fromErp ? normalizeEventAlbum(fromErp) : undefined;
}

export async function fetchEventAlbumSlugs(): Promise<string[]> {
  return (
    (await erpnextMethod<string[]>(
      "printechs_digital.api.website.get_event_album_slugs",
      {},
      REVALIDATE_SECONDS,
    )) ?? []
  );
}

export type { MediaAsset };
