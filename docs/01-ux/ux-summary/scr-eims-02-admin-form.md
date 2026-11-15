# UX Summary – SCR-EIMS-02 Employee admin form

| Field | Value |
| --- | --- |
| Screen Id | SCR-EIMS-02 |
| Module | EIMS |
| Roles | Admin |
| User journeys | UJ-EIMS-01, UJ-EIMS-06, UJ-EIMS-07, UJ-SYS-04 |
| Mockup | `docs/01-ux/mockups/scr-eims-02-admin-form.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets Admin onboard a new employee with the minimum details needed to sign in, and later maintain the Admin-owned details (manager, role, wage rate, active status).

## 2. Description

- **Create mode:** name, email, date of joining, role, manager, hourly wage rate. On save, a success panel shows the generated Employee Id and a one-time temporary password with Copy.
- **Edit mode:** name and email are read-only (the employee maintains them in My Profile); Admin edits date of joining, role, manager and rate. An "Account" section offers **Deactivate employee** with a confirmation dialog. Status badges show profile status and Active/Inactive.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| SCR-EIMS-01, Admin dashboard | This screen (create) | "+ Onboard employee" |
| SCR-EIMS-01 "Edit" | This screen (edit) | – |
| This screen | SCR-EIMS-01 | Cancel, or "Back to employees" after create |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Employee Id | Read-only | – | System-generated, unique (EMP0001…) | Employee.employeeId | System |
| First / Middle / Last name | Text | First, Last | Max 50 characters | Employee name fields | Admin on create; employee after |
| Email | Email | Y | Valid format; unique (EIMS-V2) | Employee.email | Admin on create; employee after |
| Date of joining | Date | Y | Not after today (EIMS-V4) | Employee.dateOfJoining | Admin |
| Role | Dropdown: Employee, Manager | Y | – | Keycloak realm role (not an Employee column) – see UXQ-12 | Admin |
| Manager | Dropdown of active managers, or "None – top-level" | Y | Active; not self (EIMS-V5) | Employee.managerId | Admin |
| Hourly wage rate (₹) | Decimal | Y | > 0, max 2 decimals (EIMS-V6) | Employee.hourlyWageRate | Admin |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Create employee | Admin | Employee + Keycloak user created; Id and temporary password shown once | Profile = Draft; Active | "Employee created…" panel |
| Save changes | Admin | Admin-owned fields updated | Profile status unchanged (Admin fields are not part of employee approval) | "Changes saved." |
| Deactivate | Admin | Confirm dialog → sign-in disabled | Is Active = false | "<name> deactivated." |
| Cancel | Admin | Back to directory | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| E1 / D-02 | Admin creates with basic details; system generates Employee Id and temporary password |
| C1, S1 / D-01, D-05 | Manager Id and hourly rate set by Admin |
| SMS-R2 | Rate change applies only to salary records generated afterwards |
| BR-C6 / EIMS-US6 | Deactivate is a soft delete; history kept |
| O3 / D-07 | "None – top-level" means Admin approves this employee's records |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | Create mode: blank fields; Employee Id shows "Generated on save" |
| Loading | Save button disabled while saving |
| Validation error | Field-level messages (duplicate email, future joining date, missing manager, invalid rate) |
| System error | Alert: "Employee could not be saved. Please try again." |
| Created | Success panel replaces the form |

## 8. Accessibility

Required fields marked with * and `required`; errors linked to fields; the temporary password panel is announced (`role="status"`).

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-12 | Role (Employee / Manager) is chosen by Admin on this form and stored in Keycloak, not in the Employee table. OK? | Product owner | Open |
| UXQ-13 | If a manager is deactivated while they still have direct reports, block it until Admin reassigns the reports? | Product owner | Open – proposed: block with message listing the reports |
