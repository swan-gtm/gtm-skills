# Duplicate and conflict decisions

## Confidence ladder

- High confidence: exact normalized verified work email or canonical profile URL.
- Medium confidence: full name plus exact company domain and no competing match.
- Low confidence: full name plus company name, nickname, stale employer, or multiple matches.

Only high and medium confidence support automatic fill-if-empty updates. Low confidence is always ambiguous.

## Existing value decisions

- Destination empty, source verified: fill after approval.
- Destination and source equal after normalization: no-op.
- Both non-empty and different: conflict-review; never overwrite automatically.
- Source probable or catch-all, destination non-empty: preserve destination.
- Source says invalid but destination contains the value: flag for review; do not erase it in this workflow.

## In-batch duplicates

Deduplicate the proposed creates before contacting the CRM. Choose the row with the strongest identity and provenance as canonical, and link the remaining source rows to its decision.

## Ambiguous write outcome

If a create times out:

1. search by verified email and profile URL;
2. check for the sync-run identifier if stored;
3. if exactly one matching record has the intended fields, classify as created;
4. if none exists and the connector confirms rejection, retry once within scope;
5. otherwise stop and request review.
