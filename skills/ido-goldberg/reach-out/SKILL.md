---
name: "reach-out"
title: Reach out
description: |
  Use this skill whenever creating outreach — a cold email, a LinkedIn message, a follow-up, or a multi-step sequence — for a company, a contact, a list, or a signal. Use it even when the user doesn't say "outreach": any request to write to, contact, message, or get in front of a prospect or account goes through here. Covers picking the hook, matching the org's voice, choosing the sequence shape, and staging everything for approval. Trigger phrasings: "reach out to", "draft outreach", "email this company", "message this prospect", "follow up with", "build a sequence", "contact these visitors".

  Also use it for strategic outreach questions ("how should our cold emails sound", "what cadence should we run") — the output is then a point of view grounded in the org's saved voice, not a sequence.
category: Outreach
---

Produces a staged outreach sequence awaiting the user's approval, with the reasoning attached: who, why now, what hook.

### The motion table — this org's, not the skill's

This table is the org's motion library. It starts seeded and is meant to be edited — rows get added, renamed, and replaced as the org's motions take shape. Open the matching reference before drafting; follow its don'ts over generic instinct.

| Situation | Reference |
|---|---|
| Named company, named contact, or a small account set | `references/targeted.md` |
| An identified website visitor | `references/website-visitor.md` |
| A recurring or scheduled list run, cold volume | `references/cold-list.md` |
| Someone engaged with a post or profile on LinkedIn | `references/linkedin-engagement.md` |
| Funding, hiring spree, leadership change, product launch | `references/company-signals.md` |
| Form fill, content download, demo request, MQL, signup | `references/inbound-hand-raiser.md` |
| Webinar or conference registrants, attendees, no-shows | `references/event-follow-up.md` |
| Third-party intent data — category research, review-site activity | `references/intent-signals.md` |
| The user gives feedback, wants outreach to sound or perform better, announces a strategy shift, or asks to set up the voice | `references/improve-outreach.md` |

No row matches (win-back, referral, reply handling) → run the procedure below and say so in the reasoning. A recurring motion with no row → propose creating its reference page and adding the row.

`references/improve-outreach.md` is how this skill becomes the org's: it says where every kind of feedback gets recorded. Open it whenever the user reacts to a draft — feedback that isn't written down is retraining that never happened.

### This org's voice and rules

Nothing recorded yet. Org-wide rules from user feedback live here, one do/don't per line with its condition when it has one. These outrank everything below except the user's live instruction.

### Anchor on the hook

Every message needs a reason it goes to this person now. Hook ladder: trigger event > relationship > their own content > company initiative > persona pain (usable, but say so in the reasoning). No hook → push back before drafting. NEVER invent a signal.

The hook informs the angle; it rarely appears in the copy. Tracking-type signals — website visits, intent data, profile views — NEVER appear in the message. A public event may be referenced once, later in the message, as an observation with its implication — NEVER as the opening sentence, never as a congratulation. Leading with someone's funding round or new hire is the clearest tell that a machine wrote the message.

### Voice

Approved sends accumulate automatically as style examples. Examples carry the voice; this skill carries the strategy — when they contradict, the skill is right, because examples can't be unsaved and lag every course change. Imitate an example's tone and rhythm, never a choice that breaks a rule. NEVER imitate copy from skill text or another org. No examples yet? Draft anyway from what's loaded — ICP pains, value prop, personas — plainly and shortly, tell the user the voice is provisional, and offer the voice setup flow in `references/improve-outreach.md`. If a contradiction keeps recurring, run that page's course-correction flow.

### Draft

- Opener, email: the hook's implication, in the contact's frame. One sentence. The event or signal itself never opens the message.
- Opener, LinkedIn: say who you are and what you want in the first line. A DM has no room for a warm-up observation — it reads as preamble and gets skipped.
- Body: one researched detail max, reacted to rather than exhibited. One proof point max — attributed, sized to the company. Never a feature list, never an invented customer or stat. On LinkedIn, drop the proof point and the hard numbers entirely; the register is a message between two people, not a pitch.
- CTA: one ask, and make it the smallest real thing that could land this week — a short list to run, one account to check, a sample to review. Offering to do concrete work, or asking for the raw material to do it, beats asking for time.
- Pitch at the reader's altitude: C-level hears risk and strategy, VP hears performance, director hears operational pain.
- Shape per email: signal → proof → ask (fresh trigger); problem → cost → fix (only when the pain is documented in the ICP); before → after → bridge (easy-to-picture change).
- Draft in the language the org sells in — a wrong-language sequence is an error, not a style choice.

### Cadence

The org's recorded cadence always wins; default: 3–5 steps, days ~0/3/7/14, single channel unless the motion says otherwise, never referencing one channel from the other. Every follow-up is shorter than the last, stands alone, and brings a genuinely new angle — new proof, sharper insight, useful asset, peer story — or gets skipped. Last touch: a 25–50 word breakup, door open, no new pitch — and once sent, honored. Multi-thread only for large accounts (~200+ employees), committee signals, or on request — different angle per contact, never the same email twice into one company.

### The final gate

Run on every message before staging; a failed check means rewrite, not tweak:

1. Delete the opener — still makes sense? The personalization is decoration; rebuild around the hook.
2. Does the close contain the word "worth"? Rewrite it. "worth 15 minutes", "worth a quick look", "worth a conversation" — anyone who receives outbound has read them a hundred times, and they cost replies. Ask for the thing itself instead.
3. Does sentence one name a funding round, a launch, a hire, or any other event? Rewrite — open with what it means for them, not with the news.
4. Could this go to anyone else this week? Then it's a blast in costume.
5. One CTA. 60–110 words, follow-ups shorter. Subject 2–5 words, lowercase, internal-looking. More "you" than "I/we".
6. Email: is the proof a number or a name? "Helps teams like yours" is not proof.
7. Read as the recipient with a full inbox: any reason to reply beyond politeness?

### Stage

Check for an existing unsent sequence to the contact — edit, don't duplicate. Stage for manual approval with the reasoning: who, why now, what hook, which reference. NEVER auto-send unless the user says so in this conversation. NEVER attach files; link instead. A channel missing its contact data gets fixed or dropped.

## What good looks like

A first-run draft — new org, zero examples — approved with a tweak, not a rewrite: a hook that fits nobody else this week, substance traceable to the org's ICP and value prop, nothing that smells like a template. Watch for: the proof point swelling into a feature list, the CTA collapsing into a calendar link, a segment blast dressed as personalization, and feedback evaporating instead of landing in the skill.
