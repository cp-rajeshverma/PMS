# UX Summary – SCR-SH-00 Shell layout

| Field | Value |
| --- | --- |
| Screen Id | SCR-SH-00 |
| Module | Shell |
| Roles | Employee / Manager / Admin |
| User journeys | UJ-SH-03, UJ-SH-04, UJ-SH-05 (frame for all journeys) |
| Mockup | `docs/01-ux/mockups/html/scr-sh-00-layout.html` |
| Version / status | 0.1 / Draft – in review |
| Last updated | 2026-11-15 |

## 1. Purpose

Gives every PMS screen one consistent frame: header, role-based menu and user menu, so users always know where they are and what they can do.

## 2. Description

- **Header (56 px):** PMS brand at left; user button at right showing avatar initials, name, role and Employee Id.
- **Sidebar (232 px):** menu items filtered by role (navigation map in the UX journey index). Active item highlighted. "Approvals" shows a red count of pending items.
- **Content area:** module screens render here, with breadcrumb and page title. Desktop width 1366 px (D-24).
- The yellow "Mockup controls" bar is mockup-only, for switching roles; it is not part of the product.

## 3. Navigation

| From (entry point) | To (exit point) | Condition |
| --- | --- | --- |
| Login (SCR-SH-01) | Home (SCR-SH-03) inside this layout | Successful sign-in |
| Sidebar item | Matching module screen | Item visible for role |
| User menu → Change password | SCR-SH-02 | Always |
| User menu → Log out | SCR-SH-01 | Always; session ended |

## 4. Fields

| Field | Type / control | Required | Validation | Data source (entity.attribute) | Editable by |
| --- | --- | --- | --- | --- | --- |
| User name | Text | – | – | Employee.firstName + lastName | None |
| Role | Text | – | – | Keycloak role claim | None |
| Employee Id | Text | – | – | Employee.employeeId | None |
| Pending approvals count | Badge | – | Hidden when 0 | Count of Submitted / Generated / Disputed items for approver, across modules | None |

## 5. Actions

| Action | Who | Result | Status change | Message shown |
| --- | --- | --- | --- | --- |
| Select menu item | All | Opens screen | – | – |
| Open user menu | All | Shows Change password, Log out | – | – |
| Log out | All | Ends session, returns to login | – | – |

## 6. Business rules applied

| Rule Id | Summary |
| --- | --- |
| Permissions matrix (BRD §4) | Menu items shown by role |
| D-24 / UXQ-04 | Admin has no personal records, so no My Profile, Attendance, Leave or Salary items |
| D-24 / UXQ-03 | Approvals inbox for Manager and Admin |

**Menu by role:** Employee – Home, My Profile, Attendance, Leave, Salary. Manager – adds Approvals and My Team. Admin – Home, Approvals, Employees.

## 7. Screen states

| State | Behaviour |
| --- | --- |
| Empty | n/a (frame only) |
| Loading | Content area shows a loading indicator; header and menu stay usable |
| Validation error | n/a |
| System error | Content area shows an error panel with Retry; menu stays usable |
| Session expired | Redirect to SCR-SH-01 with message "Your session has expired. Please sign in again." |

## 8. Accessibility

Landmarks (`header`, `nav`, `main`); user menu is a keyboard-operable menu button with `aria-expanded`; visible focus outline; colour contrast at least 4.5:1; pending count is announced as part of the link name.

## 9. Open questions

| Id | Question | Owner | Status |
| --- | --- | --- | --- |
| UXQ-08 | Session idle timeout length | Product owner | Accepted (D-26) – 30 minutes |
