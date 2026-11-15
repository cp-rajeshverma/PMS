# UX Summary – SCR-LMS-03 Team leave review

| Field | Value |
| --- | --- |
| Screen Id | SCR-LMS-03 |
| Module | LMS |
| Roles | Manager |
| User journeys | UJ-LMS-04 |
| Mockup | `docs/01-ux/mockups/scr-lms-03-team-review.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets a manager approve or reject direct reports' leave, seeing who else in the team is away on those dates.

## 2. Description

Under Leave, a "Team" tab with **Pending** and **History** sub-tabs, filters by team member and type. Pending rows show an **Also away** column listing team members with approved or pending leave overlapping those dates. Multi-select approve; reject with remarks. History shows decisions and remarks.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Leave → Team tab, SCR-SH-04 "Open" | This screen | Manager |
| "My leave" tab | SCR-LMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee, Type, Dates, Days | Text | – | – | Leave + Employee | None |
| Also away | Text + count | – | Overlapping approved or submitted leave of the same manager's team | Leave (team) | None |
| Requested / Decision | Text | – | – | Leave.date; approverId, approvedDate, remarks | None |
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
