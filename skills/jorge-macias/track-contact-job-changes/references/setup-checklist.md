---
title: Setup checklist
description: Reference for the Track contact job changes skill.
---

# Setup checklist

Run once, then save the answers so later runs load them instead of re-asking. Detect what the operator
already has connected and pre-fill from it; only ask for what you can't infer. Confirm a summary before saving.

Capture:

## CRM & write policy
- Which CRM holds the contacts.
- Whether the skill may **write** to it. If not, the play runs in report-only mode — it proposes changes and exports them, but never writes.

## Match keys
- **Person** — how to locate and dedupe a contact, in priority order: record id → email → LinkedIn URL.
- **Company** — how to decide two companies are the same, in priority order: domain/website → LinkedIn company page → name. These drive both "still there?" and "is the new company already in the CRM?".

## Data sources (four capabilities)
Name the tool the operator will use for each. If a capability has nothing available, suggest current market options and have them pick or connect one — do not proceed without a work-history source, which is required.
1. **LinkedIn-URL finder** — resolves a profile URL from name + company, with name validation.
2. **Work-history source** — returns current employer + title + start date AND past employers. Required.
3. **Email lookup** — a verified email for the moved contact (for opt-out / update / verification).
4. **Company enrichment** — size, industry, revenue, domain, LinkedIn, geo for a net-new company (feeds tiering).

## Tier rules
- The criteria that make a net-new company worth creating as an account (a **fit** account → Tier 1). See [tiering.md](tiering.md). Anything not a fit → skip & flag.

## Opt-out rules
- The conditions that make a move a dead end when the **new company is already in the CRM** — e.g. it's a current customer, a competitor, or a partner. When one matches → flag & opt out. Otherwise → update the contact.

## Field mapping
- The CRM property names to write: current company, title, LinkedIn URL, job-change flag, job-change date, previous company, opt-out flag, account tier, review/needs-attention flag. Only map the fields the operator wants written.

## Confidence thresholds
- The bar that separates "still there" / "confirmed left" from "can't confirm". A high bar keeps the database clean; borderline comparisons should fall to "can't confirm" rather than a guessed write.

Re-running setup overwrites the saved config after showing current values as defaults. The operator can also edit it by hand.
