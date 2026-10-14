# Copy examples

Every message below follows copy a team actually used or locked for a live event campaign, with event names, cities, dates and company names replaced by placeholders. Replace every `{placeholder}` with real values before sending.

The point of each example for this skill: how the copy stays true until the cutoff, and where the copy would go stale if the sequence outlived the event.

## Example 1: pre-event meetings at a conference (multi-day runway)

Source: the locked cadence for a multi-day conference campaign. Ask: 15 minutes in person. Blank connection request, no note.

Cadence: blank connection request, 1 hour wait, LinkedIn message 1, 1 day, LinkedIn message 2, 23 hours, email 1, 24 hours, email 2 in the same thread, 12 days, post-event message.

LinkedIn message 1:

> Hi {first}, thanks for connecting. {intro} {insight} We'll both be at {event_name} in {city}, would love to grab 15 minutes there and hear what you're focused on for the rest of the year.

Email 1 (subject: `{company_name} x {sender_company} at {event_name}`):

> Hi {first}, {intro} {insight} We'll both be at {event_name} in {city}, hoping to grab 15 minutes there and hear what you're focused on for the rest of the year.

Post-event message, sent about 12 days after email 2 (hedged, because the sender does not know whether they met):

> Hi {first}, {city} is always a blur. If we didn't get a proper 15 minutes at {event_name}, still keen to show you what we're building at {sender_company}. What does your schedule look like over the next couple of weeks?

What to learn from it:
- The event name and city are written out. The copy never says "next week".
- The post-event message is a separate, final step that opens with "{city} is always a blur". It only makes sense after the event, so it is scheduled after it. The pre-event steps must be dead before then, which is exactly the job of the kill.
- The playbook's own copy rules: no dashes, no semicolons, no exclamation points, LinkedIn messages 25 to 50 words, emails 70 to 140 words.

## Example 2: attendance unknown, two options in one message

Source: a second campaign for people whose company was on the event's list but who were not confirmed attendees. It offers a meeting if they are going and a call if not, so the message stays true whether or not they attend.

LinkedIn message 1:

> Hi {firstname}, thanks for connecting. {sender_firstname} here, {sender_role} at {sender_company}. {company_insight}. A few of us are at {event_name} in {event_city} and {company_name} is on the attendee list. If you're going, would love 15 minutes there, and if not, happy to do a quick call instead.

Post-event message, fixed, sent 3 business days after the event ends:

> Hi {firstname}, {event_name} came and went and I don't think our paths crossed. Still keen to find 15 minutes to show you what we're building at {sender_company} for teams like {company_name}. What does your schedule look like over the next couple of weeks?

What to learn from it: "{event_name} came and went" is true only after the event. The campaign's own timing rule, "3 business days after the event ends", is a cutoff-aware step: it is anchored to the event end date, not to the day the sequence started.

## Example 3: dinner invite as a side door, with timing words that must be adjusted

Source: a pre-conference play. A researched first email asks for a meeting. Two follow-ups carry the dinner and a nudge, both fixed and nameless.

Email, day 3 (the dinner invite):

> We're also hosting an exec dinner on {dinner_night} if that's preferable - can shoot over the reg link if interested. Lmk!

LinkedIn message after the email:

> tried you on email - in town for {event_name} this week?

The source says to adjust "this week" or "next week" to the timing of the send against the conference, and not to paste the registration link in the email but to offer to send it.

What to learn from it: "{dinner_night}" and "this week" are exactly the relative phrases that go stale. This is the case the skill exists for. The kill job has to end this sequence before the dinner night passes, and before "this week" stops being true. Without the kill, a late connection acceptance would deliver "in town for {event_name} this week?" after the conference.

## Example 4: a first email that names the conference and one signal

Source: examples quoted in a pre-conference play for the first email, capped at 250 characters.

> You've been engaging a lot with our content on LinkedIn. Given we're both in {city} this week for {event_name}, thought it might be a great time to connect. How's your sched looking?

> Given the focus on deploying AI agents into call centers, was curious if agents are also driving your own GTM motion. Happy to chat on it live if you're at {event_name} next week. Making the trip?

What to learn from it: both lines carry a relative time ("this week", "next week"). The first is true only while the event week is current, and the second only the week before. Each one sets its own cutoff under the rules in `cutoff-rules.md`.

## What is still missing

There is no real copy here from a same-day dinner top-up or a webinar invite, because neither has been run as a sequence yet. Add one when you have an approved message. Until then the skill gives the rule for those cases in `cutoff-rules.md`, without invented copy.

## Checklist before approving time-sensitive copy

1. Find every relative time word in the copy ("this week", "next week", "tonight", "{dinner_night}").
2. For each, write down the moment it becomes false.
3. Check the sequence's cutoff is before the earliest of those moments.
4. Confirm any step meant for after the event is anchored to the event's end date, not to the start of the sequence.
