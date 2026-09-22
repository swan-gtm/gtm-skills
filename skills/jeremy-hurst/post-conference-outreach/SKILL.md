---
name: "post-conference-outreach"
title: "Post-conference outreach"
description: "Use this skill when the booth or badge-scan list comes back from a conference and every scan needs a follow-up that sounds like it was written by the teammate who actually had the conversation. It reads scanner initials to pick the sender, classifies each scan Hot, Warm, or Cold from facts rather than labels, lets the hottest temperature on an account win for every colleague scanned there, and routes Hot to a 2-step booked-meeting confirm and Warm/Cold to a 7-step nurture built on the booth notes. Every account is researched first. Nothing auto-sends."
category: Events
---

# Post-conference outreach

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{EVENT_NAME}}` - The conference as people say it in a DM
- `{{PRODUCT}}` - Your product name as it reads in a lowercase DM
- `{{SCANNER_INITIALS_MAP}}` - Initials to teammate, as they appear at the start of badge-scan notes (e.g. `JD` -> Jane Doe, `MK` -> Mike Kim)
- `{{EXEC_SENDER}}` - Teammate with the authority lens: talks to whoever owns the problem and its budget
- `{{SALES_LEADER_SENDER}}` - Teammate with the seller-management lens: talks to people who manage sellers
- `{{PRACTITIONER_SENDER}}` - Teammate with the practitioner lens: talks to hands-on operators of the GTM stack
- `{{EXEC_SENDER_MIN_ORG_SIZE}}` - Employee count above which {{EXEC_SENDER}} may send on the persona fallback (default: 100)
- `{{CRM}}` - Your CRM (e.g. HubSpot, Attio, Salesforce)
- `{{ELEVATOR_PITCH}}` - Your persona-matched elevator pitch reference (one variant per persona; never hardcoded in a sequence)
- `{{DEMO_LIBRARY}}` - Your list of demo video URLs by use case (e.g. enterprise platform, seller prospecting, expansion, general)
- `{{LEAVE_BEHIND_RESOURCE}}` - A low-ego resource you own that is useful even to people who never buy (a public playbook, a free tool, a library)
- `{{CALENDAR_LINKS}}` - Booking links per sender, plus the rule for which calendar a non-sales sender drops
- `{{ATTENDEE_TAG}}` - The tag or memory line you use to record "this person attended {{EVENT_NAME}}"
- `{{M1_CHAR_CAP}}` - Hard character cap on the first email body (default: 250; +25% only when real history is woven in)
- `{{VOICE_GUIDE}}` - Optional: a sender's voice guide to load when they are the sender

---

### When to use this page

A **booth or badge-scan list upload**, or a manual chat ask to run **post-conference follow-up** on named scans. The hook is the in-person conversation at the booth (or the scan with no notes). Temperature routes the shape. Sender is whoever had the conversation when initials are on the notes; otherwise the persona owner.

This is a reusable play. Fill in {{EVENT_NAME}} from the upload or the invocation. Score or scoring tier does **not** route or skip anyone.

**Do not use this play when:**

- The list is pre-event attendees and the ask is a meeting before or during the conference plus a side event. That is pre-conference outreach.
- You already sat with them at an in-person dinner (or the upload is a dinner guest list with a status column). That is a dinner follow-up (a separate play, not included here).
- They registered for or attended an event and the ask is generic warm-up with no booth scan and no dinner. That is a generic event-registrant play (a separate play, not included here).
- {{CRM}} shows the account is a current customer or closed-won (including alias or sibling domains). Existing-customer hard stop. Do not sequence.

Approval is always queued for a human. There is no auto-send carve-out on this play.

---

### Research every account before drafting (mandatory)

Do not draft M1, assign temperature, or stage a sequence for a row until this has run on that domain.

For every row, read **both**:

1. **Account memory** for the company (the contact's domain, plus any alias or sibling domain already on the account).
2. **{{CRM}} activity at the company level**, not just this contact. Pull the company's engagements, notes, meetings, emails, and open or closed deals. Scan every associated contact, not only the person on the list.

Empty memory plus a quiet {{CRM}} feed is still a completed research pass. Record what was read in the reasoning log:

`research: [memory + CRM records actually read]; prior deal: none | [deal stage + one-line context]; history: none | substantive`

If that line is missing, the research did not happen. Do not build.

This is in addition to your standard live-thread and account-engagement gates, not a substitute for them. Customer or closed-won still hard-stops.

**Substantive historical context** (any one is enough): a live meeting already held with someone at the account, and/or a real back-and-forth on email or LinkedIn (not unreplied outbound). When that exists, weave **one** concrete thread into M1 naturally. Do not dump the history, do not ignore it. That weave also raises the M1 character cap (see M1 below). History weaving applies to **Scenario 2 M1** only. Do not pad Scenario 1's short confirm or include-you lines with extra history.

A live unanswered inbound thread and an already-engaged owner still hard-stop.

---

### Booked-meeting gate - scoped exception (Hot, including account-max Hot)

Your standard account-engagement gate normally hard-stops any sequence when a meeting is already booked. **This play is a manual-invocation exception for Scenario 1 (Hot) only**: the contact who has the meeting **and** other scans at the same account who inherit Hot via account-max temperature.

Hot *is* a booked next-step meeting. Do not hard-stop those rows. Stage the 2-step Hot path below (confirm the date, or ask to include the colleague; do not run the Warm/Cold 7-step).

Customer or closed-won, a live unanswered inbound thread, a different sender's live thread, and an already-engaged owner still hard-stop. If a meeting is actually on the calendar for this contact or a colleague at the account, the row is Scenario 1, not Warm/Cold.

---

### Temperature (router)

Read a dedicated temperature or lead-temperature column first. If none, read the notes for an explicit `hot` / `warm` / `cold`. Then apply the definitions. Do not trust the label over the facts.

**Hot:** we met them at the conference **and** a next-step discussion is **actually on the calendar** (not "let's find time", not "I'll send you something"). A date on the calendar is required.

**Warm:** highly relevant persona + high-quality target company (high ACV potential) + some stated interest (a use case you address, stated interest in a follow-up), **and no booked meeting**.

**Cold:** highly relevant persona + high-quality target company, **no** stated interest. Nurture. Keep them in orbit.

**Label vs facts:**

- Field or notes say Hot but there is no booked date: **not Hot**. Treat as Warm if interest is stated, else Cold. Flag the mismatch in the reasoning log.
- Field or notes say Warm/Cold but a meeting is on the calendar: **upgrade to Hot**.
- No field and no temperature word in the notes: infer from the definitions (booked date = Hot; stated interest, no date = Warm; ICP fit, no interest = Cold). If they are not a relevant persona or not a high-quality target, skip and flag. Do not run this play on junk scans.

**Highest temperature on the account wins.** Classify every scan on the file (and any already-known booked meeting at the domain from research). Then apply the **max** temperature at the company to every remaining row at that company.

Example: one person at the company books a follow-up (Hot). A later scan of someone else at the same company is Warm or Cold. Treat the later scan as **Hot** too: Scenario 1, not the 7-step. M1 on the inherited-Hot contact is the include-you variant below, not the date-confirm variant.

Hot (own meeting or inherited) runs **Scenario 1** (2 steps). Warm and Cold run **Scenario 2** (7 steps). Temperature does not change sender.

---

### Sender (who had the conversation, then persona fallback)

This play **overrides tier-based sender routing**. One contact, one sender.

**1. Badge-scan initials (first).** Notes often start with the scanner's initials. Match the start of the notes (trim, case-insensitive) against {{SCANNER_INITIALS_MAP}}.

Initials mean that teammate had the conversation. They send, including the exec sender on a small account and a non-sales teammate who scanned. Do not "correct" initials with the persona rubric.

**2. Other obvious scanner.** If there are no initials but the upload, the thread, or the invocation names who worked the booth or who is asking you to follow up, that person sends.

**3. Fallback: persona owner.** Only when there are no initials and no other way to tell who had the conversation. Assign from the contact's actual role (judgment on the real job, not a fixed title list). Same exec size gate as pre-conference outreach: {{EXEC_SENDER}} only if org > {{EXEC_SENDER_MIN_ORG_SIZE}} employees **and** authority-lens; otherwise {{SALES_LEADER_SENDER}} keeps the exec-persona contact.

| Sender | When | Mandate | Desired outcome |
|---|---|---|---|
| **{{EXEC_SENDER}}** | Their initials, or fallback: org > {{EXEC_SENDER_MIN_ORG_SIZE}} **and** owner of the problem or budget | Authority lens | Meeting |
| **{{SALES_LEADER_SENDER}}** | Their initials, or fallback: people who manage sellers; also exec-mandate contacts at or under the size gate | Seller-management lens, plus small-org exec fallback | Meeting |
| **{{PRACTITIONER_SENDER}}** | Their initials, or fallback: hands-on practitioners (GTM engineers, RevOps who run the stack, growth and funnel leads, director-level marketing ops or GTM systems owners) | Practitioner lens | Meeting |
| **Any other scanner** (e.g. a partnerships or marketing teammate) | Their initials only; they are not in the persona fallback | They had the conversation | Meeting; if the notes are a partner conversation, keep it a partner conversation. Do not silently convert it into a customer pitch. |

Hard exclusions on the **fallback only** (initials still win):

- {{PRACTITIONER_SENDER}} never connects with salespeople or sales managers. Those fallback rows go to {{SALES_LEADER_SENDER}}.
- Prefer VP or Head over Director of Sales for {{SALES_LEADER_SENDER}}.
- Prefer director-level operators over manager-level RevOps for {{PRACTITIONER_SENDER}}.

If a row has no resolvable LinkedIn URL, skip the LinkedIn steps and flag. Do not invent a URL. If there is no work email after enrichment, fall back to LinkedIn-only rather than emailing a personal inbox.

Load {{VOICE_GUIDE}} when it exists for the chosen sender.

---

### Scenario 1 - Hot (booked meeting, including inherited)

Two steps. Day 0. Do **not** pitch, demo, zoom out, drop a resource, or ask for a *new* meeting. The CTA is confirm (own meeting) or include (colleague's meeting).

| Step | Timing | Channel | Content |
|---|---|---|---|
| 1 / M1 | Day 0 | Email | Confirm the booked date, or ask to include them on a colleague's booked meeting. |
| 2 | Immediate (same day as M1) | LinkedIn connection request | Blank. No note. Auto-skips if already connected. |

**M1 - this contact is the one with the meeting (verbatim shape):**

```
Great meeting you, NAME. Look forward to going deeper on DATE!
```

**M1 - this contact inherited Hot from a colleague's booked meeting (verbatim shape):**

```
Great meeting you, NAME. I'm scheduled to chat with your ROLE NAME on DATE - make sense to include you?
```

Example: `Great meeting you, Mike. I'm scheduled to chat with your CRO Dave on Oct 11th - make sense to include you?`

`DATE` is the booked meeting date, short month for long month names (`Oct 11th`, `Dec 2nd`; `May 4th` is already short). `ROLE NAME` is the colleague's title + first name as you would say it (`your CRO Dave`), not a legal entity or email. Use the contact's first name. Do not add booth notes, pitch, or a second ask.

If the date cannot be formatted from the file, {{CRM}}, or the calendar, stop and flag. Do not guess a day. If inherited Hot but you cannot name the colleague, flag. Do not send a date-confirm as if this contact owns the meeting.

---

### Scenario 2 - Warm / Cold (7-step nurture)

Same shape for Warm and Cold. Temperature only changes **M1**: Warm/Cold with notes end on an open-ended question. Cold with no stated interest still gets the question when notes exist (the notes are the hook, not a fake "you seemed interested"). No notes: generic fallback, no invented question.

Do **not** add a side-event step to this 7-step. The calendar drop is the meeting ask. Do not mix in pre-conference side-event copy.

| Step | Timing | Channel | Content |
|---|---|---|---|
| 1 / M1 | Day 0 | Email | Booth notes (or generic fallback), plus history weave when research found it. **Max {{M1_CHAR_CAP}} characters** (+25% only with substantive history). Warm/Cold + notes ends on an open-ended question. |
| 2 | Immediate (same day as M1) | LinkedIn connection request | Blank. No note. Auto-skips if already connected. |
| 3 / M2 | Day 3 | Email | 2-min-chat lead-in + persona-matched {{ELEVATOR_PITCH}} |
| 4 / DM1 | Day 7 | LinkedIn DM | Tried you on email + persona or situation-matched demo |
| 5 / DM2 | Day 12 | LinkedIn DM | Zoom-out |
| 6 / DM3 | Day 19 | LinkedIn DM | {{LEAVE_BEHIND_RESOURCE}} drop |
| 7 / DM4 | Day 27 | LinkedIn DM | Calendar drop |

Gaps stretch on purpose. Do not even-space the later DMs.

This play is **exempt** from your cold-outreach no-mention, no-pitch, no-CTA rules on **M1 only** (the booth conversation is the prior relationship; M1 may name the chat). M2 is the first explicit pitch. The persona-matched pitch check applies from M2 onward.

---

### M1 - notes, character cap, history weave, temperature close

Booth notes are the hook. Read them first. Strip the leading initials before writing. Do not put your internals in the email.

Then apply the research pass. If **substantive historical context** exists (a live meeting already held with the account, and/or a real email or LinkedIn back-and-forth), weave **one** concrete thread into M1 in a natural way. Do not dump the history. Do not ignore it. Do not use history as a substitute for the booth notes when notes exist: notes first, history as the second beat.

**Hard cap: {{M1_CHAR_CAP}} characters** on the M1 email body (full message, including the name). **+25% only when that substantive history is actually woven in.** Quiet research (empty memory, quiet {{CRM}}) does not get the bump. If a draft exceeds the cap that applies, cut before staging. Record the character count **and** which cap was used in the reasoning log.

**Notes exist (Warm or Cold):** one concrete callback from the notes, tied to an **open-ended question**. Do not dump the notes. Do not pitch. Do not drop a calendar link in M1.

**No notes:** generic event follow-up. Do not invent a conversation.

```
NAME - Great meeting you!
```

Never mention a badge scan, a booth list, or that you "pulled attendees".

---

### M2 - 2-min context + canonical pitch (Warm / Cold only)

Email. Continue the thread; do not write a second opener. Pull the persona-matched pitch from {{ELEVATOR_PITCH}}. Do not hardcode a pitch here. Drop any casual aside for C-level and VP recipients.

Lead-in (keep this shape; sentence case for email):

```
Realizing we only chatted for 2 mins, so you probably don't have full context on what we actually do... [persona-matched pitch]
```

If the booth notes already showed they know what you do, still run this step. The 2-min line is the point. Do not skip M2 because the scan looked sophisticated.

---

### DM1 - demo (Warm / Cold only)

LinkedIn DM. Lowercase. No name-fronting.

```
tried you on email. quick {{PRODUCT}} demo to paint a better picture: [demo url]
```

Pull the URL from {{DEMO_LIBRARY}}. Never hardcode. Never wrap in markdown. Pick **one**, matching the **booth notes** first, then the persona. Typical library: an enterprise or platform demo for large-org strategic conversations, a seller-prospecting demo for AEs, SDRs, and sales managers, an expansion or upsell demo for PLG and usage-growth conversations, and a general product demo as the fallback. Record which asset and why.

---

### DM2 - zoom-out (Warm / Cold only)

```
to be clear, {{PRODUCT}}'s not just for [the use case this sequence has been about] - [persona-matched other applications].
```

Match the zoom-out to the persona: sales, RevOps, and GTM engineering get one set of applications; marketing and demand gen another; ABM another. The persona-matched pitch check fails if the zoom-out still lists the wrong function's use cases.

---

### DM3 - leave-behind resource (Warm / Cold only)

Canonical low-ego leave-behind. Skip if they have already consumed {{LEAVE_BEHIND_RESOURCE}}; swap in a different resource you own rather than restating the same one.

```
even if you never check out {{PRODUCT}}, thought i'd share [what it is, one clause]: [url]
```

Own it ("our playbook", "our library"). Never "found this".

---

### DM4 - calendar drop (Warm / Cold only)

Bare calendar. No new angle.

```
will leave my cal for if/when relevant: [cal url]
```

Sender's calendar from {{CALENDAR_LINKS}}. When {{EXEC_SENDER}} is the sender, follow your size rule for whose calendar to drop (default: under 200 employees, {{SALES_LEADER_SENDER}}'s calendar; 200 and above, {{EXEC_SENDER}}'s). A non-sales sender (practitioner or other scanner) drops {{SALES_LEADER_SENDER}}'s intro calendar as the handoff, unless the notes are clearly a partner conversation owned by that scanner (then do not drop a customer calendar: flag and stop after DM3, or keep the thread with the partner owner).

Plain-text URL. Never markdown.

---

### List-upload / manual-invocation execution

- **Research every row first.** No exceptions.
- Classify temperature per contact, then apply **account-max** temperature before choosing Scenario 1 vs 2.
- Sequence every row that is Hot, Warm, or Cold unless a standard gate trips (customer, live thread, already-engaged owner). Scenario 1 booked meeting (own or inherited) is **not** a trip.
- Check existing sequences per contact; read the full message history; edit, don't duplicate.
- Blank connection requests (no note). Plain-text URLs. No unfilled merge fields left in copy.
- Stage queued for approval. Confirm: "Drafted a [2-step Hot / 7-step Warm/Cold] post-conference sequence for [contact] at [company], staged for your approval. Sender: [name]. Temperature: [Hot/Warm/Cold]. Hook: [one line]."
- **After staging:** write the person-level attendee line to account memory and apply {{ATTENDEE_TAG}} on the company. One line per person per event. Skip only rows that were never sequenced.

The reasoning log on every sequence must include:

- Sender source: `initials=XX`, `named scanner`, or `persona fallback` + mandate + exec size gate verdict when fallback
- Temperature + evidence (field, notes word, or inferred; booked date if Hot) + `account-max=` and whether this row inherited Hot from a colleague
- `research:` + `prior deal:` + `history:` line
- Event name
- M1 character count + which cap on Scenario 2; Hot date used (and colleague name and role if inherited) on Scenario 1
- Demo asset chosen + why (Scenario 2)
- Pitch variant (Scenario 2)
- A compact pre-flight line citing this play's sender override, and the Hot booked-meeting exception when Hot

---

### Rules

- MUST read badge-scan initials first and send from that teammate.
- MUST fall back to the persona owner only when initials and scanner are unknown. Apply the exec size gate on that fallback only.
- MUST research every account (memory + {{CRM}} company activity) before drafting. No exceptions.
- MUST classify Hot / Warm / Cold from the definitions, not from a wrong label. Then apply **highest temperature on the account** to every scan at that company.
- MUST run Scenario 1 (2-step) for Hot, own meeting *or* inherited, and Scenario 2 (7-step) for Warm/Cold. Do not mix.
- MUST keep Warm/Cold M1 <= {{M1_CHAR_CAP}} characters, or <= +25% only when substantive history is woven into M1.
- MUST pull the pitch from {{ELEVATOR_PITCH}} and demo and calendar URLs from {{DEMO_LIBRARY}} and {{CALENDAR_LINKS}}. Never hardcode.
- MUST NOT hard-stop Scenario 1 rows for the booked meeting that makes them Hot (own or inherited).
- MUST NOT sequence a closed-won or customer account.
- MUST NOT mention the badge scan or list as the source.
- NEVER auto-send on this play.
- MUST, after staging, write the attendee line to account memory and apply {{ATTENDEE_TAG}} on the company. One line per person per event.

---

## What good looks like

The scan notes are the whole advantage. A good M1 sounds like the person who stood at the booth wrote it in 30 seconds. A mediocre M1 could have gone to anyone you scanned.

What to spot first: the initials, then whether a meeting is actually booked **at the account**, then one line in the notes worth continuing. Temperature is a fact pattern, not a vibe. Highest temperature on the account wins.

What gets overlooked:

- Treating "let's follow up" as Hot. It is Warm.
- Sending the 7-step to a Warm scan when a colleague at the same company already has a meeting on the calendar. That row is inherited Hot.
- Skipping memory and {{CRM}} company activity because "it's a list upload".
- Rewriting initials to match the persona rubric. If the sales leader scanned a RevOps director, the sales leader still sends.
- A 251-character M1 with no history weave. Cut it. The bump is only when history is actually in the message.
- The generic demo on an AE, or the AE demo on a CMO.

Failure modes: running the pre-conference play on a badge-scan file; hard-stopping Hot because a meeting is booked; treating a second scan at a Hot account as Warm/Cold; padding Scenario 1 with booth-notes history; putting side-event copy into Scenario 2; pitching in M1; name-fronting the DMs; hardcoding demo URLs.

Success: the Hot email is a date confirm or an include-you on the colleague's date; the Warm/Cold M1 could only have been written from those notes (and, when history exists, one real prior thread); the rest of the cadence is pitch, demo, zoom-out, leave-behind, calendar, from the teammate who actually met them.
