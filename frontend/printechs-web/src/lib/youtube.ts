export function youtubeVideoId(url: string): string | null {
  const value = url.trim();
  if (!value) return null;

  const fromUrl = (parsed: URL): string | null => {
    const host = parsed.hostname.replace(/^www\./, "");
    if (host === "youtu.be") {
      return parsed.pathname.split("/").filter(Boolean)[0] || null;
    }
    if (host.endsWith("youtube.com") || host.endsWith("youtube-nocookie.com")) {
      if (parsed.pathname.startsWith("/embed/") || parsed.pathname.startsWith("/shorts/")) {
        return parsed.pathname.split("/")[2] || null;
      }
      return parsed.searchParams.get("v");
    }
    return null;
  };

  try {
    const parsed = new URL(value);
    const id = fromUrl(parsed);
    if (id) return id;
  } catch {
    // fall through to regex
  }

  const match = value.match(
    /(?:youtube\.com\/watch\?v=|youtu\.be\/|youtube\.com\/embed\/|youtube\.com\/shorts\/)([A-Za-z0-9_-]{6,})/,
  );
  return match?.[1] ?? null;
}
