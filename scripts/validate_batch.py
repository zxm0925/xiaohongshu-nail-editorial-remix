#!/usr/bin/env python3
"""Validate a remix batch manifest and its final image files."""

import argparse
import json
from pathlib import Path

from PIL import Image


REQUIRED = {"item", "author", "title", "link", "output_path", "theme", "theme_palette", "rights_status"}


def resolve_output(root, manifest_path, value):
    path = Path(value)
    if path.is_absolute():
        return path
    candidate = root / path
    if candidate.exists():
        return candidate
    return manifest_path.parent / path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    errors = []
    items = data.get("items", [])
    if data.get("final_image_count") != len(items):
        errors.append("final_image_count does not match items length")
    themes = []
    backgrounds = []
    for number, item in enumerate(items, 1):
        missing = sorted(REQUIRED - item.keys())
        if missing:
            errors.append(f"item {number}: missing {', '.join(missing)}")
            continue
        themes.append(item["theme"])
        backgrounds.append(str(item["theme_palette"].get("background")))
        output = resolve_output(args.root, args.manifest, item["output_path"])
        if not output.exists():
            errors.append(f"item {number}: output missing: {output}")
        else:
            with Image.open(output) as image:
                if image.width < 1000 or image.height < 1400:
                    errors.append(f"item {number}: output too small: {image.size}")
        if not item.get("author") or not item.get("title"):
            errors.append(f"item {number}: empty source credit")
    if len(themes) != len(set(themes)):
        errors.append("theme names repeat within the batch")
    if len(backgrounds) != len(set(backgrounds)):
        errors.append("background palettes repeat within the batch")
    if data.get("contains_credentials") is not False:
        errors.append("contains_credentials must be false")
    print(json.dumps({"valid": not errors, "items": len(items), "errors": errors}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
