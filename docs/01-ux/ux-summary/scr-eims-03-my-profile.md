# UX Summary – SCR-EIMS-03 My profile

| Field | Value |
| --- | --- |
| Screen Id | SCR-EIMS-03 |
| Module | EIMS |
| Roles | Employee, Manager (own profile) |
| User journeys | UJ-EIMS-02, UJ-EIMS-04, UJ-EIMS-05 |
| Mockup | `docs/01-ux/mockups/html/scr-eims-03-my-profile.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets employees complete and maintain their own personal details and submit them for their manager's approval.

## 2. Description

A status banner explains where the profile stands. A read-only "Set by your administrator" block shows Employee Id, manager, date of joining and hourly rate. Below, editable sections: Name, Parents, Birth, Employment (last employer), Address, Contact.

| Status | Behaviour |
| --- | --- |
| Draft | Editable; Save draft + Submit for approval |
| Submitted | Read-only; banner "waiting for <manager>" |
| Approved | Read-only with **Edit profile**; editing shows a warning that the profile goes back for approval |
| Rejected | Editable; red banner with the manager's remarks |

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Menu "My Profile", dashboard banner or to-do | This screen | Employee, Manager |
| This screen | Stays; status updates | After submit |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| First / Middle / Last name | Text | First, Last | Max 50 | Employee name fields | Employee |
| Father's / Mother's name | Text | Y | Max 100 | Employee.fatherName / motherName | Employee |
| Date of birth | Date | Y | Age ≥ 18 on date of joining (EIMS-V1) | Employee.dateOfBirth | Employee |
| Place of birth | Text | Y | Max 100 | Employee.placeOfBirth | Employee |
| Country of birth | Dropdown | Y | From country list | Employee.countryOfBirth | Employee |
| Last employer | Text | N | Max 100 | Employee.lastEmployer | Employee |
| Address line 1 / 2, City, State | Text | All but line 2 | Max 100 | Employee address fields | Employee |
| Country | Dropdown | Y | – | Employee.country | Employee |
| Zip / PIN code | Text | Y | 6 digits when country is India | Employee.zip | Employee |
| Email | Email | Y | Valid; unique (EIMS-V2) | Employee.email | Employee |
| Mobile number | Text | Y | Exactly 10 digits (EIMS-V3) | Employee.mobile | Employee |
| Employee Id, Manager, Date of joining, Hourly rate | Read-only | – | – | Employee | Admin only |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Save draft | Owner | Saved without validation of required fields | Stays Draft / Rejected | "Draft saved." |
| Submit for approval | Owner | Validated and sent to manager | Draft / Rejected / Approved → Submitted | "Profile submitted to <manager> for approval." |
| Edit profile | Owner | Unlocks fields, shows re-approval warning | – (until submitted) | Warning banner |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| E2 / D-02, BR-C5 | Edit after approval goes back to Submitted |
| BR-C4 | Rejected profile can be fixed and resubmitted |
| AMS-V5, LMS-V6 | Attendance and leave need an approved profile |
| EIMS-V1 to V4 | Field validations |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | First visit: only Admin-entered fields filled; Draft banner |
| Loading | Form skeleton |
| Validation error | Field-level messages + toast "Please correct the highlighted fields." |
| System error | Alert: "Profile could not be saved. Please try again." |
| Read-only (Submitted / Approved) | Inputs locked; actions hidden |

## 8. Accessibility

Sections use headings; every input has a label; errors are linked to inputs and announced; date inputs accept keyboard entry.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-14 | While an approved profile is being re-approved, other modules keep using the last approved data and the employee keeps working normally. OK? | Product owner | Accepted (D-29) – yes |
