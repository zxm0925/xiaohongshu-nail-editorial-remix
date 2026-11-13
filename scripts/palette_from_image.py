#!/usr/bin/env python3
"""Extract a quiet editorial palette from one nail image."""

import argparse
import json
from pathlib import Path

from PIL import Image


def mix(a, b, ratio):
    return tuple(round(a[i] * (1 - ratio) + b[i] * ratio) for i in range(3))


def hex_color(rgb):
    return "#" + "".join(f"{value:02X}" for value in rgb)


def palette(path):
    image = Image.open(path).convert("RGB")
    image.thumbnail((160, 160), Image.Resampling.LANCZOS)
    quantized = image.quantize(colors=12, method=Image.Quantize.MEDIANCUT)
    colors = sorted(quantized.getcolors(), reverse=True)
    raw = [quantized.getpalette()[index * 3:index * 3 + 3] for _, index in colors]
    useful = [tuple(c) for c in raw if 35 < sum(c) / 3 < 235]
    if not useful:
        useful = [tuple(raw[0])]
    dominant = useful[0]
    supporting = useful[min(1, len(useful) - 1)]
    accent = useful[min(2, len(useful) - 1)]
    return {
        "source": str(Path(path)),
        "dominant": hex_color(dominant),
        "supporting": hex_color(supporting),
        "accent_raw": hex_color(accent),
        "background": hex_color(mix(dominant, (248, 247, 243), 0.72)),
        "ink": hex_color(mix(supporting, (42, 40, 38), 0.38)),
        "accent": hex_color(mix(accent, (245, 243, 239), 0.48)),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    result = json.dumps(palette(args.image), ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(result + "\n", encoding="utf-8")
    else:
        print(result)


if __name__ == "__main__":
    main()

