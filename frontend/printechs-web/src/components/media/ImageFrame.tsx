import Image from "next/image";
import type { ReactNode } from "react";
import {
  shouldShowImageSizeLabel,
  type ImageSpec,
} from "@/lib/image-specs";
import { withBasePath } from "@/lib/paths";

type ImageFrameBaseProps = {
  src: string;
  alt: string;
  spec: ImageSpec;
  className?: string;
  imageClassName?: string;
  priority?: boolean;
  showSizeLabel?: boolean;
  overlay?: ReactNode;
};

type FillImageFrameProps = ImageFrameBaseProps & {
  fill: true;
  sizes: string;
  width?: never;
  height?: never;
};

type FixedImageFrameProps = ImageFrameBaseProps & {
  fill?: false;
  width: number;
  height: number;
  sizes?: never;
};

export type ImageFrameProps = FillImageFrameProps | FixedImageFrameProps;

function SizeLabel({ spec }: { spec: ImageSpec }) {
  return (
    <div className="pointer-events-none absolute inset-x-0 top-0 z-20 flex justify-center p-2 sm:p-3">
      <div className="rounded-sm bg-paper/95 px-3 py-1.5 text-center shadow-soft ring-1 ring-line backdrop-blur-sm">
        <p className="font-mono text-xs font-bold tabular-nums text-ink sm:text-sm">
          {spec.label}
        </p>
        {spec.ratio ? (
          <p className="mt-0.5 text-[0.6rem] font-semibold uppercase tracking-[0.14em] text-slate sm:text-[0.65rem]">
            {spec.ratio}
          </p>
        ) : null}
      </div>
    </div>
  );
}

export function ImageFrame(props: ImageFrameProps) {
  const {
    src,
    alt,
    spec,
    className = "",
    imageClassName = "object-cover",
    priority = false,
    showSizeLabel,
    overlay,
  } = props;

  const resolvedSrc = withBasePath(src);
  const showLabel = shouldShowImageSizeLabel(src, showSizeLabel);

  return (
    <div className={`relative overflow-hidden ${className}`}>
      {"fill" in props && props.fill ? (
        <Image
          src={resolvedSrc}
          alt={alt}
          fill
          priority={priority}
          className={imageClassName}
          sizes={props.sizes}
        />
      ) : (
        <Image
          src={resolvedSrc}
          alt={alt}
          width={props.width}
          height={props.height}
          priority={priority}
          className={imageClassName}
        />
      )}

      {showLabel ? <SizeLabel spec={spec} /> : null}
      {overlay}
    </div>
  );
}
