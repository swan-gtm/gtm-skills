---
name: "track-contact-job-changes"
title: Track contact job changes
description: "Use this skill when you need to find which contacts in the CRM have changed jobs and act on it — a quarterly database refresh, a \"did anyone move?\" sweep, a churn-risk or new-champion check, or a job-change signal firing on a known contact. It reads each contact's current role from their work history, compares it to what the CRM believes, and routes the movers: still-there contacts get refreshed, confirmed leavers get their old and new roles separated, movers to non-fit companies get flagged and opted out, and movers to net-new fit companies get the company enriched, tiered, and optionally created as an account. Every CRM write is proposed for approval first — the database is never polluted and no contact is silently overwritten. Also known as: job change detection, contact data refresh, champion tracking, buyer-moved alerts."
category: Signals
---

One line: run this when you want the CRM's contacts to reflect where those people actually work now,
and to catch champions who moved to a new account. It produces a reviewed batch of CRM changes, never a
silent rewrite.

**Golden rule: propose, then confirm.** Collect every proposed change and show it as one table before
touching the CRM. And **never act on the wrong person** — if the enriched identity doesn't match the
contact, it goes to "can't confirm", not to a write.

## Setup (once)

Before the first run, capture the operator's configuration and save it — see
[references/setup-checklist.md](references/setup-checklist.md). It records: the CRM and whether writes
are allowed; the **match keys** for a person (record id, email, LinkedIn URL) and a **company** (domain,
LinkedIn company URL, name); the four data sources the play needs (a LinkedIn-URL finder, a work-history
source that returns current + past roles, an email lookup, a company-enrichment source); the **tier
rules** that define a create-worthy account; the **opt-out rules** that mark a move as a dead end; and
the CRM field names to write. On a later run, load the saved config; if none exists, run setup first.

## The play (per contact)

1. **Confirm the contact is in the CRM** using the person match keys, and read their current company,
   title, and LinkedIn URL.
2. **Have a LinkedIn URL?** If not, look one up from name + company and **validate the found profile's
   name against the contact** before trusting it. Retry once. Still nothing → mark *can't confirm* and stop.
3. **Pull current + past roles** from the work-history source. Validate the returned person's name against
   the contact. On a name mismatch → the stored URL is likely wrong → mark *can't confirm* (re-find), stop.
4. **Compare the current employer to the CRM company** using the matching rules in
   [references/matching.md](references/matching.md) — domain and LinkedIn-page agreement decide it; a name
   alone never does. Three outcomes:
   - **Still there** → propose refreshing title/tenure if they changed; otherwise mark verified. Done.
   - **Can't confirm** (weak or conflicting signals) → propose re-finding the URL or flag for review. Never guess. Done.
   - **Confirmed left** → separate old (the CRM company) from new (the current employer), and continue.
5. **Is the new company already in the CRM?** Match it with the same rules.
   - **Yes** → apply the opt-out rules. If the new company is a customer, competitor, or otherwise
     disqualifying → **flag & opt out** (stop outreach, record the move). Otherwise → **update the
     contact** to the new company/title and re-associate to the existing account.
   - **No** → **enrich the company**, then **tier it** against the rules in
     [references/tiering.md](references/tiering.md). A **fit** account → propose **creating the account**,
     then update the contact onto it. A **non-fit** account → **skip & flag** (don't create it), but still
     update the contact's new company/title so the record is honest. Both paths end at an updated contact.
6. **Approve & apply.** Present the batch as one table — contact, old → new company, outcome, fields to
   write, and the evidence/confidence behind it. Apply only what's approved. If writes are disabled,
   export the table instead of writing.

## What good looks like

A great run leaves every still-employed contact quietly verified, every real mover refreshed to their
actual new role, and every champion who landed at a net-new fit account surfaced as a new opportunity —
with a one-glance approval table the operator can trust and audit. Confidence is earned from domains and
LinkedIn pages, not from fuzzy name overlap; acquisitions and rebrands are treated as "same company" only
when the hard identifiers agree.

The mediocre version pollutes the database: it overwrites a contact because two company names looked
similar, acts on a same-name stranger's profile, creates duplicate accounts for a company already in the
CRM under a different name, or auto-writes a pile of changes no human ever saw. The tell of the expert:
they trust "confirmed left" only when the new employer is hard-identified, and they would rather leave a
record as "can't confirm" than write a confident lie.

## Rules

- MUST propose every CRM create/update in a single review step and apply only what a human approves.
- MUST validate the enriched person's name against the contact before using any profile; on mismatch, route to "can't confirm".
- MUST decide company sameness from domain / LinkedIn-page agreement first; a name-only match is never sufficient to write.
- MUST keep the old company as previous-role history when a contact is updated — never erase where they came from.
- NEVER create a new account for a company that already exists in the CRM under a different name or domain.
- NEVER opt a contact out, or overwrite their role, on low-confidence or single-signal evidence.
- NEVER continue when writes are disabled — export the proposed changes instead.
