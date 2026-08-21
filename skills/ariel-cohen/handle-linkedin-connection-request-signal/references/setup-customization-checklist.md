# Setup & Customization Checklist

Work through this before enabling the skill. Every item is either a
placeholder to fill, a policy decision to make consciously, or a behavioral
invariant to preserve.

## Placeholders to fill

- [ ] `{{PROFILE_OWNER}}` — whose inbound connection requests this instance
      processes. Run one instance per monitored team member.
- [ ] `{{CRM}}` — your CRM (e.g. HubSpot, Attio).
- [ ] `{{INTERNAL_DOMAINS}}` — every domain your own team uses; requests from
      these stop silently.
- [ ] `{{VISIBILITY_CHANNEL}}` — the Slack channel that gets one visibility
      post per processed request. A dedicated channel (e.g.
      #connection-requests) keeps it reviewable without noise in your MQL
      channel.
- [ ] `{{CRM_HYGIENE_SKILL}}` — your create/update-companies-and-contacts
      skill. The hard gate in Step 6 assumes it exists; if you don't have one,
      inline your CRM field conventions there.
- [ ] `{{LEAD_SCORING_SKILL}}` — your scoring methodology. This skill passes
      it explicit active-signal overrides; make sure your scoring skill
      accepts contextual instructions and owns the MQL alert.
- [ ] `{{REACTIVATION_SKILL}}` — optional. If you have a closed-lost
      reactivation skill, the qualifying branch loads it for the deal-owner
      notification. If not, replace with a direct DM/notification to the deal
      owner.
- [ ] `{{SELF_SERVE_THRESHOLD}}` — default: fewer than 50 employees AND ≤$10M
      raised. This is what separates "decision maker = MQL" from "decision
      maker = self-serve."
- [ ] `{{REACTIVATION_WINDOW}}` — default ~90 days. Below this, a closed-lost
      request reads as residue from the lost deal, not new intent.

## Policy decisions

- [ ] **Outreach stays off by default.** The skill ships score-+ alert-only:
      no replies, no accepts, no sequences, no tasks. The original deployment
      ran this way as a deliberate first phase to validate signal quality
      before wiring any action on top. Turn outreach on only as a conscious
      opt-in, and even then route it through your approval flow.
- [ ] **Visibility-channel scope.** Default posts SCORED / NOT ICP / EXISTING
      CUSTOMER / EXISTING RELATIONSHIP and stays silent on
      anonymous/internal/partner/duplicates. Widen or narrow deliberately.
- [ ] **Persona lists.** The decision-maker and weak-persona lists are tuned
      for a GTM-tooling ICP — rewrite both for your buying committee.

## Behavioral invariants (do not weaken)

- [ ] The CRM-pollution gate: no CRM write without identified + resolved +
      not-internal + not-customer + ICP, all five.
- [ ] UNRESOLVED beats guessed: an empty enrichment waterfall ends the run,
      it never ends in a guessed company.
- [ ] The headline is never a company name, and a headline-vs-enrichment
      conflict always triggers a live profile check.
- [ ] The invitation note travels verbatim — never summarized, never invented.
- [ ] Closed-lost requesters are reactivation candidates, not silent drops —
      and the MQL channel gets exactly one post per reactivation.
- [ ] Never the maximum tier on a lone LinkedIn signal; weak personas cap at
      the awareness tier.
