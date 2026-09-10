# Draft patterns

The shape of the email, by what the call actually was. Every pattern below caps
at 150 words and three visible action items. Overflow becomes a named next call,
never a longer email.

## The universal spine

Every draft, regardless of type, is four moves in this order:

1. **The one thing** — the single most consequential item, in the first line.
   Usually the user's own commitment with a date on it.
2. **The commitments, dated and owned** — a short list, each with a name and a
   date. Theirs and yours, in the same list, so the reciprocity is visible.
3. **The forwardable sentence** — one sentence a champion can paste to someone
   who was not on the call, stating what this is and why it matters to them.
4. **One ask** — a booked slot, a document, an introduction. Exactly one.

No greeting paragraph, no "it was great speaking with you", no recap of what
they told you about their business. They were there.

## By call type

**First discovery.** Lead with the thing you owe. The forwardable sentence
carries the most weight here, because the person who decides is usually not on a
first call. Ask for the next meeting with two concrete slots. Do not attach
collateral unless it was asked for by name.

**Technical or security review.** Lead with the artifact and its date. Answer
the unanswered question in writing or state exactly when you will. This is the
one call type where being slightly longer is correct — a security contact
forwards the email itself as evidence. Still no recap.

**Pricing or commercial call.** Restate every number that was said aloud, in
writing, correctly. If a figure was hedged on the call ("call it low five
figures"), either confirm it or correct it now — this is the entire purpose of
the email. Ambiguity here is what becomes a procurement fight.

**Stalled or re-engagement call.** One paragraph. Name the gap plainly without
apologizing for it, state what changed since, make one ask. If nothing has
changed since the last touch, the correct output is no email and a note to that
effect.

**Renewal or customer check-in.** Lead with what you owe them operationally, not
with commercial terms. Commitments here are usually support or roadmap items
and they age worse than sales promises because nobody is chasing them.

**Multi-call account (deduped).** Structure by workstream, not by call. Two
headers maximum. The recipient should not be able to tell it was assembled from
three conversations.

## Anti-patterns

- **The recap.** Any draft whose first paragraph narrates the call. If the email
  would still make sense to someone who did not attend *and* to someone who did,
  it is doing neither job.
- **The swappable draft.** If replacing the account name produces a valid email
  for a different account, it is a template. Something said on the call must be
  in it, ideally quoted.
- **The stacked ask.** Three questions at the end. The recipient answers the
  easiest one and the other two die.
- **The undated commitment.** "I'll get that over to you shortly." Shortly is
  not a date and creates the exact rot the sweep exists to catch.
- **The apology opener.** "Sorry for the delay" spends the first line on the
  seller's feelings. State the new date and move.
- **Borrowed voice.** A draft written in a register the user does not use costs
  more to fix than to write from scratch. Match their prior sent mail; when
  there is no sample, stay plain and short and say that voice was not matched.

## Worked example

From the discovery call in `commitment-extraction.md` — Dana, VP Ops, SOC 2
raised twice, 40-seat pricing hedged aloud, Marcus joining next time.

> **Subject:** SOC 2 report + 40-seat pricing
>
> Dana — SOC 2 report is attached; that was the piece you said had to be
> resolved before this goes anywhere internally, so it goes first.
>
> - SOC 2 Type II report — attached (me, today)
> - Confirmed 40-seat pricing — I'll send the real number Thursday, not the
>   rough one I gave on the call (me, Thu)
> - Marcus joining the next session (you)
>
> For Marcus: we handle the workflow your team is running manually today, and
> the open question is what it costs at 40 seats rather than whether it works.
>
> Thursday or Friday afternoon for the next one — which is easier?

Why it works: the user's own two commitments are dated and owned, the hedged
number is explicitly flagged as being corrected rather than left to anchor, the
forwardable sentence is written for Marcus rather than for Dana, and there is
exactly one ask. It never mentions Dana's last vendor, which is the most
memorable and least useful thing she said.
