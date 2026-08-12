# Setup & customization checklist

Work through this once before enabling the skill.

## 1. Placeholders

- [ ] `{{WEB_RESEARCH_TOOL}}` — name the AI web-research tool or agent whose summaries feed
  your scoring, alerts, and outreach. If you use several, list them all — the rule applies
  to every one of them.
- [ ] `{{PEOPLE_SEARCH_TOOL}}` — name your people/employee search tool that can filter by
  company domain and title (e.g. LinkedIn Sales Navigator, Apollo, Lusha). Used as one of
  the accepted at-source verification methods.

## 2. Policy decisions

- [ ] **Where the gate applies.** The default (recommended) scope is: scoring/tiering, ACV
  assessments, MQL alerts, outreach copy, and CRM/account notes. If you have other surfaces
  where hiring claims land (call prep docs, QBR decks), add them explicitly.
- [ ] **Discard vs. re-verify.** When a claim fails verification, the default is to drop it
  silently. If your team prefers a re-verify queue (a human checks the careers page before
  the claim is deleted), define who owns that queue and the SLA.
- [ ] **At-source verification beyond hiring.** The wrong-domain discard rule already
  covers *everything* derived from a misattributed research answer (see invariant 4 below).
  Decide whether to additionally require at-source verification for non-hiring firmographic
  facts (funding, headcount, tech stack) even when citations look clean (recommended for
  facts that drive scoring).

## 3. Behavioral invariants (do not weaken these)

- Web-research prose alone is never a sufficient source for a hiring claim.
- Company match means name AND domain — a shared ATS tenant or job-board slug is not a match.
- Failed signals are dropped, never hedged ("they may be hiring…" is not allowed).
- Discarding is total: when citations point at the wrong domain, every fact derived from
  that answer goes, not just the hiring lines.

## 4. Wire it in

- [ ] Reference this skill from every workflow that produces scores, MQL alerts, or outreach
  containing hiring language, so it loads before hiring claims are written.
- [ ] If you run scheduled scoring or signal triggers, add a line to their instructions:
  "hiring/open-roles signals must pass hiring-signal-verification before use."
