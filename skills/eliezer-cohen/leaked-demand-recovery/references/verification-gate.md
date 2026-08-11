# The verification gate

Read this before running step 3. Every re-engagement workflow assumes the CRM is right. It usually
is not, and the failure is asymmetric: a missed recovery forfeits one opportunity, while messaging
someone who already booked, already replied, or is already being worked costs the relationship.

## Failures this gate exists to prevent

Each of these has produced a false drop in a live pipeline.

- A CRM last-contacted field reported a prospect silent for three weeks. The mailbox showed an email
  sent five days earlier. The field lags, misses sends from other addresses, and misses non-email
  channels entirely.
- A follow-up was flagged as never sent because the search used the company name as a keyword. It had
  been sent as a reply inside an older scheduling thread whose subject never contained that name.
- A mailbox search returned only its first page. Later pages were silently absent, and valid sends
  were flagged as missing.
- A thread search returned only the first few messages per thread. The most recent message, a
  submitted proposal, sat further down and was invisible to every search made against it.
- A CRM auto-flipped past meetings to a completed status regardless of whether anyone attended,
  making that status worthless as evidence a call happened.

The rule that follows: **a single system is never sufficient evidence, in either direction.** Not
evidence that someone was dropped, and not evidence that they were not.

## Verification rules

- **Only a forward-dated event counts as a live booking.** A past-dated meeting is not a booking to
  protect, and an auto-applied completed status is not proof anyone attended.
- **When systems disagree, the system closest to the event wins.** The calendar beats the CRM on
  bookings. The mailbox beats the CRM on last contact. The recorder beats the calendar on attendance.
- **An empty result means the query was wrong, not that the person is cold.** Resolve the actual
  contact record and email domain first, then search by address and by domain. Never conclude "no
  activity" from a keyword search that returned nothing.
- **Paginate to exhaustion.** If a response carries a continuation token, follow it until there is
  none. A partial pull manufactures false drops.
- **Never conclude a thread's last message from search snippets.** Search commonly truncates threads
  to their first few messages. If any other system suggests activity more recent than the last
  visible message, fetch the full thread before deciding anything.
- **Search by recipient address, not by keyword.** A follow-up sent as a reply inside an older thread
  will not match a company-name search.
- **Two checks are required before flagging an owed follow-up as unsent:** the complete sent history,
  and a targeted search restricted to that recipient's domain after the event date. Either alone has
  produced false positives.
- **Note channel blind spots rather than assuming silence.** Messages sent over social, SMS, or from
  a personal address will not appear. Absence of evidence in the mailbox is not evidence of absence,
  and the gap belongs in the output as a stated limitation.

## Recording the verdict

State the evidence checked for every candidate, whether it passed or failed, so the call is auditable
by someone who was not there. A verdict without its evidence is an assertion, and assertions are what
this gate exists to replace.
