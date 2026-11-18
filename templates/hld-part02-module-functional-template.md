# <Project> – HLD Part02-M<n>: <Module name> (<MOD>) Functional Design

Document ID: <PRJ>-HLD-Part02-M<n>-<MOD>-Functional-v<x.y>
Module: <Module name> (<MOD>)
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

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

## 2. Introduction: Function design

This document describes the high-level solution approach for each system function of the [<Module name>] module: APIs, database, orchestration and scenarios. Architecture-wide decisions (stack, resilience defaults, logging, security) are in Part01; cross-module flows and common design conventions (API, events, errors) are in the Part02 anchor. Neither is repeated here.

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | <PRJ>-BRD (anchor), <PRJ>-BRD-M<n>-<MOD>, <PRJ>-BRD-M<n>-SUP | v<x> |
| 2 | UX Journey Index and UX Summaries | v<x> |
| 3 | Decision log / ADRs | D-01 to D-<nn> |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-Architecture-and-Design | Overall architecture and design |
| 2 | <PRJ>-HLD-Part01a-Principles-Patterns-Decisions | Principles and patterns catalogue; ADR register |
| 3 | <PRJ>-HLD-Part02-Functional (anchor) | Module index, cross-module flows, common design conventions, roll-up inventories |
| 4 | <PRJ>-HLD-Part02-M<n>-<MOD>-Functional | Solution approach of the other functional modules |
| 5 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Solution approach for supporting modules |
| 6 | <PRJ>-HLD-Part03-Datamodel (anchor) and <PRJ>-HLD-Part03-M<n>-<MOD>-Datamodel | Data model |
| 7 | API / event contracts (`contracts/`) | OpenAPI and event schemas |

## 3. Module: <Module name>

### 3.1 Preread

#### 3.1.1 Overview

<What the module does, who uses it, what it owns (data, APIs, events), what it depends on.>

#### 3.1.2 Module process flow

<Diagram: the module's main business flow with its system functions (by id), decision points and handovers to other modules / jobs. Flows that span several modules are designed once in the Part02 anchor §5 and only referenced here.>

#### 3.1.3 High-level ER diagram

<Module ER diagram; full definition in <PRJ>-HLD-Part03-M<n>-<MOD>-Datamodel.>

#### 3.1.4 Status lifecycle

Business statuses and transitions are defined in the module BRD (<PRJ>-BRD-M<n>-<MOD>) §6.<n>. This section records only the technical handling: where status is stored, how transitions are enforced, events emitted per transition.

| Transition | Enforced in | Event emitted | Audit / activity entry |
| --- | --- | --- | --- |

#### 3.1.5 System function index

| Function id | System function | Type (screen / API / backend job) | UX screen | Delivery phase | Design status |
| --- | --- | --- | --- | --- | --- |
| <MOD>0010 | | Screen | SCR-<MOD>-01 | POC | Draft |

### 3.2 <Module name> system functions

Repeat 3.2.n for every function in the index.

#### 3.2.1 <MOD>0010 – <Function name> (Module: <MOD>, <Design status>)

> Guidance
> - Design status: Draft / In review / Approved / Deferred.
> - Keep the design technology-neutral (no framework-specific terms such as Spring annotations) so it holds across replatforming (Java → Node.js / Python FastAPI).
> - Do not restate what lives elsewhere: business rules and validations reference BRD ids; screen behaviour already in the UX summary is referenced, not copied.

##### 3.2.1.1 Purpose, trigger and conditions

<One or two sentences: what the function lets the user / system do.>

| Item | Detail |
| --- | --- |
| Delivery phase | POC / Phase 2 |
| Trigger | <user action / event / schedule> |
| Pre-conditions | <state that must hold before the function runs> |
| Post-conditions | <resulting state, statuses, events emitted> |

##### 3.2.1.2 Actor & data scope

Per role × screen access matrix (module BRD §4.2):

| Role | Access (Read / Read-write / Approve / None) | Data scope (row-level) |
| --- | --- | --- |
| Employee | | Own records only |
| Manager | | Own + direct reportees |
| Admin | | All |

##### 3.2.1.3 Requirement traceability

| Source | References |
| --- | --- |
| BRD functional requirements | FR-<MOD>-… |
| BRD business / validation rules | BR-…, VR-… |
| BRD NFRs | NFR-… |
| UX | UJ-…, SCR-… |
| Decisions | D-…, ADR-… |
| Related functions – depends on | <MOD>00nn … |
| Related functions – used by | <MOD>00nn … |

##### 3.2.1.4 Navigation & prototype reference

**Navigation:** <Menu > Screen > Tab>

**Prototype:** `docs/01-ux/mockups/<file>.html` · UX summary `docs/01-ux/ux-summary/<file>.md`

##### 3.2.1.5 Solution approach

###### 3.2.1.5.1 Design description

The [<Function name>] function lets users work with the following sections / activities:

1. <Section / activity>
2. <Section / activity>

**<Section / activity name>**

1. <What the section shows or captures.>
2. Data is fetched / saved via API: [API-<MOD>-nn : <METHOD> /<ctx>/<resource> (Purpose : …)]
3. DB entity: [<ENTITY>]
4. <Rules applied (BR / VR ids), query vs edit mode, defaults.>

###### 3.2.1.5.2 Design notes

1. <Design choices, options considered and why, ids / sequences, caching, pagination, concurrency.>

###### 3.2.1.5.3 Sequence & orchestration

<Sequence diagram (e.g. Mermaid) for the main flow; alt / opt blocks for alternative and error paths. Participants: User, Frontend, Gateway, <Service>, other services, Broker, DB.>

Cross-service and asynchronous steps only (omit for a single-service synchronous function):

| Step | Type (sync call / event / job / workflow) | Producer → consumer | Event / API | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- |

###### 3.2.1.5.4 Frontend

Only what is not already in the UX summary:

1. <Components, state handling, API call mapping, client-side validation, empty / loading / error / read-only states, accessibility notes.>

###### 3.2.1.5.5 Backend

| API id | API name | Method & endpoint | Purpose | Request (key fields) | Response (key fields) | Roles |
| --- | --- | --- | --- | --- | --- | --- |
| API-<MOD>-01 | | | | | | |

<Server-side validation, transaction boundary, idempotency, events published, jobs.>

###### 3.2.1.5.6 Database

| Entity | Operation (C / R / U / soft-D) | Purpose in this function |
| --- | --- | --- |

###### 3.2.1.5.7 Validation & error handling

| Rule ref (BRD VR / BR) | Layer (UI / API / DB) | Error code | HTTP status | Message |
| --- | --- | --- | --- | --- |

###### 3.2.1.5.8 Security & data privacy

| Item | Detail |
| --- | --- |
| Authorization check per API | API-<MOD>-nn: role + data-scope rule |
| Sensitive fields | <e.g. salary, bank account, PAN> |
| Masking (UI / API response) | |
| Encryption (in transit / at rest / field-level) | |
| Logging rule | <never log / mask in logs> |

###### 3.2.1.5.9 Notifications, audit & activity log

| Trigger | Notification (NOT id) | Activity log entry | Audit fields captured |
| --- | --- | --- | --- |

###### 3.2.1.5.10 Scenarios

Business and technical scenarios the design must satisfy; basis for test cases.

| Scenario id | Scenario | Type (positive / negative / edge / concurrency / failure) | Requirement ref | Pre-condition | Expected result | Test level (unit / API / E2E) |
| --- | --- | --- | --- | --- | --- | --- |

##### 3.2.1.6 Notes, issues & assumptions

1. Note / Issue / Assumption / Q: <text>

## 4. NFR summary & inventories

### 4.1 NFR summary

NFR detail is kept out of each function's design description; functions reference an NFR id, and the authoritative value lives here.

| Seq | NFR id | Category | Requirement | Design approach | Applicable function(s) |
| --- | --- | --- | --- | --- | --- |

### 4.2 API inventory

Roll-up of the per-function API tables (§3.2.n.5.5); the API id is the key.

| API id | API name | Purpose | Method & endpoint | Request (key fields) | Roles | Idempotent | Function |
| --- | --- | --- | --- | --- | --- | --- |

Resilience defaults (timeouts, retries, circuit breaker, idempotency): Part01 §8.5.

### 4.3 Event inventory

| Seq | Event | Producer | Consumer(s) | Queue / topic | Key payload fields | Function |
| --- | --- | --- | --- | --- | --- | --- |

### 4.4 Scheduled job inventory

| Seq | Job | Schedule | Purpose | Function |
| --- | --- | --- | --- | --- |

### 4.5 Error code catalogue

| Error code | HTTP status | Meaning | Message |
| --- | --- | --- | --- |

## 5. Appendix

### 5.1 Future scope (not designed in this phase)

| Area | Requirement ref | Note |
| --- | --- | --- |

### 5.2 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
