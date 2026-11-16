# <Project> – Business Requirements Document (BRD)

Document ID: <PRJ>-BRD-v<x.y>
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

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

<What this document defines and who uses it (design team, BMAD agents, QA).>

### 2.2 Reference documents

**Input documents**

| # | Document | Version | Use |
| --- | --- | --- | --- |
| 1 | UX Journey Index | v<x> | Journeys, screens, navigation |
| 2 | UX Summaries (per screen) | v<x> | Fields, actions, rules per screen |
| 3 | Decision log | D-01 to D-<nn> | Approved decisions |

**Downstream documents (consume this BRD)**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-AnD | Overall architecture and design |
| 2 | <PRJ>-HLD-Part02-M<n>-<MOD>-Functional | Solution approach per functional module |
| 3 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Solution approach for supporting modules |
| 4 | <PRJ>-HLD-Part03-Datamodel | Data model |

### 2.3 Glossary and abbreviations

| Term | Meaning |
| --- | --- |

### 2.4 Requirement ID conventions

| Prefix | Meaning | Example |
| --- | --- | --- |
| FR-<MOD>-<NNN> | Functional requirement of a module | FR-AMS-004 |
| BR-<MOD>-<NN> | Business rule (BR-CMN for cross-module) | BR-CMN-03 |
| VR-<MOD>-<NN> | Validation rule | VR-EIMS-02 |
| NFR-<NN> | Non-functional requirement | NFR-05 |
| NOT-<NN> | Notification requirement | NOT-03 |
| JOB-<NN> | Scheduled / backend job | JOB-02 |
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

## 4. Stakeholders, roles and access

### 4.1 Stakeholders

| Stakeholder | Interest / responsibility |
| --- | --- |

### 4.2 Roles

| Role id | Role name | Type (internal / system) | Description |
| --- | --- | --- | --- |

### 4.3 Role × screen access matrix

R = read, R/W = read and write, A = approve, — = no access.

| Screen id | Screen | <Role 1> | <Role 2> | <Role 3> |
| --- | --- | --- | --- | --- |

## 5. Business process and user journeys

### 5.1 End-to-end business process

<Diagram: main flow across modules, from onboarding to salary acceptance.>

### 5.2 User journeys

| Journey id | Journey | Actor | Screens | Requirement ids |
| --- | --- | --- | --- | --- |

## 6. Entity status lifecycles

Repeat 6.n per business entity. HLDs refer to this chapter for statuses.

### 6.1 <Entity> lifecycle

<State diagram.>

| Status code | Status | Business meaning | Set by |
| --- | --- | --- | --- |

| From | To | Action | Actor | Condition / rule |
| --- | --- | --- | --- | --- |

## 7. Functional requirements

Repeat 7.n per module and 7.n.m per screen or system function.

### 7.1 <Module code> – <Module name>

**Overview:** <one paragraph>

#### 7.1.1 <SCR-id> – <Screen / function name>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-<MOD>-001 | | Must | POC | SCR-<MOD>-01 | |

**User stories**

| Id | As a | I want to | So that |
| --- | --- | --- | --- |

## 8. Business rules

| Rule id | Rule | Applies to (module / screen) | Source (decision / UX) |
| --- | --- | --- | --- |

## 9. Data requirements

Repeat 9.n per entity.

### 9.1 <Entity>

| Attribute | Description | Type / format | Mandatory | Validation (VR id) | Set by |
| --- | --- | --- | --- | --- | --- |

## 10. Notifications and alerts

| Id | Event / trigger | Recipient(s) | Channel (in-app / email) | Timing | Message summary |
| --- | --- | --- | --- | --- | --- |

## 11. Integrations and scheduled jobs

| Id | Name | Type (event / API / scheduled) | Trigger / schedule | Source → target | Business outcome |
| --- | --- | --- | --- | --- | --- |

## 12. Reporting and dashboard

| Id | Report / widget | Audience | Content | Filters |
| --- | --- | --- | --- | --- |

## 13. Non-functional requirements

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

### 13.1 Business volumetrics (input to HLD)

| Volume type | Year 1 | Growth % per year |
| --- | --- | --- |
| Users | | |
| Transactions per year (by entity) | | |

## 14. Assumptions, constraints and dependencies

| Type | Id | Statement |
| --- | --- | --- |
| Assumption | A-01 | |
| Constraint | C-01 | |
| Dependency | DEP-01 | |

## 15. Risks

| Risk id | Risk | Likelihood | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |

## 16. Traceability matrix

| Journey id | Screen id | Req id | Rule ids | Test ref (later) |
| --- | --- | --- | --- | --- |

## 17. Open items

| Id | Question | Owner | Due | Status / decision |
| --- | --- | --- | --- | --- |

Approved decisions are kept in `docs/decisions/decision-log.md`.

## 18. Appendix

### 18.1 Future scope (not in this phase)

| Area | Requirement ref | Note |
| --- | --- | --- |
