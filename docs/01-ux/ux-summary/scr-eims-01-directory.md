# UX Summary – SCR-EIMS-01 Employee directory

| Field | Value |
| --- | --- |
| Screen Id | SCR-EIMS-01 |
| Module | EIMS |
| Roles | Admin (all employees, full actions), Manager ("My Team": direct reports, read-only) |
| User journeys | UJ-EIMS-01, 06, 07, 08, 09 |
| Mockup | `docs/01-ux/mockups/html/scr-eims-01-directory.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets Admin find and manage any employee, and lets a manager see who is in their team.

## 2. Description

Search box (name, Employee Id, email), profile-status filter and a "Show inactive" toggle above a table. Admin sees Manager and Hourly rate columns and Edit / Reset password actions; managers see their direct reports only, without rates, and a View action. Inactive employees are dimmed with an "Inactive" badge.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Menu "Employees" / "My Team", Admin dashboard | This screen | Admin, Manager |
| "+ Onboard employee" | SCR-EIMS-02 (create) | Admin |
| "Edit" | SCR-EIMS-02 (edit) | Admin |
| "View" | SCR-EIMS-04 (read-only) | Manager |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee Id | Text | – | – | Employee.employeeId | None |
| Name + role chip | Text | – | – | Employee name; Keycloak role | None |
| Email | Text | – | – | Employee.email | None |
| Manager | Text | – | Admin only | Employee.managerId → name | None |
| Joined | Date | – | – | Employee.dateOfJoining | None |
| Rate (₹/h) | Number | – | Admin only | Employee.hourlyWageRate | None |
| Profile | Badge | – | – | Employee.status | None |
| Search, status filter, show inactive | Inputs | N | – | – | User |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Search / filter | Admin, Manager | List narrows | – | Count updates |
| Reset password | Admin | Confirm dialog → temporary password shown once with Copy | Keycloak: temporary password, must change at next sign-in | "Temporary password issued…" |
| Edit | Admin | Opens SCR-EIMS-02 | – | – |
| View | Manager | Opens read-only profile | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| Permissions matrix (BRD §4) | Admin views all; Manager views own team |
| D-07 / O6 | Admin resets passwords; no self-service reset |
| BR-C6 | Inactive employees hidden by default, never deleted |
| D-24 / UXQ-04 | Admin is a system account, not listed as an employee |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | "No employees found — Try a different search or filter." |
| Loading | Table skeleton |
| Validation error | n/a |
| System error | Alert above table with Retry |

## 8. Accessibility

Search has an accessible label; table has header cells; action buttons include the employee name in their accessible name; dialog traps focus.

## 9. Open questions

None.
