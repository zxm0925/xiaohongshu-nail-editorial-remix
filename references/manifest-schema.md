# Manifest schema

The manifest is UTF-8 JSON.

## Batch fields

- `batch_id`: unique increasing ID.
- `processed_at`: ISO 8601 timestamp.
- `final_image_count`: number of final image items.
- `style`: short design-system description.
- `published`: boolean.
- `rights_status_default`: normally `unverified` until evidence exists.
- `items`: array of item objects.
- `contains_credentials`: must be false.
- `contains_private_tokens`: must be false.

## Item fields

- `item`, `note_id`, `author`, `title`, `link`.
- `source_paths`, `output_path`.
- `theme`, `theme_palette`, `hero_material`.
- `copy_lines`.
- `processing_status`, `rights_status`.
- `unresolved_issues`.

Use exact source credits. When a supporting image has another creator, record both the note author and image creator instead of collapsing them into one credit.

