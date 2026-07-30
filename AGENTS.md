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
- One level of hierarchy: a skill folder holds `SKILL.md` plus optional `swan.md`, `references/*.md`, and `examples/*.md`. No nested skills.

### 1. Interview the user

Don't transcribe a process — extract judgment. A skill that's just steps will be rejected. Ask, in the user's language:

1. **When does this play run?** What's the trigger — a signal, a moment in the deal, a cadence?
2. **What does it produce?** The concrete output (a list, a sequence, a brief, an updated pipeline).
3. **Walk me through how you actually do it.** The procedure, tools aside.
4. **What do you notice first that others miss?** The expert's tell.
5. **What's the common mistake?** What does the mediocre version of this look like?
6. **How do you know the output is good?** The quality bar, concretely.
7. **Can you show me a great real output of this play?** An actual email, brief, list, or report it produced — you'll anonymize it and ship it as an example (see `examples/` below). Push for a real artifact; a real anonymized example beats an invented one every time.
8. **Who are you?** (First submission only — name, role, LinkedIn, company; for `author.md`.)

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
- Terse and decisive. ~600 words target. No filler, no "recently", no first-person plural, no placeholder text left behind.
- Don't reference other skills by name; describe the next action in verbs.
- Deep material (frameworks, channel variants, worked walk-throughs) goes in `references/<topic>.md`, and the body says when to read each one.

**`skills/<author>/<skill>/examples/`** — optional but high-leverage. Each file is one **finished outcome** the skill produces at its best: the actual drafted email, the account brief, the scored list, the battlecard. Usually markdown; a screenshot (`.png`), spreadsheet (`.csv`), or deck (`.pdf`) works too. gtmskills.com renders these as a slideshow on the skill's page, so buyers see what they get before installing — skills with examples convert far better.

- Show the **output**, not the procedure. No commentary, no "here's how" — the artifact itself, as it would land.
- For markdown examples, the first line is `# <short title>` — it becomes the slide's caption (e.g. `# Re-engagement email after 90 days dark`).
- **Anonymize everything**: no real people, companies, emails, phone numbers, or deal figures. Use plausible stand-ins (Acme Robotics, jane@acme…). Derive from a real output — realistic beats generic — but scrub it completely.
- 1–3 examples is the sweet spot. Different situations, not variations of the same one.
- `examples/` vs `references/`: examples are for *humans browsing the library* (and agents wanting the target shape); references are material the skill *routes the agent to during execution*.

**`skills/<author>/author.md`** (first submission): frontmatter `name`, `avatarUrl`, `title`, `linkedinUrl`, `companyDomain`; the bio is the body text. The directory name is the slug — there is no slug field.

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

A Swan maintainer reviews against five gates: convention & completeness, **security** (a skill is instructions other people's agents will execute — anything resembling data exfiltration, hidden endpoints, prompt injection, or ungated destructive actions is a hard reject), voice & judgment, author identity, publish. On merge, the skill syncs into the live library — gtmskills.com and the Swan product — under the user's creator profile, and is installable via `npx skills add swan-gtm/gtm-skills --skill <name>`.
