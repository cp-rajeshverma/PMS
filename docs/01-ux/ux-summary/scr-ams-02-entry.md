# UX Summary – SCR-AMS-02 Attendance entry

| Field | Value |
| --- | --- |
| Screen Id | SCR-AMS-02 |
| Module | AMS |
| Roles | Employee, Manager (own attendance) |
| User journeys | UJ-AMS-01, UJ-AMS-02 |
| Mockup | `docs/01-ux/mockups/html/scr-ams-02-entry.html` |
| Version / status | 1.1 / Approved (D-105; v1.0 D-34) |
| Last updated | 2026-11-21 |

## 1. Purpose

Lets an employee record one day's working times and submit them for approval, or fix a rejected entry.

## 2. Description

Date, From time and To time, with hours worked calculated live. A side panel lists the rules. The banner and buttons depend on the record's status:

| Status | Behaviour |
| --- | --- |
| New / Draft | Editable; Save draft + Submit for approval; a saved Draft also offers **Discard** |
| Rejected | Editable; red banner with manager's remarks; **Discard** offered (e.g. after a reopen for a day not worked) |
| Draft / Rejected on a leave day | Banner: the entry cannot be submitted while submitted or approved leave covers the date – discard it (D-77) |
| Submitted | Read-only; "waiting for approval" banner |
| Approved | Read-only; "locked, salary record generated" banner |

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| SCR-AMS-01, dashboard "Fix" / "Enter" | This screen | – |
| Submit | SCR-AMS-01 | Valid |
| Cancel | SCR-AMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Date | Date picker | Y | Not future; not before date of joining (AMS-V3); unique per employee (AMS-V1); not a leave day (AMS-V4). Read-only once the record exists | Attendance.date | Owner |
| From time | Time | Y | – | Attendance.fromTime | Owner |
| To time | Time | Y | After From time, same day (AMS-V2) | Attendance.toTime | Owner |
| Hours worked | Calculated, read-only | – | To − From, 2 decimals | (shown only; SMS stores Day Hour) | System |
| Confirm over 12 hours | Checkbox, shown above 12 hours | Y when shown | Must be ticked to submit (warn, not block, D-31) | – | Owner |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Save draft | Owner | Saved | → Draft | "Draft saved." |
| Submit for approval | Owner | Validated, sent to manager | Draft / Rejected → Submitted | "Attendance for <date> submitted to <manager>." |
| Discard | Owner (Draft or Rejected) | Confirm dialog → entry kept inactive, date free again | Is Active = false (status kept) | "Attendance for <date> discarded." |
| Cancel | Owner | Back to calendar | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| AMS-V1 to V5 | One per day, same-day times, no future, no leave clash, approved profile needed |
| BR-CMN-04, BR-CMN-05 | Rejected can be fixed; approved is locked |
| D-77 | Draft or Rejected can be discarded (soft delete); 15-minute steps 00:00–23:45, minimum 0.25 h |
| D-31 | Above 12 hours the employee confirms the times before submitting |
| S4 / SMS-R1 | Approval triggers the salary record (UJ-SYS-01) |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | Date blank (or pre-filled from calendar); From 09:00 default; hours "—" |
| Loading | Buttons disabled while saving |
| Validation error | Field messages: "Date cannot be in the future", "already exists — Open it", "You have leave on <date>…", "To time must be after From time" |
| System error | Alert: "Attendance could not be saved. Please try again." |
| Read-only | Inputs locked, buttons hidden |

## 8. Accessibility

Native date and time inputs (keyboard-entry friendly); errors linked to fields; calculated hours announced as text.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-16 | Can an employee withdraw a Submitted attendance before the manager decides? | Product owner | Accepted (D-31) – no; ask the manager to reject it (keeps AMS simple) |
| UXQ-17 | Time precision | Product owner | Accepted (D-31) – 15-minute steps (e.g. 09:15), so hours are clean (8.25 h) |
| UXQ-18 | Very long days | Product owner | Accepted (D-31) – warn (not block) above 12 hours: "Over 12 hours — please confirm the times." |
