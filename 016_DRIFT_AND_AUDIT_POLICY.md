# Drift and Audit Policy

## Drift Types

- Missing instruction file
- Outdated pointer block
- Conflicting policy
- Wrong path
- Wrong remote URL
- Missing crossref
- Missing registry card
- Missing MCP mapping
- Missing server mapping

## Reports

- `reports/repo-drift-report.md`
- `reports/broken-link-report.md`
- `logs/drift-log.jsonl`

## Fix Rule

Fix drift by append-only pointer update first.
Do not overwrite full repo instruction files without permission.
