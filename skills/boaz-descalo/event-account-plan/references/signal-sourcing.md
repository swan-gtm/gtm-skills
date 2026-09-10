# Signal sourcing

Firmographics decide *which* accounts. Signals decide *why now*, and why-now is
what makes a rep pick up the phone in the two weeks before a show. Read this
before the first batch of connector calls — every trap below costs hours if you
rediscover it live.

## The signal hierarchy

Get as many as the connectors allow, in this order of value:

1. **Tech-stack tags for the vendor's own product and for every named
   competitor.** The single highest-value query in the pipeline. Own product →
   existing customer, routed to the expansion track. Competitor → displacement
   target, scored.
2. **A dead or dying competitor.** Search for this explicitly, every time, by
   name: shut down, acquired and sunset, end-of-life, no longer sold. Its
   install base *must* migrate and the deadline is not yours to create. Nothing
   else on this list converts like it.
3. **Existing-customer flag** — the vendor's tech tag OR the logo on the
   customers page. Two sources because both are incomplete; a logo page lags
   churn and a tech tag misses private deployments.
4. **Scoops, news, funding rounds, exec hires** — Tier 1 only. Rich, slow, and
   not worth pulling for 400 accounts.
5. **Intent topics** — if the account has them enabled. Many do not. Check
   rather than assume, and record the coverage rate in the method section.

## Connector traps

**Contact search with a title filter usually accepts only ONE company at a
time.** Pass eight company IDs together with a job-title list and you get zero
rows back — not an error, not a warning, an empty result that looks like the
accounts simply have no matching people. Two workarounds, both far better than
fifty single-company calls:

- Filter by **department** (Information Technology, for example) plus
  **management level**. This does accept many company IDs at once.
- Filter by **job function**, which is more precise. Look the function IDs up
  first, then batch about eight company IDs per call with a page size of 100
  and filter titles yourself afterwards.

Run both passes and merge. Department catches the executives; job function
catches the hands-on owners who will actually be at the booth.

**Look up enum values before filtering.** Industries, departments, job
functions, tech products, and metro regions are controlled vocabularies.
Guessing returns either an error or — worse — a silently empty result. Note
whether the field wants the `id` or the `name`; it differs field to field within
the same connector.

**Tech-product lookups usually need the vendor name first**, then the products
belonging to that vendor. One call per vendor. Do this for the vendor's own
product and every competitor named on their site, before scoring.

**Big results overflow the context window.** A batched contact search returns on
the order of 65,000 characters. When the harness saves an oversized result to a
file, do not read it back in — write a small script that parses every saved
result file and keep the raw payloads out of the conversation entirely. The
pipeline is designed as separate steps precisely so this stays possible.

**Know which calls cost credits.** Search, lookup, and scoops are typically
free; enrich and research calls are not. A "no credits" answer rules out every
enrich-style call and every find-and-enrich tool, and it means no emails and no
phone numbers anywhere in the deliverable. Confirm at the end that you spent
none — an explicit "zero credits spent" line in the method section is worth
writing.

## Match rates and what to do with misses

Expect roughly 90% of accounts to resolve against a company-data connector.
Carry the missing 10% through the whole pipeline with blank firmographics rather
than dropping them: an unresolved row is usually a small private company, a
regional division, or a name typed into a registration form by hand — and a
named attendee from an unresolved company is still a named attendee in the room.

Never let a blank become a zero. Blank size, blank industry, and blank tech tags
each need to read as *unknown* in the score and in the file, because the fix for
unknown (ask a human, search the web) is different from the fix for low.

## What to write down about coverage

Signals are worth exactly as much as a reader's confidence in them, and that
confidence comes from stating the gaps. For each signal type, record:

- how many accounts you queried, and how many returned anything
- which competitors you had tech tags for and which you did not
- whether intent was available at all
- what you searched for and did not find — especially the dead-competitor
  search, since a null result there is a real finding

A plan that says "eleven accounts run a competitor that reached end-of-life,
tech-tag coverage was 62%, so treat the absence of a tag as unknown" is
trustworthy. The same plan without those numbers is a spreadsheet of guesses
with good formatting.
