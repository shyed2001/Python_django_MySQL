# SWE_Project_Planning_with_AI
**Version:** 1.0  
**Last updated:** 2025-12-25 04:54 PM (Asia/Dhaka)  
**Scope:** Planning & design artifacts for SWE/SWD/R&D projects using AI (ideation → PRD → architecture plan).

---

## 1) Planning philosophy (truth, not vibes)
- **Planning is design + constraints.** AI generates options; humans pick trade-offs.
- **SLC v1.0 (Simple, Lovable, Complete)** beats a bloated “MVP.”
- **Plan-gate execution:** no multi-file code changes until the plan is approved.
- **Working software is the primary measure of progress**, but planning prevents shipping the wrong thing.

**References:**  
- Agile Manifesto: https://agilemanifesto.org/  
- Agile Principles: https://agilemanifesto.org/principles.html  
- Scrum Guide 2020: https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf  

---

## 2) AI roles during planning (pick the right mode)
### Mode A — Research Analyst (market + competitors)
- competitor feature map, pricing, positioning
- “strong demand + weak UX” opportunities
- compliance constraints and local-market factors

### Mode B — Brutal Critic (risk + blind spots)
- attack assumptions
- list failure modes
- propose mitigation + “kill criteria”

### Mode C — PRD Drafter (structure and completeness)
AI drafts. You own:
- scope boundaries
- success metrics
- non-goals
- constraints and risk acceptance

### Mode D — Architect’s Assistant
AI proposes: schema/API options, infra tradeoffs; you set the north-star architecture.

---

## 3) Planning workflow (Phase 0 → Phase 2)
### Phase 0 — Idea & validation (What/Why)
**Outcome:** one-page concept brief + evidence of demand.

**Steps**
1. Market scan (competitors, gaps, target segment)
2. Problem statement (1 paragraph)
3. Persona + job-to-be-done
4. SLC v1.0 scope (must-have / nice-to-have / out-of-scope)
5. Success metrics (3–5 measurable)
6. Top 5 risks + kill criteria

**Checklist**
- [ ] Persona + job-to-be-done written
- [ ] SLC scope defined + NOT-in-scope list written
- [ ] 3–5 success metrics defined
- [ ] Top 5 risks + kill criteria defined

---

### Phase 1 — Requirements (PRD + user stories)
**Outcome:** PRD v1 + testable acceptance criteria.

**Steps**
1. PRD skeleton (AI drafts; you refine)
2. Convert into user stories (“As a…, I want…, so that…”)
3. Acceptance criteria (Given/When/Then)
4. Non-functional requirements (security, performance, compliance, observability)
5. Dependencies + assumptions

**Minimum PRD template**
```md
# PRD: <Product/Feature>
## Problem
## Target users
## Goals (measurable)
## Non-goals (explicit out-of-scope)
## User journeys (happy path + 3 failure paths)
## User stories
## Acceptance criteria (Given/When/Then)
## Non-functional requirements
- Security
- Performance budgets
- Availability/reliability
- Privacy/compliance
- Observability/logging
## Risks + mitigations
## Milestones
## Open questions
```

**Checklist**
- [ ] PRD reviewed and signed off
- [ ] Acceptance criteria are measurable/testable
- [ ] Non-goals present (scope creep shield)

---

### Phase 2 — Architecture & plan-of-record (How)
**Outcome:** plan.md + ADRs + deliverable map.

**Steps**
1. System boundaries (frontend/back/services/data/integrations)
2. Data model (tables/entities, relationships, constraints)
3. Narrow API surface (few endpoints; each does one thing)
4. Branching/release approach
5. plan.md: milestones → tasks → verification

**Branching reference:** GitHub Flow  
- https://docs.github.com/get-started/quickstart/github-flow  

**ADR template**
```md
# ADR-0001: <Decision title>
## Context
## Decision
## Options considered
## Consequences
## Migration / rollout plan
```

**Checklist**
- [ ] Boundary sketch exists
- [ ] Data model defined
- [ ] API endpoints defined
- [ ] Plan includes verification (tests/harness)
- [ ] Stop conditions defined

---

## 4) Planning artifacts (definition of “ready to build”)
- `agents.md` (project rules & architecture summary)
- `active_context.md` (current plan/decisions/next steps)
- `plan.md` (execution plan per milestone)
- PRD + ADRs
- Risk register (top 10 risks + mitigations)
- Verification harness commands list

---

## 5) Planning prompts (copy/paste)
### Requirements interview (Yes/No first)
```text
Before writing a PRD, interview me with up to 12 yes/no questions.
Then draft the PRD with explicit non-goals and measurable success metrics.
```

### Brutal critic
```text
Act as a brutal critic.
List the top 10 reasons this project could fail (product, engineering, security, ops).
Then propose mitigations and kill criteria.
```

### Plan gate (no code)
```text
Write plan.md only (no code).
Include: files/modules to create, milestones, risks, test plan, rollback plan.
Stop and wait for approval.
```
