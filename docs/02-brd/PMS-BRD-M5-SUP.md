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
| FR-UM-014 | A manager's data scope follows the current Manager Id: after the Admin changes an employee's manager, the new manager sees and approves that employee's new items from then on, and the old manager no longer sees the employee. Items already waiting follow open item OI-04. | Must | POC | BR-CMN-01, FR-EIMS-017, OI-04 | Given B's manager changes from M1 to M2, when M1 opens My Team, then B is not listed; when M2 opens it, B is listed. |
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
| FR-AUTH-011 | Change password: any signed-in user can open Change password from the user menu, enter the current password, the new password and its confirmation, and save; Cancel returns to the dashboard. A wrong current password shows "Current password is incorrect." | Must | POC | SCR-SH-02, SCR-SH-00 | Given a signed-in user, when the current password is wrong, then "Current password is incorrect." is shown and the password is not changed. |
| FR-AUTH-012 | A new password must meet the password policy – at least 8 characters, an upper-case and a lower-case letter, a number, a special character, not the Employee Id (D-28) – and differ from the current or temporary password (D-97). A checklist shows each rule as met (✓) or not (○), not by colour alone. Otherwise "The new password does not meet all the rules below." or "Passwords do not match." is shown. There is no password history or expiry in the POC (Future). | Must | POC | SCR-SH-02, D-28, D-97 | Given "Emp0007!x" for EMP0007, when saved, then it is refused because it contains the Employee Id. Given the new password equals the current one, then it is refused. |
| FR-AUTH-013 | A temporary password does not expire; it stays valid until it is replaced at sign-in or by a later reset (FR-UM-006). It is shown only once, to the Admin (NFR-EIMS-02). How it reaches the employee is open item OI-EIMS-01. | Must | POC | D-97, FR-EIMS-005, FR-EIMS-041 | Given a temporary password issued 10 days ago and not used, when the employee signs in with it, then Set password opens. |
| FR-AUTH-014 | Passwords are never stored or shown in readable form; Show / Hide reveals only what the user is typing on the sign-in page. | Must | POC | SCR-SH-01, NFR-03 | Given any screen, report or log, then no password appears in readable form. |
| FR-AUTH-015 | If a password cannot be saved for technical reasons, "Password could not be saved. Please try again." is shown and the old password stays valid. | Must | POC | SCR-SH-02 | Given the save fails, then the message is shown and the previous password still signs in. |

### 6.3 Session and log out – SCR-SH-00 (UJ-SH-05)

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-020 | A session ends after 30 minutes without activity. The next action opens the sign-in page with "Your session has expired. Please sign in again." (FR-CMN-016); unsaved entries are lost. There is no warning before the timeout (Future). | Must | POC | SCR-SH-00, D-26, D-97 | Given a user is idle for 30 minutes, when they click a menu item, then the sign-in page shows the expiry message. |
| FR-AUTH-021 | A user may be signed in on several browsers at the same time; each session times out on its own. | Must | POC | D-97 | Given EMP0007 is signed in on two browsers, then both work, and logging out of one does not end the other. |
| FR-AUTH-022 | All the user's sessions end at once when the Admin deactivates the user or resets the password (FR-UM-006, FR-UM-007); the next action in any of them opens the sign-in page. | Must | POC | D-97 | Given EMP0007 is signed in, when the Admin resets the password, then EMP0007's next action opens the sign-in page. |
| FR-AUTH-023 | Log out is in the user menu and needs no confirmation. It ends the session in PMS and in the identity provider and opens the sign-in page without a message; the browser Back button does not show PMS pages again. | Must | POC | SCR-SH-00, UJ-SH-05, D-97 | Given a signed-in user logs out, when they press Back, then the sign-in page is shown, not the previous screen. |
| FR-AUTH-024 | The header shows the signed-in user's name, role and Employee Id; for the PMS Administrator it shows "PMS Administrator" without an Employee Id (open item OI-11). | Must | POC | SCR-SH-00, FR-CMN-015, OI-11 | Given the Admin signs in, then the header shows "PMS Administrator" and no Employee Id. |

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
