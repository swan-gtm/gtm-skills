---
name: personalized-outbound-ab-test
title: Prove personalization beats your baseline
description: "Use this skill when someone claims AI personalization lifts reply rates, or before you let an agent write outbound at scale. Runs a control/personalized/holdout split on your connection list, enforces a safety gate on every generated message, and returns a defensible read on whether personalization actually beat the generic baseline."
category: Outreach
tags: [Sales, SDR]
---

Run this before you let an agent write outbound at scale. It produces a measured answer to "does personalization actually beat our generic message?" and a holdout that receives the winner.

## The play

1. **Split the list into three.** Control (e.g. 100) gets the generic baseline. Personalized (e.g. 100) gets researched messages. Holdout (the rest) waits for the result, then gets the winner. Without a control you are not testing, you are just spending.

2. **Build the do-not-contact list first.** Exclude anyone already in an open thread, in the CRM as an active deal, or recently sequenced. Skipping this is how you send a "nice to meet you" to a customer. Do this before enrichment so you never pay to research someone you cannot contact.

3. **Enrich only the Personalized arm.** Pull current role, headline, employer, and recent activity per lead. The control arm needs nothing, so half your enrichment spend disappears.

4. **Write one message per lead, then gate it.** Every message must pass all six checks or it silently drops to the baseline:
   - **Account-safe** — no links, no phone numbers, no mass-template feel.
   - **Factually grounded** — every personal reference traces to retrieved data. Zero invented facts.
   - **Human** — no AI tells, in the sender's own rhythm.
   - **Respectful** — warm, no creepy over-familiarity.
   - **Rule-compliant** — length cap, CTA placement, banned vocabulary, whatever the sender set.
   - **Recognizably theirs** — the hook is something only that person would recognize as about them.

5. **Re-verify programmatically.** Do not trust the model's self-report. Recompute length, dash counts, CTA position, name casing, and banned phrases after generation. Anything that fails gets fixed or dropped to baseline.

6. **Ship with a fallback.** Set the generic message as the fallback for the personalized variable, so a missing field degrades to proven copy instead of sending `{PERSONAL_MSG}` to a prospect.

7. **Read replies, not opens.** Compare reply rate and positive-reply rate between the two arms. Send the winner to the holdout.

## What good looks like

- A message that "smells like AI" or misattributes a fact costs more than sending nothing. It burns the relationship and the sender's reputation, and neither shows up in your open rate.
- The mediocre version personalizes the first line and leaves the rest a template. Prospects read the seam instantly.
- The gate is the deliverable, not decoration. Expect to drop 10-30% of generated messages to baseline. A gate that never rejects anything is not being enforced.
- You know it worked when you can state the lift as a number, with the control that produced it, and defend the exclude list you used.

## Rules

- MUST run a control arm. A personalized-only send produces no evidence.
- MUST build the exclude list before enriching.
- MUST re-verify constraints programmatically after generation.
- NEVER let a message reference a fact the research did not return.
- NEVER send at full volume before the A/B result is in. That is what the holdout is for.
