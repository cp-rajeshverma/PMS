# UX Summary – SCR-AMS-01 My attendance

| Field | Value |
| --- | --- |
| Screen Id | SCR-AMS-01 |
| Module | AMS (leave days read from LMS) |
| Roles | Employee, Manager (own attendance; Manager also sees a "Team" tab) |
| User journeys | UJ-AMS-01, UJ-AMS-02 |
| Mockup | `docs/01-ux/mockups/html/scr-ams-01-my-attendance.html` |
| Version / status | 1.1 / Approved (D-105; v1.0 D-34) |
| Last updated | 2026-11-21 |

## 1. Purpose

Gives employees a month-at-a-glance view of their attendance, what is approved, what needs action, and which weekdays are missing.

## 2. Description

Four tiles: approved hours (and days), waiting for approval, needs your action (rejected or draft), missing weekdays. A month calendar (Mon–Sun) shows each day's status badge and times; leave days show a Leave badge; weekdays up to yesterday with no attendance or leave are outlined as **Missing** (reminder only, D-28; today is never missing, D-104). A Draft or Rejected entry on a date now covered by submitted or approved leave carries the flag **"Leave on this day – discard"** (D-77). Today is highlighted; future days are greyed. A Calendar / List toggle switches to a table view (D-24 / UXQ-02).

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Menu "Attendance", dashboard | This screen | Employee, Manager |
| "+ Enter attendance", a missing or empty day | SCR-AMS-02 (new, date pre-filled) | Past or today |
| A day with attendance / list "Edit" or "View" | SCR-AMS-02 (that record) | – |
| "Team" tab | SCR-AMS-03 | Manager |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Tiles | Numbers | – | – | Aggregates of Attendance for month | None |
| Day cell | Badge + times + hours | – | – | Attendance (date, fromTime, toTime, status); Leave (LMS) | None |
| List columns | Date, From, To, Hours, Status (with the leave flag where it applies), Manager remarks | – | – | Attendance; Leave (LMS) | None |
| Month | Prev / Next | – | Not before date of joining; not after current month | – | User |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Click a day | Owner | Opens entry for that date | – | – |
| Switch Calendar / List | Owner | Changes view | – | – |
| Change month | Owner | Loads that month | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| A1 / AMS-V1 | One entry per day |
| A3 / AMS-V4 | Leave days cannot hold attendance (no entry possible from a leave cell) |
| D-08 | Weekends allowed; not flagged as missing |
| D-28 / UXQ-11, D-104 | Missing-weekday reminder, days up to yesterday |
| D-77 | Draft or Rejected entry on a leave day is flagged and can only be discarded |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | New joiner: all weekdays since joining up to yesterday show Missing; tiles 0 |
| Loading | Calendar skeleton |
| Validation error | n/a |
| System error | Alert with Retry; leave data failing alone shows "Leave days unavailable" note, attendance still shown |
| Profile not approved | Banner: "Your profile must be approved before you can enter attendance." "+ Enter attendance" disabled (AMS-V5) |

## 8. Accessibility

Each day is a button with an accessible name ("Thu 12 Nov, Rejected"); status is text, not only colour; the List view offers the same data in a table.

## 9. Open questions

None.
