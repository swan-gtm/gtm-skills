# GTM Skills

[![skills.sh](https://skills.sh/b/swan-gtm/gtm-skills)](https://skills.sh/swan-gtm/gtm-skills)

Open, production-grade go-to-market skills for AI agents — prospecting, research, outreach, signals, pipeline, RevOps. Built and curated by [Swan](https://getswan.com), authored by the GTM community.

Every skill is a plain `SKILL.md` any agent can read — Claude Code, Cursor, Codex, Claude Desktop, and 70+ others. Use them anywhere; run them with full execution inside [Swan](https://getswan.com).

Browse the library at **[gtmskills.com](https://gtmskills.com)**.

## Install

```bash
# one skill
npx skills add swan-gtm/gtm-skills --skill reach-out

# everything from one creator
npx skills add swan-gtm/gtm-skills/skills/ido-goldberg

# the whole library (interactive picker)
npx skills add swan-gtm/gtm-skills
```

Add `-a claude-code`, `-a cursor`, `-a codex`, etc. to target a specific agent; `--list` to see what's here.

**Using Swan?** Every skill runs natively there with tools wired — hit **Use with Swan** on [gtmskills.com](https://gtmskills.com).

## Submit your skill — with your AI

You don't need to know git. Paste this to Claude, Cursor, or any capable agent:

> Fetch https://raw.githubusercontent.com/swan-gtm/gtm-skills/main/AGENTS.md and follow its submission flow. Interview me about my GTM skill, draft it in their format, and submit it.

Your agent will interview you, package your playbook in our format, validate it, and open the PR (or a submission issue if it can't use git). Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## Layout

```
skills/
  <creator>/               # a creator's space — their profile + all their skills
    author.md              # who they are
    <skill>/
      SKILL.md             # the skill — portable, tool-agnostic
      swan.md              # optional — Swan-specific execution layer
      references/          # optional — deeper material the skill routes to
      examples/            # optional — finished outcomes, shown as a slideshow on gtmskills.com
```

The folder name is the skill's permanent identity. Categories, tags, and everything else live in frontmatter.

## What makes a skill good here

Skills encode **judgment, not just steps** — what the best operator notices first, what gets overlooked, what good output looks like. They speak in GTM verbs ("check the CRM", "load the ICP"), never vendor tool names, so they work whatever your stack is. The bar is documented in [CONTRIBUTING.md](CONTRIBUTING.md); enforcement is `node tools/validate.mjs` + human review.

## License

MIT — see [LICENSE](LICENSE). Attribution stays with you: your profile travels with your skills.
