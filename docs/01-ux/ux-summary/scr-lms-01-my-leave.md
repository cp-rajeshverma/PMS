# UX Summary – SCR-LMS-01 My leave

| Field | Value |
| --- | --- |
| Screen Id | SCR-LMS-01 |
| Module | LMS |
| Roles | Employee, Manager (own leave; Manager also sees a "Team" tab) |
| User journeys | UJ-LMS-01, UJ-LMS-02, UJ-LMS-03 |
| Mockup | `docs/01-ux/mockups/html/scr-lms-01-my-leave.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Shows employees all their leave requests and their status, and lets them cancel a pending request or fix a rejected one.

## 2. Description

Tiles: approved days this year by type (Casual, Sick, Earned) and pending requests. An info note states that balances are not tracked and days are calendar days. Filters by status and type. A table lists requests (dates, type, days, requested date, status, manager remarks) newest first; cancelled requests are dimmed.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Menu "Leave", dashboard to-do | This screen | Employee, Manager |
| "+ Request leave" | SCR-LMS-02 (new) | – |
| "Edit" on a rejected row | SCR-LMS-02 (fix) | Rejected |
| "Team" tab | SCR-LMS-03 | Manager |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Tiles | Numbers | – | Approved only, current calendar year | Leave aggregates | None |
| Dates, Type, Days | Text | – | Days = To − From + 1 | Leave.fromDate, toDate, leaveType | None |
| Requested | Date | – | – | Leave.date (request date, L1) | None |
| Status, Manager remarks | Badge, text | – | – | Leave.status, remarks | None |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Cancel (Submitted only) | Owner | Confirm dialog → withdrawn | Submitted → Cancelled | "Leave request cancelled." |
| Edit (Rejected only) | Owner | Opens request form pre-filled | – | – |
| Filter | Owner | List narrows | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| L2, L3 / D-04 | Three full-day types; no balances |
| O4 / D-07 | Cancel only while Submitted |
| D-08 | Calendar days, weekends counted (see UXQ-19) |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "No leave requests — Use + Request leave to apply." |
| Loading | Table skeleton |
| Validation error | n/a |
| System error | Alert with Retry |
| Profile not approved | Banner; "+ Request leave" disabled (LMS-V6) |

## 8. Accessibility

Status shown as text badges; cancel dialog states the consequence; table headers for all columns.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-19 | Leave days count every calendar day, including weekends (follows D-08: no weekend rules). OK for the POC? | Product owner | Accepted (D-32) – yes |
| UXQ-20 | New status **Cancelled** for withdrawn requests (O4 allowed cancelling but named no status). OK? | Product owner | Accepted (D-32) – yes |
