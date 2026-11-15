# UX Summary – SCR-EIMS-04 Profile review

| Field | Value |
| --- | --- |
| Screen Id | SCR-EIMS-04 |
| Module | EIMS |
| Roles | Manager (direct reports), Admin (top-level employees) |
| User journeys | UJ-EIMS-03, UJ-EIMS-09 (read-only) |
| Mockup | `docs/01-ux/mockups/scr-eims-04-profile-review.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets the approver check a submitted profile and approve or reject it, seeing exactly what changed for an update.

## 2. Description

Header with name, Employee Id, joining and submission dates, and status. Three cases:

| Case | Behaviour |
| --- | --- |
| New profile | Single "Submitted" column; Approve / Reject |
| Update to approved profile | "Previously approved" and "Submitted (new)" columns; changed rows highlighted with a "Changed" badge and the old value struck through |
| Read-only view (from My Team) | Single "Value" column; no actions |

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| SCR-SH-04 "Open" | This screen | Pending profile |
| SCR-EIMS-01 "View" | This screen (read-only) | Manager |
| "Back" | SCR-SH-04 or SCR-EIMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Profile fields | Read-only table | – | – | Submitted Employee record; last approved version for comparison | None |
| Remarks (reject dialog) | Text area | Y | Not blank, max 500 | Employee.remarks | Approver |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Approve | Manager, Admin | Profile becomes current | Submitted → Approved | "Profile approved." |
| Reject | Manager, Admin | Dialog → returned to employee | Submitted → Rejected | "Profile rejected and returned to <name>." |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| BR-C3 | Remarks required to reject |
| BR-C8 | A manager cannot approve their own profile |
| O3 / D-07 | Admin approves top-level employees |
| E2 / D-02 | Updates show what changed since last approval |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | n/a |
| Loading | Table skeleton |
| Validation error | "Remarks are required to reject." |
| System error | Alert with Retry |
| Already decided | Actions hidden; banner "Already approved/rejected by <name> on <date>" |

## 8. Accessibility

Changed rows are marked by a text badge, not only colour; struck-through old values are also in their own column header ("Previously approved").

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-15 | Showing the comparison needs the last approved version kept alongside the submitted one (e.g. an approved-snapshot of the Employee record). Accept this storage need for HLD? | Product owner | Accepted (D-29) – yes |
