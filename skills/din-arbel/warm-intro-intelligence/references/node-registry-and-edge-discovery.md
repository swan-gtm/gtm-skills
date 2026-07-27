---
title: Node Registry and Edge Discovery
description: Reference for the Warm intro intelligence skill.
---

# Node Registry and Edge Discovery

Sub-page of the Warm Intro Intelligence skill. Load when executing Step 4 - querying the node registry and computing edges for a target contact.

---

## Node Registry - Sources

### Your Employees
Source: the `{{TEAM_ROSTER}}` sub-page - a maintained list of all your company's employees with LinkedIn handles and full career history (past companies + years). Load it for every warm intro run. This is the primary source for the shared-employment and champion-migration checks below; it means "does anyone at the company - any department, including finance - share history with the target" works company-wide, not just for CRM owners.

**Building `{{TEAM_ROSTER}}` (one-time setup, then maintenance):**
- Run a LinkedIn company-employees scrape (e.g. the harvestapi/linkedin-company-employees Apify actor) on your company's LinkedIn slug, in full mode, to pull every employee with their career history.
- Format per line: **Name** - title (country) - `linkedin-handle` - past: Company (years); Company (years); ...
- LinkedIn handle: prefix with https://www.linkedin.com/in/ to get the full URL.
- Record the pull date and headcount at pull on the roster page.
- Refresh every ~90 days (employment data expiry window) or when headcount materially changes: re-run the same scrape and regenerate the roster.

If the roster is older than ~90 days or headcount has materially changed, refresh it before running the play.

For each employee, check in priority order:

1. **Shared employment (from roster)** - compare the employee's past companies against (a) the target account itself, and (b) the target contact's employment history. An employee who previously worked AT the target company, or ALONGSIDE the target contact at a prior company (company name overlap with date overlap), is a warm bridge. Seniority proximity: any overlap at a company under 100 employees counts; VP+ level at larger companies counts.

2. **CRM activity** - search engagement records (meetings, calls, email threads) where the employee is the owner or sender AND the prospect company or target contact appears as the associated company or contact. For each match: record engagement type, date, and whether the prospect contact replied (for emails).

3. **LinkedIn messages** - if the employee has LinkedIn connected as a personal tool, check their chat history for threads involving the target contact's name or email address.

4. **LinkedIn 1st-degree connections** - if Sales Nav is connected for this employee, check whether the target contact is a 1st-degree connection.

### Customers
Source: `{{CUSTOMER_LIST}}` (your active-customers list - source of truth). Note: if this is a COMPANY-level list, it returns client companies, not people. To get customer contacts, pull the CRM contacts associated with each client company.

Sourcing for edge discovery and the Champion Migration pool:
1. Pull the client companies from `{{CUSTOMER_LIST}}`.
2. For each client company, pull its associated CRM contacts (name, title, email, LinkedIn URL). This is a free CRM read.
3. Filter to genuine relationships only (the Known Contacts pool rule below): keep contacts with a logged meeting, logged call, or a replied email thread. Drop contacts with no engagement. This keeps the pool to people your company actually knows and avoids enriching hundreds of dead records.

For each qualified customer contact, check:
1. **LinkedIn 1st-degree connection** to the target contact - if Sales Nav is available.
2. **Shared employment history** - compare employment histories for company name overlap and date overlap using the same seniority proximity rule above.
3. **CRM notes** - search notes on the customer company record for any explicit mention of the prospect company name.
4. **Event tags** - check account memory for both the customer contact and prospect contact appearing in the same event.

### Partners
Source: `{{PARTNER_LIST}}` - your partner records in the CRM.

Gotcha (HubSpot custom objects): if your partners live in a custom object and your partner list is a saved view over that object, the standard list-members tool CANNOT read it - it returns "unsupported list object type." Read the custom object directly instead.

Read partner records via a direct HubSpot API call using your own private-app token, loaded from your credential store - never paste a literal token into this skill or any code committed anywhere: `GET /crm/v3/objects/{{HUBSPOT_PARTNERS_OBJECT_ID}}` with `properties=first_name,last_name,full_name,email_address,partner_status,partner_tier,partner_type` and `associations=companies,contacts`. Each record is a person with an email and associations to companies (`0-2`) and contacts (`0-1`).

Filter out noise before use: personal free-mail addresses with no company/contact association, and any record whose email domain is `{{COMPANY_DOMAIN}}` (those are your own employees, not external partners). Keep records that have at least one company or contact association, or a business email.

For each qualified partner contact, apply the same discovery checks as Customers above (LinkedIn 1st-degree, shared employment, notes, event tags), and include them in the Champion Migration relationship pool.

### Investors
Source: the `{{INVESTOR_REGISTRY}}` sub-page - the maintained list of your company's investor firms. Load it for every warm intro run. Supplement with Crunchbase for the prospect's investor list.

**Building `{{INVESTOR_REGISTRY}}` (you maintain this):**
- List every firm that has invested in your company. For each firm, record: firm name, individual partner(s) tied to your company, board seat (if any), and their role in your company.
- **Individual partners are the highest-value field.** A firm-level match is a weaker signal; a named partner with a confirmed edge to the target is actionable. Populate partner names from funding announcements, Crunchbase, and LinkedIn - and when a partner name is added, also capture their LinkedIn URL so the person-level checks (Sales Nav 1st-degree, shared employment) can run.
- Refresh the firm list whenever your company raises a new round or adds investors.
- Watch for firm name variations when matching against Crunchbase prospect data: short names vs. full legal names, abbreviations, and "Capital"/"Partners"/"Ventures" suffixes (e.g. "Greenfield" vs "Greenfield Partners", "DCG" vs "Digital Currency Group"). Match on the variation set, not the exact string.

Two checks:
1. **Shared portfolio** - does any firm in the registry also appear as an investor in the prospect company? (Crunchbase lookup on the prospect.) A confirmed shared investor is a **Moderate** edge - the overlap is a verifiable fact and VCs routinely facilitate portfolio-company intros, even though the specific partner relationship isn't yet identified.
2. **Investor partner -> prospect** - for registry firms with a named individual partner recorded, check that person's LinkedIn employment history and 1st-degree connection (Sales Nav) against the target contact. A confirmed person-to-person signal keeps the path at **Moderate** with stronger evidence, and can reach **Verified** if a direct logged interaction exists.

Note: if your registry is currently firm-level only, a confirmed shared investor is Moderate. Individual partner names strengthen the evidence within the Moderate tier.

### Advisors and Board Members
Source: Scrape `{{COMPANY_DOMAIN}}` (your website) for named advisors and board members. Enrich each with LinkedIn URL and current role.

For each advisor or board member, check:
1. **LinkedIn 1st-degree connection** to the target contact - if Sales Nav available.
2. **Shared employment history** with the target contact.
3. **Account memory** for any pre-cached relationship data or intake flags.

### Call Transcripts
Source: your call-transcript tool (e.g. Fireflies, Gong, Granola), connected at the org level.

Search transcripts for any call where the prospect company name, target contact names, or known company aliases are mentioned. Look specifically for:
- A rep saying "I know [Name] at [Company]" or "I worked with [Name]" or "I have a contact at [Company]"
- Any mention of the target contact's name in a call involving one of your reps
- Discussion of a personal relationship with the prospect or someone at the prospect company

For each matching transcript:
- Record who was on the call (rep name), the date, and the exact quote or context
- Treat as a Verified edge if the rep explicitly states a personal relationship with the named contact
- Treat as Moderate if the rep mentions knowing someone at the company without naming the specific target contact
- Treat as Inferred if the prospect company is merely discussed with no relationship claim

Transcripts are checked for every warm intro request regardless of other signals. They often surface relationships that were never logged in the CRM.

### Warm Relationship Intake Flags
Source: account memory for the prospect company and any org-level intake memory.

Check for stored intake flags where:
- The bridge is one of your employees, a customer contact, partner contact, investor, or advisor.
- The external contact is the target contact or works at the prospect company in a relevant role.

Return any matching flags with stored confidence tier, intro_willingness value, context, and date logged.

### Known Contacts (Relationship Pool) - Champion Migration

This node type flips the core question. Instead of asking "does a bridge share history with the target contact?", it asks "does someone your company already has a genuine relationship with now work at the target account?" When there is a hit, the person you know IS the warm contact - a 1-hop path.

**Governing test for pool membership:** if surfaced as a champion-migration candidate, the assigned rep should reasonably recognize the person as someone your company actually knows. Use this test to decide any edge case the inclusion list does not cover.

**Build the Relationship Pool (include):**
- CRM contacts with a logged meeting (any company).
- CRM contacts with a logged call (any company).
- CRM contacts on an email thread with at least one reply from that contact (any company).
- Current customer contacts - associated contacts of companies on `{{CUSTOMER_LIST}}`, filtered to those with real engagement per the Customers section above.
- Former customer contacts - contacts previously associated with a company that has left `{{CUSTOMER_LIST}}`, or on churned/Closed Lost records tied to a former customer.
- Current partner contacts - qualified records from `{{PARTNER_LIST}}`, read per the Partners section above.
- Former partner contacts - partner records no longer active / previously associated with a departed partner company.
- Closed Lost deal champions - the primary/champion contact on a Closed Lost deal.
- (Future) manually confirmed warm relationships from intake flags.

**Exclude from the pool:**
- One-way outreach only (no reply logged).
- Contacts with no engagement of any kind.
- Contacts that exist in the CRM but were never interacted with.
- LinkedIn connections without any real logged interaction.
- Your own employees appearing in the partners object (`{{COMPANY_DOMAIN}}` email domain).

**Efficiency rule (controls cost):** build the pool from cheap CRM reads and filter to genuinely-engaged contacts FIRST. Only then enrich current-employer for the filtered pool. Never enrich every contact in the CRM. Even where contact enrichment is cheap, the filter keeps the pool meaningful and the run fast.

**Primary check - Champion Migration:**
For each pool member, compare their CURRENT employer against the target account. A match means a person your company genuinely knows now works at the target. This is the highest-value output of the play. Record: the pool member's name, current title at the target, prior company where the relationship was formed, the rep who owned the original relationship (meeting owner / call owner / email sender / deal owner), and the last interaction date.

**Secondary check - Team Migration (detect and flag only):**
If two or more pool members now work at the target account, flag it as a team-migration cluster. This is informational awareness for the rep ("we already know N people here") only. It does NOT influence edge confidence, path confidence, or ranking in V1. If 2+ members also moved from the same prior company into the target, note that prior company in the cluster flag.

**Bridge attribution:** always name the specific rep who owned the original relationship, so the output card names a concrete connector rather than just the company.

**Cost gate:** run this node ONLY for qualified/target accounts at query time. Do not run for accounts that are not qualified targets.

Each champion-migration hit becomes its own candidate 1-hop path (rep -> known contact now at target) and feeds the standard Step 5/6 scoring and ranking. Champion-migration paths receive no separate ranking logic - they compete on the existing axes (path confidence, recency, persona priority, hops).

---

## Edge Computation

For each potential path found, compute edges before assigning confidence. Do not assign confidence from a single weak signal when stronger signals are available from another source - check all available sources for a given edge first.

### Path Types

**1-hop path:** Bridge directly knows target contact.
Example: [Founding AE] -> Prospect CFO

**2-hop path:** Bridge knows an intermediary who knows the target contact.
Example: [Founding AE] -> Customer Contact -> Prospect VP of Partnerships

Prefer 1-hop paths over 2-hop paths when confidence is equal.

### Per-Edge Data to Collect

For every edge found, record:
- Source system: CRM / LinkedIn / Memory / Public / Intake
- Last verified date: date of the most recent logged interaction or verification
- Expiry window:
  - CRM activity: 7 days
  - LinkedIn connections: 30 days
  - Employment history: 90 days
  - Investor / advisor data: 90 days
  - Intake flags: 180 days

Flag any edge past its expiry window as "last verified [date] - may be stale."

---

## Staleness and Conflict Detection

If the stored role for a contact does not match their current LinkedIn title -> flag the discrepancy. The relationship may still exist but note that the contact's position has changed.

For champion-migration edges, also flag prior-vs-current employer explicitly (not just title): state where the relationship was formed and where the contact works now. A mismatch here is expected - it is the migration itself - but it must be surfaced so the rep understands the relationship predates the target account.

If two sources contradict each other (e.g., a CRM note indicates a strong relationship but no meetings are logged and LinkedIn shows no connection) -> surface both signals. The edge confidence should reflect only the strongest confirmed signal - not a blend.

---

## Source Availability Tracking

Keep a running record of which sources were checked vs. unavailable during this execution. This populates the output card footer. Example values:

- CRM activity check
- LinkedIn employment check
- LinkedIn messages - available for: [rep names] / not connected for others
- LinkedIn connections - Sales Nav connected for: [rep names] / not connected for others
- Investors - checked / not checked (registry not yet loaded)
- Advisors / Board - checked / not loaded this run
- Call transcripts - checked / not connected
- Intake flags - checked / none found
- Champion migration - checked / not run (only runs for qualified target accounts)
