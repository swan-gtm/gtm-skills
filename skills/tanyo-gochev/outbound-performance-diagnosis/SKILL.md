---
name: outbound-performance-diagnosis
title: Outbound performance diagnosis
description: |
  Use this skill when an outbound campaign is underperforming and the cause isn't obvious — replies
  dropped, meetings dried up, a sequence that worked stopped working, or the numbers look fine but
  nothing closes. Works through the funnel in fixed order so the real leak gets fixed instead of the
  most visible one. Produces the diagnosis, the evidence for it, and the single next fix. Trigger
  phrasings: "why did our reply rate drop", "campaign isn't working", "diagnose this campaign",
  "opens are fine but no replies", "replies but no meetings", "should we change the copy",
  "our sequence stopped working".
category: RevOps
---

Applies to a live campaign with data. Produces the leak, the evidence, and one fix — not a list of everything that could be improved.

## Work the layers in order and stop at the first break

The order is not optional. Each layer's numbers are meaningless until the layer above it is healthy, and the classic failure is optimising subject lines for an audience that never received the email.

**Layer 1 — delivery.** Bounce rate, spam complaints, inbox placement. **If this layer is broken, stop. Change nothing else.** You cannot learn anything about copy, offer, or targeting from messages that never arrived, and every test you run in that state teaches you something false.

**Layer 2 — engagement.** Opens, and how they decay across steps. Treat opens as diagnostic, not as a result: tracking pixels cost you placement, and open data is unreliable enough on some clients that low opens with healthy replies usually means the pixel, not the copy. A drop of more than about a fifth per step is sequence fatigue or degrading deliverability, not a subject-line problem.

**Layer 3 — replies.** Total reply rate and reply rate by step. Read it against opens:

- Opens healthy, replies near zero → **copy or offer.** They're reading and not moved.
- Opens weak and replies weak → **fix delivery and subject first.** Reply data isn't readable yet.
- Replies healthy, mostly negative → **segment.** The message may be fine for someone else.

**Layer 4 — quality.** Positive replies, negative replies, referrals, and "not now". This is the layer that matters, and the one most reports omit. A campaign with a 12% reply rate that is almost entirely "remove me" is worse than a 4% campaign that is mostly positive — it's burning the domain and the list at once.

## Replies but no meetings

The most expensive leak, and it's rarely a campaign problem. Either the reply handling is too slow, the ask is too soft, or the offer demanded a meeting before delivering anything of value. Check response time before rewriting anything — interest decays in hours.

## Change one thing

Hold everything constant except the variable under test, and give it enough volume to be readable. Two changes at once produces a result you cannot attribute, and the wrong lesson gets carried into the next campaign as received wisdom. Below a few hundred sends per variant, variance swamps the effect you're looking for — don't call it.

## What good looks like

The tell of a good operator: they check delivery before forming any opinion, and they can say which layer the campaign is failing at before they say what to do about it.

The mediocre version rewrites the copy. It's the most visible lever, it feels productive, and it's the wrong answer most of the time — the leak is usually one layer up, in delivery or targeting or the offer itself.

Good output names one layer, cites the numbers that locate it there, prescribes exactly one change, and states what result would prove the diagnosis right. A diagnosis that recommends five improvements hasn't diagnosed anything.

## Rules

- MUST verify delivery health before analysing anything downstream.
- MUST quote sample sizes with every rate.
- MUST separate positive from total replies before judging a campaign.
- MUST prescribe one change at a time.
- NEVER conclude that copy is the problem while a delivery metric is out of range.
