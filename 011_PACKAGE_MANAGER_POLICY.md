# Package Manager Policy

## Detection

- pnpm-lock.yaml -> pnpm
- package-lock.json -> npm
- yarn.lock -> yarn
- uv.lock -> uv
- pyproject.toml -> Python project tooling
- requirements.txt -> pip-compatible workflow

## Rule

Never replace lockfiles.
Never migrate package managers without permission.
Respect local conventions first.
