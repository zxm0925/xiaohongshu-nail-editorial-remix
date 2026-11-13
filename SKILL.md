---
name: xiaohongshu-nail-editorial-remix
description: Turn credited Xiaohongshu nail-art source images into asymmetric editorial scrapbook collages with asset-specific palettes, distinct decorative themes, preserved attribution, and batch manifests. Use for nail remix batches, collage redesigns, or requests to follow this credited two-image editorial system; do not use for reposting without source records or for unrelated beauty graphics.
---

# Xiaohongshu Nail Editorial Remix

Create a nail-first editorial collage, not a generic social template.

## Required outcome

- Preserve the source identity: exact author name, original title, source link, and any visible creator or return-image credit.
- Use one dominant nail-focused image at upper left and one supporting image at lower right. Keep sparse whitespace and purposeful overlap.
- Derive each design's background, ink, and accent colors from that manicure. Soften and desaturate supporting colors so the nails remain dominant.
- Give every item in a batch its own material story. Do not reuse the same hero sticker, flower, bow, butterfly, or theme color across multiple items unless the user explicitly requests a series motif.
- Keep decorative objects outside the critical nail area. Use at most three or four small supporting objects plus one simple line doodle.
- Keep editorial commentary separate from the original title. Commentary may bridge the photo/background boundary but must not look like original source copy.
- Do not add engagement counts, fake UI, invented personal experience, or unsupported product claims.

## Workflow

1. Record every input image, source URL, requested image number, author, title, and known permission basis.
2. Select only crops that clearly show nail color, texture, decoration, or a meaningful hand pose. Reject video frames, blurred crops, or redundant third images when the user requests a two-image layout.
3. Preserve authentic source identity. Prefer cropping the original header/title from a supplied screenshot instead of redrawing it.
4. Sample the manicure palette. Use `scripts/palette_from_image.py` when a deterministic starting palette helps, then refine visually.
5. Name a material theme that explains the manicure rather than merely matching color, such as `icy crystal`, `amber coffee`, `pearl shell`, or `smoky lace`.
6. Check the rest of the current batch before choosing stickers. A new item must not duplicate another item's hero material.
7. Compose at portrait social size, normally 1440 x 1920. Keep the upper-left source card dominant, the lower-right supporting image secondary, and the commentary in open space.
8. Inspect the rendered image at full size. Verify nail visibility, source text, credit placement, title cropping, sticker edges, and color harmony.
9. Save a new batch folder without overwriting earlier work. Include images, `manifest.json`, and a source-comparison Markdown file.
10. Run `scripts/validate_batch.py` before delivery.

## Routing

- Read [references/design-system.md](references/design-system.md) when selecting palettes, stickers, type, or layout.
- Read [references/workflow.md](references/workflow.md) when building a full batch or adapting the system to new source material.
- Read [references/manifest-schema.md](references/manifest-schema.md) when creating or validating batch metadata.
- Read [references/rights-and-credits.md](references/rights-and-credits.md) before publication, commercial use, or public portfolio release.

## Publishing boundary

Local collage creation does not imply permission to publish. Keep rights status explicit. Do not label a result ready to publish while source-image, personality, music, trademark, or platform-label requirements remain unresolved.
