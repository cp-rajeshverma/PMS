# PMS – HLD Part02-M1: Employee Information Management System (EIMS) Functional Design

Document ID: PMS-HLD-Part02-M1-EIMS-Functional-v1.0
Module: Employee Information Management System (EIMS)
Project: Payroll Management System (PMS) – proof of concept (POC), Stage 3 Solution Design
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 23-Nov-2026 | Rajesh Verma | First draft of §1–§2 and §3.1, based on the approved BRD set v1.0 (D-107), UX v1.1 (D-105), PMS-HLD-Part01 v1.0 rev 0.9, Part01a v1.0 rev 0.7, the Part02 anchor v1.0 rev 0.5 and the Part03 anchor v1.0 rev 0.4; threat-review method, settlement of the identity-provider order in this document and review grouping of 23 Nov 2026 (D-130) |
| 1.0 | 0.2 | 23-Nov-2026 | Rajesh Verma | §3.2.1 EIMS0010 employee directory drafted: API-EIMS-01, role copy on EMPLOYEE, search, sort and paging (D-131) |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3.1 approved (D-130); §3.2.1 EIMS0010 approved (D-131) |
| Product owner | Rajesh Verma | 23-Nov-2026 | §1–§3.1 approved (D-130); §3.2.1 EIMS0010 approved (D-131) |
| Business analyst | | | |
| Dev lead | | | |

## 2. Introduction: Function design

This document describes the high-level solution approach for each system function of the Employee Information Management System (EIMS) module: APIs, database, orchestration and scenarios. Architecture-wide decisions (stack, resilience defaults, logging, security) are in PMS-HLD-Part01; cross-module flows and common design conventions (API, events, errors, audit and activity log, frontend) are in the Part02 anchor. Neither is repeated here. This is the first module document of the Part02 set; AMS, LMS, SMS and SUP follow its structure and depth.

Reading rules:

- Conventions of the Part02 anchor §2 apply: function ids `EIMS0010` to `EIMS0200` in steps of 10 (anchor §4); API references `[API-EIMS-nn : METHOD /api/eims/v1/<resource> (Purpose : …)]`, rolled up in §4.2; business statuses stay in PMS-BRD-M1-EIMS §6; the design is technology-neutral and names the identity provider, gateway and broker by role.
- Requirements, rules and screen behaviour are referenced by their BRD and UX ids (FR-EIMS, VR-EIMS, BR-EIMS, BR-CMN, SCR-EIMS, UJ-EIMS) and not restated. Column definitions belong to PMS-HLD-Part03-M1-EIMS-Datamodel (planned); this document names entities and the rules of the Part03 anchor, not columns.
- Cross-module flows XF-01, XF-07, XF-08 and XF-09 stay in the Part02 anchor §5; the function chapters here design only the EIMS steps of each flow.
- The identity-provider side of an account change (UM0010 to UM0050) is designed in PMS-HLD-Part02-M5-SUP (planned); here it is a call to that function. The order of the identity-provider call and the EIMS commit, retry of a half-done onboarding and recovery (OI-P02-01) are settled in this document, with EIMS0020 and EIMS0040 to EIMS0060, because EIMS owns the transaction and the Employee Id counter (Part03 anchor §2.3); PMS-HLD-Part02-M5-SUP references them.
- Design status per function: Not started until its chapter is drafted, then Draft, In review, Approved or Deferred (D-123).
- Notifications: none in the POC (C-05, NM is Phase 2). Each function's §3.2.n.5.9 shows "None (C-05)" with its audit and activity-log entries; in-app items (BRD §10) are dashboard and inbox items supplied by EIMS0200.
- Every diagram keeps a text-version table.

**Threat review in §3.2.n.5.8 (closes OI-P01a-08).** Every function's "Security & data privacy" part applies STRIDE – Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege – only at the trust boundaries the function crosses. The template's five rows (authorization, sensitive fields, masking, encryption, logging) are kept; one "Threat review" row is added per boundary crossed, naming only the STRIDE threats that apply there and the control that answers each, by reference to PMS-HLD-Part01 §9 and §16.2 or the Part02 anchor §6. A threat without an existing control is recorded as an open item of the document, not designed ad hoc. The detailed method text goes to docs/04-standards/security (planned).

| Boundary | From → to | Typical threats | Existing controls (reference) |
| --- | --- | --- | --- |
| TB-1 | Browser → edge and API gateway | S (stolen session), T (forged request), I (data in transit), D (request flood) | HttpOnly session cookie and CSRF token (ADR-004, Part01 §9.6); TLS with HSTS, WAF and rate limit at the edge (ADR-005, Part01 §9.8); payload limit 1 MB |
| TB-2 | API gateway → EIMS service | S (call without a valid user), E (route or record outside the role or data scope), R (action without a trace) | Gateway route per role group, access token validated again by the service (Part01 §9.7, §9.8); role and data scope in the service and in the query (UM0060); neutral refused response (anchor §6.3, D-99); flow reference and activity log (Part01 §10.3, §10.5) |
| TB-3 | Other service or shell → EIMS, and EIMS → AMS / LMS | S (caller not the service it claims), E (internal API reached from the browser), I (more data than the caller needs) | Service token or relayed user token, network policies per service pair (Part01 §9.9, D-111); `/internal/` APIs never routed by the gateway (anchor §6.1); responses limited to the fields of the integration (INT-03 to 05, 07, 09) |
| TB-4 | EIMS → identity provider (INT-08) | S (misuse of the admin API), T / R (account change without a record), I (temporary password exposed) | Separate service client with client credentials limited to user management – create, update role, reset credential, disable, end sessions (Part01 §9.2, ADR-003); account changes audited by EIMS and recorded as security events (anchor §6.4, AUTH0060); password never stored or logged (FR-ADM-104, NFR-EIMS-02) |
| TB-5 | EIMS service → eims database | T (change outside the application), R (change without audit), I (data at rest) | Database per service with its own credentials (Part03 anchor §2.2); audit entry in the same transaction, insert-and-select-only grant (Part03 anchor §2.5); encrypted storage and backups (Part03 anchor §6) |

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | PMS-BRD (anchor) – §4.3 roles and data scope, §5.3 dashboard and inbox, §6 BR-CMN, §7 INT-03 to INT-05, INT-07 to INT-09; PMS-BRD-M1-EIMS; PMS-BRD-M5-SUP (FR-UM-001 to 015, FR-AUTH, FR-ADM-101 to 117) | v1.0, approved baseline (D-107) |
| 2 | UX Journey Index and UX Summaries SCR-EIMS-01 to 04, SCR-SH-03, SCR-SH-04; mockups `docs/01-ux/mockups/html/scr-eims-0*.html` | v1.1 (D-105) |
| 3 | Decision log / ADRs | D-01 to D-131; ADR-001 to ADR-006 |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | PMS-HLD-Part01-Architecture-and-Design v1.0 rev 0.9 | Overall architecture and design: integration catalogue §8.2, resilience defaults §8.5, authorization §9.7 to §9.9, log record §10.3, flow reference §10.5, masking §10.8, load tests §14, OWASP mapping §16.2, NFR realization §16.3 |
| 2 | PMS-HLD-Part01a-Principles-Patterns-Decisions v1.0 rev 0.7 | Principles and patterns catalogue (AP-SEC-16 threat modelling); ADR register |
| 3 | PMS-HLD-Part02-Functional (anchor) v1.0 rev 0.5 | Function index §4, cross-module flows XF-01, XF-07 to XF-09 (§5), API, error, audit and frontend conventions (§6), roll-up inventories (§7) |
| 4 | PMS-HLD-Part02-M2-AMS, M3-LMS, M4-SMS-Functional (planned) | Callers of the EIMS APIs; providers of INT-09 (AMS0120, LMS0080) |
| 5 | PMS-HLD-Part02-M5-SUP-Functional (planned) | UM0010 to UM0060, AUTH, ADM0010 to ADM0060 called by EIMS functions |
| 6 | PMS-HLD-Part03-Datamodel (anchor) v1.0 rev 0.4 and PMS-HLD-Part03-M1-EIMS-Datamodel (planned) | Data model: eims ownership, conventions, common columns, common audit entry; EIMS entity definitions |
| 7 | API contract `contracts/openapi/eims-v1.yaml` (planned) | OpenAPI 3 contract of the EIMS APIs |

## 3. Module: Employee Information Management System

### 3.1 Preread

#### 3.1.1 Overview

EIMS holds the employee master data of PMS and is the source of the reporting line that every approval in PMS follows.

| Item | Detail |
| --- | --- |
| What it does | Onboarding one employee at a time with a system-generated Employee Id and temporary password; maintenance of the Admin-owned fields (date of joining, role, manager, hourly wage rate); deactivation; password reset; the employee's own profile with submit, withdraw and approval; profile change requests on an approved profile; the employee directory (PMS-BRD-M1-EIMS §7) |
| Who uses it | Admin (onboarding, maintenance, directory, top-level employee's approvals); Manager (own profile, direct reports in the directory and their approvals); Employee (own profile and change requests); system SYS-EIMS (Employee Id and temporary password, UJ-SYS-04) – BRD §4 |
| What it owns | Data in the eims database: EMPLOYEE and PROFILE_CHANGE_REQUEST, system tables EMPLOYEE_ID_COUNTER and AUDIT_ENTRY (Part03 anchor §2.2). APIs under `/api/eims/v1`: the screen APIs of SCR-EIMS-01 to 04 and the APIs other modules and the shell use – INT-03, INT-04, INT-05, INT-07 (§4.2). EIMS publishes and consumes no events |
| What it does not own | The user account, role and password – held in the identity provider and changed only through UM0010 to UM0050 (INT-08, BR-EIMS-09, ADR-003); attendance and leave – read only through the INT-09 checks of AMS0120 and LMS0080 |
| Depends on | Identity provider through UM (INT-08); AMS and LMS for the date-of-joining check (INT-09, XF-07); API gateway and shell (session, routing, layout); ADM0010 to ADM0060 for audit, activity log and flow reference |
| Used by | Shell (INT-07: EIMS card and inbox items, SH0020 to SH0040); AMS, LMS, SMS and the shell (INT-03 employee details, INT-04 approver); SMS (INT-05 hourly wage rate) |
| In-memory copies of other services' data | None. EIMS reads AMS and LMS only for the INT-09 check, at the moment of the change and never cached; OI-P03-03 stays with PMS-HLD-Part02-M2-AMS |
| Last approved profile | The EMPLOYEE record is always the last approved profile (or the not-yet-approved first profile); a profile change request holds the requested values separately, so other modules keep reading the approved values while a request is open (BR-CMN-11, FR-EIMS-028, D-70 – replaces the D-29 snapshot). The previous values are kept on the request when it is approved (BRD §9.2) |

#### 3.1.2 Module process flow

```mermaid
flowchart TD
  A0(["Admin: + Onboard employee"]) --> F20["EIMS0020 Onboard employee<br/>+ EIMS0030 Employee Id, temporary password<br/>(UM0010 account)"]
  F20 --> D1["Profile Draft, Active"]
  D1 --> F70["EIMS0070 View my profile<br/>EIMS0080 Save draft"]
  F70 --> F90["EIMS0090 Submit / resubmit"]
  F90 --> S1["Profile Submitted"]
  S1 -- "withdraw" --> F100["EIMS0100 Withdraw"] --> D1
  S1 --> F140["EIMS0140 Open for review<br/>(manager; Admin for top-level)"]
  F140 --> Q1{"Decision"}
  Q1 -- "approve" --> F150["EIMS0150 Approve"] --> AP["Profile Approved"]
  Q1 -- "reject" --> F160["EIMS0160 Reject with remarks"] --> RJ["Profile Rejected"] --> F70
  AP --> F110["EIMS0110 Start / save change request"]
  F110 --> F120["EIMS0120 Submit / resubmit request"]
  F120 --> F140
  F110 & F120 -- "withdraw" --> F130["EIMS0130 Withdraw request"]
  F150 -- "change request: values applied" --> AP
  A1(["Admin: directory EIMS0010"]) --> F40["EIMS0040 Edit Admin-owned fields<br/>(INT-09 check XF-07; manager change XF-08;<br/>role change UM0050)"]
  A1 --> F50["EIMS0050 Deactivate (UM0040)"]
  A1 --> F60["EIMS0060 Reset password (UM0030)"]
  F50 --> IN["Inactive"]
  AP -. "INT-03, INT-04, INT-05" .-> X["AMS, LMS, SMS, shell<br/>EIMS0170, EIMS0180, EIMS0190"]
  S1 -. "INT-07 inbox and card" .-> SH["Shell<br/>EIMS0200"]
```

**Text version of the diagram**

| Step | Function id | Actor | From state | Action / decision | To state / handover |
| --- | --- | --- | --- | --- | --- |
| 1 | EIMS0020, EIMS0030 | Admin; system | – | Onboard: validate, generate Employee Id and temporary password, create the account (UM0010) | Profile Draft, account Active (XF-01) |
| 2 | EIMS0070, EIMS0080 | Employee | Draft or Rejected | View, save draft | Unchanged |
| 3 | EIMS0090 | Employee | Draft or Rejected | Submit or resubmit | Submitted; item for the approver (EIMS0200) |
| 4 | EIMS0100 | Employee | Submitted (no decision yet) | Withdraw | Draft |
| 5 | EIMS0140 | Manager; Admin for the top-level employee | Submitted | Open for review | Unchanged |
| 6 | EIMS0150 / EIMS0160 | As step 5 | Submitted | Approve / reject with remarks | Approved / Rejected (back to step 2) |
| 7 | EIMS0110 | Employee | Profile Approved, no open request | Start and save a change request | Request Draft |
| 8 | EIMS0120 | Employee | Request Draft or Rejected | Submit or resubmit (at least one changed value) | Request Submitted; review as steps 5–6 |
| 9 | EIMS0130 | Employee | Request Draft, Submitted (no decision) or Rejected | Withdraw | Request Withdrawn |
| 10 | EIMS0150 | Approver | Request Submitted | Approve: requested values applied to the profile, previous values kept on the request | Request Approved; profile stays Approved |
| 11 | EIMS0010, EIMS0040 | Admin | Any active employee | Change date of joining (INT-09, XF-07), role (UM0050, XF-09), manager (XF-08) or hourly wage rate | Profile status unchanged (FR-EIMS-012) |
| 12 | EIMS0050 | Admin | Active | Deactivate (UM0040, XF-09) | Inactive |
| 13 | EIMS0060 | Admin | Active | Reset password (UM0030, XF-09) | Temporary password shown once |
| 14 | EIMS0170 to EIMS0190 | AMS, LMS, SMS, shell | – | Read employee details, approver, hourly wage rate | Read only |
| 15 | EIMS0200 | Shell | – | Read the EIMS card, to-do items and inbox items | Read only (XF-05) |

#### 3.1.3 High-level ER diagram

Entity level only; full definitions in PMS-HLD-Part03-M1-EIMS-Datamodel (planned).

```mermaid
flowchart LR
  EMP["EMPLOYEE"]
  PCR["PROFILE_CHANGE_REQUEST"]
  CNT["EMPLOYEE_ID_COUNTER<br/>(control, one row)"]
  AUD["AUDIT_ENTRY<br/>(insert-only)"]
  EMP -- "reports to (0..1 : 0..n)" --> EMP
  EMP -- "has (1 : 0..n, at most one open)" --> PCR
  CNT -. "issues Employee Id to" .-> EMP
  AUD -. "records changes of (by record type and id)" .-> EMP & PCR
```

**Text version of the diagram**

| Entity | Related entity | Relationship | Cardinality | Rule |
| --- | --- | --- | --- | --- |
| EMPLOYEE | EMPLOYEE | reports to (Manager Id) | 0..1 : 0..n | Empty only for the one top-level employee (BR-CMN-01, VR-EIMS-05); no reporting loop |
| PROFILE_CHANGE_REQUEST | EMPLOYEE | is raised for | 0..n : 1 | At most one open request (Draft, Submitted, Rejected) per employee (BR-EIMS-03) |
| EMPLOYEE_ID_COUNTER | EMPLOYEE | issues the Employee Id | 1 : 0..n | Raised in the same local transaction that saves the employee; never reused (Part03 anchor §2.3, BR-EIMS-01) |
| AUDIT_ENTRY | EMPLOYEE, PROFILE_CHANGE_REQUEST, user account | records each change | 0..n : 1 | Record types EMPLOYEE, PROFILE_CHANGE_REQUEST, USER_ACCOUNT; no foreign key; written in the same transaction (Part03 anchor §2.5) |

The role is not on EMPLOYEE: it is held with the user account in the identity provider (BR-EIMS-09).

#### 3.1.4 Status lifecycle

Business statuses and transitions are defined in PMS-BRD-M1-EIMS §6.1 (profile), §6.2 (Active / Inactive) and §6.3 (profile change request). Technical handling:

- Profile status is the `status` of EMPLOYEE, request status the `status` of PROFILE_CHANGE_REQUEST, both with check constraints of the BRD codes; Active / Inactive is `is_active` of EMPLOYEE (Part03 anchor §2.3, §2.4).
- Each transition is one command API of the owning function. The service checks the actor, data scope and current status, then updates the record with the version the command carries (row_version + 1); a version or status that no longer matches is refused (EIMS-CON-001 or a BUS code) and nothing changes (anchor §6.1).
- EIMS emits no events: other modules read the current values at the time they need them (INT-03, INT-04, INT-07).
- Every transition writes its audit entries in the same local transaction and an activity-log record with the function's step names (anchor §6.4).

| Transition | Enforced in | Event emitted | Audit / activity entry |
| --- | --- | --- | --- |
| Profile – → Draft, account Active | EIMS0020 (with UM0010) | None | EMPLOYEE `created` with initial values; USER_ACCOUNT `created` (no password) |
| Profile Draft / Rejected → Draft / Rejected (save) | EIMS0080 | None | One entry per changed field |
| Profile Draft / Rejected → Submitted | EIMS0090 | None | Changed fields and `status` |
| Profile Submitted → Draft | EIMS0100 | None | `status` |
| Profile Submitted → Approved / Rejected | EIMS0150 / EIMS0160 | None | `status` with the remarks of a rejection; approver and decision time |
| Request – → Draft, Draft → Draft | EIMS0110 | None | PROFILE_CHANGE_REQUEST `created`; changed fields |
| Request Draft / Rejected → Submitted | EIMS0120 | None | Changed fields and `status` |
| Request Draft / Submitted / Rejected → Withdrawn | EIMS0130 | None | `status` |
| Request Submitted → Approved (values applied) / Rejected | EIMS0150 / EIMS0160 | None | Request `status`; on approval one EMPLOYEE entry per applied field |
| Account Active → Inactive | EIMS0050 (with UM0040) | None | EMPLOYEE `is_active`; USER_ACCOUNT disabled |
| Admin-owned field change (profile status unchanged) | EIMS0040 (role change with UM0050) | None | One EMPLOYEE entry per field; USER_ACCOUNT role |
| Password reset | EIMS0060 (with UM0030) | None | USER_ACCOUNT password reset (no value) |

#### 3.1.5 System function index

| Function id | System function | Type (screen / API / backend job) | UX screen | Delivery phase | Design status |
| --- | --- | --- | --- | --- | --- |
| EIMS0010 | View the employee directory – search, filter, show inactive (FR-EIMS-001 to 004, 006) | Screen | SCR-EIMS-01 | POC | Approved |
| EIMS0020 | Onboard an employee – create the employee and the user account (FR-EIMS-010, 011, 014; INT-08) | Screen | SCR-EIMS-02 | POC | Not started |
| EIMS0030 | Generate Employee Id and temporary password (FR-EIMS-040, 041; UJ-SYS-04) | Backend process | – (shown once on SCR-EIMS-02) | POC | Not started |
| EIMS0040 | Edit Admin-owned fields – date of joining, role, manager, hourly wage rate (FR-EIMS-012 to 017; INT-08, INT-09) | Screen | SCR-EIMS-02 | POC | Not started |
| EIMS0050 | Deactivate an employee (FR-EIMS-018; INT-08) | Screen | SCR-EIMS-02 | POC | Not started |
| EIMS0060 | Reset an employee's password (FR-EIMS-005; INT-08) | Screen | SCR-EIMS-01 | POC | Not started |
| EIMS0070 | View my profile and its status (FR-EIMS-020) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0080 | Save a profile draft (FR-EIMS-021) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0090 | Submit or resubmit my profile (FR-EIMS-022, 024) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0100 | Withdraw my submitted profile (FR-EIMS-023) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0110 | Start and save a profile change request (FR-EIMS-025, 026) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0120 | Submit or resubmit a profile change request (FR-EIMS-026, 027) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0130 | Withdraw a profile change request (FR-EIMS-027) | Screen | SCR-EIMS-03 | POC | Not started |
| EIMS0140 | Open a profile or change request for review, or read only from the directory (FR-EIMS-030 to 032, 034, 035) | Screen | SCR-EIMS-04 | POC | Not started |
| EIMS0150 | Approve profiles or change requests, one or several; apply approved changes (FR-EIMS-033, 028) | Screen | SCR-EIMS-04, SCR-SH-04 | POC | Not started |
| EIMS0160 | Reject a profile or change request with remarks (FR-EIMS-033) | Screen | SCR-EIMS-04, SCR-SH-04 | POC | Not started |
| EIMS0170 | Provide employee details to other modules (INT-03) | API | – | POC | Not started |
| EIMS0180 | Resolve the approver of a record (INT-04) | API | – | POC | Not started |
| EIMS0190 | Provide the current hourly wage rate (INT-05) | API | – | POC | Not started |
| EIMS0200 | Supply EIMS dashboard tiles, to-do items and inbox items (INT-07) | API | SCR-SH-03, SCR-SH-04 | POC | Not started |

Review grouping (each review adds a revision row): R1 §1–§3.1 · R2 EIMS0010 · R3 EIMS0020–EIMS0030 · R4 EIMS0040 · R5 EIMS0050–EIMS0060 · R6 EIMS0070–EIMS0100 · R7 EIMS0110–EIMS0130 · R8 EIMS0140–EIMS0160 · R9 EIMS0170–EIMS0200 · R10 §4–§5.

### 3.2 EIMS system functions

#### 3.2.1 EIMS0010 – View the employee directory (Module: EIMS, Approved)

##### 3.2.1.1 Purpose, trigger and conditions

The Admin finds any employee and starts onboarding, editing or a password reset from the list; a manager sees the direct reports and opens a read-only profile.

| Item | Detail |
| --- | --- |
| Delivery phase | POC |
| Trigger | Admin opens "Employees" or a manager opens "My Team" (menu or Admin dashboard); any change of search, status filter, "Show inactive", sort or page |
| Pre-conditions | Signed in as Admin or Manager |
| Post-conditions | None – read only |

##### 3.2.1.2 Actor & data scope

| Role | Access (Read / Read-write / Approve / None) | Data scope (row-level) |
| --- | --- | --- |
| Employee | None – route refused (EIMS-ACC-002) | – |
| Manager | Read | Direct reports only: Manager Id = own Employee Id; manager and hourly wage rate not returned (FR-EIMS-002, BR-EIMS-10) |
| Admin | Read; starts EIMS0020, EIMS0040, EIMS0060 | All employees; the Admin account is not an employee and is never listed (BR-EIMS-08, D-24) |

##### 3.2.1.3 Requirement traceability

| Source | References |
| --- | --- |
| BRD functional requirements | FR-EIMS-001 to 004, 006; RPT-EIMS-06 |
| BRD business / validation rules | BR-EIMS-08, BR-EIMS-10; BR-CMN-06 |
| BRD NFRs | NFR-01, NFR-03, NFR-04; NFR-EIMS-01 |
| UX | UJ-EIMS-01, 06, 07, 08, 09; SCR-EIMS-01 |
| Decisions | D-24, D-58, D-63, D-99, D-105, D-124, D-130, D-131 |
| Related functions – depends on | UM0060 (role and scope check), UM0070 (no-access page), ADM0030, ADM0040 (activity log, flow reference) |
| Related functions – used by | EIMS0020 (+ Onboard employee), EIMS0040 and EIMS0050 (Edit), EIMS0060 (Reset password), EIMS0140 (View, read only) |

##### 3.2.1.4 Navigation & prototype reference

**Navigation:** Admin: Menu > Employees (or Admin dashboard) > Employee directory · Manager: Menu > My Team > Employee directory

**Prototype:** `docs/01-ux/mockups/html/scr-eims-01-directory.html` · UX summary `docs/01-ux/ux-summary/scr-eims-01-directory.md`

##### 3.2.1.5 Solution approach

###### 3.2.1.5.1 Design description

The [View the employee directory] function lets users work with the following sections / activities:

1. Search, status filter and "Show inactive"
2. Employee list with count and paging
3. Row and page actions (Admin: + Onboard employee, Edit, Reset password; Manager: View)

**Search, status filter and "Show inactive"**

1. One search box matches name, Employee Id or email; the profile-status filter and the "Show inactive" toggle narrow the list (FR-EIMS-003, 004).
2. Each change reloads the list from page 1 via [API-EIMS-01 : GET /api/eims/v1/employees (Purpose : list employees in the caller's data scope with search, filter, sort and paging)].
3. DB entity: [EMPLOYEE]
4. Search: one parameter `q`, case-insensitive "contains" on the full name, the Employee Id and the email. Filters: `status` (DRAFT, SUBMITTED, APPROVED, REJECTED) and `includeInactive` (default false, so inactive employees are hidden, BR-CMN-06).

**Employee list with count and paging**

1. Admin columns: Employee Id, name with role, email, manager, date of joining, hourly wage rate, profile status (FR-EIMS-001). Manager columns: the same without manager and rate (FR-EIMS-002). Inactive rows carry the "Inactive" badge (FR-EIMS-004).
2. Data fetched via [API-EIMS-01 : GET /api/eims/v1/employees (Purpose : as above)]; the count is `totalItems` (FR-EIMS-003).
3. DB entity: [EMPLOYEE] – the manager's name from the same table (reports-to relationship).
4. Paging per anchor §6.1: `page` from 1, `size` default 25, maximum 100. Sort: default Employee Id ascending; `sort` on `employeeId`, `name`, `dateOfJoining`, `status`.

**Row and page actions**

1. Admin: "+ Onboard employee" opens SCR-EIMS-02 in create mode (EIMS0020); "Edit" opens SCR-EIMS-02 in edit mode (EIMS0040, EIMS0050); "Reset password" runs EIMS0060 (FR-EIMS-005, 006).
2. Manager: "View" opens SCR-EIMS-04 read only (EIMS0140, FR-EIMS-034).
3. The actions call their own functions' APIs; this function only lists.

###### 3.2.1.5.2 Design notes

1. **One endpoint for both roles (D-131).** Admin and Manager use the same API; the service applies the data scope in the query – Admin: all employees; Manager: `Manager Id = token Employee Id` – so out-of-scope rows are never read (Part01 §9.7). For a manager the response leaves the manager and hourly wage rate fields out (not empty values), so the rate never leaves the service (BR-EIMS-10).
2. **Role mirror (D-131).** The role chip needs each employee's role. The identity provider holds the role and stays the authority for sign-in and the token role claim (BR-EIMS-09, ADR-003); EIMS keeps a copy of the role on EMPLOYEE, written only by EIMS0020 (with UM0010) and EIMS0040 (with UM0050) in the order settled in those chapters (OI-P02-01). The copy is not part of profile approval. The directory, the manager list (VR-EIMS-05, FR-EIMS-014) and the role-change rule (BR-EIMS-06) read the copy and need no identity-provider call. Column in PMS-HLD-Part03-M1-EIMS-Datamodel (planned).
3. **Search and sort.** "Contains" matching over about 100 to 200 rows (BRD §13, Part01 §14.5) needs no special index in the POC; the index plan is in PMS-HLD-Part03-M1-EIMS-Datamodel (planned). Sort by `name` orders by first name, then last name; Employee Id is always the final sort key, so pages are stable.
4. **No caching.** Every call reads the database; nothing is kept in memory between requests (§3.1.1). The list carries no record version: the list is read only, and each action loads its record with its version.
5. **Admin account.** The PMS Administrator is an identity-provider account without an EMPLOYEE record (BR-EIMS-08, FR-UM-004), so no filter is needed to keep it out.

###### 3.2.1.5.3 Sequence & orchestration

```mermaid
sequenceDiagram
  actor U as Admin / Manager
  participant FE as Shell / EIMS package
  participant GW as API gateway
  participant E as EIMS service
  participant DB as eims database
  U->>FE: Open Employees / My Team, search, filter, page
  FE->>GW: GET /api/eims/v1/employees?q&status&includeInactive&page&size&sort (session cookie)
  GW->>GW: Session valid, route allowed for Admin or Manager
  alt Employee role
    GW-->>FE: 403 EIMS-ACC-002
    FE-->>U: No-access page (UM0070)
  else Admin or Manager
    GW->>E: Same request (access token, X-Flow-Ref)
    E->>E: Validate parameters, scope from role and Employee Id
    alt Invalid parameter
      E-->>FE: 400 EIMS-VAL-001
    else Valid
      E->>DB: Select page and count within scope
      DB-->>E: Rows, totalItems
      E-->>FE: 200 items, page, size, totalItems (manager: no rate, no manager)
      FE-->>U: Table, count, or "No employees found"
    end
  end
```

Single-service synchronous function: no cross-service or asynchronous steps.

**Text version of the diagram**

| Step | From → to | Message | Result |
| --- | --- | --- | --- |
| 1 | User → frontend | Open the screen or change search, filter, sort or page | – |
| 2 | Frontend → gateway | GET employees with the query parameters | Session cookie |
| 3 | Gateway | Session and route check | Employee role: 403 EIMS-ACC-002, no-access page |
| 4 | Gateway → EIMS | Same request with access token and flow reference | – |
| 5 | EIMS | Validate parameters; derive scope from role and Employee Id | Invalid: 400 EIMS-VAL-001 |
| 6 | EIMS → database | Select one page and the total count within scope | Rows and count |
| 7 | EIMS → frontend | 200 with items, page, size, totalItems | Fields per role |
| 8 | Frontend → user | Table and count, or the empty state | – |

###### 3.2.1.5.4 Frontend

Only what is not already in the UX summary:

1. One screen component for both menu entries; the role claim from the session chooses the columns and row actions (Admin: Edit, Reset password; Manager: View), never as the only check (Part01 §9.7).
2. Search, filter, "Show inactive", sort and page are kept in the page URL query, so a refresh or the browser's back button returns to the same list; any change except paging resets to page 1.
3. The search request is sent on Enter or when typing pauses; an earlier response that arrives late is ignored.
4. States per UX summary §7: table skeleton while loading; empty state with the BRD message; system error panel with Retry and "Reference: <flow reference>" (anchor §6.5).

###### 3.2.1.5.5 Backend

| API id | API name | Method & endpoint | Purpose | Request (key fields) | Response (key fields) | Roles |
| --- | --- | --- | --- | --- | --- | --- |
| API-EIMS-01 | List employees | GET /api/eims/v1/employees | Employees in the caller's data scope, with search, filter, sort and paging | Query: `q`, `status`, `includeInactive`, `page`, `size`, `sort` | `items[]`: employeeId, firstName, middleName, lastName, role, email, dateOfJoining, status, isActive; Admin only: managerId, managerName, hourlyWageRate; plus `page`, `size`, `totalItems` | Admin (all), Manager (direct reports) |

1. Server-side validation: `page` ≥ 1, `size` 1 to 100, `sort` and `status` from the listed values; anything else is refused with EIMS-VAL-001.
2. Read only: one read transaction for the page and the count; no audit entry, no events.
3. Idempotent and safe; reads may be retried (anchor §6.1).

###### 3.2.1.5.6 Database

| Entity | Operation (C / R / U / soft-D) | Purpose in this function |
| --- | --- | --- |
| EMPLOYEE | R | Rows and count within the data scope; manager name through the reports-to relationship; `is_active` for "Show inactive"; role copy for the role chip |

No in-memory copy of other services' data (OI-P03-03 not affected).

###### 3.2.1.5.7 Validation & error handling

| Rule ref (BRD VR / BR) | Layer (UI / API / DB) | Error code | HTTP status | Message |
| --- | --- | --- | --- | --- |
| Anchor §6.1 paging and sort | API | EIMS-VAL-001 | 400 | Generic validation message (not reachable from the screen controls) |
| BRD §4.2 – Employee has no access | Gateway / API | EIMS-ACC-002 | 403 | "You don't have access to this page." (FR-UM-015) |
| – (no match) | UI | – | 200 (empty list) | "No employees found – Try a different search or filter." (FR-EIMS-003) |
| – | API | EIMS-SYS-001 | 500 | Generic message with "Reference: <flow reference>" |

###### 3.2.1.5.8 Security & data privacy

| Item | Detail |
| --- | --- |
| Authorization check per API | API-EIMS-01: gateway route for Admin and Manager; service checks the role claim and applies the scope in the query (Admin all; Manager by own Employee Id) |
| Sensitive fields | Email (sensitive personal, D-71); hourly wage rate (sensitive pay) |
| Masking (UI / API response) | Within scope shown unmasked (Part03 anchor §6); for a manager the rate and manager fields are not returned |
| Encryption (in transit / at rest / field-level) | TLS at the edge; encrypted storage; no field-level encryption (Part03 anchor §6) |
| Logging rule | Activity log holds caller, role, filters used (whether a search was given, never its text), page, count and result; never `q`, names, emails or rates (Part01 §10.8, NFR-EIMS-01) |
| Threat review – TB-1 browser → gateway | S: session theft – HttpOnly cookie, idle timeout (ADR-004, Part01 §9.6). I: data in transit – TLS and HSTS. D: repeated searches – gateway rate limit per user (Part01 §9.8) |
| Threat review – TB-2 gateway → EIMS | E: Employee calling the route – gateway route per role and service role check (EIMS-ACC-002). E / I: manager reading other teams or rates – scope in the query and role-shaped response (Part01 §9.7). T: injected filter values – contract validation and parameterised queries (Part01 §16.2 A03) |
| Threat review – TB-5 EIMS → database | I: data at rest – encrypted storage and backups (Part03 anchor §6). No writes, so no tampering or repudiation threat |

###### 3.2.1.5.9 Notifications, audit & activity log

| Trigger | Notification (NOT id) | Activity log entry | Audit fields captured |
| --- | --- | --- | --- |
| List requested | None (C-05) | `process` API-EIMS-01; steps `validated`, `scope-applied`, `listed` (count); exit with result and duration | None – read only |
| Refused (Employee role) | None | Event type `refused` with the reason and user (FR-ADM-117) | None |

###### 3.2.1.5.10 Scenarios

| Scenario id | Scenario | Type | Requirement ref | Pre-condition | Expected result | Test level |
| --- | --- | --- | --- | --- | --- | --- |
| EIMS0010-S01 | Admin lists employees | Positive | FR-EIMS-001 | 30 active, 2 inactive employees | 30 rows over 2 pages of 25, all Admin columns, totalItems 30, no Admin account row | API, E2E |
| EIMS0010-S02 | Manager lists the team | Positive | FR-EIMS-002, BR-EIMS-10 | Manager M1 with 3 direct reports | Only the 3 reports; no `hourlyWageRate` or `managerId` in the response | API |
| EIMS0010-S03 | Search by Employee Id | Positive | FR-EIMS-003 | EMP0007 exists | `q=EMP0007` returns 1 row, totalItems 1 | API |
| EIMS0010-S04 | Search by part of an email, any case | Positive | FR-EIMS-003 | Email `asha.k@…` | `q=ASHA` finds the row | API |
| EIMS0010-S05 | No match | Edge | FR-EIMS-003 | – | 200 with empty items; empty-state message shown | API, E2E |
| EIMS0010-S06 | Inactive hidden, then shown | Positive | FR-EIMS-004, BR-CMN-06 | One inactive employee | Not listed by default; listed with `isActive` false and the badge when `includeInactive=true` | API, E2E |
| EIMS0010-S07 | Status filter | Positive | FR-EIMS-003 | Mixed statuses | `status=SUBMITTED` returns only Submitted profiles | API |
| EIMS0010-S08 | Employee calls the API | Negative | BRD §4.2, FR-UM-015 | Employee session | 403 EIMS-ACC-002; no-access page; refused entry in the activity log | API, E2E |
| EIMS0010-S09 | Manager after a manager change | Edge | FR-EIMS-017, XF-08 | B moved from M1 to M2 | B listed for M2 at once, no longer for M1 | API |
| EIMS0010-S10 | Invalid paging or sort | Negative | Anchor §6.1 | – | `size=500` or `sort=hourlyWageRate,asc` → 400 EIMS-VAL-001 | API |
| EIMS0010-S11 | Search text not logged | Negative | NFR-EIMS-01 | Search by an email | Activity log shows that a search was applied, not the text | API (log review) |
| EIMS0010-S12 | Response time | Performance | NFR-01, PT-08 | 200 employees (Part01 §14.5) | p95 ≤ 500 ms at the service at 2× load | Performance |

##### 3.2.1.6 Notes, issues & assumptions

1. Note: the role copy (design note 2) is written only by EIMS0020 and EIMS0040; how it stays in step with the identity provider when one of the two steps fails is designed with those functions (OI-P02-01).
2. Note: the Admin dashboard's "Recently onboarded employees" (RPT-EIMS-05) is supplied by EIMS0200, not by this API.

Further function chapters are added review by review (R3 to R9).

## 4. NFR summary & inventories

Drafted with R10.

## 5. Appendix

Drafted with R10.
