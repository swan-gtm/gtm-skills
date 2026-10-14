# The kill job

A one-time scheduled job that stops every sequence still alive in one group at the cutoff, then reports. Arm it before approving or sending anything.

## Schedule

- Run once, at the cutoff, converted to UTC if the scheduler uses UTC. Check daylight saving on the cutoff date.
- Name it `Self-kill: <group name>` so anyone can find it.
- Owner: one person for a personal event, the team for a shared one. The owner receives the report.

## Hand-off instructions

Write these for someone who was not in the conversation:

1. **Context.** Who asked, which group (name and id), the cutoff, and why.
2. **Sweep at run time.** List every sequence in the group, paging to the end. Never use a stored list.
3. **Stop** every sequence that is active, queued, waiting on a connection or awaiting approval.
4. **Leave alone** sequences already finished, stopped or errored. Never touch a contact who replied.
5. **Verify.** List the group again and confirm none is still active. Retry failures once.
6. **Report once** to the owner: counts stopped, already finished, replied and failed; the group link; and the names of people who replied, since they need a human answer. If any failed to stop, create a task for the owner instead of only messaging.
7. **Never** create, send or edit outreach.

## Prefer stop over delete

Stop keeps the history and, on most platforms, can be resumed. Delete only if the owner asked. Where a stop on a not-yet-started sequence is permanent, that is acceptable for a kill, but say so in the report.

## If the cutoff moves

Update the existing job's schedule instead of creating a second one. If it already ran, create a new group and job.

## If you cannot schedule natively

Use an external scheduler that calls the platform's API with the group id and the same steps above. State in the report that it runs outside the platform, and who owns the key.
