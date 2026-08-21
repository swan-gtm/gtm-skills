---
name: track-champion-job-changes
title: Track champion job changes
description: |
  Use this skill when someone wants to track job changes for champions, get alerted when a
  champion or past buyer moves companies, follow champions to their new company, detect when
  a key contact leaves a customer account, turn customer alumni into pipeline, or monitor
  buying contacts for role changes. Builds a recurring Clay workflow that watches your
  champions — past buyers, power users, and key contacts at existing customers — and tells
  you the moment one changes jobs, then turns each move into two plays: FOLLOW the mover into
  their new company (your warmest possible outbound) and BACKFILL the seat they left (protect
  the existing account). Requires the Clay CLI + agent plugin (workflow tools).
  Do NOT use for general CRM contact cleanup or re-verifying a whole list's emails and titles
  (that is a contact-refresh job), or for sourcing net-new prospects by persona (people search).
  It sends nothing and writes nothing to your CRM without explicit approval.
category: Signals
tags: [Sales, RevOps]
---

# Track champion job changes

A champion who moves is the warmest pipeline you will ever get — someone who already bought
or used your product, now sitting inside a new account with fresh budget authority and a
honeymoon window in which tooling decisions are open. And every move is TWO plays, not one:
the new company becomes a target (FOLLOW), and the vacated seat at your existing customer
becomes a relationship risk (BACKFILL). Most teams run neither because nobody is watching.
This skill builds the watcher: a scheduled Clay **workflow** that checks each champion's
current employer, flags real moves, and produces a play-ready digest.

Clay workflows are an **Alpha** product — say so to the user before building, so they can
calibrate expectations.

## Step 0 — Verify Clay is working

Run `clay whoami; echo "exit_code=$?"`. If it fails, or the Clay workflow MCP tools
(`read`, `edit_node`, `validate_workflow`, `execute_clay_action`) are missing, run the Clay
plugin's `setup` skill (or follow
https://raw.githubusercontent.com/clay-run/agent-plugins/main/GETTING_STARTED.md), then
restart the agent if setup says to and re-run this skill. Confirm which workspace you are
signed into and tell the user before touching anything.

## Step 1 — Collect the inputs (interview the user; do not guess)

1. **The champion list.** Where do champions live today? A CRM export (CSV), an existing Clay
   table, or a Clay Audience segment. Minimum viable row: name + LinkedIn URL + the account
   (domain) you know them from. If there's no LinkedIn URL, ask for email instead — the
   workflow will resolve it. If champions aren't in an Audience yet, help the user get the
   list into one — an Audience segment is what lets the workflow re-check everyone on a
   schedule.
2. **What counts as a champion.** Past buyer? Power user? Deal contact on closed-won?
   This defines the list; don't expand it silently.
3. **The ICP filter for the FOLLOW play.** Industry, size, region — a mover whose new company
   is outside ICP gets logged, not pursued.
4. **Cadence.** Weekly is the sensible default; monthly for lists under ~200.
5. **Where the digest goes.** A summary table the user reads, a CSV, or a Slack/webhook
   destination the user owns.

## Step 2 — Plan the workflow and get approval

Present this plan, mapped to the user's inputs, and wait for approval before building
(follow the `workflows` skill's build protocol throughout):

```
TRIGGER: audience-scheduled over the "Champions" segment (weekly tick)
         + a manual trigger for testing
  1. [tool]        Resolve current employment. Resolution order matters:
                   (a) LinkedIn URL on file → person enrichment (cpj-enrich-person);
                   (b) no URL → people-index search by name + last-known company;
                   (c) reverse email→LinkedIn lookup LAST (weakest coverage; fails often).
                   → current employer name, domain, title, current-role start date
  2. [code]        Extract + compare, deterministically — never an LLM. Pin the tool
                   node's whole $.result (deep paths fail the run when empty), find the
                   is_current experience entry, normalize both domains, and emit flat
                   string fields: verdict (current / moved / unverified), evidence with
                   dates, new-company domain/name/title/start. Use non-empty sentinels
                   ("none") — a pinned value that resolves empty fails the run.
  3. [conditional] Rules mode, routing on the verdict string (rules cannot compare two
                   dynamic fields — that is why the code node computes the verdict).
                   → current: deterministic digest leaf (code node), end
                   → unverified: "could not verify" digest leaf (code node), end
                   → moved: continue. Genuinely ambiguous cases (rebrand/acquisition
                   suspicion) belong in the digest flagged for human review.
  4a. FOLLOW branch (real move):
      [tool]        Enrich the NEW company (industry, headcount, region)
      [conditional] ICP gate — outside ICP: log "moved, out of ICP", end
      [agent]       Compose the play: champion-arrival note anchored on the shared
                    history (which product, which account, when), plus 2-3 suggested
                    buying-committee titles to source at the new account
  4b. BACKFILL branch (real move, runs in parallel):
      [tool]        Find people at the OLD account matching the vacated title/persona
      [agent]       Pick the most likely successor + note why; flag "seat vacated"
  5. [leaf]        Append one digest row per champion: verdict, evidence, plays
```

Build node-by-node with `edit_node`, confirm every action's real shape with
`execute_clay_action` before wiring it, run `validate_workflow` with prettier, and show the
user the graph. Where more than one Clay action can do a step (several person-enrichment or
people-finding functions usually exist), list the options by human-readable name with costs
and let the user choose.

Build gotchas verified against the Alpha at time of writing — re-verify node shapes with
`execute_clay_action` before trusting them:
- Code nodes are `def handler(context):` returning a dict; read inputs with
  `context.get_input("name")`. Top-level `return` is a syntax error.
- Pin inputs via the flat `inputSchema` shorthand (`{"x": {"type":"string","sourceNodeId":
  "wfn_...","sourcePath":"$.field"}}`). Pins that resolve to undefined OR empty string fail
  the whole run — pin container objects, not deep paths, and emit sentinels.
- Prompt `{{vars}}` on agent nodes fill reliably from flat string/object pins; a raw array
  pin can leave the model claiming it got nothing. Flatten arrays in a code node first.
- Tool-node parameters wire via `tools[].inputMappingConfig` references, and the referenced
  value must ALSO be pinned on that tool node's `inputSchema` when it comes from 2+ hops back.
- Keep agents on a cheap model while wiring, then graduate only the nodes that write prose;
  comparisons and routing stay in code — an LLM asked to compare domains may wander off to
  the web instead.

## Step 3 — Test small, then scale

1. Run 3–5 champions through with `clay workflows runs test` — include at least one you
   know has NOT moved (the no-change path must terminate cheaply) and, if possible, one
   known mover.
2. Walk the user through each run's path. Fix, re-test.
3. Before the first full run: estimate cost (roughly 1–3 credits per champion per check —
   verify against the actual actions chosen with `execute_clay_action` / `clay credits`),
   state the total, and get explicit approval.
4. Publishing the draft as live automation is the user's click in the editor — prompt them,
   don't attempt it yourself.

## What good looks like

- **Join and compare on domains, never company-name strings.** Names differ across sources
  ("Initech Ltd" vs "Initech"); domains don't. If the enriched employer has no domain,
  validate one before deciding anything.
- **A move verdict must trace to evidence in the enrichment payload** — quote the old and
  new employer with dates in the digest. Never infer a move from a name mismatch alone, and
  never fabricate a change to have something to report. Empty or errored enrichment = "could
  not verify", not "no change" and not "moved" — and watch for the sneaky version: an
  enrichment can return status SUCCESS with an empty payload. Gate on the presence of an
  actual employer value, never on the run status.
- **Use the current-role start date.** A mover who started < 12 months ago is in the
  honeymoon window — tooling decisions are open. Rank the FOLLOW digest by recency.
- **Both plays evaluated for every real move.** A digest that only follows movers and never
  flags vacated seats is half the value.
- **The FOLLOW note leans on the shared history** — which product, at which account, roughly
  when. "Congrats on the new role" with no history is generic outbound wearing a costume.
- The common mistake: treating every domain mismatch as a move. Acquisitions and rebrands
  produce mismatches constantly; the verdict step exists because of them.

## Rules

- MUST get explicit user approval before the first full run, any CRM write, and any
  publish/schedule — and NEVER send outreach automatically; the digest ends at play-ready.
- MUST re-check credits before scaling a run to the full list.
- NEVER drop a champion silently: every input row lands in the digest as verified-current,
  moved (with plays), out-of-ICP, or could-not-verify.

## Output

Per scheduled run, one digest with a row per champion:
`champion · old account · verdict (current / moved / could-not-verify) · evidence · new company ·
new title · ICP fit · FOLLOW note draft · suggested committee titles · BACKFILL successor ·
seat-vacated flag`
plus a summary line: champions checked, moves found, plays generated, rows needing human review.

## Worked example

Input: 120 champions in an Audience segment "Champions — Closed Won", weekly cadence,
ICP = B2B software 100–5,000 employees, digest to a summary table.
First test run of 5: 4 verified current, 1 real move — Jordan Lee, former Head of RevOps at
longtime customer acme.com, now VP RevOps at northfield.io (2,300-person B2B software firm,
in ICP). Digest row: verdict MOVED with LinkedIn evidence; FOLLOW note referencing the
three years Jordan ran your product at Acme; suggested committee: CFO, Director of Sales Ops;
BACKFILL: Priya Shah, current Director of RevOps at Acme, flagged as likely successor;
seat-vacated alert on the Acme account. Weekly cost at 120 champions ≈ 150–350 credits;
user approved before the first full run.
