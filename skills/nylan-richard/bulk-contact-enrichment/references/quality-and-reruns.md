# Quality classes and rerun policy

Normalize provider-specific statuses into operational classes.

## Result classes

- Verified: passed the provider's strongest deliverability or identity check.
- Probable: good evidence but below the verified threshold.
- Catch-all or ambiguous: domain or source cannot prove the individual address.
- Invalid: evidence says the value should not be used.
- No match: no approved value was found for the submitted identity.
- Insufficient identity: the input lacked enough evidence for a reliable lookup.
- Operational error: authentication, rate limit, timeout, schema, or provider failure.

No match, insufficient identity, and operational error are different outcomes. Keep them separate in metrics and rerun decisions.

## Retry rules

- Schema or validation error: fix the request; do not count as a provider miss.
- Authentication error: stop and ask the user to reconnect.
- Clear transient failure with no accepted job: retry once within the approved scope.
- Timeout after a job may have been accepted: reconcile the original job identifier before any retry.
- No match: rerun only through a deliberately approved alternate source or with improved identity data.
- Invalid result: do not retry the same source with the same input.

## Quality report

Report coverage using eligible rows as the denominator and disclose exclusions. A 70% match rate over 700 eligible rows is not 70% coverage of a 1,000-row file.
