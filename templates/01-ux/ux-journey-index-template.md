# PMS – UX Journey Index

| Field | Value |
| --- | --- |
| Version | 0.1 |
| Status | Draft / In review / Approved |
| Owner | <name> |
| Last updated | <yyyy-mm-dd> |

Every user journey in PMS, including journeys run by backend scheduled jobs, with the screens that make up each.

## Journeys

| Journey Id | Journey name | Module | Actor (role or system job) | Trigger | Screens (in order) | Outcome |
| --- | --- | --- | --- | --- | --- | --- |
| UJ-<MOD>-01 | <e.g. Submit daily attendance> | AMS | Employee | <what starts it> | SCR-AMS-01 → SCR-AMS-02 | <end state> |
| UJ-SYS-01 | <e.g. Nightly salary reconciliation> | SMS | System (scheduled job) | <cron / event> | n/a (backend) | <end state> |

## Screen catalogue

| Screen Id | Screen name | Module | Roles | Mockup file | UX summary file |
| --- | --- | --- | --- | --- | --- |
| SCR-<MOD>-01 | <name> | <module> | <roles> | `docs/01-ux/mockups/html/<file>.html` | `docs/01-ux/ux-summary/<file>.md` |

## Navigation map

<Diagram or list of how screens link to each other, starting from login and the shell menu.>

## Sign-off

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | | | |
| Business stakeholder | | | |
