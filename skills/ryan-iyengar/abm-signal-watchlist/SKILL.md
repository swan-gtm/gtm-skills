---
name: abm-signal-watchlist
title: Build an ABM signal watchlist
description: |
  Use this skill for ongoing monitoring across a fixed target-account list; use trigger-based-outbound when evaluating one already-detected event. Produces a resolved account watchlist, signal definitions, stakeholder coverage plan, ranked action queue, and learning loop.
category: ABM
tags: [Sales, Marketing, Demand Gen]
---

Use this when account selection is known but timing is not. Produce a stable company watchlist and an action queue tied to verified changes and appropriate stakeholders.

## Resolve the account list

Start from companies, not purchased people. For every target, retain the submitted name and resolve a canonical domain, operating entity, parent relationship, segment, owner, and ICP evidence. Search existing and archived CRM records before proposing creation.

Route ambiguous domains, subsidiaries, and namesakes for review. Do not watch an unresolved company name: signal matching will blend unrelated entities and contaminate both action and learning.

Classify each account as watch, research, or exclude. “Watch” requires stable identity and fit. “Research” means fit or identity is incomplete. “Exclude” records a durable reason.

## Define meaningful changes

Create a signal specification before collecting events. For each signal family, document the observable event, primary evidence, freshness window, expected business implication, false-positive patterns, and likely buying roles.

Favor changes that alter capacity, priority, risk, leadership, or operating complexity. Generic news volume and social engagement are not inherently buying signals. Read [references/watchlist-rubric.md](references/watchlist-rubric.md) to rank account fit, event strength, and stakeholder access separately.

## Build stakeholder coverage

For each watched account, identify the minimum role coverage needed to act on likely signal families. Verify current employment and account relationship. Preserve known relationships, previous replies, opportunity context, and customer status.

Missing contact coverage is a research task, not permission to create speculative people. Resolve every proposed contact against existing identities and attach it to a canonical account. Name one accountable owner for the account.

## Operate the queue

On each cadence:

1. Collect fresh events and preserve exact evidence and occurrence dates.
2. Resolve each event to one watched account.
3. Suppress duplicate events and changes already acted upon.
4. Re-evaluate fit, active opportunities, recent touches, and exclusions.
5. Rank the account-event-contact combination, not the event alone.
6. Return engage, research, nurture, or skip with a reason and counterargument.

An engage decision needs a verified stakeholder and a specific, evidence-supported implication. Research is correct when the event is strong but contact access is missing. Skip is correct when timing, fit, or context fails.

Use [references/worked-watchlist.md](references/worked-watchlist.md) for subsidiary resolution and multi-stakeholder examples.

## Govern activation

Create a reviewable task containing the account, contact, event, source, recent history, hypothesis, and proposed channel. Require human approval before sending or bulk-creating records. Route active-deal evidence to the opportunity owner rather than starting parallel outreach.

Record outcomes by account, contact, signal family, and hypothesis. Adjust weights only after sufficient volume; retain negative and skipped outcomes to prevent survivorship bias.

## What good looks like

- Every watched company has a canonical identity, fit reason, and owner.
- Signal specifications name both expected implications and false positives.
- The queue ranks account-event-contact combinations.
- Strong events without stakeholder coverage become research, not blind outreach.
- Active relationships and suppressions override campaign enthusiasm.
- Outcome history improves prioritization without erasing human context.

The mediocre version uploads company names, watches every available event, buys contacts after a signal, and sends generic messages before resolving subsidiaries or checking active relationships.

## Rules

- MUST resolve canonical account identity before monitoring or creating contacts.
- MUST preserve exact event evidence, occurrence date, and stakeholder rationale.
- MUST require approval before record creation or outreach.
- NEVER treat activity volume as intent without a plausible implication.
- NEVER launch parallel outreach against an active opportunity or customer conflict.
- NEVER allow missing stakeholder coverage to become a domain-only send.
