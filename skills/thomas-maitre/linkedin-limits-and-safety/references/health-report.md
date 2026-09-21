# The Monday health check and the one-screen report

## The check

Run every Monday. One line per question, yes or no:

- Invites sent last week under 100? Acceptance rate above 30 percent?
- Pending invites older than 3 weeks withdrawn?
- Any action sent on a weekend?
- Any note over 200 characters on a free account?
- Any day with visits, reactions or comments at the cap? (Cap days are fine
  occasionally; five in a row is a pattern.)
- Replies to messages within 24 hours? A conversation opened by a tool and abandoned
  by a human is the thing that earns the "I'm not interested in your bot" screenshot.

## The report

Plain words, one screen, no table dump:

```
Account: <name>, <free | Premium>. Today <used>/<cap> actions.
Invites 12/20, messages 8/40, visits 31/40, reactions 14/30, comments 3/15.
Last 7 days: <invited> invited, <accepted> accepted (<rate>%). <verdict>.
Weekdays, <start> to <end> <tz>. Cap: <fine | lower it because ...>.
Tools touching this account: <names>. Pending invites over 3 weeks: <n>, withdrawn.
Next check: Monday.
```

## Verdict rules

| Condition | Verdict |
|---|---|
| acceptance under 30 percent | "fix targeting before sending more" |
| any action at cap for 5 days running | "pattern, lower the cap" |
| any warning sign from the ladder this week | "pause, then halve the cap for two weeks" |
| stale invites not withdrawn | "withdraw today; counts against the weekly limit" |
| none of the above | "fine; hold the cap" |

The verdict is one of those five sentences. A report with a paragraph of nuance in
place of a verdict is a report nobody acts on.

## Worked example

```
Account: Marie D., free. Today 58/145 actions.
Invites 20/20, messages 8/40, visits 22/40, reactions 8/30, comments 0/15.
Last 7 days: 96 invited, 24 accepted (25%). Fix targeting before sending more.
Weekdays, 08:00 to 19:00 Europe/Paris. Cap: lower invites to 10 for two weeks.
Tools touching this account: one outreach tool, one by-hand user. Pending over 3 weeks: 41, withdrawn.
Next check: Monday.
```

The invites were at cap five days running and the acceptance rate is 25 percent: two
verdict conditions at once. The cap goes down and the targeting gets fixed before it
goes back up.
