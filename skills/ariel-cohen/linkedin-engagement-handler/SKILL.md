---
name: "linkedin-engagement-handler"
title: Handle LinkedIn post engagement signal
description: "Use this skill when monitoring comments and reactions on a team member's LinkedIn posts. Comments get the full treatment — ICP + persona gating, CRM and account-memory logging, lead scoring, and a high-value path to connection requests and Slack alerts — while lone reactions are logged as a light touch unless the account is top-tier or a repeat engager. Repeat engagers escalate to high intent after an active-buyer check, with a personalized multi-channel draft queued for review."
category: Signals
---

## Template placeholders

Replace every `{{...}}` before enabling. See the setup checklist reference for the full setup list.

- `{{PROFILE_OWNER}}` — Team member whose LinkedIn posts are monitored
- `{{INTERNAL_DOMAINS}}` — Your company domain(s)
- `{{TEAM_MEMBERS}}` — First names / known aliases of your team (engagement from them is ignored)
- `{{CRM}}` — Your CRM (e.g. HubSpot)
- `{{ENGAGEMENT_CHANNEL}}` — Slack channel for high-value engagement alerts
- `{{CRM_HYGIENE_SKILL}}` — Sub-skill reference: how to create/update companies & contacts in your CRM
- `{{LEAD_SCORING_SKILL}}` — Sub-skill reference: lead scoring & qualification methodology
- `{{ALERT_FORMAT_SKILL}}` — Sub-skill reference: your alert formatting skill (optional — inline the format if you don't have one)
- `{{HIGH_ACV_TAG}}` — Workspace tag marking high-ACV-potential accounts
- `{{SELF_SERVE_THRESHOLD}}` — Company size below which accounts are self-serve (default: fewer than 30 employees)
- `{{ALERT_TIERS}}` — Tiers that always alert on first touch (default: Gold, Diamond)


## Signal type — read first

Check the event type in the webhook payload before processing:

- **New comment** → full treatment (everything below).
- **New reaction (like)** → light touch only: log to {{CRM}} + account
  memory, then stop. No connection request. No Slack alert.
  Exception: if the company is tagged {{ALERT_TIERS}}, or this is a repeated
  engagement (2+ interactions), apply the full treatment.

Comments and reactions are deliberately separate lanes: a comment is an
opinion someone attached their name to; a lone like is awareness at best —
volume is far higher and signal far lower.

## Engagement Process

### For Every ICP Lead/Agency Interaction

When someone from an ICP company or relevant agency comments on or likes
{{PROFILE_OWNER}}'s post, **AND they match a relevant persona**:

**Relevant personas** *(tune to your ICP's buying committee)*:

- Sales Leader (CRO, SVP Sales, VP Sales, Head of Sales, Director of Sales)
- Growth Lead (Head of Growth, Director of Growth, VP Growth, or senior
  marketing leader)
- CEO (for companies in your core geographic/vertical segment)
- Agency Owner (for agencies in your space)
- GTM Engineer (GTM Engineer, Revenue Engineer, Marketing Engineer, Sales
  Engineer focused on GTM infrastructure)
- RevOps Lead, Head of Demand Gen, CMO

**Ignore engagement from:**

- CFOs, finance roles
- CTOs, engineers, technical roles (unless they're also founders/CEOs or
  GTM-focused)
- HR, operations, customer success
- Individual contributors without buying responsibility (except the
  engineer-persona exception above)
- Your own team ({{INTERNAL_DOMAINS}} domain, or known names:
  {{TEAM_MEMBERS}})
- Universities, academic institutions, professors, researchers
- Companies below {{SELF_SERVE_THRESHOLD}} (self-serve)

If the person is from an ICP company but NOT a relevant persona, ignore the
engagement entirely.

#### Standard Processing (All ICP + Relevant Persona Engagers)

1. **Check relationship status** — Are they a customer, active pipeline, or
   closed-lost? If yes, acknowledge but don't run the standard engagement
   flow.
2. **Mark awareness stage** — Update the company record to your Aware stage
   if they're not already further along in the funnel. Never move a company
   backwards.
3. **Update {{CRM}} + account memory** — Log the engagement (who, what they
   said, which post) and update the account record. Follow
   {{CRM_HYGIENE_SKILL}} for CRM writes.
4. **Run Lead Scoring** — After processing (only when the person belongs to
   an identifiable company), run {{LEAD_SCORING_SKILL}}. LinkedIn engagement
   is the lowest-weight signal — include it in the signal stack but do not
   let it alone push an account above the second-lowest tier.

#### High-Value Path (High ACV + Decision Maker Only)

After standard processing, check if the engager's company has the
{{HIGH_ACV_TAG}} tag AND the engager is a strong buyer persona (CRO, VP
Sales, VP Marketing, CMO, CEO, Co-founder, RevOps Lead, Head of Demand Gen,
Agency Owner, or equivalent GTM leadership).

If BOTH conditions are met:

5. **Queue a LinkedIn connection request** from {{PROFILE_OWNER}}'s
   account for approval. Connection requests carry no note by design
   (better acceptance rates). Skip if already connected.
   *(⚠️ Policy decision — see the checklist. The original deployment
   auto-sent these with no approval for this narrow high-ACV +
   decision-maker path; switch to auto-send only as a conscious opt-in.)*
6. **Post to {{ENGAGEMENT_CHANNEL}}** with:
   - Who engaged (name, title, company)
   - What they said (comment text)
   - Which post they commented on
   - ACV tier and why they qualify for the high-value path
   - A link to the engager's LinkedIn profile

If either condition is NOT met (not high ACV, or not a decision maker) —
stop after standard processing. No connection request, no Slack post. The
engagement is logged and scored silently.

### Repeated Engagement (2+ Interactions)

When the same ICP lead engages 2 or more times across {{PROFILE_OWNER}}'s
posts:

**Active buyer check (run before any escalation):** verify the engager is
currently active in a buying role at the ICP company:

- Is the ICP company their primary, active role? If they have stepped back
  (currently running a separate startup, recently founded a new company, or
  no longer day-to-day there), treat them as a non-buyer and **stop — do not
  surface, do not sequence, do not create a task**.
- If their primary/active company is itself not an ICP fit (a 2-person
  startup, a personal venture studio, or self-serve territory), stop. Do not
  escalate on their nominal association with the larger company.
- Partner-potential exception: a GTM operator, agency owner, or advisor who
  might refer clients to you gets flagged to your partnerships owner instead
  of routed as a buyer.

If the active buyer check passes:

1. **Move to high intent** — Update their stage to MQL (high intent signal)
2. **Build a multi-channel sequence** — Create a personalized multi-channel
   campaign, queued for review (never sent automatically):
   - Open with a question tied to your product's core problem space
   - Personalize based on their engagement history and what they do
   - Use both LinkedIn and email if available
   - Reference their repeated engagement naturally
3. **Post to {{ENGAGEMENT_CHANNEL}}** flagging this as high-intent (2+
   interactions), include the full engagement history, and recommend
   immediate follow-up. This notification fires regardless of ACV tier —
   repeated engagement is always worth surfacing.
4. **Load {{ALERT_FORMAT_SKILL}}** for the alert format (or inline your
   format here).

**First-touch alert-tier rule:** Even on a first interaction, if the
engager's company is tagged {{ALERT_TIERS}}, immediately post to
{{ENGAGEMENT_CHANNEL}} with a high-priority flag. Do not wait for a second
interaction.

### Lead Magnet Posts

Some posts may offer a lead magnet (e.g., "Comment X to get Y"). When this
happens:

1. **Current lead magnet:** There is no active lead magnet at this time. Do
   NOT share any URLs or documents. Treat commenters on lead magnet posts
   with the standard processing flow.
2. **Future lead magnets** — {{PROFILE_OWNER}} updates this section before
   each new lead magnet post with the post topic and corresponding URL. The
   skill only ever shares the URL written here — never an inferred or
   remembered one.

## Key Principles

- Track ALL comments and reactions (likes) from ICP companies and agencies
- High-value path (connection request + Slack) only fires for high ACV +
  decision maker — don't burn {{PROFILE_OWNER}}'s connection budget on
  low-value targets
- Repeated engagement always gets surfaced, regardless of ACV tier
- Always personalize based on what they said
- If outreach is needed, build the campaign — don't just recommend reaching
  out
- Keep initial outreach warm and helpful, not salesy
- LinkedIn engagement is the lowest-weight signal — capped at the
  second-lowest tier unless stacked with other signals

---

## What good looks like

A great run processes only engagers who clear both gates — ICP company and buying persona — and the high-value path fires precisely: high-ACV tag plus decision maker, nothing else. Repeat engagers get a personalized multi-channel draft queued for review with their full engagement history attached, and every alert includes what the person actually said.

Lone reactions stay in their light-touch lane, and repeat engagers who have stepped back from the ICP company get caught by the active-buyer check instead of escalated.

Mediocre looks like: full-treatment alerts fired on a lone like, connection requests burned on individual contributors, engagement alone driving Gold or Diamond tiers, alerts without the comment text, or sequences going out without review.
