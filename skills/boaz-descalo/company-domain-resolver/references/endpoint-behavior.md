# Clearbit autocomplete endpoint behavior

```
GET https://autocomplete.clearbit.com/v1/companies/suggest?query=<url-encoded name>
```

- **No API key, no auth header, no account.** Just a GET.
- Returns a JSON array of **up to 5** matches, best-guess first:
  `[{"name": "Ramp", "domain": "ramp.com", "logo": null}, ...]`
- No match returns `[]` with HTTP 200, not a 404.
- `logo` is **null in practice** — do not promise logos off this endpoint.
  If a logo is needed, fall back to
  `https://www.google.com/s2/favicons?domain=<domain>&sz=128` and tell the
  user it's a favicon, not a brand asset.
- Undocumented and unsupported. It is a typeahead for a signup form, not a
  contracted data API. Assume no SLA, keep volume modest, pace requests, and
  never present its output as authoritative without the confidence column.
- Quoting a multi-word query (`?query="bright data"`) makes no difference;
  don't bother.

## Two things that will burn you

1. **Legal suffixes wreck results.** `Stripe Inc.` returns `stripe-inc.jp`
   (wrong company). `Bright Data Ltd` returns `[]`. `Stripe` and
   `Bright Data` both resolve correctly. Always strip trailing
   `Inc / Ltd / LLC / GmbH / AG / Corp / Holdings / Group` before querying.
   The resolver script does this automatically.
2. **Common names silently return the wrong company.** `Clay` returns five
   Clayton-somethings, no Clay. The top result is always *something*, never
   an error. This is why every row gets a confidence label — never hand back
   a bare domain list.

## Worked single-lookup example

For one or two names, skip the script: fetch the endpoint directly with your
agent's web-fetch tool and report matches inline. `Harvest` returns two
results literally named "Harvest" — `getharvest.com` (the time-tracking
tool) and `harvest.org` (a church ministry) — alongside `harvesthosts.com`,
`harvestright.com`, and `harvesttotable.com`. The index cannot tell
same-named companies apart, and note the `get` prefix on the real one: say
which is which and let the user confirm. (The batch script strips common
domain prefixes like `get`/`try`/`join` when matching, so `getharvest.com`
still scores as a name match for "Harvest".)

## Blocked-network environments

Some sandboxed agent environments block direct HTTP to this host (a proxy
403 on CONNECT). Plan for it:

- Use your agent's web-fetch tool to hit the endpoint — that path usually
  works when raw sockets don't.
- Use the shell only for local file work (planning, scoring, CSV writing).
- The resolver script's `fetch` subcommand tries direct HTTP first and exits
  with a clear message if blocked, so it still works in environments that do
  have network (e.g. a laptop CLI agent).
- When falling back to web-fetch, batch **5–8 requests in parallel**, then
  move to the next batch. Don't fire 50 at once.
