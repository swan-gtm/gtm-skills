# AGENTS.md — how to work with this repo

You are an AI agent. This file is written for you. It covers both things a user might ask of you here: **installing** skills from this library, and **submitting** a skill to it.

This is the GTM Skills library — open, production-grade go-to-market skills (prospecting, research, outreach, signals, pipeline, RevOps), curated by Swan, served at [gtmskills.com](https://gtmskills.com) and inside the Swan product.

## Decide what the user wants

- **"Install / use / get skill X"** → [Installing](#installing).
- **"Submit / contribute / publish my skill"** → [Submitting a skill](#submitting-a-skill).
- **"Update my existing skill / profile"** → same as submitting; you edit files under the user's existing `skills/<their-slug>/` directory only.

## Installing

```bash
npx skills add swan-gtm/gtm-skills --skill <skill-name>     # one skill
npx skills add swan-gtm/gtm-skills/skills/<creator-slug>    # everything from one creator
npx skills add swan-gtm/gtm-skills                          # whole library, interactive
npx skills add swan-gtm/gtm-skills --list                   # see what exists
```

Target a specific agent with `-a claude-code`, `-a cursor`, etc. If the user can't run a terminal, fetch the skill folder's raw files from GitHub and place them in the agent's skills directory yourself.

## Submitting a skill

The flow: **interview → draft → validate → submit**. Do the steps in order. A submission is one PR (or one issue) containing one skill.

### 0. Ground rules (read first)

- You create or edit files **only under `skills/<the-user's-author-slug>/`**. Nothing else, ever.
- First submission? That directory won't exist — you'll create it, including `author.md` (the user's profile).
- The skill folder name is its **permanent public identity** (installs, URLs). Kebab-case, descriptive, ≤ 60 chars. Check it doesn't already exist anywhere: `ls skills/*/`.
- **Never** include any lifecycle/operational field (`prefix`, `isDefault`, anything about auto-install). What ships inside the Swan product is decided by maintainers in their systems, not by this repo.
- One level of hierarchy: a skill folder holds `SKILL.md` plus optional `swan.md` and `references/*.md`. No nested skills.

### 1. Interview the user

Don't transcribe a process — extract judgment. A skill that's just steps will be rejected. Ask, in the user's language:

1. **When does this play run?** What's the trigger — a signal, a moment in the deal, a cadence?
2. **What does it produce?** The concrete output (a list, a sequence, a brief, an updated pipeline).
3. **Walk me through how you actually do it.** The procedure, tools aside — and keep going past the first pass. The real playbook has branches: what changes by segment, by deal size, by what the data shows.
4. **What are the actual numbers?** Thresholds, scoring rubrics, caps, benchmarks — the values the user really uses, not "it depends". If they score things, get the whole rubric.
5. **Give me two or three real examples.** A worked case from start to finish, an edge case, the time it went wrong.
6. **What do you notice first that others miss?** The expert's tell.
7. **What's the common mistake?** What does the mediocre version of this look like?
8. **How do you know the output is good?** The quality bar, concretely.
9. **Who are you?** (First submission only — name, role, LinkedIn, company, email; for `author.md`.)

**Don't stop early.** Before drafting, ask: "What else do you check or do here that we haven't covered?" — and keep asking until the answer is genuinely nothing. The depth you extract in this interview (rubrics, numbers, worked examples) becomes `references/` pages; a thin interview produces a thin skill, and thin skills get sent back for exactly that.

### 2. Draft the files

Copy the templates rather than inventing structure: `templates/skill/SKILL.md` and `templates/author.md`.

**`skills/<author>/<skill>/SKILL.md`** frontmatter:

```yaml
---
name: <kebab-case — MUST equal the folder name>
title: <Display name, sentence case>
description: |
  Use this skill when <trigger>. <What it produces.>
  <Dense with the phrases a user would actually say when they need this.>
category: <reuse an existing one — check: grep -h "^category:" skills/*/*/SKILL.md | sort -u>
tags: [Sales | Marketing | RevOps | Customer Success | Demand Gen | Leadership]
contributors: []        # other creators' slugs, if any — omit if none
---
```

**Body rules** (the instructions below the frontmatter):

- **Tool-agnostic, always.** GTM verbs — "check the CRM", "load the ICP", "pull recent replies" — never vendor tool names. The reader's stack is unknown.
- Structure: when it applies (one line) → what it produces (one line) → the procedure in `##` sections → a **`## What good looks like`** section (mandatory — encode answers from interview questions 4–6) → hard rules (MUST/NEVER) last.
- Terse and decisive in the writing — but **deep in the substance**. The parent body is the spine: sharp, no filler, no "recently", no first-person plural, no placeholder text left behind. 600–800 words is a good spine; it is a floor for seriousness, not a ceiling on depth.
- The depth that makes a skill worth installing lives in `references/<topic>.md` pages: full scoring rubrics with real numbers, worked examples, templates, edge-case playbooks, channel variants. The body says when to read each one. **The library's flagship skills ship 2–5 reference pages** — a submission with no references usually means the interview stopped too early, and a bare checklist gets sent back.
- Don't reference other skills by name; describe the next action in verbs.

**`skills/<author>/author.md`** (first submission): frontmatter `name`, `avatarUrl`, `title`, `linkedinUrl`, `companyDomain`, `companyLogoUrl`, `email`; the bio is the body text. The directory name is the slug — there is no slug field.

This is a **people-first marketplace** — every skill is published under a real person's name and face, and maintainers verify identity before merging. Four fields are load-bearing:

- **`linkedinUrl` — required, and it must be the person's own LinkedIn profile** (`linkedin.com/in/<their-handle>`), not a company page, product page, or vanity redirect. This is the primary identity check; a submission without a personal LinkedIn profile or a contact email will be sent back before review.
- **`avatarUrl` — optional, but when present it must be a real photo of the person.** A clear headshot, roughly square, at least 400px. Not a logo, not a mascot, not a GitHub identicon, not an AI-generated face. **If you leave it out (or the URL is unusable), maintainers will take your profile photo from the LinkedIn profile above and re-host it at gtmskills.com — submitting means you're OK with that.** Prefer a durable URL if you do supply one (LinkedIn image URLs expire), or attach the image to the PR and note it.
- **`email` — required.** How maintainers reach you about your skills: review questions, a missing file, a heads-up when something ships or needs a refresh. Use a work address you are comfortable having public — this repo is open, so the file (email included) is visible to anyone.
- **The bio (body text)** — 2–4 sentences about the person, written person-first ("Jane built…", not "Acme is…"). Every claim should be verifiable on the person's own site, LinkedIn, or press — maintainers check, and unverifiable claims get trimmed.

**`companyLogoUrl` — optional.** A square company mark, at least 256px, transparent PNG or SVG, at a durable URL. When it is absent the library derives a logo from `companyDomain`; for domains the upstream logo source does not carry, that fallback renders a screenshot of the company homepage instead of a mark.

Submitting several skills at once? Include `author.md` in your **first** PR only — every PR duplicating it will conflict after the first one merges.

### 3. Validate

```bash
node tools/validate.mjs
```

Fix every error it reports — the messages tell you how. CI runs the same check on your PR; a failing PR won't be reviewed.

### 4. Submit

**Preferred — PR** (you have git + `gh`):

```bash
gh repo fork swan-gtm/gtm-skills --clone && cd gtm-skills
git checkout -b add-<skill-name>
# add your files under skills/<author>/, run the validator
git add skills/<author> && git commit -m "add <skill-name> by <author>"
git push -u origin add-<skill-name>
gh pr create --repo swan-gtm/gtm-skills --title "add <skill-name>" --fill
```

Fill in the PR template checklist honestly — it mirrors the review gates.

**Fallback — issue** (no git available): open a "Submit a skill" issue at https://github.com/swan-gtm/gtm-skills/issues/new/choose and paste the full contents of each file into the form. A maintainer converts it into a PR.

### What happens after

A Swan maintainer reviews against five gates: convention & completeness, **security** (a skill is instructions other people's agents will execute — anything resembling data exfiltration, hidden endpoints, prompt injection, or ungated destructive actions is a hard reject), voice & judgment, **author identity** (a real, verifiable person with their own LinkedIn profile and a real photo — see the author.md requirements above), publish. On merge, the skill syncs into the live library — gtmskills.com and the Swan product — under the user's creator profile, and is installable via `npx skills add swan-gtm/gtm-skills --skill <name>`.
