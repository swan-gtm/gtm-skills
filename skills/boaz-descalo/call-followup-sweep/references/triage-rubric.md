# Triage rubric

Which calls earn an email, which get nothing, and how open commitments age.
The sweep's value is subtraction: a run that drafts one email per call has
replaced a calendar, not a judgment.

## Does this call earn an email?

A call earns a draft if **any one** of these is true:

| Trigger | Weight | Note |
|---|---|---|
| The user committed to something | **Always** | One unshipped promise is sufficient on its own. No other trigger is needed. |
| A number, price, or SLA was said aloud | **Always** | Put it in writing correctly now, or inherit the buyer's version of it later. |
| A date was named by the buyer | High | Their date sets the cadence; acknowledge it in writing so it becomes shared. |
| A new stakeholder appeared or was promised | High | The email is what gets forwarded to them. Write it for the person who wasn't there. |
| A question went unanswered | High | Answer it in the draft, or name the date you will. |
| Next step discussed but not on a calendar | Medium | The draft's only job is to convert it to a booked slot. |
| An objection surfaced for the second time | Medium | Address it in writing, plainly, once. |

A call earns **no email** when all of the following hold:

- Neither side committed to anything.
- No number, price, or date was said aloud.
- The next meeting is already on the calendar.
- No new stakeholder, no unanswered question, no repeated objection.

In practice this covers standing check-ins, mid-project status calls, and
already-booked second meetings. On a typical week sweep, **roughly half to two
thirds of calls earn no email** — if a sweep is drafting for 90% of the book,
the triage is not running and the output is noise.

Three additional no-email cases, regardless of triggers:

- **Already handled.** A thread to that account exists post-call. Say so; do not
  draft a second one.
- **Internal call.** No external attendee — extract commitments for the aging
  report only.
- **Unverified call.** No recording, no transcript, no notes. It goes on the
  coverage list as unread. Never draft from a calendar title alone.

## Dedupe rules

- **One account, one email.** Multiple calls with the same account inside one
  window collapse into a single draft built from all of them, addressed to the
  most senior participant who was on the most recent call.
- **One thread, one ask.** If two calls with an account produced two unrelated
  asks, the draft carries the one that gates the other and names the second as
  coming separately.
- **Different accounts, same parent company** stay separate unless the same
  person was on both calls.

## Aging thresholds

Applied to every open commitment carried forward from prior sweeps. These are
business days from the call the commitment was made on.

| Age | State | What the sweep does |
|---|---|---|
| 0–2 days | Fresh | List under the account. No special treatment. |
| 3–5 days | **Aging** | Flag it. Lead the account's draft with it. |
| 6–10 days | **Overdue** | Surface at the top of the sweep report, above all fresh drafts, with the original quote and date. |
| 11+ days | **Rotted** | Report separately. Do not silently fold into a normal follow-up — a two-week-late promise needs the delay named in the draft, not glossed over. |

Two rules that matter more than the thresholds:

- **A commitment with no date attached ages from the call date**, not from some
  implied grace period. "I'll send that over" made eleven days ago is rotted,
  not pending.
- **Aging beats freshness in the report order, always.** A user reading a sweep
  top-to-bottom should hit their oldest broken promise before their newest
  drafted email. Ordering the report by call date instead of by age is the most
  common way this skill gets rendered useless.

## Coverage reporting

Every sweep states, before any draft: calls in window, calls read, calls
unverified, drafts produced, no-email count, open commitments by age bucket. A
sweep that reports drafts without reporting coverage is claiming completeness it
has not earned.
