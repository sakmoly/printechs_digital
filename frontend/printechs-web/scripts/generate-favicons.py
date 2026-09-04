#!/usr/bin/env python3
"""Generate favicon assets from the official printechs.com favicon."""

from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "public/images/company/favicon-source.png"
APP_DIR = ROOT / "src/app"
MARK_SCALE = 0.92


def square_canvas(
    image: Image.Image,
    size: int,
    background=(255, 255, 255, 255),
    scale: float = MARK_SCALE,
) -> Image.Image:
    canvas = Image.new("RGBA", (size, size), background)
    image = image.copy()
    target = max(1, int(size * scale))
    image.thumbnail((target, target), Image.Resampling.LANCZOS)
    offset = ((size - image.width) // 2, (size - image.height) // 2)
    canvas.paste(image, offset, image)
    return canvas


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"Missing favicon source: {SOURCE}")

    mark = Image.open(SOURCE).convert("RGBA")
    APP_DIR.mkdir(parents=True, exist_ok=True)

    square_canvas(mark, 512).save(APP_DIR / "icon.png", optimize=True)
    square_canvas(mark, 180).save(APP_DIR / "apple-icon.png", optimize=True)

    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    ico_images = [square_canvas(mark, size).convert("RGBA") for size, _ in ico_sizes]
    ico_images[0].save(
        APP_DIR / "favicon.ico",
        format="ICO",
        sizes=ico_sizes,
        append_images=ico_images[1:],
    )

    print("Generated from official printechs.com favicon:")
    for path in (APP_DIR / "favicon.ico", APP_DIR / "icon.png", APP_DIR / "apple-icon.png"):
        print(f"  {path} ({path.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    main()
