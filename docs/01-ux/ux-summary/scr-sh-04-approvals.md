# UX Summary – SCR-SH-04 Approvals inbox

| Field | Value |
| --- | --- |
| Screen Id | SCR-SH-04 |
| Module | Shell (aggregates pending items from EIMS, AMS, LMS, SMS) |
| Roles | Manager (direct reports), Admin (top-level employee profiles) |
| User journeys | UJ-SH-04, UJ-EIMS-03, UJ-AMS-03, UJ-LMS-04, UJ-SMS-01, UJ-SMS-03 |
| Mockup | `docs/01-ux/mockups/html/scr-sh-04-approvals.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

One place for a manager's daily approval routine, so they can clear all pending items across modules quickly (D-24 / UXQ-03).

## 2. Description

Tabs filter by module (All, Profiles, Attendance, Leave, Salary) with counts. A table lists each item: type, employee, details, submitted time (or the employee's dispute remark), status and actions. Selecting rows shows a bulk bar to approve several at once (UXQ-01). Reject opens a dialog that requires remarks. A disputed salary row offers **Reopen attendance**, which explains the effect (attendance back to Rejected, salary Voided) before confirming.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Menu "Approvals", Dashboard | This screen | Manager, Admin |
| "Open" on a row | Module review screen (SCR-EIMS-04, SCR-AMS-03, SCR-LMS-03, SCR-SMS-02) | Needs full detail |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Type | Chip | – | – | Source module | None |
| Employee | Name + Id | – | – | Employee | None |
| Details | Text | – | – | Record summary (date, times, hours, leave type and range, wage) | None |
| Submitted / note | Text | – | – | Updated date, or dispute remark | None |
| Status | Badge | – | – | Record status | None |
| Remarks (dialog) | Text area | Y for reject / reopen | Not blank, max 500 characters | Record.remarks | Approver |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Approve (row) | Manager, Admin | Item removed from inbox (salary rows have Approve only, no Reject) | Submitted → Approved; Salary Generated → Manager Approved | "<Type> for <name> approved." (+ "Salary record will be generated." for attendance) |
| Approve selected | Manager, Admin | Items removed | As above | "<n> item(s) approved." |
| Reject | Manager, Admin | Dialog → item returned to employee | Submitted → Rejected | "… rejected and returned to the employee." |
| Keep as is (dispute) | Manager | Dialog → explanation required | Salary Disputed → Manager Approved | "Dispute closed. <name> can accept the record." |
| Reopen attendance (dispute) | Manager | Dialog → attendance returned to employee | Attendance Approved → Rejected; Salary → Voided | "Attendance reopened. Salary record voided." |
| Open | Manager, Admin | Opens module review screen | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| BR-C3 | Remarks required to reject |
| BR-C8 | A manager never sees their own records here |
| D-07 / O1, O2 | Disputes resolved by reopening attendance; manager cannot reject a generated salary record |
| D-24 / UXQ-01 | Multi-select approve; reject one at a time |
| D-25 | Reopen voids the salary record |
| BR-C1 / O3 | Admin approves the top-level employee's profile |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "All caught up — Nothing is waiting for your approval." |
| Loading | Table skeleton |
| Validation error | "Remarks are required to reject." |
| System error | Alert above table; failed bulk items stay selected with a per-row error |
| Item changed meanwhile | "This item was changed by someone else. Refresh to see the latest." |

## 8. Accessibility

Checkboxes and action buttons have descriptive labels including the employee name; dialogs trap focus and return it on close; toasts are announced (`aria-live`).

## 9. Open questions

None.
