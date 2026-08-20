---
name: audience-icp-filter
title: Audience ICP filter
description: |
  Use this skill when a list of people already exists and someone needs to know who on it is worth
  contacting — event or webinar attendees, registrants, a prospecting export, a CRM segment, a
  newsletter or community list. Produces every lead sorted into ICP match, needs review, or no
  match, with a reason attached to each, the team's own colleagues and competitors stripped out,
  and nobody silently dropped. Trigger phrasings: "filter this list against my ICP", "who here
  matches our ICP", "clean up this lead list", "qualify my signups", "segment this audience",
  "who should we follow up with after the webinar", "did we import junk", "remove the bad leads".
category: Prospecting
tags: [Sales, RevOps]
---

Applies to a list that already exists and needs sorting before anyone contacts it. Produces four labelled buckets, a reason per lead, and reconciled counts.

## Every imported list is mostly noise

Colleagues are in it. Competitors are watching. A third of the job titles are unreadable, half the companies are stale, and somewhere in there are the twelve people actually worth a message. The default response — skim it, sort by gut, start sequencing — leaks in the direction that hurts most: someone's own coworker gets a cold pitch.

This skill starts from an existing list. Importing or scraping is a different job with different prerequisites; folding it in makes both slower.

## Check the data before asking about the ICP

The instinct is to ask what the ICP is first. Do the opposite: measure what the list actually contains, then ask only about criteria the data can support.

There is no point offering geography filtering on a list where the location field is empty. It doesn't filter anything — it routes everyone into review and calls that a result. The same applies to industry, and to exclusion when there's no company and no email to match on.

Run the coverage check, read which criteria are blocked, and say so before the conversation about the ICP starts. If enrichment is needed, quote what it will cost and get an explicit yes before spending anything. If the team declines, proceed — but name the criteria you dropped and say that exclusion is now best-effort. Filtering on a criterion the data can't support and presenting the result as clean is the worst available outcome, because it looks like work. The field-by-field thresholds and the ICP question set are in `references/coverage-and-icp.md`.

## Two passes, and neither is optional

**Pass 1 is deterministic.** `scripts/build.py` pattern-matches seniority and function across the title and, when the title is silent, the bio; applies exclusions uniformly across every identity field; and refuses to emit a result whose bucket counts don't reconcile against the input. Nobody gets lost, and the same list classifies the same way twice. Never hand-sort a list — it's unauditable and it's exactly how colleagues leak through.

**Pass 2 is semantic, and it is the agent's job.** Patterns can't read meaning. `Chief Happiness Officer` and `Chief Medical Officer` both resolve as C-level and neither is a buyer. A competitor nobody thought to list sits quietly in the match bucket. `Founder @ Stealth Mode` lands in review when it's obviously in ICP.

The point of the skill is that nobody hand-sorts a list. Handing back a fifty-lead review bucket is not a result — it's the original problem with extra steps. Work the queue down; leave only the genuinely ambiguous handful for a human.

## Review the queue, not the list

The expensive mistake is re-reading everything in pass 2. On a 250-lead list, lead-by-lead review took eight minutes and changed almost nothing, because most classifications were never in doubt.

Pass 1 returns a bounded queue instead: the ambiguous, the matches inferred from a bio rather than a title, the matches whose company reads like an agency or a freelancer, the leads dropped on a soft geography or industry miss, and the leads dropped on a seniority or function read out of free text rather than off the title. Each carries a flag saying why it's there. On a clean list that's fifteen to twenty-five leads, and it's the whole of pass 2's work. Anything outside the queue was confident enough to trust.

A large review bucket is a signal, not a workload. It usually means the list was never enriched, or the ICP is under-specified — most often that nobody answered whether founders qualify regardless of stated function. Diagnose the cause and say it rather than moving forty leads by hand. `references/pass-two-review.md` covers the flags and the false-positive patterns.

## Exclusion leaks in three specific ways

Matching on company name alone fails, every time, on real data:

**Empty company and empty email.** The only clue is the bio — "Client Partner @ Acme". Filtering on the company field lets them straight through.

**Job-changers.** The company field says one employer and the email domain says another. Either field alone gives the wrong answer; a hit on *either* has to exclude.

**Collapsed spellings.** `@AcmeLabs` and `acme-labs` contain none of the string "Acme Labs". A punctuation-stripped comparison catches them — but only above about five characters, or short tokens start firing inside unrelated words.

Always seed the exclusion list with the team's own company and domain. It's the most common leak and by far the most embarrassing. And when extending exclusions in pass 2, remember that a competitor's name inside someone's *bio* is usually a tool they use, not their employer — check it's the employer or the domain before dropping them. Full doctrine in `references/exclusion-doctrine.md`.

## What good looks like

The tell of a good operator: they look at the field fill rates before they look at the list. They know that "filter by geography" on a list with 12% location coverage is not a filter, and they'd rather deliver three honest criteria than six decorative ones.

The mediocre version sorts by job title alone, produces a tidy match list, and quietly includes two colleagues and a competitor — because the colleague's company field was blank and the competitor was spelled with a hyphen. It looks cleaner than the good version. That's the trap: on this task, output that looks tidy is usually output that dropped the hard cases.

Good output reconciles. Every lead is in exactly one bucket, every bucket decision carries a reason, and the totals add back to the input count. If somebody asks "what happened to the other 40?", the answer is in the file, not in a shrug. And the review bucket that comes back to the user is small enough to decide in two minutes.

## Rules

- MUST measure field coverage before asking what the ICP is, and drop criteria the data can't support.
- MUST get explicit approval, with a quoted cost, before spending anything on enrichment.
- MUST run both passes — deterministic classification, then semantic review of the queue.
- MUST match exclusions across company, both email fields, bio and company URL, with a punctuation-stripped comparison for longer terms.
- MUST seed exclusions with the team's own company and domain.
- MUST reconcile: every lead in exactly one bucket, with a reason, totalling the input.
- MUST queue any lead that left the ICP on a signal inferred from free text — a wrong drop is invisible by construction, so no lead may be discarded on an inference without a second look.
- NEVER classify a list by hand.
- NEVER exclude someone on a competitor name found only in their bio without confirming it's their employer.
- NEVER drop ambiguous leads to keep the output tidy — route them to review.
- NEVER hand back the full review bucket as the deliverable.
