# SDLC-Pipe — Master Build Prompt (v2)

> **How to use:** Start a fresh session in this project and paste everything between "PROMPT START" and "PROMPT END" into it. Fill in the `‹placeholders›` first, or leave them for the builder to ask about.
> Part B (at the end) holds the design rationale and recommendations.
>
> **v2 changes:** Solution Design (HLD) now comes before BMAD Planning. BMAD drives every stage once Mockups, BRD and HLD are ready. Build is broken into explicit coding steps. The tech stack is fixed: SQLite, Node.js, React, REST + OpenAPI. There are now two pipeline types, **Transformation Project** and **Change Request (CR)**, and each CR or CR bundle runs its own full lifecycle.

---

## PART A — PROMPT START

### 1. Role and objective

You are a senior full-stack engineer and delivery architect. Build **SDLC-Pipe**, a lightweight web application that tracks, visualizes and governs the **full software delivery lifecycle** of applications.

SDLC-Pipe supports **two types of delivery pipeline**, managed separately but using the same engine:

1. **Transformation Project pipeline**: the end-to-end build of a new application, from initiation to go-live and hypercare.
2. **Change Request (CR) pipeline**: after go-live, each CR (or a bundle of CRs grouped into a CR release) runs **its own lifecycle**, which mirrors the transformation stages in a delta form (Delta Mockup → Delta BRD → Delta HLD → BMAD → Build → Test → Release).

The first application is **PMS (Payroll Management System)**, with four modules: EIMS (Employee Information), AMS (Attendance), LMS (Leave) and SMS (Salary). SDLC-Pipe must stay **application-agnostic**: PMS is seed data, not hard-coded logic.

For any stakeholder, SDLC-Pipe must answer these questions in under 10 seconds:

1. Where is this pipeline right now? (current stage, health, % complete)
2. What has been done, by whom, and when? (completed stages, milestones, artifacts, authors, completion dates)
3. What comes next, and is anything blocking it? (upcoming stages, gates, pending reviews, open gaps)
4. Do the artifacts agree with each other? (review findings and gap analysis between consecutive stages)
5. For a live application: which CRs are in flight, at what stage, and which baseline artifacts do they change?

### 2. Before you write code

1. Read this whole prompt. Ask me up to 8 clarifying questions in one batch, covering only what blocks the design.
2. Propose: (a) the domain model and SQLite schema, (b) a screen map, (c) MVP scope versus later phases, and (d) the folder structure. Wait for my approval.
3. Build iteratively, MVP first. Each increment must run end-to-end and come with seed data.

### 3. Tech stack (fixed)

| Layer | Choice |
|---|---|
| Frontend | **React JS** (Vite), React Router, a light component library or Tailwind, and a charting library (e.g. Recharts) |
| Backend | **Node.js** (Express), with a clear layer structure: routes → controllers → services (domain rules) → repositories |
| Database | **SQLite**, with versioned migrations and a seed script (e.g. Knex or Prisma, or better-sqlite3 with plain SQL migrations) |
| API | **REST + OpenAPI 3** spec (Swagger UI served at `/api/docs`) |
| Files | Artifacts stored on the local file system (`/storage`) or referenced by URL; storage behind an interface so S3/SharePoint/Git can be added later |
| Run | `npm install && npm run dev` runs everything locally; `npm run seed` loads the PMS demo data |

### 4. Core domain model

```
Portfolio
 └── Application (long-lived product, e.g. PMS; has Modules: EIMS, AMS, LMS, SMS)
      ├── Baseline Artifact Register   (current approved version of every artifact)
      └── Pipeline  (type = TRANSFORMATION | CR)
           ├── Lifecycle Template       (stage blueprint for this pipeline type)
           ├── Stage
           │    ├── Gate                entry/exit criteria + approvers
           │    ├── Step                ordered steps inside a stage (e.g. coding steps, BMAD steps)
           │    └── Milestone
           │         └── Artifact
           │              ├── Version history
           │              ├── Review   (peer / stage-exit / cross-stage gap)
           │              └── Finding (Gap)
           ├── Trace Links (Requirement ↔ Design ↔ Story ↔ Code/PR ↔ Test ↔ Release)
           └── Activity Log (append-only)

CR pipeline extras:
   CR Pipeline ── contains 1..n Change Requests (single CR or CR bundle / release)
              └── baseline_ref: which approved artifact versions it starts from
```

**Key rule:** a **Transformation pipeline** creates the first **baseline** of an application's artifacts (BRD v1.0, HLD v1.0, PRD v1.0…). Each **CR pipeline** starts from that baseline, produces **delta artifacts**, and when it is released, **promotes them into a new baseline** (e.g. BRD v1.1). The Application page shows the transformation history and all CR pipelines together, but they are managed as separate pipelines.

#### Key entities and minimum attributes

| Entity | Key attributes |
|---|---|
| Application | id, code, name, description, owner, modules[], go_live_date, status (In Build / Live / Retired), health (RAG) |
| Pipeline | id, app_id, **type (TRANSFORMATION / CR)**, code (e.g. PMS-TX-01, PMS-CR-2027-03), name, template_id, baseline_ref (CR only), owner, planned_start/end, actual_start/end, status, health |
| ChangeRequest | id, pipeline_id (when assigned), title, requester, business_justification, modules[], type (Enhancement / Defect / Regulatory / Tech-debt), priority, size, status (intake), CAB decision, linked_baseline_items[] |
| LifecycleTemplate | id, name, pipeline_type, version, stages[], is_default |
| Stage | id, pipeline_id, name, sequence, **driven_by (Manual / BMAD)**, status, planned/actual dates, owner, % complete (derived) |
| Step | id, stage_id, name, sequence, bmad_agent (optional: Analyst / PM / UX / Architect / PO / SM / Dev / QA), status, assignee, planned/actual dates |
| Gate | id, stage_id, type (entry/exit), criteria[] (checklist), approvers[], decision (Pending / Passed / Passed-with-conditions / Failed), decided_by, decided_on |
| Milestone | id, stage_id, name, planned_date, actual_date, status |
| Artifact | id, code (e.g. PMS-BRD-001), name, type, pipeline_id, stage_id, milestone_id, module, is_delta (CR), base_artifact_id (CR), author, contributors[], reviewers[], current_version, status, planned_completion, actual_completion, location (file / URL / repo path), tags[], depends_on[] |
| ArtifactVersion | id, artifact_id, version, change_summary, author, created_on, file_ref/hash, is_baseline |
| Review | id, artifact_ids[], review_type, reviewers[], started_on, closed_on, verdict (Approved / Approved-with-comments / Rework) |
| Finding (Gap) | id, review_id, source_artifact, target_artifact, category (Missing / Inconsistent / Ambiguous / Out-of-scope / NFR gap), severity (Critical/High/Med/Low), description, owner, due_date, status (Open / In-progress / Resolved / Accepted-risk / Deferred-to-CR) |
| TraceLink | from_item (e.g. BRD-AMS-012), to_item (e.g. STORY-AMS-07), link_type (derives / implements / verifies / changes) |
| User / Role | name, email, roles: Sponsor, PM, BA, Architect, Dev Lead, Developer, QA Lead, DevOps, Business SME, CR Requester, CAB Member, Auditor, Admin |
| ActivityLog | who, action, entity, before/after (JSON), timestamp |

#### Status vocabularies (configurable)

- **Pipeline / Stage / Step / Milestone:** Not Started → In Progress → In Review → Completed | Blocked | On Hold | Skipped (N/A)
- **Artifact:** Planned → Draft → In Review → Rework → Approved (Baselined) → Superseded
- **CR intake** (before a CR joins a pipeline): Raised → Triaged → Impact Assessed → CAB: Approved / Rejected / Deferred → Assigned to CR Pipeline

### 5. Lifecycle templates

#### 5.1 Default Transformation template

Stages 0–3 are **foundation stages**, done manually with the organisation's templates. From Stage 4 onward, every stage is **BMAD-driven**, using Mockups, BRD and HLD as its inputs.

| # | Stage | Driven by | Steps / typical artifacts | Exit gate (examples) |
|---|---|---|---|---|
| 0 | **Initiation & Governance** | Manual | Project Charter, Stakeholder Register / RACI, **Document Templates** (BRD, HLD, Test plan…), Tooling setup | Templates finalized and approved |
| 1 | **Discovery & UX** | Manual | As-is process notes, **Mockups / Wireframes**, Clickable prototype | Mockups reviewed by business |
| 2 | **Business Requirements** | Manual | **BRD**, Business rules catalogue, Glossary | BRD signed off; Mockups ↔ BRD gap review closed |
| 3 | **Solution Design (HLD)** | Manual | **HLD**, logical data model, integration view, NFR & security approach, tech-stack decision (ADRs) | HLD approved; BRD ↔ HLD gap review closed. **Mockups + BRD + HLD baselined = "BMAD-ready"** |
| 4 | **BMAD Planning** | BMAD | Steps: **Project Brief** (Analyst) → **PRD** (PM) → **UX Spec** (UX) → **Architecture / detailed design** (Architect, refines HLD) → **PO validation & sharding** (PO) → **Epics & Stories** (SM) | PRD ↔ BRD coverage ≥ ‹95›%; Architecture ↔ HLD consistent; Stories ↔ PRD coverage = 100% |
| 5 | **Build** | BMAD | **Coding steps, repeated for each story / sprint:** ① Story drafted (SM) → ② Story validated / approved (PO) → ③ Dev environment & branch → ④ Implementation (Dev agent) → ⑤ Unit tests written & passing → ⑥ Self-check against story DoD → ⑦ Code review / PR review → ⑧ QA review (QA agent) → ⑨ Merge to main + CI build green → ⑩ Story marked Done | All stories Done; code-review & unit-test evidence present; CI green |
| 6 | **Testing** | BMAD | Test strategy, test cases (from stories' acceptance criteria), SIT report, performance / security report, defect log, **UAT sign-off** | Zero open Critical/High defects; UAT signed |
| 7 | **Release & Deployment** | BMAD | Release notes, deployment runbook, rollback plan, Go/No-Go checklist | Go/No-Go approved |
| 8 | **Go-Live & Hypercare** | BMAD | Cutover plan, hypercare log, incident register, handover to support. **Baseline v1.0 frozen** | Hypercare exit criteria met → Application status = Live |

> Show the **coding steps** in Stage 5 as a per-story progress strip (Story × Step matrix). Story status rolls up to the epic, epic status rolls up to the stage.

#### 5.2 Default CR template (for a single CR or a CR bundle)

The CR template mirrors the transformation stages as deltas against the current baseline:

| # | Stage | Driven by | Steps / typical artifacts | Exit gate |
|---|---|---|---|---|
| 0 | **CR Intake & Triage** | Manual | CR form(s), business justification, priority, bundling decision | CR(s) triaged and assigned to this pipeline |
| 1 | **Impact Analysis & CAB** | Manual | Impact analysis (auto-suggested from trace links), effort estimate, risk, **CAB decision** | CAB approved |
| 2 | **Delta UX** | Manual | Delta mockups (or "N/A – no UI change") | Business reviewed |
| 3 | **Delta Requirements** | Manual | **Delta BRD** (changed / new requirement IDs) | Signed off; Delta Mockup ↔ Delta BRD gaps closed |
| 4 | **Delta Solution Design** | Manual | **Delta HLD** / ADR (or N/A) | Approved → "BMAD-ready" |
| 5 | **BMAD Planning** | BMAD | Delta Brief → PRD update → Architecture update → Stories | Coverage of delta requirements = 100% |
| 6 | **Build** | BMAD | Same **coding steps** as transformation Stage 5 | All CR stories Done; CI green |
| 7 | **Testing** | BMAD | CR test cases, **regression test** of impacted areas, UAT | UAT signed; regression passed |
| 8 | **Release** | BMAD | Release notes, deployment, rollback plan | Go/No-Go approved |
| 9 | **Close & Re-baseline** | Manual | Post-release verification; **delta artifacts merged into a new baseline** (e.g. BRD v1.1, PRD v1.2) | Baseline updated, CR(s) closed |

Templates are editable by admins. Allow lighter CR variants, e.g. "Minor CR" with Delta UX and Delta HLD skipped by default.

### 6. Functional requirements

#### 6.1 Portfolio and application views
- **Portfolio:** one card per application, showing its status (In Build / Live), the active transformation pipeline stage, the number of CR pipelines in flight, RAG health, and the next milestone.
- **Application page**, with tabs:
  - **Transformation:** the pipeline dashboard (see 6.2).
  - **Change Requests:** CR intake backlog (Kanban by intake status), a list of CR pipelines (each with its own mini pipeline strip, stage, RAG and target release), and a CR calendar / release plan.
  - **Baseline:** the current approved version of every artifact, its version history, and which pipeline (Transformation or CR-xx) produced each version.

#### 6.2 Pipeline dashboard (same component for both pipeline types)
- **Pipeline strip:** a horizontal stage flow (like a CI/CD pipeline view). Each stage is colour-coded by status, shows its dates and a Manual/BMAD badge, and is clickable.
- KPI tiles: stages completed / total, artifacts approved / total, stories Done / total (Build stage), open gaps by severity, overdue items, days to go-live / release.
- **"Done / Doing / Next" panel:** recently completed artifacts and steps (with author and date), work in progress, and what is upcoming in the next ‹14› days.
- Planned vs actual timeline (Gantt-lite).
- Module filter (EIMS / AMS / LMS / SMS / All).

#### 6.3 Navigate anywhere
- A persistent left-hand tree: Application → Pipeline → Stage → Step / Milestone → Artifact → Version / Review.
- An interactive workflow map with upstream/downstream arrows, e.g. Mockups → BRD → HLD → Brief → PRD → Architecture → Stories → Code → Tests → Release.
- A breadcrumb (`PMS › Transformation › Stage 4 BMAD Planning › PRD › v1.3 › Review #2`) and a deep link (URL) for every node.
- Every node shows: status, owner/author, planned date, actual completion date, last updated, and open findings count.

#### 6.4 Stage detail
- Entry/exit gate checklist with approvers and decision.
- Ordered **steps**, each with its BMAD agent role where applicable. The Build stage shows the Story × Coding-Step matrix.
- Milestones and artifacts table (sortable and filterable by status, author, module, or overdue).
- A decisions log (lightweight ADR list).

#### 6.5 Artifact registry and viewer
- A searchable registry across all pipelines, with filters for type, pipeline type, stage, status, author, module and delta/baseline.
- Artifact page: metadata, versions (with baseline flags), reviews, upstream/downstream links, findings, and activity.
- Inline viewer for Markdown, PDF, images and HTML. External links for Figma, Git, SharePoint and similar.
- For CR delta artifacts: a side-by-side **baseline vs delta** view.

#### 6.6 Reviews and gap analysis between consecutive stages
- Peer reviews with a verdict.
- **Cross-stage gap reviews** for consecutive pairs:
  Mockups ↔ BRD, BRD ↔ HLD, HLD ↔ Architecture, BRD ↔ PRD, PRD ↔ Epics & Stories, Stories ↔ Code/PR, Stories ↔ Test cases.
  For CR pipelines: CR ↔ Delta BRD, Delta BRD ↔ Delta HLD, Delta BRD ↔ updated Stories, impacted items ↔ regression tests.
- A **coverage matrix** showing covered / partial / missing / orphan items and % coverage per pair.
- Findings become Gap records (severity, owner, due date) that roll up to the stage gate (e.g. "Exit blocked: 2 Critical gaps").
- **Optional AI-assisted gap analysis** (pluggable; off by default): send two artifacts to an LLM, get suggested findings, and have a human accept or reject each one.

#### 6.7 Traceability and impact
- Requirement IDs (e.g. `BRD-AMS-012`, `FR-LMS-004`, `STORY-SMS-21`, `TC-EIMS-033`) are parsed from Markdown front-matter or headings, or entered manually.
- An end-to-end trace: Business need → HLD component → FR → Story → PR/commit → Test → Release → CR(s) that changed it.
- **Impact view** (used in CR Stage 1): select a requirement or module to see every dependent artifact, story and test.

#### 6.8 Notifications and activity
- In-app notifications (email optional): review assigned, gate awaiting approval, overdue item, gap assigned, CR status change, CAB decision.
- An activity feed per pipeline and an immutable audit log.

#### 6.9 "Artifacts-as-code" sync (for BMAD outputs)
- Optional YAML front-matter in Markdown artifacts, plus a manifest (`sdlc-pipe.yaml`) per pipeline:

```yaml
artifact_code: PMS-PRD-001
type: PRD
pipeline: PMS-TX-01        # or PMS-CR-2027-03
stage: BMAD-Planning
step: PRD
module: ALL
author: ‹name›
status: In Review
version: 1.3
depends_on: [PMS-BRD-001, PMS-HLD-001, PMS-BRIEF-001]
```
- A **Sync** button (and `POST /api/pipelines/{id}/sync`) scans a local folder or repo (e.g. BMAD `docs/brief.md`, `docs/prd.md`, `docs/architecture.md`, `docs/stories/*.md`) and creates or updates artifacts, versions, story statuses and coding-step progress.

#### 6.10 Reports and export
- A one-click status report per pipeline or per application (PDF / Markdown / Excel) for steering committees and CAB meetings.
- Excel export of the artifact register, baseline register, traceability matrix and CR register.

#### 6.11 Administration
- Manage applications, modules, pipeline types, lifecycle templates (stages, steps, BMAD agent mapping, gate criteria), artifact types, status lists, users and roles.
- Role-based access: Viewer, Contributor, Reviewer, Approver, CAB Member, Admin. Read-only share links for executives.

### 7. Stakeholder views (role-based landing pages)

| Persona | Default landing view |
|---|---|
| Sponsor / Steering committee | Portfolio RAG, go-live countdown, CR throughput, top risks |
| Project / Delivery Manager | Pipeline strip, overdue items, gate readiness, 2-week plan |
| Business Analyst | My artifacts (BRD, Delta BRD), review comments, coverage |
| Architect | HLD / Architecture, NFR coverage, ADR log, BRD ↔ HLD gaps |
| Dev Lead / Developers | Story × Coding-Step matrix, PR / CI status |
| QA Lead | Test coverage vs stories, defects, UAT, regression status |
| Business SME / CR Requester | My CRs, CAB status, UAT tasks, release dates |
| CAB Member | CRs awaiting decision, with impact analysis |
| Auditor / PMO | Audit trail, approvals evidence, baseline history |

### 8. Non-functional requirements
- Lightweight: a single command to run locally, with seed data on first run.
- Dashboard loads in under 2 seconds with ~50 applications, ~200 pipelines and ~5,000 artifacts on SQLite.
- Auth: ‹local accounts with JWT for the POC; SSO-ready later›.
- Every state change is audit-logged. Soft deletes only.
- Accessibility: WCAG 2.1 AA. Status is never shown by colour alone (use icons and labels too).
- Business rules (status transitions, gate evaluation, coverage %, re-baselining) live in a service layer with unit tests.

### 9. API (indicative)
```
GET/POST   /api/apps                              GET  /api/apps/{id}/overview
GET/POST   /api/apps/{id}/pipelines?type=TRANSFORMATION|CR
GET        /api/pipelines/{id}/dashboard          PATCH /api/stages/{id}
GET/POST   /api/stages/{id}/steps                 PATCH /api/steps/{id}
GET/POST   /api/stages/{id}/milestones            POST /api/gates/{id}/decision
GET/POST   /api/artifacts (filters)               POST /api/artifacts/{id}/versions
GET        /api/apps/{id}/baseline                GET  /api/artifacts/{id}/trace
POST       /api/reviews                           POST /api/reviews/{id}/findings
GET        /api/pipelines/{id}/coverage?from=BRD&to=PRD
GET/POST   /api/apps/{id}/change-requests         POST /api/change-requests/{id}/cab-decision
POST       /api/pipelines/{id}/change-requests    (assign/bundle CRs into a CR pipeline)
GET        /api/change-requests/{id}/impact       POST /api/pipelines/{id}/rebaseline
POST       /api/pipelines/{id}/sync               GET  /api/pipelines/{id}/report?format=pdf|md|xlsx
GET        /api/activity?entity=&id=
```

### 10. Seed data: PMS (current real state)

**Application PMS, Transformation pipeline `PMS-TX-01`:**

| Stage | Status | Notes |
|---|---|---|
| 0 Initiation & Governance | **Completed** | Document templates finalized on ‹date› by ‹author› |
| 1 Discovery & UX | **Completed** | Mockups for EIMS / AMS / LMS / SMS designed on ‹date› by ‹author› |
| 2 Business Requirements | **In Progress** | BRD ‹x›% complete, owner ‹BA name›, target ‹date›; Mockups ↔ BRD gap review pending |
| 3 Solution Design (HLD) | Not Started | Planned ‹dates› |
| 4 BMAD Planning | Not Started | Starts when Mockups + BRD + HLD are baselined |
| 5 Build (coding steps) | Not Started | — |
| 6–8 Testing → Hypercare | Not Started | Target go-live ‹date› |

**Demo application (already live)** so the CR views are not empty: one completed transformation pipeline, a baseline register, 5 CRs in intake (various statuses), one **single-CR pipeline** in Build, and one **CR bundle pipeline** (3 CRs) in Delta Requirements.

### 11. Key screens (MVP)
1. Portfolio overview
2. Application page (Transformation / Change Requests / Baseline tabs)
3. Pipeline dashboard (strip + KPIs + Done/Doing/Next + timeline)
4. Tree navigator and workflow map
5. Stage detail (gates, steps, Story × Coding-Step matrix, milestones, artifacts)
6. Artifact detail (viewer, versions, reviews, trace, findings, baseline vs delta)
7. Gap analysis / coverage matrix
8. CR intake board and CR detail (impact, CAB)
9. Reports
10. Admin (templates, users, roles)

### 12. Delivery phases
- **Phase 1 (MVP):** schema and migrations, both default templates, PMS and demo seed data, portfolio and application pages, pipeline dashboard, tree navigation, stage/step/artifact CRUD with author/status/dates, Build coding-step matrix, manual reviews and findings, activity log, OpenAPI docs.
- **Phase 2:** CR intake, CAB, and CR pipelines (single and bundle); baseline register and re-baselining; coverage matrix and traceability; gates with approvals; reports; notifications.
- **Phase 3:** BMAD folder/repo sync; AI-assisted gap analysis; role-based landing pages; Git/CI status for coding steps; delivery metrics.

### 13. Acceptance criteria (MVP)
- [ ] The PMS dashboard shows the **Transformation pipeline at Stage 2 – BRD In Progress**, with Templates and Mockups Completed, including author and completion date. HLD is shown as the next stage, ahead of BMAD Planning.
- [ ] Stages 4–8 are visibly marked **BMAD-driven**, and BMAD Planning shows the Brief → PRD → UX → Architecture → PO → Epics & Stories steps.
- [ ] The Build stage shows a Story × Coding-Step matrix, and updating a step updates the story, epic and stage progress.
- [ ] Transformation and CR pipelines are listed and managed separately under an application. A CR pipeline can contain one CR or a bundle of CRs and follows the CR template.
- [ ] I can click any stage, step, milestone or artifact, see its status, author, planned date and completion date, and navigate back via the breadcrumb.
- [ ] I can log a review with findings, and open Critical findings show on the stage card and block the exit gate.
- [ ] `npm run dev` and `npm run seed` work on a fresh clone, and Swagger UI is available at `/api/docs`.

### 14. Output expectations
- Clean, typed code (JSDoc or TypeScript), a README (setup, seed, architecture diagram), an OpenAPI spec, and unit tests for the domain rules.
- After each phase, give a short summary: what was built, how to run it, known gaps, and what comes next.

**PROMPT END**

---

## PART B — Recommendations: making SDLC-Pipe useful for all stakeholders

1. **Make gates the heart of the tool.** Explicit entry/exit criteria, with open gaps and unapproved artifacts blocking a gate automatically, turn SDLC-Pipe into a governance tool rather than a tracker.
2. **Make "BMAD-ready" an explicit gate.** Mockups + BRD + HLD baselined is a clear, checkable handoff from human-authored foundation work to BMAD-driven delivery. It is also a natural point for a steering-committee checkpoint.
3. **Separate pipelines, shared baseline.** Keeping Transformation and CR pipelines separate gives each its own focus, cadence and stakeholders (steering committee vs CAB). The **baseline register** connects them: every CR starts from a baseline and re-baselines on release, so the application always has one current version of each artifact.
4. **One traceability thread.** Requirement IDs carried from BRD → HLD → PRD → Story → PR → Test → CR make gap analysis, UAT readiness and CR impact analysis largely automatic. Invest here before polishing the UI.
5. **Make coding steps visible without building another Jira.** The Story × Coding-Step matrix gives managers real progress (not just "In Build"). Later, pull PR and CI status from Git instead of entering it by hand.
6. **Artifacts-as-code sync.** BMAD already writes structured Markdown, so front-matter plus a sync button keeps SDLC-Pipe up to date with no double entry. Double entry is the main reason tools like this get abandoned.
7. **"Done / Doing / Next" first.** Most stakeholders spend about 30 seconds in the tool. Answer that first, then let them drill down.
8. **Role-based landing pages** (Sponsor, PM, BA, Architect, Dev, QA, CAB, Auditor) drive adoption more than any single feature.
9. **Delivery metrics** that carry across Infogain engagements: planned vs actual per stage, review rework rate, gap density per artifact type, first-pass gate rate, CR lead time and CR throughput per release.
10. **Dogfood it.** Track SDLC-Pipe's own build (as a Transformation pipeline) inside SDLC-Pipe from day one.
