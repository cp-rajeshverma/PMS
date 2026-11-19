# UX Summary – SCR-SH-01 Login

| Field | Value |
| --- | --- |
| Screen Id | SCR-SH-01 |
| Module | Shell (built as a Keycloak login theme, D-16) |
| Roles | All |
| User journeys | UJ-SH-01, UJ-SH-02, UJ-SH-05 |
| Mockup | `docs/01-ux/mockups/html/scr-sh-01-login.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-15 |

## 1. Purpose

Lets an active employee sign in to PMS with Employee Id and password, and routes first-time users to set their own password.

## 2. Description

A centred card with the PMS brand, Employee Id and Password fields, a Show/Hide password toggle and a Sign in button. Error and warning messages appear above the fields. Help text tells users to contact the administrator for a forgotten password (D-07 / O6). The yellow "Mockup controls" bar lets reviewers pick the sign-in outcome; it is not part of the product.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Opening PMS, Log out, session expiry | This screen | Not signed in |
| This screen | Dashboard (SCR-SH-03) | Valid credentials |
| This screen | Set password (SCR-SH-02) | Valid temporary password (first login or after Admin reset) |

## 4. Fields

| Field | Type / control | Required | Validation | Data source (entity.attribute) | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee Id | Text | Y | Not empty; case-insensitive (EMP0007 = emp0007) | Keycloak username = Employee.employeeId | User |
| Password | Password, Show/Hide toggle | Y | Not empty | Keycloak credential | User |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Sign in – valid | All | Opens Dashboard | – | – |
| Sign in – temporary password | All | Opens Set password | – | – |
| Sign in – wrong credentials | All | Stays; password cleared | – | "Employee Id or password is incorrect. Please try again." |
| Sign in – inactive account | All | Stays | – | "Your account is inactive. Contact your PMS administrator." |
| Sign in – locked | All | Stays | – | "Too many failed attempts. Your account is locked for 15 minutes." |
| Show / Hide | All | Reveals or masks password | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| C3 / D-01 | Login with Employee Id + password; roles Employee, Manager, Admin |
| BR-C6 / EIMS-US6 | Deactivated employees cannot sign in |
| D-07 / O6 | No self-service reset; Admin resets passwords |
| Security | The message never reveals whether the Employee Id exists |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | Fields blank; focus in Employee Id |
| Loading | Button shows "Signing in…" and is disabled |
| Validation error | Field-level message under each empty field; red border |
| System error | Alert: "PMS is unavailable right now. Please try again shortly." |
| Locked | Warning alert (amber), as above |

## 8. Accessibility

Labels bound to inputs; alerts use `role="alert"`; correct `autocomplete` (username, current-password); Show/Hide has an accessible name; works with keyboard only (Enter submits).

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-09 | Lock the account after failed attempts? | Product owner | Accepted (D-26) –: lock 15 minutes after 5 failed attempts (Keycloak brute-force detection) |
