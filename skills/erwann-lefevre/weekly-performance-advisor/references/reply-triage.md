# Triaging the reply queue

The first section of any weekly review, and the one that decides whether the review was worth running.

## Classify

Four buckets, read from the whole thread rather than the last message:

| Class | Meaning |
|---|---|
| `interested` | Positive intent — wants to know more, asks a question, engages with the offer |
| `neutral` | Replied without committing — "not now", "send me info", a deflection to someone else |
| `not_interested` | Explicit no |
| `wrong_fit` | Not the right person or company at all |

Flag explicit meeting or call requests separately. They aren't just interested — they're a scheduled loss if missed.

## Only actionable replies get rows

`interested` and `neutral` are listed. `not_interested` and `wrong_fit` collapse to a count.

Rejections are worth knowing in aggregate and not worth reading individually. Listing them pads the queue with items requiring no action, which is how a triage list stops being read.

Neutral belongs in the actionable set. "Not now" is a follow-up date, and it's the bucket most often silently dropped.

## Urgency order

Group, then sort within group:

1. Meeting and call requests
2. Interested
3. Neutral

Within each group, **longest-waiting first**. Show the wait in days on every row.

Past about three days, a warm reply has cooled enough to mark as urgent. The specific threshold matters less than having one — the failure being prevented is a genuinely interested prospect sitting under a pile of newer, less interesting replies because the queue was sorted newest-first.

Note that this ordering deliberately puts an old neutral below a fresh interested reply, but an old interested reply above a fresh one. Intent outranks recency across groups; recency decides within them.

## Correcting automatic qualification

Where a system pre-classifies replies, review the classification rather than trusting it — automatic qualification is reliably over-optimistic about anything containing polite language, and a courteous brush-off scores as interested.

Keep a visible count of corrections. It's a small number that says something useful: a classifier consistently mislabelling one category is a finding in its own right, and it's invisible if corrections are made silently.

Correct the working view, not the source system. The person reviewing should confirm changes there themselves — a weekly report shouldn't be quietly rewriting CRM state as a side effect of being generated.

## Counting the week

Count from every reply received this week, not from the queue of replies still awaiting an answer. Otherwise answering someone removes them from the week's total, and the weekly number falls as the team does more work.

Two headline counts are enough: positive replies, and total replies. Positive is the one worth leading with — total replies moves with send volume and says little on its own.
