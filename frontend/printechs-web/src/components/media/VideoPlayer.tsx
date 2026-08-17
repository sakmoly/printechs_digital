import { withBasePath } from "@/lib/paths";

type VideoPlayerProps = {
  type: "youtube" | "hosted";
  source: string;
  title: string;
  poster?: string;
  className?: string;
};

export function VideoPlayer({
  type,
  source,
  title,
  poster,
  className = "",
}: VideoPlayerProps) {
  const posterSrc = poster ? withBasePath(poster) : undefined;
  if (type === "youtube") {
    return (
      <div className={`aspect-video overflow-hidden bg-ink ${className}`}>
        <iframe
          className="h-full w-full"
          src={`https://www.youtube-nocookie.com/embed/${source}`}
          title={title}
          loading="lazy"
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
        preload="metadata"
        poster={posterSrc}
        title={title}
      >
        <source src={source.startsWith("http") ? source : withBasePath(source)} />
        Your browser does not support the video tag.
      </video>
    </div>
  );
}
