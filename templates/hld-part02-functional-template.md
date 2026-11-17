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

This document describes the high-level solution approach for each system function of the [<Module name>] module: APIs, database, orchestration and scenarios. Architecture-wide decisions (stack, resilience defaults, logging, security) are in Part01 and are not repeated here.

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | <PRJ>-BRD | v<x> |
| 2 | UX Journey Index and UX Summaries | v<x> |
| 3 | Decision log / ADRs | D-01 to D-<nn> |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-AnD | Overall architecture and design |
| 2 | <PRJ>-HLD-Part01a-Principles-Patterns | Principles and patterns catalogue |
| 3 | <PRJ>-HLD-Part01b-AnA | Authentication & authorization |
| 4 | <PRJ>-HLD-Part02-M<n>-<MOD>-Functional | Solution approach per functional module (one per module) |
| 5 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Solution approach for supporting modules |
| 6 | <PRJ>-HLD-Part03-Datamodel | Data model |
| 7 | API / event contracts (`contracts/`) | OpenAPI and event schemas |

## 3. Module: <Module name>

### 3.1 Preread

#### 3.1.1 Overview

<What the module does, who uses it, what it owns (data, APIs, events), what it depends on.>

#### 3.1.2 Module process flow

<Diagram: the module's main business flow with its system functions (by id), decision points and handovers to other modules / jobs.>

#### 3.1.3 High-level ER diagram

<Module slice of the ER diagram; full definition in Part03 §<x>.>

#### 3.1.4 Status lifecycle

Business statuses and transitions are defined in BRD §6.<n>. This section records only the technical handling: where status is stored, how transitions are enforced, events emitted per transition.

| Transition | Enforced in | Event emitted | Audit / activity entry |
| --- | --- | --- | --- |

#### 3.1.5 System function index

| Function id | System function | Type (screen / API / backend job) | UX screen | Delivery phase | Design status |
| --- | --- | --- | --- | --- | --- |
| <MOD>0010 | | Screen | SCR-<MOD>-01 | POC | Draft |

### 3.2 <Module name> system functions

Repeat 3.2.n for every function in the index.

#### 3.2.1 <MOD>0010 – <Function name> (Module: <MOD>, <Design status>)

##### 3.2.1.1 Purpose

<One or two sentences: what the function lets the user / system do.>

Delivery phase: <POC / Phase 2>

##### 3.2.1.2 Requirement traceability

| Source | References |
| --- | --- |
| BRD functional requirements | FR-<MOD>-… |
| BRD business / validation rules | BR-…, VR-… |
| BRD NFRs | NFR-… |
| UX | UJ-…, SCR-… |
| Decisions | D-…, ADR-… |

##### 3.2.1.3 Navigation & prototype reference

**Navigation:** <Menu > Screen > Tab>

**Prototype:** `docs/01-ux/mockups/<file>.html` · UX summary `docs/01-ux/ux-summary/<file>.md`

##### 3.2.1.4 Solution approach

###### 3.2.1.4.1 Design description

The [<Function name>] function lets users work with the following sections / activities:

1. <Section / activity>
2. <Section / activity>

**<Section / activity name>**

1. <What the section shows or captures.>
2. Data is fetched / saved via API: [API : <METHOD> /<ctx>/<resource> (Purpose : …)]
3. DB entity: [<ENTITY>]
4. <Rules applied (BR / VR ids), query vs edit mode, defaults.>

###### 3.2.1.4.2 Design notes

1. <Design choices, options considered and why, ids / sequences, caching, concurrency.>

###### 3.2.1.4.3 Actor

Per role × screen access matrix (BRD §4.3):

| Role | Access |
| --- | --- |
| <Role> | Read / Read-write / Approve |

###### 3.2.1.4.4 Sequence flow

<Sequence diagram (e.g. Mermaid) for the main flow; alt / opt blocks for alternative and error paths. Participants: User, Frontend, Gateway, <Service>, other services, Broker, DB.>

###### 3.2.1.4.5 Orchestration & events

| Step | Type (sync call / event / job / workflow) | Producer → consumer | Event / API | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- |

###### 3.2.1.4.6 Frontend

1. <Layout, components, states (empty / loading / error / read-only), client-side validation, navigation.>

###### 3.2.1.4.7 Backend

| # | API name | Method & endpoint | Purpose | Request (key fields) | Response (key fields) | Roles |
| --- | --- | --- | --- | --- | --- | --- |

<Server-side validation, authorization checks, transaction boundary, idempotency, events published, jobs.>

###### 3.2.1.4.8 Database

| Entity | Operation (C / R / U / soft-D) | Purpose in this function |
| --- | --- | --- |

###### 3.2.1.4.9 Validation & error handling

| Rule id | Check | Layer (UI / API / DB) | Error code | HTTP status | Message |
| --- | --- | --- | --- | --- | --- |

###### 3.2.1.4.10 Notifications, audit & activity log

| Trigger | Notification (NOT id) | Activity log entry | Audit fields captured |
| --- | --- | --- | --- |

###### 3.2.1.4.11 Scenarios

Business and technical scenarios the design must satisfy; basis for test cases.

| Scenario id | Scenario | Type (positive / negative / edge / concurrency / failure) | Pre-condition | Expected result |
| --- | --- | --- | --- | --- |

##### 3.2.1.5 Notes, issues & assumptions

1. Note / Issue / Assumption / Q: <text>

## 4. NFR summary & inventories

### 4.1 NFR summary

NFR detail is kept out of each function's design description; functions reference an NFR id, and the authoritative value lives here.

| Seq | NFR id | Category | Requirement | Design approach | Applicable function(s) |
| --- | --- | --- | --- | --- | --- |

### 4.2 API inventory

| Seq | API name | Purpose | Method & endpoint | Request (key fields) | Roles | Idempotent | Function |
| --- | --- | --- | --- | --- | --- | --- | --- |

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
