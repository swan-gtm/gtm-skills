# Base Copywriting Rules

Universal rules for any outbound message — email, LinkedIn invite note, LinkedIn DM — across any persona. These are hard constraints: a message that breaks them is rewritten before it ships.

These rules are channel- and persona-agnostic. Channel specifics live in `linkedin-rules.md` and `email-rules.md`. The CTA framework lives in `cta-framework.md`. The angle method lives in `angle-framework.md`.

## 1. Length per channel

| Channel | Target | Hard limit |
|---|---|---|
| Email body | 50–100 words | 120 words |
| Email subject | 3–5 words | 6 words |
| LinkedIn invite note | 150–200 chars | 200 chars (hard limit, no exception) |
| LinkedIn DM | 40–70 words | 90 words |

Shorter beats longer. If a message exceeds the target, cut before sending.

## 2. Message structure

**Email**
```
Subject: [3–5 words, lowercase, internal-email feel]
[Opening: 10–20 words, names a tension or signal, never a question]
[Body: 2–3 sentences, develop the tension, no product pitch]
[Bridge: 1 sentence, what becomes possible]
[CTA: 1 ask, low-friction, value-framed — see cta-framework.md]
```

**LinkedIn DM (post-acceptance)**
```
[Opening: 10–15 words, an observation about their world, no question]
[1–2 sentences developing the observation]
[Soft close: a genuine question or open door, not a meeting request]
```

**LinkedIn invite note**
```
[1–2 sentences max, 200 chars strict, signal- or tension-based, no pitch, no link]
```

## 3. Opening rules

**Required:** 10–20 words max; names a specific tension, signal or insight the reader recognizes instantly; peer-to-peer tone.

**Forbidden:**
- Starting with a question
- Starting with "I" (sender-focused, not prospect-focused)
- Starting with a compliment ("Loved your post", "Impressive...")
- "I came across your profile / your company"
- "I hope this finds you well"
- Mentioning your product or company in the first line
- Corporate buzzwords ("leverage synergies", "optimize revenue", "drive impact")

## 4. Body rules

- **One problem per message.** Never stack two pains.
- **Short sentences.** One sentence = one line on mobile, max 20 words.
- **Active voice always.** "You can track X", not "X can be tracked".
- **Pronouns: "you" / "your team" / "your stack"** — never "I" as the subject.
- **No feature or benefit dumping** in a first-touch body.
- **Talk in problems and outcomes**, not "saving time" or "saving money".
- **Concrete over abstract.** "skip the manual data entry" beats "we save you time".

## 5. CTA rules (summary)

- One ask per message. Never two questions or multiple options.
- Low-friction, value-framed: what the prospect gains from the conversation.
- Never ask for a meeting in step 1 — value first, ask later.
- Full framework: see `cta-framework.md`.

## 6. Read-aloud test

Before a message ships, read it aloud:
- It must flow in under 15 seconds.
- It must sound like a person talking, not a sales script.
- No sentence should force a breath mid-way.
- If a sentence sounds corporate or plastic, rewrite it.

## 7. Anti-AI-tells checklist

A message must never contain these patterns — they flag it as machine-written instantly:

| AI tell | Why it breaks |
|---|---|
| Em-dash (—) or en-dash (–) in the body | The most obvious LLM signature |
| "Furthermore", "Moreover", "Additionally" | Corporate connectors |
| "Thus", "Hence", "Therefore" | Academic tone |
| "It is worth noting that..." | Filler hedging |
| "Imagine a world where..." | ChatGPT signature |
| Perfect triplets ("X, Y, and Z" repeated across consecutive sentences) | Generative pattern |
| Long sentences with multiple subordinate clauses | LLM over-formulation |
| Uniformly polite tone with no variation | "Plastic perfection" |
| 2+ exclamation marks in one message | LLM over-emphasis |
| ALL CAPS words | Pseudo-emphasis |

## 8. Forbidden phrases — universal

Always rewrite if any of these appear. (This list is universal — it applies to every user. Positioning-specific banned words are separate; see §10.)

**Opener clichés:** "I hope this finds you well", "I hope you're doing well", "I came across your profile/company", "I noticed you/your company...", "I wanted to reach out because", "I'm reaching out to", "Quick question:".

**Follow-up clichés:** "Just checking in", "Following up on", "Circling back", "Bumping this", "Did you see my last email?", "Did you have a chance to", "I haven't heard back".

**CTA clichés:** "Would you be open to a 30-min call?", "Can we jump on a quick call?", "Let me know if interested!", "Click here/link/below", "Book a slot in my calendar", "When works for you?".

**Filler / weak verbs:** leverage, utilize, optimize, streamline, facilitate, enable, empower, unlock, robust, synergies, best-in-class, world-class, cutting-edge, next-generation. → Use a strong, specific action verb instead.

**Hedging:** "I believe", "I think", "Perhaps", "It might be possible that", "imagine if you did X". → State it directly or cut it.

## 9. Creepy / boundary phrases

Technically informative but signal stalking. Avoid even when a real signal exists.

| Avoid | Use instead |
|---|---|
| "Saw you engaged with..." | "[Topic] is a real tension at [stage] right now" |
| "I noticed you visited our website" | Don't mention it |
| "I see you opened my last email" | Don't mention it |
| "Your colleague [Name] mentioned you..." | Don't fabricate name-drops |

Reference the *theme or content* a signal points to, never the individual action.

## 10. Two things that come from the user, not this file

- **Tone of voice** — match the user's brand voice, based on whatever the user has told you about how their company writes. Otherwise, default to a clear, confident, peer-to-peer "expert colleague" register and ask the user if a specific tone is required.
- **Positioning-specific banned words** — some companies ban words tied to their positioning (e.g. a premium brand banning "cheap", a platform banning "tool"). If the user has named such words, enforce them on top of §8. Default: none.

## 11. Variable / merge-tag rule

The only merge tag assumed safe in a message body is the first-name tag of the user's outreach tool (commonly `{{firstname}}`). Do not invent custom variables (`{{company}}`, `{{role}}`) unless the user states they have configured them. The skill generates full-text messages, not templates with intermediate slots.
