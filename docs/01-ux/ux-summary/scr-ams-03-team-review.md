# UX Summary – SCR-AMS-03 Team attendance review

| Field | Value |
| --- | --- |
| Screen Id | SCR-AMS-03 |
| Module | AMS |
| Roles | Manager (direct reports); Admin (top-level employee only, read limited to those records, D-58) |
| User journeys | UJ-AMS-03, UJ-AMS-04, UJ-SMS-03 |
| Mockup | `docs/01-ux/mockups/html/scr-ams-03-team-review.html` |
| Version / status | 1.1 / Approved (D-105; v1.0 D-34) |
| Last updated | 2026-11-21 |

## 1. Purpose

Lets a manager approve or reject direct reports' attendance, review history, and reopen an approved day when its salary is disputed.

## 2. Description

Under Attendance, a "Team" tab with two sub-tabs: **Pending** (count) and **History**. Filters: team member, date range (History opens on the current month and includes reports who became inactive, marked "Inactive", D-77). Pending rows above 12 hours carry an **"Over 12 h"** flag (information only). The Admin sees the same screen limited to the top-level employee, without the team-member filter or the "My attendance" tab. Pending rows have checkboxes for multi-select approve (UXQ-01), plus Approve / Reject per row. History shows the decision, remarks and status; an approved day whose salary is disputed shows a "Salary disputed" badge and a **Reopen** button.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Attendance → Team tab, SCR-SH-04 "Open", SCR-SMS-02 "Resolve" | This screen | Manager |
| SCR-SH-04 "Open" | This screen (top-level employee only) | Admin |
| "My attendance" tab | SCR-AMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee, Date, From, To, Hours (+ "Over 12 h", "Inactive") | Text, badges | – | – | Attendance + Employee | None |
| Submitted / Decision | Text | – | – | updatedDate; approverId, approvedDate, remarks | None |
| Status + Salary disputed badge | Badges | – | – | Attendance.status; Salary.status (SMS) | None |
| Filters | Dropdown, dates | N | From ≤ To | – | Manager |
| Remarks (dialogs) | Text area | Y | Not blank, max 500 | Attendance.remarks | Manager |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Approve (row or selected) | Manager | Locked; `AttendanceApproved` event published | Submitted → Approved | "Approved. Salary record … will be generated." |
| Reject | Manager | Dialog → back to employee | Submitted → Rejected | "Rejected and returned to <name>." |
| Reopen (disputed only) | Manager | Dialog explains effect → back to employee; `AttendanceReopened` event | Approved → Rejected; Salary → Voided | "Attendance reopened. Salary record voided." |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| BR-C3, BR-C8 | Remarks required; no self-approval |
| D-07 / O1, D-25 | Reopen only for a disputed salary; voids the salary record |
| D-16 | Approve / reopen publish events consumed by SMS |
| D-24 / UXQ-01 | Multi-select approve; reject one at a time |
| D-31, D-77 | "Over 12 h" flag for approvers; History default current month incl. inactive reports |
| D-58, D-63 | Admin decides only the top-level employee's attendance |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "Nothing pending — All attendance in this range has been decided." |
| Loading | Table skeleton |
| Validation error | "Remarks are required to reject." |
| System error | Alert; failed bulk items stay selected with per-row error |
| Rejected rows in History | Action column shows "With employee" |

## 8. Accessibility

Sub-tabs are links with clear selected state; checkboxes and buttons name the employee and date; dialogs trap focus.

## 9. Open questions

None.
