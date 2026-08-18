---
name: meeting-prep
title: Meeting prep
description: |
  Use this skill when a meeting is coming up and you need to know who is in the
  room before you walk in. Produces a meeting briefing: each attendee's role,
  background, and recent public activity with conversation hooks, a
  cross-attendee relationship map, company context, specific talking points,
  watch-outs, and — for sales, partnership, and investor meetings — value
  positioning grounded in research. Triggers: "prepare me for my meeting",
  "who am I meeting with", "research this person", "meeting prep", "brief me
  on this person", "I have a meeting with this company", "get me ready for my
  call", "what should I know about them", "background on someone before our
  meeting", "attendee research".
category: Sales
tags: [Sales]
---

# Meeting prep

Runs before any meeting where you'd benefit from knowing the people across the table better than they expect. Produces one briefing per meeting: who the attendees are, what they've been saying publicly, how they connect to each other, what's happening at their company, and exactly what to bring up — never a generic dossier.

## The play

### 1. Pin down the meeting

Extract from the request (or ask): attendee names, company, meeting date, and any context the user volunteers ("they're evaluating us", "board intro"). If a calendar is connected, offer to pull today's meetings so the user can pick one; if not, skip silently. If only a name is given, proceed and infer the company from research.

Then establish the **meeting type**, because it gates the whole briefing shape:

| Signal in the request | Type |
|---|---|
| "prospect", "demo", "sales call" | Sales / discovery |
| "interview", "candidate" | Interview |
| "board", "investor" | Board / investor |
| "partner", "integration" | Partnership |
| "check-in", "sync", "1:1" with a colleague | Internal |
| No signal | **Ask — don't guess** |

The type decides whether the Value Positioning section is produced: yes for sales/discovery, partnership, and board/investor; no for interview, internal, and general external. That's worth one clarifying question when there's no signal.

### 2. Load what you already know

Keep a running file per person and per company in your workspace (e.g. `people/alex-kim.md`, `companies/widgetco.md`). Before searching:

- Person file updated **within 24 hours** → offer to reuse it: "I have a fresh profile on this person — use it, or refresh?" (Meeting prep is per-meeting, not per-day — never refuse a second prep in one day.)
- Person file **under 30 days old** → load it as known context and research only what's new since. Pass the known facts into the research so it doesn't re-report them.
- **Over 30 days old** or missing → full refresh.

Follow cross-references between files: if an attendee's file links to a company or competitor you've researched before, load that too — prior meeting notes and tracked-competitor intel are the highest-value content a briefing can carry.

### 3. Research each attendee, in parallel

One research thread per attendee, run concurrently. Read `references/attendee-research.md` for the full query fan-out (two groups of searches), name-disambiguation rules, page-extraction limits, and the exact profile format each thread must return. For a single attendee, just run the searches directly — no fan-out overhead. If any thread fails or comes back empty, rerun its searches yourself; never leave a gap in the briefing.

While threads run, have them flag overlaps for the relationship map: shared past employers, schools, boards, communities. "My attendee worked at that company 2019–2022 — did yours overlap?" is the question that produces relationship maps worth reading.

### 4. Gap check — no "Role Unknown"

Every attendee needs at least a confirmed title and company before you write anything. For anyone thin (fewer than 3 meaningful results):

1. Search the people indices of social platforms for "[Name] [Company]" — the most reliable way to find someone.
2. Restrict a web search for the bare name to linkedin.com.
3. If you have their email, search "[first] [last] [email-domain]" — the email domain disambiguates common names far better than the name alone.
4. Try name variations: first + last only, full name + title if known.

If still nothing, say so honestly in the briefing: "Limited public presence — could not confirm role. Consider asking for their LinkedIn URL." Never speculate. Collect each attendee's LinkedIn URL along the way — readers want the link.

### 5. Company context

Lighter than a full company deep-dive — only what's useful in this conversation. Run in parallel: company news from the last two weeks; product launches and announcements; the about page on their own domain; funding history; and a search pairing their company with yours, which catches prior partnerships, shared investors, or competitive overlap. Fewer than 3 news results → retry without the date window.

Two craft points: wrap multi-word company names in quotes (or anchor to their domain) so "Acme Supply" doesn't drown in noise; and validate **event dates, not article dates** — a snippet saying "last year" or "back in Q3" is background context, never "recent news". If a company file already exists in your workspace, load it and run only the fresh-news search.

### 6. Value positioning (sales, partnership, board/investor only)

Read `references/value-positioning.md`. Cross-reference what you learned about their company against your own sales context — differentiators, integrations, case studies, tracked competitors — to produce value mappings, integration hooks, and a positioning paragraph calibrated to this specific meeting. Skip entirely for interview, internal, and general meetings.

### 7. Deep-read the top sources

Pick the 3–5 most informative URLs across everything found and extract the full pages. Priority order: the attendee's own posts, articles, or talks; recent company announcements relevant to the meeting; interviews or profiles of the attendee; the company team page if a title is still unconfirmed; and, when positioning is active, pages revealing their stack or challenges. Multiple attendees → person URLs beat company URLs.

### 8. Write the briefing

Follow `references/briefing-format.md` — section order, per-type adaptations, and sourcing rules. Lead with the Quick Take; most readers stop there.

### 9. Save and offer to share

Update the per-person and per-company files with structured facts (role, background, interests, communication style) and cross-references both ways, so the next prep starts warm. Save the briefing itself. Then offer to place it wherever the user works — a doc, a channel — keeping source links intact. Offer; don't push it anywhere without a yes.

## What good looks like

- The best operators mine **continuity first**: open items and preferences from prior meetings, then the attendee's own words — a direct quote from a post or talk is worth ten biography lines as a conversation hook.
- The mediocre version: generic talking points ("ask about their priorities"), a guessed title, year-old news presented as recent, and positioning advice that could apply to any company on earth.
- You know it's good when the Quick Take alone would carry the meeting; every talking point names something specific ("ask about the migration they announced last month"); every external claim carries a source URL; and gaps are stated plainly instead of papered over.

## Rules

- MUST source every factual claim about an external person or company with a URL. Claims drawn from your own sales-context notes are attributed to those notes.
- NEVER speculate about a person's role or background — write "no public information found" and suggest asking for their profile link.
- NEVER present an old event as recent news; check the event date, not the article date.
- MUST skip the Value Positioning section for interview, internal, and general external meetings.
- NEVER write a generic value mapping — every mapping pairs a specific researched finding with a specific capability of yours, or it's cut.
- NEVER distribute the briefing or any researched data outside the user's own workspace and tools without explicit approval.
