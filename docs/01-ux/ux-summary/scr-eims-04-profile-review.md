# UX Summary – SCR-EIMS-04 Profile review

| Field | Value |
| --- | --- |
| Screen Id | SCR-EIMS-04 |
| Module | EIMS |
| Roles | Manager (direct reports), Admin (top-level employees) |
| User journeys | UJ-EIMS-03, UJ-EIMS-09 (read-only) |
| Mockup | `docs/01-ux/mockups/html/scr-eims-04-profile-review.html` |
| Version / status | 1.1 / Approved (D-105; v1.0 D-34) |
| Last updated | 2026-11-21 |

## 1. Purpose

Lets the approver check a submitted profile or profile change request and approve or reject it, seeing exactly what changed in a change request.

## 2. Description

Header with name, Employee Id, joining and submission dates, and status. Three cases:

| Case | Behaviour |
| --- | --- |
| New profile | Single "Submitted" column; Approve / Reject |
| Profile change request (D-70) | "Approved profile" and "Requested change" columns; changed rows highlighted with a "Changed" badge and the old value struck through; approving applies the new values and the profile stays Approved |
| Request withdrawn | Banner "Withdrawn by the employee on <date>"; no actions (e.g. opened from an old link) |
| Read-only view (from My Team) | Single "Value" column; no actions |

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| SCR-SH-04 "Open" | This screen | Pending profile or change request |
| SCR-EIMS-01 "View" | This screen (read-only) | Manager |
| "Back" | SCR-SH-04 or SCR-EIMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Profile fields | Read-only table | – | – | Submitted Employee record; for a change request, the approved profile and the requested values | None |
| Remarks (reject dialog) | Text area | Y | Not blank, max 500 | Employee.remarks | Approver |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Approve | Manager, Admin | New profile becomes current, or requested values applied | Profile or request: Submitted → Approved | "Profile approved." |
| Reject | Manager, Admin | Dialog → returned to employee | Profile or request: Submitted → Rejected | "Profile rejected and returned to <name>." |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| BR-C3 | Remarks required to reject |
| BR-C8 | A manager cannot approve their own profile |
| O3 / D-07 | Admin approves top-level employees |
| D-70, D-72 | Change requests show what changed against the approved profile; the profile stays Approved |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | n/a |
| Loading | Table skeleton |
| Validation error | "Remarks are required to reject." |
| System error | Alert with Retry |
| Already decided or withdrawn | Actions hidden; banner "Already approved/rejected by <name> on <date>" or "Withdrawn by the employee" |

## 8. Accessibility

Changed rows are marked by a text badge, not only colour; struck-through old values are also in their own column header ("Previously approved").

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-15 | Showing the comparison needs the last approved version kept alongside the submitted one (e.g. an approved-snapshot of the Employee record). Accept this storage need for HLD? | Product owner | Accepted (D-29) – yes; replaced by the profile change request, which holds old and new values (D-70) |
