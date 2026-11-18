# <Project> – Business Requirements Document (BRD) – Anchor

Document ID: <PRJ>-BRD-v<x.y>
Scope: business context, roles, end-to-end process, cross-module rules and system-wide NFRs; module requirements are in the module BRDs
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - This anchor holds what spans modules. Module requirements live only in <PRJ>-BRD-M<n>-<MOD> (one per functional module) and <PRJ>-BRD-M<n>-SUP (supporting functions); the anchor never repeats them.
> - Glossary, roles, cross-module rules (BR-CMN) and system-wide NFRs are defined here once and referenced from module BRDs.
> - The end-to-end business process stays whole and readable in §5.

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | First draft from UX v<x> |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | | | |
| Business analyst | | | |
| Business stakeholder | | | |

## 2. Introduction

### 2.1 Purpose

<What the BRD set defines and who uses it (business stakeholders, design team, BMAD agents, QA).>

### 2.2 Reference documents

**Input documents**

| # | Document | Version | Use |
| --- | --- | --- | --- |
| 1 | UX Journey Index | v<x> | Journeys, screens, navigation |
| 2 | UX Summaries (per screen) | v<x> | Fields, actions, rules per screen |
| 3 | Decision log | D-01 to D-<nn> | Approved decisions |

**Downstream documents (consume the BRD set)**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-Architecture-and-Design | Overall architecture and design |
| 2 | <PRJ>-HLD-Part02-Functional (anchor) and module / SUP documents | Functional design |
| 3 | <PRJ>-HLD-Part03-Datamodel (anchor) and module / SUP documents | Data model |

### 2.3 Module BRD documents

| Module | Document | Business owner / SME | Version | Status |
| --- | --- | --- | --- | --- |
| <MOD1> | <PRJ>-BRD-M1-<MOD1> | | | |
| SUP | <PRJ>-BRD-M<n>-SUP | | | |

### 2.4 Glossary and abbreviations

| Term | Meaning |
| --- | --- |

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

Priority uses MoSCoW (Must / Should / Could / Won't). Delivery phase: POC / Phase 2 / Future.

## 3. Business overview

### 3.1 Business background

<Business problem, current situation, why the system is needed.>

### 3.2 Business objectives

| # | Objective | Measure of success |
| --- | --- | --- |

### 3.3 Scope

| Module | In scope (POC) | Phase 2 / Future |
| --- | --- | --- |

**Out of scope**

- <item – reason>

## 4. Stakeholders and roles

### 4.1 Stakeholders

| Stakeholder | Interest / responsibility |
| --- | --- |

### 4.2 Role catalogue

| Role id | Role name | Type (internal / system) | Description | Data scope (own / reportees / all) |
| --- | --- | --- | --- | --- |

### 4.3 Role × module access

Screen-level access is in each module BRD §4.2. R = read, R/W = read and write, A = approve, — = no access.

| Module | <Role 1> | <Role 2> | <Role 3> |
| --- | --- | --- | --- |

## 5. End-to-end business process and journeys

### 5.1 End-to-end business process

<Diagram: the main business flow across modules, e.g. from onboarding to salary acceptance, showing which module owns each step.>

| Step | Business activity | Module | Actor | Outcome / hand-over | Module BRD ref |
| --- | --- | --- | --- | --- | --- |

### 5.2 Journey index

| Journey id | Journey | Actor | Module(s) | Module BRD ref |
| --- | --- | --- | --- | --- |

## 6. Cross-module business rules

| Rule id | Rule | Modules affected | Source (decision / UX) |
| --- | --- | --- | --- |
| BR-CMN-01 | | | |

## 7. Integrations and cross-module jobs

| Id | Name | Type (event / API / scheduled / external system) | Trigger / schedule | Source → target | Business outcome |
| --- | --- | --- | --- | --- | --- |

## 8. System-wide non-functional requirements

Module-specific NFRs are in each module BRD §13.

| NFR id | Category | Requirement | Measure / target |
| --- | --- | --- | --- |
| NFR-01 | Performance | | |
| NFR-02 | Availability | | |
| NFR-03 | Security | | |
| NFR-04 | Usability and accessibility | | |
| NFR-05 | Auditability | | |
| NFR-06 | Data integrity | | |
| NFR-07 | Scalability | | |
| NFR-08 | Maintainability / configurability | | |

### 8.1 Business volumetrics (input to HLD)

| Volume type | Year 1 | Growth % per year |
| --- | --- | --- |
| Users (by role) | | |
| Transactions per year (by module) | | |
| Peak periods (e.g. month-end payroll) | | |

## 9. Assumptions, constraints and dependencies

| Type | Id | Statement |
| --- | --- | --- |
| Assumption | A-01 | |
| Constraint | C-01 | |
| Dependency | DEP-01 | |

## 10. Risks

| Risk id | Risk | Likelihood | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |

## 11. Traceability roll-up

| Module | Journeys | Screens | Functional requirements | Rules | Coverage status |
| --- | --- | --- | --- | --- | --- |

## 12. Open items

| Id | Question | Owner | Due | Status / decision |
| --- | --- | --- | --- | --- |

Approved decisions are kept in `docs/decisions/decision-log.md`.

## 13. Appendix

### 13.1 Future scope (not in this phase)

| Area | Requirement ref | Note |
| --- | --- | --- |
