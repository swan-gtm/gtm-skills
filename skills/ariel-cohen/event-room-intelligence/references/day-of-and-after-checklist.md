---
title: "Day-of and after-event checklist"
description: "How the floor team uses the dossier on the day, and how to close the loop afterwards by crossing LinkedIn connection requests and profile views against the roster."
---

# Day-of and after-event checklist

## The day before

- [ ] Re-run the live `{{CRM}}` join. Tiers and stages move daily; a dossier built three days out has drifted.
- [ ] Re-check approval status. Late approvals from hunt accounts change the card order.
- [ ] Confirm the PDF opens on a phone with page one as the first hunt card, and that photos render (embedded, not linked).
- [ ] Send the file directly to `{{FLOOR_TEAM}}` and the owners of the deal accounts. No public link, no shared drive folder with broad access.
- [ ] Agree who takes which hunt accounts. Two people approaching the same buyer looks uncoordinated.

## On the day

- [ ] Read the hunt cards on the way in. Five seconds per card: buyer, in the room or not, the play.
- [ ] Use the faces grid at the door for recognition, then go back to the card before speaking.
- [ ] Open with the champion or hand-raiser where one exists; ask for the intro to the rank-0 person rather than cold-approaching the buyer.
- [ ] For delegations (a manager plus their team), offer a group demo slot instead of five separate conversations.
- [ ] For deal accounts: do not pitch. Collect intel, confirm next steps, hand the name to the owner.
- [ ] For customers: thank, ask for a reference, find the expansion seat.
- [ ] Competitors on the watch list: be friendly, do not demo.
- [ ] Capture every conversation as a two-line note (who, what they said, what they want next) before leaving the venue. Memory decays by the next morning.

## After the event (within 48 hours)

The dossier is also the join key for everything the event produced.

1. **Cross the connection-request list against the roster.** Pull the pending and accepted LinkedIn connection requests received by each member of `{{FLOOR_TEAM}}` in the event window. Match by normalised name against the roster. Last run about 40 percent of requesters were on the registration list; the remainder are people who heard the talk second-hand or came unregistered, and they need mapping and sizing from scratch.
2. **Cross the profile-view list the same way.** Profile views in the event window are a weaker signal than requests but the overlap with hunt-account attendees is the list to follow up first.
3. **Tag the cohort at ingest.** Every matched person and account gets an event note in `{{CRM}}` and account memory: `event: <slug>, attended / requested / viewed, met by <name>, said <two lines>`. Without the tag, downstream scoring treats these as anonymous signals with no context.
4. **Update the alias list.** Every registrant you resolved manually, every mover you found, goes into `{{ALIAS_LIST}}` so the next event maps them on rung 3.
5. **Update the committee.** Every `Left` line becomes a CRM contact update; every new rank-0 person becomes a CRM contact if missing. This is the one CRM write this skill produces, and it is a human-reviewed batch, not an automated sync.
6. **Hand-offs.** The conversation notes from the floor go to the account owners as a list, one line per account, in card order. Outreach is theirs to send.

## What not to do

- Do not publish the dossier as a web page or a shared link, even internally. It carries personal data, photos, work emails, and deal values.
- Do not send any message from this skill. It recommends; humans send.
- Do not reuse last event's dossier for a follow-up event without re-running Phases 2 and 3. The whole point is that titles and tiers are current.
