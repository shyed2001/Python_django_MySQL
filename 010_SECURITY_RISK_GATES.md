# Security Risk Gates

## Must Ask Before

- Global installs
- MCP config changes
- Hook changes
- Lockfile replacement
- Package-manager migration
- Credential/account changes
- Destructive edits
- Broad rewrites
- Production changes
- Remote server changes
- Git push or force push

## Protected Files

- .env
- .env.*
- secrets.*
- id_rsa
- id_ed25519
- known_hosts
- config files containing tokens
- deployment keys
- production configs
- MCP configs
- Git hooks
