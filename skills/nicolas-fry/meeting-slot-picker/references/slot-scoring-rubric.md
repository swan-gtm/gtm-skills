# Slot scoring rubric

The full scoring logic behind step 4. Score every candidate slot the same way, every time, so the same calendar produces the same pick on a different day. Doing it by feel drifts. Work through the arithmetic explicitly and keep the reason string for each slot: the reason is what goes into the summary for the user.

## Inputs to collect first

Every candidate carries both clock readings. Converting timezones is the error-prone step, so do it once, deliberately, before scoring, and never inside the scoring.

| Input | Default | Notes |
|---|---|---|
| Duration | 30 min | Use the length the booking page offers. |
| Counterparty workday | 09:00 to 17:00, lunch 12:00 to 13:00 | Override when their real pattern is known (an early-shift plant manager, a team that lunches at 11:30). |
| User workday | 09:00 to 18:00 | Take it from the calendar's working hours if set. |
| Each candidate | day, counterparty local start, user local start | Write both. If they are the same zone, write the same time twice. |
| Busy items per day | start, end, title, real meeting or not | Real meeting = another human is expected. Reminders, solo focus blocks and task nudges are not. |

## Revenue mode (counterparty's clock)

### Hard zeros

A slot scores 0 and drops out if any of these is true. Each check uses the full duration, not just the start time.

| Check | Example of a zero |
|---|---|
| Starts before or ends after the counterparty's workday | A 30-minute slot at 16:45 runs to 17:15. |
| Overlaps the counterparty's lunch at all | A 30-minute slot at 11:45 runs into 12:00. |
| Overlaps anything on the user's calendar, solo blocks included | A slot on top of the user's inbox block still double-books them. |
| Falls outside the user's working hours | Their 09:00 is the user's 06:00 when they are 3 hours ahead. |

### Windows

Match the slot's start time against these windows in order. The first match wins, and a slot in a weak window scores 30 or 20, never the 40 default. Taking the higher of the window score and the default would floor the weak windows at 40 and erase the penalty, and the weak windows are exactly the ones this exists to steer away from.

| Order | Window (default workday) | Defined as | Score | Reason to give |
|---|---|---|---|---|
| 1 | 13:00 to 13:45 | lunch end to lunch end + 45 min | 100 | First slot after their lunch, fed and reset, afternoon open behind them. |
| 2 | 09:00 to 10:00 | workday start to start + 60 min | 92 | First thing in their morning, freshest attention before the day's fires start. |
| 3 | 13:45 to 15:30 | lunch end + 45 min to workday end - 90 min | 72 | Early-to-mid afternoon, still has runway behind it. |
| 4 | 10:00 to 11:00 | start + 60 min to lunch start - 60 min | 66 | Mid-morning, solid, though the pull toward lunch has started. |
| 5 | 11:00 to 12:00 | last 60 min before lunch | 30 | Hungry and watching the clock. |
| 6 | 15:30 to 17:00 | last 90 min of the workday | 20 | Commute, pickup, hard stops, mental checkout. |
| none | any other in-hours start | | 40 | Inside their workday but in no preferred window. Happens with nonstandard workdays. |

The two weak windows share one cause: **the counterparty has a wall in front of them.** Someone with a wall coming compresses the conversation, skips the questions they wanted to ask, defers the decision and proposes "a follow-up" instead of moving. The prize in a revenue conversation is optionality: if it is going well, the call can keep going. When a real calendar does not fit the table, reason from that.

### Runway penalty

Runway on their side is wasted if the user has a hard stop right behind it. Subtract **15** when a real meeting on the user's calendar starts 0 to 29 minutes after the slot ends. Reminders and solo blocks do not trigger it, because the user can slide them. Apply it once per slot, for the nearest such meeting. A post-lunch slot with a hard stop 10 minutes behind it scores 85: still good, but below a clean first-hour slot at 92.

## Focus mode (user's clock)

### The one rule

Pick the slot that leaves the **longest unbroken free block** in the day as long as possible. That single rule produces clustering without a pile of sub-rules. A 30-minute meeting dropped into an open morning costs far more than 30 minutes, because it turns one usable 3-hour block into two 75-minute stubs. The same meeting pressed against an existing commitment costs almost nothing, because the morning was already broken there.

### Free-block arithmetic

1. List every busy item in the user's workday, solo blocks included.
2. Merge overlapping or touching items into single occupied spans.
3. List the gaps: start of day to the first span, between spans, last span to end of day. The edge gaps count.
4. **Before** = the longest gap.
5. Add the candidate slot as one more busy item and repeat. **After** = the new longest gap.

Example: workday 09:00 to 18:00, meetings 13:00 to 14:00 and 16:00 to 16:30. Gaps are 09:00 to 13:00 (4h00), 14:00 to 16:00 (2h00), 16:30 to 18:00 (1h30). Before = 4h00. A slot at 11:00 splits the morning into 2h00 and 1h30, so after = 2h00. A slot at 14:00 leaves the morning untouched, so after = 4h00.

### Score

| Component | Points |
|---|---|
| Base | 100 x after / before (100 if the day has no free time to begin with) |
| Day already has at least one real meeting | +6. Concentrating interruption beats spreading it. |
| Slot starts within 60 min of the day's start or ends within 60 min of its end | +4. Edges fragment less than the middle. |
| Overlaps any busy item or falls outside the user's workday | Hard zero |

A slot that costs nothing on a day with meetings scores 106. Cutting a clean day's 8h30 block to 8h00 at the edge scores about 98. Cutting a 7h00 block to 4h30 scores about 70. Scores compare well within a day. Across days, read the reason strings too: a 98 on a clean day and a 97.5 on a busy day are a tie, and the tiebreaker is to keep the clean day clean.

### Known blind spot

Only the longest block counts. Two slots that both leave the longest block intact score the same even if one shreds a 2-hour afternoon block and the other does not. When the top slots tie, prefer the one that sits directly against an existing meeting.

## Meeting load (both modes)

Count real meetings already on the day, add one for the candidate. At **3 or more**, say so in one line in the recommendation and name a lighter nearby day if one exists. This is guidance, not a gate. Revenue-producing and time-sensitive meetings are what a crowded day is for; never push a prospect out a week to protect a calendar.

## Reading the result

| Situation | Action |
|---|---|
| Top slot 10 or more points ahead of the next | Book it. |
| Top two under 10 points apart, same day | Book the higher one. |
| Top two under 10 points apart, different days | Offer both with the tradeoff named. |
| Best revenue slot this week scores 30 or less | Treat it as a fork: see the edge-case playbook. |
| Every candidate is a zero | Report why (timezone gap, conflicts) and ask for another window. |
