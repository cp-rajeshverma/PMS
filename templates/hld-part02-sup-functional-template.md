# <Project> – HLD Part02-M<n>: Supporting Modules (SUP) Functional Design

Document ID: <PRJ>-HLD-Part02-M<n>-SUP-Functional-v<x.y>
Module: Supporting modules (Admin & master data, User & access, Authentication & authorization, Notification, Document)
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - This document covers capabilities that are shared across the functional modules (Part02-M1..M<n>) and are not owned by any single business domain.
> - Every system function uses the per-function structure of the Part02 module functional template §3.2.1 (D-38).
> - Design status values: Draft / In review / Approved / Deferred / Moved (to another Part02 document; keep a one-line stub with the new location).
> - Keep the design technology-neutral so it holds across replatforming; product-specific configuration (e.g. identity provider realm settings) goes in Design notes.
> - A sub-module that does not apply to the project keeps its heading with "Not applicable – <reason>".

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
| Security lead | | | |
| Dev lead | | | |

## 2. Introduction: Function design

This document describes the high-level solution approach for the supporting system functions common to all functional modules ([<MOD1>, <MOD2>, …]): APIs, database, orchestration and scenarios. Architecture-wide decisions, including the authentication and authorization architecture (Part01 §9), are in Part01.

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
| 1 | <PRJ>-HLD-Part01-Architecture-and-Design | Overall architecture and design |
| 2 | <PRJ>-HLD-Part01a-Principles-Patterns-Decisions | Principles and patterns catalogue; ADR register |
| 3 | <PRJ>-HLD-Part02-Functional (anchor) | Module index, cross-module flows, common design conventions, roll-up inventories |
| 4 | <PRJ>-HLD-Part02-M1..M<n>-<MOD>-Functional | Functional modules (consumers of this document) |
| 5 | <PRJ>-HLD-Part03-Datamodel | Data model |
| 6 | API / event contracts (`contracts/`) | OpenAPI and event schemas |

### 2.2 Supporting module overview

| Sub-module | Prefix | Owning component (service / platform product) | Realization (custom build / platform configuration / product feature) | Consumer modules |
| --- | --- | --- | --- | --- |
| Admin functions & master data | ADM | | | |
| User & access management | UM | | | |
| Authentication & authorization | AUTH | | | |
| Notification management | NM | | | |
| Document management | DM | | | |

### 2.3 System function index

| Function id | System function | Sub-module | Type (screen / API / backend job / configuration) | UX screen | Delivery phase | Design status |
| --- | --- | --- | --- | --- | --- | --- |
| ADM0010 | | ADM | | | POC | Draft |

## 3. Admin functions & master data

### 3.1 Admin functions

#### 3.1.1 ADM0010 – Activity log & audit log (Module: ADM, <Design status>)

<Per-function structure (Part02 module functional template §3.2.1). Guidance:>

- **Activity log**: chronological, human-readable history of a business entity; format `<activity> – <description> – <performed by> – <performed at>`; activities configured in an activity rule table.
- **Audit log**: field-level change tracking for audited attributes (old value, new value, by, when, reason); append-only, no update / delete API.
- List the business entities covered (one row per entity of M1..M<n>) and how each module captures entries (synchronous API / event / outbox).

#### 3.1.2 ADM00nn – <Other admin function> (Module: ADM, <Design status>)

### 3.2 Master data

Typical functions (keep those the BRD requires; mark others Not applicable):

| Function | Purpose |
| --- | --- |
| Manage valid values (lookup / code tables) | Dropdown and status values: id_type, code, description, display sequence, status |
| Manage configuration parameters | Business thresholds and system parameters changeable without deployment |
| Manage business calendar / holidays | Non-working days for business-day calculations (SLA, due dates, payroll period) |
| Master data loader | File / integration based bulk load (file → stage → main), with file log and error file |
| <Domain master> | <e.g. department, designation, pay component> |

#### 3.2.1 ADM0100 – <Master data function> (Module: ADM, <Design status>)

<Per-function structure (Part02 module functional template §3.2.1). Standard CRUD guidance: create, search & list (paginated), view, edit, activate / deactivate, soft delete; uniqueness; no hard delete of values referenced by transactions; changes audit-logged; changes apply prospectively; cache invalidation.>

## 4. Supporting non-functional modules

### 4.1 User & access management

#### 4.1.0 Overview & requirement map

<What the sub-module owns (users, roles, features, role × feature permissions, hierarchy, delegation, access log) and where each is mastered (application DB vs identity provider).>

| Requirement id | Requirement | Priority | System function | Actor |
| --- | --- | --- | --- | --- |

**Role catalogue**

| Seq | Role id | Role name | Role type (business / system / external) | Description |
| --- | --- | --- | --- | --- |

**Role × feature matrix** (or reference BRD §4.3)

| Feature / screen | <Role 1> | <Role 2> | <Role 3> |
| --- | --- | --- | --- |

Legend: R = Read · R/W = Read + write · A = Approve · — = No access

Typical functions: UM0010 Manage user · UM0020 Add / remove user role (incl. bulk) · UM0030 Manage role · UM0040 Role expiry job · UM0050 Access log · UM0060 Manage feature · UM0070 Manage feature element · UM0080 Role-level feature / element permission · UM0090 Manage user group · UM0100 Manage user hierarchy (manager – reportee) · UM0110 Manage delegation.

#### 4.1.1 UM0010 – <Function name> (Module: UM, <Design status>)

<Per-function structure (Part02 module functional template §3.2.1).>

### 4.2 Authentication & authorization

Architecture, token design, OAuth / OIDC flows, MFA approach and API-level security are defined in Part01 §9; this section covers only the user-facing and job functions.

#### 4.2.1 Responsibility matrix

| Function | Owner (identity provider / application / gateway) |
| --- | --- |
| User authentication (credentials, SSO, MFA) | |
| Token issue, refresh and revocation | |
| Token validation at the edge | |
| Application authorization (role / permission / data scope) | |
| Role & permission management | |
| Session management | |

#### 4.2.2 User categories

| User category | Description | Authentication path | MFA |
| --- | --- | --- | --- |

#### 4.2.3 Identity provider integration parameters

| Item | Value (per environment) |
| --- | --- |
| Protocol / flow | <e.g. OIDC Authorization Code + PKCE> |
| Issuer / realm | |
| Client(s) | |
| Redirect / logout URLs | |
| Token lifetimes (access / refresh / idle session) | |
| Claims consumed | |
| Secrets location | <secret store; never in code> |

#### 4.2.4 AUTH0010 – Sign-in (Module: AUTH, <Design status>)

#### 4.2.5 AUTH0020 – Sign-out & session expiry (Module: AUTH, <Design status>)

#### 4.2.6 AUTH0030 – User onboarding / first login (Module: AUTH, <Design status>)

#### 4.2.7 AUTH0040 – Password & MFA management (Module: AUTH, <Design status>)

<Per-function structure (Part02 module functional template §3.2.1), or a pointer stub when owned entirely by the identity provider.>

### 4.3 Notification management

#### 4.3.0 Overview

<Channels (in-app, email, SMS – in / out of scope), modes (real-time / batch), deep links, template and placeholder approach, delivery architecture (event → notification service → channel), retry and dead-letter handling.>

**Notification catalogue** (BRD §10 NOT ids)

| NOT id | Notification type | Trigger (event / schedule) | Mode (real-time / batch) | Recipients | In-app | Email | Template id |
| --- | --- | --- | --- | --- | --- | --- | --- |

#### 4.3.1 NM0010 – Notification engine (Module: NM, <Design status>)

<Include the notification request / response contract (fields, type, mandatory, description) and the event subscription list.>

#### 4.3.2 NM0020 – Notification bell & history (Module: NM, <Design status>)

#### 4.3.3 NM0030 – Manage notification rules & templates (Module: NM, <Design status>)

<Per-function structure (Part02 module functional template §3.2.1).>

### 4.4 Document management

#### 4.4.1 DM0010 – Manage document (Module: DM, <Design status>)

<Per-function structure (Part02 module functional template §3.2.1). Guidance: upload / list / download / remove (soft) / metadata; allowed file types, max size and count as configuration; malware scan; storage location; access follows the owning business record.>

## 5. NFR summary & inventories

### 5.1 NFR summary

| Seq | NFR id | Category | Requirement | Design approach | Applicable function(s) |
| --- | --- | --- | --- | --- | --- |

### 5.2 API inventory

Roll-up of the per-function API tables; the API id is the key.

| API id | API name | Purpose | Method & endpoint | Request (key fields) | Roles | Idempotent | Function |
| --- | --- | --- | --- | --- | --- | --- | --- |

Resilience defaults (timeouts, retries, circuit breaker, idempotency): Part01 §8.5.

### 5.3 Event inventory

| Seq | Event | Producer | Consumer(s) | Queue / topic | Key payload fields | Function |
| --- | --- | --- | --- | --- | --- | --- |

### 5.4 Scheduled job inventory

| Seq | Job | Schedule | Purpose | Function |
| --- | --- | --- | --- | --- |

### 5.5 Configuration parameter inventory

| Parameter | Default | Unit | Changeable by | Used by function(s) |
| --- | --- | --- | --- | --- |

### 5.6 Error code catalogue

| Error code | HTTP status | Meaning | Message |
| --- | --- | --- | --- |

## 6. Appendix

### 6.1 Future scope (not designed in this phase)

| Area | Requirement ref | Note |
| --- | --- | --- |

### 6.2 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
