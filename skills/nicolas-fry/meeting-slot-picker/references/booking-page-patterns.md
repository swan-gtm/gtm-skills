# Booking page patterns

Read before driving a counterparty's booking page. Almost every booking page is three screens: a calendar to pick a day, a slot list for that day, and a form for name and email. The loop is: open the page, read it, select a candidate day, re-read to get that day's slots, repeat for each candidate day, score, then book the winner.

## Reading the page reliably

- **Extract text, not pictures, for slots.** A slot list usually scrolls. A screenshot shows the visible handful, which is how an agent concludes a day has no afternoon availability when it has nine slots. Read the page text and record each slot as structured data: day, start time, displayed timezone. Use screenshots only for layout: which month is showing, which days are greyed out, where the navigation arrows sit.
- **Confirm the day selection landed.** Most pages show a status line or heading naming the selected day. Check it names the day just selected before trusting the slot list.
- **Stale reads.** These pages update in place without changing the address. After selecting a day or moving a month, re-read before trusting anything. If the page still names the previous day, the selection did not land.
- **Controls that do nothing.** A month arrow or day cell sometimes has its click handler on a parent element, so selecting the obvious element produces no change. If an action changes nothing visible, take a screenshot, locate the control by position, and try again.
- **Available versus unavailable days.** Pages mark open days with emphasis (bold, a dot, a highlighted cell) and dim the rest. Confirm which convention the page uses from a screenshot before assuming a dim day is closed.

## The timezone selector trap

Most booking pages display slots in a timezone chosen from the viewer's browser or a selector, not the host's zone. Treat the displayed zone as only a label for the numbers on screen:

1. Note the zone the page displays.
2. Convert each slot to the counterparty's local time and the user's local time.
3. Never read the displayed zone as the host's zone unless the page explicitly says it is the host's.

If the selector can be changed, setting it to the user's zone removes one conversion. Write down which zone was showing either way.

## Four booking-flow patterns

| Pattern | How it behaves | What to watch |
|---|---|---|
| **One-step slot click** | Selecting a slot jumps straight to the form. | A mis-click goes straight to the form for the wrong time. Re-read the time shown on the form before submitting. Email validation can run in the background and briefly disable the submit control; wait for it to re-enable. |
| **Slot plus confirm** | Selecting a slot reveals a second control (confirm or next) in its place. | The first click does not reserve anything. Some event types add custom questions after this step; treat them like a routing form. |
| **Pre-qualification routing form** | A form asks qualifying questions (company size, budget, use case, region) before any slots appear. The answers decide which person and which slots are shown. | Answer only what is already known for certain. A wrong answer can route the meeting to the wrong team entirely. If a question is unknown, stop and ask the user. |
| **Signed-in, prefilled form** | The page uses the viewer's signed-in identity and fills name and email automatically. | Verify the prefilled identity is the user, not another account in the same browser, before confirming. |

## Filling the form

- Name and email: the user's own, exactly as they use them with this counterparty.
- Optional fields (phone, notes, "anything to share before the call", guests): leave empty unless the user supplied the content. A note written on the user's behalf is a message sent on their behalf.
- Duration: never change it from what the page offers.

## Verifying the booking

Report success only after the page shows an explicit confirmation state naming the booked time. A form that silently failed validation looks a lot like one that worked: the page may stay on the form with an inline error below the fold. If no confirmation state appears, re-read the page, look for validation messages, and tell the user exactly what happened instead of reporting a booking.
