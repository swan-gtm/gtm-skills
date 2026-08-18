# Re-runs, memory, and dedup

Brand monitoring only earns its keep on the second run: memory is what turns a pile of search results into "here's what's new." Keep a running memory file per brand in your workspace (one file per brand, e.g. `brand-monitor/[brand]/memory.md`), plus a saved copy of each run's report next to it.

## The memory file

Holds, per known mention:

- **Fingerprint:** `{url, platform, published_date}`. Normalize URLs before fingerprinting — strip query parameters and trailing slashes, lowercase the host — so the same post shared with tracking parameters doesn't read as new.
- **Last composite score and tier**, plus the last engagement counts observed (reposts, replies, upvotes, views). These counts are the baseline that makes real velocity scoring possible on the next pass.
- **Status for Crisis/Watch items:** open or handled.

Also record run metadata at the top: last run timestamp, window covered, source profile used, competitors tracked, routing preference. Load this before asking setup questions — a returning user confirms, never re-enters.

## Dedup lifecycle (runs after scoring, before tier assignment)

For every mention found this run, check its fingerprint against memory:

1. **Not in memory → net-new.** Full treatment: tier, card, routing.
2. **In memory, composite moved 10+ points → returning.** Keep it in the feed at its new tier with a `↩ returning · score changed` badge. A score shift is news — usually velocity or fresh replies — and must never be suppressed as a duplicate.
3. **In memory, score unchanged → suppressed.** Move to the Log tier; exclude from Crisis/Watch/Engage unless the user asked for full history.

Open the report with the split: `X net-new · Y returning (score changed) · Z suppressed (already logged)`. After the run, write the new fingerprints, scores, and engagement counts back to memory.

**Carry-forward:** Crisis and Watch items stay listed on every subsequent run — with current status and velocity arrow — until the user marks them handled. Suppression applies to noise, never to open incidents.

## Date windowing by run type

- **First run:** use the window the user confirmed (default: last 7 days). No baseline exists — velocity is proxy-only and labeled `~estimated`; say explicitly that trends start on the next pass.
- **Refresh (a day or more since last run):** window from the last run's timestamp to now. Sweep for net-new mentions; re-fetch open Crisis/Watch items to update velocity.
- **Same-day repeat (within ~2 hours):** don't re-sweep everything. Re-fetch every mention that scored Watch or higher and compare engagement to the stored counts — 20%+ growth upgrades the tier and marks `↑ accelerating`; flat or declining marks `→ stable` / `↓ declining`. Add a quick pass over the fastest sources (the profile's tier-1 social) for brand-new items.
- **User names an explicit window** ("June 1–15", "since the launch"): use it verbatim; dedup still applies.

## Cadence guidance

- **Continuous monitoring:** daily or every few days.
- **Launches and campaigns:** every 6–12 hours for the first 48 hours.
- **Crisis mode (any open Crisis item):** every 1–2 hours until the item is handled or clearly declining.

Whatever the cadence, always record the run timestamp — it is what makes the next window calculation and the "only what's new" promise possible.
