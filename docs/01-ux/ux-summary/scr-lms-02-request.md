# UX Summary – SCR-LMS-02 Leave request

| Field | Value |
| --- | --- |
| Screen Id | SCR-LMS-02 |
| Module | LMS (checks attendance days via AMS) |
| Roles | Employee, Manager (own leave) |
| User journeys | UJ-LMS-01, UJ-LMS-03 |
| Mockup | `docs/01-ux/mockups/scr-lms-02-request.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets an employee request full-day leave for a date range, or correct a rejected request, and submit it to their manager.

## 2. Description

Leave type as three option buttons (Casual, Sick, Earned), From and To dates, and a live count of leave days with the date range. A side panel lists the rules. When fixing a rejected request, a red banner shows the manager's remarks.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| SCR-LMS-01 "+ Request leave" / "Edit" | This screen | – |
| Submit | SCR-LMS-01 | Valid |
| Cancel | SCR-LMS-01 | – |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Leave type | Option buttons | Y | Casual / Sick / Earned (LMS-V5) | Leave.leaveType | Owner |
| From date | Date | Y | Not before date of joining (LMS-V2); past allowed (D-07 / O5) | Leave.fromDate | Owner |
| To date | Date | Y | ≥ From date (LMS-V1); defaults to From date | Leave.toDate | Owner |
| Leave days | Calculated | – | Calendar days inclusive | – | System |
| Request date | Hidden | – | Set to today on submit (L1) | Leave.date | System |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Submit for approval | Owner | Validated and sent to manager | New / Rejected → Submitted | "<Type> leave <range> submitted to <manager>." |
| Cancel | Owner | Back to list | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| LMS-V1 to V6 | Range valid, not before joining, no overlap with own submitted/approved leave, no day with submitted/approved attendance, valid type, approved profile |
| BR-C4 | Rejected request can be corrected and resubmitted |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | Casual selected; dates blank; days "—" |
| Loading | Submit disabled while saving |
| Validation error | "To date must be on or after From date", "Overlaps your submitted Casual leave (…)", "You already have attendance on Tue 10 Nov…" |
| System error | Alert: "Leave request could not be submitted. Please try again." |

## 8. Accessibility

Leave type is a labelled radio group; errors linked to the date fields; day count is plain text.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-21 | Add an optional "Reason" text for the manager? The Leave entity has no such field today. | Product owner | Accepted (D-32) – no, keep the agreed entity for the POC |
| UXQ-22 | Save as draft for leave? | Product owner | Accepted (D-32) – no; leave is short to fill, submit directly |
