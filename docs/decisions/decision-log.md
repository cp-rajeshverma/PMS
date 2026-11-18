# PMS – Decision Log

Every approved project decision, newest first. Approver for all entries: Rajesh Verma (product owner). Architecture-significant decisions also get an ADR in `adr/`.

| Id | Date | Area | Decision |
| --- | --- | --- | --- |
| D-34 | 16 Nov 2026 | Gate | **Step 2 (UX) approved**: UX journey index v1.0, 17 mockups, 17 UX summaries. Next: Step 3 (BRD) |
| D-47 | 18 Nov 2026 | Templates | Part01 document ID spelled out: <PRJ>-HLD-Part01-Architecture-and-Design (was <PRJ>-HLD-Part01-AnD); references in all templates, project memory and README updated; section references use "Part01 §n" |
| D-46 | 18 Nov 2026 | Templates | Template file hld-part01-and-template.md renamed to hld-part01-architecture-and-design-template.md; document ID <PRJ>-HLD-Part01-AnD unchanged |
| D-45 | 18 Nov 2026 | Templates | ADR template merged into Part01a, renamed Principles, Patterns & Decisions: §5 ADR register (with related catalogue ids), §6 ADR record format; each ADR stays a separate file in docs/decisions/adr; AnD §18 refers to Part01a §5; adr-template.md retired |
| D-44 | 18 Nov 2026 | Templates | Separate SUP data model template (hld-part03-sup-datamodel-template.md): need-basis assessment, one section per supporting group, entity structure referenced from module data model template §3.1; module data model template no longer carries SUP content |
| D-43 | 18 Nov 2026 | Templates | Data model split: Part03 anchor (conventions, ownership, entity index with links, entity-level master ER, cross-service consistency, roll-ups) + Part03-M<n>-<MOD>-Datamodel per module + Part03-M<n>-SUP-Datamodel (need basis); columns defined only in module documents |
| D-42 | 17 Nov 2026 | Templates | HLD Part03 data model template approved; supporting-module entities modelled on a need basis only (skipped where an existing capability provides them). Template set frozen; NPQMS reference PDFs may be removed from the Claude Project |
| D-41 | 17 Nov 2026 | Templates | HLD Part02 supporting modules (SUP) template approved |
| D-40 | 17 Nov 2026 | Templates | No separate Part01b A&A document: A&A architecture becomes a full chapter in AnD §9 (users / roles, IdP, OAuth/OIDC flows, MFA, JWT design, sessions, authorization model, API-level and service-to-service security, secrets); references in Part02 and SUP templates updated. SUP template has no per-function appendix; it refers to the Part02 functional template §3.2.1 |
| D-39 | 17 Nov 2026 | Templates | HLD Part02 functional module template approved (with D-38 refinements) |
| D-38 | 17 Nov 2026 | Templates | Part02 functional template, per-function chapter refined: Actor & data scope moved up; trigger / pre- / post-conditions; related functions in traceability; sequence and orchestration merged; new Security & data privacy subsection; scenarios carry requirement ref and test level; API ids with §4.2 as roll-up; reference BRD/UX instead of restating; design status values and technology-neutral guidance |
| D-37 | 17 Nov 2026 | Templates | AnD template v2 approved (BDUF checklist, functional / system / network / deployment / integration architecture, A&A summary, unified logging, PT strategy & plan) together with Part01a Principles & Patterns Catalogue (330 items, 18 groups); diagram sections keep a text-version table |
| D-36 | 16 Nov 2026 | Templates | BRD template v2 approved (document ID, reference documents, requirement ID conventions, role × screen matrix, entity status lifecycles, notifications, jobs, volumetrics) |
| D-35 | 16 Nov 2026 | Process | Design artifact set: PMS-BRD; PMS-HLD-Part01-AnD; PMS-HLD-Part02-M1..M4 (EIMS, AMS, LMS, SMS) Functional; PMS-HLD-Part02-M5-SUP-Functional; PMS-HLD-Part03-Datamodel. Single HLD template retired (supersedes D-15 template list). NPQMS reference PDFs stay in the Claude Project only until templates are frozen, then removed; never copied into the repo |
| D-33 | 16 Nov 2026 | SMS | Employees can accept several salary records at once (UXQ-23); no auto-accept, dashboard keeps reminding (UXQ-24); manager can close a dispute with **Keep as is** + required explanation, record returns to Manager Approved (UXQ-25) |
| D-32 | 16 Nov 2026 | LMS | Leave days are calendar days incl. weekends (UXQ-19); new status Cancelled for withdrawn requests (UXQ-20); no Reason field (UXQ-21); no draft for leave, submit directly (UXQ-22) |
| D-31 | 16 Nov 2026 | AMS | No withdrawal of Submitted attendance; manager rejects instead (UXQ-16). Times in 15-minute steps (UXQ-17). Warn, not block, above 12 hours a day (UXQ-18) |
| D-30 | 16 Nov 2026 | UX | Mockup styles and shared behaviour live in one stylesheet and one script (`docs/01-ux/mockups/assets/pms-mockup.css`, `pms-mockup.js`), linked by every mockup; seed for the future design-system package |
| D-29 | 16 Nov 2026 | EIMS | Role (Employee/Manager) chosen by Admin at onboarding, stored in Keycloak (UXQ-12); deactivating a manager with direct reports is blocked until reports are reassigned (UXQ-13); during re-approval other modules use the last approved profile (UXQ-14); last approved profile version is stored for change comparison, to be designed in HLD (UXQ-15) |
| D-28 | 16 Nov 2026 | Security / UX | Password policy: at least 8 characters, upper and lower case, a number, a special character, not the Employee Id (UXQ-10). Dashboard reminder for Mon–Fri days with no attendance or leave, reminder only (UXQ-11) |
| D-27 | 16 Nov 2026 | UX | Visual design of SCR-SH-00 and SCR-SH-01 approved as the style for all remaining mockups |
| D-26 | 16 Nov 2026 | Security | Session idle timeout 30 minutes (UXQ-08); account locked 15 minutes after 5 failed sign-ins, via Keycloak brute-force detection (UXQ-09) |
| D-25 | 15 Nov 2026 | SMS | New salary status **Voided**, set only by the system when linked attendance is reopened (UJ-SYS-03). Voided records stay visible (hidden by default, "Show voided" toggle), are excluded from totals, and the void reason is kept in Remarks. Rule becomes: one non-voided salary record per attendance |
| D-24 | 15 Nov 2026 | UX | UXQ-01–05, 07 accepted: multi-select approve (reject one at a time); attendance month calendar + list toggle; shell approvals inbox + module team tabs; Admin is system-only; reconciliation 01:00 IST; clean neutral light theme at 1366 px |
| D-23 | 15 Nov 2026 | Architecture | Frontend composition for the POC: build-time packages. Each module frontend is a library imported and built into `platform/shell-ui`; move to runtime micro-frontends (Module Federation) after the POC (ADR-001) |
| D-22 | 15 Nov 2026 | AI tooling | `.claude/settings.json` (machine-specific bmad-loop hooks) moved to `.claude/settings.local.json` and git-ignored, per the user-level memory layer |
| D-21 | 15 Nov 2026 | Architecture | Message broker edition: Apache ActiveMQ Artemis |
| D-20 | 15 Nov 2026 | Tooling | Git repository initialised locally; remote on GitHub under account `cp-rajeshverma` |
| D-19 | 15 Nov 2026 | Templates | Template outlines approved: UX journey index, UX summary, BRD, HLD, ADR (Markdown, in `templates/`) |
| D-18 | 15 Nov 2026 | Repository | Single repository `PMS` (D:\POC\PMS) with one BMAD install; services stay independent via separate builds, path-filtered pipelines, database per service, contracts-only sharing |
| D-17 | 15 Nov 2026 | AI tooling | BMAD GDS (game development) module is not relevant to PMS; its agents and skills must not be used (rule PR-01) |
| D-16 | 15 Nov 2026 | Architecture | Spring Cloud Gateway; Keycloak; one database per service; event-driven AMS → SMS with outbox and nightly reconciliation job on Apache ActiveMQ; contract-first OpenAPI 3; JUnit 5 + Mockito + Testcontainers; clickable HTML mockups; Markdown templates |
| D-15 | 15 Nov 2026 | Process | BRD and HLD follow predefined templates kept in `templates/` |
| D-14 | 15 Nov 2026 | Process | Before BMAD: UX mockups + UX summaries, then BRD (BA input), then HLD (Architect input). These form the BMAD knowledge base; BMAD runs from VS Code |
| D-13 | 15 Nov 2026 | Process | Experience-led design: all user journeys (frontend and backend scheduled jobs) are designed first, with business stakeholders |
| D-12 | 15 Nov 2026 | Technology | Backend in Java Spring Boot first; later replatformed to Node.js and Python FastAPI |
| D-11 | 15 Nov 2026 | Technology | React + TypeScript, PostgreSQL, JWT + bcrypt, GitHub + GitHub Actions, Docker, Azure App Service + Azure Database for PostgreSQL, Dev/QA/Prod, Playwright, k6 |
| D-10 | 15 Nov 2026 | Architecture | One microservice and one DB entity per module (EIMS, AMS, LMS, SMS); every architecture, design and SDLC standard applies in full |
| D-09 | 15 Nov 2026 | Requirements | BRD v1.0 approved as the Phase 1 baseline (input to the template-based BRD in Step 3) |
| D-08 | 15 Nov 2026 | Requirements | Assumptions: single company, IST, INR, no weekend or holiday rules, English desktop web UI, about 20 sample employees |
| D-07 | 15 Nov 2026 | Requirements | Open items O1–O6 accepted: dispute reopens attendance; manager cannot reject salary; Admin approves top-level employee; leave cancel while Submitted; past-dated leave allowed; Admin resets passwords |
| D-06 | 15 Nov 2026 | Scope | PMS is a lightweight POC to test an AI-enabled end-to-end SDLC; one table per module |
| D-05 | 15 Nov 2026 | SMS | S1–S6: hourly rate on Employee; hours × rate; generated on attendance approval; manager approves then employee accepts or disputes; no paid leave |
| D-04 | 15 Nov 2026 | LMS | L1–L4: request date; Casual/Sick/Earned full days; no balances; no overlaps |
| D-03 | 15 Nov 2026 | AMS | A1–A3: one entry per day; same-day times; no clash with leave |
| D-02 | 15 Nov 2026 | EIMS | E1–E3: system-generated Employee Id; re-approval on edit; validations |
| D-01 | 15 Nov 2026 | Common | C1–C5: Manager Id; workflow fields; simple login with three roles; reject and resubmit; soft delete |

## Pending decisions

None.
