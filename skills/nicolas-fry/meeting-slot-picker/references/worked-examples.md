# Worked examples

Three cases run end to end with the scoring rubric. Every score below is the rubric applied exactly, so these double as a check: if the same inputs produce different numbers, the arithmetic went wrong somewhere.

## 1. Cross-timezone revenue booking (prospect 3 hours ahead)

**Setup.** The VP of Operations at a 200-person logistics firm replies to a proposal with "grab time on my calendar next week" and a booking link. Her signature puts her in the Eastern zone. The user works Pacific, 08:00 to 17:00. Her lunch is unknown, so the default 12:00 to 13:00 applies (see the edge-case playbook). The user picks Tuesday.

**Calendar read for Tuesday (user's clock).**

| Time (PT) | Item | Real meeting? |
|---|---|---|
| 08:00 to 08:30 | REMINDER: send proposal | No, a nudge |
| 11:00 to 11:30 | Pipeline review | Yes |

Meeting load: 1. The reminder does not count toward load, but it still occupies its half hour.

**Slots offered, with both clocks written down before scoring.**

| Her time (ET) | User time (PT) | Score | Reason |
|---|---|---|---|
| 13:00 | 10:00 | **100** | First slot after her lunch. Pipeline review starts 30 min after the call ends, so no runway penalty. |
| 13:30 | 10:30 | 85 | Post-lunch window, but the pipeline review starts 0 min after: -15. |
| 14:30 | 11:30 | 72 | Early-to-mid afternoon. |
| 11:30 | 08:30 | 30 | Her last hour before lunch. |
| 15:30 | 12:30 | 20 | Her last 90 minutes. |
| 16:00 | 13:00 | 20 | Her last 90 minutes. |
| 14:00 | 11:00 | 0 | Collides with the user's pipeline review. |
| 09:00 | 06:00 | 0 | Her best morning window, but 06:00 for the user. Outside the user's hours. |

**The trap, both directions.** Her 09:00 looks like a 92 in her clock and is a 06:00 call for the user. And the user's own instinct, "after my lunch, around 12:30", lands in her last 90 minutes and scores 20. Writing both clocks per slot is what catches both.

**Pick.** Tuesday 1:00 PM ET / 10:00 AM PT. Reason line for the user: "1:00 PM her time, first slot after her lunch with the afternoon open behind it, and 30 minutes of buffer before your pipeline review." Tuesday becomes a 2-meeting day, so no load note.

**Confirmation draft, held for approval.**

> Hi [first name], grabbed time through your booking link. Tuesday, [month] [day] at 1:00 PM ET is confirmed. Looking forward to walking through the proposal.

## 2. Internal clustering (before and after free-block numbers)

**Setup.** A vendor the user already pays sends a booking link for a 30-minute onboarding check-in. Not revenue-facing: focus mode, user's clock. The user says "Monday or Wednesday". Workday 09:00 to 18:00.

**Calendar read.**

| Day | Items | Real meetings | Free gaps | Longest block |
|---|---|---|---|---|
| Monday | Customer call 13:00 to 14:00, team sync 16:00 to 16:30 | 2 | 09:00 to 13:00 (4h00), 14:00 to 16:00 (2h00), 16:30 to 18:00 (1h30) | 4h00 |
| Wednesday | Inbox block 09:00 to 09:30 (solo) | 0 | 09:30 to 18:00 (8h30) | 8h30 |

**Scoring.**

| Slot | Longest block before, after | Base | Bonuses | Score |
|---|---|---|---|---|
| Mon 14:00 | 4h00, 4h00 | 100 | +6 day has meetings | **106** |
| Mon 15:30 | 4h00, 4h00 | 100 | +6 | **106** |
| Wed 09:30 | 8h30, 8h00 | 94.1 | +4 edge | 98.1 |
| Wed 17:30 | 8h30, 8h00 | 94.1 | +4 edge | 98.1 |
| Mon 09:00 | 4h00, 3h30 | 87.5 | +6, +4 edge | 97.5 |
| Mon 11:00 | 4h00, 2h00 | 50 | +6 | 56 |
| Wed 13:00 | 8h30, 4h30 | 52.9 | none | 52.9 |

Wed 13:00 is what an unguided booking looks like: an open afternoon, an easy click, and the user's only 8-hour day becomes two 4-hour halves.

**The fork.** Monday 14:00 wins on score and sits directly behind the customer call, but it makes Monday a 3-meeting day, and this meeting is neither revenue-producing nor time-sensitive. That is a real question, so ask:

> Two options for the vendor check-in:
> 1. Mon 2:00 PM, right after the customer call. Costs no focus time, but makes Monday your 3rd meeting.
> 2. Wed 9:30 AM, right after your inbox block. Wednesday stays meeting-free apart from this, and keeps an 8-hour block.
>
> Monday if you want Wednesday untouched, Wednesday if Monday already feels full.

Between 14:00 and 15:30 on Monday, the rubric ties. 14:00 sits directly against the customer call, so it is the one to offer.

## 3. Ambiguous classification

**Setup.** A fractional COO who has sent the user two client referrals asks for "a coffee chat to catch up" via a booking link. Partner or networking? It could go either way. Same timezone. Thursday, workday 09:00 to 18:00, one real meeting: board prep 10:00 to 11:00.

**Score both modes before asking.**

| Slot | Revenue score | Revenue reason | Focus score | Focus reason |
|---|---|---|---|---|
| 09:00 | 92 | Her first hour; board prep is 30 min after, no penalty | **110** | Longest block stays 7h00; day has meetings; edge |
| 11:00 | 30 | Her hour before lunch | 98.9 | 7h00 to 6h30 |
| 13:00 | **100** | First slot after her lunch | 70.3 | 7h00 to 4h30 |
| 16:30 | 20 | Her last 90 minutes | 88.6 | 7h00 to 5h30; edge |

**Decision.** 09:00 is near the top in both modes, so the classification does not change the answer. Book it and skip the question. State the read anyway: "Treating this as partner-adjacent; 9:00 works either way, first thing for her and it keeps your 7-hour afternoon intact."

**When no slot is good in both modes,** the classification decides the answer, so ask: "Is this a partnership conversation or a catch-up? If partnership, 1:00 PM gives her the afternoon; if catch-up, 9:00 keeps your afternoon clear." One question, two concrete options.
