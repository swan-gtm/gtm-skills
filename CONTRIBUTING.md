# Contributing

The easiest way to contribute is to **let your AI agent do it**: paste the prompt from the [README](README.md#submit-your-skill--with-your-ai) into Claude, Cursor, or any capable agent. It will interview you, draft your skill in our format, validate it, and submit. Everything below also works by hand.

## The model

- `skills/<your-slug>/` is your space — your profile (`author.md`) plus every skill you've authored. A contribution only ever touches your own directory.
- The skill folder name is its permanent public identity (install commands, URLs). Globally unique, kebab-case, never renamed after merge.
- **This repo is content only.** Nothing here controls what Swan auto-installs or injects — those are operational decisions made by maintainers in Swan's systems. Frontmatter carrying lifecycle fields (`prefix`, `isDefault`, …) fails validation.
- Full file-format spec: [AGENTS.md](AGENTS.md). Templates: [templates/](templates/).

## Submitting

1. Fork, branch, add your files under `skills/<your-slug>/` (first time: include `author.md` — see `templates/author.md`).
2. Run `node tools/validate.mjs` and fix everything it reports.
3. Open a PR — one skill per PR — and fill in the checklist.

No git? Open a ["Submit a skill" issue](https://github.com/swan-gtm/gtm-skills/issues/new/choose) and paste your files into the form; a maintainer converts it to a PR crediting you.

## The quality bar

- **Judgment, not steps.** A skill captures what the best operator notices first, the trap the average one falls into, and what good output looks like. Every skill has a `## What good looks like` section. A bare checklist gets sent back.
- **Tool-agnostic.** GTM verbs ("check the CRM", "load the ICP") — never vendor tool names. Readers run HubSpot, Salesforce, Attio, spreadsheets, or nothing.
- **Dense description.** Leads with "Use this skill when…" — it's what an agent reads to decide when to fire your skill.
- **Compact.** ~600 words of instructions; past ~800, move depth into `references/`.
- **Show, don't tell.** Include 1–3 fully anonymized finished outcomes in `examples/` — they render as a slideshow on your skill's gtmskills.com page and are the single best predictor of installs.
- **No rot.** No dates, no "recently", no UI-specific references.

## Review — the five gates

Every submission goes through, in order: **1. Convention** (validator + spec; we fix small things rather than bounce), **2. Security** (see below — hard gate), **3. Voice & judgment** (we may edit for house voice; substance stays yours), **4. Author identity** (real person, real profile), **5. Publish** (merge → syncs to gtmskills.com and the Swan product under your creator profile).

## Security — hard rejects

A skill is instructions that other people's agents will execute against their live CRM, inbox, and company data. We read every file and reject outright:

- sending data to any endpoint, inbox, or webhook the reader doesn't own
- hardcoded secrets, tokens, or third-party URLs that receive data
- prompt-injection patterns ("ignore previous instructions", disabling approval gates)
- destructive or bulk actions without an explicit human approval step
- asking end users for credentials

Report a suspicious published skill: see [SECURITY.md](SECURITY.md).

## License & attribution

Contributions are MIT-licensed ([LICENSE](LICENSE)). Attribution is structural — your `author.md` travels with your skills, and the library and gtmskills.com credit you everywhere your skills appear.
