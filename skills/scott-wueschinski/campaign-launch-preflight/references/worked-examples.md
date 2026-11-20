# Worked examples

Five launches from one multi-campaign rollout for a managed cloud services provider, anonymized. In each case the dashboard that caused the problem reported success.

## 1. The 2% qualification rate that was not a list problem

Four signal-sourced campaigns imported 3,985 leads. Scoring qualified 145 of them, under 4%. The security and compliance campaign qualified 13 of 716, under 2%.

The instinct was to blame the source list. The cause was gate 1: all four campaigns had a blank campaign context, so every lead was scored against the account-level ICP, which described buyers of a managed operations service. Security buyers scored zero against an operations profile. The account context also listed target industries as a gate, so most leads scored zero on industry alone.

The fix was to write a context per campaign, change industry to a weighting, rank a verified platform footprint above it, and re-score. The re-score took the account to about three quarters of its monthly scoring allowance, most of which one correctly configured run would have saved. It also rewrote scores without re-qualifying anyone, so a second approval pass was needed.

**The lesson:** a low qualification rate on a hand-chosen list is a context problem until proven otherwise.

## 2. "Ready to launch" with zero approved leads

The same four campaigns showed "ready" in the campaign system and one showed "240 contactable". The approved count was zero in all four. The 240 was 228 leads still in the imported state, 5 enriched and 7 that had failed enrichment; none was approved. A push that afternoon would have sent nothing and reported success.

**The lesson:** quote the approved count from the system that pushes, never a readiness label.

## 3. Leads with no email in an email-first sequence

After the re-score, 139 qualified leads came from social engagement signals. They held profile links and zero email addresses. Enrichment found an email for 107; 78 verified; 29 unverified addresses were left out. The sendable pool was 78, not 139. Separately, 66 of 70 leads in a needs-review queue were personal mailboxes and were refused.

**The lesson:** report the funnel with every denominator: imported, enriched, verified, qualified, approved.

## 4. The step 2 problem

A first-step read of one campaign passed. A read of every step found 16 of 25 steps signed by a rep who had moved off the account, and two sibling campaigns whose 20 steps were empty shells with null subjects, null bodies and null delays. A second campaign held 25 steps in the campaign system and 17 on the sending platform; pushing would have overwritten the platform's sequence and the new sender with the stale one.

**The lesson:** read every rendered step, and reconcile the two copies of a sequence before any push.

## 5. Fifteen mailboxes, one badge

Every mailbox in the rollout showed a "bad DNS" badge on launch day, and all fifteen sat at a lower daily cap than standard with warm-up paused. Opening one technical panel showed SPF, DKIM, DMARC, MX and blacklists passing; the only failing line was a missing custom tracking domain, which matters only when tracking is on. Tracking was turned off, caps were raised to the standard and read back (two mailboxes had dropped the click and needed a second pass), and warm-up was restarted.

What the team did not do was read the other fourteen panels. The gate stayed "not checked" for those mailboxes until each was read, because the same badge can hide a second failing line.

**The lesson:** a badge is a symptom. Name the failing line, per mailbox, and report "not checked" honestly.
