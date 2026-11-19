# UX Summary – SCR-SMS-02 Team salary review

| Field | Value |
| --- | --- |
| Screen Id | SCR-SMS-02 |
| Module | SMS (reopen action calls AMS) |
| Roles | Manager |
| User journeys | UJ-SMS-01, UJ-SMS-03, UJ-AMS-04 |
| Mockup | `docs/01-ux/mockups/html/scr-sms-02-team-review.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets a manager approve the team's generated wages and resolve disputes, with team totals for the period.

## 2. Description

Under Salary, a "Team" tab with **Needs action** (Generated + Disputed, disputes first) and **All records** sub-tabs; filters for team member, date range and "Show voided". Generated rows: Approve (row or selected). Disputed rows: the employee's remark, **Keep as is** (wage was correct; explanation required) and **Reopen attendance** (wage was wrong), each with a dialog explaining the effect. There is no Reject for salary (D-07 / O2). A "Team totals in period" table shows approved hours, earned amount and open items per employee.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Salary → Team tab, SCR-SH-04 "Open" | This screen | Manager |
| "My salary" tab | SCR-SMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee, Date, Hours, Rate, Amount, Status | Text, badges | – | – | Salary + Employee | None |
| Notes | Text | – | – | Salary.remarks (dispute remark / void reason) | None |
| Team totals | Table | – | Accepted + Manager Approved only | Salary aggregates | None |
| Remarks (reopen dialog) | Text area | Y | Not blank, max 500 | Attendance.remarks | Manager |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Approve (row or selected) | Manager | Employee can review | Generated → Manager Approved | "Approved. <name> can now review it." |
| Keep as is (disputed) | Manager | Dialog → explanation required; employee asked to accept again | Disputed → Manager Approved | "Dispute closed. <name> can accept the record." |
| Reopen attendance (disputed) | Manager | `AttendanceReopened` → attendance back to employee | Attendance Approved → Rejected; Salary Disputed → Voided | "Attendance reopened. Salary record voided." |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| S4, S5 / D-05 | Generated on attendance approval; manager approves |
| D-07 / O1, O2 | Disputes resolved by reopening attendance; no salary reject |
| D-25 | Voided records hidden by default, excluded from totals |
| BR-C8 | Manager's own salary is approved by their manager, not here |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "Nothing needs action — All generated records are approved and there are no open disputes." |
| Loading | Table skeleton |
| Validation error | Remarks required in reopen dialog |
| System error | Alert; failed bulk items stay selected |
| Dispute where attendance was right | Keep as is (D-33) |

## 8. Accessibility

Disputes are sorted first and labelled with text; amounts right-aligned; dialog explains consequences before confirming.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-25 | If the manager believes the attendance (and so the wage) was correct, how is a dispute closed without reopening? | Product owner | Accepted (D-33) – add **Keep as is** with a remark; record goes back to Manager Approved for the employee to accept |
