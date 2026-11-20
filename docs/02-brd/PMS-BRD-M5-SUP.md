# PMS – BRD-M5: Supporting Functions (SUP)

Document ID: PMS-BRD-M5-SUP-v1.0
Module: Supporting functions – user management (UM) and authentication and authorization (AUTH); administration and master data (ADM), notifications (NM) and document management (DM) on a need basis
Project: Payroll Management System (PMS) – proof of concept (POC), Step 3 BRD
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 20-Nov-2026 | Rajesh Verma | First draft from UX v1.0 (D-34), PMS-BRD v1.0 rev 0.11, PMS-BRD-M1-EIMS v1.0 rev 0.1 and decisions D-01 to D-97 |

### 1.2 Review and approval

Names are added when the customer shares them.

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | Rajesh Verma | | |
| Business analyst | [BA] | | |
| Module business owner / SME | [HR Manager] | | |
| Module business owner / SME | [Finance Manager] | | |
| Security / IT owner | [Security / IT owner] | | |

## 2. Introduction

### 2.1 Purpose

This document defines the supporting functions PMS needs, on a need basis (D-53, D-57). It covers two capabilities in the POC:

- **User management (UM)** – the user account behind every employee and the PMS Administrator: creation at onboarding, role, temporary passwords, password reset, deactivation, and who may do what on which data (authorization).
- **Authentication and session (AUTH)** – sign-in with Employee Id and password, setting and changing the own password, password policy, lockout, idle timeout and log out.

Administration and master data (ADM), notifications (NM) and document management (DM) keep their sections with the result of the need-basis assessment (§3); they are Phase 2 (D-57) and carry no POC requirements.

The Admin screens that drive user management – onboarding, role, deactivation and password reset – belong to EIMS (PMS-BRD-M1-EIMS §7.1, §7.2, §7.5). This document defines the capability behind them and references those requirements instead of repeating them. Roles, the role catalogue, role × module access, cross-module rules (BR-CMN) and system-wide NFRs are in the anchor PMS-BRD and are referenced, not repeated. The requirements are technology-neutral: the user accounts, credentials and roles are held in an **identity provider** (anchor DEP-01, INT-08); the product is chosen in PMS-HLD-Part01-Architecture-and-Design §9.

### 2.2 Reference documents

| # | Document | Version | Use |
| --- | --- | --- | --- |
| 1 | PMS-BRD (anchor) | v1.0 rev 0.11 | Glossary, scope (§3.3), roles and role catalogue (§4.2), role × module access (§4.3), end-to-end step 2 (§5.1), journeys UJ-SH-01, 02, 05 (§5.2), FR-CMN-015, 016 (§5.3), BR-CMN-01, 06, 08, INT-08, NFR-03 to NFR-05, C-05, C-06, DEP-01, R-04 |
| 2 | PMS-BRD-M1-EIMS | v1.0 rev 0.1 | Admin screens that drive user management: FR-EIMS-005, 010, 012, 016, 018, 040, 041; hand-over to the identity provider (§3.3, INT-08) |
| 3 | PMS-BRD-M2-AMS, PMS-BRD-M3-LMS, PMS-BRD-M4-SMS | v1.0 rev 0.1 | Consumers of sign-in, roles and data scope |
| 4 | UX Journey Index (navigation map, user menu) and UX Summaries SCR-SH-00, SCR-SH-01, SCR-SH-02, SCR-EIMS-01, SCR-EIMS-02, with their mockups | v1.0 (D-34) | Journeys, screens, fields, messages |
| 5 | PMS – Business Requirements Document (baseline) §4 | v1.0 (D-09) | Roles, permissions matrix, login (Employee Id and password, no single sign-on, no self-registration) |
| 6 | Decision log | D-01 to D-97 | Approved decisions, in particular D-01, D-07, D-24, D-26, D-28, D-29, D-57, D-58, D-63, D-71, D-97 |

### 2.3 Terms used in this document

Terms already in the anchor glossary (Employee Id, Admin, temporary password, soft delete) are not repeated.

| Term | Meaning |
| --- | --- |
| Identity provider | The shared service that holds user accounts, passwords and roles, signs users in and enforces the password policy, lockout and idle timeout (anchor DEP-01, INT-08) |
| User account | The sign-in identity of one person: user name, password, role and enabled / disabled state. Every employee has exactly one; the PMS Administrator has one without an employee record |
| Session | The period from sign-in to log out or expiry during which the user can work without signing in again |
| Lock | Temporary block on sign-in for 15 minutes after 5 failed attempts in a row (D-26) |
| Data scope | The records a role may see and act on: own, direct reports, all employee master data, or the top-level employee's records (anchor §4.2, §4.3) |

## 3. Need-basis assessment

### 3.1 Assessment

| Capability | Needed? (Yes / No / Partial) | Provided by (existing capability) | Project requirements in | Consumer modules |
| --- | --- | --- | --- | --- |
| Admin functions & master data (ADM) | No – Phase 2 (D-57) | Not needed in the POC: every business value (idle timeout, lockout limits, password policy, reconciliation time, remarks length, leave types) is fixed by an approved decision and changed only through a release or deployment setting; no Admin configuration screen (OI-05 closed, D-97). Employee master data is EIMS | §4 (need-basis result only) | All |
| User & access management (UM) | Yes | Identity provider for user accounts, roles and passwords; the EIMS Admin screens SCR-EIMS-01 and SCR-EIMS-02 are the user interface (FR-EIMS-005, 010, 012, 016, 018, 040, 041). The reporting line (Manager Id) is EIMS master data (BR-CMN-01) | §5 | EIMS (drives it), Shell, AMS, LMS, SMS (role and data scope) |
| Authentication & session (AUTH) | Yes | Identity provider for sign-in, password policy, lockout and session; Shell screens SCR-SH-00, SCR-SH-01, SCR-SH-02 | §6 | All |
| Notification engine (NM) | No – Phase 2 (D-57) | Not needed in the POC: users are guided by in-app dashboard reminders and the approvals inbox (anchor §5.3, module BRDs §10); no email or SMS (C-05) | §7 (need-basis result only) | – |
| Audit & activity log | Partial | Record audit fields are kept by each module (BR-CMN-02, BR-CMN-07, NFR-05). Security events (sign-in, lockout, password and account changes) are recorded by the identity provider – required in §6. Project requirement (D-98): the important activities and events of every use case are logged in sequence, linked to the flow they belong to, so the complete execution flow can be followed when investigating an issue or a functional breakdown. No audit viewer screen in the POC (Phase 2, ADM) | §6, §8 | All |
| Document management (DM) | No – Phase 2 (D-57) | Not needed in the POC: no module stores attachments or documents | §9 (need-basis result only) | – |

### 3.2 Scope of UM and AUTH in the POC

| In scope (POC) | Phase 2 / Future | Out of scope |
| --- | --- | --- |
| One user account per employee, created at onboarding with the Employee Id as user name and a temporary password (with FR-EIMS-010, 041) | – | Self-registration – accounts are created by the Admin only (baseline §4) |
| One PMS Administrator account set up when PMS is installed; not an employee (D-24, D-97) | – | More than one Admin account |
| Role Employee or Manager per employee, chosen by the Admin and held with the user account (D-29) | – | Custom roles or per-user permissions |
| Authorization by role and data scope on every request (anchor §4.2, §4.3, NFR-03) | Future: skip-level manager view (D-63); delegation of approvals (R-02) | – |
| Sign-in with Employee Id and password; temporary password replaced at first sign-in; change own password | Future: self-service password reset (C-06, D-07); single sign-on (anchor §3.3) | Multi-factor sign-in |
| Password policy (D-28); new password differs from the current one (D-97) | Future: password history and expiry (D-97) | – |
| Lock for 15 minutes after 5 failed sign-ins; Admin password reset also unlocks (D-26, D-97) | – | Separate unlock action |
| Idle timeout 30 minutes; several sessions per user allowed; log out (D-26, D-97) | Future: warning before idle timeout (D-97) | – |
| Deactivation disables sign-in and ends open sessions (BR-CMN-06, D-97) | Future: reactivation (D-71) | – |
| Security events recorded by the identity provider (D-97) | Phase 2: audit viewer (ADM) | – |
| Activity log: important activities and events of every use case logged in sequence, so the complete execution flow can be followed for investigation (D-98) | Phase 2: audit viewer (ADM) | – |

### 3.3 Hand-overs with other modules

| Direction | Module / system | What | When | Ref |
| --- | --- | --- | --- | --- |
| In | EIMS | Create user account (Employee Id, role, temporary password) | Admin onboards an employee | FR-EIMS-010, 041, INT-08 |
| In | EIMS | Change role | Admin changes the role | FR-EIMS-012, 016, INT-08 |
| In | EIMS | Issue a new temporary password and unlock | Admin resets a password | FR-EIMS-005, INT-08 |
| In | EIMS | Disable the account and end its sessions | Admin deactivates an employee | FR-EIMS-018, INT-08 |
| Out | Shell, EIMS, AMS, LMS, SMS | Signed-in user: user name (Employee Id), role | Every request | NFR-03, anchor §4.3 |
| Out | Shell | Session ended (log out, idle timeout, deactivation, password reset) | When it happens | FR-CMN-016 |
| In | Shell, EIMS, AMS, LMS, SMS, identity provider | Activities and events of each use case, in sequence and linked to their flow | As each step happens | §8, D-98 |

## 4. Admin functions and master data

To be drafted (need-basis result).

## 5. User and access management

To be drafted.

## 6. Authentication and session

To be drafted.

## 7. Notification engine

To be drafted (need-basis result).

## 8. Audit and activity log

To be drafted.

## 9. Document management

To be drafted (need-basis result).

## 10. Business and validation rules

To be drafted.

## 11. Data requirements

To be drafted.

## 12. Non-functional requirements (supporting-specific)

To be drafted.

## 13. Traceability matrix

To be drafted.

## 14. Open items

To be drafted.
