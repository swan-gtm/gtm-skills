---
title: "Per-format LinkedIn benchmarks"
description: "Reference for the LinkedIn ads & ABM audit skill."
---

# Per-format LinkedIn benchmarks

Source: ZenABM's 2026 LinkedIn ABM Benchmarks Report (B2B SaaS). Full report:
https://zenabm.com/linkedin-abm-benchmarks-report

These are the medians you grade the user's live numbers against. **Higher is better** for CTR, effective CTR to
LP and dwell time; **lower is better** for CPC, effective CPC to LP and CPM.

| LinkedIn ad format     |   CTR |    CPC | Effective CTR to LP | Effective CPC to LP |    CPM | Dwell time |
| ---------------------- | ----: | -----: | ------------------: | ------------------: | -----: | ---------: |
| **Thought Leader Ads** | 2.68% |  $2.29 |               0.29% |               $3.06 | $49.37 |      6.63s |
| **Single Image Ads**   | 0.42% | $13.23 |               0.42% |              $13.23 | $59.15 |      3.64s |
| **Lead Gen Form Ads**  | 0.45% | $12.33 |               0.00% | n/a — $811.09 / lead| $75.59 |      3.18s |
| **Carousel Ads**       | 0.32% | $13.30 |               0.31% |              $13.30 | $45.28 |      4.56s |
| **Document Ads**       | 0.30% | $12.05 |               0.00% |                 n/a | $72.02 |      3.15s |
| **Video Ads**          | 0.24% | $15.61 |               0.24% |              $15.61 | $38.94 |      3.91s |

Notes on reading the table:

- **Thought Leader Ads are the headline value play** — ~2.7% CTR and a $3.06 effective cost per landing-page
  click, roughly 4x cheaper per LP click than image ads. If a user is under-investing in TLAs, that is almost
  always the single biggest fix.
- **Single Image Ads:** CTR and effective CTR to LP are the same because a standard image ad's click *is* the
  landing-page click. Same for Carousel and Video. So for those formats, CTR ≈ effective CTR to LP and CPC ≈
  effective CPC to LP — small differences come from non-LP clicks (likes, profile clicks) being stripped out.
- **Lead Gen Form and Document ads have no outbound landing page**, so effective CTR to LP is ~0 and effective CPC
  to LP is n/a. **Do not grade these on LP metrics.** Judge Lead Gen Forms on **cost per lead** (benchmark
  **$811.09/lead**) and Documents on CTR, CPM and dwell.
- **TLAs are split by whether they carry a link.** A TLA with no link in the post cannot produce landing-page
  clicks, so its effective-to-LP metrics are n/a — mark them "no link", not a failure. Only TLAs with a link get
  graded on the 0.29% / $3.06 effective columns.
- **Dwell time** may not be returned by the connector. Include the column only when the data has it; otherwise
  omit it from the report rather than showing blanks.

## Pause thresholds (for the decay / prune check)

Once an ad has **1,000+ impressions**, judge it on CTR vs its format median and flag it to pause if it falls below
~two-thirds of the median:

| Format   | Median CTR | Pause below (after 1,000+ impressions) |
| -------- | ---------: | -------------------------------------: |
| TLA      |      2.68% |                                  ~1.8% |
| Image    |      0.42% |                                  ~0.30% |
| Carousel |      0.32% |                                  ~0.21% |
| Document |      0.30% |                                  ~0.20% |
| Video    |      0.24% |                                  ~0.16% |

An ad is **decaying** if its weekly CTR has dropped three weeks in a row, OR it is below the pause threshold for
its format after clearing 1,000 impressions. Both are report-worthy; the second is the more urgent.

## Which metric decides the grade

**For link-driving formats (Single Image, Carousel, Video), the deciding cost metric is effective CPC to LP
(`cost / landingPageClicks`), not raw CPC.** Compare it to the format's effective-CPC-to-LP benchmark above
(Image $13.23, Carousel $13.30, Video $15.61). Raw CPC is secondary context. This is because raw CPC bills for
non-landing-page clicks (likes, reactions, expands) that never reach the site, so it understates the true cost of
a real visit. TLAs are graded on both (raw CPC $2.29 and effective CPC to LP $3.06), because the two diverge
sharply. Lead-gen and document ads have no LP and are graded on cost-per-lead / CTR / CPM instead.

## Grading convention

For each metric, mark a **pass** when the user is at or better than benchmark, a **flag** when worse. Use a
neutral dash "—" for n/a metrics (no-link TLAs, LP metrics on lead-gen/document). Keep the marks consistent so a
reader can skim the scorecard and know instantly what to fix.
