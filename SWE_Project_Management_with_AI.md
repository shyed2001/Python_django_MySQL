# SWE_Project_Management_with_AI
**Version:** 1.0  
**Last updated:** 2025-12-25 04:54 PM (Asia/Dhaka)  
**Scope:** Execution governance for SWE/SWD/R&D projects using AI (cadence, backlog, risk, quality, release).

---

## 1) Management philosophy (run it like a system)
- **Project management = cadence + governance + visibility.**
- AI accelerates execution; humans own prioritization, risk acceptance, and release decisions.
- Aim: **reduce uncertainty every week** (requirements, tech, timeline, risk).

**References:**  
- Agile Manifesto: https://agilemanifesto.org/  
- Scrum Guide 2020: https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf  

---

## 2) AI roles + human approval gates
### AI roles
- Backlog assistant (slicing, acceptance criteria, dependency mapping)
- Tech lead assistant (design options, risks, implementation sequence)
- QA assistant (test plans, regression tests)
- Docs/comms assistant (meeting notes, status, release notes)

### Mandatory approval gates
Require human approval for:
- schema migrations
- auth/authz changes
- new dependencies
- CI/CD and infra changes
- multi-file refactors

---

## 3) Operating cadence (weekly rhythm)
### Recommended cadence
- Backlog grooming (30–60 min)
- Sprint planning (60–90 min)
- Daily sync (10–15 min)
- Demo/review (30–60 min)
- Retro (30–45 min)

Scrum reference: https://scrumguides.org/docs/scrumguide/v2020/2020-Scrum-Guide-US.pdf  

---

## 4) Backlog management (AI-assisted)
### Story slicing rules
- Stories are “thin” (1–2 days max)
- Every story includes: acceptance criteria + test plan hints + out-of-scope

**Prompt**
```text
Split this epic into 5–12 user stories.
Each story must include acceptance criteria (Given/When/Then), risks, and a minimal test plan.
```
---

## 5) Risk management (top-10 risk register)
Track:
- Product risk
- Technical risk
- Security risk
- Delivery risk
- Ops risk

**Prompt**
```text
Create a risk register.
For each risk: likelihood, impact, early warning signals, mitigation, contingency.
```
---

## 6) Execution governance (Git + review + release)
### Branching
Use short-lived branches + PR review (GitHub Flow):  
- https://docs.github.com/get-started/quickstart/github-flow  

### Code review standards
Use Google Engineering Practices guidance:  
- Overview: https://google.github.io/eng-practices/review/  
- Standard: https://google.github.io/eng-practices/review/reviewer/standard.html  

---

## 7) Stakeholder reporting (no surprises)
### Weekly status template
```md
# Weekly Status — <Project>
## Sprint goal
## Shipped this week
## In progress
## Risks / blockers (with mitigation)
## Metrics (lead time, bugs, test pass rate)
## Next week priorities
```

**Prompt**
```text
Rewrite this update for executives:
- concise, clear risks, clear asks
Text: <paste>
```
---

## 8) Metrics (simple, actionable)
- Lead time (ticket → merged)
- Deployment frequency
- Change failure rate
- MTTR
- Test pass rate / flaky tests count
- Security findings per release

---

## 9) Checklists
### Pre-sprint
- [ ] Sprint goal written
- [ ] Stories have acceptance criteria + tests planned
- [ ] Risks reviewed + owners assigned
- [ ] CI is green

### Pre-release
- [ ] Tests passing
- [ ] Security review done
- [ ] Rollback plan documented
- [ ] Monitoring/alerts ready
- [ ] Release notes written
