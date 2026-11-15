# UX Summary – SCR-SMS-01 My salary

| Field | Value |
| --- | --- |
| Screen Id | SCR-SMS-01 |
| Module | SMS |
| Roles | Employee, Manager (own salary; Manager also sees a "Team" tab) |
| User journeys | UJ-SMS-02, UJ-SMS-04 |
| Mockup | `docs/01-ux/mockups/scr-sms-01-my-salary.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Shows employees their daily wages for a period, and lets them accept or dispute each record once their manager has approved it.

## 2. Description

Tiles: earned in period (Accepted + Manager Approved), to review (count and amount), waiting for manager (Generated), disputed. Date-range filter (default: current month to today) and a "Show voided" toggle (hidden by default, D-25). Table per day: date, attendance times, hours, rate, amount, status, notes. Manager Approved rows have Accept / Dispute and a checkbox for **Accept selected**. Voided rows are greyed with the amount struck through and the void reason. A footer shows the period total.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Menu "Salary", dashboard "Review" | This screen | Employee, Manager |
| "Team" tab | SCR-SMS-02 | Manager |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Date, Attendance | Text | – | – | Salary.date; Attendance times (via attendanceId) | None |
| Hours | Number, 2 decimals | – | – | Salary.dayHour | None |
| Rate (₹/h) | Number | – | Copied at generation (SMS-R2) | Salary.dayWageRate | None |
| Amount | Currency, 2 decimals | – | Hours × Rate | Salary.dayWageAmount | None |
| Status | Badge | – | Generated, Manager Approved, Accepted, Disputed, Voided | Salary.status | None |
| Notes | Text | – | – | Salary.remarks (dispute remark or void reason) | None |
| Dispute remark (dialog) | Text area | Y | Not blank, max 500 | Salary.remarks | Employee |
| Period, Show voided | Dates, checkbox | N | From ≤ To | – | User |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Accept (row or selected) | Owner | Record final | Manager Approved → Accepted | "Salary for <date> accepted." / "<n> salary record(s) accepted." |
| Dispute | Owner | Dialog explains what happens → sent to manager | Manager Approved → Disputed | "Dispute sent to <manager>." |
| Change period / show voided | Owner | Table and tiles update | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| S3 / D-05 | Amount = hours × rate, 2 decimals, INR |
| S5 / D-05 | Manager approves first, then employee accepts or disputes |
| SMS-R2 | Rate fixed at generation |
| SMS-R4 | No one edits hours, rate or amount |
| D-25 | Voided: visible on demand, excluded from totals |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "No salary records in this period." |
| Loading | Table skeleton |
| Validation error | "A remark is required to dispute." |
| System error | Alert with Retry |
| Nothing to review | "To review" tile shows 0; no checkboxes |

## 8. Accessibility

Amounts right-aligned with tabular numbers; struck-through voided amounts also carry a "Voided" text badge; dialog traps focus.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-23 | Employee can **Accept selected** (several at once), like managers' bulk approve? | Product owner | Open – proposed: yes |
| UXQ-24 | Should records left in Manager Approved be auto-accepted after some days if the employee does nothing? | Product owner | Open – proposed: no auto-accept in the POC; dashboard keeps reminding |
