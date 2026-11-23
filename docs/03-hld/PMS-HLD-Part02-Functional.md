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
| 1.0 | 0.1 | 23-Nov-2026 | Rajesh Verma | First draft of §1–§3, based on the approved BRD set v1.0 (D-107), UX v1.1 (D-105), PMS-HLD-Part01 v1.0 rev 0.9 and PMS-HLD-Part01a v1.0 rev 0.5; Part02 anchor design answers of 23 Nov 2026 |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3 approved (D-122) |
| Product owner | Rajesh Verma | 23-Nov-2026 | §1–§3 approved (D-122) |
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
