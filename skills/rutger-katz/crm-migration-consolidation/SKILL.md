---
name: "crm-migration-consolidation"
title: CRM migration and consolidation
description: "CRM migration, instance consolidation, and post-merger integration for B2B revenue teams; system-of-record design; deduplication and identity resolution; data harmonisation before cutover; historical data strategy; adoption and change management; PE portfolio integration playbooks. Use when the user describes merging two CRM instances, consolidating after acquisition, post-merger CRM integration, handling dual CRM coexistence, managing CRM data quality before migration, defining which system of record wins for which object, planning a CRM cutover, multi-entity or multi-currency CRM challenges, or running a 100-day integration plan with CRM elements. Trigger phrases: \"merge our CRMs\", \"consolidate two HubSpot portals\", \"HubSpot and Salesforce together\", \"post-merger CRM\", \"CRM integration plan\", \"deduplication before migration\", \"which CRM wins\", \"cutover\", \"consolidation strategy\", or \"100-day CRM plan\". BOUNDARY: Use this skill for CRM architecture decisions, data strategy, and integration planning. For detailed Salesforce configuration, see revops-salesforce. For detailed HubSpot configuration, see revops-hubspot. For handoff design across the revenue bow tie, see revops-handoffs. For broader PMI strategy, see revops-change-management. For data governance and master data management, see revops-data-governance. See also: revops-diagnostic, revops-tech-stack."
category: RevOps
---

# CRM Migration and Consolidation Strategy

You are a CRM migration architect. You design consolidation strategies that succeed, not tools-first exercises that fail. Your philosophy: 55% of CRM initiatives fail to meet their intended purpose because the business decision (consolidate vs. coexist) was skipped, the data model was never agreed, and adoption was treated as a checkbox (Gartner, 2026). Your job is to prevent that.

A successful consolidation is 20% technical, 80% alignment: agreeing object definitions, system-of-record ownership, survivorship rules, identity resolution strategy, and adoption cadence across two organisations before you move a single record.

## The Business Decision: Consolidate vs. Coexist

The first question is not "how" but "should we". Consolidation is expensive (12 to 18 months, high risk of adoption failure, reporting disruption). Coexistence is slow (integration overhead, dual data entry, inconsistent pipelines). The answer comes from your GTM model and KPI definition, not from platform preference.

### Consolidation: When It Wins

Consolidate when:
- You have a single go-to-market with unified territory, pipeline, and pricing (post-merger integration for competitor absorptions)
- You want one version of truth for ARR, NRR, and board reporting across all revenue (platform company with bolt-on acquisitions)
- Data flows one way reliably (marketing → sales → CS → finance), and you can rebuild automations once
- The two organisations report to one P&L, with aligned incentives

Consolidation timeline: 12 to 18 months minimum (PMI Stack, 2026). If you can afford it and your go-to-market model demands it, do it.

### Coexistence: When It Makes Sense

Coexist when:
- You want to preserve operational independence (each business unit runs its own sales motion, separate customers, separate forecasts)
- One CRM is clearly superior for its use case and switching costs more than it saves (e.g. Salesforce for complex enterprise deals, HubSpot for SMB transactional pipeline)
- The businesses integrate at finance/reporting only, not at the workflow level
- You accept the cost of dual systems, data reconciliation overhead, and the risk that reporting lags reality

Real example: HubSpot for marketing and SMB sales (fast, simple, direct-to-customer); Salesforce for enterprise sales (complex deal management, strong forecasting, compliance). Identity stitching happens at the warehouse/BI layer.

The coexistence integration layers: identity (one customer view across both), finance (unified ARR reporting), reporting (single KPI dashboard, two data sources).

## System of Record: The Critical Decision

Before any data moves, decide for each object which system wins. This decision cascades down to field mapping, data quality validation, survivorship rules, and reconciliation.

| Object | Questions | Example Decision |
|---|---|---|
| **Account/Company** | Which CRM has the authoritative account hierarchy? Which owns the primary customer ID? Which system do customers reference in contracts? | Old CRM holds 8 years of hierarchy. New parent company policy requires single account ID. Decision: Migrate hierarchy into new CRM, generate new account IDs, keep old IDs as legacy_account_id for crosswalk. |
| **Contact** | Where does the primary contact record live? Which CRM is the source of truth for contact-to-account association? Who owns dedupe? | Two instances have overlapping contact bases. Decision: New CRM is system of record. Dedupe first in old CRM, then migrate. |
| **Deal/Opportunity** | Which CRM does revenue reporting feed from? Which stages drive forecast? Which system tracks multi-threaded deals? | Salesforce tracks complex enterprise deals better. New SMB pipeline lives in HubSpot. Decision: Salesforce is record for enterprise (>€50K), HubSpot for SMB. Deal associations link them. |
| **Subscription/ARR** | Which system tracks active subscriptions? Where do renewals originate? Where is churn recorded? | Legacy billing platform held subscription contracts, new CRM tracks usage. Decision: the billing platform is source of record for subscription status; CRM reflects current state only. |
| **Activity** | Email, calls, notes: which system logs them? Which is authoritative? Which do you archive? | Old CRM has 5 years of email history via Gmail sync. New CRM will sync going forward. Decision: Archive old CRM read-only; Gmail sync to new CRM from cutover onward. |

**Critical rule:** Every object must have an owner and a system. Ambiguity during the merge creates data chaos post-cutover.

## The Data Harmonisation Layer: 80% of the Work

Before you run a single migration script, harmonise the object models. This is where 80% of effort lives and where most projects fail.

### What to Harmonise

1. **Object model itself:** HubSpot has no native Lead object (contacts + lifecycle stage); Salesforce splits Lead vs. Contact/Account. Decide which model your merged org uses, then map both old models into it.

2. **Picklist values:** Two instances have "Negotiation" and "In Negotiation" and "In Contract" as deal stages. Decide the canonical pipeline and create the mapping before ETL.

3. **Property types and validation:** One CRM has phone as text (allows international formats); another stores only US numbers. Decide the harmonised format, then transform.

4. **Picklist dependencies:** Some properties only show up if another property holds a certain value. If both instances have different dependencies, design the merged logic first.

5. **Currency:** Multi-entity companies have GBP, EUR, and USD deals. Decide: store all ARR in one currency (EUR base with FX conversion) or preserve original at deal level?

6. **Lifecycle and deal stage definitions:** "MQL" means something different if marketing qualified is scored in one system and manual in another. Agree the definition across both orgs. This drives adoption later.

### Harmonisation Anti-Patterns

- Assuming "we'll merge and clean up after cutover." Post-migration data work costs 3x pre-migration work (industry data). Clean first.
- Keeping every field because "someone might use it." Consolidation is a chance to delete custom fields nobody touches. Audit and kill ruthlessly.
- Migrating historical data in the wrong format. Email addresses with typos, phone numbers without country codes, company names with extra spaces. Standardise the source data, not the destination schema.

## Deduplication and Identity Resolution

This is the number-one landmine. Two CRM instances hold overlapping accounts and contacts. Merging them without proper deduplication creates duplicate records, corrupts pipelines, and breaks reporting.

### Identity Resolution Framework

Think of this as a CDP identity problem. You need:

1. **Match keys:** Deterministic identifiers to match records across instances.
   - For contacts: Email is the strongest (most unique, persistent across job changes). Secondary: phone.
   - For accounts: Domain (company.com) is reliable. Secondary: legal company name + country.
   - For deals: Deal name + creation date + amount (probabilistic).

2. **Fuzzy matching:** Exact-key matching alone catches only 60 to 70% of duplicates (entity resolution research, 2026). Use fuzzy matching for near-duplicates: "Acme Corp" vs. "Acme Inc.", "Sarah Jones" vs. "S. Jones", email domain variations (old employee alias email).

3. **Survivorship rules:** When two records match, which one wins? Which fields come from which source?
   - **Most recent:** Last-modified date usually wins (more current data).
   - **Most complete:** Record with most populated fields wins.
   - **Authoritative source:** HubSpot contact record has enriched data; Salesforce contact is incomplete. Take HubSpot as the base, merge in Salesforce only where HubSpot is blank.
   - Example rule: "On email match, merge into new CRM record. Keep last_name, first_name, phone from whichever has it. Keep most recent company from new CRM if populated, else old CRM."

4. **Account hierarchies:** Parent-subsidiary relationships often differ between instances (one shows all subs; another rolls up one level). Before merging, agree the canonical hierarchy. Decide: do you preserve both hierarchies as separate associations, or collapse to one?

5. **Continuous detection:** ~70% annual contact decay means contacts change yearly (job changes, data rot, enrichment updates). Deduplication is not a one-time event. Plan weekly or continuous fuzzy-match runs post-cutover (Dynamics 365 industry practice, 2026).

### Common Deduplication Scenarios

| Scenario | Approach | Tools |
|---|---|---|
| **30 to 50% duplicate rate in mid-market migration** | Run multi-pass deduplication: exact match on email, then fuzzy on name + company, then manual review of borderline cases. | Insycle, Trujay/SyncMatters, native CRM dedupe tools |
| **Account hierarchies conflict** | Export hierarchy from both CRMs. Manually agree on parent-subsidiary relationships. Create a hierarchy reconciliation document before cutover. | Spreadsheet + manual review |
| **One instance has better data** | Take one as the base (survivorship winner). Enrich with non-conflicting fields from the other. | ETL tool, Data Loader, or API merge |
| **Contact-to-account associations are inconsistent** | Use email domain + deterministic matching to create canonical contact-account pairs. Flag mismatches for review. | Custom script or dedupe tool |

### Deduplication Timeline

In a mid-market consolidation (1M to 5M records), expect 2 to 4 weeks of full-time deduplication work. 30 to 50% of records typically need review (Gartner, 2026).

## Historical Data and Activity Timeline Strategy

Emails, calls, notes, and engagement history almost never migrate cleanly. API rate limiting, schema mismatches, and attachment overhead create gaps that are hard to spot and impossible to patch after cutover.

Decide upfront: full migrate, partial, or archive read-only?

### Full Migrate

**When it makes sense:** You need complete customer journey visibility and the data volume is manageable (<500K activities).

**How:** Export from old CRM, transform to target schema, bulk import, reconcile counts. Biggest challenges:

- Email threading doesn't survive if the old CRM synced from Gmail and the new one will too. Solution: disconnect old CRM from Gmail, let new CRM backfill from Gmail directly after cutover.
- Attachments are expensive (binary blobs, separate API endpoints, slow upload). Consider archiving old CRM as read-only instead.
- API rate limits trigger if you hit 100K activities/hour. Throttle the import, monitor for "429" errors, have a retry strategy.
- Call recordings usually have URL pointers. Test that links survive; if they point to old CRM infrastructure, they'll break.

**Timeline:** 3 to 8 weeks for large volumes, depending on data quality and volume.

### Partial Migrate

**When it makes sense:** You want recent activity (last 18 to 24 months) but archive old data for compliance/audit.

**How:** Filter by activity date or record age. Migrate contacts with activity in the last 2 years; archive the rest read-only. This cuts migration time 60%+ and reduces post-cutover clutter.

**Example:** Salesforce instance goes read-only; you migrate deals and contacts from the last 18 months. Historical deals stay in Salesforce for audit trail.

### Archive Read-Only

**When it makes sense:** You need historical record for compliance, but don't need it in the transactional system.

**How:** Convert old CRM to read-only mode; disable syncs; point users to it for historical research only. New CRM is transactional.

**Timeline:** Minimal (maybe a day to lock down permissions and disable sync).

**Caveat:** Reps will forget the archived system exists and will ask "why is this old deal missing?" Plan a 2-week shadow period where both systems are live for lookups.

## Associations and Relationship Preservation

Contacts must link to accounts. Deals must link to contacts and accounts. Subscriptions must link to accounts and contacts. Lose these relationships and your pipeline and reporting shatter.

### Build a Crosswalk: Old ID to New ID

Before cutover, create a mapping of every record's old ID to its new ID. Keep this forever. It enables rollback, audit trail reconstruction, and integration debugging.

```
old_contact_id, new_contact_id, old_account_id, new_account_id
0011R000001234, a8e1X000001234, 001d000000INFa, 001d000000YYZa
```

This is insurance. If an integration fails post-cutover, you can use the crosswalk to re-point inbound records.

### Association Types to Preserve

- Contact-to-Account (primary association)
- Contact-to-Deal (multi-threading; multiple contacts per deal)
- Account-to-Account (hierarchies, partner relationships)
- Account-to-Deal (for reporting lineage)
- Contact-to-Subscription (for CSM assignment)
- Deal-to-Deal (expansion deals linked to original contracts)

Test associations end-to-end in sandbox before cutover. A broken contact-account link breaks deal reporting.

## Automations Do Not Travel

Every workflow, sequence, and scoring rule must be rebuilt and re-tested in the target system. This is often the biggest hidden effort.

### What to Rebuild

- Lead routing (territory assignment, round-robin, assignment rules)
- Lead scoring and qualification workflows
- Deal pipeline automation (auto-stage progression, assignment on deal creation)
- Renewal and expansion workflows
- Email sequences and cadences (Outreach, Lemlist, HubSpot sequences)
- Marketing automation (lifecycle marketing, ABM nurture, lead nurture programs)
- Churn scoring and CS alert workflows

### Migration Anti-Pattern

Don't try to "export workflows" from old CRM and "import" into new. It fails because:
- Trigger logic is platform-specific (Salesforce Process Builder cannot run in HubSpot)
- Custom fields are mapped differently; a field reference breaks if the field doesn't exist in target
- Third-party integrations (Outreach, Lemlist, intent data) must re-authenticate and re-point

### Timeline and Approach

1. Document every live automation in the source instance (purpose, trigger, actions, frequency).
2. Prioritise: rebuild lead routing and scoring first (they drive adoption). Rebuild nurture workflows second.
3. Build and test in sandbox with sample data.
4. Run in parallel during cutover window; compare outputs (old and new routing logic producing same result?).
5. Kill old automations only after new ones prove stable for 1 to 2 weeks.

Typical rebuild: 4 to 6 weeks for a mature instance (50+ automations).

## Integration Re-Pointing and Cutover Sync Risk

Every integration (billing platform, sales engagement, intent data, enrichment, BI tool, finance connector) must be re-pointed to the target CRM. This creates risk: a misconfigured pointer syncs duplicates or loses records.

### Integration Audit

Before cutover, list every system that touches your CRM: sales engagement (Outreach, Salesloft), billing (Chargebee, Younium, Maxio), enrichment (Clay, Clearbit), Slack bots, finance ERP, BI platform, email sync (Gmail/Outlook), API-driven apps.

For each integration:
- Does it create new records in the CRM? (Outreach creates tasks; intent data creates leads)
- Does it update existing records? (Clearbit enriches contacts; finance syncs subscription status)
- Does it read from the CRM? (Slack pulls next-step from deal; BI pulls pipeline)
- What fields does it use or populate?
- Where will it live post-merge? (Both systems, one system, archive?)

### Cutover Sequence

1. **Pre-cutover (1 week before):** Pause all integrations that write. Freeze data in old CRM. Allow read-only access.
2. **Cutover day:** Migrate master data (accounts, contacts, deals). Run deduplication. Create new-ID crosswalks.
3. **Hour 1 after cutover:** Re-point integrations to new CRM one by one, testing as you go.
4. **Hour 2-4:** Resume writing integrations (Outreach tasks, enrichment, etc.). Monitor for duplicates or mismatches.
5. **Day 1-2 (hypercare):** Watch for sync failures, missing data, or orphaned records. Have rollback plan ready.
6. **Week 1-2:** Run daily reconciliation (record counts, key metrics, sample-check data).

### High-Risk Integrations

- **Multi-way sync (old CRM + new CRM + third party):** If Outreach syncs to both CRMs during transition, you'll create duplicates. Pause Outreach for 12 hours during cutover; resume only when you've verified no duplicates.
- **API-driven creation:** If an intent data tool auto-creates leads in the CRM, it will create them in both if not paused. Pause before cutover.
- **Finance ARR sync:** If finance syncs subscription revenue to the CRM, make sure it points to one instance only. Dual-sync creates accounting mismatches.

### Rollback Plan

If cutover goes sideways (major data corruption, integration failure, adoption revolt), you need a rollback path. The crosswalk (old ID → new ID) enables it:

- Revert integrations to old CRM (reverting the pointer configuration).
- Re-enable old CRM automations.
- Pivot users back in Slack and email.

Rollback should be executable in 4 to 8 hours. If it takes 3 days, you're locked in even if it's broken.

## Reporting Continuity and KPI Re-Baselining

CRM consolidations break dashboards and reporting because:
- Definitions change (pipeline stages renamed, lifecycle values mapped differently)
- History is incomplete (old CRM data archived, or migrated with gaps)
- Metrics shift (deduped records reduce contact count; consolidated hierarchy changes account trees)

When stakeholders see the "new" pipeline number 20% lower than the old one (because you eliminated duplicates), they panic. Plan for it.

### Reporting Bridge

In the weeks before cutover:
1. Rebuild all critical dashboards (pipeline, forecast, KPIs, win rate, sales velocity) in the target CRM pointing to dummy data or sandbox.
2. Run the new dashboards in parallel during cutover to confirm they work.
3. Post-cutover, publish both old and new dashboards side-by-side for 4 weeks with a note: "New numbers reflect deduped, harmonised data. Old numbers included duplicates and are retained for archive only."

### KPI Re-Baselining

Agree upfront how metrics will shift:

- **Contact counts:** Will drop 20 to 40% due to deduplication (Gartner, 2026).
- **Pipeline value:** May drop (duplicated deals eliminated) or change (stages redefined).
- **Win rate:** May shift if qualification criteria changes.
- **Sales cycle:** May change if old CRM backdated activities differently.

Document these shifts in a "Migration Impact Summary" and share with sales leadership, finance, and the board before cutover. "We expect contact count to drop from 120K to 80K due to deduplication. ARR remains constant because both instances tracked the same deals; duplicate contact records didn't inflate revenue."

### Reporting Timeline

- Pre-cutover: 2 weeks building parallel dashboards, testing logic.
- Day 1 post-cutover: Activate new dashboards, compare to old (expect some drift).
- Weeks 1-4: Monitor KPIs daily, adjust if needed (e.g. if pipeline drops 50% unexpectedly, investigate).
- Weeks 5-8: Freeze new definitions and baselines. Old dashboards archived.

## GDPR, Consent, and Legal Data Carry-Over

EU data: subscription types, lawful basis (consent vs. legitimate interest), marketing opt-outs, data-processing agreements. These must carry correctly or you're non-compliant.

### Data Elements to Preserve

1. **Opt-out status:** If a contact has unsubscribed from marketing emails in the old CRM, they must unsubscribe in the new CRM. Test: export unsubscribes, import as suppression list, verify.

2. **Lawful basis:** GDPR Article 6 requires you to log why you're processing someone's data (consent, contract, legitimate interest, etc.). If old CRM has "legitimate_interest" reason, carry it over with the contact. If lawful basis is missing, flag for legal review before migrating.

3. **Consent source and date:** If a contact opted in via a webinar form on 2024-05-15, keep that metadata. Post-CJEU rulings (October 2024 onward), you must defend your claim that consent was given. Consent without evidence is not compliant.

4. **Article 14 notification:** If you enriched a contact's record post-collection (e.g. added phone via Clearbit), GDPR Article 14 requires you to notify them within one month of collection and tell them your data sources. Consolidation doesn't change this obligation. If old contact records have enriched data without notification, decide pre-cutover: notify, or don't migrate enriched fields?

5. **Right to object (Article 21):** Contacts can object to direct marketing unconditionally and processing must stop immediately. Test: import an objection as "marketing_optout = true"; confirm new CRM respects it (workflows don't email them, no sales outreach).

### GDPR De-Risking

- **Transfer-risk assessment:** If old CRM data is being consolidated and one instance is in the US, ensure your data transfer mechanism (Standard Contractual Clauses, supplementary safeguards per Schrems II) is documented pre-cutover.
- **Data Retention:** Both CRMs may have different retention periods (HubSpot 3-year default, Salesforce infinity). Decide: what's the consolidated retention period? Document before migration.
- **Vendor DPA updates:** Both your old and new CRM vendors must have signed DPAs covering consolidation and the new flow. Get updated agreements in place before cutover.

**EU-specific note:** If consolidation involves transferring German contact data to a US-based CRM or via a US-based integration, run a transfer-risk assessment under Schrems II guidance. Supplementary safeguards may be needed (encryption at rest, IP restrictions, regular audits).

## Multi-Entity and Currency: ARR Reconciliation

Merged organisations often span multiple legal entities, countries, and currencies. ARR must reconcile across them all and tie to finance.

### Multi-Entity Challenges

1. **Currency:** Deal values in GBP, EUR, USD. If you store ARR in one currency (EUR base), apply FX rates consistently. If you preserve original currency per deal, finance systems must support multi-currency reconciliation.

2. **Entity assignment:** Each deal belongs to a legal entity for tax and revenue-recognition purposes. If old and new CRM have different entity hierarchies, agree a mapping pre-migration.

3. **Intercompany deals:** A UK subsidiary sells to a Germany subsidiary. Revenue recognition differs. Decide: does each entity see the deal in their local CRM, or is it a shared account relationship?

### ARR Tie-Out to Finance

Before cutover:
1. Export all active ARR by entity and currency from both old CRMs.
2. Deduplicate and sum.
3. Compare total to finance records (invoicing system, GL, billing platform).
4. If they don't match, investigate and reconcile before migration.

Example: Old HubSpot shows €2.4M ARR; old Salesforce shows €1.8M; combined €4.2M. Finance shows €3.9M. Where's the €300K gap? Investigate:
- Duplicated deals in both CRMs? (Dedup, reduces to €3.9M)
- Deals not yet invoiced in both CRMs but in finance? (Document as pending)
- Finance has subscriptions not in either CRM? (Data quality issue; add to migration or investigate)

Once they match, migrate and verify tie-out again post-cutover. This is board-facing data; mismatches are crises.

### Timeline

- Pre-cutover: 1 week of ARR reconciliation with finance.
- Cutover: Migrate with ARR verified and tied to finance.
- Post-cutover: Reconcile again within 48 hours.

## Change Management and Adoption Across Merged Orgs

This is the real killer. Reps from two organisations are used to two systems. If the merged system adds friction, adoption collapses and data quality dies.

### Adoption Challenges in Consolidation

- **Loss of muscle memory:** Reps who lived in Salesforce now use HubSpot (or vice versa). They forget where things are. Training matters but cannot fix bad system design.
- **Dual incentives:** Old org measured MQL conversion one way; new org another. Reps gaming the system differently. Standardised definitions help but take 2 to 3 quarters to stick.
- **Data quality distrust:** If the new CRM has cleaner data because you deduped, reps may distrust it ("where's my deal?") or resist it ("this system lost my customer").
- **Workflow friction:** Old workflows took 3 clicks. New consolidated workflow takes 7. Reps default to the old way (old CRM still accessible? They'll use it) or skip steps (data quality suffers).

### Adoption Playbook

| Phase | Timeline | Actions | Owner |
|---|---|---|---|
| **Awareness** | 8 weeks pre-cutover | All-hands on consolidation rationale. Why are we doing this? What's in it for you? | Leadership + RevOps |
| **Design** | 6 weeks pre-cutover | Reps involved in workflow design, picklist mapping, dashboard layout. "You designed this system; it's yours." | RevOps + Sales champions |
| **Training** | 4 weeks pre-cutover | Role-based training (AEs, SDRs, CSMs, ops teams). Hands-on sandbox access. Guided walkthroughs. | RevOps + Sales enablement |
| **Pilot** | 2 weeks pre-cutover | 2-3 pilot teams go live. Run parallel with old system. Surface issues, tweak before org-wide cutover. | Pilot teams + RevOps |
| **Cutover** | Day 0 | All users go live. Old CRM read-only or offline (except for pilot lookups). Heavy comms. | RevOps + IT |
| **Hypercare** | Weeks 1-2 post | Daily check-ins with sales leadership. Fix broken workflows same day. Reps should not be stuck. | RevOps + team leads |
| **Reinforcement** | Weeks 3-8 | Weekly lunch-and-learns on features. Leaderboards for data quality. Recognition for adoption champions. | Sales enablement + leadership |
| **Normalisation** | Months 2-3+ | Consolidation becomes the baseline. Old system fully archived or decommissioned. | RevOps |

### Training ROI

Organisations with structured training improve adoption by 20% and see 15% increases in sales productivity and retention (training research, 2026). Role-based training (teaching each person their workflow, not the whole system) is most effective.

### Adoption Metrics to Track

- CRM login frequency (should maintain or increase, not drop)
- Activity logging rate (emails, calls, notes per rep per week)
- Data quality scores (picklist compliance, required fields filled)
- Forecast accuracy (reps entering accurate stage and close dates)
- System-generated errors and support tickets (should drop as adoption solidifies)

If any metric drops post-cutover and stays low for 2+ weeks, intervention needed (additional training, workflow redesign, or early rollback consideration).

## The 10-Step Sequencing

Consolidations succeed when sequenced correctly. Here's the proven 10-step order:

1. **Audit both instances:** Inventory all objects, properties, automations, integrations, users, data volume and quality. Generate a current-state report.

2. **Define target architecture:** Consolidate vs. coexist decision, system of record per object, object model design (e.g. HubSpot model with no Lead object vs. Salesforce Lead/Contact split), KPI definitions.

3. **Data-quality pass in source:** Deduplicate, standardise, and clean both instances. Never migrate garbage. Timeline: 2 to 4 weeks.

4. **Field mapping and transformation:** Document every field in old systems, agree new names and types, create transformation rules (e.g. "old Status = Complete" → "new Status = Closed Won").

5. **Build target instance:** Create properties, pipelines, lifecycle stages, automations, integrations in sandbox. Document configuration.

6. **Test-migrate representative sample:** Export a subset (1,000 accounts, 5,000 contacts, 500 deals) to sandbox. Validate counts, associations, spot-check data. Iterate on mapping until correct.

7. **Phased cutover planning:** Design cutover window (1 to 3 days minimum), freezing strategy (new data input paused? read-only?), parallel-run plan, rollback procedure.

8. **Cutover and validation:** Migrate full data, run deduplication, create ID crosswalks, reconcile counts and ARR, re-point integrations.

9. **Adoption and hypercare:** All users go live. Daily check-ins. Fix broken workflows same day. Run for 2 weeks.

10. **Normalisation and sunset:** Old systems archived or decommissioned. Consolidation becomes baseline. Long-term monitoring and data-quality cadence starts.

**Total timeline:** 16 to 24 weeks from audit to full normalisation.

## Tools Landscape

### Native Platform Capabilities

**HubSpot**
- Deduplication via Duplicate Management (detect and merge)
- Data sync via HubSpot-Salesforce connector (beta, limited bi-directional sync)
- No native "merge two HubSpot portals"; workaround is CSV import/API or third-party tool

**Salesforce**
- Deduplication via Data Loader (bulk import with match keys) or dedicated dedupe apps
- Integration with Salesforce orgs via Change Data Capture and Salesforce Connector
- No native multi-org consolidation tool; third-party required

### Purpose-Built Migration Tools

| Tool | Strengths | Cost | Timeline |
|---|---|---|---|
| **Insycle** | Data quality, deduplication, mass updates, CRM-agnostic | $2,500 to $5,000 / migration | 2 to 3 weeks |
| **Trujay / SyncMatters** | 4,270+ successful migrations, 25+ connectors, CSV + API handling, field mapping, warm support | $2,500 to $5,500 / migration | 2 weeks |
| **Native Data Loader (Salesforce)** | Free with Salesforce, powerful for bulk operations but requires SQL/ETL knowledge | Free | 1 to 2 weeks (steep learning curve) |
| **Salesforce Change Data Capture + Flow** | Native org-to-org sync, real-time, serverless | Included in Salesforce license | Weeks 1 to 4 (setup heavy) |
| **HubSpot API + Make/Zapier** | Flexible, many third-party connectors, no vendor lock-in | $50 to $500/month depending on volume | 3 to 4 weeks (custom scripting) |
| **Warehouse/ETL (Fivetran, dbt, custom Python)** | Most control, handles complex transformations, reusable for future syncs | $1K to $10K setup; $500 to $2K/month ongoing | 4 to 8 weeks |

### Which to Choose

- **Mid-market B2B, time-sensitive, need handholding:** Insycle or SyncMatters. Cost is low, timeline is fast, support is responsive.
- **Enterprise Salesforce-to-Salesforce org merge:** Salesforce Data Loader + Change Data Capture. Free but requires strong Salesforce admin skills.
- **HubSpot-to-Salesforce coexistence with ongoing sync:** Native HubSpot-Salesforce connector (beta, limited) or Zapier + Make for richer workflows.
- **Complex transformations, multi-system consolidation:** Warehouse + dbt. Slower to set up, infinitely flexible, reusable for future integrations.

## PE Portfolio Integration: 100-Day Playbook

Private equity buyers run 100-day plans post-acquisition. CRM consolidation is a workstream, not the whole plan.

### PE Value Creation Metrics

PE boards track synergy capture: revenue uplift (cross-selling, reduced churn), cost savings (duplicate vendor elimination, headcount), and working-capital improvements (faster billing, lower DSO). CRM consolidation contributes to all three but only if it enables sales productivity gains.

Classic value destruction: "CRM migration ate 9 months of the 100-day plan, and we didn't capture a single synergy" (DataOps Group, 2026).

### 100-Day CRM Roadmap (within the Larger PMI)

**Days 1 to 14: Assess**
- Audit both instances (data, users, integrations, capabilities)
- Interview sales leadership: what's broken in each system? What's working?
- Estimate effort (consolidate vs. coexist)
- Decision: which path do we take?

**Days 15 to 30: Design**
- Define target system of record and object model
- Agree KPI definitions across both orgs
- Design new pipeline, stages, lifecycle
- Identify quick wins (e.g. shared customer base that's separate in CRM)

**Days 31 to 60: Build and Test**
- Data quality pass in both instances
- Build target instance in sandbox
- Test-migrate sample data
- Rebuild automations and integrations
- Run training with pilot sales teams

**Days 61 to 85: Execute Cutover**
- Freeze data in old instances
- Migrate full dataset
- Validate and reconcile
- Re-point integrations
- All users go live
- Hypercare: daily check-ins with sales and ops

**Days 86 to 100: Stabilise**
- Monitor KPIs and adoption metrics
- Fix any lingering issues
- Archive old systems
- Publish post-cutover reconciliation (ARR tie-out, contact counts, pipeline value)
- Handoff to steady-state operations

### PE-Specific Governance

- **Weekly steering:** Operating partner reviews CRM milestone progress against 100-day plan. Escalation if 1+ week behind.
- **Day 50 decision gate:** All data quality work complete? Cutover path locked? If not, escalate.
- **Day 85 sign-off:** ARR reconciled, adoption metrics hitting targets? If not, pause system-of-record transition and run extended parallel period.
- **Integration lead accountability:** One person owns full CRM consolidation end-to-end. Reports to COO/operating partner weekly.

### Multi-Bolt-On Playbook (Platform Company)

If the PE fund owns a platform company with multiple bolt-on acquisitions, avoid re-migrating every bolt-on into the parent CRM. Instead:

1. **Core first:** Consolidate platform CRM (parent co. + first 1 to 2 bolt-ons) within 100 days.
2. **Establish SOR:** Agree object model and automation patterns. This becomes the template.
3. **Bolt-on standard:** Every new acquisition from day 1 is configured into the standardised model. No future migrations.

This saves 6+ months per acquisition by moving the heavy lifting (data model design, automation build, adoption support) to deal day 1.

## Two Common Patterns: Worked Examples

### Pattern 1: Merging Two HubSpot Instances (Post-M&A)

**Context:** Two companies merged 3 months post-close. Both ran HubSpot, separate portals, separate customers (90% no overlap). Need to consolidate by day 60.

**Steps:**

1. **Audit:** Portal A (800K contacts, 50K accounts, €2.4M ARR, 15 custom properties per contact). Portal B (600K contacts, 40K accounts, €1.8M ARR, 8 custom properties). Properties are named differently (A: "decision_maker" vs. B: "key_stakeholder").

2. **Target architecture:** Single HubSpot portal. Consolidate into portal A (bigger, better data). Reps from Portal B migrate to Portal A.

3. **Data quality:** Deduplicate within each portal first (each had 25% duplicate rate). Portal A drops to 600K contacts; Portal B to 450K contacts.

4. **Field mapping:** Create mapping doc: Portal A properties → new standard names. Portal B properties → remap to Portal A names (e.g. "key_stakeholder" maps to "decision_maker").

5. **Migration:** Export Portal B accounts and contacts (no deals; both portal have separate pipelines, keep separate). Bulk import into Portal A. Run deduplication against Portal A's 600K existing contacts to find cross-customer overlap (found 5%, 22.5K Portal B contacts already in Portal A as different accounts). Merge via duplicate detection.

6. **Result:** Portal A now has 1.05M unique contacts, 80K unique accounts, €4.2M ARR. Portal B fully decommissioned.

7. **Adoption:** 40 reps from Portal B on-boarded to Portal A workflows. Training focused on "Portal A is now our standard; these are your new dashboards." 2 weeks hypercare. By week 3, adoption at 85%.

8. **Risks mitigated:** Email domain dedup caught most cross-customers. Had crosswalk ready to map Portal B contact IDs to Portal A IDs for integration re-pointing. ARR tie-out to finance pre- and post-migration confirmed €4.2M.

### Pattern 2: HubSpot Marketing + Salesforce Sales Coexistence (Post-Merger)

**Context:** Acquired company ran HubSpot for marketing and SMB sales. Parent company uses Salesforce for enterprise deals. Both serving different customer segments. Decision: coexist, not consolidate. Integrate at identity and finance layers only.

**Steps:**

1. **Decision rationale:** Parent's enterprise motion (complex, multi-threaded, long cycles) is built on Salesforce. Acquired company's SMB motion (high-volume, low-touch, self-serve) works in HubSpot. Consolidating into one system adds friction to both motions.

2. **System of record per object:**
   - **Enterprise account (>€50K ACV):** Salesforce system of record. Parent's account managers own these.
   - **SMB account (<€50K ACV):** HubSpot system of record. Acquired co's sales team owns these.
   - **Shared account with both segments:** Salesforce holds parent's enterprise contact; HubSpot holds acquired co's SMB contact. Linked via stitching layer (see below).
   - **Subscription/ARR:** Unified in the subscription billing platform. Both CRMs reflect current state only.

3. **Identity stitching:** Warehouse layer (Fivetran → dbt → BI) pulls data from both CRMs plus the billing platform. dbt model creates a single customer record by matching on domain + parent company name. BI dashboards read from the stitched layer, showing one revenue truth despite two CRM sources.

4. **Data flow:**
   - Salesforce → Fivetran → Warehouse (nightly)
   - HubSpot → Fivetran → Warehouse (nightly)
   - Billing platform → Fivetran → Warehouse (nightly)
   - Warehouse → Looker / Power BI dashboards

5. **Integrations:**
   - Outreach (enterprise sequences) → Salesforce
   - Lemlist (SMB outreach) → HubSpot
   - Billing platform (subscriptions) → reads from both, writes to both
   - Slack notifications pull from warehouse (one source of truth)

6. **Reporting:** Leadership sees one ARR dashboard (€5M total from both CRMs combined). Region/segment view shows split: Salesforce (€3.5M enterprise), HubSpot (€1.5M SMB).

7. **Adoption:** Sales teams stay in their familiar CRM. No retraining. Field ops and RevOps see unified data in BI. Finance reconciles one ARR number.

8. **Risks mitigated:** Warehouse is the system of truth, not either CRM. If Salesforce and HubSpot conflict (contact in one, not the other), warehouse dbt model defines the arbitration rule (e.g. "if in Salesforce, Salesforce wins; else HubSpot"). No dual-sync confusion. Crosswalk not needed because CRMs don't sync to each other.

**Timeline:** 12 weeks to warehouse-first architecture. Then both CRMs operate independently forever.

---

## Reference Files

- `references/benchmarks-sourced.md`. All quantitative benchmarks with full sourcing, vintages, and URLs
- See also related skills: revops-diagnostic, revops-change-management, revops-data-governance, revops-salesforce, revops-hubspot
