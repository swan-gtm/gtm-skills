---
name: company-domain-resolver
title: Company domain resolver
description: |
  Use this skill when you have a list of company names — a CSV, CRM export,
  event attendee list, or pasted prospecting list — and need website domains
  before enrichment, dedupe, or CRM import. Produces the original list with a
  resolved domain and a per-row match-confidence label, using the free, keyless
  Clearbit autocomplete endpoint. Trigger on "find the domains for these
  companies", "what's the website for X", "clean up this company list",
  "resolve these company names", "add domains to this CSV", "company name to
  domain", or Clearbit autocomplete/suggest. Also applies proactively when a
  company list is missing domains and the next step needs them.
category: Prospecting
tags: [Sales, RevOps]
contributors: []
---

Applies whenever a company list has names but no domains and the next step —
enrichment, dedupe, CRM import — needs them. Produces the same list back with
`resolved_domain`, `matched_name`, a confidence label per row, and the rows
that need human review called out, never a bare domain list.

## The play

1. **Get the input and confirm the column.** Accept a CSV/TSV, plain-text
   list, or names pasted in chat. For a CSV, name the company column
   explicitly. Over ~40 names, tell the user each name is one HTTP call and
   confirm before starting.
2. **Resolve via the free Clearbit autocomplete endpoint** —
   `https://autocomplete.clearbit.com/v1/companies/suggest?query=<name>`. No
   key, no auth, up to 5 matches best-guess first, `[]` on no match. It is an
   undocumented typeahead, not a contracted API: keep volume modest, pace
   requests, and read `references/endpoint-behavior.md` before your first
   batch — it covers the two failure modes that silently corrupt lists.
3. **For one or two names**, query directly with your agent's web-fetch tool
   and report matches inline, flagging when several results share a name.
4. **For a batch**, use the resolver script in
   `references/resolver-script.md`. It runs plan → fetch → merge: dedupes on a
   normalized key, strips legal suffixes before querying, then scores every
   row. If the environment blocks direct HTTP, the script's plan output lists
   the URLs so you can fetch them with your agent's web-fetch tool (5–8 in
   parallel per batch) and feed the responses back to the merge step.
5. **Score every row.** Confidence labels and what they mean:

   | confidence | meaning | review |
   |---|---|---|
   | `exact` | name and domain both match, ranked first | no |
   | `strong` | exactly one result's domain matches the name | no |
   | `plausible` | same slug on several TLDs; picked the gTLD | spot-check |
   | `ambiguous` | several same-named companies, different domains | yes |
   | `weak` | nothing lined up; top result is a guess | yes |
   | `none` | empty response — not in the index | yes |

6. **Report, don't just deliver a file.** Give counts per confidence level and
   list the specific rows needing review with their alternatives. If `weak`
   plus `none` exceed a third of the list, say so plainly — the input is
   likely full of internal shorthand, DBA names, or companies the index
   doesn't cover. For those rows, offer (don't auto-run) a web search on
   `"<company name>" official site` as a second pass.
7. **Hand off.** Domains are the join key for enrichment and CRM dedupe. For
   people-level data (titles, emails, profiles), pass the resolved domains to
   a real enrichment step — this endpoint returns name and domain only.

## What good looks like

- The best operator distrusts the top result by default. This endpoint always
  returns *something* for common words — "Clay" returns five
  Clayton-somethings and no Clay — so a bare domain list with no confidence
  column is malpractice, not a deliverable.
- The common mistake is querying names as-is. Legal suffixes wreck results:
  "Stripe Inc." returns `stripe-inc.jp` (wrong company), "Bright Data Ltd"
  returns nothing, while "Stripe" and "Bright Data" both resolve cleanly.
  Strip trailing Inc/Ltd/LLC/GmbH/Corp/Holdings/Group before every query.
- Good output is auditable: every original column preserved, every row
  labeled, alternatives shown for ambiguous rows, and the review burden
  quantified up front ("41 exact/strong, 6 need review, here they are") —
  never a 30% weak-match rate buried in a file.

## Rules

- MUST attach a confidence label to every resolved row — never hand back a
  bare name→domain list.
- MUST record empty responses as explicit no-matches, distinct from rows that
  were never fetched — those are different problems with different fixes.
- NEVER write `weak`, `ambiguous`, or `none` rows into a CRM unattended;
  resolve them with the user first.
- NEVER present this endpoint's output as authoritative company data or
  promise logos from it — it is a best-effort typeahead index.
