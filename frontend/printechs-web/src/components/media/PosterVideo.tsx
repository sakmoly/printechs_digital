"use client";

import { useState } from "react";
import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS } from "@/lib/image-specs";
import { withBasePath } from "@/lib/paths";

type PosterVideoProps = {
  type: "youtube" | "hosted";
  source: string;
  title: string;
  poster?: string;
  className?: string;
};

export function PosterVideo({
  type,
  source,
  title,
  poster,
  className = "",
}: PosterVideoProps) {
  const [playing, setPlaying] = useState(false);
  const posterSrc = poster
    ? withBasePath(poster)
    : "/images/placeholders/video-poster.svg";

  if (playing) {
    if (type === "youtube") {
      return (
        <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
          <iframe
            className="h-full w-full"
            src={`https://www.youtube-nocookie.com/embed/${source}?autoplay=1&rel=0`}
            title={title}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>
      );
    }

    return (
      <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
        <video
          className="h-full w-full object-cover"
          controls
          autoPlay
          preload="metadata"
          poster={withBasePath(posterSrc)}
          title={title}
        >
          <source src={withBasePath(source)} />
        </video>
      </div>
    );
  }

  return (
    <button
      type="button"
      onClick={() => setPlaying(true)}
      className={`group relative block aspect-video w-full overflow-hidden bg-ink text-left focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-signal ${className}`}
      aria-label={`Play video: ${title}`}
    >
      <ImageFrame
        src={posterSrc}
        alt=""
        spec={IMAGE_SPECS.videoPoster}
        fill
        className="h-full w-full"
        imageClassName="object-cover transition duration-700 ease-premium group-hover:scale-105"
        sizes="(max-width: 1280px) 100vw, 72rem"
        overlay={
          <>
            <div className="absolute inset-0 bg-ink/35 transition group-hover:bg-ink/25" />
            <span className="absolute left-1/2 top-1/2 flex h-16 w-16 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full bg-signal text-ink shadow-lift transition group-hover:scale-105 sm:h-20 sm:w-20">
              <span className="ml-1 border-y-[10px] border-l-[16px] border-y-transparent border-l-ink" />
            </span>
          </>
        }
      />
    </button>
  );
}
