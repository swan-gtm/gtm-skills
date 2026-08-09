# Prompt file contract

The output is one file the user uploads into their AI-visibility platform's prompt importer. Exact column names, engine codes, and region codes are defined by **your** platform — treat the shape below as a representative contract and adapt the enums to whatever your importer accepts.

## Columns

A row is one monitoring prompt. A workable column set:

| Column | Purpose |
|---|---|
| `prompt` | The question, written the way a real buyer asks an assistant, in the row's language. No fabricated brand names in non-branded rows. |
| `description` | Short human summary, e.g. `<persona> · <source>`. |
| `topic` | One of the few category topics, or the single branded topic. |
| `is_branded` | `true` only for brand-pass rows. |
| `awareness_stage` | Awareness / consideration / decision. Skew to consideration + decision. |
| `platforms` | Which assistants to monitor this prompt on — a subset of the engines your platform supports. |
| `regions` | Region codes supported by your platform, and only codes whose primary language matches this row's language. |
| `persona`, `icp`, `key_source`, `reason`, `language` | Documentation columns: who asks, the segment, honest provenance, why it matters, and the prompt's language. |

Keep the operational columns (prompt, topic, branded flag, stage, engines, regions) aligned to what the importer actually reads; the rest document the research for human review.

## Provenance labels (be honest)

`social:<community>` · `keyword:<term>` · `sales_transcript` · `competitor:<name>` · `brand_page` (brand pass only). Every row carries one.

## Language and region rules

- Generate the prompt text **once per language**, in that language — translate, don't machine-localize spelling.
- A row's `regions` may only contain codes whose primary language equals the row's `language`. English text can group all English-primary regions; German text is German-market only; and so on.
- Bilingual B2B markets (e.g. tech audiences that search in English even in a non-English country) are a judgment call — confirm with the user, and if they want native coverage, add native-language rows *in addition to*, not instead of, the English ones.
- If a requested region isn't supported by the platform, say so and drop or remap it.

## Engine rules

- Assign **2–4 engines per prompt**, varied across the set so monitoring isn't skewed to one.
- Lean technical personas toward research-style engines; business/exec personas toward mainstream assistants and search-embedded answers; decision-stage "best / alternatives" queries toward the search-embedded engines that surface them heavily.
- Only include engines you actually monitor — don't add one you can't track.

## Validation before handoff

Parse the file and assert: header matches the contract; valid UTF-8 (non-ASCII languages are expected); no empty prompt; branded flag and awareness stage in their allowed sets; every engine and region in the platform's allowed enums; each row's regions all share its language; no duplicate prompt text; a small number of category topics plus at most one branded topic. Then print the distributions (per topic, persona, awareness stage, language/region, branded vs non-branded) and show the user before finalizing. Keep the total reasonable (roughly 60–200 prompts) unless the user asks for more — authenticity beats volume.
