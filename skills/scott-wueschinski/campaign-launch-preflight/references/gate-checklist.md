# Gate checklist

Each line is a check you can mark go, hold, or not checked. Record the evidence beside every go: the count, its denominator, and the system it came from.

## Gate 1: scoring context

Write the campaign context before the first lead is scored. A usable context answers five questions in plain sentences:

| Field | What it says | Example |
|---|---|---|
| Buyer | The role and seniority this campaign sells to | "Security and compliance leaders, director and above" |
| Problem | The problem the offer solves, in the buyer's words | "Audit findings on cloud workloads they cannot staff to remediate" |
| Weighted signals | What raises a score, ranked | "1. Verified footprint on the platform we support. 2. Open security roles. 3. Recent audit or breach disclosure" |
| Industry | Industries that raise the score, written as a weighting | "Healthcare and financial services weight higher; others are not excluded" |
| Disqualifiers | What drops a lead to zero regardless of other signals | "Current customer; competitor; under 50 employees" |

Checks:

- [ ] Every campaign in the launch has its own context, read back after writing it, not only the account-level ICP.
- [ ] Industry appears as a weighting, never as a gate. A gated industry list zeroes every lead outside it, including the best-fit ones.
- [ ] A verified technology or platform footprint outranks industry. A company that runs the platform you support is a better lead in an unlisted industry than a listed company that does not.
- [ ] Contexts are settled before the first scoring run, and the scoring budget for the period covers one run of the full list.
- [ ] If a re-score is planned, a separate approval pass is planned after it. In most systems, a re-score rewrites scores and leaves qualification status as it was.

## Gate 2: sendable pool

- [ ] Count leads with a verified work email, a first name and a company. Report that number, not the imported number.
- [ ] Personal mailboxes are excluded. Unverified and catch-all addresses are excluded or held in a separate, lower-volume test.
- [ ] For an email-first sequence, the leads hold email. A list sourced from social engagement often arrives with profile links and no email; enrich and verify before quoting a pool.
- [ ] Report the funnel: imported, enriched, verified, qualified. Each stage shows its denominator.

## Gate 3: approval count

- [ ] Count approved leads per campaign from the system that performs the push.
- [ ] The campaign is in the state the push requires (commonly "ready", not "draft").
- [ ] The number you quote for the push equals the approved count. "Contactable" includes leads that failed enrichment and leads awaiting review.
- [ ] Leads moved from an older campaign are paused or suppressed in the old one, so no one receives two sequences at once.
- [ ] To stop a lead that has already entered a campaign, use suppression rather than disqualification; systems often refuse disqualification after entry, and suppression can be undone.

## Gate 5: rendered copy

- [ ] Read every step, rendered, for up to three leads per campaign (all of them if it holds fewer).
- [ ] Every merge field resolves. No literal braces, brackets or blank greetings.
- [ ] The sender name is right on every step, and no other sender's name appears anywhere, signatures included.
- [ ] Every step holds real content: subject, body and delay. Template shells with null bodies pass a step count check.
- [ ] An opt-out line is on every email step.
- [ ] Voice or video steps use only the named sender's own recording or voice. If none exists, turn the step off.
- [ ] Where the sequence lives in two systems, step count and sender agree before the push.

## Gate 6: post-launch verification

- [ ] Leads on the sending platform equal approved leads pushed, exactly.
- [ ] Launch state was read on the sending platform. A start click that did not register still reads as "draft" there.
- [ ] Campaign ids, counts and the source read are logged in the launch record.
- [ ] A resumed campaign resumes at the intended step and delay. A pause stretches every gap that crosses it.
