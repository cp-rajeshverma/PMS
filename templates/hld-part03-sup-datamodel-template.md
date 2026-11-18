# <Project> – HLD Part03-M<n>: Supporting Modules (SUP) Data Model

Document ID: <PRJ>-HLD-Part03-M<n>-SUP-Datamodel-v<x.y>
Module: Supporting modules (User & access, Notification, Audit & activity log, Reference & master data, Document, Integration & messaging)
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - Supporting-module entities are modelled on a need basis only. Where an existing platform or product provides the capability, keep the group heading with "Provided by <product / service> – not modelled here" and model only the local entities still needed (e.g. a local user reference or mapping table).
> - Each entity uses the entity structure of the module data model template §3.1 (purpose, columns, constraints & indexes, relationships, data classification, volumetrics & retention, notes); it is not repeated here.
> - Conventions, common columns, ownership rules and cross-service consistency are in the anchor <PRJ>-HLD-Part03-Datamodel.
> - Entity status values: Draft / In review / Approved / Removed / Moved.
> - Every diagram keeps a text-version table beneath it.

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | Data model based on BRD v<x> and Part02-SUP v<x> |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Data / DB lead | | | |
| Security lead | | | |
| Dev lead | | | |

## 2. Introduction

This document defines the entities of the supporting modules that the project needs to model itself, and records which supporting capabilities are provided by existing platforms or products.

### 2.1 Reference documents

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-BRD (§4, §9, §10) | Roles, data requirements, notifications |
| 2 | <PRJ>-HLD-Part03-Datamodel (anchor) | Conventions, common columns, ownership, cross-service consistency |
| 3 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Supporting functions that use these entities |
| 4 | <PRJ>-HLD-Part01-Architecture-and-Design (§9 A&A, §10 logging) | Identity, audit and logging architecture |

## 3. Need-basis assessment

| Group | Needed? (Yes / No / Partial) | Provided by (existing capability) | Local entities modelled | Owning component | Consumer modules |
| --- | --- | --- | --- | --- | --- |
| User & access management | | | | | |
| Notification | | | | | |
| Audit & activity log | | | | | |
| Reference & master data | | | | | |
| Document | | | | | |
| Integration & messaging | | | | | |

## 4. Database design

### 4.1 User & access management

<"Provided by <product> – not modelled here", or entities below. Typical: USER (local reference), ROLE, FEATURE, USER_ROLE_MAP, ROLE_FEATURE_MAP, USER_HIERARCHY, USER_DELEGATION. State which attributes are mastered by the identity provider.>

#### 4.1.1 <ENTITY_NAME> (<Status>)

<Entity structure per module data model template §3.1.>

### 4.2 Notification

<Typical: NOTIFICATION_TEMPLATE, NOTIFICATION_RULE, NOTIFICATION_TXN.>

### 4.3 Audit & activity log

<Typical: ACTIVITY_LOG, AUDIT_LOG, USER_ACCESS_LOG, USER_SESSION (append-only).>

### 4.4 Reference & master data

<Typical: lookup / valid values, configuration parameters, business calendar, domain masters.>

### 4.5 Document

<Typical: DOCUMENT (polymorphic owner: owner_type + owner_id).>

### 4.6 Integration & messaging

<Typical: OUTBOX_EVENT, INBOX / processed-message (idempotency), INTERFACE_LOG, JOB_RUN_LOG. State whether each functional service holds its own copy of these tables.>

## 5. ER diagram

<Diagram of the modelled groups; entities of functional modules shown as stubs (business key only).>

| Entity | Related entity | Relationship (verb) | Cardinality | Same / cross-service |
| --- | --- | --- | --- | --- |

## 6. Volumetrics & retention

| Entity | Initial volume | Growth (per month) | 3-year volume | Retention | Archival / purge approach |
| --- | --- | --- | --- | --- | --- |

## 7. Appendix

### 7.1 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
