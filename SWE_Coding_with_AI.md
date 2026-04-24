# SWE_Coding_with_AI
**Version:** 1.0  
**Last updated:** 2025-12-25 04:54 PM (Asia/Dhaka)  
**Scope:** Day-to-day engineering-grade coding with AI (context, planning, tests, debugging, security, review).

---

## 1) The only loop you should run
**Plan → Execute → Verify → Review → Checkpoint**

- Plan: steps, touched files, risks, tests (NO code yet)
- Execute: small diffs, scoped edits
- Verify: tests + typecheck + lint + smoke
- Review: PR mindset, edge cases, failure modes
- Checkpoint: commit + update `active_context.md`

---

## 2) Context engineering (stop repeating yourself)
Create:
- `agents.md` (stack, architecture, style, gotchas)
- `active_context.md` (decisions, progress, next steps)
- `progress.md` (compaction snapshot)

### Cursor rules (example)
Cursor rules live under `.cursor/rules`.  
Docs: https://cursor.com/docs/context/rules  

---

## 3) Spec-driven coding (determinism > vibes)
- GitHub Spec Kit: https://github.com/github/spec-kit  
- Spec-driven workflow article: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/  

---

## 4) MCP (tool-connected agents) — optional but powerful
- MCP spec: https://modelcontextprotocol.io/specification/2025-06-18  
Use for filesystem/git/db tooling, but apply least-privilege and auth discipline.

---

## 5) Testing SOP (TDD option)
1) tests first
2) run → confirm red
3) implement minimal code
4) regression test per bug

**Prompt**
```text
Write tests first for these scenarios: <examples>.
Do not write implementation.
Stop after tests.
```
---

## 6) Debugging SOP
1) reproduce
2) add debug logs
3) list 2–3 hypotheses
4) test one at a time
5) fix + regression test
6) clean up logs

---

## 7) Code review SOP
- Google review guidance: https://google.github.io/eng-practices/review/  
- Standard: https://google.github.io/eng-practices/review/reviewer/standard.html  

Use AI to: summarize diffs, spot missing tests, suggest edge cases.
Humans decide merge.

---

## 8) Security SOP (OWASP baseline)
- OWASP Top 10 (2021): https://owasp.org/Top10/2021/  

Minimum checks per PR:
- no secrets in code/logs
- authZ checks for protected actions
- boundary validation
- injection risks (SQL/command/template)
- safe dependency usage
- safe errors (no leakage)

**Prompt**
```text
Audit this diff for OWASP Top 10 risks (injection, broken access control, secrets leakage, insecure defaults).
Propose minimal fixes and tests.
```
---

## 9) Branching & checkpoints
GitHub Flow: https://docs.github.com/get-started/quickstart/github-flow  

Rules:
- short-lived branches
- small PRs
- harness green before merge
