# UX Summary – SCR-SH-03 Dashboard

| Field | Value |
| --- | --- |
| Screen Id | SCR-SH-03 |
| Module | Shell (reads summary data from EIMS, AMS, LMS, SMS APIs) |
| Roles | Employee / Manager / Admin (different content per role) |
| User journeys | UJ-SH-01, UJ-SH-03; entry point to UJ-EIMS-02/04, UJ-AMS-01/02, UJ-LMS-01, UJ-SMS-02 |
| Mockup | `docs/01-ux/mockups/scr-sh-03-dashboard.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Shows each user, right after login, what needs their action and where they stand, so nothing is missed.

## 2. Description

- **Employee:** four tiles (hours this month, earnings this month excluding voided, leave this month, profile status); a "Things to do" list (rejected items to fix, missing attendance days, salary records to review, pending requests); recent activity.
- **Manager:** same as Employee, plus a "Waiting for your approval" card with counts per module and a button to the approvals inbox.
- **Admin:** tiles for active employees, profiles not yet approved, items waiting for Admin, and the last reconciliation run (UJ-SYS-02); recently onboarded employees; "+ Onboard employee" button.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Login, Home menu | This screen | Signed in |
| "Fix" / "Enter" (attendance) | SCR-AMS-02 | Item listed |
| "Review" (salary) | SCR-SMS-01 | Item listed |
| "View" (leave) | SCR-LMS-01 | Item listed |
| "Open approvals inbox" / "Review" | SCR-SH-04 | Manager, Admin |
| "+ Onboard employee" | SCR-EIMS-02 | Admin |
| "View all employees" | SCR-EIMS-01 | Admin |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Hours this month | Tile | – | – | Sum of approved Attendance hours, current month | None |
| Earnings this month | Tile | – | Excludes Voided and Disputed | Sum of Salary.dayWageAmount (Manager Approved + Accepted) | None |
| Leave this month | Tile | – | – | Approved Leave days in month; pending count | None |
| Profile status | Badge | – | – | Employee.status | None |
| Things to do | List | – | – | Rejected records, missing days, salary to review, pending requests | None |
| Approval counts | List | – | – | Items where approver = user, by module | None |
| Last reconciliation | Badge + text | – | – | Reconciliation job run log | None |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Open a to-do item | Employee, Manager | Opens the screen to act | – | – |
| Open approvals | Manager, Admin | Opens SCR-SH-04 | – | – |
| Onboard employee | Admin | Opens SCR-EIMS-02 | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| D-25 | Voided salary excluded from earnings |
| D-24 / UXQ-04 | Admin has no personal tiles |
| UXQ-11 (proposed) | "Missing attendance" reminder for Mon–Fri days with no attendance or leave, from date of joining |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "Things to do": "You're all caught up." Approvals card hidden when 0 |
| Loading | Skeleton tiles and lists |
| Validation error | n/a |
| System error | Each card fails independently with "Couldn't load. Retry" (one module down does not blank the page) |
| Profile not approved | Top banner: "Complete your profile to start entering attendance and leave" with button to SCR-EIMS-03 |

## 8. Accessibility

Tiles have text labels (not colour only); to-do priority dots are decorative, the text states the issue; headings structure the page (h1, h2).

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-11 | Show a "missing attendance" reminder for Mon–Fri days with no attendance or leave? (Reminder only; weekends stay allowed per D-08) | Product owner | Open |
