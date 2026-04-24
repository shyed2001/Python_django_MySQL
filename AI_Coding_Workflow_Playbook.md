# AI_Coding_Workflow_Playbook (SOP)
**Version:** 1.0  
**Last updated:** 2025-12-19 09:54 PM (Asia/Dhaka)  
**Purpose:** A single, repeatable operating system for coding with AI—fast **and** safe, without “vibe-coding chaos.”

---

## References (videos used to build this SOP)
```text
Marina Wyss — 99% Of People Don't Know The RIGHT WAY to Code with AI
https://www.youtube.com/watch?v=dzinqNTacbc

Visual Studio Code — Essential AI prompts for developers
https://www.youtube.com/watch?v=H3M95i4iS5c

ForrestKnight — Everything You Need to Know About Coding with AI // NOT vibe coding
https://www.youtube.com/watch?v=5fhcklZe-qE

Theo (t3.gg) — How I code with AI right now
https://www.youtube.com/watch?v=-g1yKRo5XtY

Dan Koe — How To Use AI Better Than 99% Of People (This Changed My Life)
https://www.youtube.com/watch?v=xgpLjLHB5sA

Pat Spizzo — Frameworks Die. These 5 Principles Don't.
https://www.youtube.com/watch?v=67Z00QLfYI0

DevForge — AI Replaced 80% of Coding, Only These 5 Skills Are Left
https://www.youtube.com/watch?v=wTT8QaE0nnw

Abdu Taviq — Frontend Frameworks Core Concepts: States, Side Effects, Change Detection, and More
https://www.youtube.com/watch?v=U7EcCfdqbNw

Abdu Taviq — Frontend Architecture Concepts | Just Enough
https://www.youtube.com/watch?v=s9dBWi4u5PY
```
---

## The mindset (non-negotiables)
- **AI is a force-multiplier, not a replacement brain.** You own the architecture, risk, and correctness.
- **Treat AI like an intern + compiler.** It can type fast, and hallucinate fast. Management is the job.
- **Small batches win.** AI loves sprint-sized tasks: scoped, testable, reversible.
- **Guardrails > vibes.** If you can’t verify it quickly, it’s not “done.”

---

## Roles & modes (use the right tool for the job)
### Mode 1 — Tutor (Learning / unfamiliar terrain)
- Autocomplete **OFF**
- Ask for explanations, docs summaries, “teach me one concept at a time”.
- Goal: build understanding and mental models.

### Mode 2 — Assistant (Productivity / familiar terrain)
- Autocomplete **ON** for boilerplate, renames, tests, scaffolding.
- If you don’t understand what it wrote, you immediately drop back to **Tutor**.

### Mode 3 — Agent (Delegation / you’re tired or stuck)
- Give a plan-first mandate, strict constraints, and a verification harness.
- You act as manager: approve plan, review diffs, run tests, accept/reject.

### Sub-agents (optional)
- Spin off narrow “investigators” for: library research, bug reproduction, performance profiling.
- Keep the main thread clean (context is money and sanity).

---

## Project “Source of Truth” files (stop repeating yourself)
Put these at the project root. They are your *institutional memory*.

### 1) `agents.md` — the agent README (static context)
Create once; update as the project evolves.

**Template:**
```md
# Project: <Name>

## Tech stack
- Language:
- Framework:
- DB:
- Runtime:
- Build tools:

## Repo map
- /src
- /tests
- /docs
- /scripts

## Architecture
- Boundaries / layers:
- Data flow summary:
- Error handling rules:

## Style rules
- Formatting:
- Naming:
- “No cleverness” rules:

## Gotchas
- Known fragile modules:
- Rate limits:
- Env vars:
- Timezones:
```

### 2) `progress.md` — context compaction (dynamic)
Use when starting a fresh task or new chat context.

**Template:**
```md
# Progress snapshot

## Goal
<what “done” means>

## Current approach
<what we’re building + why>

## Completed
- [x] ...

## Blockers / failures
- [ ] ... (include error text + where)

## Next steps
1) ...
2) ...
```

### 3) `tutor.md` — teaching behavior (for learning sessions)
```md
You are my programming tutor.
- Ask questions before answering.
- Teach one concept at a time.
- If I’m wrong, nudge me; don’t immediately solve it.
- Show small examples, then let me try.
```

### 4) Project rules file (`.cursorrules`, `warp.md`, etc.)
Use for tool-specific “always follow these rules” constraints:
- allowed dependencies
- branch naming conventions
- API patterns
- database schema conventions
- security rules

---

## The core workflow: Plan → Execute → Verify → Review
This is the main SOP loop. Run it like a factory line.

### Step 0 — Define the ticket (1–2 paragraphs)
- What’s the change?
- What files are in scope?
- What’s out of scope?
- What does success look like (tests, UI behavior, perf)?

### Step 1 — Context injection (minimum necessary)
Provide:
- `agents.md` (always)
- relevant code snippets OR file list
- current error logs (if debugging)
- constraints (no new deps, keep API stable, etc.)

### Step 2 — Planning gate (no code yet)
Tell the AI to output:
- Implementation steps
- Risks / edge cases
- “Quick tests” to validate each step
- 2–3 approaches with pros/cons (when design choices exist)

**Approval rule:** You (human) approve plan before any code is written.

### Step 3 — Execution (small diffs, scoped edits)
- Limit edits to named files.
- Ask for incremental commits/patches.
- Avoid sweeping refactors unless explicitly requested.

### Step 4 — Verification (harness runs)
Run your harness (choose what applies):
- unit tests / integration tests
- typecheck (e.g., `tsc`)
- lint / format check
- quick “dry-run” scripts
- logs at debug level for the touched flows

### Step 5 — Review (PR mindset)
- Read diff line-by-line.
- Ask: “Why this pattern? What are failure modes? What breaks backward compatibility?”
- Apply security checklist before merge.

### Step 6 — Checkpoint (Git discipline)
- Commit early, commit often—each commit is a lighthouse for rollback.
- Use branches/worktrees for risky changes.
- If the agent derails: **throw away the branch**. Code is cheap; confusion is expensive.

---

## Prompt playbook (copy/paste patterns)
### A) Q&A Strategy Prompt (force requirements discovery)
```text
Before proposing a solution, interview me.
Ask only yes/no questions first (max 12).
Then propose 2–3 approaches with pros/cons.
Then wait for my approval before writing any code.
```

### B) Pros & Cons Prompt (force trade-off clarity)
```text
Give me 3 ways to implement this.
For each: pros, cons, risks, and when NOT to use it.
Then recommend one based on my constraints: <constraints>.
```

### C) Stepwise Prompt (controlled execution)
```text
Break this into steps.
Do step 1 only.
Stop and wait for the keyword: NEXT.
Do not proceed without NEXT.
```

### D) Role Prompt (tutor / reviewer / security auditor)
```text
Act as a senior code reviewer.
Be skeptical. Point out edge cases, performance traps, security risks.
Suggest minimal diffs and clear tests.
```

### E) Planning Template (ForrestKnight / Theo style)
```text
Output a plan.md first (no code):
- data flow
- key functions
- files to touch
- test plan
- risks
If you hit ambiguity: stop and output options + trade-offs.
```

### F) Meta-prompt (Dan Koe style: prompt that builds prompts)
```text
First: extract instructions/rules for doing this task well.
Second: interview me to gather missing context.
Third: produce an action plan.
Fourth: guide execution step-by-step with verification checks.
```

---

## Testing SOP (TDD option)
Use when correctness matters and specs are clear.

1) **Write tests first** to describe expected behavior (no implementation mocking).
2) Run tests → confirm red (fail).
3) Implement code to pass tests.
4) Do not modify tests unless the spec itself changed (and document why).
5) Add regression tests for every bug you fix.

**AI instruction snippet:**
```text
Write tests first based on these I/O examples: <examples>.
Do NOT write the implementation yet.
Then stop and wait.
```

---

## Debugging SOP (fast, surgical)
1) Reproduce reliably (single command).
2) Add debug logs (structured if possible).
3) Localize: identify the smallest failing unit.
4) Hypothesize: list 2–3 plausible root causes.
5) Test hypotheses (one change at a time).
6) Fix + regression test.

**Minimum debug payload to AI:**
- exact error text
- repro steps
- relevant code region
- expected vs actual
- environment details (OS, runtime, versions)

---

## Context management SOP (avoid context rot)
- Start a new task? **New context.**
- Before switching: write `progress.md` snapshot.
- Keep conversations sprint-sized; avoid meandering mega-threads.
- When you must keep a long thread: periodically compress into `progress.md` and continue from that.

---

## Architecture SOP (timeless integration principles)
Use these as design “quality gates” (Pat Spizzo core principles):
- **Narrow interface first:** fewer endpoints, single responsibility.
- **Versioning is relationships:** breaking changes get a new version; backward compat is a feature.
- **Make invalid states impossible:** state machines > many booleans; schema constraints at boundaries.
- **Idempotency is mandatory:** safe retries, dedupe keys, upserts where appropriate.
- **Optimize for debuggability:** correlation IDs, structured logs, precise errors.

---

## Frontend SOP (framework-agnostic mental model)
No matter the framework, you’re managing:
- **State** (local + derived)
- **Communication** (props/events + shared state/store)
- **Side effects** (async work that updates state)
- **Change detection** (when/what re-renders)

Also: separate **Components** (UI atoms) from **Containers** (orchestration).
Use **Services + Adapters** to isolate third-party tech and keep swapping costs low.

---

## Security & Code Review checklist (because AI loves foot-guns)
- Secrets: no keys in code, logs, or commits
- AuthZ: authorization checks on every protected action (not just auth)
- Input validation: boundaries first (API, DB)
- Injection risks: SQL/command/template injection review
- Error handling: no leaking sensitive internals to users
- Dependency risk: new deps justified, pinned, reviewed
- Observability: logging + correlation IDs where needed

---

## The “Five Human Moats” (skills to keep sharp)
AI can write code. You must still own:
- system design
- product/UX judgment
- performance debugging
- security review
- legacy integration + real-world constraints

---

## Quickstart (one-screen operating ritual)
1) Update `agents.md` (or confirm it’s accurate)
2) Create a ticket description (goal + constraints)
3) Ask AI for **plan only**
4) Approve plan
5) Execute in small diffs
6) Run harness (tests/typecheck/lint)
7) Review diff line-by-line
8) Commit + tag checkpoint
9) Write `progress.md` snapshot if continuing later

---

## Footnote
This SOP is a structured, “transcript-style paraphrase” merged from the referenced videos listed at the top.
