# <Project> – HLD Part03: Data Model (Anchor)

Document ID: <PRJ>-HLD-Part03-Datamodel-v<x.y>
Scope: data model anchor – conventions, ownership, index and cross-service view; entity definitions are in the module data model documents
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - This anchor document holds what is common to all services. Entity definitions live only in the module data model documents (<PRJ>-HLD-Part03-M<n>-<MOD>-Datamodel, one per module, plus <PRJ>-HLD-Part03-M<n>-SUP-Datamodel); the anchor never repeats columns.
> - Entity status values: Draft / In review / Approved / Removed / Moved (keep a one-line stub with the reason or new location).
> - Business statuses and their transitions come from the module BRDs §6; this document defines only how they are stored.
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

This document is the anchor of the [<Project>] data model: modelling conventions, data ownership per service, the entity index with links to the module data model documents, the master ER view, cross-service consistency, and roll-up summaries of classification, volumetrics and schema management.

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | <PRJ>-BRD (anchor §8.1 volumetrics) and module BRDs (§6 status lifecycles, §9 data requirements, §13 volumetrics) | v<x> |
| 2 | Decision log / ADRs | D-01 to D-<nn> |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-Architecture-and-Design (§12 data architecture, §13 data migration) | Overall architecture and design |
| 2 | <PRJ>-HLD-Part01a-Principles-Patterns-Decisions | Principles and patterns catalogue; ADR register |
| 3 | <PRJ>-HLD-Part02-Functional (anchor) and <PRJ>-HLD-Part02-M1..M<n>-<MOD>-Functional | Functional design (entity usage per function, cross-module flows) |
| 4 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Supporting modules |
| 5 | <PRJ>-HLD-Part03-M1..M<n>-<MOD>-Datamodel | Module data models (entity definitions) |
| 6 | <PRJ>-HLD-Part03-M<n>-SUP-Datamodel | Supporting-module data model (need basis) |
| 7 | Contracts (`contracts/`) | API and event schemas |

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
| Enumerations / statuses | <lookup table or check constraint; values from module BRDs §6> |
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

## 3. Module data model documents & entity index

### 3.1 Module data model documents

| Module | Document | Service / database | Version | Status |
| --- | --- | --- | --- | --- |
| <MOD1> | <PRJ>-HLD-Part03-M1-<MOD1>-Datamodel | | | |
| SUP | <PRJ>-HLD-Part03-M<n>-SUP-Datamodel | | | |

### 3.2 Entity index

| # | Entity | Module document (section) | Service | Type (master / transaction / history / config / log / reference) | Status |
| --- | --- | --- | --- | --- | --- |

## 4. ER diagrams

### 4.1 Master ER diagram (logical, all services)

<Diagram at entity level only (no columns): all entities grouped by owning service; cross-service references drawn as dashed lines.>

| Entity | Related entity | Relationship (verb) | Cardinality | Same / cross-service |
| --- | --- | --- | --- | --- |

Service-wise ER diagrams with full entity definitions are in each module data model document.

## 5. Cross-service data & consistency

| Data object | Owner service | Consumer service | Mechanism (API call / event-replicated read copy / none) | Event(s) | Consistency (strong / eventual, max lag) | Reconciliation |
| --- | --- | --- | --- | --- | --- | --- |

## 6. Data classification & privacy summary

Roll-up of the classification tables in the module documents.

| Entity.column | Classification | Masking (UI / API / logs) | Encryption (at rest / field-level) | Access rule (role, data scope) | Retention |
| --- | --- | --- | --- | --- | --- |

## 7. Volumetrics, retention & archival

Roll-up of the module documents.

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

### 9.1 Open items

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
