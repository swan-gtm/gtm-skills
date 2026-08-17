# Build guide: read-mostly, one source of truth, sane refresh

How to construct the surface on any stack without it turning into a maintenance burden. These are the three patterns that decide whether a command center survives past its first month.

## Pattern 1: mirror, do not own

Every lane reflects a system of record you already keep. The command center reads that system and lays the current state on one screen. It does not become the place the data lives.

Why this is the whole game: the fastest way to kill a personal dashboard is to let it hold state that also lives elsewhere. The two copies drift within days, you catch the surface being wrong once, and you never trust it again. Mirror and link out, and the surface can be wrong only if the source is wrong.

Concretely:
- Read from the source on a schedule; render a view; link each item back.
- Store nothing on the surface except the few interaction bits below.
- If a lane needs data no system currently holds, fix that in the source system first, then mirror it. Do not let the dashboard become the shadow database.

## Pattern 2: read-mostly, with a few kept-here actions

A pure read-only board sends you back to the source tool for every small thing, which defeats the point. Allow a short list of low-friction actions that keep you on the surface, and push everything heavier back to the source.

- Keep on the surface: mark an item done, add a short note, attach a link, snooze or flag.
- Send back to the source: composing a real deliverable, editing a record's core fields, anything a teammate also touches.

Give every item a stable id so a kept-here action (a done toggle, a note) attaches to the right item across refreshes instead of creating a duplicate.

## Pattern 3: a refresh cadence you can reason about

Decide, per lane, how fresh it needs to be, and make the refresh boring and predictable.

- Fast-moving lanes (inbound, replies) refresh often; slow lanes (events, content calendar) refresh daily.
- Show a last-refreshed marker so you know whether you are looking at live state or a cache.
- If the surface runs unattended (a scheduled job assembling it), assume the job cannot reach every source every time; degrade gracefully, show the stale marker, and never present a cache as live.

## Assembly options

You do not need a bespoke app. In rough order of effort:

1. A single page your existing tools already offer (a saved board view, a filtered list) - start here if one tool holds most of your lanes.
2. A lightweight page that pulls from each source's export or API on a schedule and renders one view.
3. A small local service that aggregates and serves the page, if you want interaction (done toggles, notes) and offline resilience.

Start at the lowest rung that covers your lanes. Build up only when a real gap forces it.

## What not to build

- A second CRM. If you are re-entering deal data, stop.
- A universal inbox that also sends. Sending and composing belong in the source tools with their approval rails.
- A metrics warehouse. Trend analysis is a weekly review artefact, not a daily operating surface.
