---
name: "conference-booking-links"
title: "Cal.com booking links"
description: "Set up and troubleshoot Cal.com meeting links for a conference, with event-specific dates, in-person location, buffers, calendar conflict checks, individual or team hosts, and public booking-page verification. Use for conference booking availability or missing meeting slots."
category: Events
---

# Conference booking links

Produce working links with verified availability for every host. Read `references/cal-com.md` for product sources and `assets/booking-worksheet.md` for inputs and results.

## Establish the configuration

Reuse known event dates, venue timezone, location, hosts, daily meeting windows, duration, buffers, minimum notice, and personal commitments. Offer 20-minute meetings with 10 minutes afterward and two hours' notice only as a starting suggestion; use the user's preferences. Do not silently purchase a plan or create accounts.

Inspect existing event types and schedules to avoid duplicates or changing unrelated booking links. Prefer available Cal.com tools; otherwise use the logged-in browser. If access is missing, produce the configuration and remaining setup steps without claiming live completion.

Choose the hosting model from the intended meeting:
- One participant: personal event type.
- Separate links per teammate with standardized settings: managed template if available and authorized, otherwise consistent personal event types.
- All specified hosts must attend: collective.
- Any suitable available teammate may attend: round robin.

Check current plan capabilities. Do not substitute a different host model merely because a feature is unavailable.

## Configure

1. Connect each host's calendar through normal account authorization. Verify both calendars checked for conflicts and the destination for newly booked meetings. Do not copy credentials or assume a connected account checks every calendar.
2. Create a dedicated conference availability schedule in the venue IANA timezone. Apply the exact permitted dates and hours, using the current date-range and date-override controls. Attach it to the event type. Keep availability outside the event closed; date overrides alone may leave recurring hours open.
3. Set the title, duration, precise in-person meeting point, before/after buffers, minimum notice, and desired slot interval. Buffers do not necessarily set the spacing between displayed start times.
4. Assign and activate the intended hosts when relevant. Verify each managed instance is usable; a shared template does not prove that every host's calendar connection or schedule works.
5. Inspect existing Busy conflicts. Keep genuine meetings, sessions the person will attend, speaking slots, travel and assigned duties Busy. A broad “whole conference” reference hold may suppress all meetings even when the invitation is unanswered. Convert it to Free only when it is confirmed to be a reference hold and the user has authority and has authorized that change. Never clear real commitments just to produce slots.
6. Preserve a useful rollback record: prior settings for modified event types, schedule IDs, host assignments and calendar selections. Store private operational IDs in the user's project, not this reusable skill.

## Test every public link

Open the public booking page, using a fresh visitor view where possible. Record the displayed timezone and test:
- First and last intended bookable days show the expected windows, subject to actual conflicts and notice limits.
- The day before, day after, and dates outside the event are unavailable.
- At least one known free slot appears; a known Busy interval and its relevant buffers are excluded.
- Selecting an offered slot reaches the booking form with the correct host, duration, date, timezone and meeting location. Do not submit a test booking without authorization; it sends real notifications.
- Visitor timezone conversion preserves the same underlying meeting instant.

Never apply an automatic “add one day” date-range workaround. If UI boundaries behave unexpectedly, compare timezone and date semantics, adjust only from evidence, and retest both included and excluded dates. Keep the dedicated schedule as an additional constraint.

For missing slots inspect, in order: selected schedule and timezone; date range/overrides; minimum notice and buffers; connected calendar health and selected conflict calendars; Busy holds; host activation; booking limits. Use Cal.com's troubleshooting view when available. A view-only calendar requires owner remediation: identify the specific blocker and owner, preserve the link as pending verification, and do not claim it fixed.

Return a per-host results table with public link, schedule window, timezone, verified free slot, verified conflict, boundary checks, and unresolved owner actions. Distinguish “configured,” “public form verified,” and “real booking tested.” Provide the links for the user to share; do not send outreach merely because links exist.
