# Evidence map — verified patents and leaked fields

A starter set that ties common on-page actions to the ranking mechanism behind them, with a Google patent and/or a field from the leaked Search API documentation as the receipt. Not exhaustive — extend it with the verification method below. For each candidate quick win, find the matching row, cite the ID/field, and confirm it before it goes in the deliverable.

## What each kind of evidence proves

- A **patent** shows how Google has described *thinking about* a problem. It does not prove the approach is live in ranking, or how heavily it is weighted.
- A **leaked field** comes from Google's internal "Content Warehouse" Search API reference — a catalog of roughly 2,596 modules and 14,014 fields describing what Google can store for documents, sites, links, and interactions. A field shows Google *stores or can consider* a signal. It does not reveal ranking weight, scoring, or even that a field is in active use — no weightings appear anywhere in the corpus.

Say which one you hold. Never let a patent or a stored field become a claim about live weighting.

## How to verify (and the anti-fabrication rule)

- **Patent:** open a patent search, load the number, and confirm it resolves to a Google-assigned patent with the stated title. Several SEO-famous patents are mis-cited (see the last section) — confirm, don't trust memory.
- **Field:** find the field on the public Content Warehouse API documentation mirror (module pages named `GoogleApi.ContentWarehouse.V1.Model.<Module>`) and read its description. Field naming is inconsistent — some snake_case, some camelCase — so search the module page rather than trusting a remembered spelling.
- If a number does not resolve, or a field is not in the docs, **do not cite it.** Present it as a hypothesis or drop it. Never approximate a patent number or invent a field name.

---

## 1. Match the title to the query

- **Action:** front-load the core query term in the title, keep it specific, drop boilerplate.
- **Mechanism:** the title is what earns the click, and title-to-query match is a stored signal.
- **Field:** `titlematchScore` (module `QualityNsrNsrData`) — *"Titlematch score of the site, a signal that tells how well titles are matching user queries."* Described at the **site** level, not strictly per-page.
- **Patent (supporting):** `US8938463B1` — the click a good title earns feeds ranking (see row 2). There is no clean, standalone Google **title-matching** patent; do not invent one.

## 2. Earn and keep the click

- **Action:** write titles and descriptions that set accurate expectations (fewer pogo-stick returns to the results page); make the above-the-fold answer fast and complete so the visit becomes the satisfying, last, longest click.
- **Mechanism:** click behaviour adjusts ranking, discounted for the fact that higher positions get more clicks regardless of relevance — so genuine post-click satisfaction is what the model isolates.
- **Patent:** `US8938463B1` — *"Modifying search result ranking based on implicit user feedback and a model of presentation bias"* (Google LLC).
- **Fields:** `goodClicks`, `badClicks`, `lastLongestClicks` (module `QualityNavboostCrapsCrapsClickSignals`, the NavBoost / "Craps" click system). The field **names** are present in the module; the mirror carries no description text for them, so the good-vs-bad and last-longest reading is analyst interpretation (iPullRank, SparkToro), not a doc quote. Cite it that way.

## 3. Make thin content original and high-effort

- **Action:** on thin or short pages, add genuinely original material — first-hand analysis, unique data, original media — and visible effort, not restated aggregate text.
- **Mechanism:** a site-level quality factor demotes low-quality resources; originality is scored most pointedly where content is sparse.
- **Patent:** `US8682892B1` — *"Ranking search results"* (Google LLC; inventor Navneet Panda — the "Panda" quality work).
- **Fields:** `OriginalContentScore` (module `PerDocData`) — *"The original content score is represented as a 7-bits, going from 0 to 127."* (iPullRank adds that only pages with little content carry this field). `contentEffort` (module `QualityNsrPQData`) — *"LLM-based effort estimation for article pages."*

## 4. Cover the topic, not just the keyword

- **Action:** cover a topic with its naturally related terms and subtopics; stop repeating one exact-match keyword.
- **Mechanism:** ranking works on meaningful phrases and their co-occurring related phrases, not isolated keywords.
- **Patent:** `US7536408B2` — *"Phrase-based indexing in an information retrieval system"* (Google LLC; inventor Anna Lynn Patterson).
- **Fields:** `chard_score_encoded` and `chard_score_variance` (module `QualityNsrNsrData`) — *"Site-level Chard (encoded as an int)."* / *"Site-level Chard Variance for all pages of a site."* "Chard" is a described content-quality predictor exposed through these fields; there is no field literally named `chard`.

## 5. Use honest, descriptive, well-placed links

- **Action:** place key internal links prominently (in the body, higher up, meaningful anchor text), not buried in boilerplate; keep anchor text — internal and inbound — descriptive and topically aligned with the destination.
- **Mechanism:** links are weighted by how likely a reader is to click them, and anchor text matched to the query contributes to the target's ranking; mismatched anchors are demoted.
- **Patents:** `US7716225B1` — *"Ranking documents based on user behavior and/or feature data"* (Google LLC; the "reasonable surfer" — links weighted by click likelihood via position, font size, anchor characteristics). `US7260573B1` — *"Personalizing anchor text scores in a search engine"* (Google LLC).
- **Field:** `anchor_mismatch_demotion` (module `CompressedQualitySignals`) — *"converted from QualityBoost.mismatched.boost."*

## 6. Signal genuine freshness, not fake dates

- **Action:** keep the on-page date, structured-data date, and displayed date consistent; signal real recency in the body (in-text dates, current references, updated facts and links), not just a changed timestamp.
- **Mechanism:** time-based signals — inception date, update frequency and amount, link/anchor growth — factor into scoring, and the content date is estimated from the content itself, not merely declared.
- **Patent:** `US7346839B2` — *"Information retrieval based on historical data"* (Google LLC; inventors include Matt Cutts and Jeff Dean).
- **Fields:** `semanticDate` (module `PerDocData`) — *"estimated date of the content of a document based on the contents of the document (via parsing), anchors and related documents."* `bylineDate` (module `QualityTimebasedSyntacticDate`) — set only when the byline date differs from the main date field (per iPullRank, it is the date shown in snippets).

## 7. Build site-level authority and topical focus

- **Action:** concentrate topical content, internal links, and quality on one domain rather than fragmenting across microsites; keep new pages semantically close to the site's core topic. Page-level wins accrue to a stronger site.
- **Mechanism:** a site-level quality/authority signal modifies page scores, and topical focus is measured as how far pages drift from the site's centre.
- **Patent:** `US8682892B1` — *"Ranking search results"* (site-level quality modification).
- **Fields:** `site_authority` (module `CompressedQualitySignals`) — *"converted from quality_nsr.SiteAuthority, applied in Qstar."* `siteFocusScore` — *"Number denoting how much a site is focused on one topic."* and `siteRadius` — *"The measure of how far page_embeddings deviate from the site_embedding."* (both in `QualityAuthorityTopicEmbeddingsVersionedItem`, alongside `siteEmbedding` — *"Compressed site/page embeddings."*). `chromeInTotal` (module `QualityNsrNsrData`) — *"Site-level Chrome views."* (a behavioural signal on-page work alone cannot manufacture).

## 8. Mind domain and new-site cautions

- **Action:** do not lean on a keyword-stuffed exact-match domain; for a new host, expect a slow start and prioritise clean, high-effort content and links over aggressive tactics.
- **Fields:** `exact_match_domain_demotion` (module `CompressedQualitySignals`) — *"converted from QualityBoost.emd.boost."* `hostAge` (module `PerDocData`) — *"The earliest firstseen date of all pages in this host/domain. These data are used in twiddler to sandbox fresh spam in serving time."* This one field is the only in-corpus evidence for a "sandbox"; do not assert a dedicated sandbox score.

---

## Do not mis-cite (checked, and wrong in the wild)

- `US7739277B2` — *"System and method for incorporating anchor text into ranking search results"* is **Microsoft**, not Google. It circulates in SEO posts as Google's anchor-text patent. It is not — cite `US7260573B1` for anchor text instead.
- `US6285999B1` — *"Method for node ranking in a linked database"* (PageRank; inventor Lawrence Page) was originally assigned to **Stanford**, with Google holding an exclusive licence; it has since expired. If you cite it, get the Stanford origin right — and note it is link-graph ranking, not an on-page quick win.
- The Panda patent `US8682892B1` is titled only *"Ranking search results"* — the "Panda" association is through inventor Navneet Panda, not the title. Use the granted number, not the application `US20120143789A1`.
- For historical data, use the granted `US7346839B2`, not the application number `US20050071741A1`.

## Naming caveats carried from the corpus

- `panda_demotion` exists in `CompressedQualitySignals`, but its description references `baby_panda_demotion` (*"converted from QualityBoost.rendered.boost."*), and separate baby-Panda fields also appear — the Panda / Baby-Panda naming is muddled in the corpus. Report the field you actually find.
- Some fields render snake_case (`site_authority`) and some camelCase (`titlematchScore`, `hostAge`) across the mirror. Always confirm the exact spelling on the module page.
