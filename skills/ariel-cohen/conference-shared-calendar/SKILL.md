---
name: "conference-shared-calendar"
title: "Shared conference calendar"
description: "Create or maintain a shared conference reference calendar from an official agenda, including sessions, side events, sharing permissions, timezone checks, and duplicate-safe updates. Use when a participant or team wants a shared event calendar or an importable agenda."
category: Events
---

# Shared conference calendar

Create a useful reference agenda that does not consume people's meeting availability.

## Establish the inputs

Use `assets/calendar-worksheet.md`. Reuse information already supplied. Ask only for missing facts that affect correctness: official source, event dates, venue IANA timezone, calendar owner/destination, and intended readers/editors. Never infer timezone from the operator's computer. Distinguish a private team calendar from a publicly shared event calendar.

Inspect the existing destination and prior imports before creating anything. Prefer an authorized existing calendar when it serves the purpose. Use a connector/API when available; otherwise use the authenticated browser. With no live access, prepare an ICS and exact setup instructions and label the live setup unfinished.

## Normalize the agenda

Read the official agenda and linked session details. Capture source ID, title, date, start/end, timezone, venue/room, speaker, source URL, and confidence. Retain concurrent sessions; this is a reference calendar, not one person's itinerary. Do not copy private notes into shared descriptions.

Prefer explicit organizer updates over stale listings. Keep a source/change log and flag contradictions. Never turn an unpublished time into a precise appointment: a known date may have a Free all-day “TIME TBD” marker; unknown dates stay in a separate unresolved list. Do not confuse a short public workshop with an independently arranged longer activity.

## Build and publish

1. Create a separately named reference calendar with the venue timezone. Verify the destination before importing or writing.
2. Make reference events **Free / transparent**. Colors are cosmetic. Sharing “see only free/busy” is a visibility permission and is different from event Free/Busy status.
3. Include source links and useful logistics. A reference copy of a dinner does not accept the original invitation or add guests. Do not add ATTENDEE fields to an ICS reference export.
4. Prefer API upserts with a saved source-ID → remote-event-ID mapping for ongoing maintenance. If using ICS, assign stable UIDs from conference namespace plus source ID; use valid timezone-aware times, CRLF, escaped text, UTF-8-safe 75-octet line folding, and exclusive all-day end dates. Validate event counts, ordering, and sample times before import.
5. ICS import is a snapshot. Stable UIDs alone do not guarantee that repeated Google imports update existing entries. Do not reimport blindly. Inspect and update the existing records, or prepare a deliberate replacement plan without deleting unrelated events.
6. Apply the requested sharing permissions. Give viewers event details and editors only the intended editing rights. Public access is a separate explicit choice. If sharing would notify people and the user has not authorized invitations, finish the calendar and present the exact recipients/permissions for approval.

Read `references/google-calendar.md` for provider steps and sources.

## Verify and hand off

Compare imported event count against the normalized agenda, accounting for pre-existing records. Check first/last dates, simultaneous sessions, room names, one all-day marker, and timezone rendering. Confirm events are Free and sharing matches the requested scope. Check recipient visibility when access permits; otherwise report it unverified.

Return the calendar link or ICS path, source timestamp, counts, permissions, unresolved times, and update instructions. Save the ID mapping/change log privately with the user's project, not inside the distributable skill. Recommend placing selected sessions and duties on each attendee's own calendar as Busy; use conference-personal-plan if installed.
