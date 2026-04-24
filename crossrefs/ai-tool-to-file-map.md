# AI Tool to File Map

| Tool | Primary File | Secondary Files | Central Template | Notes |
|---|---|---|---|---|
| Codex | `AGENTS.md` | none | `adapters/AGENTS.template.md` | Repo instruction front gate |
| GitHub Copilot | `.github/copilot-instructions.md` | `.github/instructions/*.instructions.md` | `adapters/copilot-instructions.template.md` | Repo custom instructions |
| Claude Code | `CLAUDE.md` | `.claude/*` | `adapters/CLAUDE.template.md` | Long session memory |
| Gemini CLI | `GEMINI.md` | optional context files | `adapters/GEMINI.template.md` | CLI context |
| Antigravity | `ANTIGRAVITY.md` | none | `adapters/ANTIGRAVITY.template.md` | IDE agent |
| Cursor | `.cursorrules` | `.cursor/rules` | `adapters/CURSOR.template.md` | Optional |
| Windsurf | `.windsurfrules` | none | `adapters/WINDSURF.template.md` | Optional |
| Cline | `.clinerules` | none | `adapters/CLINE.template.md` | Optional |
