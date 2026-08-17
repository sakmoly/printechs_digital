import type { Video } from "@/types/content";
import { Section } from "@/components/ui/Section";
import { Heading } from "@/components/ui/Heading";
import { PosterVideo } from "@/components/media/PosterVideo";

export function VideoSection({ video }: { video: Video }) {
  return (
    <Section tone="ink">
      <Heading
        eyebrow="Digital experience"
        title={video.title}
        description={video.summary}
        tone="light"
      />
      <PosterVideo
        type={video.video.type}
        source={video.video.source}
        title={video.video.title}
        poster={video.video.poster}
      />
    </Section>
  );
}
