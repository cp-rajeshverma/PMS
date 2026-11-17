# <Project> – HLD Part03: Data Model

Document ID: <PRJ>-HLD-Part03-Datamodel-v<x.y>
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - One section per owning service / module (database-per-service); supporting-module entities follow the functional modules.
> - Entity status values: Draft / In review / Approved / Removed / Moved (keep a one-line stub with the reason or new location).
> - Business statuses and their transitions come from BRD §6; this document defines only how they are stored.
> - Keep the model technology-neutral where possible; engine-specific types (e.g. `jsonb`, `uuid`) are allowed only for the chosen database (Part01 §11).
> - Every diagram keeps a text-version table beneath it.

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | Data model based on BRD v<x> and Part02 v<x> |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Data / DB lead | | | |
| Dev lead | | | |
| Security lead | | | |

## 2. Introduction: Data model

This document describes the logical and high-level physical data model of [<Project>]: entities, columns, keys, relationships, data ownership per service, classification, volumetrics and retention.

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | <PRJ>-BRD (§6 status lifecycles, §9 data requirements, §13 volumetrics) | v<x> |
| 2 | Decision log / ADRs | D-01 to D-<nn> |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-AnD (§12 data architecture, §13 data migration) | Overall architecture and design |
| 2 | <PRJ>-HLD-Part01a-Principles-Patterns | Principles and patterns catalogue |
| 3 | <PRJ>-HLD-Part02-M1..M<n>-<MOD>-Functional | Functional modules (entity usage per function) |
| 4 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Supporting modules |
| 5 | Contracts (`contracts/`) | API and event schemas |

### 2.2 Data ownership (database per service)

| Service / module | Database / schema | Entities owned | Entities read from other services (how: API / event-replicated copy) |
| --- | --- | --- | --- |

Rules: no foreign keys or joins across service databases; a reference to another service's entity is held as its business key and resolved through that service's API or a replicated read copy (§5).

### 2.3 Modelling conventions

| Topic | Convention |
| --- | --- |
| Entity and column naming | <e.g. UPPER_SNAKE entity names in this document, snake_case columns, singular nouns> |
| Primary key | <e.g. surrogate `id` (uuid); business key held separately with a unique constraint> |
| Business identifiers | <format and generator, e.g. `EMP-YYYY-NNNN` via a sequence table> |
| User references | <type and length used for every *_user_id / *_by column> |
| Date / time | <timestamp with time zone, stored in UTC; display time zone> |
| Money | <numeric(precision, scale); currency handling> |
| Enumerations / statuses | <lookup table or check constraint; values from BRD §6> |
| Soft delete | <is_deleted / status = Inactive; no hard delete of referenced rows> |
| Optimistic locking | <row_version column on entities edited concurrently> |
| Semi-structured data | <when JSON columns are allowed> |
| Audit columns | §2.4 |

### 2.4 Common columns (apply to every entity unless stated)

| Column | Type | Null | Notes |
| --- | --- | --- | --- |
| created_by | | N | reference to user |
| created_at | | N | default current timestamp |
| updated_by | | Y | reference to user |
| updated_at | | Y | |
| row_version | | N | optimistic lock (where applicable) |

## 3. Database design

### 3.0 Entity index

| # | Entity | Service / module | Type (master / transaction / history / config / log / reference) | Section | Status |
| --- | --- | --- | --- | --- | --- |

### 3.1 <Module 1> (<MOD>) – service `<service-name>`, database `<db-name>`

#### 3.1.1 <ENTITY_NAME> (<Status>)

**Purpose:** <one sentence; functions that create / read / update it (Part02 function ids)>

| Column | Type | Null | Key (PK / UK / FK / IDX) | Default | Notes (allowed values, rule ref BR/VR, source) |
| --- | --- | --- | --- | --- | --- |
| id | | N | PK | | surrogate key |
| <business_key> | | N | UK | | e.g. EMP-2026-0001 |
| status | | N | IDX | | values per BRD §6.<n> |
| audit columns | | | | | §2.4 |

**Constraints & indexes**

| Name | Type (UK / CHECK / FK / IDX) | Columns | Purpose |
| --- | --- | --- | --- |

**Relationships**

| Related entity | Cardinality | Via column | Same service / cross-service (resolved by API / event) |
| --- | --- | --- | --- |

**Data classification**

| Column(s) | Classification (Public / Internal / Confidential / PII / Sensitive-financial) | Protection (masking / encryption / access rule) |
| --- | --- | --- |

**Volumetrics & retention:** <initial rows, growth per month / year, retention period, archival / purge rule>

**Notes:** <history handling, reopen / versioning, concurrency, decisions (D-…)>

#### 3.1.2 <ENTITY_NAME>_HISTORY / _STATUS_LIFECYCLE (<Status>)

<History and status-transition entities follow the same structure; state whether append-only.>

### 3.2 <Module 2> (<MOD>) – service `<service-name>`, database `<db-name>`

### 3.<n> Supporting modules

Model supporting-module entities on a need basis only. Where a capability is provided by an existing platform or product (e.g. identity provider for users / roles / sessions, an enterprise notification or document service), do not model its entities; keep the group heading with "Provided by <product / service> – not modelled here" and list only the local entities the project still needs (e.g. a local user reference or mapping table).

| Group | Needed? (Yes / No / Partial) | Provided by (existing capability) | Local entities modelled |
| --- | --- | --- | --- |

Typical groups, when they are needed:

- **User & access management** – USER, ROLE, FEATURE, USER_ROLE_MAP, ROLE_FEATURE_MAP, USER_HIERARCHY, USER_DELEGATION; state which attributes are mastered by the identity provider.
- **Notification** – NOTIFICATION_TEMPLATE, NOTIFICATION_RULE, NOTIFICATION_TXN.
- **Audit & activity log** – ACTIVITY_LOG, AUDIT_LOG, USER_ACCESS_LOG, USER_SESSION (append-only).
- **Reference / master data** – lookup (valid values), configuration parameters, business calendar, domain masters.
- **Document** – DOCUMENT (polymorphic owner: owner_type + owner_id).
- **Integration & messaging** – OUTBOX_EVENT, INBOX / processed-message (idempotency), INTERFACE_LOG, job run log.

## 4. ER diagrams

### 4.1 Master ER diagram (logical, all services)

<Diagram: all entities grouped by owning service; cross-service references drawn as dashed lines.>

| Entity | Related entity | Relationship (verb) | Cardinality | Same / cross-service |
| --- | --- | --- | --- | --- |

### 4.2 Service-wise ER diagrams

#### 4.2.1 <Service / module>

<Diagram with full entity definitions of this service; entities of other services shown as stubs.>

| Entity | Related entity | Relationship (verb) | Cardinality |
| --- | --- | --- | --- |

## 5. Cross-service data & consistency

| Data object | Owner service | Consumer service | Mechanism (API call / event-replicated read copy / none) | Event(s) | Consistency (strong / eventual, max lag) | Reconciliation |
| --- | --- | --- | --- | --- | --- | --- |

## 6. Data classification & privacy summary

| Entity.column | Classification | Masking (UI / API / logs) | Encryption (at rest / field-level) | Access rule (role, data scope) | Retention |
| --- | --- | --- | --- | --- | --- |

## 7. Volumetrics, retention & archival

| Entity | Initial volume | Growth (per month) | 3-year volume | Retention | Archival / purge approach |
| --- | --- | --- | --- | --- | --- |

## 8. Schema management & reference data

| Topic | Approach |
| --- | --- |
| Schema migration tool and naming | |
| Versioning and backward-compatible changes (expand / contract) | |
| Seed / reference data (lookups, roles, configuration) | |
| Test data and masking for non-production | |
| Backup, restore and point-in-time recovery | |

## 9. Appendix

### 9.1 Sample data – <scenario name>

<Worked scenario showing rows across the main entities for one business flow (e.g. from creation to approval), with a timeline table.>

| # | When | Action / actor | Entities affected |
| --- | --- | --- | --- |

### 9.2 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
