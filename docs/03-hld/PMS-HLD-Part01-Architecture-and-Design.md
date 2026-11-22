# PMS – HLD Part01: Application Architecture & Design

Document ID: PMS-HLD-Part01-Architecture-and-Design-v1.0
Project: Payroll Management System (PMS) – proof of concept (POC), Stage 3 Solution Design
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 22-Nov-2026 | Rajesh Verma | First draft of §1–§4, based on the approved BRD set v1.0 (D-107), UX v1.1 (D-105) and decisions D-01 to D-108; Part01 design answers of 22 Nov 2026 (D-109) |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 22-Nov-2026 | §1–§4 approved (D-109); full document pending |
| Product owner | Rajesh Verma | 22-Nov-2026 | §1–§4 approved (D-109); full document pending |

## 2. Introduction

This document describes the overall architecture and design of the Payroll Management System (PMS). It is a Big Design Up Front (BDUF) artifact: it must be approved before implementation starts (D-108).

It is the first of the 14 HLD documents of Stage 3 (D-108). Principles, patterns and the architecture decision register are catalogued in PMS-HLD-Part01a-Principles-Patterns-Decisions; functional design per module is in Part02 and the data model in Part03. Requirements are referenced by their BRD ids (INT, JOB, NFR, C, DEP, R, FR, BR) and not repeated here.

The design is technology-neutral wherever the replatforming goal requires it (D-12, NFR-08): products are named only in §6.2 (cloud mapping), §7 (deployment), §9.2 (identity provider) and §11 (technology stack).

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | PMS-BRD (anchor), PMS-BRD-M1-EIMS, PMS-BRD-M2-AMS, PMS-BRD-M3-LMS, PMS-BRD-M4-SMS, PMS-BRD-M5-SUP | v1.0 – approved baseline (D-107) |
| 2 | UX Journey Index and 17 UX Summaries (with HTML mockups) | v1.1 (D-105) |
| 3 | Decision log / ADRs | D-01 to D-109; ADR-001 to ADR-003 |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | PMS-HLD-Part01-Architecture-and-Design | Overall architecture and design (this document) |
| 2 | PMS-HLD-Part01a-Principles-Patterns-Decisions | Catalogue of principles and patterns with applicability and realization; ADR register (§5) and format (§6) |
| 3 | PMS-HLD-Part02-Functional (anchor) | Module and function index, cross-module flows, common API / event / error / audit / frontend conventions, roll-up inventories, requirement coverage |
| 4 | PMS-HLD-Part02-M1-EIMS-Functional, PMS-HLD-Part02-M2-AMS-Functional, PMS-HLD-Part02-M3-LMS-Functional, PMS-HLD-Part02-M4-SMS-Functional | Solution approach for the system functions of each functional module |
| 5 | PMS-HLD-Part02-M5-SUP-Functional | Solution approach for the supporting functions (UM, AUTH, audit and activity log) |
| 6 | PMS-HLD-Part03-Datamodel (anchor) | Data conventions, ownership, entity index, master ER, cross-service consistency |
| 7 | PMS-HLD-Part03-M1-EIMS-Datamodel to PMS-HLD-Part03-M4-SMS-Datamodel, PMS-HLD-Part03-M5-SUP-Datamodel | Entity definitions per module |
| 8 | Standards and guardrails (`docs/04-standards/`) | The 12 OBJ-06 areas (D-61): architecture and design; frontend and UX; API and integration; coding and code review; database and data management; security; logging and observability; performance and scalability; resilience and availability; testing and quality; DevOps, CI/CD and deployment; documentation, traceability and delivery governance. Written after the HLD documents (D-108) |

### 2.2 Application overview

#### 2.2.1 Business background

PMS is a lightweight payroll application built as a proof of concept (D-06). Its purpose is to prove a governed end-to-end delivery approach, with a formal approval gate at each step, and to produce a reusable set of standards and guardrails (OBJ-05, OBJ-06). The business scope is the core of hourly payroll for a single company in India, in IST and INR (A-01).

Users are about 100 employees in year 1, about 10 of them managers, and one PMS Administrator (BRD §8.1). Every business record is entered by the employee and approved by the manager (by the Administrator for the top-level employee), and no wage is ever entered by hand (BR-CMN-01, BR-CMN-08, KPI-02).

The main flow (BRD §5.1) runs from onboarding an employee, through profile approval, daily attendance and leave, to a salary record generated automatically from each approved attendance day, approved by the manager and accepted or disputed by the employee; a dispute is closed with Keep as is or by reopening the attendance. A nightly reconciliation makes sure every approved attendance day has exactly one valid salary record (JOB-CMN-01, KPI-04).

#### 2.2.2 Application background

**Modules.** Four functional modules, each a separate microservice with its own database (D-10, C-01, C-02): EIMS – employee master data, profile approval and profile change requests; AMS – daily attendance; LMS – full-day leave; SMS – daily wages generated from approved attendance, with approval, acceptance and disputes. A shell provides sign-in, the role-based layout and menu, the dashboard and the approvals inbox (BRD §5.3).

**Supporting capabilities.** User and access management (UM) and authentication and session (AUTH), provided by the identity provider with the EIMS Admin screens as the user interface; the audit log and the activity log with one flow reference per user action or job run (BR-CMN-19, NFR-09). Administration, notifications and document management are Phase 2 (D-57).

**Architecture in one paragraph.** Microservices decomposed by business capability, one database per service and contracts-only sharing (D-10, D-16, D-18). A single-page web frontend in which each module's screens are built into one shell application at build time (D-23, ADR-001). All browser calls pass through an API gateway, which validates the access token and routes to the module services; module services expose contract-first REST APIs (D-16). Users sign in at a standards-based identity provider that holds accounts, roles, passwords, lockout and sessions and issues signed tokens (D-16, D-26, D-29; D-109). The AMS → SMS hand-overs are asynchronous events through a message broker, written with a transactional outbox and backed by the nightly reconciliation (INT-01, INT-02, JOB-CMN-01, D-16, D-21). Every service and the identity provider use a relational database, one per service. Everything runs as containers on a container orchestration platform, deployed on-premises for the POC and designed to move unchanged to a public cloud (AWS) later (D-109); Development, QA and Production environments (D-11).

**Peripheral systems.** The identity provider is the only system outside the module services that PMS integrates with (INT-08, DEP-01); it is part of the PMS platform. There are no external business systems: no email or SMS gateway (C-05), no single sign-on (BRD §3.3) and no biometric or clock-in devices. The Administrator sends temporary passwords by company email outside PMS (FR-AUTH-013). IT operations read the activity log and the identity provider's security events for investigation (FR-ADM-105, FR-ADM-116, FR-AUTH-030).

## 3. Architecture approach & governance (BDUF)

### 3.1 Design-before-build artifact checklist

Implementation starts only when every mandatory artifact below is approved. The Stage 3 plan and order are in D-108; the gate is the Stage 3 sign-off.

| # | Artifact | Document / section | Mandatory before build | Stakeholders to align | Status | Approved on |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Functional architecture | Part01 §5 | Yes | Product owner, BA | Not started | |
| 2 | System architecture | Part01 §6 | Yes | Architect, IT operations / infrastructure, Security / IT owner | Not started | |
| 3 | Deployment architecture | Part01 §7 | Yes | Architect, IT operations / infrastructure, DevOps | Not started | |
| 4 | Integration architecture | Part01 §8 | Yes | Architect, module dev leads | Not started | |
| 5 | Authentication & authorization | Part01 §9 | Yes | Security / IT owner, Architect | Not started | |
| 6 | Logging & observability | Part01 §10 | Yes | IT operations, Architect | Not started | |
| 7 | Principles & patterns compliance | Part01a | Yes | Architect | Not started (after Part01, D-108) | |
| 8 | Functional HLDs per module | Part02 anchor, M1-EIMS to M4-SMS, M5-SUP | Yes | BA, HR Manager, Finance Manager, dev leads | Not started | |
| 9 | Data model | Part03 anchor, M1-EIMS to M4-SMS, M5-SUP | Yes | Architect, DBA | Not started | |
| 10 | API and event contracts | `contracts/openapi`, `contracts/events` | Yes | Dev leads | Not started (from Part02) | |
| 11 | Performance test strategy & plan | Part01 §14 | Before PT | QA, IT operations | Not started | |
| 12 | Standards & guardrails | `docs/04-standards/` (12 areas, D-61) | Yes | Architect, dev leads | Not started (after the HLD documents, D-108) | |

### 3.2 Stakeholder alignment log

| Date | Topic / artifact | Stakeholders | Outcome | Decision ref |
| --- | --- | --- | --- | --- |
| 15 Nov 2026 | Architecture style and technology stack | Product owner | One microservice and one database per module; frontend, database, container, pipeline and test technology (§11) and Dev/QA/Prod; backend technology first, replatformed later; gateway, identity provider, event-driven AMS → SMS with outbox and reconciliation, contract-first APIs; single repository with independent services; broker edition; build-time frontend composition | D-10, D-11, D-12, D-16, D-18, D-21, D-23 (ADR-001) |
| 16 Nov 2026 | Security policy | Product owner | Idle timeout 30 minutes, lock 15 minutes after 5 failed sign-ins, password policy, role held in the identity provider | D-26, D-28, D-29 |
| 18 Nov 2026 | Scope, roles, NFR targets, standards | Product owner | UM and AUTH in the POC, ADM / NM / DM Phase 2; Admin and manager data scope; NFR targets and volumetrics; 12 OBJ-06 standards areas | D-57, D-58, D-59, D-61, D-63 |
| 20 Nov 2026 | SUP rules, audit and activity log | Product owner | Session, account and security-event rules; own password change ends other sessions; audit log and activity log with flow reference, masking, 90-day retention | D-97, D-100, D-101 |
| 21 Nov 2026 | BRD set sign-off and Stage 3 plan | Product owner; BA, HR Manager, Finance Manager, Security / IT owner (BRD review) | BRD set v1.0 approved; HLD order and dates | D-106, D-107, D-108 |
| 22 Nov 2026 | Part01 architecture questions | Product owner, Enterprise Architect | Hosting on-premises first, AWS as the later cloud target (Azure dropped); container orchestration platform; identity provider issues tokens and holds passwords; network zones; per-tier redundancy; data tier; environments; no data migration; no MFA in the POC | D-109; ADR-002, ADR-003 |

## 4. Architecture principles & patterns

The full catalogue (Part01a) assesses every principle and pattern. This chapter summarizes compliance with the design known today; catalogue ids are those of the Part01a catalogue. Part01a is drafted after this document (D-108) and confirms or corrects the entries below.

### 4.1 Compliance summary by group

Counts are filled when Part01a is assessed (open item OI-P01-01). Key items are those already fixed by approved decisions.

| Group (Part01a) | Applied | Partial | Deferred | N/A | Key items |
| --- | --- | --- | --- | --- | --- |
| A. Architecture approach & governance (GOV) | Part01a | Part01a | Part01a | Part01a | BDUF gate per stage (§3.1, D-108); decision log and ADRs; BRD → HLD → code → test traceability (KPI-05) |
| B. X-First principles (XF) | Part01a | Part01a | Part01a | Part01a | §4.2 |
| C. Well-architected qualities (WA) | Part01a | Part01a | Part01a | Part01a | §4.3 |
| D. Software design principles (SD) | Part01a | Part01a | Part01a | Part01a | Technology-neutral design (D-12) |
| E. Twelve-Factor App (TF) | Part01a | Part01a | Part01a | Part01a | Containers; configuration by deployment setting (D-97); stateless services |
| F. Frontend & experience architecture (FE) | Part01a | Part01a | Part01a | Part01a | Shell with build-time module packages (ADR-001); WCAG 2.1 AA (NFR-04) |
| G. Microservice design patterns (MS) | Part01a | Part01a | Part01a | Part01a | §4.4 |
| H. Cloud design patterns (CP) | Part01a | Part01a | Part01a | Part01a | §4.4 |
| I. Enterprise integration patterns (EIP) | Part01a | Part01a | Part01a | Part01a | §4.4 |
| J. Integration principles (INT) | Part01a | Part01a | Part01a | Part01a | Contract-first (AP-INT-02); correlation id (AP-INT-06); reconciliation (AP-INT-12) |
| K. Data architecture (DATA) | Part01a | Part01a | Part01a | Part01a | Database per service, no cross-database keys; soft delete (BR-CMN-06) |
| L. Security architecture (SEC) | Part01a | Part01a | Part01a | Part01a | Identity provider; role and data-scope check on every request (NFR-03, FR-UM-013) |
| M. Logging & observability (OBS) | Part01a | Part01a | Part01a | Part01a | Activity log with flow reference; audit log (NFR-09, BR-CMN-19) |
| N. Performance & scalability (PERF) | Part01a | Part01a | Part01a | Part01a | NFR-01, NFR-07; automated load tests (D-11) |
| O. Resilience & availability (RES) | Part01a | Part01a | Part01a | Part01a | Outbox and nightly reconciliation; per-card dashboard loading (FR-CMN-008) |
| P. DevOps & continuous delivery (DEV) | Part01a | Part01a | Part01a | Part01a | Path-filtered pipelines per service (D-18) |
| Q. Testing & quality (QA) | Part01a | Part01a | Part01a | Part01a | Unit, component and container-based integration tests; end-to-end UI tests; load tests (D-11, D-16) |
| R. AI-assisted delivery (AI) | Part01a | Part01a | Part01a | Part01a | Assessed in Part01a |

### 4.2 X-First principles

| Principle | How the design complies | Ref |
| --- | --- | --- |
| UX first (AP-XF-01) | All 30 user journeys and 17 screens were designed and approved with the business before the BRD and the HLD (experience-led design); the HLD designs against the approved UX v1.1 | D-13, D-14, D-34, D-105, C-07 |
| API first / contract first (AP-XF-02) | Every service capability is an OpenAPI 3 contract and every event a versioned schema, kept in `contracts/` and written before implementation; services share contracts only | D-16, D-18 |
| Security first (AP-XF-03) | Sign-in, passwords, lockout and sessions at the identity provider; tokens validated at the gateway and again in each service; role and data scope checked on every request, never by hiding menu items alone; least-privilege Admin scope; sensitive data masked in logs | NFR-03, FR-UM-013, FR-UM-015, D-58, D-101; §9, §16 |
| Performance first (AP-XF-04) | Response, hand-over and batch targets fixed before design; performance test strategy and plan in this document; load profile from the BRD volumetrics | NFR-01, NFR-07, BRD §8.1; §14, §17 |
| Cloud first (AP-XF-05) – adapted: cloud-ready | The POC runs on-premises; the design stays cloud-ready: containers on a container orchestration platform, configuration outside the images, no on-premises-only products, and every component mapped to an AWS service in §6.2 | Proposed D-109; NFR-08 |
| Data first (AP-XF-06) | Data ownership is fixed per module before services are built; one database per service; entities modelled in Part03 before code | D-10, C-02, D-43 |
| Privacy by design (AP-XF-11) | Sensitive attributes classified (D-71, D-93); visible only within the role's data scope; masked in the activity log; synthetic test data only | NFR-EIMS-01, FR-ADM-115, R-04 |
| Observability first (AP-XF-07) | Activity log for every operation, job and event with one flow reference across modules, shown in system error messages; audit log for every data change | NFR-09, BR-CMN-19, FR-ADM-111 to 117; §10 |
| Automation first (AP-XF-08) | Every service built, tested and deployed by its own pipeline; tests automated at unit, component, integration, end-to-end and load level | D-11, D-16, D-18; §15 |
| Accessibility first (AP-XF-10) | WCAG 2.1 AA applied from the mockups onward; nothing conveyed by colour alone; keyboard operable | NFR-04, D-59 |

### 4.3 Well-architected compliance

| Quality | Design response | Ref |
| --- | --- | --- |
| Resiliency (AP-WA-01) | The AMS → SMS hand-overs are written in the same transaction as the business change (outbox) and retried until delivered; salary generation is repeatable without duplicates; the nightly reconciliation repairs anything missed; timeout, retry and circuit-breaker defaults in §8.5 | INT-01, INT-02, JOB-CMN-01, R-01, R-03, D-16 |
| Availability (AP-WA-02) | 99 % in Production during business hours; two instances of every stateless tier; daily backup with RPO 24 h and RTO 8 h; single site for the POC – per-tier detail in §6.4 | NFR-02, D-59, D-109 |
| Decentralized (AP-WA-03) | Each module owns its data and its service; no shared database; modules interact only through APIs and events; the gateway and identity provider are shared platform components with no business logic | D-10, C-02, D-18 |
| Independent & autonomous (AP-WA-04) | Separate builds, path-filtered pipelines and independent deployment per service; contracts-only sharing. Exception: module screens are built into the shell for the POC, so a UI change redeploys the shell (ADR-001) | D-18, D-23, NFR-08 |
| Auto provisioning (AP-WA-05) | Environments and deployments created from code and pipelines; the provisioning approach for the on-premises platform is settled in §7 and §15 (open item OI-P01-02) | D-11, D-109 |
| Scalability (AP-WA-06) | Stateless services scale out per service on the container platform; sized for 100 employees, scale out per module to 10×, load-tested to 2× | NFR-07, D-59 |
| Security (AP-WA-07) | Identity provider, token validation at gateway and service, role and data-scope checks, private back-end network zones, encryption in transit, secrets outside code; detail in §9 and §16 | NFR-03, NFR-SUP-01 to 03 |
| Continuous delivery (AP-WA-08) | One pipeline per service with quality gates; promotion Dev → QA → Prod | D-11, D-18; §15 |
| Failure isolation (AP-WA-09) | One module being down does not stop the others: each dashboard card loads on its own; AMS approval does not wait for SMS (asynchronous hand-over); database per service | NFR-02, FR-CMN-008, INT-01 |
| Observability (AP-WA-10) | Central activity log with flow reference, audit log, metrics, health checks and alerts; detail in §10 | NFR-09, D-101 |

### 4.4 Patterns applied

Pattern selection follows from the approved decisions; Part01a records applicability and realization for each id.

| Category | Patterns applied (Part01a ids) | Where |
| --- | --- | --- |
| Microservice design patterns | Decompose by business capability (AP-MS-01); Database per service (AP-MS-03); API gateway (AP-MS-05); Saga – choreography for AMS → SMS (AP-MS-08); Transactional outbox (AP-MS-10); Domain events (AP-MS-12); API composition for the dashboard and approvals inbox (AP-MS-15); Idempotent consumer (AP-MS-16); Externalized configuration (AP-MS-18); Health check API (AP-MS-19); Log aggregation (AP-MS-20); Audit logging (AP-MS-23); Access token (AP-MS-25); Service instance per container (AP-MS-28); API versioning (AP-MS-33) | §5.3, §6, §8, §9, §10; INT-01 to INT-10, FR-CMN-008, BR-CMN-19, NFR-09 |
| Cloud design patterns | Choreography (AP-CP-07); Federated identity (AP-CP-17); Gateway offloading and routing (AP-CP-20, AP-CP-21); Health endpoint monitoring (AP-CP-23); Idempotent consumer (AP-CP-24); Publisher-subscriber (AP-CP-31); Retry (AP-CP-35); Scheduler agent supervisor for the nightly reconciliation (AP-CP-37); Static content hosting for the frontend (AP-CP-41); Circuit breaker (AP-CP-08) and rate limiting (AP-CP-34) – settings in §8.5 and §9.8 | §6, §8, §9; JOB-CMN-01 |
| Enterprise integration patterns | Messaging (AP-EIP-04) and Remote procedure invocation (AP-EIP-03) as the two integration styles; Event message (AP-EIP-17); Guaranteed delivery (AP-EIP-11); Dead letter channel (AP-EIP-10); Correlation identifier (AP-EIP-20) for the flow reference; Message broker (AP-EIP-37); Transactional client (AP-EIP-48); Event-driven consumer (AP-EIP-50); Durable subscriber (AP-EIP-54); Idempotent receiver (AP-EIP-55) | §8; INT-01, INT-02, FR-ADM-113 |

## 5. Functional architecture

To be drafted (review 2: §5–§8).

## 6. System architecture

To be drafted (review 2: §5–§8).

## 7. Deployment architecture

To be drafted (review 2: §5–§8).

## 8. Integration architecture

To be drafted (review 2: §5–§8).

## 9. Authentication & authorization

To be drafted (review 3: §9–§10).

## 10. Unified & centralized logging and observability

To be drafted (review 3: §9–§10).

## 11. Technology stack

To be drafted (review 4: §11–§15).

## 12. Data architecture (summary)

To be drafted (review 4: §11–§15).

## 13. Data migration strategy

To be drafted (review 4: §11–§15).

## 14. Performance test strategy and plan

To be drafted (review 4: §11–§15).

## 15. Environment strategy

To be drafted (review 4: §11–§15).

## 16. Security & NFR

To be drafted (review 5: §16–§20).

## 17. Volumetrics

To be drafted (review 5: §16–§20).

## 18. Architecture decisions

To be drafted (review 5: §16–§20).

## 19. Risks and technical debt

To be drafted (review 5: §16–§20).

## 20. Appendix

### 20.1 Open items

| Id | Open item | Owner | Due |
| --- | --- | --- | --- |
| OI-P01-01 | Part01a assessment: counts per group in §4.1 and confirmation of the catalogue ids in §4.2 to §4.4 | Enterprise Architect | Part01a |
| OI-P01-02 | Provisioning approach (infrastructure and environments as code) for the on-premises platform | Enterprise Architect, IT operations | Part01 §7 and §15 |
