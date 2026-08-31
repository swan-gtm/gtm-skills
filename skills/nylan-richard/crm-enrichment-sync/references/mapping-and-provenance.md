# Mapping and provenance model

Every proposed mapping has four columns: source, destination, transform, and write policy.

## Default contact mappings

- First and last name → contact name fields → trim and preserve Unicode → create or fill-if-empty.
- Verified work email → primary work email → lowercase → create or fill-if-empty; conflict-review if different.
- Direct or mobile phone → matching phone type → normalize international format → fill-if-empty.
- Current title → job title → trim → fill-if-empty; conflict-review when different.
- Company domain → account association key → normalize domain → match only unless company creation was separately approved.
- Professional profile URL → dedicated profile field → canonicalize URL → create or fill-if-empty.
- Enrichment source and retrieval time → source metadata fields or note → no destructive transform → append.

## Provenance minimum

Persist, in fields or the external sync ledger:

- source system;
- retrieved-at timestamp;
- verification or confidence class;
- source row ID;
- sync-run ID;
- original non-empty value when a conflict exists.

## Type checks

- Validate picklist values against the destination options.
- Never place multi-value source data into a scalar field without a declared selection rule.
- Never coerce unknown into false, zero, or an empty string.
- Preserve country and timezone semantics during phone and location normalization.
