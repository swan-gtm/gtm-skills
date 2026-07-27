---
title: "Red-flag and green-flag catalog"
description: "Reference for the LinkedIn ads & ABM audit skill."
---

# Red-flag and green-flag catalog

Roll the audit's findings into two short, prioritized lists. Every item must **name the culprit (or winner)** —
the specific campaign, ad set, ad or account — the **metric** that triggered it, and the **fix**. Vague flags
("CTR could be better") are useless; specific ones ("Ad set 'Enterprise-Image' CTR 0.18% vs 0.42% benchmark after
14k impressions — pause the two weakest images, shift spend to the TLA set") are the product.

## Red flags — look for these

- **Decaying ads** — CTR down three weeks in a row, or below the format pause threshold after 1,000+ impressions.
  Fix: pause / refresh the creative; move budget to winners.
- **Efficiency drop** — more spend, less engagement/fewer clicks period-over-period. Fix: name the ad set that
  grew spend without output; rein it in.
- **Spend spike** — a campaign/ad set whose spend jumped with no matching lift in clicks/pipeline. Fix: cap or
  investigate; check for audience overlap or a runaway auto-bid.
- **Too many ads for the budget** — actual serving ads far above `affordableAds`, per-ad spend below $25/day. Fix:
  consolidate to the affordable count so LinkedIn can optimize.
- **Impression hogs** — one or few accounts eating a lopsided share of impressions (starving the rest of the
  list). Fix: consider frequency-capping or excluding them so budget reaches under-served target accounts. Only
  flag when the share is genuinely disproportionate.
- **Deals without engagement** — influenced/open deals on accounts your ads never touched (from `list_deals` +
  `list_companies`). Fix: add those accounts to the target list; your ABM isn't covering real pipeline.
- **Format mis-allocation** — heavy spend in a weak-effective-CPC-to-LP format (e.g. video/lead-gen) while TLAs
  are underfunded. Fix: the reallocation from the metrics reference.
- **Below-benchmark core metric** — account CPC/CPM well above, or CTR/effective-CTR-to-LP well below, benchmark.
  Fix: point to the format(s) dragging the average.

## Green flags — celebrate and double down

- **Top-performing ads and campaigns** in the window (by clicks, effective CTR to LP, or influenced pipeline).
  Action: scale spend, clone the angle into new creatives.
- **Formats punching above their spend share** — e.g. TLAs at 15% of spend but 60% of LP clicks / deal influence.
  Action: shift more budget here (ties to the reallocation).
- **Accounts heating up** — companies surging in engagement or newly moved to Interested. Action: hand to
  BDRs/AEs now, while intent is warm.
- **Improving efficiency** — clicks/engagement up while spend flat or down; CPC/CPM trending down. Action: keep
  the current creative/bid strategy; it's working.

Keep each list to the few that actually matter for this account — 3-6 items each is plenty. A clean account with
few flags is a fine result; don't manufacture problems to fill the list.
