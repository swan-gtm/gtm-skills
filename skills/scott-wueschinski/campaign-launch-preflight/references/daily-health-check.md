# Daily sending health check

The preflight ends at launch; sending health does not. Run this every sending day, after the send window closes, for every campaign in a sending state, and for two further sending days after a campaign completes, pauses or stops, because bounces and complaints from the last send arrive late. Do not reuse a mailbox on a new campaign until those two reads are clean.

## What to read

| Measure | Granularity | Source |
|---|---|---|
| Sends, bounces, spam complaints, replies, unsubscribes | Per campaign and per mailbox, that day | The sending platform's analytics, never the summary card alone |
| Mailbox health score | Per mailbox, that day | The sending platform's own health or deliverability score |
| Inbox placement | Per sending domain, weekly | A seed placement test reporting inbox, spam and missing counts |

Placement needs its own test because bounce and complaint rates can stay flat while mail quietly lands in spam. Bounces measure sending; placement measures arrival.

Log every read with the date, the campaign, the denominators and the source.

## When to hold

Use relative triggers per mailbox, and adopt an absolute threshold only when you have a source you trust for it. Rates are cumulative for the campaign to date, counted against the send that caused each event, so a late bounce never divides by a small day.

Pause a mailbox the same day when any of these holds:

- its cumulative bounce or complaint rate is at least double what it read the previous sending day;
- it read zero bounces and complaints the previous sending day and reads any today;
- the platform marks it disconnected, errored or warm-up failed;
- its health score has fallen below the platform's own "good" band.

Worked readings: 0 of 40, then 1 of 60, pauses it. 1 of 100, then 3 of 140, pauses it (1.0% to 2.1%). 1 of 100, then 2 of 500, does not (1.0% to 0.4%).

Pause every mailbox on a domain when its weekly seed test inbox share falls to half or less of the previous week's. The first test sets the baseline and holds nothing.

A campaign whose aggregate rate doubles while no single mailbox breaches gets a same-day read of its mailbox mix, not a pause; a hold needs a mailbox to act on.

## Ongoing hygiene

- Compare reply rates across live campaigns on the same mailboxes weekly. A campaign far below its siblings on the same infrastructure usually carries a blocked word or phrase. Find it, rewrite, and relaunch as a new campaign.
- Refresh copy at least every two weeks. A push of unchanged copy does not count as a refresh; rerun the spam-word check and the rendered read after every rewrite.
- After any raise in a daily limit, take one full day's read before raising again.

Every pause is reported with its numbers, and the undo is resuming the mailbox.
