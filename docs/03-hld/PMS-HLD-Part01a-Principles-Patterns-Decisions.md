# PMS – HLD Part01a: Architecture Principles, Patterns & Decisions

Document ID: PMS-HLD-Part01a-Principles-Patterns-Decisions-v1.0
Project: Payroll Management System (PMS) – proof of concept (POC), Stage 3 Solution Design
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 23-Nov-2026 | Rajesh Verma | First draft of §1–§3, based on PMS-HLD-Part01-Architecture-and-Design v1.0 rev 0.8 (D-109 to D-116), the approved BRD set v1.0 (D-107) and ADR-001 to ADR-006 |
| 1.0 | 0.2 | 23-Nov-2026 | Rajesh Verma | Draft of §4 groups A–F (GOV, XF, WA, SD, TF, FE); open items OI-P01a-01 to 03 |

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3 approved (D-117); §4 A–F approved (D-118) |
| Product owner | Rajesh Verma | 23-Nov-2026 | §1–§3 approved (D-117); §4 A–F approved (D-118) |

## 2. How to use this document

This document holds (a) the catalogue of architecture principles and patterns the PMS design is assessed against (§3–§4, referenced from PMS-HLD-Part01-Architecture-and-Design §4) and (b) the register and record format of architecture decisions (ADRs, §5–§6, referenced from Part01 §18). It is the second of the 14 HLD documents of Stage 3 (D-108) and closes Part01 open item OI-P01-01. For each catalogue row it records:

| Column | Meaning |
| --- | --- |
| Id | Stable id, used in HLDs, ADRs and reviews (e.g. AP-RES-03) |
| Applicability | **Applied** · **Partial** · **Deferred** (later phase) · **N/A** (with reason) |
| Realization | How the design meets it (component, setting, pattern), one line |
| Ref | Where it is designed: Part01 / Part02 / Part03 section, ADR, decision, standard |

**Reading rules for PMS**

- **Applied** – the POC design meets the item in full; detail may still be designed in a later HLD document or standard.
- **Partial** – the POC meets part of the item; the realization states which part, and the remainder is Deferred (Part01 §20.3) or an open item (§7).
- **Deferred** – not in the POC; planned for a later phase (Part01 §20.3 or the decision named in Ref).
- **N/A** – does not fit PMS; the reason is stated (assumption, constraint or decision).
- A row Deferred or N/A because of a decision references the ADR or decision id in Ref.
- Rows are never deleted; project-specific rows are added at the end of a group.
- Where Part01 §4 already states an item, this document uses the same reading.
- Ref values for documents not yet written: "Part02 (planned)", "Part03 (planned)" and "docs/04-standards/<area> (planned)", where <area> is one of the 12 standards areas of OBJ-06 (D-61): architecture-and-design, frontend-and-ux, api-and-integration, coding-and-code-review, database-and-data, security, logging-and-observability, performance-and-scalability, resilience-and-availability, testing-and-quality, devops-and-cicd, documentation-and-governance.
- The catalogue stays technology-neutral; a product is named only where Part01 §6.2, §7, §9.2 or §11 already names it.
- Items the design does not settle yet are recorded as open items OI-P01a-nn (§7) for the HLD document or standard that settles them; they are not decided here.

**Sources:**

- Cloud design patterns – Azure Architecture Center (https://learn.microsoft.com/en-us/azure/architecture/patterns/)
- Enterprise Integration Patterns – Hohpe & Woolf (https://www.enterpriseintegrationpatterns.com/patterns/messaging/)
- Microservice patterns – microservices.io (C. Richardson)
- Twelve-Factor App (12factor.net)
- Well-Architected Framework
- OWASP Top 10

The catalogue sources describe patterns only; they do not set the PMS platform (ADR-002).

## 3. Group summary

330 items in 18 groups. Counts per applicability are filled when the §4 group reviews are complete and are copied to Part01 §4.1.

| Group | Code | Rows | Applied | Partial | Deferred | N/A |
| --- | --- | --- | --- | --- | --- | --- |
| A. Architecture approach & governance | GOV | 11 | 10 | 1 | 0 | 0 |
| B. X-First principles | XF | 13 | 11 | 1 | 0 | 1 |
| C. Well-architected qualities | WA | 15 | 13 | 2 | 0 | 0 |
| D. Software design principles | SD | 19 | 17 | 2 | 0 | 0 |
| E. Twelve-Factor App | TF | 12 | 11 | 1 | 0 | 0 |
| F. Frontend & experience architecture | FE | 10 | 5 | 3 | 0 | 2 |
| G. Microservice design patterns | MS | 34 | | | | |
| H. Cloud design patterns | CP | 44 | | | | |
| I. Enterprise integration patterns | EIP | 64 | | | | |
| J. Integration principles | INT | 13 | | | | |
| K. Data architecture | DATA | 17 | | | | |
| L. Security architecture | SEC | 20 | | | | |
| M. Logging & observability | OBS | 12 | | | | |
| N. Performance & scalability | PERF | 10 | | | | |
| O. Resilience & availability | RES | 10 | | | | |
| P. DevOps & continuous delivery | DEV | 11 | | | | |
| Q. Testing & quality | QA | 10 | | | | |
| R. Delivery governance & knowledge management | DG | 5 | | | | |
| **Total** | | **330** | | | | |

Group R follows D-116: tool-neutral wording, ids AP-DG-01 to AP-DG-05, linked to OBJ-05, KPI-05 and OBJ-06 area 12.

## 4. Catalogue

### A. Architecture approach & governance (GOV)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-GOV-01 | Big Design Up Front (BDUF) | Enterprise architecture artifacts (architecture & design, A&A, HLDs, data model, contracts) are approved before implementation starts | Applied | Design-before-build checklist; build starts only after the Stage 3 gate approves the HLD set, contracts and standards | Part01 §2, §3.1; D-108 |
| AP-GOV-02 | Stakeholder alignment | Functional, system, deployment and integration architectures are reviewed and signed off with the stakeholders concerned | Applied | Section-by-section review with the product owner and the roles concerned; alignment log and per-chapter alignment tables | Part01 §3.2, §5.4, §6.5, §7.5, §8.6, §9.11; D-106 |
| AP-GOV-03 | Architecture decision records | Every significant decision is recorded with context, options and consequences | Applied | Every approved decision in the decision log; significant ones as ADR files in the §6 format, indexed in §5 | §5, §6; docs/decisions/decision-log.md |
| AP-GOV-04 | End-to-end traceability | Requirement → design → code → test are linked by ids | Applied | BRD ids (FR, BR, VR, NFR, INT, JOB) referenced in the HLD; function ids carried into contracts, code and tests (KPI-05) | Part01 §2; Part02 (planned); docs/04-standards/documentation-and-governance (planned) |
| AP-GOV-05 | Standards & guardrails compliance | Design and code follow published standards; deviations need an ADR | Applied | 12 standards areas written in Stage 3 and signed off with the HLD set; a deviation needs an ADR | D-61, D-108; docs/04-standards/ (planned) |
| AP-GOV-06 | Architecture review gates | Formal review at end of design, before build, before go-live | Applied | Stage gates (Stage 2 BRD gate passed, Stage 3 HLD gate before build); performance results and restore test before the go-live gate | Part01 §3.1, §14.7, §14.8; D-107, D-108 |
| AP-GOV-07 | Approved technology stack | Only technologies on the approved stack are used; additions via ADR | Applied | Stack and version policy fixed in Part01 §11; a product change is an ADR (e.g. edge product, ADR-005) | Part01 §11; D-112; ADR-005 |
| AP-GOV-08 | Documentation as code | Architecture and design docs are versioned with the code | Applied | Markdown documents in the single repository are the master copy, with version and revision history | D-18; Part01 §1 |
| AP-GOV-09 | Reuse → buy → build | Prefer reuse of platform capabilities, then proven products, then custom build | Applied | Accounts, passwords, sessions and security events from the identity provider; broker, gateway and observability from proven open-source products; custom code only for the business modules | Part01 §5.1, §11; ADR-003 |
| AP-GOV-10 | Evolutionary architecture | Architecture can change incrementally; fitness functions verify key qualities | Partial | Incremental steps planned (runtime micro-frontends, backend replatforming, shared session store); quality checks exist as pipeline gates and NFR tests, but no fitness functions are defined | Part01 §15, §16.3, §20.3; OI-P01a-01 |
| AP-GOV-11 | Replatforming readiness | Contracts, events and data are language-neutral so services can move runtime | Applied | Contract-first REST and event schemas with JSON payloads; technology-neutral HLD; databases accessed only by their own service | Part01 §8.2, §19 AR-09; D-12, NFR-08 |

### B. X-First principles (XF)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-XF-01 | UX first | User journeys and mockups are designed and approved before functional and technical design | Applied | 30 journeys and 17 screens approved before the BRD and HLD; the HLD designs against UX v1.1 | Part01 §4.2; D-105, C-07 |
| AP-XF-02 | API first / contract first | Every capability is a versioned API contract (OpenAPI / event schema) defined before implementation | Applied | OpenAPI 3 contracts and versioned event schemas in `contracts/`, written before implementation; services share contracts only | Part01 §4.2, §8.2; D-16, D-18; Part02 (planned) |
| AP-XF-03 | Security first | Security controls designed in at every layer from the start | Applied | Identity provider, token checks at gateway and service, role and data scope on every request, zones, masking | Part01 §4.2, §9, §16 |
| AP-XF-04 | Performance first | Performance budgets and load profile defined at design time | Applied | NFR-01 targets, load profile and performance test plan fixed in the HLD | Part01 §4.2, §14, §17 |
| AP-XF-05 | Cloud first | Managed cloud services preferred over self-managed infrastructure | Partial | Read as cloud-ready for the on-premises POC: containers, configuration outside the images, every component mapped to an AWS service; managed services used only in the AWS target | Part01 §4.2, §6.2; ADR-002; D-117 |
| AP-XF-06 | Data first | Data ownership, model and quality defined before services | Applied | Data ownership fixed per module; one database per service; entities modelled before code | Part01 §4.2, §12; D-10, C-02; Part03 (planned) |
| AP-XF-07 | Observability first | Logs, metrics, traces and health checks designed in, not added later | Applied | Activity log with flow reference, audit log, metrics, traces, health checks and alerts designed in the HLD | Part01 §4.2, §10; NFR-09 |
| AP-XF-08 | Automation first | Build, test, deploy, provisioning and checks are automated | Applied | Pipeline per service with automated tests and scans; deployment charts; infrastructure code for AWS | Part01 §4.2, §15; D-110, D-112 |
| AP-XF-09 | Test first | Tests and acceptance criteria written before or with code | Applied | Acceptance criteria for every BRD requirement before design; tests written with the code and enforced by the coverage gate | BRD module §7; Part01 §15; docs/04-standards/testing-and-quality (planned) |
| AP-XF-10 | Accessibility first | Accessibility standard (e.g. WCAG 2.1 AA) applied from mockups onward | Applied | WCAG 2.1 AA from the mockups; nothing conveyed by colour alone; keyboard operable | Part01 §4.2; NFR-04 |
| AP-XF-11 | Privacy by design | Personal data minimized, classified and protected by default | Applied | Sensitive attributes classified; shown only within the role's data scope; masked in logs; synthetic test data only | Part01 §4.2, §10.8; NFR-EIMS-01, R-04 |
| AP-XF-12 | Mobile / responsive first | Layouts designed for the smallest supported screen first | N/A | Desktop browsers only; layouts designed for 1366 px wide screens | A-03, NFR-04; D-117 |
| AP-XF-13 | Cost aware (FinOps) | Cost is a design input; resources sized and switched off when idle | Applied | Sized from the volumetrics; Dev scaled to zero when unused; AWS production simulation built on demand and torn down; no cache server or licensed components | Part01 §7.4, §15, §17; D-110 |

### C. Well-architected qualities (WA)

| Id | Quality | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-WA-01 | Resiliency | System recovers from failures and continues to function | Applied | Outbox hand-over retried until delivered; repeatable salary generation; nightly reconciliation; timeout, retry and circuit-breaker defaults | Part01 §4.3, §8.5; ADR-006 |
| AP-WA-02 | Availability | System meets its availability target with no single point of failure | Partial | 2 instances per stateless tier in Prod, daily backup (RPO 24 h, RTO 8 h); single site, single-node database and broker; target verified in the AWS production simulation; replica and multi-AZ Future | Part01 §4.3, §6.4, §19 AR-03, §20.3; D-109 |
| AP-WA-03 | Decentralized | No central component that every request or team depends on | Applied | Each module owns its service and database; gateway and identity provider are shared platform components without business logic | Part01 §4.3; D-10, C-02 |
| AP-WA-04 | Independent & autonomous | Each service is built, deployed, scaled and failed independently | Partial | Separate builds, path-filtered pipelines and deployments per service; module screens are built into the shell, so a UI change redeploys the shell; runtime micro-frontends Future | Part01 §4.3, §19 AR-08, §20.3; ADR-001 |
| AP-WA-05 | Auto provisioning | Infrastructure and environments are created from code (IaC) | Applied | Deployment charts for every PMS component; infrastructure code for AWS; local cluster from the container platform or a cluster definition file | Part01 §4.3, §11.2; D-110 |
| AP-WA-06 | Scalability | Capacity grows horizontally without redesign | Applied | Stateless services scale out per service; scale-out to 10×, load-tested to 2× | Part01 §4.3; NFR-07 |
| AP-WA-07 | Security | Confidentiality, integrity and availability protected end to end | Applied | Identity provider, token validation at gateway and service, role and data scope, private zones, encryption in transit at the edge, secrets outside code | Part01 §4.3, §9, §16 |
| AP-WA-08 | Continuous delivery | Every change can be released safely at any time through a pipeline | Applied | One pipeline per service with quality gates; promotion Dev → QA → Prod | Part01 §4.3, §15 |
| AP-WA-09 | Failure isolation | A failing component does not cascade to others | Applied | Dashboard cards load independently; AMS approval does not wait for SMS; database per service; circuit breakers | Part01 §4.3, §8.5; FR-CMN-008 |
| AP-WA-10 | Observability | Internal state is understandable from logs, metrics and traces | Applied | Central activity log with flow reference, metrics, traces, dashboards and alerts | Part01 §4.3, §10 |
| AP-WA-11 | Reliability (WAF pillar) | Workload performs its intended function correctly and consistently | Applied | Exactly one non-voided salary record per approved attendance; version check against overwrites; reconciliation with 0 mismatches as target | Part01 §8, §16.3; NFR-06, KPI-04 |
| AP-WA-12 | Cost optimization (WAF pillar) | Delivers business value at the lowest reasonable cost | Applied | Open-source components; one workstation for the POC; AWS simulation only on demand; no cache server in the POC | Part01 §6.2, §7.4; D-110 |
| AP-WA-13 | Operational excellence (WAF pillar) | Operations are automated, monitored and continuously improved | Applied | Pipeline-only deployment, dashboards and email alerts, monthly patching, monthly restore test | Part01 §10.7, §12, §15; D-112 |
| AP-WA-14 | Performance efficiency (WAF pillar) | Resources match demand efficiently | Applied | Replicas sized from the volumetrics; per-service scale-out; QA scaled to Prod sizing only for the test window | Part01 §7.4, §14, §17 |
| AP-WA-15 | Sustainability | Resource usage and energy footprint minimized | Applied | Small footprint on one machine; idle environments scaled to zero; cloud resources torn down after use | Part01 §7.4, §15 |

### D. Software design principles (SD)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-SD-01 | Single responsibility | A class / module has one reason to change | Applied | One business capability per service; class-level rule in the coding standard | Part01 §5.3; docs/04-standards/coding-and-code-review (planned) |
| AP-SD-02 | Open–closed | Open for extension, closed for modification | Applied | Coding standard rule | docs/04-standards/coding-and-code-review (planned) |
| AP-SD-03 | Liskov substitution | Subtypes are usable wherever their base type is expected | Applied | Coding standard rule | docs/04-standards/coding-and-code-review (planned) |
| AP-SD-04 | Interface segregation | Clients depend only on the interfaces they use | Applied | One API per module context; coding standard rule for internal interfaces | Part01 §5.3; docs/04-standards/coding-and-code-review (planned) |
| AP-SD-05 | Dependency inversion | Depend on abstractions, not concrete implementations | Applied | Server interfaces generated from the contracts; coding standard rule | Part01 §11.1; docs/04-standards/coding-and-code-review (planned) |
| AP-SD-06 | Separation of concerns | Presentation, business logic and data access kept apart | Applied | Frontend packages, services and databases separated; per-function design splits frontend, backend and database | Part01 §5.3; D-38; Part02 (planned) |
| AP-SD-07 | High cohesion, loose coupling | Related logic together; minimal dependencies between modules | Applied | Module per business capability; modules coupled only through contracts and events | Part01 §5.3, §8; D-10, D-18 |
| AP-SD-08 | DRY | Each piece of knowledge has one authoritative representation | Applied | Contracts are the single source for server interfaces and frontend clients; requirements referenced by id, not repeated | Part01 §2, §11.1 |
| AP-SD-09 | KISS | Prefer the simplest design that works | Applied | Build-time module packages, no cache server, no service mesh, single-node broker for the POC | ADR-001; D-110; Part01 §20.3 |
| AP-SD-10 | YAGNI | Build only what current requirements need | Applied | Supporting functions on need basis; ADM, NM and DM in Phase 2 | D-42, D-57; PMS-BRD-M5-SUP §3 |
| AP-SD-11 | Law of Demeter | Objects talk only to their immediate collaborators | Applied | Coding standard rule | docs/04-standards/coding-and-code-review (planned) |
| AP-SD-12 | Composition over inheritance | Build behaviour by composing objects | Applied | Coding standard rule | docs/04-standards/coding-and-code-review (planned) |
| AP-SD-13 | Fail fast | Detect and report invalid state at the earliest point | Applied | Requests validated against the contract and BRD validation rules at entry; stale updates refused by the version check | Part01 §8.4, §9.8 |
| AP-SD-14 | Convention over configuration | Sensible defaults; configure only exceptions | Applied | Framework defaults; only environment-specific values are deployment settings | Part01 §11; D-97 |
| AP-SD-15 | Immutability by default | Prefer immutable objects and append-only records | Applied | Audit log append-only; records never physically deleted; salary records voided, not changed | Part01 §12; BR-CMN-06, FR-ADM-103; Part03 (planned) |
| AP-SD-16 | Hexagonal / clean architecture | Domain core isolated from frameworks via ports and adapters | Partial | Technology-neutral design and contract-generated interfaces support replatforming; the internal service structure is not yet set | Part01 §19 AR-09; D-12; OI-P01a-02 |
| AP-SD-17 | Domain-driven design | Bounded contexts, ubiquitous language, aggregates | Applied | Domains and towers per bounded context; BRD terms and statuses as the common language; one business entity per module | Part01 §5.3; C-01, D-10 |
| AP-SD-18 | Stateless services | No session state held in service instances | Partial | Business services hold no session state; the API gateway holds user sessions in memory with session affinity; shared session store Future | Part01 §6.4, §19 AR-02, §20.3; ADR-004 |
| AP-SD-19 | Defensive validation | Validate at every trust boundary; server-side validation is authoritative | Applied | Validation in every service against contract and BRD rules; the UI check is never the only one | Part01 §9.7, §9.8 |

### E. Twelve-Factor App (TF)

| Id | Factor | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-TF-01 | Codebase | One codebase tracked in version control, many deploys | Applied | Single repository with one independently built folder per service; the same build deployed to every environment | D-18; Part01 §15 |
| AP-TF-02 | Dependencies | Explicitly declared and isolated | Applied | Dependencies declared in each service's build files with pinned versions; packaged in the container image | Part01 §11 |
| AP-TF-03 | Config | Configuration stored in the environment, not code | Applied | Deployment settings per environment in deployment values; secrets from protected pipeline secrets | Part01 §9.10, §11.2; D-97 |
| AP-TF-04 | Backing services | Treated as attached resources | Applied | Database, broker and identity provider attached by configured address and credentials; on AWS the database is replaced by the managed service without code change | Part01 §6.2 |
| AP-TF-05 | Build, release, run | Strictly separated stages | Applied | Image built once by the pipeline, released with environment values, run by the platform | Part01 §15, §16.2 A08 |
| AP-TF-06 | Processes | Stateless, share-nothing processes | Partial | Business services are stateless; the API gateway keeps user sessions in memory (session affinity); shared session store Future | Part01 §19 AR-02, §20.3; ADR-004 |
| AP-TF-07 | Port binding | Services export themselves via a port | Applied | Every component serves HTTP on its own container port | Part01 §7.3 |
| AP-TF-08 | Concurrency | Scale out via the process model | Applied | Replicas per service added by the platform | Part01 §6.2; NFR-07 |
| AP-TF-09 | Disposability | Fast start-up and graceful shutdown | Applied | Failed instances replaced by the platform; readiness checks before traffic; shutdown settings in the resilience standard | Part01 §6.4; docs/04-standards/resilience-and-availability (planned) |
| AP-TF-10 | Dev/prod parity | Environments kept as similar as possible | Applied | Same images, deployment charts and database version in every environment; differences listed per environment | Part01 §7.4; D-115 |
| AP-TF-11 | Logs | Logs treated as event streams | Applied | Structured JSON logs to standard output, collected centrally | Part01 §10.1, §10.4 |
| AP-TF-12 | Admin processes | One-off admin tasks run as one-off processes | Applied | Seed, performance-test data and backup jobs run as separate jobs; schema migrations versioned with the service | Part01 §6.2, §13; D-112 |

### F. Frontend & experience architecture (FE)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-FE-01 | Headless frontend | UI consumes the backend only through APIs | Applied | The shell and module packages call the services only through the gateway APIs | Part01 §6.1, §8.2 |
| AP-FE-02 | Single-page application | One entry point; client-side routing and rendering | Applied | One shell application with client-side routing, served as static content | Part01 §5.3, §6.1, §11.1 |
| AP-FE-03 | Micro-frontends | Each module owns its UI; composed in a shell (build-time or runtime) | Partial | Each module owns its screens package, composed into the shell at build time; runtime composition Future | ADR-001; Part01 §5.3, §20.3 |
| AP-FE-04 | Shared design system | One component library and style tokens for all modules | Partial | One shell layout and the shared mockup assets for all modules; the component library and style tokens are not yet defined | Part01 §5.1; FR-CMN-015; D-82; OI-P01a-03 |
| AP-FE-05 | Backend for frontend | Aggregation API tailored to a UI where needed | N/A | One client type (desktop browser); the dashboard composes module calls in the client, one call per card | Part01 §8.2 (row 8); A-03, FR-CMN-008 |
| AP-FE-06 | Responsive layout | Works across supported screen sizes | Partial | Desktop widths from 1366 px on the latest Chrome and Edge; no tablet or phone layouts | NFR-04, A-03; D-117 |
| AP-FE-07 | Accessibility | Keyboard, screen reader, contrast per standard | Applied | WCAG 2.1 AA, contrast at least 4.5:1, keyboard operable; automated checks in end-to-end tests | Part01 §16.3; NFR-04 |
| AP-FE-08 | Internationalization readiness | Text externalized; locale-aware formats | N/A | English only, one time zone (IST) and one currency (INR) | A-01, A-03; D-117 |
| AP-FE-09 | Client-side security | Tokens handled securely; no secrets in the browser | Applied | Browser holds only an HttpOnly session cookie and a CSRF token; tokens stay in the gateway | Part01 §9.5; ADR-004 |
| AP-FE-10 | Consistent feedback | Standard loading, empty, error and success states | Applied | Consistent layout and messages on every screen; per-card error with Retry; system errors show the flow reference | FR-CMN-008, FR-CMN-015, FR-ADM-114; Part02 (planned) |

Groups G–R: to be drafted.

## 5. Architecture decision register (ADRs)

To be drafted.

## 6. ADR record format

To be drafted.

## 7. Open items

| Id | Open item | Catalogue ids | Owner | Due |
| --- | --- | --- | --- | --- |
| OI-P01a-01 | Fitness functions: which key qualities (e.g. response time, coupling between modules, contract compatibility) are checked automatically, and how | AP-GOV-10 | Enterprise Architect | docs/04-standards/architecture-and-design |
| OI-P01a-02 | Internal service structure: whether domain logic is isolated from framework code by ports and adapters, to support replatforming (D-12) | AP-SD-16 | Enterprise Architect | docs/04-standards/coding-and-code-review |
| OI-P01a-03 | Shared design system: component library and style tokens used by the shell and every module package | AP-FE-04 | Enterprise Architect | Part02 anchor or docs/04-standards/frontend-and-ux |
