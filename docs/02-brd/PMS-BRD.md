# PMS – Business Requirements Document (BRD) – Anchor

Document ID: PMS-BRD-v1.0
Scope: business context, roles, end-to-end process, cross-module rules and system-wide NFRs; module requirements are in the module BRDs
Project: Payroll Management System (PMS) – proof of concept (POC), Step 3 BRD
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 18-Nov-2026 | Rajesh Verma | First draft from UX v1.0 (D-34), BRD v1.0 baseline (D-09) and decisions D-01 to D-54 |

### 1.2 Review and approval

Names are added when the customer shares them.

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | Rajesh Verma | | |
| Business analyst | [BA] | | |
| Business stakeholder | [HR Manager] | | |
| Business stakeholder | [Finance Manager] | | |

## 2. Introduction

### 2.1 Purpose

The PMS BRD set defines what the Payroll Management System POC must do, for whom and under which business rules. It turns the approved UX (Step 2) and the approved decisions into traceable, numbered requirements.

This anchor holds everything that spans modules: business context, roles, the end-to-end process, cross-module rules (BR-CMN), integrations, system-wide NFRs, risks and the traceability roll-up. Module requirements are only in the module BRDs (§2.3); the anchor does not repeat them.

Users of the BRD set:

- Business stakeholders (HR Manager, Finance Manager) – confirm and approve the requirements.
- Design team – input to the HLD set (Part01, Part01a, Part02, Part03).
- Development team – basis for epics, stories, code and documentation (D-14).
- QA – basis for test scenarios and UAT.

### 2.2 Reference documents

**Input documents**

| # | Document | Version | Use |
| --- | --- | --- | --- |
| 1 | UX Journey Index (`docs/01-ux/ux-journey-index.md`) | v1.0, approved (D-34) | Journeys, screens, navigation, status lists |
| 2 | UX Summaries (`docs/01-ux/ux-summary/*.md`, 17 screens) | v0.1, approved with the UX set (D-34) | Fields, actions, rules per screen |
| 3 | UX mockups (`docs/01-ux/mockups/*.html`, 17 screens) | approved (D-34) | Screen behaviour and layout |
| 4 | PMS – Business Requirements Document (baseline) | v1.0 (D-09) | Input only; content redistributed into this BRD set (D-53) |
| 5 | Decision log (`docs/decisions/decision-log.md`) | D-01 to D-54 | Approved decisions |
| 6 | ADR-001 Frontend composition (`docs/decisions/adr/`) | Accepted (D-23) | Shell and module frontend constraint |

**Downstream documents (consume the BRD set)**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | PMS-HLD-Part01-Architecture-and-Design | Overall architecture and design |
| 2 | PMS-HLD-Part01a-Principles-Patterns-Decisions | Principles, patterns, ADR register |
| 3 | PMS-HLD-Part02-Functional (anchor) and module / SUP documents | Functional design |
| 4 | PMS-HLD-Part03-Datamodel (anchor) and module / SUP documents | Data model |

### 2.3 Module BRD documents

| Module | Document | Business owner / SME | Version | Status |
| --- | --- | --- | --- | --- |
| EIMS – Employee Information | PMS-BRD-M1-EIMS | HR Manager, Finance Manager | – | Not started |
| AMS – Attendance | PMS-BRD-M2-AMS | HR Manager, Finance Manager | – | Not started |
| LMS – Leave | PMS-BRD-M3-LMS | HR Manager, Finance Manager | – | Not started |
| SMS – Salary | PMS-BRD-M4-SMS | HR Manager, Finance Manager | – | Not started |
| SUP – Supporting functions | PMS-BRD-M5-SUP | HR Manager, Finance Manager | – | Not started (need-basis assessment after M1–M4, D-53) |

### 2.4 Glossary and abbreviations

| Term | Meaning |
| --- | --- |
| PMS | Payroll Management System |
| POC | Proof of concept |
| EIMS / AMS / LMS / SMS | Employee Information / Attendance / Leave / Salary Management System |
| SUP | Supporting functions: ADM (administration), UM (user management), AUTH (authentication), NM (notifications), DM (document management) |
| Shell | The single web app that hosts every module screen: login, dashboard, approvals inbox, menu (ADR-001) |
| Employee Id | System-generated unique id (EMP0001, EMP0002, …); also the sign-in user name |
| Manager Id | Employee Id of an employee's manager, set by Admin; the manager approves the employee's records |
| Top-level employee | Employee with no manager ("None – top-level"); Admin approves their records |
| Direct report | Employee whose Manager Id is the given manager |
| Admin | System role that onboards and maintains employees; has no personal records (D-24) |
| Temporary password | Password issued by the system at onboarding or Admin reset; must be replaced at next sign-in |
| Approved-profile snapshot | Last approved version of an employee profile, used by other modules while a change is being re-approved (D-29) |
| Hourly Wage Rate | Wage per hour in INR, set by Admin on the employee |
| Day Hour | Hours worked on a day (To Time – From Time) |
| Day Wage Amount | Day Hour × Hourly Wage Rate, rounded to 2 decimals, INR |
| Salary record | One record per approved attendance day, holding hours, rate and wage |
| Generated / Manager Approved / Accepted / Disputed / Voided | Salary statuses; Voided is set only by the system when the linked attendance is reopened (D-25) |
| Keep as is | Manager closes a salary dispute without change, with an explanation; record returns to Manager Approved (D-33) |
| Reopen attendance | Manager returns approved attendance to the employee after a salary dispute; the salary record is voided (D-07, D-25) |
| Cancelled | Leave status for a request the employee withdrew while Submitted (D-32) |
| Reconciliation | Nightly job (01:00 IST) that creates missed salary records and logs mismatches (D-24) |
| Soft delete | Record marked inactive (Is Active = false); never physically deleted |
| IST / INR | Indian Standard Time / Indian Rupee |

### 2.5 Requirement ID conventions

| Prefix | Meaning | Example |
| --- | --- | --- |
| FR-<MOD>-<NNN> | Functional requirement of a module (supporting: ADM, UM, AUTH, NM, DM) | FR-AMS-004 |
| BR-<MOD>-<NN> | Business rule (BR-CMN for cross-module, defined in this anchor) | BR-CMN-03 |
| VR-<MOD>-<NN> | Validation rule | VR-EIMS-02 |
| NFR-<NN> | System-wide non-functional requirement (this anchor) | NFR-05 |
| NFR-<MOD>-<NN> | Module-specific non-functional requirement | NFR-SMS-01 |
| NOT-<MOD>-<NN> | Notification requirement | NOT-LMS-03 |
| JOB-<MOD>-<NN> | Scheduled / backend job (JOB-CMN for cross-module) | JOB-CMN-01 |
| UJ-…, SCR-… | User journey / screen ids from UX | UJ-AMS-01, SCR-AMS-02 |

Priority uses **MoSCoW (Must / Should / Could / Won't)** . Delivery phase: POC / Phase 2 / Future.

**Mapping from the BRD v1.0 baseline ids**

Baseline ids are renumbered to this convention. The old id is kept in the "Source" column of each requirement so the history stays traceable.

| Baseline id | New id | Where |
| --- | --- | --- |
| BR-C1 to BR-C8 | BR-CMN-01 to BR-CMN-08 (same order) | This anchor §6 |
| EIMS-V1 to EIMS-V6 | VR-EIMS-01 to VR-EIMS-06 | PMS-BRD-M1-EIMS |
| AMS-V1 to AMS-V5 | VR-AMS-01 to VR-AMS-05 | PMS-BRD-M2-AMS |
| LMS-V1 to LMS-V6 | VR-LMS-01 to VR-LMS-06 | PMS-BRD-M3-LMS |
| SMS-R1 to SMS-R4 | BR-SMS-01 to BR-SMS-04 | PMS-BRD-M4-SMS |
| EIMS-US*, AMS-US*, LMS-US*, SMS-US* | FR-<MOD>-<NNN> (mapping table in each module BRD) | Module BRDs |
| C1–C5, E1–E3, A1–A3, L1–L4, S1–S6, O1–O6 | Not renumbered; cited through their decisions D-01 to D-07 | Decision log |

## 3. Business overview

### 3.1 Business background

PMS is a lightweight payroll application built as a proof of concept (D-06). Its main purpose is to prove a modern, governed end-to-end delivery approach, from requirements through go-live, with a formal approval gate at each step (D-13, D-14).

The business scope is the core of hourly payroll for a single company in India (D-08): keep verified employee master data, record daily attendance and leave, and calculate daily wages automatically from approved attendance. Every record is entered by the employee and approved by the manager, and the employee confirms the resulting wage, so no wage is ever entered by hand.

The application is deliberately small – four functional modules, each a separate service with its own database (D-10) – but every architecture, design and SDLC standard applies in full, so the result can serve as a reusable reference.

### 3.2 Business objectives

| # | Objective | Measure of success |
| --- | --- | --- |
| OBJ-01 | Keep employee master data, submitted by the employee and approved by the manager | All EIMS journeys pass UAT (KPI-01); no profile reaches Approved without an approver (KPI-03) |
| OBJ-02 | Record daily attendance, submitted by the employee and approved by the manager | All AMS journeys pass UAT (KPI-01); no attendance reaches Approved without an approver (KPI-03) |
| OBJ-03 | Manage leave requests, raised by the employee and approved by the manager | All LMS journeys pass UAT (KPI-01); no leave reaches Approved without an approver (KPI-03) |
| OBJ-04 | Calculate daily wages automatically from approved attendance, approved by the manager and reviewed by the employee | Wage accuracy (KPI-02); salary completeness after reconciliation (KPI-04) |
| OBJ-05 | Run every delivery step with a formal review and approval gate at the end of each step | Gate and traceability measure (KPI-05) |
| OBJ-06 | Produce a reusable set of standards and guardrails covering: (1) architecture and design; (2) frontend and UX, including accessibility; (3) API and integration (contract-first, events); (4) coding and code review; (5) database and data management, including data privacy; (6) security (identity, secrets, secure coding); (7) logging and observability; (8) performance and scalability; (9) resilience and availability; (10) testing and quality; (11) DevOps, CI/CD and deployment (environments, branching, release); (12) documentation, traceability and delivery governance | All 12 standards approved at their gate (KPI-05) |
| OBJ-07 | Keep the application small: four functional modules, one business entity per module (D-06, D-10) | Four module services delivered within the agreed scope (§3.3) |

**Measures of success (KPIs)**

| KPI | Measure | Target |
| --- | --- | --- |
| KPI-01 | User journeys (UJ-*) passing UAT end to end with the seeded sample data | 100 % of the 30 journeys; 100 % of Must requirements |
| KPI-02 | Salary records whose Day Wage Amount = Day Hour × Hourly Wage Rate (2 decimals) | 100 %; zero manual wage entries |
| KPI-03 | Records approved without an approver, or with missing audit fields | 0 |
| KPI-04 | Approved attendance days without exactly one non-voided salary record after the nightly reconciliation | 0 mismatches |
| KPI-05 | Delivery steps closed with a recorded approval in the decision log, with BRD → HLD → code → test traceability | 100 % of steps |

### 3.3 Scope

| Module | In scope (POC) | Phase 2 / Future |
| --- | --- | --- |
| Shell (common) | Login, set / change password, dashboard per role, approvals inbox, role-based menu | Future: runtime micro-frontends instead of build-time packages (ADR-001) |
| EIMS – Employee Information | Admin onboarding (Employee Id and temporary password), profile complete / submit / approve, re-approval on edit, Admin-owned fields (role, manager, rate, date of joining), deactivation, password reset, employee directory | – |
| AMS – Attendance | Daily attendance entry (15-minute steps), submit, approve / reject, reopen after a salary dispute, month calendar and list | Future: shifts, breaks, overnight work, biometric or clock-in integration |
| LMS – Leave | Full-day Casual / Sick / Earned leave, submit, cancel while Submitted, approve / reject, past and future dates | Future: leave balances, accruals and entitlement checks; half-day leave |
| SMS – Salary | Automatic daily wage from approved attendance, manager approval, employee accept (single or several) or dispute, keep as is or reopen, earnings for a period | Future: paid leave in salary; statutory deductions (PF, ESI, PT, TDS); allowances; payslips; monthly payroll runs |
| SUP – Supporting functions | UM (users and roles in Keycloak) and AUTH (sign-in, temporary and own passwords, password policy, lockout, idle timeout) | Phase 2: ADM (configuration and master data), NM (email / SMS notifications), DM (documents) |

**Out of scope**

- Leave balances, accruals, entitlement checks and half-day leave – deferred; leave is recorded only (D-04).
- Paid leave in salary – approved leave earns no wage in the POC (D-05).
- Statutory deductions (PF, ESI, PT, TDS), allowances, payslips, monthly payroll runs – payroll is limited to daily wages.
- Shifts, breaks, overnight work, biometric or clock-in integration – one same-day entry per day (D-03).
- Holiday calendar and weekend rules – any date may carry attendance or leave (D-08).
- Single sign-on, multi-company, multi-currency – single company, INR only (D-08).
- Email or SMS notifications – the POC uses dashboard reminders only; NM is Phase 2.
- Self-service password reset – Admin resets passwords (D-07).
- Personal records for Admin – Admin is a system role only (D-24).
- Withdrawal of submitted attendance, leave reason and leave drafts, auto-accept of salary records – kept out to keep the POC simple (D-31, D-32, D-33).

All out-of-scope items are deferred, not rejected.

## 4. Stakeholders and roles

_Pending – drafted after review of §1–§3._

## 5. End-to-end business process and journeys

_Pending._

## 6. Cross-module business rules

_Pending._

## 7. Integrations and cross-module jobs

_Pending._

## 8. System-wide non-functional requirements

_Pending._

## 9. Assumptions, constraints and dependencies

_Pending._

## 10. Risks

_Pending._

## 11. Traceability roll-up

_Pending._

## 12. Open items

_Pending._

Approved decisions are kept in `docs/decisions/decision-log.md`.

## 13. Appendix

_Pending._
