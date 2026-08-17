import { ImageFrame } from "@/components/media/ImageFrame";
import { IMAGE_SPECS, type ImageSpec } from "@/lib/image-specs";

type ResponsiveImageProps = {
  src: string;
  alt: string;
  spec?: ImageSpec;
  width?: number;
  height?: number;
  className?: string;
  priority?: boolean;
};

export function ResponsiveImage({
  src,
  alt,
  spec = IMAGE_SPECS.industry,
  width = 960,
  height = 640,
  className = "",
  priority = false,
}: ResponsiveImageProps) {
  return (
    <ImageFrame
      src={src}
      alt={alt}
      spec={spec}
      width={width}
      height={height}
      priority={priority}
      className={className}
      imageClassName="h-auto w-full object-cover"
    />
  );
}
