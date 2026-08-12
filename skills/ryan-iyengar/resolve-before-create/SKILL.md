---
name: resolve-before-create
title: Resolve before creating CRM records
description: |
  Use this skill before importing, enriching, or manually creating contacts and accounts in a CRM. Produces a create, link, review, or reject decision that prevents duplicates while preserving uncertain matches for human resolution.
category: RevOps
tags: [RevOps]
---

Use this before any workflow creates CRM records. Produce an evidence-backed identity decision for every proposed contact or account.

## Normalize without destroying evidence

Retain the raw input, then derive normalized comparison values. Lowercase domains and emails, remove URL protocols and paths, standardize whitespace, and separate legal suffixes from company names. Do not strip meaningful subdomains, country distinctions, or name tokens merely to force a match.

Identify the strongest available keys. For people, prioritize verified email, provider identity, account relationship, full name, and role. For accounts, prioritize canonical domain, verified external identity, legal entity, address, and normalized name. A company name alone is weak evidence; a shared consumer-email domain is not account identity.

## Search broadly, decide narrowly

Search active and archived records, alternate emails, former domains, aliases, parent-child relationships, and identifiers merged within the organization’s retention window. Search each strong key independently so a formatting error in one field does not hide an existing record.

Build candidate pairs and compare corroborating and conflicting evidence. Return one of four decisions:

- **Link:** one candidate is unambiguous and the new data belongs on it.
- **Create:** no credible candidate exists after all strong keys are searched.
- **Review:** multiple candidates remain or important evidence conflicts.
- **Reject:** the input lacks minimum identity evidence or violates an exclusion rule.

Use [references/match-rubric.md](references/match-rubric.md) for numeric scoring. The score supports the decision; it does not override a hard conflict.

## Plan the action

For a link decision, specify which existing record receives each new value and whether the update fills a blank or replaces data. Do not overwrite a verified value with an unverified enrichment.

For a create decision, include the keys searched, search time, candidate count, proposed owner, source, consent or lawful-use context, and required relationships. Accounts should carry a stable domain where available. Contacts should not be created as ownerless, accountless records when those relationships are known.

For review decisions, show the smallest evidence set a human needs: candidate identifiers, matching fields, conflicts, recent activity, ownership, and downstream relationships. Do not ask the reviewer to rediscover the match.

Before applying the action, repeat the search. Another workflow may have created the record after planning. If a new candidate appears, invalidate the create decision and resolve again.

Read [references/worked-resolution.md](references/worked-resolution.md) for common domain, email, and subsidiary cases.

## Monitor the gate

Track proposed creates, prevented duplicates, ambiguous reviews, false links, false creates, and resolution time. Sample both approved creates and links. A gate that prevents duplicates by routing everything to review is not working; neither is one that boasts high automation while creating costly false links.

Investigate sudden increases by source. A spike often indicates a changed export format, upstream identifier loss, a new acquisition, or an integration searching a narrower population than it writes.

## What good looks like

- Every create decision lists the keys and populations searched.
- Exact identifiers drive high-confidence matches, while names provide corroboration rather than proof.
- Conflicts such as different legal entities or verified emails force review.
- The action is re-resolved immediately before creation.
- New records arrive with ownership, provenance, and known relationships.
- Reviewers see actionable evidence rather than a vague “possible duplicate” warning.

The mediocre version checks only exact email or company name, ignores archived records, creates first and deduplicates later, or links records because a fuzzy score crossed a threshold despite contradictory evidence.

## Rules

- MUST retain raw source values and record the search evidence.
- MUST re-run resolution immediately before creation.
- MUST require human review for conflicting strong identifiers or irreversible merges.
- NEVER match accounts on normalized name alone.
- NEVER replace verified data with weaker enrichment without approval.
- NEVER create records to evade an ambiguous match.
