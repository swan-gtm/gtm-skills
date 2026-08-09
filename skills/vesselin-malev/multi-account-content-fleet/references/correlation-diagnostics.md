# Correlation diagnostics

Fleet health is a correlation question, not an average question. A dashboard reporting fleet-wide totals will never surface the failure this chapter describes.

## The baseline

Per account, track a rolling median of impressions per post over the trailing 10 posts. Median, not mean, because one outlier post distorts a mean for weeks and hides the trend underneath.

Record alongside it: posting window, format, and topic lane. Diagnosis needs these attached, and reconstructing them after the fact is where most fleet analysis stalls.

Re-baseline after any deliberate change to lanes, cadence, or production process. Comparing across a process change produces a number that means nothing.

## Reading the chart

Plot every account's baseline on one chart.

**Independent movement is health.** Accounts rising and falling on their own schedules means each is being judged on its own merits. Expect this to look messy. Messy is the goal.

**Correlated movement is the alarm.** All accounts moving together, up or down, means the fleet shares a signature that the feed has priced in. The direction matters less than the correlation. Correlated rises are equally diagnostic, and they usually precede a correlated fall, because the shared element that worked is the shared element that gets discounted.

**One account diverging** is an account-level issue. Check its lane, its cadence, its recent format changes. This is the only case where post-by-post analysis is the right tool.

## When correlated decline hits

Stop diagnosing individual posts. Post-level analysis on a correlated decline produces plausible explanations for every post and fixes nothing, because the cause is not in any post. It is in what they share.

Hunt the shared element in this order, cheapest to break first:

1. **Posting window.** Did windows drift together? Did a scheduling tool normalize them?
2. **Format.** Pull the last 20 posts fleet-wide. What percentage are one format? Above 60% is a signature.
3. **Hook shape.** Read only the first lines, all accounts, stripped of names. If they are interchangeable, that is the answer.
4. **Formatting.** Line break patterns, emoji use, bold conventions, list structure. These converge silently because they come from whoever is doing production.
5. **Production batch.** Were these written in one session by one person? Check the calendar, not people's memories.
6. **Topic.** Did the lanes collapse toward whatever is hot in the category?

Break one element at a time and give it three posts per account before judging. Breaking several at once means learning nothing about which mattered, and fleets tend to repeat the same convergence.

## After the break

Re-baseline from scratch. The old baseline described a fleet with the shared element in it and is no longer a comparison.

Expect the corrected accounts to separate before they recover. Divergence is the first sign the fix worked, and it usually shows up a cycle before the numbers do. An operator who judges the fix on impressions alone will abandon it too early.

## The trap

The most common failure is optimizing toward whatever the best-performing account does. It is a reasonable instinct and it produces the exact signature this chapter is about. Every account adopting the winner's hook shape converges the fleet within a month, and the winner's numbers fall with everyone else's.

When one account outperforms, copy the principle, never the pattern. If it is winning because it tells specific customer stories, other accounts should tell their own specific stories from their own banks. They should not adopt its opening line, its structure, or its posting time.
