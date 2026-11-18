# PMS – Payroll Management System (POC)

Lightweight POC to test an AI-enabled, end-to-end SDLC. Four microservices (EIMS, AMS, LMS, SMS), one DB entity each, in a single repository with a single BMAD install.

## Repository layout

| Path | Purpose |
| --- | --- |
| `_bmad/`, `_bmad-output/` | BMAD install and BMAD-generated artifacts (planning, implementation, test) |
| `templates/` | Frozen design templates (D-35 to D-48): UX journey index, UX summary, BRD, HLD Part01 architecture & design, Part01a principles, patterns & decisions (incl. ADR format), Part02 functional anchor, Part02 module functional, Part02 SUP, Part03 data model anchor, Part03 module data model, Part03 SUP data model |
| `docs/` | Project knowledge base read by BMAD (`project_knowledge`) |
| `docs/01-ux/` | Clickable HTML mockups and one UX summary per mockup (Step 2) |
| `docs/02-brd/` | Business Requirements Document (Step 3) |
| `docs/03-hld/` | High-Level Design (Step 4) |
| `docs/04-standards/` | Standards and guardrails |
| `docs/decisions/` | Decision log and architecture decision records (ADRs) |
| `memory/` | AI memory: `platform/`, `project/`, `sessions/` |
| `contracts/` | Contract-first OpenAPI specs and event schemas, shared by all services |
| `services/<module>/` | `frontend/` (micro-frontend) and `backend/` (Spring Boot) per module |
| `platform/` | Spring Cloud Gateway, shell UI, Keycloak realm config |
| `infra/` | Docker Compose, ActiveMQ Artemis, PostgreSQL, Azure deployment |
| `.github/workflows/` | One CI/CD pipeline per service (path-filtered) |

## Lifecycle

1. Project structure and templates
2. UX mockups + UX summaries
3. BRD (template + BA input)
4. HLD (template + Architect input), with standards and guardrails
5. BMAD lifecycle (Analysis, Planning, Solutioning, Implementation)
6. Deployment, go-live and hypercare
