# Contact-file field mapping

Map by meaning and evidence, not header similarity.

## Identity fields

- `source_row_id`: stable identifier added before cleaning.
- `profile_url_raw` and `profile_url_normalized`: preserve original and canonical URL.
- `full_name_raw`: original display value.
- `first_name_normalized`, `last_name_normalized`: populate only when parsing is defensible.
- `company_name_raw`: original company value.
- `company_domain_normalized`: lowercase domain with protocol and `www` removed.

Preferred identity order:

1. canonical professional-profile URL;
2. existing verified work email;
3. normalized full name plus company domain;
4. normalized full name plus unambiguous company name.

Rows below level 4 need review rather than blind lookup.

## Result fields

Append rather than replace:

- `work_email_candidate`
- `work_email_status`
- `phone_candidate`
- `phone_status`
- `enrichment_source`
- `enriched_at`
- `enrichment_job_id`
- `enrichment_note`

If the original field is empty and the result meets the approved quality threshold, copy the candidate into the delivery column. If the original is non-empty and differs, preserve both and set `enrichment_note = conflict_review`.

## Duplicate handling

Assign a `duplicate_group_id`. Look up one canonical identity per group, but return every source row. Duplicate removal is a separate user decision.
