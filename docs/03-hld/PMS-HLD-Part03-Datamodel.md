# PMS – HLD Part03: Data Model (Anchor)

Document ID: PMS-HLD-Part03-Datamodel-v1.0
Scope: data model anchor – conventions, ownership, index and cross-service view; entity definitions are in the module data model documents
Project: Payroll Management System (PMS) – proof of concept (POC), Stage 3 Solution Design
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 23-Nov-2026 | Rajesh Verma | First draft of §1–§3, based on the approved BRD set v1.0 (D-107), PMS-HLD-Part01 v1.0 rev 0.9, PMS-HLD-Part01a v1.0 rev 0.6 and PMS-HLD-Part02-Functional v1.0 rev 0.4; Part03 anchor design answers of 23 Nov 2026 (D-126) |
| 1.0 | 0.2 | 23-Nov-2026 | Rajesh Verma | Draft of §4 (master ER of the 5 business entities with text-version table; system tables and what they relate to) and §5 (cross-service data and consistency, 12 data objects) (D-127) |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3 approved (D-126); §4–§5 approved (D-127) |
| Data / DB lead | | | |
| Dev lead | | | |
| Security lead | | | |

## 2. Introduction: Data model

This document is the anchor of the PMS data model: modelling conventions, data ownership per service, the entity index with links to the module data model documents, the master ER view, cross-service consistency, and roll-up summaries of classification, volumetrics and schema management. Entity definitions (columns, keys, indexes) are only in the module data model documents (PMS-HLD-Part03-M1-EIMS to M4-SMS and M5-SUP); this anchor never repeats them (D-43). The common columns (§2.4) and the common audit entry (§2.5) are the only column lists here, because every service uses them unchanged. Rows that depend on a module document not yet written show "Module document (planned)" and are completed as each module document is written.

Reading rules:

- Business statuses and their transitions stay in the module BRDs §6; this document holds only how they are stored.
- Engine-specific types are used only for the chosen database, PostgreSQL 18 in every environment (Part01 §11, D-115); everything else is technology-neutral (Part01 §2).
- Rules that a standard will detail refer to `docs/04-standards/database-and-data (planned)` (Part01a §2).

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | PMS-BRD (anchor §6 BR-CMN rules, §7 integrations, §8.1 volumetrics) and module BRDs PMS-BRD-M1-EIMS to M4-SMS (§6 status lifecycles, §9 data requirements, §13 volumetrics), PMS-BRD-M5-SUP (§8 audit and activity log, §11 data) | v1.0, approved baseline (D-107) |
| 2 | Decision log `docs/decisions/decision-log.md` and ADRs `docs/decisions/adr/` | D-01 to D-125; ADR-001 to ADR-006 |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | PMS-HLD-Part01-Architecture-and-Design v1.0 rev 0.9 (§8.3 outbox and job lock, §10.8 privacy and retention, §11 technology stack, §12 data architecture, §13 data migration and seed data, §17 volumetrics) | Overall architecture and design |
| 2 | PMS-HLD-Part01a-Principles-Patterns-Decisions v1.0 rev 0.6 | Principles and patterns catalogue (group DATA); ADR register |
| 3 | PMS-HLD-Part02-Functional (anchor) v1.0 rev 0.4 and PMS-HLD-Part02-M1-EIMS to M4-SMS-Functional (planned) | Functional design: function index, cross-module flows XF-01 to XF-09, API, event and audit conventions (§6) |
| 4 | PMS-HLD-Part02-M5-SUP-Functional (planned) | Supporting modules (UM, AUTH, ADM) |
| 5 | PMS-HLD-Part03-M1-EIMS to M4-SMS-Datamodel (planned) | Module data models (entity definitions) |
| 6 | PMS-HLD-Part03-M5-SUP-Datamodel (planned) | Supporting-module data model (need basis) |
| 7 | Contracts (`contracts/openapi`, `contracts/events`) | API and event schemas |

### 2.2 Data ownership (database per service)

| Service / module | Database / schema | Entities owned | Entities read from other services (how: API / event-replicated copy) |
| --- | --- | --- | --- |
| EIMS | eims | EMPLOYEE, PROFILE_CHANGE_REQUEST; system tables EMPLOYEE_ID_COUNTER, AUDIT_ENTRY | Attendance and leave before a new date of joining – API (INT-09, AMS0120, LMS0080); user account – identity-provider admin API (INT-08), not stored in eims |
| AMS | ams | ATTENDANCE; system tables OUTBOX_EVENT, JOB_LOCK, AUDIT_ENTRY | Employee details and approver – API (INT-03, INT-04), short-lived in-memory copy; leave on a date – API (INT-06, LMS0070); salary status – API (INT-10, SMS0110) |
| LMS | lms | LEAVE_REQUEST; system table AUDIT_ENTRY | Employee details and approver – API (INT-03, INT-04), short-lived in-memory copy; attendance on leave dates – API (INT-06, AMS0110) |
| SMS | sms | SALARY_RECORD; system tables ATTENDANCE_APPLIED_VERSION, PROCESSED_EVENT, RECONCILIATION_RUN, RECONCILIATION_MISMATCH, JOB_LOCK, AUDIT_ENTRY | Attendance – event (INT-01, INT-02): the values a salary record needs are copied into it when generated; approved attendance – paged API for the nightly reconciliation (AMS0100); hourly wage rate – API (INT-05, EIMS0190), copied into the salary record (BR-SMS-02) |
| Identity provider | Its own database | User accounts, credentials (hashed), roles, sessions, security events – not modelled by PMS (D-29, ADR-003); need-basis check in PMS-HLD-Part03-M5-SUP | Employee Id, role and enabled state – set by EIMS through the admin API (INT-08) |
| Shell and API gateway | None | None – the shell composes module cards from the module APIs (INT-07); the gateway keeps user sessions in memory (ADR-004) | – |

Rules: no foreign keys or joins across service databases; a reference to another service's entity is held as its business key (Employee Id) or its record id (attendance id in SMS) and resolved through that service's API or, for SMS, from the copied event values (§5). There are no replicated read tables: copies of another service's data are short-lived and in memory only (Part01 §12, AP-DATA-09).

### 2.3 Modelling conventions

| Topic | Convention |
| --- | --- |
| Entity and column naming | Entity (table) names singular, UPPER_SNAKE in the documents and lower snake_case in the database (`EMPLOYEE` → `employee`); columns snake_case; no module prefix, since each service has its own database. Constraint and index names: `pk_<table>`, `uk_<table>_<columns>`, `fk_<table>_<referenced table>`, `ck_<table>_<column>`, `ix_<table>_<columns>`. Detail in docs/04-standards/database-and-data (planned), AP-DATA-14 |
| Primary key | Surrogate `id` of type `uuid`, generated by the service; it is also the record id in APIs and events (`/attendance-entries/{id}`, event `subject.id`). A business key, where one exists, is held separately with a unique constraint (AP-DATA-15) |
| Business identifiers | Employee Id `EMP` + 4 digits (`EMP0001`), column `employee_id` `varchar(7)`, unique in EMPLOYEE, never reused (FR-EIMS-040, BR-EIMS-01, D-71). Generated from a counter row in EMPLOYEE_ID_COUNTER that is raised in the same local transaction that saves the employee: a rolled-back onboarding leaves no gap, and concurrent onboardings wait on the counter row. Whether a failure after the identity-provider call can still leave a gap depends on the order of the two steps, designed in PMS-HLD-Part02-M5-SUP (OI-P02-01). Records without a business id (profile change request, attendance, leave request, salary record) are known by their `id` |
| References to other records | Inside a database: foreign key on `id`. Across databases: no foreign key (C-02, D-10, AP-DATA-07); the reference holds the other service's key – `employee_id` for employees, `attendance_id` (`uuid`) for attendance in SMS – and is checked through that service's API or event |
| User references | Every `*_by` column and `approver_id` is `varchar(30)` holding an Employee Id, the PMS Administrator's user name (FR-UM-004) or `SYSTEM` for jobs and events; for changes made on an event, the envelope actor (Part02 §6.2). No foreign key, as user accounts live in the identity provider |
| Date / time | Timestamps `timestamptz`, stored in UTC and shown in IST (BR-CMN-18, AP-DATA-13, D-117); column suffix `_at`. Business dates (work date, leave dates, date of birth, date of joining) `date`, meaning the IST calendar date; times of day (attendance from and to) `time` in 15-minute steps (D-77). The BRD's "Created Date", "Approved Date" etc. are stored as `created_at`, `approved_at` |
| Money | Amounts and hourly wage rates `numeric(12,2)`, INR only, no currency column (D-08); rounded half up to 2 decimals (D-90). Hours `numeric(5,2)` |
| Enumerations / statuses | Stored as the upper-case codes of the API (Part02 §6.1) in a `varchar` column with a check constraint listing the values of the module BRD §6 (e.g. `DRAFT`, `SUBMITTED`, `APPROVED`, `REJECTED`); no lookup tables in the POC, as values change only by release (D-97) |
| Soft delete | Business records are never physically deleted (BR-CMN-06, AP-DATA-04): `is_active` = false marks a discarded or deactivated record. Only the system tables named in §7 are cleaned up |
| Optimistic locking | `row_version` on every business record (§2.4): integer, 1 on creation, raised by 1 on each change. It is the version carried in command bodies and returned with each record, and it is `subject.version` in attendance events (Part02 §6.1, §6.2; FR-CMN-014, NFR-06). An update states the version it was based on; no row changed means 409 (`<MOD>-CON-001`) |
| Semi-structured data | `jsonb` only where the content is a message or a set of fields that varies per row: the outbox event (envelope and payload, Part02 §6.2). Any other use is decided in the module document with its reason |
| Append-only and system tables | Audit, outbox, processed-event, version, run, mismatch, counter and job-lock tables have none of the common columns of §2.4; each module document defines their columns. The audit table is written with an insert-only database grant (§2.5) |
| Database users | Per service, a schema owner used only by the migrations, and an application user with the rights its functions need – on AUDIT_ENTRY insert and select only (FR-ADM-103). Credentials per service and environment (Part01 §9.10) |
| Audit columns | §2.4; audit log §2.5 |

### 2.4 Common columns (apply to every business record unless stated)

Business records: EMPLOYEE, PROFILE_CHANGE_REQUEST, ATTENDANCE, LEAVE_REQUEST, SALARY_RECORD.

| Column | Type | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | N | Primary key (§2.3) |
| status | varchar(20) | N | Upper-case status code from the module BRD §6, check constraint (BR-CMN-02) |
| approver_id | varchar(30) | Y | Who decided the record; stored only with the decision – a waiting item has no stored approver, which is resolved from the current Manager Id when listed or decided (BR-CMN-02, D-123 (5)) |
| approved_at | timestamptz | Y | When the decision was taken (BRD "Approved Date") |
| remarks | varchar(500) | Y | Rejection, reopen or void reason (BR-CMN-02, BR-CMN-03) |
| is_active | boolean | N | Default true; false = soft-deleted (BR-CMN-06) |
| created_by | varchar(30) | N | Reference to user (§2.3) (BR-CMN-07) |
| created_at | timestamptz | N | Default current timestamp, UTC |
| updated_by | varchar(30) | Y | Reference to user |
| updated_at | timestamptz | Y | UTC |
| row_version | integer | N | Optimistic lock and event subject version: 1 on creation, + 1 on each change (§2.3) |

### 2.5 Common audit entry (one AUDIT_ENTRY table in each service database)

Not in the template. One structure for eims, ams, lms and sms (Part02 §6.4, ADM0010); module documents list only which records and fields they audit. Written in the same local transaction as the change (D-110 (12)); one entry per changed field, a creation with its initial values, a status change with old and new status and the remarks (FR-ADM-101, 102). Append only: the application user may insert and select, never update or delete; kept as long as the record, so never cleaned up (FR-ADM-103). Sensitive values are kept in full and protected like the record; passwords are never recorded (FR-ADM-104).

| Column | Type | Null | Notes |
| --- | --- | --- | --- |
| id | uuid | N | Primary key |
| flow_ref | char(14) | N | Flow reference of the user action, job run or event (Part01 §10.5, FR-ADM-113) |
| record_type | varchar(30) | N | Entity name, e.g. `EMPLOYEE`, `ATTENDANCE`, `USER_ACCOUNT` (account changes made through EIMS) |
| record_id | varchar(40) | N | Employee Id for EMPLOYEE and USER_ACCOUNT, otherwise the record `id` |
| field | varchar(40) | N | Column changed, or `created` / `status` |
| old_value | text | Y | Empty on creation; sensitive when the field is sensitive (§6) |
| new_value | text | Y | As old_value |
| process | varchar(60) | N | API id, job id or event type (e.g. `API-AMS-nn`, `JOB-CMN-01`, `ams.attendance.approved`) |
| changed_by | varchar(30) | N | Employee Id, Admin user name or `SYSTEM`; the envelope actor for event-driven changes |
| changed_at | timestamptz | N | UTC |

Index `ix_audit_entry_record (record_type, record_id, changed_at)` serves the history extract of one record in time order (ADM0020, FR-ADM-105); no other index in the POC.

## 3. Module data model documents & entity index

### 3.1 Module data model documents

| Module | Document | Service / database | Version | Status |
| --- | --- | --- | --- | --- |
| EIMS | PMS-HLD-Part03-M1-EIMS-Datamodel | EIMS service / eims | – | Not started |
| AMS | PMS-HLD-Part03-M2-AMS-Datamodel | AMS service / ams | – | Not started |
| LMS | PMS-HLD-Part03-M3-LMS-Datamodel | LMS service / lms | – | Not started |
| SMS | PMS-HLD-Part03-M4-SMS-Datamodel | SMS service / sms | – | Not started |
| SUP (UM, AUTH, ADM) | PMS-HLD-Part03-M5-SUP-Datamodel | Identity provider (need basis); common audit entry §2.5 | – | Not started |

Each module document is written after its Part02 module document (D-108).

### 3.2 Entity index

Status "Not started" with document section "Module document (planned)" until the module document is drafted, then the entity status values of the conventions (Draft, In review, Approved, Deferred, Moved, Removed) – as in the Part02 function index (D-123).

**Business entities**

| # | Entity | Module document (section) | Service | Type (master / transaction / history / config / log / reference) | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | EMPLOYEE | PMS-HLD-Part03-M1-EIMS – Module document (planned) | EIMS | Master | Not started |
| 2 | PROFILE_CHANGE_REQUEST | PMS-HLD-Part03-M1-EIMS – Module document (planned) | EIMS | Transaction | Not started |
| 3 | ATTENDANCE | PMS-HLD-Part03-M2-AMS – Module document (planned) | AMS | Transaction | Not started |
| 4 | LEAVE_REQUEST | PMS-HLD-Part03-M3-LMS – Module document (planned) | LMS | Transaction | Not started |
| 5 | SALARY_RECORD | PMS-HLD-Part03-M4-SMS – Module document (planned) | SMS | Transaction | Not started |

**System tables** (no common columns of §2.4; type "control" added to the template types for state the system keeps to run a rule)

| # | Entity | Module document (section) | Service | Type | Status |
| --- | --- | --- | --- | --- | --- |
| 6 | AUDIT_ENTRY | This anchor §2.5 (structure); each module document lists what it audits | EIMS, AMS, LMS, SMS (one table in each database) | History | Draft (§2.5) |
| 7 | EMPLOYEE_ID_COUNTER | PMS-HLD-Part03-M1-EIMS – Module document (planned) | EIMS | Control – one row, last Employee Id number issued (§2.3) | Not started |
| 8 | OUTBOX_EVENT | PMS-HLD-Part03-M2-AMS – Module document (planned) | AMS | Log – events written with the status change, published by AMS0090; sent rows kept 90 days (§7) | Not started |
| 9 | JOB_LOCK (ams) | PMS-HLD-Part03-M2-AMS – Module document (planned) | AMS | Control – one run at a time of the outbox clean-up job | Not started |
| 10 | ATTENDANCE_APPLIED_VERSION | PMS-HLD-Part03-M4-SMS – Module document (planned) | SMS | Control – one row per attendance id with the last applied version; its row lock serialises two SMS instances on one attendance (Part02 §6.2) | Not started |
| 11 | PROCESSED_EVENT | PMS-HLD-Part03-M4-SMS – Module document (planned) | SMS | Log – one row per consumed event id (unique), kept 90 days (§7) | Not started |
| 12 | RECONCILIATION_RUN | PMS-HLD-Part03-M4-SMS – Module document (planned) | SMS | Log – one row per nightly run: start, end, result, counts, flow reference; last run on the Admin dashboard (SMS0120) | Not started |
| 13 | RECONCILIATION_MISMATCH | PMS-HLD-Part03-M4-SMS – Module document (planned) | SMS | Log – one row per mismatch found by a run (FR-SMS-044), linked to the run | Not started |
| 14 | JOB_LOCK (sms) | PMS-HLD-Part03-M4-SMS – Module document (planned) | SMS | Control – one run at a time of JOB-CMN-01 (Part01 §8.3) | Not started |

User accounts, credentials, roles, sessions and security events are held by the identity provider and are not PMS entities (§2.2); PMS-HLD-Part03-M5-SUP records the need-basis result.

## 4. ER diagrams

### 4.1 Master ER diagram (logical, all services)

Entity level only, business entities grouped by owning service; cross-service references are dashed (held as a key, no foreign key). System tables are listed below the diagram.

```mermaid
flowchart LR
  subgraph EIMS["EIMS – eims"]
    EMP["EMPLOYEE"]
    PCR["PROFILE_CHANGE_REQUEST"]
  end
  subgraph AMS["AMS – ams"]
    ATT["ATTENDANCE"]
  end
  subgraph LMS["LMS – lms"]
    LV["LEAVE_REQUEST"]
  end
  subgraph SMS["SMS – sms"]
    SAL["SALARY_RECORD"]
  end
  EMP -- "reports to (0..1 : 0..n)" --> EMP
  EMP -- "has (1 : 0..n)" --> PCR
  ATT -. "belongs to (n : 1)" .-> EMP
  LV -. "belongs to (n : 1)" .-> EMP
  SAL -. "belongs to (n : 1)" .-> EMP
  SAL -. "is paid for (0..n : 1, at most one non-voided)" .-> ATT
```

| Entity | Related entity | Relationship (verb) | Cardinality | Same / cross-service |
| --- | --- | --- | --- | --- |
| EMPLOYEE | EMPLOYEE | reports to (Manager Id; empty for the one top-level employee, BR-CMN-01) | 0..1 : 0..n | Same (eims) |
| PROFILE_CHANGE_REQUEST | EMPLOYEE | is raised for | 0..n : 1 | Same (eims) |
| ATTENDANCE | EMPLOYEE | belongs to (Employee Id) | 0..n : 1 | Cross (ams → eims) |
| LEAVE_REQUEST | EMPLOYEE | belongs to (Employee Id) | 0..n : 1 | Cross (lms → eims) |
| SALARY_RECORD | EMPLOYEE | belongs to (Employee Id) | 0..n : 1 | Cross (sms → eims) |
| SALARY_RECORD | ATTENDANCE | is paid for (attendance id); at most one non-voided record per attendance (BR-SMS-01, NFR-06) | 0..n : 1 | Cross (sms → ams) |
| ATTENDANCE, LEAVE_REQUEST, PROFILE_CHANGE_REQUEST, SALARY_RECORD | EMPLOYEE | decided by (approver_id, stored only with the decision) | 0..n : 0..1 | Cross, except PROFILE_CHANGE_REQUEST and EMPLOYEE in eims |
| ATTENDANCE | LEAVE_REQUEST | checked against on the same employee and date (INT-06); no stored reference | – | Cross (ams ↔ lms) |

Employee Ids are never deleted or reused (BR-CMN-06, FR-EIMS-040), so a cross-service reference never points to a missing employee.

**System tables and what they relate to**

| System table | Service | Relates to | Relationship |
| --- | --- | --- | --- |
| AUDIT_ENTRY | eims, ams, lms, sms | Every business record of its own database (record type + record id) | Many entries per record, no foreign key (one table for all record types) |
| EMPLOYEE_ID_COUNTER | eims | EMPLOYEE | One row; holds the last number issued |
| OUTBOX_EVENT | ams | ATTENDANCE | 0..n events per attendance (approved, reopened), written in the same transaction |
| JOB_LOCK | ams, sms | Outbox clean-up job; JOB-CMN-01 | One row per job |
| ATTENDANCE_APPLIED_VERSION | sms | ATTENDANCE (attendance id, cross-service) | One row per attendance whose event or reconciliation was applied |
| PROCESSED_EVENT | sms | OUTBOX_EVENT (event id, cross-service) | One row per consumed event |
| RECONCILIATION_RUN | sms | – | One row per nightly run |
| RECONCILIATION_MISMATCH | sms | RECONCILIATION_RUN (foreign key); ATTENDANCE and SALARY_RECORD by id | 0..n per run |

Service-wise ER diagrams with full entity definitions are in each module data model document.

## 5. Cross-service data & consistency

| Data object | Owner service | Consumer service | Mechanism (API call / event-replicated read copy / none) | Event(s) | Consistency (strong / eventual, max lag) | Reconciliation |
| --- | --- | --- | --- | --- | --- | --- |
| Approved attendance: attendance id, Employee Id, work date, from and to time, hours, version | AMS | SMS | Event; the values a salary record needs are copied into SALARY_RECORD when it is generated (SMS0080, XF-02) | ams.attendance.approved (INT-01) | Eventual: normally under 1 minute (NFR-01); up to the next night if delivery fails | JOB-CMN-01 creates any missing record (XF-04) |
| Reopened attendance | AMS | SMS | Event; voids the non-voided salary record (SMS0090, XF-03) | ams.attendance.reopened (INT-02) | Eventual: normally under 1 minute; the record stays Disputed meanwhile | JOB-CMN-01 voids any record whose attendance is no longer Approved |
| Order and duplicates of the two events | AMS | SMS | Version and event id stored in ATTENDANCE_APPLIED_VERSION and PROCESSED_EVENT in the salary change transaction (Part02 §6.2) | INT-01, INT-02 | A lower or equal version, or a known event id, changes nothing | JOB-CMN-01 stores the version it read in the same way |
| Approved attendance for a date range | AMS | SMS (reconciliation job) | Paged API, service token (AMS0100) | – | Read at run time | This is the reconciliation |
| Hourly wage rate | EIMS | SMS | API (INT-05, EIMS0190) at generation; copied into the salary record (BR-SMS-02) | – | Strong at the read; the copied rate is not changed by a later rate change (BR-CMN-13, no rate history, D-90) | None needed |
| Employee details (name, manager, active state, date of joining) | EIMS | AMS, LMS, SMS, shell | API (INT-03, EIMS0170); short-lived in-memory copy, lifetime set in the module documents | – | Strong at the read; a cached copy may lag by its lifetime | None |
| Approver of a record | EIMS | AMS, LMS, SMS, shell | API (INT-04, EIMS0180) whenever an item is listed or decided; approver_id stored only with the decision (D-123 (5)) | – | Strong at the decision; a manager change moves waiting items at once (XF-08) | None needed |
| Attendance / leave on the same date | AMS, LMS | LMS, AMS | API (INT-06, AMS0110, LMS0070) on save and submit; never skipped | – | Check-then-act across two databases: two simultaneous submissions can both pass (OI-P02-02) | None in the POC (OI-P02-02) |
| Records before a new date of joining | AMS, LMS | EIMS | API (INT-09, AMS0120, LMS0080) before the change is saved | – | As above (OI-P02-02) | None in the POC (OI-P02-02) |
| Salary status of approved attendance | SMS | AMS (and the shell through AMS) | API (INT-10, SMS0110) when history and inbox views load and before a reopen | – | Read at view time; reopen refused server-side unless the record is Disputed (D-122) | None needed |
| Dashboard tiles, to-do items, inbox items | EIMS, AMS, LMS, SMS | Shell | API (INT-07), one call per module card | – | Read at load; each card fails on its own (FR-CMN-008) | None |
| User account: Employee Id, role, enabled state | EIMS (values) | Identity provider (holds the account) | Admin API (INT-08) on onboarding, role change, reset and deactivation | – | Two steps in two systems; order and recovery designed in PMS-HLD-Part02-M5-SUP (OI-P02-01) | None in the POC (OI-P02-01) |

## 6. Data classification & privacy summary

Drafted in a later review.

## 7. Volumetrics, retention & archival

Drafted in a later review.

## 8. Schema management & reference data

Drafted in a later review.

## 9. Appendix

### 9.1 Open items

Drafted in a later review.
