---
name: sales-hire-offer-close
title: Sales hire offer close
description: |
  Use this skill when a hiring manager is about to make an offer to a sales, marketing, customer success or other GTM hire and wants it accepted, resigned on and started without a fall-off. Pulls the candidate's stated motive and numbers, runs a close-ready gate, sizes the gap on total package, prices up to three offer structures on cost, signal and risk, writes word-for-word trial closes, rates counter-offer risk with a defence plan and resignation rehearsal, and schedules a dated notice-period plan from resignation day to start day. Ends with one Yes/No decision for a human. Handles one offer or several in flight. Triggers on "we're ready to offer", "what should we offer", "will this number land", "structure the offer", "they want more money", "counter-offer", "they're resigning today", "worried they'll get bought back", "notice period", "they accepted, now what", "offer stage".
category: Hiring
tags: [Sales, Leadership]
---

# Sales hire offer close

Runs from the moment a hiring manager decides to offer until the new hire's first day. Produces a close plan and a Yes/No decision on the number, never an offer sent by the agent.

**The prime rule: never make an offer you have not trial-closed.** A formal offer is the last step of a close, not the first. If the candidate's answer to "if this lands, are you accepting?" is not yet known, the offer is not ready, however strong the final round felt.

Offers die two ways. An information gap: a number goes out before anyone confirmed what the candidate would accept. An unmanaged risk: the candidate accepts, resigns, gets bought back, and nobody rehearsed that conversation. The play closes both.

## Template placeholders

Replace every `{{...}}` before enabling. The setup checklist in `references/setup-customization-checklist.md` covers each one.

- `{{ATS}}`: where the candidate, their stage history and interview notes live
- `{{COMP_APPROVER}}`: who signs the ceiling for this role
- `{{REVIEW_CHANNEL}}`: where the close card is posted
- `{{CALENDAR}}`: where notice-period touches are scheduled
- `{{OFFER_OWNER}}`: who holds the candidate relationship through notice (hiring manager, recruiter or talent partner)
- `{{CURRENCY}}`: currency for every figure on the card
- `{{PACKAGE_BASIS}}`: how total package is counted, for example base plus on-target commission plus super or pension plus equity at a stated value

## Trial mode (recommended for the first three offers)

Build the full card but write nothing to `{{ATS}}` or `{{CALENDAR}}`. Post it to `{{REVIEW_CHANNEL}}` marked TRIAL and let the hiring manager run the close their usual way alongside it. Compare after day one: which risks the card called, and which it missed. Switch writes on once the card is calling them.

## Diagnostic questions (before the first run)

Ask these once per team. They show where offers are leaking.

1. Of the last ten offers, how many were declined, how many accepted then reneged, and how many started and left inside six months?
2. Who can approve a number above the band, and how long does that take?
3. Does anyone ask the candidate what they will accept before the offer is written?
4. Who talks to the candidate between resignation and day one, and how often?
5. When a candidate was bought back, did anyone see it coming? What was the signal?

## The play

### Step 1. Pull the inputs

- From `{{ATS}}`: the role, stage history, interview and debrief notes, any stated reasons for moving, and any numbers the candidate has given.
- From `{{COMP_APPROVER}}`: the approved ceiling on `{{PACKAGE_BASIS}}`, in `{{CURRENCY}}`, and what flexes (sign-on, equity, start date, title) without a new approval.
- If the panel debrief flagged concerns or counter-offer signals, carry them in. They are the first inputs to Step 6.

Search before asking. Anything the notes already hold is used, with its date. Anything older than the last interview is reconfirmed with the candidate, not trusted.

### Step 2. Run the close-ready gate

Three checks, all required:

- **Motive.** The candidate's real reason for moving, in their own words. "New challenge" does not count.
- **Numbers.** Current base, current total, expectation, walk-away and notice period, all confirmed by the candidate, not inferred from a salary band.
- **Ceiling.** The actual number, signed by `{{COMP_APPROVER}}`. Not the advertised range.

If any check fails, stop. Post a short card naming the missing check and the exact conversation that fills it, with the script from `references/scripts.md`. A defence built on a motive nobody established fails at the moment it is needed.

### Step 3. Size the gap

Expectation against ceiling on total package, as a figure and a percentage. Keep the walk-away separate: the expectation is the opening position, the walk-away is the deal. Convert every figure to `{{PACKAGE_BASIS}}` first. Comparing one company's base with another's on-target earnings is the most common way two sides think they are further apart than they are.

### Step 4. Build up to three structures

Price each on cost to the company, what it signals to the candidate, and its risk. `references/offer-structures.md` holds the structure library, the gap thresholds and the sales-specific checks. Recommend one and say why in a sentence.

### Step 5. Trial close both sides

Before anything is written, ask the candidate the direct question and give the approver the honest read on whether their preferred number lands. Scripts are in `references/scripts.md`. Record both answers word for word. A trial close that gets "I'd have to think about it" is an answer: something is missing, and Step 2 runs again.

### Step 6. Rate the counter-offer risk

LOW, MEDIUM or HIGH against the evidence bar in `references/counter-offer-risk.md`. Every rating cites the signal that set it. That reference also holds the sourced retention figures to use in the candidate conversation, each with its year and population.

### Step 7. Rehearse the resignation

Predict what the current employer will say, who will say it and with what number, and rehearse the candidate's reply. HIGH risk means the rehearsal is booked before the offer goes out.

### Step 8. Write the notice-period plan

Dated touches from resignation day to day one, each with an owner and a purpose. Minimum set: resignation day, end of week one, a mid-notice touch with the future manager or team, two weeks out on logistics, the day before start.

### Step 9. Post the close card and stop

Post to `{{REVIEW_CHANNEL}}`, full content every time. A human makes the offer.

```
[Candidate] / [Role] / Offer stage / [date]
Close-ready: Motive [Y/N] | Numbers [Y/N] | Ceiling [Y/N]
Gap: expectation [X] vs ceiling [Y] on total = [Z] ([%]) | Walk-away: [W]
Recommended structure: [name] | Cost [ ] | Signal [ ] | Risk [ ]
Trial close: candidate "[answer, quoted]" | approver "[answer, quoted]"
Counter-offer risk: [LOW/MEDIUM/HIGH] because [evidence]
Notice plan: resign [date] | wk1 [date] | mid [date] | logistics [date] | start [date]
Decision: Make the offer at [number/structure]? Yes / No
          Book the resignation rehearsal before the offer goes out? Yes / No
```

### Step 10. Write back, after the decision

Only after a human answers Yes:

- Log the close card as a note on the candidate in `{{ATS}}`, including the trial-close quotes and the risk rating.
- Create each notice-period touch in `{{CALENDAR}}` or as a task, with `{{OFFER_OWNER}}` as owner.
- Read every write back. Not found means retry once, then post a visible warning: "Notice plan not scheduled, manual entry needed". A missed mid-notice touch is how a quiet buy-back goes unnoticed.

Write failures never block the card. Never record an offer as made, accepted or signed. Those are human events.

## Batch mode

With several offers in flight, build one card each, then a summary ranked by risk: HIGH counter-offer risk first, then any card that failed the close-ready gate, then everything else by start date. Never reuse one candidate's motive or numbers on another's card.

## Handoffs

The skill works on its own. When other parts of the hiring process exist, it uses them:

- **Before:** a panel debrief that captured the candidate's reasons for moving in their own words, and any counter-offer signals, fills the motive check and seeds the risk rating.
- **After:** the notice-period plan ends on day one. Pass the candidate's stated motive and the promises made in the close to whoever runs onboarding, so the first 90 days keep them.

## What good looks like

- The formal offer is a formality. The candidate already said yes to its shape, in their own words, before it was written.
- Every structure on the card is priced three ways. Two out of three is a guess.
- A sign-on closes a gap without moving the salary band, and also tells the candidate the band would not move. Good plans say that out loud.
- A review promise carries a date and a measurable trigger, or it is left out. "We'll look at it in six months" is a hope, and candidates hear it that way.
- The best operators notice which number the candidate repeats. People anchor on the figure that matters to them, and it is often not the base.
- In sales hires the commission plan is half the offer. A strong close walks the candidate through how on-target earnings are actually paid: quota, accelerators, ramp, clawbacks, and what the last cohort really earned.
- The counter-offer conversation happens before the resignation, never after the buy-back offer is already on the table.

## Anti-patterns

- **The cold email offer.** A PDF lands with no call before it. The candidate's first reaction happens alone, or with their current manager.
- **Negotiating against yourself.** Raising the number before the candidate has asked, because the panel is nervous. It teaches the candidate the first number was not real.
- **The exploding deadline.** "We need an answer by Friday." It gets a yes that turns into a reneged acceptance, or a no that did not need to happen.
- **Silence during notice.** Four weeks without a call while the current employer works on them every day. The hire is not done until day one.
- **OTE theatre.** Quoting on-target earnings the last cohort did not hit. The candidate finds out in their first commission statement and starts looking again.

## Why the hard rules exist

- **The close-ready gate.** The usual reneged offer was built on a motive nobody checked. The candidate said "growth", the offer bought growth, and the real reason was the manager they wanted to leave, who then promised to change.
- **Confirmed numbers only.** Bands and inferences get the current package wrong more often than not, usually on commission, equity and benefits. A number off by ten percent turns a close into a negotiation.
- **No pressure tactics.** A pushed yes is a fall-off waiting for a reason. Replacing a sales hire who leaves in month two costs a full search plus a quarter of lost pipeline.
- **Sourced statistics only.** Candidates and their managers check. One invented figure costs the credibility of every true one.

## Rules

- MUST pass all three close-ready checks before building a plan. NEVER estimate a number the candidate or approver did not confirm.
- MUST end with a Yes/No for a human. NEVER send, extend or change an offer from this skill.
- MUST quote the candidate's own words when reconfirming their reasons for leaving. Paraphrase loses the pull.
- MUST read back every write and report failures on the card.
- NEVER coach pressure, guilt or exploding deadlines.
- NEVER inflate a counter-offer statistic. Use the sourced figures in the reference with their year and population, or say nothing.
- NEVER let the plan touch protected attributes. Family plans, age or health are not inputs to a counter-offer rating.
