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
| 1.0 | 0.3 | 23-Nov-2026 | Rajesh Verma | Draft of §4 groups G–L (MS, CP, EIP, INT, DATA, SEC); open items OI-P01a-04 to 11; §2 Partial rule clarified |
| 1.0 | 0.4 | 23-Nov-2026 | Rajesh Verma | Draft of §4 groups M–R (OBS, PERF, RES, DEV, QA, DG); all 330 rows assessed; §3 totals; open items OI-P01a-12 to 17 |

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3 approved (D-117); §4 A–F approved (D-118); §4 G–L approved (D-119); §4 M–R approved (D-120) |
| Product owner | Rajesh Verma | 23-Nov-2026 | §1–§3 approved (D-117); §4 A–F approved (D-118); §4 G–L approved (D-119); §4 M–R approved (D-120) |

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
- **Partial** – the POC meets part of the item; the realization states which part, and the remainder is Deferred (Part01 §20.3), an open item (§7) or excluded by the assumption, constraint or decision named in Ref.
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
| G. Microservice design patterns | MS | 34 | 25 | 3 | 1 | 5 |
| H. Cloud design patterns | CP | 44 | 24 | 2 | 1 | 17 |
| I. Enterprise integration patterns | EIP | 64 | 28 | 1 | 0 | 35 |
| J. Integration principles | INT | 13 | 11 | 2 | 0 | 0 |
| K. Data architecture | DATA | 17 | 14 | 2 | 0 | 1 |
| L. Security architecture | SEC | 20 | 13 | 6 | 1 | 0 |
| M. Logging & observability | OBS | 12 | 12 | 0 | 0 | 0 |
| N. Performance & scalability | PERF | 10 | 8 | 1 | 0 | 1 |
| O. Resilience & availability | RES | 10 | 7 | 3 | 0 | 0 |
| P. DevOps & continuous delivery | DEV | 11 | 7 | 4 | 0 | 0 |
| Q. Testing & quality | QA | 10 | 9 | 1 | 0 | 0 |
| R. Delivery governance & knowledge management | DG | 5 | 5 | 0 | 0 | 0 |
| **Total** | | **330** | **230** | **35** | **3** | **62** |

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

### G. Microservice design patterns (MS)

| Id | Pattern | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-MS-01 | Decompose by business capability | Services aligned to business capabilities | Applied | One service per business module: EIMS, AMS, LMS, SMS | Part01 §4.4, §5.3; D-10 |
| AP-MS-02 | Decompose by subdomain | Services aligned to DDD subdomains / bounded contexts | Applied | Domains Employee, Time & absence, Pay and Platform; one tower per bounded context | Part01 §5.3 |
| AP-MS-03 | Database per service | Each service owns its data; no direct access by others | Applied | One database per service with its own credentials; no foreign keys across databases | Part01 §4.4, §12; C-02 |
| AP-MS-04 | Shared database (anti-pattern check) | Confirm services do not share tables | Applied | Confirmed: no shared tables; one database server per environment holds separate databases, each reachable only with its owner's credentials | Part01 §6.3, §12 |
| AP-MS-05 | API gateway | Single entry point for clients; routing, auth, rate limits | Applied | Gateway holds the session, relays the token, routes by module context and limits request rates | Part01 §4.4, §6.1, §9.8; ADR-004 |
| AP-MS-06 | Backends for frontends | Separate gateway / API per client type | N/A | One client type (desktop browser) | A-03; AP-FE-05 |
| AP-MS-07 | Service discovery / registry | Services locate each other dynamically | Applied | Services call configured internal service names resolved by the container platform; no separate registry | Part01 §6.2, §16.2 A10 |
| AP-MS-08 | Saga – choreography | Distributed transaction via events between services | Applied | Attendance approval and reopen in AMS drive salary generation and voiding in SMS by events | Part01 §4.4, §8.2; ADR-006 |
| AP-MS-09 | Saga – orchestration | Distributed transaction via a central orchestrator | N/A | No long-running multi-step process; the dispute cycle is a sequence of user actions with events | Part01 §8.4 |
| AP-MS-10 | Transactional outbox | Events written in the same DB transaction as state, then published | Applied | AMS writes each event to its outbox table in the status-change transaction | Part01 §8.2, §8.3; ADR-006 |
| AP-MS-11 | Polling publisher / transaction log tailing | How outbox events are relayed to the broker | Applied | Polling publisher: an outbox relay in AMS reads unsent rows, publishes and marks them sent after the broker confirms; no log tailing | Part01 §8.3 |
| AP-MS-12 | Domain events | Services publish events when domain state changes | Applied | Attendance approved (INT-01) and attendance reopened (INT-02) | Part01 §4.4, §8.2 |
| AP-MS-13 | Event sourcing | State stored as a sequence of events | N/A | State kept as current records with a field-level audit log | Part01 §12; BR-CMN-19 |
| AP-MS-14 | CQRS | Separate read and write models | N/A | One model per service; read volumes are small | Part01 §12, §17 |
| AP-MS-15 | API composition | Query that joins data from several services in a composer | Applied | Dashboard tiles, to-dos and the approvals inbox composed in the shell, one call per module card | Part01 §4.4, §8.2 (row 8); FR-CMN-008 |
| AP-MS-16 | Idempotent consumer | Duplicate messages processed safely | Applied | SMS checks event id and attendance id before processing; one non-voided salary record per attendance | Part01 §8.5; ADR-006; NFR-06 |
| AP-MS-17 | Circuit breaker | Stop calling a failing service for a period | Applied | Per downstream service: opens after 50 % failures in a 20-call window, half-open after 30 s | Part01 §8.5 |
| AP-MS-18 | Externalized configuration | Configuration outside the deployable artifact | Applied | Settings per environment in deployment values and platform secrets | Part01 §4.4, §9.10; D-97 |
| AP-MS-19 | Health check API | Endpoint reporting liveness and readiness | Applied | Liveness and readiness endpoints per component, reachable inside the cluster only | Part01 §4.4, §9.8, §10.7 |
| AP-MS-20 | Log aggregation | Logs from all services collected centrally | Applied | All components ship structured logs to one collector and log store | Part01 §4.4, §10.1 |
| AP-MS-21 | Distributed tracing | Requests traced across services with trace ids | Applied | Trace context on every call and event; traces in the trace store | Part01 §10.5 |
| AP-MS-22 | Application metrics | Services expose metrics for monitoring | Applied | Metrics from every component to the metric store; dashboards and alerts | Part01 §10.7 |
| AP-MS-23 | Audit logging | User actions recorded per business entity | Applied | Field-level audit entries in each module database, written in the same transaction as the change | Part01 §4.4, §10.2; BR-CMN-19 |
| AP-MS-24 | Exception tracking | Exceptions reported centrally with context | Applied | Errors logged with error code, stack trace and flow reference; error-rate alert | Part01 §10.3, §10.7 |
| AP-MS-25 | Access token | Identity propagated to services via a token (e.g. JWT) | Applied | Signed JWT access token relayed by the gateway; service token for system calls | Part01 §9.5, §9.9; ADR-003, ADR-004 |
| AP-MS-26 | Consumer-driven contract test | Consumers define contract tests the provider must pass | Partial | Providers and consumers verified against the shared contracts (schema-based); consumer-driven tests not yet decided | Part01 §15; D-117; OI-P01a-04 |
| AP-MS-27 | Service component test | Service tested in isolation with test doubles | Applied | Component tests per service with test doubles and containerised database, broker and identity provider | Part01 §11.1, §15; D-16 |
| AP-MS-28 | Service instance per container | Each service instance in its own container | Applied | One container image per component; each replica in its own container | Part01 §4.4, §7.2; ADR-002 |
| AP-MS-29 | Sidecar | Cross-cutting concerns in a co-deployed process | Deferred | No sidecars; cross-cutting concerns in the service and a central collector; service mesh Future | Part01 §9.9, §20.3; AR-04 |
| AP-MS-30 | Microservice chassis / service template | Common framework and starter for all services | Partial | Same framework, security and observability set-up in every service; a service template is copied per service; no shared runtime library | Part01 §11; D-18, D-117; OI-P01a-05 |
| AP-MS-31 | Strangler application | Incremental replacement of a legacy system | N/A | Greenfield; no legacy system | Part01 §13; D-109 |
| AP-MS-32 | Anti-corruption layer | Translation layer between different domain models | Applied | Only EIMS translates employee records into identity-provider accounts; no other module uses the identity provider's model | Part01 §8.2 (row 9); INT-08; Part02 (planned) |
| AP-MS-33 | API versioning | Backward-compatible evolution of service contracts | Applied | Versioned contracts with backward-compatible changes; version scheme in the API standard | Part01 §4.4; docs/04-standards/api-and-integration (planned); OI-P01a-11 |
| AP-MS-34 | Self-contained service | A service can answer synchronous requests without waiting on others | Partial | Employee and approver details read from EIMS synchronously, with circuit breaker and short-lived in-memory copies; shared cache Future | Part01 §8.2, §12, §20.3; D-110 |

### H. Cloud design patterns (CP)

Source: Azure Architecture Center cloud design patterns catalogue.

| Id | Pattern | Summary | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-CP-01 | Ambassador | Helper service sends network requests on behalf of a consumer | N/A | Client-side resilience is built into each service; no proxy per consumer | Part01 §8.5 |
| AP-CP-02 | Anti-Corruption Layer | Façade / adapter between a modern application and a legacy system | N/A | Greenfield; no legacy system | Part01 §13; D-109 |
| AP-CP-03 | Asynchronous Request-Reply | Decouple backend processing from the frontend while giving a timely response | N/A | No long-running user request; every user action completes synchronously | Part01 §8.4 |
| AP-CP-04 | Backends for Frontends | Separate backend services per frontend | N/A | One client type (desktop browser) | A-03; AP-FE-05 |
| AP-CP-05 | Bulkhead | Isolate elements into pools so one failure does not take down others | Applied | Each module runs in its own containers with its own database and credentials; one module failing does not stop the others | Part01 §4.3 (AP-WA-09); FR-CMN-008 |
| AP-CP-06 | Cache-Aside | Load data into a cache on demand | Partial | Services keep short-lived in-memory copies of read-mostly data from EIMS, loaded on demand; shared cache Future | Part01 §6.1, §12, §20.3; D-110 |
| AP-CP-07 | Choreography | Services decide how to process a business operation without a central orchestrator | Applied | AMS publishes, SMS reacts; no orchestrator | Part01 §4.4, §8.2; ADR-006 |
| AP-CP-08 | Circuit Breaker | Handle faults of variable duration when calling remote services | Applied | Circuit breaker per downstream service with the §8.5 defaults | Part01 §4.4, §8.5 |
| AP-CP-09 | Claim Check | Split large messages into a claim check and a payload | N/A | Events are small (about 0.5 KB) | Part01 §17 |
| AP-CP-10 | Compensating Transaction | Undo steps of an eventually consistent operation | Applied | Attendance reopen voids the salary record (INT-02); reconciliation voids records whose attendance is no longer approved | Part01 §5.2, §8.2; ADR-006 |
| AP-CP-11 | Competing Consumers | Several consumers process messages from one channel | Applied | The SMS instances consume from the one subscription queue; processing is idempotent | Part01 §6.2, §8.3; ADR-006; Part02 (planned) |
| AP-CP-12 | Compute Resource Consolidation | Consolidate tasks into one computational unit | Applied | Nightly reconciliation runs inside SMS; the three environments share one cluster | Part01 §6.1, §6.2 |
| AP-CP-13 | CQRS | Separate read and update interfaces | N/A | One model per service; read volumes are small | Part01 §17; AP-MS-14 |
| AP-CP-14 | Deployment Stamps | Independent copies of components including data stores | N/A | Single company and single site; environments are separate but not stamps | A-01; D-109 |
| AP-CP-15 | Event Sourcing | Append-only store of events describing changes | N/A | Current-state records with an audit log | AP-MS-13 |
| AP-CP-16 | External Configuration Store | Configuration in a central location outside the package | Applied | Deployment values and platform secrets per environment, outside the images | Part01 §9.10, §11.2 |
| AP-CP-17 | Federated Identity | Delegate authentication to an external identity provider | Applied | Sign-in at the OIDC identity provider; services accept its tokens | Part01 §4.4, §9.2, §9.3; ADR-003 |
| AP-CP-18 | Gatekeeper | Dedicated host validates and sanitizes requests before back ends | Applied | Edge with WAF rule set and payload limits as the only entry | Part01 §6.3, §9.8; ADR-005 |
| AP-CP-19 | Gateway Aggregation | Gateway aggregates several requests into one | N/A | Composition in the client, one call per card, so each card fails on its own | Part01 §8.2 (row 8); FR-CMN-008 |
| AP-CP-20 | Gateway Offloading | Offload shared functionality to a gateway | Applied | TLS, WAF and security headers at the edge; session, token relay and rate limits at the gateway | Part01 §4.4, §9.8; ADR-004, ADR-005 |
| AP-CP-21 | Gateway Routing | Route requests to several services through one endpoint | Applied | Gateway routes by module context /eims, /ams, /lms, /sms | Part01 §4.4, §8.2 (row 12) |
| AP-CP-22 | Geode | Back ends deployed across geographically distributed nodes | N/A | Single site and single region (ap-south-1 on AWS) | D-109; Part01 §6.3 |
| AP-CP-23 | Health Endpoint Monitoring | Functional checks exposed through endpoints | Applied | Health endpoints checked by the platform and the alert rules | Part01 §4.4, §10.7 |
| AP-CP-24 | Idempotent Consumer | Duplicate delivery has the same effect as single delivery | Applied | As AP-MS-16 | Part01 §8.5; ADR-006 |
| AP-CP-25 | Index Table | Indexes over frequently queried fields | Applied | Database indexes for the heaviest queries | Part01 §16.3; Part03 (planned) |
| AP-CP-26 | Leader Election | One instance coordinates collaborating instances | Applied | A database lock lets one SMS instance run each reconciliation | Part01 §6.1, §6.4; ADR-006 |
| AP-CP-27 | Materialized View | Prepopulated views for query needs | N/A | Volumes are small; queries read the service's own tables | Part01 §17 |
| AP-CP-28 | Messaging Bridge | Intermediary between incompatible messaging systems | N/A | One broker | Part01 §6.1 |
| AP-CP-29 | Pipes and Filters | Complex processing broken into reusable steps | N/A | No multi-step message processing | Part01 §8 |
| AP-CP-30 | Priority Queue | Higher-priority requests processed first | N/A | One event flow with no priorities | Part01 §8.2 |
| AP-CP-31 | Publisher-Subscriber | Announce events to many consumers asynchronously | Applied | Attendance events topic; SMS is the only subscriber in the POC | Part01 §4.4, §8.3 |
| AP-CP-32 | Quarantine | External assets checked against agreed quality before use | Applied | Dependencies and container images scanned before use; no high or critical findings | Part01 §15, §16.1 |
| AP-CP-33 | Queue-Based Load Leveling | Queue buffers load between a task and a service | Applied | The broker buffers bulk attendance approvals for salary generation | Part01 §8.3, §14.2 (PT-03) |
| AP-CP-34 | Rate Limiting | Control resource consumption to avoid throttling | Applied | Per user and route at the gateway; per client address on the sign-in path at the edge | Part01 §4.4, §9.8 |
| AP-CP-35 | Retry | Retry anticipated transient failures | Applied | Reads retried with backoff; broker redelivery; outbox relay retries | Part01 §4.4, §8.5 |
| AP-CP-36 | Saga | Data consistency across microservices | Applied | Choreographed AMS → SMS hand-over with compensation and reconciliation | AP-MS-08; ADR-006 |
| AP-CP-37 | Scheduler Agent Supervisor | Coordinate actions across distributed services | Applied | Nightly reconciliation job with result logging, alerts and repair | Part01 §4.4, §8.2 (row 3); JOB-CMN-01 |
| AP-CP-38 | Sequential Convoy | Ordered processing of related messages without blocking others | Partial | Events carry the attendance id as business key; the ordering rule for approved and reopened events of one attendance is not yet designed | Part01 §8.2; OI-P01a-06 |
| AP-CP-39 | Sharding | Horizontal partitions of a data store | N/A | Total database size below 3 GB in year 5 | Part01 §17 |
| AP-CP-40 | Sidecar | Components in a separate process or container | Deferred | No sidecars in the POC; service mesh Future | Part01 §20.3; AR-04 |
| AP-CP-41 | Static Content Hosting | Static content served from storage / CDN | Applied | Static web server serves the shell build; no CDN | Part01 §4.4, §6.1 |
| AP-CP-42 | Strangler Fig | Incremental migration of a legacy system | N/A | Greenfield | Part01 §13 |
| AP-CP-43 | Throttling | Control consumption by applications, tenants or services | Applied | Rate limits and payload limits at the gateway and edge | Part01 §9.8 |
| AP-CP-44 | Valet Key | Token giving restricted direct access to a resource | N/A | No file or blob storage in the POC (document management Phase 2) | D-57 |

### I. Enterprise integration patterns (EIP)

Source: Enterprise Integration Patterns (Hohpe & Woolf), messaging patterns catalogue.

| Id | Category | Pattern | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-EIP-01 | Integration style | File Transfer | N/A | No file interfaces; bulk data by paged REST | Part01 §8.4; C-05 |
| AP-EIP-02 | Integration style | Shared Database | N/A | Excluded: database per service | C-02; AP-MS-04 |
| AP-EIP-03 | Integration style | Remote Procedure Invocation | Applied | Synchronous REST for queries and commands between services | Part01 §4.4, §8.2 |
| AP-EIP-04 | Integration style | Messaging | Applied | Broker events for the AMS → SMS hand-over | Part01 §4.4, §8.2 |
| AP-EIP-05 | Channels | Message Channel | Applied | Attendance events topic, SMS subscription queue, dead-letter queue | Part01 §8.3 |
| AP-EIP-06 | Channels | Point-to-Point Channel | Applied | SMS subscription queue and dead-letter queue | Part01 §8.3 |
| AP-EIP-07 | Channels | Publish-Subscribe Channel | Applied | Attendance events topic | Part01 §8.3 |
| AP-EIP-08 | Channels | Datatype Channel | Applied | The topic carries attendance events only | Part01 §8.3 |
| AP-EIP-09 | Channels | Invalid Message Channel | Applied | Events that cannot be processed go to the dead-letter queue after the allowed redeliveries, with an alert | Part01 §8.5 |
| AP-EIP-10 | Channels | Dead Letter Channel | Applied | Dead-letter queue after 5 attempts; alert; reconciliation repairs the outcome | Part01 §4.4, §8.5; ADR-006 |
| AP-EIP-11 | Channels | Guaranteed Delivery | Applied | Persistent broker storage, outbox until confirmed, durable subscription | Part01 §4.4, §6.4, §8.3 |
| AP-EIP-12 | Channels | Channel Adapter | Applied | Outbox relay moves events from the AMS database to the broker | Part01 §8.3 |
| AP-EIP-13 | Channels | Messaging Bridge | N/A | One broker | Part01 §6.1 |
| AP-EIP-14 | Channels | Message Bus | N/A | One event flow; services integrate mainly by REST | Part01 §8.4 |
| AP-EIP-15 | Message construction | Command Message | N/A | Commands are REST calls | Part01 §8.4 |
| AP-EIP-16 | Message construction | Document Message | N/A | Data transfer between services is by REST queries | Part01 §8.4 |
| AP-EIP-17 | Message construction | Event Message | Applied | Attendance approved and reopened events | Part01 §4.4, §8.2 |
| AP-EIP-18 | Message construction | Request-Reply | N/A | Request-reply is synchronous REST, not messaging | Part01 §8.4 |
| AP-EIP-19 | Message construction | Return Address | N/A | No messaging request-reply | AP-EIP-18 |
| AP-EIP-20 | Message construction | Correlation Identifier | Applied | Flow reference in every event envelope and HTTP header | Part01 §4.4, §10.5; FR-ADM-113 |
| AP-EIP-21 | Message construction | Message Sequence | N/A | Events are small and single | Part01 §17 |
| AP-EIP-22 | Message construction | Message Expiration | N/A | Every event must be processed; events never expire | ADR-006; NFR-06 |
| AP-EIP-23 | Message construction | Format Indicator | Applied | Event type and version in the envelope | Part01 §8.2 |
| AP-EIP-24 | Routing | Pipes and Filters | N/A | No multi-step message processing | AP-CP-29 |
| AP-EIP-25 | Routing | Message Router | N/A | One subscriber; no routing logic | Part01 §8.3 |
| AP-EIP-26 | Routing | Content-Based Router | N/A | As AP-EIP-25 | Part01 §8.3 |
| AP-EIP-27 | Routing | Message Filter | N/A | As AP-EIP-25 | Part01 §8.3 |
| AP-EIP-28 | Routing | Dynamic Router | N/A | As AP-EIP-25 | Part01 §8.3 |
| AP-EIP-29 | Routing | Recipient List | N/A | Publish-subscribe topic instead | AP-EIP-07 |
| AP-EIP-30 | Routing | Splitter | N/A | One event per attendance status change | Part01 §8.2 |
| AP-EIP-31 | Routing | Aggregator | N/A | No messages combined | Part01 §8.2 |
| AP-EIP-32 | Routing | Resequencer | Partial | Events carry the attendance id as business key; the ordering rule for one attendance is not yet designed | OI-P01a-06; AP-CP-38 |
| AP-EIP-33 | Routing | Composed Message Processor | N/A | No composite messages | Part01 §8.2 |
| AP-EIP-34 | Routing | Scatter-Gather | N/A | Dashboard composition is client-side REST, not messaging | AP-MS-15 |
| AP-EIP-35 | Routing | Routing Slip | N/A | No multi-step routing | Part01 §8.4 |
| AP-EIP-36 | Routing | Process Manager | N/A | No orchestrated process | AP-MS-09 |
| AP-EIP-37 | Routing | Message Broker | Applied | One persistent broker per environment | Part01 §4.4, §6.1, §6.2 |
| AP-EIP-38 | Transformation | Message Translator | N/A | Producer and consumer use the same event schema | Part01 §8.2 |
| AP-EIP-39 | Transformation | Envelope Wrapper | Applied | Common envelope: event id, type, version, flow reference, trace context, acting user, time | Part01 §8.2, §9.9, §10.5 |
| AP-EIP-40 | Transformation | Content Enricher | Applied | SMS adds the current hourly wage rate from EIMS when generating a salary record | Part01 §8.2 (row 6); INT-05 |
| AP-EIP-41 | Transformation | Content Filter | N/A | No message reduced on the way | Part01 §8.2 |
| AP-EIP-42 | Transformation | Claim Check | N/A | Events are small | AP-CP-09 |
| AP-EIP-43 | Transformation | Normalizer | N/A | One producer, one format | Part01 §8.2 |
| AP-EIP-44 | Transformation | Canonical Data Model | N/A | Each service owns its model; only the envelope is common | D-18; AP-EIP-39 |
| AP-EIP-45 | Endpoints | Message Endpoint | Applied | AMS outbox relay and SMS event consumer | Part01 §8.3 |
| AP-EIP-46 | Endpoints | Messaging Gateway | Applied | Broker access confined to the AMS outbox relay and the SMS consumer | Part01 §6.3, §8.3 |
| AP-EIP-47 | Endpoints | Messaging Mapper | Applied | Events mapped to and from the schemas in `contracts/events` | Part01 §8.2; ADR-006 |
| AP-EIP-48 | Endpoints | Transactional Client | Applied | Outbox write in the business transaction; SMS processing and idempotency record in one transaction | Part01 §4.4, §8.3, §12 |
| AP-EIP-49 | Endpoints | Polling Consumer | N/A | The SMS consumer is event-driven | AP-EIP-50 |
| AP-EIP-50 | Endpoints | Event-Driven Consumer | Applied | SMS consumes events as they arrive | Part01 §4.4, §8.3 |
| AP-EIP-51 | Endpoints | Competing Consumers | Applied | As AP-CP-11 | Part01 §6.2, §8.3 |
| AP-EIP-52 | Endpoints | Message Dispatcher | N/A | One message type per consumer | Part01 §8.3 |
| AP-EIP-53 | Endpoints | Selective Consumer | N/A | SMS takes every attendance event | Part01 §8.3 |
| AP-EIP-54 | Endpoints | Durable Subscriber | Applied | Durable subscription for SMS | Part01 §4.4, §8.3; ADR-006 |
| AP-EIP-55 | Endpoints | Idempotent Receiver | Applied | Event id and attendance id checked before processing | Part01 §4.4, §8.5 |
| AP-EIP-56 | Endpoints | Service Activator | Applied | The consumer calls the salary generation or void operation | Part01 §8.2 |
| AP-EIP-57 | System management | Control Bus | N/A | Broker managed with platform tooling | Part01 §6.2 |
| AP-EIP-58 | System management | Detour | N/A | No message routing to detour | Part01 §8.3 |
| AP-EIP-59 | System management | Wire Tap | Applied | Publish and consume written to the activity log with the flow reference | Part01 §8.2 (row 14), §10.2 |
| AP-EIP-60 | System management | Message History | Applied | Flow reference and acting user carried in the envelope and logged at each step | Part01 §9.9, §10.5 |
| AP-EIP-61 | System management | Message Store | Applied | Published events kept in the AMS outbox table; clean-up rule in Part03 | Part01 §8.3, §17; Part03 (planned) |
| AP-EIP-62 | System management | Smart Proxy | N/A | No messaging request-reply | AP-EIP-18 |
| AP-EIP-63 | System management | Test Message | N/A | Health checks and alerts monitor the flow | Part01 §10.7 |
| AP-EIP-64 | System management | Channel Purger | N/A | Test environments are restored from snapshots | Part01 §14.5 |

### J. Integration principles (INT)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-INT-01 | Async by default between services | Events for state propagation; synchronous calls only when an immediate answer is needed | Applied | State change AMS → SMS by events; synchronous queries only where the user needs the answer at once | Part01 §8.4 |
| AP-INT-02 | Contract-first interfaces | OpenAPI for REST, schema for events, versioned | Applied | OpenAPI 3 contracts and event schemas in `contracts/`, versioned | Part01 §4.1, §8.2; D-16 |
| AP-INT-03 | Protocol selection guide | REST/HTTPS for queries and commands, broker (AMQP/JMS) for events, batch files for bulk | Applied | Selection guide in Part01; bulk by paged REST instead of files | Part01 §8.4 |
| AP-INT-04 | Authenticated integrations | Every call carries a user or service token; no anonymous endpoints | Applied | Relayed user token or service token on every call; broker credentials per service | Part01 §7.3, §9.9 |
| AP-INT-05 | Transport security | TLS on every connection | Partial | TLS at the edge and to the managed database on AWS; traffic inside the local cluster is not encrypted and is limited by network policies; mutual TLS / service mesh Future | Part01 §7.3, §16.1, §19 AR-04, §20.3 |
| AP-INT-06 | Correlation id propagation | One id carried across HTTP headers and message headers | Applied | Flow reference in the HTTP header and the event envelope | Part01 §4.1, §10.5 |
| AP-INT-07 | At-least-once delivery with idempotency | Consumers deduplicate by message id | Applied | Redelivery with backoff; SMS deduplicates by event id and attendance id | Part01 §8.5; ADR-006 |
| AP-INT-08 | Timeouts, retries and backoff | Bounded timeouts; retry only transient errors | Applied | Connect and response timeouts; reads retried with backoff; commands not retried automatically | Part01 §8.5 |
| AP-INT-09 | Dead-letter handling | Poison messages parked, alerted and replayable | Partial | Parked in the dead-letter queue and alerted; reconciliation repairs the outcome; replay procedure not yet defined | Part01 §8.3, §8.5, §10.7; OI-P01a-07 |
| AP-INT-10 | Event schema evolution | Backward-compatible changes; version in the envelope | Applied | Version in the envelope; compatibility rules in the API standard | Part01 §8.2; docs/04-standards/api-and-integration (planned); OI-P01a-11 |
| AP-INT-11 | Canonical event envelope | Standard header fields (id, type, version, time, source, correlation id) | Applied | Common envelope with event id, type, version, flow reference and time | Part01 §8.2; Part02 (planned) |
| AP-INT-12 | Reconciliation for eventual consistency | Scheduled check repairs missed events | Applied | Nightly reconciliation creates missing and voids stale salary records | Part01 §4.1, §8.2 (row 3); ADR-006 |
| AP-INT-13 | Connection management | Pooled connections, keep-alive, limits per client | Applied | Pooled database and HTTP connections; limits in the performance standard | Part01 §14.9; docs/04-standards/performance-and-scalability (planned) |

### K. Data architecture (DATA)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-DATA-01 | Single source of truth | Each data item owned by exactly one service | Applied | Each entity owned by one module; others read through its API | Part01 §12; C-02 |
| AP-DATA-02 | No cross-service joins | Data from other services obtained via API or events | Applied | APIs and events only; no cross-database queries | Part01 §8.4, §12 |
| AP-DATA-03 | Schema migration as code | Versioned migrations (e.g. Flyway) run by the pipeline | Applied | Versioned migration scripts per service, applied when the service starts after a pipeline deployment | Part01 §11.1, §12; D-112 |
| AP-DATA-04 | Soft delete | Records flagged inactive, never physically deleted | Applied | Records never physically deleted | Part01 §12; BR-CMN-06 |
| AP-DATA-05 | Standard audit columns | created/updated by and at on every table | Applied | Audit fields on every business record | Part01 §12; BR-CMN-02, BR-CMN-07 |
| AP-DATA-06 | Optimistic locking | Version column prevents lost updates | Applied | Version on every record; stale updates refused | Part01 §8.4, §12; FR-CMN-014 |
| AP-DATA-07 | Referential integrity policy | Within a service: DB foreign keys; across services: application checks | Applied | Foreign keys inside a database only; cross-service checks by API (e.g. INT-09) | Part01 §8.2, §12; Part03 (planned) |
| AP-DATA-08 | Read / write separation | Reporting reads separated from transactional writes where needed | N/A | Small volumes; no reporting workload in the POC | Part01 §17 |
| AP-DATA-09 | Caching strategy | What is cached, TTL, invalidation | Partial | Short-lived in-memory copies of employee and approver details only; shared cache Future | Part01 §12, §20.3; D-110 |
| AP-DATA-10 | Data classification | Personal and sensitive data identified and tagged | Applied | Sensitive attributes classified in the BRD; masked in logs | Part01 §10.8; D-71, D-93; Part03 (planned) |
| AP-DATA-11 | Retention & archival | Retention period and archival per entity | Applied | Business records and audit kept with the record; logs 90 days in Prod; outbox clean-up in Part03; no archival needed at these volumes | Part01 §10.8, §17; FR-ADM-103; Part03 (planned) |
| AP-DATA-12 | Backup & restore | RPO / RTO defined and tested | Applied | Daily backup, RPO 24 h, RTO 8 h; restore tested before go-live and monthly | Part01 §6.4, §12; NFR-02 |
| AP-DATA-13 | UTC storage of timestamps | Stored in UTC, displayed in user time zone | Applied | Timestamps stored in UTC and shown in IST; business dates stored as dates | Part01 §10.3; BR-CMN-18, A-01; D-117; Part03 (planned) |
| AP-DATA-14 | Naming conventions | Consistent table, column and key naming | Applied | Conventions in the data model anchor and the database standard | Part03 (planned); docs/04-standards/database-and-data (planned) |
| AP-DATA-15 | Business keys vs surrogate keys | Immutable business id alongside technical primary key | Applied | Business ids (e.g. Employee Id) kept alongside technical keys; key design per entity in Part03 | FR-UM-001; Part03 (planned) |
| AP-DATA-16 | Immutable approved records | Approved / financial records changed only by new versions | Partial | Salary records are voided and regenerated, never changed; profile changes go through change requests; approved attendance can be reopened by business rule | D-70, D-78, D-90; Part03 (planned) |
| AP-DATA-17 | Pagination for lists | All list queries paginated server-side | Applied | List APIs and the reconciliation query paged server-side | Part01 §8.2 (row 3), §8.4; Part02 (planned) |

### L. Security architecture (SEC)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-SEC-01 | Zero trust | Every request authenticated and authorized, inside or outside the network | Partial | Every request carries a token validated at gateway and service, with role and data-scope checks; no mutual TLS inside the cluster; service mesh Future | Part01 §9.8, §9.9, §20.3 |
| AP-SEC-02 | Least privilege | Users, services and pipelines get only the access they need | Applied | Role data scopes; service clients with only the roles they need; own database user per service; namespace-scoped deploy account | Part01 §9.1, §9.2, §7.3 |
| AP-SEC-03 | Defense in depth | Layered controls: network, gateway, service, data | Applied | WAF at the edge, network policies, gateway checks, service and query checks, encrypted disks | Part01 §16.1 |
| AP-SEC-04 | Secure by default | Deny by default; features opened explicitly | Applied | Network policies deny all other flows; gateway routes deny by default; unused identity-provider features disabled | Part01 §6.3, §9.2, §16.2 |
| AP-SEC-05 | Centralized identity (OAuth2 / OIDC) | One identity provider issues tokens | Applied | One OIDC identity provider realm per environment | Part01 §9.2; ADR-003 |
| AP-SEC-06 | Token validation at gateway and service | JWT signature, expiry, audience checked at both layers | Applied | Signature, issuer, audience, expiry checked at gateway and in every service | Part01 §9.8 |
| AP-SEC-07 | Role-based access control | Permissions by role, enforced on API and UI | Applied | Roles Employee, Manager, Admin; route, operation and data-scope checks; menu by role | Part01 §9.7; FR-UM-013 |
| AP-SEC-08 | Multi-factor authentication | MFA policy per user type | Deferred | No MFA in the POC; can be enabled by configuration later, starting with the PMS Administrator | Part01 §9.4, §20.3; D-109 |
| AP-SEC-09 | Password & session policy | Complexity, lockout, idle timeout, session expiry | Applied | Password policy, lock after 5 failures, 30 minutes idle, 10 hours absolute | Part01 §9.2, §9.6; D-26, D-28 |
| AP-SEC-10 | Secrets management | Secrets in a vault, rotated, never in code | Partial | Platform secrets per service from protected pipeline secrets, rotated per release; cloud secret store only on AWS | Part01 §9.10, §19 AR-04; D-110 |
| AP-SEC-11 | Encryption in transit | TLS 1.2+ everywhere | Partial | TLS 1.2+ at the edge with HSTS and to the managed database on AWS; not inside the local cluster; mutual TLS Future | Part01 §16.1, §19 AR-04, §20.3 |
| AP-SEC-12 | Encryption at rest | Databases, storage and backups encrypted | Applied | Workstation and backup drives encrypted by the operating system; managed encryption on AWS | Part01 §16.1; D-114 |
| AP-SEC-13 | Input validation & output encoding | Prevent injection and XSS | Applied | Contract and BRD rule validation; parameterised queries; output encoding by the UI library; WAF rule set | Part01 §16.2 A03 |
| AP-SEC-14 | API protection | Rate limiting, CORS, security headers, size limits | Applied | Rate limits, single origin, security headers, 1 MB payload limit | Part01 §9.8 |
| AP-SEC-15 | OWASP Top 10 coverage | Each category mapped to a control | Applied | Each category mapped to a control | Part01 §16.2 |
| AP-SEC-16 | Threat modelling | STRIDE (or similar) per component at design time | Partial | Threat review in the security and privacy part of each Part02 function design; method not yet chosen | Part01 §16.2 A04; D-38; OI-P01a-08 |
| AP-SEC-17 | Dependency scanning & SBOM | Vulnerable libraries blocked in the pipeline | Partial | Dependency and image scans block high and critical findings; SBOM not yet defined | Part01 §15, §16.1; OI-P01a-09 |
| AP-SEC-18 | SAST / DAST | Static and dynamic security testing in the pipeline | Partial | Static code scanning as a pipeline gate; security testing in QA; dynamic scanning not yet defined | Part01 §15, §16.1; OI-P01a-10 |
| AP-SEC-19 | Audit trail | Security-relevant actions logged, tamper-evident | Applied | Identity-provider security events and refused requests in the security log; audit entries cannot be changed or deleted | Part01 §10.2; FR-AUTH-030, FR-ADM-103 |
| AP-SEC-20 | Personal data masking | No personal data in logs or non-production data | Applied | Log allow-list with masking in the collector; synthetic data in every non-production environment | Part01 §10.8; R-04, NFR-SUP-04 |

### M. Logging & observability (OBS)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-OBS-01 | Unified & centralized logging | All nodes ship logs to one platform | Applied | Every component ships logs, metrics and traces to one collector and central stores | Part01 §10.1 |
| AP-OBS-02 | Structured logs | JSON with a standard field set | Applied | Structured JSON with the standard log record | Part01 §10.3 |
| AP-OBS-03 | Correlation & trace ids | Every log line carries correlation and trace ids | Applied | Flow reference and trace and span ids are mandatory fields | Part01 §10.3, §10.5 |
| AP-OBS-04 | Standard log levels | Agreed meaning of ERROR / WARN / INFO / DEBUG | Applied | Four levels with a level policy per node; no DEBUG in Prod | Part01 §10.3, §10.4 |
| AP-OBS-05 | Business event logging | Business events logged for business KPIs | Applied | Event publish and consume and job runs logged; business KPIs derived from logs | Part01 §10.2, §10.6 |
| AP-OBS-06 | System metrics (RED / USE) | Rate, errors, duration; utilization, saturation, errors | Applied | Request rate, error rate and p95 latency; database storage, queue depth and outbox backlog | Part01 §10.6, §10.7 |
| AP-OBS-07 | Distributed tracing | OpenTelemetry traces across gateway, services and broker | Applied | Trace context across gateway, services and events; 100 % sampling in the POC | Part01 §10.5 |
| AP-OBS-08 | Health & readiness probes | Liveness and readiness endpoints per service | Applied | Probes per component, inside the cluster only | Part01 §9.8, §10.7 |
| AP-OBS-09 | Dashboards | Business and system dashboards | Applied | Integration, operations, business quality, service health, performance, security and business activity dashboards | Part01 §10.6 |
| AP-OBS-10 | SLO-based alerting | Alerts on SLO breaches, not raw noise | Applied | Alert thresholds derived from NFR-01 and NFR-02 with duration windows; email to IT operations | Part01 §10.7; D-111 |
| AP-OBS-11 | Log retention | Retention per log type | Applied | Prod 90 days, Dev / QA and platform 14 days; audit with the record | Part01 §10.2, §10.8; D-101 |
| AP-OBS-12 | Audit log separate from technical log | Business audit in the database; technical logs in the log platform | Applied | Audit tables in each module database; activity and security logs in the log store | Part01 §10.1, §10.2 |

### N. Performance & scalability (PERF)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-PERF-01 | Performance budgets | Response-time targets per screen / API | Applied | Page load p95 ≤ 2 s, API p95 ≤ 500 ms, salary record ≤ 1 minute, reconciliation < 5 minutes | Part01 §14.1; NFR-01 |
| AP-PERF-02 | Horizontal scaling | Stateless instances added under load | Applied | Replicas added per service | Part01 §6.2; NFR-07 |
| AP-PERF-03 | Caching | Reference data and expensive reads cached | Partial | Short-lived in-memory copies of read-mostly data; shared cache Future | Part01 §12, §20.3; D-110 |
| AP-PERF-04 | Async processing for heavy work | Long tasks moved off the request path | Applied | Salary generation by event after approval; reconciliation as a nightly job | Part01 §8.2; ADR-006 |
| AP-PERF-05 | Connection pooling | DB and HTTP connections pooled | Applied | As AP-INT-13 | Part01 §14.9; docs/04-standards/performance-and-scalability (planned) |
| AP-PERF-06 | Efficient queries | Indexes, no N+1, projections | Applied | Indexes per entity; data scope applied in the query; heaviest reads load-tested | Part01 §9.7, §14.2 (PT-06), §16.3; Part03 (planned) |
| AP-PERF-07 | Payload efficiency | Pagination, compression, minimal payloads | Applied | Server-side paging; 1 MB payload limit; details in the performance standard | Part01 §8.4, §9.8; docs/04-standards/performance-and-scalability (planned) |
| AP-PERF-08 | Static content via CDN | Frontend assets served from edge | N/A | Internal users at one site; the static web server behind the edge serves the assets | A-01, A-03; Part01 §6.1 |
| AP-PERF-09 | Capacity planning | Sizing from volumetrics, reviewed yearly | Applied | Sizing from the volumetrics with 20 % headroom, load-tested to 2× | Part01 §17; NFR-07 |
| AP-PERF-10 | Performance testing | Load, stress, soak, spike before go-live | Applied | Load, stress, soak and spike tests; final verification in the AWS production simulation | Part01 §14 |

### O. Resilience & availability (RES)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-RES-01 | Timeouts everywhere | Every remote call bounded | Applied | Connect and response timeouts per integration type; consumer processing limit | Part01 §8.5 |
| AP-RES-02 | Retry with backoff and jitter | Transient errors retried safely | Applied | Reads retried with exponential backoff; broker redelivery with backoff; jitter in the resilience standard | Part01 §8.5; docs/04-standards/resilience-and-availability (planned) |
| AP-RES-03 | Circuit breaking | Failing dependencies isolated | Applied | Circuit breaker per downstream service | Part01 §8.5 |
| AP-RES-04 | Bulkheads | Resource pools per dependency | Partial | Isolation per service, database and credentials; separate resource pools per dependency inside a service not yet defined | Part01 §4.3; OI-P01a-12 |
| AP-RES-05 | Graceful degradation | Partial functionality when a dependency is down | Applied | Dashboard cards fail on their own with Retry; approval does not wait for SMS; salary status shown as unknown with Retry | Part01 §8.2; FR-CMN-008 |
| AP-RES-06 | Redundancy across zones | No single point of failure | Partial | 2 replicas per stateless tier in one zone; single-node database and broker; multi-AZ, database replica and clustered broker Future | Part01 §6.4, §19 AR-03, §20.3; D-109 |
| AP-RES-07 | RTO / RPO targets | Recovery objectives defined and tested | Applied | RPO 24 h, RTO 8 h; restore tested before go-live and monthly | Part01 §12; NFR-02; D-112 |
| AP-RES-08 | Idempotent operations | Safe to retry writes | Applied | Event processing idempotent; commands carry the record version and repeated submits are refused by status rules | Part01 §8.5 |
| AP-RES-09 | Self-healing | Failed instances replaced automatically | Applied | The platform restarts failed instances and routes to healthy ones | Part01 §6.4 |
| AP-RES-10 | Failure injection | Planned tests of failure scenarios | Partial | Replica failover demonstrated locally; restore tests; spike test recovery; no planned failure-injection test set yet | Part01 §6.4, §14.4; OI-P01a-13 |

### P. DevOps & continuous delivery (DEV)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-DEV-01 | CI/CD pipeline per service | Build, test, scan, deploy automated | Applied | One path-filtered pipeline per service and platform component | Part01 §15; D-18 |
| AP-DEV-02 | Branching strategy | Agreed model (e.g. trunk-based) with protected main | Applied | Trunk-based with short-lived branches and reviewed pull requests to main | Part01 §15; D-112 |
| AP-DEV-03 | Infrastructure as code | All environments from code | Applied | Deployment charts per component; infrastructure code for AWS | Part01 §11.2; D-110 |
| AP-DEV-04 | Build once, deploy many | Same immutable artifact promoted across environments | Applied | Images built once with immutable tags and promoted Dev → QA → Prod | Part01 §15, §16.1, §16.2 A08 |
| AP-DEV-05 | Containerization | Services packaged as container images | Applied | One container image per component | Part01 §7.2; D-11 |
| AP-DEV-06 | Automated quality gates | Coverage, static analysis, security scan block merges | Applied | Coverage ≥ 80 %, contract tests, code, dependency, image and secret scans with no high or critical findings | Part01 §15; D-112 |
| AP-DEV-07 | Deployment strategy | Rolling / blue-green with rollback | Partial | Pipeline deploys per environment with 2 replicas in Prod; rollout and rollback approach not yet defined | Part01 §6.4, §15; OI-P01a-14 |
| AP-DEV-08 | Feature toggles | Incomplete features hidden in production | Partial | Incomplete work kept out of Prod by release tags and product-owner approval; feature toggles not yet decided | Part01 §15; OI-P01a-15 |
| AP-DEV-09 | Semantic versioning | Versions for services, APIs and events | Partial | Release tags drive QA and Prod deployment; version scheme not yet defined | Part01 §15; OI-P01a-11 |
| AP-DEV-10 | Automated database migrations | Migrations run in the pipeline, reversible plan | Partial | Versioned migrations applied automatically on deployment; backup before release and reversal plan not yet defined | Part01 §11.1, §12; OI-P01a-16 |
| AP-DEV-11 | No secrets in repository | Secret scanning in pipeline | Applied | Secret scanning as a pipeline gate; secrets only in protected pipeline secrets | Part01 §9.10, §15 |

### Q. Testing & quality (QA)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-QA-01 | Test pyramid | Many unit, fewer integration, few end-to-end tests | Applied | Unit, component, contract, integration, end-to-end and load tests at their pipeline stages | Part01 §15 |
| AP-QA-02 | Coverage targets | Unit test and code-quality thresholds enforced | Applied | Coverage ≥ 80 % and no high or critical findings as gates | Part01 §15; D-112 |
| AP-QA-03 | Contract testing | API and event contracts verified on both sides | Applied | Providers and consumers verified against `contracts/` in the pipeline | Part01 §15; D-117 |
| AP-QA-04 | Integration tests with real dependencies | Containers for DB and broker in tests | Applied | Containerised database, broker and identity provider in tests | Part01 §11.1; D-16 |
| AP-QA-05 | End-to-end tests | Critical journeys automated | Applied | End-to-end UI tests in QA, with accessibility checks | Part01 §15, §16.3 |
| AP-QA-06 | Performance tests | Per PT strategy | Applied | PT-01 to PT-08 per the strategy | Part01 §14 |
| AP-QA-07 | Security tests | Per security testing plan | Applied | Security testing in QA: direct-link tests per role and screen, sign-in behaviour, log review | Part01 §15, §16.3; NFR-SUP-02; docs/04-standards/testing-and-quality (planned) |
| AP-QA-08 | Test data management | Synthetic data; no production personal data | Applied | Synthetic seed and performance-test data; snapshot restore before each run | Part01 §13, §14.5; R-04 |
| AP-QA-09 | Shift-left quality | Reviews, static checks and tests early | Applied | Design approved before build; pull-request review, scans and tests on every change | Part01 §3.1, §15 |
| AP-QA-10 | Definition of done | Agreed checklist per story | Partial | Pipeline gates and acceptance criteria per requirement exist; the definition-of-done checklist is not yet written | Part01 §15; OI-P01a-17 |

### R. Delivery governance & knowledge management (DG)

Group R follows D-116: tool-neutral wording; linked to OBJ-05, KPI-05 and OBJ-06 area 12.

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-DG-01 | Human review | Every artifact is reviewed and approved by an accountable person | Applied | Every document reviewed section by section and approved by the accountable owner; each approval recorded in the decision log | §1; decision log; D-60, D-116 |
| AP-DG-02 | Traceable output | Artifacts state their inputs and the decisions they implement | Applied | Every document lists its reference documents and cites requirement and decision ids | Part01 §2.1; KPI-05; D-116 |
| AP-DG-03 | Layered project knowledge | Organisation, project, user and session knowledge kept separate | Applied | Organisation standards, project rules and documents, personal settings and session notes kept in separate layers of the repository | D-116 |
| AP-DG-04 | Guardrail rules | Project rules restrict which delivery tools may be used | Applied | Standing project rules, each traced to a decision, restrict the delivery tools and reference sources used | D-17, D-54, D-60, D-116 |
| AP-DG-05 | Curated knowledge base | Only approved project documents are used as delivery inputs | Applied | Only the repository documents and approved decisions are used as inputs; superseded reference material excluded | D-54, D-116 |

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
| OI-P01a-04 | Consumer-driven contract tests in addition to schema-based contract verification | AP-MS-26 | Enterprise Architect | docs/04-standards/testing-and-quality |
| OI-P01a-05 | Service template: content and upkeep of the template copied per service (framework, security, observability, error body, flow reference) without a shared runtime library (D-18) | AP-MS-30 | Enterprise Architect | docs/04-standards/coding-and-code-review |
| OI-P01a-06 | Ordering of attendance approved and reopened events for the same attendance (late or out-of-order delivery) | AP-CP-38, AP-EIP-32 | Enterprise Architect | Part02 anchor (event conventions) |
| OI-P01a-07 | Dead-letter queue: inspection and replay procedure for IT operations | AP-INT-09 | Enterprise Architect | docs/04-standards/api-and-integration |
| OI-P01a-08 | Threat-modelling method (e.g. STRIDE) for the security and privacy part of each Part02 function | AP-SEC-16 | Enterprise Architect | docs/04-standards/security, before Part02 modules |
| OI-P01a-09 | Software bill of materials: whether and how it is produced per image | AP-SEC-17 | Enterprise Architect | docs/04-standards/devops-and-cicd |
| OI-P01a-10 | Dynamic application security testing: whether and where it runs (e.g. QA) | AP-SEC-18 | Enterprise Architect | docs/04-standards/testing-and-quality |
| OI-P01a-11 | Version scheme for services, APIs and events, and compatibility rules | AP-MS-33, AP-INT-10, AP-DEV-09 | Enterprise Architect | docs/04-standards/api-and-integration |
| OI-P01a-12 | Bulkheads inside a service: separate connection and thread pools per downstream dependency | AP-RES-04 | Enterprise Architect | docs/04-standards/resilience-and-availability |
| OI-P01a-13 | Planned failure-injection tests (instance, broker, database and dependency failure) and where they run | AP-RES-10 | Enterprise Architect | docs/04-standards/testing-and-quality |
| OI-P01a-14 | Deployment rollout and rollback approach (e.g. rolling update with rollback to the previous release) | AP-DEV-07 | Enterprise Architect | docs/04-standards/devops-and-cicd |
| OI-P01a-15 | Whether feature toggles are used, and how | AP-DEV-08 | Enterprise Architect | docs/04-standards/devops-and-cicd |
| OI-P01a-16 | Database migration reversal plan (backward-compatible changes, backup before release, roll-forward or restore) | AP-DEV-10 | Enterprise Architect | docs/04-standards/database-and-data |
| OI-P01a-17 | Definition-of-done checklist per story | AP-QA-10 | Enterprise Architect | docs/04-standards/documentation-and-governance |
