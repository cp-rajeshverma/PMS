# UX Summary – SCR-LMS-03 Team leave review

| Field | Value |
| --- | --- |
| Screen Id | SCR-LMS-03 |
| Module | LMS |
| Roles | Manager (direct reports); Admin (top-level employee only, read limited to those records, D-58) |
| User journeys | UJ-LMS-04 |
| Mockup | `docs/01-ux/mockups/html/scr-lms-03-team-review.html` |
| Version / status | 1.1 / Approved (D-105; v1.0 D-34) |
| Last updated | 2026-11-21 |

## 1. Purpose

Lets a manager approve or reject direct reports' leave, seeing who else in the team is away on those dates.

## 2. Description

Under Leave, a "Team" tab with **Pending** and **History** sub-tabs, filters by team member and type. Pending rows show the submitted time (of the last submission) and an **Also away** column listing the approver's other direct reports with approved or pending leave overlapping those dates; it is empty for the top-level employee's requests (D-84). Multi-select approve; reject with remarks. History shows decisions and remarks and has a date range filter that opens on requests overlapping the current month and includes reports who became inactive, marked "Inactive" (D-84, D-88). The Admin sees the same screen limited to the top-level employee, without the team-member filter or the "My leave" tab.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Leave → Team tab, SCR-SH-04 "Open" | This screen | Manager |
| SCR-SH-04 "Open" | This screen (top-level employee only) | Admin |
| "My leave" tab | SCR-LMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee, Type, Dates, Days | Text | – | – | Leave + Employee | None |
| Also away | Text + count | – | Overlapping approved or submitted leave of the same manager's team | Leave (team) | None |
| Submitted / Decision | Text | – | – | Leave.submittedDate (last submission); approverId, approvedDate, remarks | None |
| History date range | Dates | N | From ≤ To; default current month | – | Manager, Admin |
| Remarks (dialog) | Text area | Y | Not blank, max 500 | Leave.remarks | Manager |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Approve (row or selected) | Manager | Request approved | Submitted → Approved | "Leave for <name> approved." |
| Reject | Manager | Dialog → back to employee | Submitted → Rejected | "Leave rejected and returned to <name>." |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| BR-C3, BR-C8 | Remarks required; no self-approval |
| D-24 / UXQ-01 | Multi-select approve; reject one at a time |
| D-06 / S6 | Approved leave earns no wage |
| D-84, D-88 | Also away empty for the top-level employee; History date range with current-month default incl. inactive reports |
| D-58, D-63 | Admin decides only the top-level employee's leave |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "Nothing pending — All leave requests have been decided." |
| Loading | Table skeleton |
| Validation error | "Remarks are required to reject." |
| System error | Alert; failed bulk items stay selected |
| Request cancelled meanwhile | Row removed with toast "This request was cancelled by the employee." |

## 8. Accessibility

"Also away" count is text, not only a coloured badge; buttons name the employee; dialogs trap focus.

## 9. Open questions

None.
