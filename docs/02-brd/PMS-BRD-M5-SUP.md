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
| 1.0 | 0.1 | 20-Nov-2026 | Rajesh Verma | First draft from UX v1.0 (D-34), PMS-BRD v1.0 rev 0.12, PMS-BRD-M1-EIMS v1.0 rev 0.1 and decisions D-01 to D-101 |
| 1.0 | 0.2 | 20-Nov-2026 | Rajesh Verma | BRD set consistency check (D-103): references to PMS-BRD rev 0.14, module BRDs rev 0.2 and D-01 to D-103; FR-AUTH-012 password wording (D-99) |
| 1.0 | 0.3 | 20-Nov-2026 | Rajesh Verma | Business open items decided (D-104): FR-UM-014 waiting items move to the new manager; FR-AUTH-013 temporary password by company email; §14 open items closed |
| 1.0 | 0.4 | 21-Nov-2026 | Rajesh Verma | UX set v1.1 approved (D-105): FR-AUTH-024, FR-ADM-114 references; OI-11 closed in §14 |
| 1.0 | 0.5 | 21-Nov-2026 | Rajesh Verma | Stakeholder review held (D-106): reviewers recorded in §1.2, verdict approved with no comments |

### 1.2 Review and approval

Reviewer names are sample names for the POC; each review decision was confirmed by Rajesh Verma (product owner) on behalf of the role (D-106). Review record: docs/02-brd/reviews/PMS-BRD-Stakeholder-Review.md.

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | Rajesh Verma | | |
| Business analyst | Ananya Desai (sample reviewer, POC – confirmed by Rajesh Verma) | 21-Nov-2026 | Reviewed – approved, no comments |
| Module business owner / SME | Sunil Bhatt (sample reviewer, POC – confirmed by Rajesh Verma) | 21-Nov-2026 | Reviewed – approved, no comments |
| Module business owner / SME | Meenakshi Pillai (sample reviewer, POC – confirmed by Rajesh Verma) | 21-Nov-2026 | Reviewed – approved, no comments |
| Security / IT owner | Arvind Kulkarni (sample reviewer, POC – confirmed by Rajesh Verma) | 21-Nov-2026 | Reviewed – approved, no comments |

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
| 1 | PMS-BRD (anchor) | v1.0 rev 0.14 | Glossary, scope (§3.3), roles and role catalogue (§4.2), role × module access (§4.3), end-to-end step 2 (§5.1), journeys UJ-SH-01, 02, 05 (§5.2), FR-CMN-015, 016 (§5.3), BR-CMN-01, 06, 08, 19, INT-08, NFR-03 to NFR-05, NFR-09, C-05, C-06, DEP-01, R-04 |
| 2 | PMS-BRD-M1-EIMS | v1.0 rev 0.2 | Admin screens that drive user management: FR-EIMS-005, 010, 012, 016, 018, 040, 041; hand-over to the identity provider (§3.3, INT-08) |
| 3 | PMS-BRD-M2-AMS, PMS-BRD-M3-LMS, PMS-BRD-M4-SMS | v1.0 rev 0.2 | Consumers of sign-in, roles and data scope |
| 4 | UX Journey Index (navigation map, user menu) and UX Summaries SCR-SH-00, SCR-SH-01, SCR-SH-02, SCR-EIMS-01, SCR-EIMS-02, with their mockups | v1.0 (D-34) | Journeys, screens, fields, messages |
| 5 | PMS – Business Requirements Document (baseline) §4 | v1.0 (D-09) | Roles, permissions matrix, login (Employee Id and password, no single sign-on, no self-registration) |
| 6 | Decision log | D-01 to D-103 | Approved decisions, in particular D-01, D-07, D-24, D-26, D-28, D-29, D-57, D-58, D-63, D-71, D-97 to D-101 |

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

Need-basis result: **Phase 2 (D-57) – no POC requirements in this section.** The Admin's employee master data work (onboarding, Admin-owned fields, deactivation, password reset) is in PMS-BRD-M1-EIMS. No business value is changeable by the Admin in the POC: each is fixed by an approved decision and changes only through a release or a deployment setting (OI-05 closed, D-97). An Admin configuration screen is Phase 2.

The audit log and activity log (§8) use the ADM prefix (FR-ADM-1xx, as in the template) but are POC requirements; they are the only part of ADM in the POC (D-101).

**Fixed business values in the POC (for reference; defined in the cited decisions)**

| Value | POC setting | Source |
| --- | --- | --- |
| Session idle timeout | 30 minutes | D-26, FR-AUTH-020 |
| Lock after failed sign-ins | 5 failed attempts in a row, locked 15 minutes | D-26, FR-AUTH-005 |
| Password policy | At least 8 characters, upper and lower case, a number, a special character, not containing the Employee Id, different from the current password | D-28, D-97, D-99, VR-AUTH-01 |
| Nightly reconciliation time | 01:00 IST | D-24, JOB-CMN-01 |
| Remarks length | Maximum 500 characters | BR-CMN-03 |
| Leave types | Casual, Sick, Earned (full days) | D-04, PMS-BRD-M3-LMS |
| Attendance time steps | 15 minutes, 00:00 to 23:45 | D-31, D-77, PMS-BRD-M2-AMS |
| Activity log retention | 90 days in Production | D-101, FR-ADM-116 |

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| – | No POC requirements (Phase 2: configuration values, lookups and master data maintained by the Admin) | – | Phase 2 | – | – |

## 5. User and access management

User accounts are held in the identity provider (anchor DEP-01, INT-08). The Admin works on them only through the EIMS screens SCR-EIMS-01 and SCR-EIMS-02; the screen behaviour is in PMS-BRD-M1-EIMS and is referenced here. The reporting line (Manager Id) is EIMS master data (BR-CMN-01); delegation of approvals and access reviews are not part of the POC (anchor §13.1, R-02).

### 5.1 User accounts

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-UM-001 | Every employee has exactly one user account, created when the Admin onboards the employee (FR-EIMS-010): the user name is the Employee Id (FR-EIMS-040), the role is the one chosen by the Admin, the password is the temporary password (FR-EIMS-041) and the account is enabled. | Must | POC | SCR-EIMS-02, UJ-EIMS-01, UJ-SYS-04, INT-08 | Given the Admin saves a valid new employee, when the employee is created as EMP0013, then a user account EMP0013 exists with the chosen role, enabled, and its next sign-in opens Set password. |
| FR-UM-002 | Accounts are created only by Admin onboarding; there is no self-registration. | Must | POC | SCR-SH-01, baseline §4 | Given the sign-in page, then it offers no way to register a new account. |
| FR-UM-003 | A user account is never removed. When the employee is deactivated, the account is disabled and kept; its user name (Employee Id) is never reused (D-71). | Must | POC | BR-CMN-06, FR-EIMS-040 | Given EMP0012 is deactivated, when a new employee is onboarded, then the new account is not EMP0012 and EMP0012 still exists, disabled. |
| FR-UM-004 | One PMS Administrator account is set up when PMS is installed, with a fixed user name that is not in the Employee Id format and an initial password that must be replaced at the first sign-in. The Admin account follows the same password policy, lockout and idle timeout as every user (§6). | Must | POC | D-24, D-97 | Given PMS is newly installed, when the Admin signs in with the initial password, then Set password opens and no other screen can be reached before a new password is saved. |
| FR-UM-005 | The Admin account is not an employee: it has no employee record, is not listed in the directory and cannot be chosen as a manager (BR-EIMS-08). It cannot be deactivated and its role cannot be changed in PMS; its password is reset by IT operations outside PMS. | Must | POC | D-24, D-97 | Given the Admin opens Employees, then the Admin account is not listed and offers no Reset password, Edit or Deactivate. |
| FR-UM-006 | Password reset (behind FR-EIMS-005): the new temporary password replaces the current password and any earlier temporary password, which stop working; any lock and the failed-attempt count are cleared; all the user's open sessions end at once; the next sign-in opens Set password. | Must | POC | SCR-EIMS-01, UJ-EIMS-08, D-07, D-97 | Given EMP0007 is locked and signed in on another browser, when the Admin resets the password, then the other session returns to sign-in at its next action, the old password is refused, and the new temporary password signs in at once and opens Set password. |
| FR-UM-007 | Deactivation (behind FR-EIMS-018): the account is disabled at once and all the user's open sessions end; the user can no longer sign in (FR-AUTH-004). There is no reactivation in the POC (BR-EIMS-07). | Must | POC | SCR-EIMS-02, UJ-EIMS-07, BR-CMN-06, D-97 | Given EMP0009 is signed in, when the Admin deactivates EMP0009, then EMP0009's next action returns to the sign-in page and the next sign-in with the correct password shows the inactive-account message. |

### 5.2 Roles and authorization

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-UM-010 | Every user holds exactly one role: Employee or Manager for employees, Admin for the PMS Administrator account only (anchor §4.2). The role is held with the user account, chosen by the Admin at onboarding and changed only by the Admin (FR-EIMS-012); it is not part of profile approval (BR-EIMS-09). A Manager cannot be changed to Employee while they have active direct reports (FR-EIMS-016). | Must | POC | SCR-EIMS-02, D-29, D-71 | Given the onboarding form, then the role list offers Employee and Manager only. |
| FR-UM-011 | A role change takes effect at the user's next sign-in; until then the menu stays as it was, but every request is checked against the current role (FR-UM-013). | Must | POC | D-97 | Given EMP0007 is signed in as Employee, when the Admin changes the role to Manager, then Approvals appears only after EMP0007 signs in again. Given a signed-in Manager is changed to Employee, when they open Team attendance, then access is refused (FR-UM-015). |
| FR-UM-012 | The menu shows only the items the role can use, as in the navigation map: Employee – Home, My Profile, Attendance, Leave, Salary; Manager – the same plus Approvals, the Team tabs and Employees (team); Admin – Home, Approvals, Employees (FR-CMN-015). | Must | POC | SCR-SH-00, UX Journey Index navigation map, D-24 | Given the Admin signs in, then the menu shows Home, Approvals and Employees only. |
| FR-UM-013 | PMS checks every request – opening a screen, reading data, taking an action – against the user's role and data scope, not only by hiding menu items: Employee – own records; Manager – own records plus direct reports' records (current Manager Id, no skip-level, D-63); Admin – all employee master data, plus the top-level employee's records for review and decision only, with no other access to attendance, leave or salary (D-58). No one approves their own records (BR-CMN-08). | Must | POC | Anchor §4.3, NFR-03, R-04 | Given manager M1 manages B but not C, when M1 requests C's attendance, then no data of C is returned and access is refused. |
| FR-UM-014 | A manager's data scope follows the current Manager Id: after the Admin changes an employee's manager, the new manager sees and approves that employee's new items from then on, and the old manager no longer sees the employee. Items already waiting move to the new manager (D-104). | Must | POC | BR-CMN-01, FR-EIMS-017, D-104 | Given B's manager changes from M1 to M2, when M1 opens My Team, then B is not listed; when M2 opens it, B is listed. |
| FR-UM-015 | A request outside the user's role or data scope (for example a saved link to another employee's record or to an Admin page) opens a neutral page "You don't have access to this page." with a link to Home. No data of the record is shown, and the message does not reveal whether the record exists. The attempt is written to the activity log (§8). | Must | POC | D-99 | Given an Employee opens a link to SCR-EIMS-02, then "You don't have access to this page." is shown with a link to Home and no employee data. |

**User stories**

| Id | As a | I want to | So that |
| --- | --- | --- | --- |
| US-UM-01 | Employee or Manager | see only the menu items and records my role and data scope allow | I find my work quickly and nobody sees data they should not |
| US-UM-02 | PMS Administrator | have a user account created and disabled together with the employee, and reset a forgotten or locked password | employees can sign in from day one and leavers cannot |
| US-UM-03 | HR Manager | have every request checked against the user's role and data scope | personal data is seen only by the employee, their manager and the Admin (R-04) |

## 6. Authentication and session

Business policy only; the architecture is in PMS-HLD-Part01-Architecture-and-Design §9. Sign-in, password and session rules apply to every account, the PMS Administrator included.

### 6.1 Sign in – SCR-SH-01 (UJ-SH-01)

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-001 | Users sign in with their Employee Id (the Admin with the Admin user name) and password. The Employee Id is not case-sensitive. There is no single sign-on and no second sign-in factor in the POC. A valid sign-in opens the dashboard (FR-CMN-001). | Must | POC | SCR-SH-01, UJ-SH-01, D-01 | Given EMP0007 has an own password, when they sign in as "emp0007" with it, then the dashboard opens. |
| FR-AUTH-002 | Both fields are required; an empty field shows "Enter your Employee Id." or "Enter your password." under it and nothing is sent. While signing in, the button shows "Signing in…" and is disabled. | Must | POC | SCR-SH-01 | Given the password is empty, when the user clicks Sign in, then "Enter your password." is shown and no sign-in attempt is counted. |
| FR-AUTH-003 | A wrong password or an unknown Employee Id shows the same message, "Employee Id or password is incorrect. Please try again.", and clears the password. The message never reveals whether the Employee Id exists. | Must | POC | SCR-SH-01, NFR-03, D-97 | Given EMP9999 does not exist and EMP0007 does, when each is tried with a wrong password, then both show the same message. |
| FR-AUTH-004 | An inactive account cannot sign in. The message "Your account is inactive. Contact your PMS administrator." is shown only when the correct password is entered; a wrong password shows the message of FR-AUTH-003. | Must | POC | SCR-SH-01, BR-CMN-06, D-97 | Given EMP0009 is inactive, when signing in with the correct password, then the inactive message is shown; with a wrong password, the generic message is shown. |
| FR-AUTH-005 | After 5 failed sign-ins in a row the account is locked for 15 minutes; while locked, every sign-in is refused, even with the correct password, with "Too many failed attempts. Your account is locked for 15 minutes." The lock ends after 15 minutes or when the Admin resets the password (FR-UM-006). A successful sign-in sets the failed-attempt count back to zero. Unknown Employee Ids are never locked and always get the message of FR-AUTH-003. | Must | POC | SCR-SH-01, D-26, D-97 | Given 4 failed attempts for EMP0007, when the 5th fails, then the locked message is shown and a correct password is refused for 15 minutes. |
| FR-AUTH-006 | A sign-in with a temporary password opens Set password (FR-AUTH-010); no other screen can be reached until an own password is saved. | Must | POC | SCR-SH-01, SCR-SH-02, UJ-SH-02, FR-EIMS-041 | Given a new employee signs in with the temporary password, when they open the dashboard address directly, then Set password is shown again. |
| FR-AUTH-007 | A forgotten password is handled by the Admin; the sign-in page says "Forgot your password? Contact your PMS administrator." There is no self-service reset (C-06). | Must | POC | SCR-SH-01, D-07 | Given the sign-in page, then the help text is shown and no reset link is offered. |
| FR-AUTH-008 | When sign-in is not possible for technical reasons, the page shows "PMS is unavailable right now. Please try again shortly." and no attempt is counted. | Must | POC | SCR-SH-01 | Given the identity provider cannot be reached, when the user signs in, then the unavailable message is shown. |

### 6.2 Passwords – SCR-SH-02 (UJ-SH-02, change password)

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-010 | Set password (first sign-in or after a reset): the user enters a new password and confirms it, with no way to skip. On save the temporary password stops working, "Password saved." is shown and the dashboard opens. | Must | POC | SCR-SH-02, UJ-SH-02 | Given a temporary password was used, when a valid new password is saved, then the dashboard opens and the temporary password is refused at the next sign-in. |
| FR-AUTH-011 | Change password: any signed-in user can open Change password from the user menu, enter the current password, the new password and its confirmation, and save; Cancel returns to the dashboard. A wrong current password shows "Current password is incorrect." On save, all the user's other open sessions end; the session in which the password was changed continues (D-100). | Must | POC | SCR-SH-02, SCR-SH-00, D-100 | Given a signed-in user, when the current password is wrong, then "Current password is incorrect." is shown and the password is not changed. Given EMP0007 is signed in on two browsers, when the password is changed in one, then the other's next action opens the sign-in page. |
| FR-AUTH-012 | A new password must meet the password policy – at least 8 characters, an upper-case and a lower-case letter, a number, a special character, not containing the Employee Id (D-28, D-99) – and differ from the current or temporary password (D-97). A checklist shows each rule as met (✓) or not (○), not by colour alone. Otherwise "The new password does not meet all the rules below." or "Passwords do not match." is shown. There is no password history or expiry in the POC (Future). | Must | POC | SCR-SH-02, D-28, D-97 | Given "Emp0007!x" for EMP0007, when saved, then it is refused because it contains the Employee Id. Given the new password equals the current one, then it is refused. |
| FR-AUTH-013 | A temporary password does not expire; it stays valid until it is replaced at sign-in or by a later reset (FR-UM-006). It is shown only once, to the Admin (NFR-EIMS-02). The Admin sends it to the employee by company email, outside PMS; PMS sends no email (C-05). | Must | POC | D-97, D-104, FR-EIMS-005, FR-EIMS-041 | Given a temporary password issued 10 days ago and not used, when the employee signs in with it, then Set password opens. |
| FR-AUTH-014 | Passwords are never stored or shown in readable form; Show / Hide reveals only what the user is typing on the sign-in page. | Must | POC | SCR-SH-01, NFR-03 | Given any screen, report or log, then no password appears in readable form. |
| FR-AUTH-015 | If a password cannot be saved for technical reasons, "Password could not be saved. Please try again." is shown and the old password stays valid. | Must | POC | SCR-SH-02 | Given the save fails, then the message is shown and the previous password still signs in. |

### 6.3 Session and log out – SCR-SH-00 (UJ-SH-05)

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-020 | A session ends after 30 minutes without activity. The next action opens the sign-in page with "Your session has expired. Please sign in again." (FR-CMN-016); unsaved entries are lost. There is no warning before the timeout (Future). | Must | POC | SCR-SH-00, D-26, D-97 | Given a user is idle for 30 minutes, when they click a menu item, then the sign-in page shows the expiry message. |
| FR-AUTH-021 | A user may be signed in on several browsers at the same time; each session times out on its own. | Must | POC | D-97 | Given EMP0007 is signed in on two browsers, then both work, and logging out of one does not end the other. |
| FR-AUTH-022 | All the user's sessions end at once when the Admin deactivates the user or resets the password (FR-UM-006, FR-UM-007); when the user changes their own password, all their other sessions end (FR-AUTH-011). The next action in an ended session opens the sign-in page. | Must | POC | D-97, D-100 | Given EMP0007 is signed in, when the Admin resets the password, then EMP0007's next action opens the sign-in page. |
| FR-AUTH-023 | Log out is in the user menu and needs no confirmation. It ends the session in PMS and in the identity provider and opens the sign-in page without a message; the browser Back button does not show PMS pages again. | Must | POC | SCR-SH-00, UJ-SH-05, D-97 | Given a signed-in user logs out, when they press Back, then the sign-in page is shown, not the previous screen. |
| FR-AUTH-024 | The header shows the signed-in user's name, role and Employee Id; for the PMS Administrator it shows "PMS Administrator" without an Employee Id (UX v1.1). | Must | POC | SCR-SH-00, FR-CMN-015, D-105 | Given the Admin signs in, then the header shows "PMS Administrator" and no Employee Id. |

### 6.4 Security events

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-030 | The identity provider records every successful and failed sign-in, lock, log out, password set, change and reset, account creation, role change and deactivation, with the user, who performed it (the user or the Admin) and the date and time (IST). Passwords are never recorded. There is no screen to view these records in the POC (Phase 2, ADM); they are available to IT operations for investigation and are part of the activity flow in §8. | Must | POC | D-97, D-98, NFR-05 | Given the Admin resets EMP0007's password, then a record shows the reset of EMP0007 by the Admin with date and time and no password. |

**User stories**

| Id | As a | I want to | So that |
| --- | --- | --- | --- |
| US-AUTH-01 | User (any role) | sign in with my Employee Id and password | I can reach my work in PMS |
| US-AUTH-02 | New employee | replace my temporary password with my own at the first sign-in | only I know my password |
| US-AUTH-03 | User (any role) | change my password at any time | I can keep my account safe |
| US-AUTH-04 | User (any role) | log out, and be signed out automatically when I leave PMS idle | nobody else can use my session |
| US-AUTH-05 | HR Manager | have accounts locked after repeated failed sign-ins and messages that do not reveal valid Employee Ids | passwords cannot be guessed easily (R-04) |

## 7. Notification engine

Need-basis result: **Phase 2 (D-57) – no POC requirements in this section.** The POC sends no email or SMS (anchor C-05). Users are guided in the application by dashboard reminders, to-do items and the approvals inbox (anchor §5.3); the individual in-app notifications are listed in each module BRD §10 (NOT-EIMS, NOT-AMS, NOT-LMS, NOT-SMS). Channels, templates, preferences, delivery, reminders and escalation are Phase 2.

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| – | No POC requirements (Phase 2: email / SMS notifications) | – | Phase 2 | – | – |

## 8. Audit and activity log

PMS keeps two logs (D-98, D-101). The **audit log** is a business record of every change to business data: which value changed from what to what, in which process, by whom and when. The **activity log** is an operational record of how the system ran: every operation's entry, completed steps and exit, so that the complete execution flow of a user action or job can be followed when investigating an issue or a functional breakdown. Both are POC requirements (anchor BR-CMN-19, NFR-09); there is no screen to view them in the POC (viewer Phase 2). Security events (sign-in, lock, password and account changes) are recorded by the identity provider (FR-AUTH-030). Record-level audit fields stay on every record (BR-CMN-02, BR-CMN-07, NFR-05).

### 8.1 Audit log

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-ADM-101 | Every create, update and status change of a business record – employee (including the Admin-owned fields), profile change request, attendance, leave, salary record – and of a user account (role, enabled / active) is written to the audit log, one entry per changed field, with: record type and id, field, old value, new value, process (use case or job, e.g. UJ-EIMS-06, JOB-CMN-01), user (Employee Id, Admin or System), date and time (IST) and the flow reference (FR-ADM-113). | Must | POC | BR-CMN-19, D-101 | Given the Admin changes EMP0007's hourly wage rate from 250.00 to 300.00, then the audit log holds one entry: Employee EMP0007, Hourly Wage Rate, 250.00 → 300.00, UJ-EIMS-06, Admin, date and time. |
| FR-ADM-102 | A record's creation is recorded with its initial values; a status change records the old and new status, together with the remarks entered (BR-CMN-03). Changes made by the system (salary generation, voiding, reconciliation) are recorded with user "System" and the job or event as process. | Must | POC | BR-CMN-19, D-101 | Given attendance is reopened, then the audit log shows attendance Approved → Rejected by the manager with the remarks, and the salary record Disputed → Voided by System. |
| FR-ADM-103 | Audit entries cannot be changed or deleted, and are kept as long as the record they belong to (records are never physically deleted, BR-CMN-06). | Must | POC | BR-CMN-19, D-101 | Given an audit entry exists, then no user, Admin included, can change or remove it. |
| FR-ADM-104 | Sensitive values (D-71 sensitive attributes, hourly wage rate, salary amounts) are kept in full in the audit log, protected like the record itself. Passwords and temporary passwords are never recorded; a password change is recorded as an event without a value. | Must | POC | D-101, NFR-03 | Given a password reset, then the audit log shows the reset of the account and no password value. |
| FR-ADM-105 | There is no screen to view the audit log in the POC (Phase 2). IT operations extract a record's history for an investigation at the request of the HR Manager or Finance Manager. | Must | POC | D-101 | Given the HR Manager asks for EMP0007's change history, then IT operations can provide every change of that record in time order with old and new values. |

### 8.2 Activity log

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-ADM-111 | Every service operation (API) writes an activity log entry on entry, on the completion of each significant intermediate step and on exit; the exit entry holds the result (success, or error with its reason) and the duration. Every entry holds the module, operation, process (use case or job), user, date and time (IST) and flow reference. | Must | POC | NFR-09, D-98, D-101 | Given a manager approves attendance, then the AMS activity log shows entry, the steps completed (for example "checked approver", "status set to Approved", "hand-over sent to salary") and exit with result and duration. |
| FR-ADM-112 | Scheduled jobs and hand-over events (JOB-CMN-01, INT-01, INT-02) are logged the same way: start, each completed step and end, with the result and counts (for example records created, voided, mismatches). | Must | POC | NFR-09, D-101 | Given the nightly reconciliation runs, then the activity log shows its start, each step and its end with the counts. |
| FR-ADM-113 | Each user action and each job run gets one flow reference, which is carried through every module, operation and event it triggers, so that all its activity and audit entries can be read in sequence. | Must | POC | NFR-09, D-101 | Given attendance approval creates a salary record, then the AMS and SMS entries of that approval share one flow reference and read in time order. |
| FR-ADM-114 | When a system error message is shown to a user, it includes "Reference: <flow reference>" so the user can quote it to support (UX v1.1, SCR-SH-00). | Must | POC | D-101, D-105 | Given saving fails for a technical reason, then the error message shows a reference that finds the flow in the activity log. |
| FR-ADM-115 | The activity log never holds passwords, temporary passwords or session secrets. Personally identifiable and confidential information – the sensitive employee attributes (D-71), hourly wage rates, salary amounts and free-text remarks – is masked; entries hold ids, statuses, counts and outcomes only. | Must | POC | D-101, NFR-EIMS-01 | Given an employee submits a profile, then the activity log shows the Employee Id and status change but not the date of birth, address or mobile number. |
| FR-ADM-116 | The activity log is read only by IT operations, for investigation; there is no viewer screen in the POC (Phase 2). Entries are kept 90 days in Production. | Must | POC | D-101 | Given an entry is older than 90 days in Production, then it is no longer kept. |
| FR-ADM-117 | Refused requests – access outside the role or data scope (FR-UM-015) and validation or business-rule refusals – are logged with the reason, user and flow reference. | Must | POC | D-99, D-101 | Given an Employee opens an Admin page, then the activity log shows the refused request with the user and reason. |

**User stories**

| Id | As a | I want to | So that |
| --- | --- | --- | --- |
| US-ADM-01 | HR Manager or Finance Manager | get the full change history of a record, with old and new values, who and when | I can answer questions and disputes about the data |
| US-ADM-02 | IT operations (support) | follow one user action or job through every module, step by step, with a reference the user can quote | I can find the cause of an issue or a functional breakdown quickly |

## 9. Document management

Need-basis result: **Phase 2 (D-57) – no POC requirements in this section.** No module in the POC stores attachments or documents (PMS-BRD-M1-EIMS to M4-SMS). Attachment types, size, access and retention are Phase 2.

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| – | No POC requirements (Phase 2: documents and attachments) | – | Phase 2 | – | – |

## 10. Business and validation rules

Cross-module rules are in the anchor §6 and referenced here: BR-CMN-01 (manager and top-level approval), BR-CMN-06 (inactive employees cannot sign in), BR-CMN-08 (no self-approval), BR-CMN-14 (manager with reports cannot be deactivated), BR-CMN-19 (audit log).

| Rule id | Rule | Type (business / validation) | Applies to | Source |
| --- | --- | --- | --- | --- |
| VR-AUTH-01 | A new password has at least 8 characters, an upper-case and a lower-case letter, a number and a special character; it does not contain the Employee Id and differs from the current or temporary password. | Validation | SCR-SH-02 | D-28, D-97, D-99 |
| VR-AUTH-02 | The confirmation equals the new password; in change mode the current password must be correct. | Validation | SCR-SH-02 | UX SCR-SH-02 |
| VR-AUTH-03 | Employee Id and password are required to sign in; the Employee Id is not case-sensitive. | Validation | SCR-SH-01 | UX SCR-SH-01 |
| BR-AUTH-01 | After 5 failed sign-ins in a row the account is locked for 15 minutes; the lock ends after 15 minutes or on an Admin password reset; a successful sign-in sets the count to zero; unknown Employee Ids are never locked. | Business | SCR-SH-01 | D-26, D-97 |
| BR-AUTH-02 | Sign-in messages never reveal whether an Employee Id exists; the inactive-account message is shown only after the correct password. | Business | SCR-SH-01 | NFR-03, D-97 |
| BR-AUTH-03 | A temporary password does not expire, must be replaced before any other screen can be used, and stops working when a later reset issues a new one. | Business | SCR-SH-01, SCR-SH-02 | D-07, D-97 |
| BR-AUTH-04 | A session ends after 30 minutes idle; several sessions per user are allowed. All sessions end on deactivation or Admin password reset; the user's other sessions end when they change their own password. | Business | All screens | D-26, D-97, D-100 |
| BR-UM-01 | Every employee has exactly one user account, whose user name is the Employee Id; accounts are created only by Admin onboarding, never removed, and their user names are never reused. | Business | SCR-EIMS-02 | D-02, D-71, D-97 |
| BR-UM-02 | There is one PMS Administrator account, set up at installation; it is not an employee and cannot be deactivated or changed in PMS. | Business | SCR-EIMS-01, SCR-EIMS-02 | D-24, D-97 |
| BR-UM-03 | Every user holds one role (Employee, Manager or Admin); the role is set by the Admin and takes effect at the next sign-in. | Business | SCR-EIMS-02, SCR-SH-00 | D-29, D-97 |
| BR-UM-04 | Every request is checked against the user's role and data scope; a request outside them shows the neutral no-access page and reveals no data. | Business | All screens | Anchor §4.3, NFR-03, D-99 |
| BR-ADM-01 | Audit entries are written for every change of a business record or user account, cannot be changed or deleted, and are kept as long as the record. | Business | All modules | BR-CMN-19, D-101 |
| BR-ADM-02 | Logs never hold passwords; the activity log masks personally identifiable and confidential information and is kept 90 days in Production. | Business | All modules | NFR-09, D-101 |

## 11. Data requirements

The user account is held in the identity provider, not in a PMS module database (D-29); the audit and activity logs are records kept by every module, not business entities (anchor C-01).

### 11.1 User account

| Entity | Attribute | Description | Type / format | Mandatory | Sensitive (Y / N) |
| --- | --- | --- | --- | --- | --- |
| User account | User name | Employee Id (EMP + 4 digits) or the Admin user name; not case-sensitive | Text | Y | N |
| User account | Password | Own or temporary password; never stored or shown in readable form | Secret | Y | Y |
| User account | Temporary password flag | Password must be replaced at the next sign-in | Yes / No | Y | N |
| User account | Role | Employee, Manager or Admin | Code | Y | N |
| User account | Enabled | No when the employee is inactive | Yes / No | Y | N |
| User account | Failed sign-in count | Failed attempts in a row since the last success | Number | Y | N |
| User account | Locked until | End of the current lock, if any | Date-time (IST) | N | N |

### 11.2 Audit log entry

| Entity | Attribute | Description | Type / format | Mandatory | Sensitive (Y / N) |
| --- | --- | --- | --- | --- | --- |
| Audit log entry | Flow reference | Reference of the user action or job run (FR-ADM-113) | Text | Y | N |
| Audit log entry | Record type, Record id | Changed record (e.g. Employee EMP0007, Attendance id) | Text | Y | N |
| Audit log entry | Field | Changed field, or "created" / "status" | Text | Y | N |
| Audit log entry | Old value, New value | Values before and after the change | Text | N (empty on creation) | Y when the field is sensitive |
| Audit log entry | Process | Use case or job (UJ-…, JOB-…) | Text | Y | N |
| Audit log entry | Changed by | Employee Id, Admin or System | Text | Y | N |
| Audit log entry | Changed at | Date and time | Date-time (IST) | Y | N |

### 11.3 Activity log entry

| Entity | Attribute | Description | Type / format | Mandatory | Sensitive (Y / N) |
| --- | --- | --- | --- | --- | --- |
| Activity log entry | Flow reference | Reference of the user action or job run | Text | Y | N |
| Activity log entry | Module, Operation | Module and service operation (API) or job | Text | Y | N |
| Activity log entry | Process | Use case or job (UJ-…, JOB-…) | Text | Y | N |
| Activity log entry | Stage | Entry, step (with a short step name) or exit | Code | Y | N |
| Activity log entry | Result, Reason | On exit or refusal: success or error, with the reason | Text | N | N (masked, FR-ADM-115) |
| Activity log entry | Duration | Time from entry to exit | Milliseconds | N | N |
| Activity log entry | User | Employee Id, Admin or System | Text | Y | N |
| Activity log entry | Logged at | Date and time | Date-time (IST) | Y | N |

## 12. Non-functional requirements (supporting-specific)

System-wide NFRs are in the anchor §8 and apply in full: NFR-01 (sign-in and password pages within the page-load target), NFR-02 (the identity provider is part of PMS availability), NFR-03 (security), NFR-05 (auditability) and NFR-09 (activity log). The requirements below add the supporting-specific measures.

| NFR id | Category | Requirement | Measure / target |
| --- | --- | --- | --- |
| NFR-SUP-01 | Security | Passwords and temporary passwords are never stored, shown, logged or sent in readable form; a temporary password is visible only once, to the Admin (FR-AUTH-014, NFR-EIMS-02). | 0 readable passwords found in security testing and log review |
| NFR-SUP-02 | Security | Every role × screen and role × action combination is checked against the role and data scope, including direct links to screens and records outside the scope (FR-UM-013, FR-UM-015). | 0 access-control defects in security testing (anchor NFR-03); every screen tested by direct link for each role |
| NFR-SUP-03 | Security | Sign-in messages do not reveal whether an Employee Id exists, and the lock applies as in BR-AUTH-01. | Verified in security testing for unknown, active, inactive and locked accounts |
| NFR-SUP-04 | Privacy | The activity log holds no unmasked personally identifiable or confidential information (FR-ADM-115). | 0 unmasked sensitive values in log review (NFR-09, NFR-EIMS-01) |
| NFR-SUP-05 | Auditability | Every change of a business record or user account can be found in the audit log with old and new value, process, user and time, and every user action or job run can be followed end to end by its flow reference. | 100 % of changes made in testing found in the audit log; 100 % of tested flows traceable across modules by one reference |

**Volumetrics (input to HLD)**

| Volume type | Year 1 | Growth % per year | Notes |
| --- | --- | --- | --- |
| User accounts | About 101 (about 100 employees and 1 Admin) | 0 % (20 % headroom) | Anchor §8.1 |
| Sign-ins per day | Not estimated | – | Peak periods as anchor §8.1 |
| Audit and activity log entries | Not estimated | – | Sized in the HLD from the record volumes in anchor §8.1 |

## 13. Traceability matrix

| Capability | Screen id | Req id | Rule ids | Test ref (later) |
| --- | --- | --- | --- | --- |
| Sign in (UJ-SH-01) | SCR-SH-01 | FR-AUTH-001 to 008; FR-UM-002 | VR-AUTH-03; BR-AUTH-01, 02; BR-CMN-06 | |
| Set password on first sign-in (UJ-SH-02) | SCR-SH-01, SCR-SH-02 | FR-AUTH-006, 010, 012 to 015 | VR-AUTH-01, 02; BR-AUTH-03 | |
| Change password (user menu) | SCR-SH-00, SCR-SH-02 | FR-AUTH-011, 012, 015 | VR-AUTH-01, 02; BR-AUTH-04 | |
| Session and log out (UJ-SH-05) | SCR-SH-00 | FR-AUTH-020 to 024 | BR-AUTH-04 | |
| Security events | – | FR-AUTH-030 | – | |
| User account at onboarding (UJ-EIMS-01, UJ-SYS-04) | SCR-EIMS-02 | FR-UM-001 to 003 (with FR-EIMS-010, 040, 041) | BR-UM-01 | |
| PMS Administrator account | – | FR-UM-004, 005 | BR-UM-02 | |
| Password reset (UJ-EIMS-08) | SCR-EIMS-01 | FR-UM-006 (with FR-EIMS-005) | BR-AUTH-01, 03, 04 | |
| Deactivation (UJ-EIMS-07) | SCR-EIMS-02 | FR-UM-007 (with FR-EIMS-018) | BR-AUTH-04; BR-CMN-06, 14 | |
| Role (UJ-EIMS-01, UJ-EIMS-06) | SCR-EIMS-02 | FR-UM-010, 011 (with FR-EIMS-012, 016) | BR-UM-03 | |
| Authorization (all journeys) | SCR-SH-00 and all screens | FR-UM-012 to 015 | BR-UM-04; BR-CMN-01, 08 | |
| Audit log (all modules) | – | FR-ADM-101 to 105 | BR-ADM-01; BR-CMN-19 | |
| Activity log (all modules) | – | FR-ADM-111 to 117 | BR-ADM-02 | |
| Admin functions and master data, notifications, documents | – | None (Phase 2, §4, §7, §9) | – | – |

Counts: functional requirements 45 (FR-UM 13, FR-AUTH 20, FR-ADM 12); rules 13 (VR-AUTH-01 to 03, BR-AUTH-01 to 04, BR-UM-01 to 04, BR-ADM-01, 02); supporting NFRs 5; user stories 10 (US-UM-01 to 03, US-AUTH-01 to 05, US-ADM-01, 02).

## 14. Open items

Cross-module open items that affect SUP are in the anchor §12 and are not repeated: OI-02 (pending items of a deactivated employee) and OI-04 (pending items on a manager change, FR-UM-014) – both closed (D-104) – and OI-11 (shell UX updates for SUP and the error reference; closed, D-105). OI-EIMS-01 (how the temporary password reaches the employee; closed, D-104) is in PMS-BRD-M1-EIMS.

| Id | Question | Owner | Due | Status / decision |
| --- | --- | --- | --- | --- |
| OI-SUP-01 | Does changing one's own password end the user's other open sessions? | Product owner | Before §6 approval | Closed (D-100): yes; the session in which the password was changed continues |
