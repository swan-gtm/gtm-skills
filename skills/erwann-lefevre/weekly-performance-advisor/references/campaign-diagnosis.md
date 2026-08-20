# Diagnosing a campaign

## Which channel sets the status

A campaign sending 900 LinkedIn messages and 60 emails is a LinkedIn campaign that also sends some email. Its email reply rate is real and it should not decide whether the campaign is broken.

- **Primary channel** = the one with more sends.
- **Co-primary** when the smaller channel carries a meaningful share of total volume — around 30% is a reasonable line.
- Only the primary (or both, when co-primary) sets campaign status.
- **Bounce is always driving.** A bounce problem damages the sending domain and the deliverability of every other campaign from that address. It counts regardless of channel weighting.

A red metric on a non-driving channel gets flagged as a leg to fix — "email leg to fix" — rather than condemning the campaign. This is the difference between "rewrite your sequence" and "the email half of this needs attention", and getting it wrong sends someone to rewrite copy that most of the audience never saw.

## Status

To fix if any driving metric is red. Watch if any driving metric is amber. On target otherwise.

## One fix, at the earliest broken step

Walk the funnel in order and take the **first** red:

1. Bounce
2. Connection acceptance
3. Email open
4. LinkedIn reply
5. Email reply

Everything downstream of a broken step is measuring a filtered audience. If connection acceptance is at 12%, the LinkedIn reply rate describes the unusual minority who accepted anyway — improving the message copy is treating a symptom while the targeting problem keeps selecting the wrong people.

**Exclude the break-up message from diagnosis.** The final touch is designed to underperform — it exists to close the loop, not to convert — and flagging it burns the one fix on a step working as intended.

## Cause and action

| Broken metric | What it usually means | What to do |
|---|---|---|
| Bounce | List quality, or a domain that hasn't been warmed | Verify the list, check warm-up and sending volume |
| Connection acceptance | Targeting, or the connection note | Revisit who's being targeted before touching copy |
| Email open | Subject line, or sender reputation and setup | Rework subjects; check technical setup if it's severe |
| LinkedIn reply | Message copy | Rewrite the opener and the CTA |
| Email reply | Message copy | Rewrite the opener and the CTA |

Note that the first two point away from copy. The reflex on any weak campaign is to rewrite the messages, and roughly half the time the messages aren't the problem.

## Confidence

State a diagnosis as strongly as the evidence supports.

Severity above roughly 40% below floor is a confident call. Below that it's directional. And **cap confidence whenever the flagged step's own volume is thin** — under about twenty sends on that specific step, a red metric is a hypothesis regardless of how far below floor it sits.

The failure this prevents is confidently telling someone their fourth touch is broken based on eleven sends.

## Ranking the fix list

Sort by **severity × people affected**.

A campaign 5% below floor reaching four thousand prospects outranks one 40% below floor reaching ninety. Severity alone ranks the small broken campaigns to the top, and fixing those first is the wrong use of a Monday.

## The channel recommendation

When both channels are scored and one is clearly working while the other isn't, that's worth saying directly: favour the channel that's working, rework or drop the other leg.

Teams frequently keep a failing email leg attached to a strong LinkedIn campaign because the sequence was designed multichannel and nobody revisited the assumption. The data says to stop.
