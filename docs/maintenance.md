# Maintenance

Maintaining a resource collection is more than checking whether a link still opens. A course can become paid, a repository can stop working, or two resources can begin teaching the same thing.

We use automation to find these cases. However, a person still opens the resource, checks what changed, and decides what belongs in the collection.

## Source of truth

`data/resources.yaml` stores our categories and resources. We generate the README status, category table, and category-page resource tables from this file. However, we write the introductions and learning paths ourselves because they need our explanation and judgment.

After changing the data:

```bash
python scripts/validate_resources.py
python scripts/generate_readme.py
python scripts/generate_readme.py --check
python scripts/check_internal_links.py
```

## Weekly link check

The link workflow runs every Saturday at 09:30 Asia/Jakarta, which is 02:30 UTC. It records failures, redirects, and websites that block an automated request. When it finds a problem, it creates or updates an issue named `Broken Resource Links`. It never deletes a resource.

For example, an HTTP 401, 403, or 429 does not always mean the resource is gone. Some documentation websites block automated clients. That is why we send these results for manual review instead of treating them as dead links.

## Monthly discovery

GitHub Actions cron cannot express “the first Saturday in Asia/Jakarta” reliably as one portable expression. The workflow runs on the weekly Saturday schedule, then continues only when the Jakarta calendar day is 1 through 7. A manual run bypasses the guard.

The discovery script uses targeted GitHub Search API queries and removes URLs we already have. It writes `Monthly Resource Review - YYYY-MM` as an issue. We receive a smaller candidate list without adding anything automatically.

The built-in `GITHUB_TOKEN` is enough for the launch workflow. We do not require a broader web-search provider. If we add one later, we should first document its secret name, price, rate limits, data handling, and fallback behavior.

## Quarterly curation

The quarterly workflow uses the same first-Saturday guard and continues only in January, April, July, and October. It proposes review work for:

- stale `last_verified` dates
- resources already marked `needs-review` or `archived`
- paid or account-dependent access that may have changed
- categories whose size or scope needs human review

Before closing the issue, we should also check broken notebooks, deprecated APIs, inactive repositories, duplicate coverage, and new areas with enough resources we can test or apply.

## Issue behavior

Scheduled jobs create or update review issues. We do not need a new broken-link issue every week, so repeated checks update the existing issue. Monthly and quarterly reports use a period-specific title so we can follow the previous decisions.

## Security

The workflows use minimum permissions and pin third-party actions to commit SHAs. Secrets are only read from GitHub Actions. Pull requests do not receive write permissions for discovery or review workflows.

