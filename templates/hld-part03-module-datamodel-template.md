# <Project> – HLD Part03-M<n>: <Module name> (<MOD>) Data Model

Document ID: <PRJ>-HLD-Part03-M<n>-<MOD>-Datamodel-v<x.y>
Module: <Module name> (<MOD>) – service `<service-name>`, database `<db-name>`
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - One document per functional module; the supporting-module data model (<PRJ>-HLD-Part03-M<n>-SUP-Datamodel) uses this template with §3.0 Need-basis assessment.
> - Conventions, common columns, ownership rules and cross-service consistency are in the anchor <PRJ>-HLD-Part03-Datamodel; do not repeat them.
> - Entity status values: Draft / In review / Approved / Removed / Moved (keep a one-line stub with the reason or new location).
> - Business statuses and transitions come from BRD §6; this document defines only how they are stored.
> - Every diagram keeps a text-version table beneath it.

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | Data model based on BRD v<x> and Part02-M<n> v<x> |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Data / DB lead | | | |
| Dev lead | | | |

## 2. Introduction

This document defines the entities owned by the [<Module name>] service: columns, keys, constraints, relationships, classification, volumetrics and retention.

### 2.1 Reference documents

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-BRD (§6, §9, §13) | Status lifecycles, data requirements, volumetrics |
| 2 | <PRJ>-HLD-Part03-Datamodel (anchor) | Conventions, common columns, ownership, cross-service consistency |
| 3 | <PRJ>-HLD-Part02-M<n>-<MOD>-Functional | Functions that use these entities |
| 4 | Contracts (`contracts/`) | API and event schemas |

### 2.2 Entity list

| # | Entity | Type (master / transaction / history / config / log / reference) | Purpose | Status |
| --- | --- | --- | --- | --- |

## 3. Database design

### 3.0 Need-basis assessment (SUP document only; delete in functional module documents)

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

### 3.1 <ENTITY_NAME> (<Status>)

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

### 3.2 <ENTITY_NAME>_HISTORY / _STATUS_LIFECYCLE (<Status>)

<History and status-transition entities follow the same structure; state whether append-only.>

## 4. ER diagram

<Diagram with full entity definitions of this service; entities of other services shown as stubs (business key only).>

| Entity | Related entity | Relationship (verb) | Cardinality | Same / cross-service |
| --- | --- | --- | --- | --- |

## 5. Module volumetrics & retention

| Entity | Initial volume | Growth (per month) | 3-year volume | Retention | Archival / purge approach |
| --- | --- | --- | --- | --- | --- |

## 6. Appendix

### 6.1 Sample data – <scenario name>

<Worked scenario showing rows across this module's entities for one business flow, with a timeline table.>

| # | When | Action / actor | Entities affected |
| --- | --- | --- | --- |

### 6.2 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
