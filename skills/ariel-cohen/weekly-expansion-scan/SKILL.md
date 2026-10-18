---
name: weekly-expansion-scan
title: Weekly expansion scan
description: |
  Use this skill to run a weekly pass over every paying customer and decide which ones the team should talk to about upgrading this week. It scores each closed-won account on account tier, ACV potential, the gap between what they pay and what an account their size should pay, headcount against price, and how fast they are burning through their plan, sorts them into Critical, High and Medium urgency, and posts a ranked digest with a named contact, the signal and a concrete suggested reach-out for each. Works across the whole book in one run, rather than scoring one account at a time. Also answers "who should we upsell this week", "expansion digest", "which customers are outgrowing their plan".
category: Deals
tags: [Sales, RevOps]
---

Applies when the question is "of everyone already paying us, who is ready to grow, and who do we call first?" Produces a ranked weekly digest, one entry per account, each with a named contact and a specific suggested move.

Expansion revenue is usually lost to neglect, not to competitors. The customers most ready to upgrade are often the quiet ones: a mid-size company on your cheapest plan, or a team that has burned 90% of its allowance three weeks before renewal. A weekly scan with fixed scoring rules catches them before the customer has to ask, or leaves.

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full list and the decisions behind each.

- `{{BILLING_SOURCE}}`: Where active subscriptions live (e.g. Stripe, Chargebee, your product database)
- `{{CRM}}`: Your CRM (e.g. HubSpot, Salesforce, Attio)
- `{{CLOSED_WON_STAGE}}`: The CRM stage or lifecycle value that marks a paying customer
- `{{TIER_TAGS}}`: Your account tiers, top two used here (default: Diamond and Gold; lower tiers are excluded)
- `{{ACV_TAGS}}`: Your ACV potential tags (default: high, medium, low)
- `{{USAGE_UNIT}}`: What customers consume on a plan (e.g. credits, seats, API calls, records)
- `{{PLAN_LADDER}}`: Your plans with price and included `{{USAGE_UNIT}}`, lowest to highest
- `{{SCALE_PRICE}}`: Monthly price of the plan you expect a mature customer to sit on (default thresholds below assume about $1,200 a month)
- `{{EXPANSION_TARGETS_FILE}}`: Optional: a maintained list of target accounts with their expansion angle and status
- `{{DIGEST_CHANNEL}}`: Where the digest posts (e.g. a #expansion-leads Slack channel)
- `{{ERROR_CHANNEL}}`: Where run failures post
- `{{EXPANSION_OWNER}}`: The person who works expansion conversations

## Step 1: Build the working universe

1. Pull every active subscription with a price above zero from `{{BILLING_SOURCE}}`: account domain, plan, monthly price, included `{{USAGE_UNIT}}`, remaining `{{USAGE_UNIT}}` this cycle, billing interval. Page through until you have all of them.
2. Pull every account at `{{CLOSED_WON_STAGE}}` from `{{CRM}}`.
3. The working universe is the intersection: in the closed-won stage AND paying. Drop any domain that appears in only one source, and log the mismatches; they are usually billing or CRM hygiene problems worth a separate look.

## Step 2: Score each account (default maximum 8.5)

Collect for each account: monthly price, tier tag, ACV tag, employee count, and burn (share of this cycle's `{{USAGE_UNIT}}` already used). Compute the score in code, not by eye.

**Tier (a gate, not just points).** Only the top two tiers in `{{TIER_TAGS}}` are scanned.
- Top tier (default Diamond): 2.0
- Second tier (default Gold): 1.0
- Anything lower or untiered: excluded from the scan entirely

**ACV potential** (from `{{ACV_TAGS}}`)
- High: 1.5
- Medium: 0.75
- Low or untagged: 0

**Price gap** (what they pay against `{{SCALE_PRICE}}`). Defaults assume a scale plan around $1,200 a month; rescale the bands to your own ladder.
- $250 a month or less: 2.0
- $251 to $500: 1.5
- $501 to $750: 1.0
- $751 to $1,200: 0.5
- Above $1,200: 0 (already at scale; less urgency)

**Headcount against price** (an ACV mismatch)
- 200+ employees paying $750 a month or less: 1.0
- 75 to 199 employees paying $750 a month or less: 0.5
- Under 75 employees: 0

**Burn** = (included − remaining) / included × 100. If the included amount is not on the subscription, take it from the plan in `{{PLAN_LADDER}}`.
- 90% or more: 2.0 (critical; they are probably already topping up)
- 70% to 89%: 1.5
- 50% to 69%: 0.75
- Under 50%: 0

If burn cannot be determined, use the most recent usage note on the account. If there is none, the default is to score burn as 0 and say so in the entry. Never guess it.

Sort descending and keep the top 25.

## Step 3: Add the expansion context

For each of the top 25, check `{{EXPANSION_TARGETS_FILE}}` if you keep one:
- Use the recorded expansion angle and category if the account is listed.
- **Skip accounts already in motion.** Default: status "live upgrade conversation" or "meeting booked". A second rep opening the same conversation is worse than missing a week.

If the account is not listed, derive the angle from the signals: burn, headcount against price, ACV tag.

## Step 4: Classify urgency

**Critical: act this week**, if any of:
- Burn 90% or more
- A buyer-initiated signal on the account (they flagged running out, asked about upgrading)
- Top tier paying $500 a month or less

**High: act within two weeks**, if any of:
- Burn 70% to 89%
- 200+ employees paying $600 a month or less
- Score 6.0 or more

**Medium: on the radar.** Everything else in the top 25.

## Step 5: Post the digest

Post to `{{DIGEST_CHANNEL}}`, one message per account so each can be claimed and threaded.

**Header message first:**

```
Weekly expansion scan, week of <Monday date>
<N> paying customers scanned

| Urgency  | Rule (from Step 4)                                              | Count |
| Critical | Burn ≥ 90%, buyer asked, or top tier paying ≤ $500/mo           | <x>   |
| High     | Burn 70 to 89%, 200+ employees paying ≤ $600/mo, or score ≥ 6.0 | <x>   |
| Medium   | The rest of the top 25                                          | <x>   |

Top 5 by urgency, then top 5 by ARR upside, below.
```

**Then two short lists:**
1. **Top 5 by urgency**: the highest composite scores.
2. **Top 5 by ARR upside**: (recommended plan price − current price) × 12, highest first, ties broken by employee count. Skip anyone already in the first list.

Then the remaining Critical and High accounts, then Medium accounts up to a total of 20. Critical and High are always posted, even if together they pass 20; in that case no Medium accounts are posted. Otherwise cut the lowest-scoring Medium accounts first.

**Each account message:**

Title line: `<urgency> <tier> <Company> (<domain>) | $<current>/mo → <recommended plan>`

Up to five bullets:
- **Who:** a named contact (champion, economic buyer or expansion owner) with their LinkedIn URL. If there is none on file, write "Contact not on file; enrichment recommended." Never invent one.
- **Signal:** the specific reason: burn, repeated top-ups, headcount against price, something the buyer said, seats filling up, a use-case ceiling.
- **Context:** current plan, relationship history, any open or past upgrade conversation.
- **Reach out:** one concrete suggestion naming who contacts them, on which channel, with what angle and what ask. Good: "`{{EXPANSION_OWNER}}` emails the ops lead about hitting 100% of their allowance, which she raised on the last call; ask is the next plan up." Bad: "Follow up with the team."
- **Score:** tier and the score out of 8.5.

In a thread reply: the score breakdown, other contacts at the account, and the CRM record link.

The digest suggests outreach; it never sends any. A person decides and acts.

## Step 6: When things go wrong

- **Fewer than 5 accounts qualify:** post the digest anyway, with a note: "Low qualifying count. ACV tags may need refreshing on recently won accounts."
- **The billing or CRM pull fails:** post the error to `{{ERROR_CHANNEL}}` and stop. A digest built on half the book is misleading.

## What good looks like

- Every account in the digest is paying, closed-won and in a top tier, and none is already in an open upgrade conversation.
- Every score can be rebuilt from its breakdown in the thread.
- Every entry names a real person and a specific move. The suggested reach-out could be sent after a two-minute edit.
- Critical accounts are the ones a person would agree are urgent on sight: running out of allowance, asking for more, or clearly underpaying for their size.
- The same account does not appear in both top-5 lists.
- When data is missing (no burn, no contact), the entry says so instead of filling the gap.
