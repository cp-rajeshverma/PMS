# <Project> – HLD Part02: Functional Design (Anchor)

Document ID: <PRJ>-HLD-Part02-Functional-v<x.y>
Scope: functional design anchor – module index, cross-module flows, common design conventions and roll-up inventories; per-function designs are in the module documents
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - This anchor holds what spans modules. Per-function designs live only in <PRJ>-HLD-Part02-M<n>-<MOD>-Functional (one per functional module) and <PRJ>-HLD-Part02-M<n>-SUP-Functional; the anchor never repeats them.
> - Inventories in §7 are roll-ups of the module documents, keyed by id, with a link to the owning function.
> - Keep the design technology-neutral so it holds across replatforming.
> - Every diagram keeps a text-version table beneath it.

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | Design based on BRD v<x> |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Business analyst | | | |
| Dev lead | | | |

## 2. Introduction

This document is the anchor of the [<Project>] functional design: it indexes the module design documents, designs the flows that cross modules, and sets the design conventions every module follows.

### 2.1 Reference documents

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-BRD (anchor), <PRJ>-BRD-M<n>-<MOD>, <PRJ>-BRD-M<n>-SUP | Requirements |
| 2 | UX Journey Index and UX Summaries | Experience design |
| 3 | <PRJ>-HLD-Part01-Architecture-and-Design | Overall architecture and design |
| 4 | <PRJ>-HLD-Part01a-Principles-Patterns-Decisions | Principles and patterns catalogue; ADR register |
| 5 | <PRJ>-HLD-Part03-Datamodel (anchor) | Data model |
| 6 | API / event contracts (`contracts/`) | OpenAPI and event schemas |

### 2.2 Module design documents

| Module | Document | Owning service | Version | Status |
| --- | --- | --- | --- | --- |
| <MOD1> | <PRJ>-HLD-Part02-M1-<MOD1>-Functional | | | |
| SUP | <PRJ>-HLD-Part02-M<n>-SUP-Functional | | | |

## 3. Functional landscape

### 3.1 Module overview

| Module | Purpose | Primary users (roles) | Key entities owned | Depends on (modules) | Used by (modules) |
| --- | --- | --- | --- | --- | --- |

### 3.2 Module dependency map

<Diagram: modules and the direction of their dependencies (sync API / event / job).>

| From module | To module | Dependency (API / event / job) | Purpose | Flow (§5) |
| --- | --- | --- | --- | --- |

## 4. System function index (all modules)

| Function id | System function | Module | Type (screen / API / backend job / configuration) | UX screen | Delivery phase | Design status | Document section |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 5. Cross-module flows

One subsection per business flow that spans two or more modules.

### 5.1 XF-01 – <Flow name>

| Item | Detail |
| --- | --- |
| Business purpose | |
| Trigger | <user action / event / schedule> |
| Modules involved | |
| Requirement refs | BRD FR / BR, UJ |
| Pre-conditions / post-conditions | |

<Sequence diagram across modules (participants: user, frontends, gateway, services, broker, jobs).>

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |

**Failure handling & compensation:** <what happens when a step fails; retries, compensating actions, manual intervention>

**Reconciliation:** <job / report that detects and repairs drift between modules>

## 6. Common design conventions

### 6.1 API conventions

| Topic | Convention |
| --- | --- |
| Base path and versioning | <e.g. /api/v1/<module>/...> |
| Resource naming | <plural nouns, kebab-case, no verbs except actions> |
| Methods and status codes | |
| Request / response envelope | |
| Error format | <e.g. RFC 9457 problem details: type, title, status, detail, code, traceId> |
| Pagination, sorting, filtering | |
| Idempotency | <Idempotency-Key header for unsafe retries> |
| Concurrency | <ETag / row_version, 409 on conflict> |
| Date, time, money, enum formats | |
| Correlation and tracing headers | |

### 6.2 Event conventions

| Topic | Convention |
| --- | --- |
| Naming | <e.g. <module>.<entity>.<past-tense-verb>> |
| Envelope (id, type, source, time, correlation id, version, payload) | |
| Versioning and compatibility | |
| Delivery and ordering guarantees | |
| Idempotent consumers | |
| Dead-letter and replay | |

### 6.3 Error code scheme

| Module | Error code range / prefix | Owner |
| --- | --- | --- |

### 6.4 Audit, activity log and notification conventions

<Which actions write an activity entry or audit record, the standard message format, and how notification triggers are raised (event → notification service). Detail in Part02-SUP.>

### 6.5 Frontend conventions

<Shared shell, navigation, common components, state handling, error and empty states; reference UX artifacts and the frontend composition ADR.>

## 7. Roll-up inventories

### 7.1 API inventory

| API id | API name | Module | Method & endpoint | Roles | Idempotent | Function |
| --- | --- | --- | --- | --- | --- | --- |

### 7.2 Event inventory

| Event | Producer module | Consumer module(s) | Queue / topic | Flow (§5) | Function |
| --- | --- | --- | --- | --- | --- |

### 7.3 Scheduled job inventory

| Job | Module | Schedule | Purpose | Function |
| --- | --- | --- | --- | --- |

### 7.4 Notification inventory

| NOT id | Notification | Triggering module / function | Recipients | Channel |
| --- | --- | --- | --- | --- |

## 8. NFR summary (cross-module)

| NFR id | Category | Requirement | Design approach | Applies to (modules / flows) |
| --- | --- | --- | --- | --- |

## 9. Requirement coverage

| BRD requirement | Function id(s) / flow | Module document section | Status |
| --- | --- | --- | --- |

## 10. Appendix

### 10.1 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
