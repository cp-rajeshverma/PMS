# UX Summary – SCR-SH-02 Set password

| Field | Value |
| --- | --- |
| Screen Id | SCR-SH-02 |
| Module | Shell (Keycloak "Update password" page, same theme as SCR-SH-01) |
| Roles | All |
| User journeys | UJ-SH-02; change password from the user menu |
| Mockup | `docs/01-ux/mockups/scr-sh-02-set-password.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-16 |

## 1. Purpose

Lets a user replace a temporary password with their own (first login or after an Admin reset), or change their password at any time.

## 2. Description

A centred card in the login style. Two modes: **First login** (new + confirm password; no way to skip) and **Change password** (current + new + confirm; Cancel link back). A live checklist under the new password shows each rule turning green as it is met.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| SCR-SH-01 | This screen (first-login mode) | Temporary password used |
| User menu → Change password | This screen (change mode) | Signed in |
| This screen | Dashboard (SCR-SH-03) | Password saved, or Cancel (change mode only) |

## 4. Fields

| Field | Type / control | Required | Validation | Data source | Editable by |
| --- | --- | --- | --- | --- | --- |
| Current password | Password | Y (change mode) | Must match | Keycloak credential | User |
| New password | Password | Y | Password policy (UXQ-10) | Keycloak credential | User |
| Confirm new password | Password | Y | Equals New password | – | User |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Save password | All | Password updated; temporary flag cleared; opens Dashboard | – | "Password saved." |
| Cancel (change mode) | All | Back to Dashboard | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| E1 / D-02 | Admin issues a temporary password at onboarding |
| D-07 / O6 | Admin reset issues a new temporary password |
| UXQ-10 (proposed) | Policy: at least 8 characters, upper and lower case, a number, a special character, not the Employee Id |

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | Checklist all grey |
| Loading | Button disabled while saving |
| Validation error | "The new password does not meet all the rules below." / "Passwords do not match." / "Current password is incorrect." |
| System error | Alert: "Password could not be saved. Please try again." |

## 8. Accessibility

Checklist is linked to the field with `aria-describedby`; rule state is conveyed by text symbols (✓ / ○) as well as colour; correct `autocomplete` values.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-10 | Password policy as listed above? | Product owner | Open |
