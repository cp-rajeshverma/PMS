# UX Summary – SCR-EIMS-03 My profile

| Field | Value |
| --- | --- |
| Screen Id | SCR-EIMS-03 |
| Module | EIMS |
| Roles | Employee, Manager (own profile) |
| User journeys | UJ-EIMS-02, UJ-EIMS-04, UJ-EIMS-05 |
| Mockup | `docs/01-ux/mockups/html/scr-eims-03-my-profile.html` |
| Version / status | 1.1 / Approved (D-105; v1.0 D-34) |
| Last updated | 2026-11-21 |

## 1. Purpose

Lets employees complete their own personal details and submit them for their manager's approval, and change an approved profile through a profile change request (D-70).

## 2. Description

A status banner explains where the profile stands. A read-only "Set by your administrator" block shows Employee Id, manager, date of joining and hourly rate. Below, editable sections: Name, Parents, Birth, Employment (last employer), Address, Contact.

| Status | Behaviour |
| --- | --- |
| Draft | Editable; Save draft + Submit for approval |
| Submitted | Read-only; banner "waiting for <manager>"; **Withdraw** returns it to Draft until a decision is taken (D-70) |
| Approved | Read-only with **Request a change**; replaced by a link to the open request when one exists |
| Rejected | Editable; red banner with the manager's remarks |

Profile change request (approved profile only; one open request per employee, D-70, D-72). The profile stays Approved and in use by all modules until the request is approved; the header shows both badges, e.g. "Approved" and "Change request: Submitted".

| Request status | Behaviour |
| --- | --- |
| Draft | Fields pre-filled with the approved values and editable; changed fields are marked with a "Changed" badge; Save draft, Submit change request, Withdraw request |
| Submitted | Read-only, showing the requested values; banner "waiting for <manager>"; Withdraw request until a decision is taken |
| Rejected | Editable; red banner with the manager's remarks; Submit change request again, or Withdraw request |
| Approved | Request closed; the new values are the approved profile |
| Withdrawn | Request closed; a new request can be started |

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
| Submit for approval | Owner | Validated and sent to manager | Draft / Rejected → Submitted | "Profile submitted to <manager> for approval." |
| Withdraw (profile) | Owner | Profile back to editing, removed from the approver's inbox | Submitted → Draft (before decision) | "Profile withdrawn. You can edit it again." |
| Request a change | Owner | Opens a change request filled with the approved values | Request: – → Draft | Change request banner |
| Submit change request | Owner | Validated; needs at least one changed value; sent to manager | Request: Draft / Rejected → Submitted | "Change request submitted to <manager> for approval." / "No changes to submit." |
| Withdraw request | Owner | Request closed; approved profile unchanged | Request: Draft / Submitted (before decision) / Rejected → Withdrawn | "Change request withdrawn." |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| D-70, D-72, BR-CMN-05, BR-CMN-11 | An approved profile changes only through a profile change request; it stays Approved meanwhile (replaces D-02 E2) |
| BR-CMN-04 | Rejected profile or request can be fixed and resubmitted |
| AMS-V5, LMS-V6 | Attendance and leave need an approved profile |
| EIMS-V1 to V4 | Field validations |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | First visit: only Admin-entered fields filled; Draft banner |
| Loading | Form skeleton |
| Validation error | Field-level messages + toast "Please correct the highlighted fields." |
| System error | Alert: "Profile could not be saved. Please try again." |
| Read-only (Submitted / Approved / request Submitted) | Inputs locked; only Withdraw or Request a change offered |

## 8. Accessibility

Sections use headings; every input has a label; errors are linked to inputs and announced; date inputs accept keyboard entry.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-14 | While an approved profile is being re-approved, other modules keep using the last approved data and the employee keeps working normally. OK? | Product owner | Accepted (D-29) – yes; superseded by the profile change request (D-70): the profile stays Approved while a request is open |
