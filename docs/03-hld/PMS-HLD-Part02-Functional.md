# PMS – HLD Part02: Functional Design (Anchor)

Document ID: PMS-HLD-Part02-Functional-v1.0
Scope: functional design anchor – module index, function index, cross-module flows, common design conventions and roll-up inventories; per-function designs are in the module documents
Project: Payroll Management System (PMS) – proof of concept (POC), Stage 3 Solution Design
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 23-Nov-2026 | Rajesh Verma | First draft of §1–§3, based on the approved BRD set v1.0 (D-107), UX v1.1 (D-105), PMS-HLD-Part01 v1.0 rev 0.9 and PMS-HLD-Part01a v1.0 rev 0.5; Part02 anchor design answers of 23 Nov 2026 (D-122) |
| 1.0 | 0.2 | 23-Nov-2026 | Rajesh Verma | Draft of §4 (function index, 77 functions) and §5 (cross-module flows XF-01 to XF-09); open items OI-P02-01 and 02 (D-123) |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3 approved (D-122); §4–§5 approved (D-123) |
| Product owner | Rajesh Verma | 23-Nov-2026 | §1–§3 approved (D-122); §4–§5 approved (D-123) |
| Business analyst | | | |
| Dev lead | | | |

## 2. Introduction

This document is the anchor of the PMS functional design: it indexes the module design documents, designs the flows that cross modules, and sets the design conventions every module follows. Per-function designs are only in the module documents (PMS-HLD-Part02-M1-EIMS to M4-SMS and M5-SUP); this anchor never repeats them (D-48). Roll-ups that depend on a module document not yet written show "Module document (planned)" and are completed as each module document is written.

Reading rules:

- Function ids are `<MOD>0010`, `<MOD>0020` … in steps of 10 per module; supporting functions use UM, AUTH and ADM (NM and DM are Phase 2, D-57). One function is one user action on a screen or one system process.
- API references use `[API-<MOD>-nn : METHOD /ctx/resource (Purpose : ...)]`; the API inventory (§7.1) is a roll-up keyed by API id.
- Business statuses and their transitions stay in the module BRDs §6; this document holds only their technical handling.
- The design is technology-neutral (Part01 §2): identity provider, broker, gateway and edge are named by role, not by product.
- Conventions that a standard will detail refer to `docs/04-standards/<area> (planned)`, with the area names of Part01a §2.

### 2.1 Reference documents

| # | Document | Purpose |
| --- | --- | --- |
| 1 | PMS-BRD (anchor), PMS-BRD-M1-EIMS, M2-AMS, M3-LMS, M4-SMS, PMS-BRD-M5-SUP – v1.0, approved baseline (D-107) | Requirements: roles and data scope (anchor §4), end-to-end process, 30 journeys and shared screens (§5), cross-module rules BR-CMN (§6), integrations INT-01 to INT-10 and JOB-CMN-01 (§7), NFR-01 to NFR-09 (§8); module functional requirements, statuses and NFRs |
| 2 | UX Journey Index v1.1 and 17 UX Summaries v1.1 (D-105); shared mockup assets `docs/01-ux/mockups/html/assets/` | Experience design, navigation map, screen states, approved visual style (D-27) |
| 3 | PMS-HLD-Part01-Architecture-and-Design v1.0 rev 0.9 | Functional, integration, security and observability architecture (§5, §8, §9, §10), NFR realization (§16.3) |
| 4 | PMS-HLD-Part01a-Principles-Patterns-Decisions v1.0 rev 0.5 | Principles and patterns catalogue; ADR register ADR-001 to ADR-006; open items OI-P01a-01 to 17 |
| 5 | PMS-HLD-Part03-Datamodel (anchor) and module data-model documents (planned) | Data model; columns defined only in the module data-model documents |
| 6 | API and event contracts (`contracts/openapi`, `contracts/events`) | OpenAPI 3 contracts and versioned event schemas, written before implementation (D-16, D-18) |
| 7 | Decision log `docs/decisions/decision-log.md` | Approved project decisions D-01 onwards |

### 2.2 Module design documents

| Module | Document | Owning service | Version | Status |
| --- | --- | --- | --- | --- |
| EIMS | PMS-HLD-Part02-M1-EIMS-Functional | EIMS service (/eims) | – | Not started |
| AMS | PMS-HLD-Part02-M2-AMS-Functional | AMS service (/ams) | – | Not started |
| LMS | PMS-HLD-Part02-M3-LMS-Functional | LMS service (/lms) | – | Not started |
| SMS | PMS-HLD-Part02-M4-SMS-Functional | SMS service (/sms), incl. JOB-CMN-01 | – | Not started |
| SUP (UM, AUTH, ADM) | PMS-HLD-Part02-M5-SUP-Functional | Identity provider, API gateway, shell; audit and activity log in every service | – | Not started |

The shell (layout, menu, dashboard, approvals inbox) has no module document of its own: its composition is designed in this anchor (§5 XF-05, §6.5), and each module document designs the tiles, to-do items and inbox items its module supplies (BRD §5.3).

## 3. Functional landscape

### 3.1 Module overview

| Module | Purpose | Primary users (roles) | Key entities owned | Depends on (modules) | Used by (modules) |
| --- | --- | --- | --- | --- | --- |
| Shell (common UI) | One layout and role-based menu for every screen; dashboard per role and approvals inbox across modules (BRD §5.3, FR-CMN-001 to 016) | Employee, Manager, Admin | None (composes module data) | EIMS, AMS, LMS, SMS (INT-07); AUTH (session) | – |
| EIMS – Employee information | Onboarding with Employee Id and temporary password, profile and profile change request with approval, Admin-owned fields, deactivation, password reset, directory | Admin, Employee, Manager; system (SYS-EIMS) | Employee, profile change request | UM / identity provider (INT-08); AMS, LMS (INT-09) | Shell, AMS, LMS, SMS (INT-03, INT-04, INT-05) |
| AMS – Attendance | Daily attendance entry, submit, discard, approve / reject, reopen after a salary dispute; hand-over to SMS | Employee, Manager, Admin (top-level employee only) | Attendance; outbox entries | EIMS (INT-03, INT-04, INT-09 as provider); LMS (INT-06); SMS (INT-10) | Shell (INT-07); SMS (INT-01, INT-02 events; JOB-CMN-01 query); LMS (INT-06); EIMS (INT-09) |
| LMS – Leave | Full-day leave request, cancel while Submitted, approve / reject | Employee, Manager, Admin (top-level employee only) | Leave request | EIMS (INT-03, INT-04); AMS (INT-06) | Shell (INT-07); AMS (INT-06); EIMS (INT-09) |
| SMS – Salary | Salary record generation and voiding from attendance events, manager approval, accept / dispute, keep as is, earnings, nightly reconciliation | Employee, Manager, Admin (top-level employee only); system (SYS-SMS, SYS-REC) | Salary record, reconciliation run; processed-event record | AMS (INT-01, INT-02, JOB-CMN-01); EIMS (INT-03, INT-04, INT-05) | Shell (INT-07); AMS (INT-10) |
| SUP – UM | User accounts and roles held in the identity provider; role and data-scope checks (FR-UM-001 to 015) | Admin (through EIMS screens); every request | User account (in the identity provider) | Identity provider | EIMS (INT-08); every module (role and scope rules) |
| SUP – AUTH | Sign-in, set and change password, lockout, idle timeout, log out, security events (FR-AUTH-001 to 030) | All roles | Session (gateway), credentials (identity provider) | Identity provider, API gateway | Shell; every module (authenticated requests) |
| SUP – ADM (POC part) | Audit log and activity log with one flow reference per user action or job run (FR-ADM-101 to 117) | IT operations (no screen in the POC) | Audit log entry (per module database), activity log entry (log platform) | Log and monitoring platform | Every module, job and event |

### 3.2 Module dependency map

```mermaid
flowchart LR
  SH["Shell"]
  EIMS["EIMS"]
  AMS["AMS"]
  LMS["LMS"]
  SMS["SMS"]
  IDP(["Identity provider<br/>(UM, AUTH)"])
  SH -- "API: INT-07" --> EIMS & AMS & LMS & SMS
  AMS & LMS & SMS -- "API: INT-03, INT-04" --> EIMS
  SMS -- "API: INT-05" --> EIMS
  EIMS -- "API: INT-09" --> AMS & LMS
  AMS <-- "API: INT-06" --> LMS
  AMS -- "Event: INT-01, INT-02" --> SMS
  SMS -- "Job: JOB-CMN-01" --> AMS
  AMS -- "API: INT-10" --> SMS
  EIMS -- "API: INT-08" --> IDP
  SH -- "Session" --> IDP
```

**Text version of the diagram**

| From module | To module | Dependency (API / event / job) | Purpose | Flow (§5) |
| --- | --- | --- | --- | --- |
| Shell | EIMS, AMS, LMS, SMS | API (INT-07), one call per module card | Dashboard tiles, to-do items, missing days, approvals inbox items and counts | XF-05 |
| AMS, LMS, SMS, shell | EIMS | API (INT-03) | Employee details: name, Employee Id, date of joining, Manager Id, profile status, active flag | XF-02, XF-05, XF-08 |
| AMS, LMS, SMS, shell | EIMS | API (INT-04) | Approver resolution: owner's manager, or the Admin for the top-level employee; no self-approval | XF-02, XF-05, XF-08 |
| SMS | EIMS | API (INT-05) | Current hourly wage rate, copied into the salary record at generation | XF-02, XF-04 |
| EIMS | AMS, LMS | API (INT-09) | Records before a new date of joining | XF-07 |
| AMS | LMS | API (INT-06) | Leave on the attendance date (save and submit) | XF-06 |
| LMS | AMS | API (INT-06) | Attendance on the leave dates (submit) | XF-06 |
| AMS | SMS | Event (INT-01) | Attendance approved → salary record generated | XF-02 |
| AMS | SMS | Event (INT-02) | Attendance reopened → salary record voided | XF-03 |
| SMS | AMS | Job (JOB-CMN-01), paged API | Approved attendance for the nightly reconciliation | XF-04 |
| AMS | SMS | API (INT-10) | Salary status of approved attendance: "Salary disputed" marker in team history and server-side check before a reopen | XF-03 |
| EIMS | Identity provider (UM) | API (INT-08) | Create account, set role, reset password, disable, end sessions | XF-01, XF-09 |
| Shell (through the gateway) | Identity provider (AUTH) | Sign-in, refresh, log out (Part01 §8.2 row 13) | Session for every request | XF-01, XF-09 |

## 4. System function index (all modules)

One function is one user action on a screen or one system process (D-122); ids `<MOD>0010` in steps of 10; SH for the shell, designed in this anchor because the shell has no module document; UM, AUTH and ADM for SUP (ADM only for the POC part FR-ADM-101 to 117, D-101). The references in brackets show the main requirement source; the full mapping is in §9. Design status "Not started" becomes Draft when the module document is drafted.

| Function id | System function | Module | Type (screen / API / backend job / configuration) | UX screen | Delivery phase | Design status | Document section |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SH0010 | Show shell layout, role-based menu and user menu (FR-CMN-015, FR-UM-012, FR-AUTH-024) | Shell | Screen | SCR-SH-00 | POC | Draft | This anchor §6.5 |
| SH0020 | Show the dashboard per role, one card per module (FR-CMN-001 to 008) | Shell | Screen | SCR-SH-03 | POC | Draft | This anchor §5.5 (XF-05), §6.5 |
| SH0030 | Show the approvals inbox across modules, tabs and counts (FR-CMN-010, 013) | Shell | Screen | SCR-SH-04 | POC | Draft | This anchor §5.5 (XF-05), §6.5 |
| SH0040 | Decide inbox items – approve one or several, reject one, keep as is or reopen – through the owning module functions (FR-CMN-011, 012, 014) | Shell | Screen | SCR-SH-04 | POC | Draft | This anchor §5.5 (XF-05), §6.1 |
| EIMS0010 | View the employee directory – search, filter, show inactive; Admin all, manager direct reports (FR-EIMS-001 to 004, 006) | EIMS | Screen | SCR-EIMS-01 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0020 | Onboard an employee – create the employee and the user account (FR-EIMS-010, 011, 014; INT-08) | EIMS | Screen | SCR-EIMS-02 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0030 | Generate Employee Id and temporary password (FR-EIMS-040, 041; UJ-SYS-04) | EIMS | Backend process | – | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0040 | Edit Admin-owned fields – date of joining, role, manager, hourly wage rate (FR-EIMS-012 to 017; INT-08, INT-09) | EIMS | Screen | SCR-EIMS-02 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0050 | Deactivate an employee (FR-EIMS-018; INT-08) | EIMS | Screen | SCR-EIMS-02 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0060 | Reset an employee's password (FR-EIMS-005; INT-08) | EIMS | Screen | SCR-EIMS-01 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0070 | View my profile and its status (FR-EIMS-020) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0080 | Save a profile draft (FR-EIMS-021) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0090 | Submit or resubmit my profile (FR-EIMS-022, 024) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0100 | Withdraw my submitted profile (FR-EIMS-023) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0110 | Start and save a profile change request (FR-EIMS-025, 026) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0120 | Submit or resubmit a profile change request (FR-EIMS-026, 027) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0130 | Withdraw a profile change request (FR-EIMS-027) | EIMS | Screen | SCR-EIMS-03 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0140 | Open a profile or change request for review, or read only from the directory (FR-EIMS-030 to 032, 034, 035) | EIMS | Screen | SCR-EIMS-04 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0150 | Approve profiles or change requests, one or several; apply approved changes (FR-EIMS-033, 028) | EIMS | Screen | SCR-EIMS-04, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0160 | Reject a profile or change request with remarks (FR-EIMS-033) | EIMS | Screen | SCR-EIMS-04, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0170 | Provide employee details to other modules (INT-03) | EIMS | API | – | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0180 | Resolve the approver of a record (INT-04) | EIMS | API | – | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0190 | Provide the current hourly wage rate (INT-05) | EIMS | API | – | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| EIMS0200 | Supply EIMS dashboard tiles, to-do items and inbox items (INT-07) | EIMS | API | SCR-SH-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M1-EIMS (planned) |
| AMS0010 | View my attendance – month calendar or list, tiles, missing weekdays, leave days (FR-AMS-001 to 008) | AMS | Screen | SCR-AMS-01 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0020 | Save an attendance draft (FR-AMS-010, 011, 014, 015; INT-06) | AMS | Screen | SCR-AMS-02 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0030 | Submit or resubmit attendance (FR-AMS-012 to 014, 016; INT-04, INT-06) | AMS | Screen | SCR-AMS-02 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0040 | Discard a Draft or Rejected entry (FR-AMS-017) | AMS | Screen | SCR-AMS-01, SCR-AMS-02 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0050 | View team attendance – pending and history, "Salary disputed" marker (FR-AMS-020, 021, 024, 026, 027; INT-10) | AMS | Screen | SCR-AMS-03 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0060 | Approve attendance, one or several, and record the hand-over event (FR-AMS-022, 030; INT-01) | AMS | Screen | SCR-AMS-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0070 | Reject attendance with remarks (FR-AMS-023) | AMS | Screen | SCR-AMS-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0080 | Reopen approved attendance after a salary dispute (FR-AMS-025, 031; INT-10, INT-02) | AMS | Screen | SCR-AMS-03, SCR-SMS-02, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0090 | Publish attendance events from the outbox (INT-01, INT-02) | AMS | Backend process | – | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0100 | Provide approved attendance for the nightly reconciliation (FR-AMS-032; JOB-CMN-01) | AMS | API | – | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0110 | Check attendance on leave dates for LMS (INT-06) | AMS | API | – | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0120 | Check attendance before a new date of joining (INT-09) | AMS | API | – | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| AMS0130 | Supply AMS dashboard tiles, to-do items, missing days and inbox items (INT-07) | AMS | API | SCR-SH-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M2-AMS (planned) |
| LMS0010 | View my leave – tiles, list, filters, team tab entry (FR-LMS-001 to 003, 006 to 009) | LMS | Screen | SCR-LMS-01 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0020 | Submit or resubmit a leave request (FR-LMS-010 to 016; INT-04, INT-06) | LMS | Screen | SCR-LMS-02 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0030 | Cancel a submitted leave request (FR-LMS-004, 005) | LMS | Screen | SCR-LMS-01 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0040 | View team leave – pending with "Also away", history (FR-LMS-020 to 022, 026 to 028) | LMS | Screen | SCR-LMS-03 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0050 | Approve leave, one or several (FR-LMS-023, 025) | LMS | Screen | SCR-LMS-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0060 | Reject leave with remarks (FR-LMS-024) | LMS | Screen | SCR-LMS-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0070 | Check leave on an attendance date for AMS (INT-06) | LMS | API | – | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0080 | Check leave before a new date of joining (INT-09) | LMS | API | – | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| LMS0090 | Supply LMS dashboard tiles, to-do items and inbox items (INT-07) | LMS | API | SCR-SH-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M3-LMS (planned) |
| SMS0010 | View my salary – period, tiles, records, voided toggle, total (FR-SMS-001 to 006, 012 to 014) | SMS | Screen | SCR-SMS-01 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0020 | Accept salary records, one or several (FR-SMS-007, 008, 011) | SMS | Screen | SCR-SMS-01 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0030 | Dispute a salary record with a remark (FR-SMS-009 to 011) | SMS | Screen | SCR-SMS-01 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0040 | View team salary – needs action, all records, team totals (FR-SMS-020, 021, 023, 027 to 029) | SMS | Screen | SCR-SMS-02 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0050 | Approve generated salary records, one or several (FR-SMS-022, 024) | SMS | Screen | SCR-SMS-02, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0060 | Close a dispute with Keep as is (FR-SMS-025) | SMS | Screen | SCR-SMS-02, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0070 | Start a reopen from a disputed salary record – dialog calling AMS0080 (FR-SMS-026) | SMS | Screen | SCR-SMS-02, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0080 | Generate a salary record on attendance approved (FR-SMS-040, 041; INT-01, INT-05) | SMS | Backend process (event) | – | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0090 | Void the salary record on attendance reopened (FR-SMS-042; INT-02) | SMS | Backend process (event) | – | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0100 | Nightly salary reconciliation (FR-SMS-043 to 045; JOB-CMN-01) | SMS | Backend job | – | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0110 | Provide salary status for approved attendance (FR-SMS-046; INT-10) | SMS | API | – | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| SMS0120 | Supply SMS dashboard tiles, to-do items, inbox items and last reconciliation run (INT-07) | SMS | API | SCR-SH-03, SCR-SH-04 | POC | Not started | PMS-HLD-Part02-M4-SMS (planned) |
| UM0010 | Create the user account at onboarding (FR-UM-001, 002; INT-08) | SUP (UM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| UM0020 | Set up the PMS Administrator account at installation (FR-UM-004, 005) | SUP (UM) | Configuration | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| UM0030 | Replace the password with a temporary one, clear the lock and end sessions (FR-UM-006) | SUP (UM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| UM0040 | Disable the account and end sessions on deactivation (FR-UM-003, 007) | SUP (UM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| UM0050 | Change the role and end sessions (FR-UM-010, 011) | SUP (UM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| UM0060 | Check role and data scope on every request (FR-UM-013, 014) | SUP (UM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| UM0070 | Return the neutral no-access response and page (FR-UM-015) | SUP (UM) | Screen | SCR-SH-00 | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| AUTH0010 | Sign in (FR-AUTH-001 to 008, 014) | SUP (AUTH) | Screen | SCR-SH-01 | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| AUTH0020 | Set password at first sign-in or after a reset (FR-AUTH-006, 010, 012, 013, 015) | SUP (AUTH) | Screen | SCR-SH-02 | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| AUTH0030 | Change my password (FR-AUTH-011, 012, 015, 022) | SUP (AUTH) | Screen | SCR-SH-02 | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| AUTH0040 | End the session after 30 minutes idle or at the absolute limit (FR-AUTH-020, 021; FR-CMN-016) | SUP (AUTH) | Backend process | SCR-SH-01 | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| AUTH0050 | Log out (FR-AUTH-023) | SUP (AUTH) | Screen | SCR-SH-00 | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| AUTH0060 | Record security events (FR-AUTH-030) | SUP (AUTH) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| ADM0010 | Write audit log entries for every data change (FR-ADM-101 to 104) | SUP (ADM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| ADM0020 | Extract a record's audit history on request (FR-ADM-105) | SUP (ADM) | Configuration (operations procedure) | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| ADM0030 | Write activity log entries for operations, jobs and events (FR-ADM-111, 112, 115, 116) | SUP (ADM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| ADM0040 | Create and carry the flow reference (FR-ADM-113) | SUP (ADM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| ADM0050 | Show "Reference: <flow reference>" in system error messages (FR-ADM-114) | SUP (ADM) | Screen | SCR-SH-00 and every screen | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |
| ADM0060 | Log refused requests (FR-ADM-117) | SUP (ADM) | Backend process | – | POC | Not started | PMS-HLD-Part02-M5-SUP (planned) |

Totals: 77 functions – Shell 4, EIMS 20, AMS 13, LMS 9, SMS 12, SUP (UM) 7, SUP (AUTH) 6, SUP (ADM) 6.

## 5. Cross-module flows

One subsection per business flow that spans two or more modules (D-122). The step table under each diagram is its text version. Business statuses are those of the module BRDs §6; this section holds only the technical hand-over. Every user action and job run carries one flow reference through all steps (Part01 §10.5); every command carries the record version (FR-CMN-014, §6.1).

| Flow | Name | Integrations | Modules |
| --- | --- | --- | --- |
| XF-01 | Onboarding and account creation | INT-08 | EIMS, SUP (UM, AUTH), shell |
| XF-02 | Attendance approval → salary generation | INT-01, INT-04, INT-05 | AMS, SMS, EIMS, shell |
| XF-03 | Salary dispute → reopen attendance → void salary record | INT-02, INT-10 | SMS, AMS, shell |
| XF-04 | Nightly salary reconciliation | JOB-CMN-01, INT-05 | SMS, AMS, EIMS |
| XF-05 | Dashboard and approvals inbox composition | INT-07, INT-03, INT-04, INT-06 | Shell, EIMS, AMS, LMS, SMS |
| XF-06 | Attendance and leave date check | INT-06 | AMS, LMS |
| XF-07 | Date-of-joining change check | INT-09 | EIMS, AMS, LMS |
| XF-08 | Manager change moving waiting items | INT-04 | EIMS, AMS, LMS, SMS, shell |
| XF-09 | Account changes ending sessions – deactivation, password reset, role change | INT-08 | EIMS, SUP (UM, AUTH), gateway |

### 5.1 XF-01 – Onboarding and account creation

| Item | Detail |
| --- | --- |
| Business purpose | A new employee gets an employee record and a user account in one Admin action, and can sign in and complete the profile |
| Trigger | Admin saves the onboarding form (SCR-EIMS-02) |
| Modules involved | EIMS, SUP (UM through the identity provider, AUTH), shell |
| Requirement refs | FR-EIMS-010, 011, 014, 040, 041; FR-UM-001, 002; FR-AUTH-006, 010, 013; INT-08; BRD §5.1 steps 1–2; UJ-EIMS-01, UJ-SYS-04, UJ-SH-01, UJ-SH-02; D-104 (OI-EIMS-01) |
| Pre-conditions / post-conditions | Pre: Admin signed in; manager chosen or "None – top-level" (only one top-level employee). Post: employee Draft; account enabled with the Employee Id as user name, the chosen role and a temporary password that must be replaced at first sign-in; temporary password shown once to the Admin |

```mermaid
sequenceDiagram
  actor A as Admin
  participant SH as Shell / EIMS screens
  participant GW as API gateway
  participant E as EIMS
  participant IDP as Identity provider
  actor U as Employee
  A->>SH: Save onboarding form
  SH->>GW: Create employee (session cookie)
  GW->>E: Create employee (access token, flow reference)
  E->>E: Validate, generate Employee Id and temporary password
  E->>IDP: Create account (Employee Id, role, temporary password)
  IDP-->>E: Account created
  E->>E: Commit employee as Draft, audit entries
  E-->>A: Employee Id and temporary password (shown once)
  A-->>U: Temporary password by company email (outside PMS)
  U->>GW: Sign in with temporary password
  GW->>IDP: Authorization code flow
  IDP-->>U: Set password, then dashboard with "complete your profile" banner
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | EIMS | EIMS0020 | Sync API through the gateway | Create employee – Module document (planned) | Validation only (FR-EIMS-011, 014) |
| 2 | EIMS | EIMS0030 | Internal | – | Employee Id sequence, never reused (FR-EIMS-040) |
| 3 | SUP (UM) | UM0010 | Sync API to the identity provider (INT-08), service account | Identity provider admin API | Keyed by Employee Id (Part01 §8.5) |
| 4 | EIMS | EIMS0020 | Internal | – | Local transaction: employee Draft and audit entries (ADM0010) |
| 5 | – | – | Manual hand-over by company email (D-104) | – | – |
| 6 | SUP (AUTH) | AUTH0010, AUTH0020 | Sign-in through the gateway (Part01 §8.2 row 13) | OIDC | Identity provider |
| 7 | Shell, EIMS | SH0020, EIMS0200 | Sync API (INT-07) | Dashboard card – Module document (planned) | Read only |

**Failure handling & compensation:** If the account cannot be created, the onboarding is refused with "Reference: <flow reference>" and no employee is saved. The exact order of steps 3 and 4, retry of a half-done onboarding by the same Employee Id and any gap in the Employee Id sequence are designed in PMS-HLD-Part02-M5-SUP, as Part01 §8.2 row 9 requires (OI-P02-01).

**Reconciliation:** None automatic in the POC. A mismatch between employees and accounts is found by IT operations from the activity log (refused or failed onboarding with its flow reference).

### 5.2 XF-02 – Attendance approval → salary generation

| Item | Detail |
| --- | --- |
| Business purpose | Every approved attendance gets exactly one salary record within 1 minute, at the current hourly wage rate |
| Trigger | Approver approves one or several attendance entries (SCR-AMS-03 or approvals inbox) |
| Modules involved | AMS, SMS, EIMS, shell |
| Requirement refs | FR-AMS-022, 030; FR-SMS-040, 041; FR-CMN-011, 014; BR-CMN-08, 12, 13; INT-01, INT-04, INT-05; NFR-01, NFR-06; UJ-AMS-03, UJ-SYS-01; ADR-006 |
| Pre-conditions / post-conditions | Pre: attendance Submitted; approver is the owner's manager (Admin for the top-level employee), never the owner. Post: attendance Approved and locked; salary record Generated with hours, copied rate and amount |

```mermaid
sequenceDiagram
  actor M as Approver
  participant GW as API gateway
  participant A as AMS
  participant E as EIMS
  participant B as Broker topic / SMS subscription
  participant S as SMS
  M->>GW: Approve selected attendance (ids, versions)
  GW->>A: Approve (access token, flow reference)
  A->>E: Resolve approver (INT-04)
  E-->>A: Approver
  A->>A: Per item: Approved, version + 1, audit, outbox row (one transaction)
  A-->>M: Result per item
  A->>B: Outbox relay publishes attendance-approved
  B->>S: Deliver (durable subscription)
  S->>S: Event id new? attendance version above last applied?
  S->>E: Current hourly wage rate (INT-05, service token)
  E-->>S: Rate
  S->>S: Salary record Generated, processed event and version stored (one transaction)
  S-->>B: Acknowledge
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | AMS | AMS0060 | Sync API through the gateway | Approve attendance – Module document (planned) | Version check per item (§6.1) |
| 2 | EIMS | EIMS0180 | Sync API (INT-04), user token relayed | Resolve approver – Module document (planned) | Read only |
| 3 | AMS | AMS0060 | Internal | – | Local transaction per item: status, version, audit, outbox row |
| 4 | AMS | AMS0090 | Event publish | attendance-approved (INT-01, §7.2) | Transactional outbox |
| 5 | SMS | SMS0080 | Event consume | attendance-approved | Idempotent consumer: event id and attendance version (§6.2) |
| 6 | EIMS | EIMS0190 | Sync API (INT-05), service token | Hourly wage rate – Module document (planned) | Read only; event not acknowledged until read |
| 7 | SMS | SMS0080 | Internal | – | Local transaction: salary record, processed-event record, audit |

**Failure handling & compensation:** In a bulk approval, failed items stay selected with their own error, the others are approved (FR-CMN-014). If the broker is down, outbox rows stay unsent and the relay retries until confirmed. If SMS or EIMS (rate) is unavailable, the event is not acknowledged and is redelivered with backoff; after 5 attempts it goes to the dead-letter queue and IT operations are alerted (§6.2). A duplicate or older event is ignored. No compensation of the approval is needed: the hand-over is eventually consistent.

**Reconciliation:** XF-04 creates any salary record still missing the next night.

### 5.3 XF-03 – Salary dispute → reopen attendance → void salary record

| Item | Detail |
| --- | --- |
| Business purpose | A disputed wage ends either confirmed (Keep as is) or corrected through the attendance, with no voided amount counted anywhere |
| Trigger | Employee disputes a Manager Approved salary record; the approver chooses Keep as is or Reopen attendance (SCR-SMS-02, approvals inbox, or team attendance history) |
| Modules involved | SMS, AMS, shell |
| Requirement refs | FR-SMS-009, 010, 025, 026, 042, 046; FR-AMS-024, 025, 031; FR-CMN-012; BR-CMN-03, 15, 16; INT-02, INT-10; UJ-SMS-02, UJ-SMS-03, UJ-AMS-04, UJ-SYS-03; D-33 |
| Pre-conditions / post-conditions | Pre: salary record Manager Approved. Post: Keep as is – record Manager Approved again with the explanation; Reopen – attendance Rejected (back to the employee), salary record Voided with the reopen remarks and date; a new salary record follows when the attendance is approved again (XF-02) |

```mermaid
sequenceDiagram
  actor U as Employee
  actor M as Approver
  participant GW as API gateway
  participant S as SMS
  participant A as AMS
  participant B as Broker topic / SMS subscription
  U->>GW: Dispute salary record (remark, version)
  GW->>S: Dispute
  S->>S: Disputed, audit (one transaction)
  M->>GW: Team attendance history
  GW->>A: Team history
  A->>S: Salary status of approved attendance (INT-10)
  S-->>A: Disputed
  A-->>M: Row marked "Salary disputed"
  alt Keep as is
    M->>GW: Keep as is (explanation, version)
    GW->>S: Keep as is
    S->>S: Manager Approved, audit
  else Reopen attendance
    M->>GW: Reopen (remarks, attendance version)
    GW->>A: Reopen
    A->>S: Salary status (INT-10)
    S-->>A: Disputed
    A->>A: Rejected, version + 1, audit, outbox row (one transaction)
    A->>B: Outbox relay publishes attendance-reopened
    B->>S: Deliver
    S->>S: Version above last applied? Void non-voided record, audit
  end
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | SMS | SMS0030 | Sync API through the gateway | Dispute – Module document (planned) | Local transaction, version check |
| 2 | AMS, SMS | AMS0050, SMS0110 | Sync API (INT-10), user token relayed | Salary status – Module document (planned) | Read only; status unknown shown with Retry, Reopen not offered |
| 3a | SMS | SMS0060 | Sync API through the gateway | Keep as is – Module document (planned) | Local transaction, version check |
| 3b | AMS | AMS0080 (from SMS0070 or AMS0050) | Sync API through the gateway | Reopen – Module document (planned) | Version check on the attendance |
| 4 | SMS | SMS0110 | Sync API (INT-10), user token relayed | Salary status | Reopen refused unless the record is Disputed (server-side, D-122) |
| 5 | AMS | AMS0080 | Internal | – | Local transaction: status, version, audit, outbox row |
| 6 | AMS | AMS0090 | Event publish | attendance-reopened (INT-02, §7.2) | Transactional outbox |
| 7 | SMS | SMS0090 | Event consume | attendance-reopened | Idempotent consumer (event id, attendance version); void is idempotent |
| 8 | AMS → SMS | AMS0030 → AMS0060 → SMS0080 | As XF-02 | attendance-approved | As XF-02; a new record because the earlier one is Voided (FR-SMS-041) |

**Failure handling & compensation:** If SMS cannot answer the salary status (step 4), the reopen is refused with a retry message and "Reference: <flow reference>". Between steps 5 and 7 the salary record stays Disputed (normally under 1 minute, NFR-01). An event that keeps failing goes to the dead-letter queue (§6.2). If Keep as is is taken by another approver between steps 4 and 7, the void still applies, because the attendance is no longer Approved (BR-CMN-15). Late or out-of-order approved and reopened events for one attendance are resolved by the version rule (§6.2): an event whose version is lower than or equal to the last applied one is ignored.

**Reconciliation:** XF-04 voids any non-voided salary record whose attendance is no longer Approved.

### 5.4 XF-04 – Nightly salary reconciliation

| Item | Detail |
| --- | --- |
| Business purpose | Every approved attendance has exactly one non-voided salary record each morning (KPI-04) |
| Trigger | Schedule, daily at 01:00 IST (JOB-CMN-01) |
| Modules involved | SMS (job), AMS, EIMS, shell (Admin dashboard) |
| Requirement refs | FR-SMS-043 to 045; FR-AMS-032; FR-CMN-007; FR-ADM-112; JOB-CMN-01, INT-05; NFR-01 (run under 5 minutes), NFR-06; UJ-SYS-02; D-90; ADR-006 |
| Pre-conditions / post-conditions | Pre: no other run holds the job lock. Post: missing records created, stale records voided, other mismatches logged; run logged with counts and shown as the last run on the Admin dashboard |

```mermaid
sequenceDiagram
  participant J as SMS reconciliation job
  participant DB as sms database
  participant A as AMS
  participant E as EIMS
  J->>DB: Take job lock (one instance)
  J->>J: New flow reference, log job start
  loop Each page
    J->>A: Approved attendance (paged, service token)
    A-->>J: Attendance ids, hours, versions
  end
  J->>DB: Compare with salary records
  J->>E: Hourly wage rate for each missing record (INT-05)
  J->>DB: Create missing (Generated), void stale, one transaction per record
  J->>DB: Log mismatches and run result, release lock
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | SMS | SMS0100 | Job, database lock (Part01 §8.3) | – | One run at a time |
| 2 | AMS | AMS0100 | Sync paged API, service token | Approved attendance for reconciliation – Module document (planned) | Read only |
| 3 | EIMS | EIMS0190 | Sync API (INT-05), service token | Hourly wage rate | Read only |
| 4 | SMS | SMS0100 | Internal | – | Local transaction per created or voided record; attendance version stored as for events (§6.2) |
| 5 | SMS | SMS0100, SMS0120 | Internal; Admin dashboard card (INT-07) | Dashboard card | Run record (start, end, result, counts) |

**Failure handling & compensation:** If AMS or EIMS cannot be reached, the job retries the run; a run that still fails is logged as failed with its flow reference, IT operations are alerted, and the Admin dashboard shows the failed last run; the next night repairs. Each record is created or voided in its own transaction, so a run that stops half-way leaves no partial record and can simply be repeated. Other mismatches (FR-SMS-044) are logged, never changed.

**Reconciliation:** This flow is the reconciliation for XF-02 and XF-03.

### 5.5 XF-05 – Dashboard and approvals inbox composition

| Item | Detail |
| --- | --- |
| Business purpose | Every user sees the next action across modules on one page, and approvers decide items of all modules in one place |
| Trigger | User opens Home (SCR-SH-03) or Approvals (SCR-SH-04); the menu's pending count on every page (SCR-SH-00) |
| Modules involved | Shell, EIMS, AMS, LMS, SMS |
| Requirement refs | FR-CMN-001 to 016; BR-CMN-08, 12, 16; INT-07, INT-03, INT-04, INT-06; BRD §5.3; UJ-SH-03, UJ-SH-04; NFR-02; D-58 |
| Pre-conditions / post-conditions | Pre: signed in. Post: each card shows its module's data or "Couldn't load" with Retry; inbox decisions are applied by the owning module |

```mermaid
sequenceDiagram
  actor U as User
  participant SH as Shell
  participant GW as API gateway
  participant E as EIMS
  participant A as AMS
  participant L as LMS
  participant S as SMS
  U->>SH: Open Home or Approvals
  par One call per module card
    SH->>GW: EIMS card
    GW->>E: Tiles, to-dos, inbox items
  and
    SH->>GW: AMS card
    GW->>A: Tiles, to-dos, missing days, inbox items
    A->>E: Employee details and direct reports (INT-03, INT-04)
    A->>L: Leave days for missing-day check (INT-06)
  and
    SH->>GW: LMS card
    GW->>L: Tiles, to-dos, inbox items
  and
    SH->>GW: SMS card
    GW->>S: Tiles, to-dos, inbox items, last reconciliation
  end
  SH-->>U: Cards render independently
  U->>SH: Approve selected (or reject, keep as is, reopen)
  SH->>GW: One request per module with its items
  GW-->>SH: Result per item
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | Shell | SH0010, SH0020, SH0030 | Client composition, one call per card (Part01 §8.4) | – | – |
| 2 | EIMS | EIMS0200 | Sync API (INT-07), user session | EIMS card – Module document (planned) | Read only, role and scope applied in the query |
| 3 | AMS | AMS0130 | Sync API (INT-07); calls EIMS0170, EIMS0180 and LMS0070 | AMS card – Module document (planned) | Read only |
| 4 | LMS | LMS0090 | Sync API (INT-07); calls EIMS0170, EIMS0180 | LMS card – Module document (planned) | Read only |
| 5 | SMS | SMS0120 | Sync API (INT-07); calls EIMS0170, EIMS0180 | SMS card – Module document (planned) | Read only; Voided excluded from totals (BR-CMN-16) |
| 6 | Shell → module | SH0040 → EIMS0150 / 0160, AMS0060 / 0070, LMS0050 / 0060, SMS0050 / 0060, SMS0070 → AMS0080 | Sync API through the gateway, one request per module | Module approve / reject / keep / reopen APIs | Per item: local transaction and version check in the owning module |

**Failure handling & compensation:** A module that is unavailable fails only its own card with Retry and the flow reference (FR-CMN-008); the menu count leaves that module out until it answers. In a bulk decision each item succeeds or fails on its own; failed items stay selected with their own error (FR-CMN-014). No cross-module transaction is needed.

**Reconciliation:** Not applicable; every card is read fresh from the owning module (no cache server in the POC, D-110 (8)).

### 5.6 XF-06 – Attendance and leave date check

| Item | Detail |
| --- | --- |
| Business purpose | No date carries both attendance and leave (BR-CMN-10) |
| Trigger | Employee saves or submits attendance (SCR-AMS-02); employee submits a leave request (SCR-LMS-02) |
| Modules involved | AMS, LMS |
| Requirement refs | BR-CMN-10; FR-AMS-007, 011, 012, 014; FR-LMS-012 to 014; INT-06; D-77 |
| Pre-conditions / post-conditions | Pre: profile approved (BR-CMN-09). Post: the record is saved or submitted only if the other module confirms no conflicting record |

```mermaid
sequenceDiagram
  actor U as Employee
  participant A as AMS
  participant L as LMS
  U->>A: Save or submit attendance for a date
  A->>L: Submitted or approved leave on the date? (INT-06)
  L-->>A: Yes / no
  A-->>U: Saved / submitted, or "You have leave on <date>"
  U->>L: Submit leave for a date range
  L->>A: Submitted or approved attendance on the dates? (INT-06)
  A-->>L: Dates found / none
  L-->>U: Submitted, or "You already have attendance on <date>"
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | AMS | AMS0020, AMS0030 | Sync API through the gateway | Save / submit attendance – Module document (planned) | Local transaction after the check |
| 2 | LMS | LMS0070 | Sync API (INT-06), service token (Part01 §9.9) | Leave on date – Module document (planned) | Read only |
| 3 | LMS | LMS0020 | Sync API through the gateway | Submit leave – Module document (planned) | Local transaction after the check |
| 4 | AMS | AMS0110 | Sync API (INT-06), service token | Attendance on dates – Module document (planned) | Read only |

**Failure handling & compensation:** If the check cannot be made, the save or submit is refused with a retry message and the flow reference; the check is never skipped (Part01 §8.2 row 7). Two submissions for the same employee and date reaching AMS and LMS at the same moment can each pass the other's check, since the check and the save are in different databases; how this is prevented or detected is open item OI-P02-02.

**Reconciliation:** None in the POC (OI-P02-02).

### 5.7 XF-07 – Date-of-joining change check

| Item | Detail |
| --- | --- |
| Business purpose | No attendance or leave lies before an employee's date of joining |
| Trigger | Admin changes the date of joining (SCR-EIMS-02) |
| Modules involved | EIMS, AMS, LMS |
| Requirement refs | FR-EIMS-015; INT-09; D-71 |
| Pre-conditions / post-conditions | Pre: Admin signed in. Post: the new date is saved only if neither AMS nor LMS holds a record before it (leave other than Cancelled) |

```mermaid
sequenceDiagram
  actor AD as Admin
  participant E as EIMS
  participant A as AMS
  participant L as LMS
  AD->>E: Save new date of joining (version)
  par
    E->>A: Attendance before the date? (INT-09)
  and
    E->>L: Leave other than Cancelled before the date? (INT-09)
  end
  A-->>E: Yes / no
  L-->>E: Yes / no
  E-->>AD: Saved, or refused with the reason
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | EIMS | EIMS0040 | Sync API through the gateway | Update Admin-owned fields – Module document (planned) | Version check |
| 2 | AMS | AMS0120 | Sync API (INT-09), service token | Records before date – Module document (planned) | Read only |
| 3 | LMS | LMS0080 | Sync API (INT-09), service token | Records before date – Module document (planned) | Read only |
| 4 | EIMS | EIMS0040 | Internal | – | Local transaction and audit |

**Failure handling & compensation:** If either check cannot be made, the change is refused with the flow reference (Part01 §8.2 row 10). A backdated record saved in AMS or LMS during the change is the same check-then-act case as XF-06 (OI-P02-02).

**Reconciliation:** None.

### 5.8 XF-08 – Manager change moving waiting items

| Item | Detail |
| --- | --- |
| Business purpose | After a manager change, new and already waiting items of the employee are decided by the new manager; the old manager no longer sees the employee |
| Trigger | Admin changes an employee's manager (SCR-EIMS-02) |
| Modules involved | EIMS, AMS, LMS, SMS, shell |
| Requirement refs | FR-EIMS-014, 017; FR-UM-014; BR-CMN-01, 08; INT-04; D-104 (OI-04); Part01 §9.7 |
| Pre-conditions / post-conditions | Pre: new manager is an active employee with the Manager role and creates no reporting loop. Post: every approval view, inbox and data-scope check resolves the approver from the new Manager Id |

```mermaid
sequenceDiagram
  actor AD as Admin
  participant E as EIMS
  actor NM as New manager
  participant SH as Shell
  participant X as AMS / LMS / SMS
  AD->>E: Save new manager (version)
  E->>E: Manager Id updated, audit (one transaction)
  NM->>SH: Open approvals inbox or team view
  SH->>X: Inbox items / team records
  X->>E: Direct reports and approver (INT-03, INT-04)
  E-->>X: Current reporting line
  X-->>NM: Waiting items of the employee now listed
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | EIMS | EIMS0040 | Sync API through the gateway | Update Admin-owned fields | Local transaction and audit; version check |
| 2 | AMS, LMS, SMS, EIMS | AMS0050 / 0130, LMS0040 / 0090, SMS0040 / 0120, EIMS0140 / 0200 | Sync API (INT-07 and module views) | Module card and team views | Read only |
| 3 | EIMS | EIMS0170, EIMS0180 | Sync API (INT-03, INT-04), user token relayed | Employee details, approver | Read only |
| 4 | AMS, LMS, SMS, EIMS | Approve / reject functions | Sync API through the gateway | Module decision APIs | Approver checked again at decision time (INT-04) |

**Failure handling & compensation:** Nothing is copied between modules: a waiting item has no stored approver until it is decided, and the approver is resolved from the current Manager Id each time an item is listed or decided (Part01 §9.7), so the move is immediate and needs no compensation. The Approver Id is stored on the record only with the decision (BR-CMN-02). If EIMS cannot be reached, approval views and decisions fail with the flow reference rather than fall back to an old reporting line.

**Reconciliation:** Not needed.

### 5.9 XF-09 – Account changes ending sessions: deactivation, password reset, role change

| Item | Detail |
| --- | --- |
| Business purpose | An Admin change to an account takes effect on every open session at once |
| Trigger | Admin deactivates an employee, resets a password or changes a role (SCR-EIMS-01, SCR-EIMS-02) |
| Modules involved | EIMS, SUP (UM, AUTH), API gateway, shell |
| Requirement refs | FR-EIMS-005, 012, 016, 018; FR-UM-003, 006, 007, 010, 011; FR-AUTH-004, 022; FR-CMN-016; BR-CMN-06, 14; INT-08; D-97, D-100, D-104 (OI-02), D-111 (6) |
| Pre-conditions / post-conditions | Pre: deactivation – no active direct reports (BR-CMN-14); role change Manager → Employee – no active direct reports (FR-EIMS-016). Post: deactivation – employee Inactive, account disabled; reset – temporary password set, lock and failed-attempt count cleared; role change – new role held; in all three, every open session of the user has ended |

```mermaid
sequenceDiagram
  actor AD as Admin
  participant E as EIMS
  participant IDP as Identity provider
  participant GW as API gateway (all instances)
  actor U as Affected user
  AD->>E: Deactivate / reset password / change role
  E->>E: Check rules (direct reports)
  E->>IDP: Disable account / set temporary password and clear lock / change role (INT-08)
  E->>IDP: End all sessions of the user
  IDP->>GW: Back-channel logout per session
  GW->>GW: Drop the gateway sessions (relayed between instances)
  E->>E: Commit employee change and audit
  E-->>AD: Done (temporary password shown once for a reset)
  U->>GW: Next action in an ended session
  GW-->>U: Sign-in page
```

| Step | Module | Function id | Interaction (sync API / event / job) | API / event | Consistency (local tx / outbox / saga / compensation) |
| --- | --- | --- | --- | --- | --- |
| 1 | EIMS | EIMS0050, EIMS0060, EIMS0040 | Sync API through the gateway | Deactivate / reset password / update Admin-owned fields | Rule checks on EIMS data |
| 2 | SUP (UM) | UM0040, UM0030, UM0050 | Sync API to the identity provider (INT-08), service account | Identity provider admin API | Keyed by Employee Id |
| 3 | SUP (AUTH) | AUTH0040 | Back-channel logout to the gateway (Part01 §9.6) | OIDC back-channel logout | Every gateway instance drops the session |
| 4 | EIMS | EIMS0050, EIMS0060, EIMS0040 | Internal | – | Local transaction and audit (password never recorded) |
| 5 | Shell | SH0010 | Next request | – | Sign-in page; a role change shows the new menu after sign-in |

**Failure handling & compensation:** If the identity provider cannot be reached, the Admin action is refused with the flow reference and nothing changes. The order of the identity-provider call and the EIMS commit, and recovery when the second fails, are designed in PMS-HLD-Part02-M5-SUP (OI-P02-01). Deactivation does not touch AMS, LMS or SMS: waiting items stay with the approver and other open items stay as they are (BR-CMN-06). A user's own password change ends only their other sessions and stays within AUTH (AUTH0030, D-100).

**Reconciliation:** None automatic in the POC; identity-provider security events (AUTH0060) and the activity log show every account change with its flow reference.
