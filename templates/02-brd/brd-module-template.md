# <Project> – BRD-M<n>: <Module name> (<MOD>)

Document ID: <PRJ>-BRD-M<n>-<MOD>-v<x.y>
Module: <Module name> (<MOD>)
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - One document per functional module. Glossary, role catalogue, cross-module rules (BR-CMN), end-to-end process and system-wide NFRs are in the anchor <PRJ>-BRD; reference them, do not repeat.
> - Supporting functions (users, login, notifications engine, audit, master data, documents) are in <PRJ>-BRD-M<n>-SUP.
> - HLD documents refer to this document's §4.2 (access), §6 (status lifecycle), §7–§8 (requirements and rules), §9 (data), §10 (notifications) and §13 (NFRs).

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
| Module business owner / SME | | | |

## 2. Introduction

### 2.1 Purpose

<What this module BRD defines.>

### 2.2 Reference documents

| # | Document | Version | Use |
| --- | --- | --- | --- |
| 1 | <PRJ>-BRD (anchor) | v<x> | Glossary, roles, end-to-end process, cross-module rules, system-wide NFRs |
| 2 | UX Journey Index and UX Summaries for <MOD> | v<x> | Journeys, screens, fields, actions |
| 3 | Decision log | D-01 to D-<nn> | Approved decisions |

## 3. Module overview and scope

### 3.1 Overview

<What the module does, for whom, and its part in the end-to-end process (anchor §5.1 steps).>

### 3.2 Scope

| In scope (POC) | Phase 2 / Future | Out of scope (reason) |
| --- | --- | --- |

### 3.3 Hand-overs with other modules

| Direction (in / out) | Other module | What is handed over | When | Anchor rule / process ref |
| --- | --- | --- | --- | --- |

## 4. Users and access

### 4.1 Users of this module

| Role id (anchor §4.2) | What they do in this module |
| --- | --- |

### 4.2 Role × screen access matrix

R = read, R/W = read and write, A = approve, — = no access.

| Screen id | Screen | <Role 1> | <Role 2> | <Role 3> | Data scope |
| --- | --- | --- | --- | --- | --- |

## 5. User journeys and screens

| Journey id | Journey | Actor | Screens | Requirement ids |
| --- | --- | --- | --- | --- |

## 6. Status lifecycle

Repeat 6.n per business entity of the module. HLDs refer to this chapter for statuses.

### 6.1 <Entity> lifecycle

<State diagram.>

| Status code | Status | Business meaning | Set by |
| --- | --- | --- | --- |

| From | To | Action | Actor | Condition / rule |
| --- | --- | --- | --- | --- |

## 7. Functional requirements

Repeat 7.n per screen or system function.

### 7.1 <SCR-id> – <Screen / function name>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-<MOD>-001 | | Must | POC | SCR-<MOD>-01 | |

**User stories**

| Id | As a | I want to | So that |
| --- | --- | --- | --- |

## 8. Business and validation rules

| Rule id | Rule | Type (business / validation) | Applies to (screen / function) | Source (decision / UX) |
| --- | --- | --- | --- | --- |

Cross-module rules that also apply: <BR-CMN ids from anchor §6>

## 9. Data requirements

Repeat 9.n per entity.

### 9.1 <Entity>

| Attribute | Description | Type / format | Mandatory | Validation (VR id) | Set by | Sensitive (Y / N) |
| --- | --- | --- | --- | --- | --- | --- |

## 10. Notifications and alerts

| Id | Event / trigger | Recipient(s) | Channel (in-app / email) | Timing | Message summary |
| --- | --- | --- | --- | --- | --- |
| NOT-<MOD>-01 | | | | | |

## 11. Scheduled jobs and integrations

| Id | Name | Type (event / API / scheduled) | Trigger / schedule | Source → target | Business outcome |
| --- | --- | --- | --- | --- | --- |

## 12. Reporting and dashboard

| Id | Report / widget | Audience | Content | Filters |
| --- | --- | --- | --- | --- |

## 13. Module non-functional requirements and volumetrics

System-wide NFRs (anchor §8) apply; list only module-specific additions.

| NFR id | Category | Requirement | Measure / target |
| --- | --- | --- | --- |
| NFR-<MOD>-01 | | | |

| Volume type | Year 1 | Growth % per year | Peak |
| --- | --- | --- | --- |

## 14. Assumptions, constraints and dependencies

| Type | Id | Statement |
| --- | --- | --- |

## 15. Traceability matrix

| Journey id | Screen id | Req id | Rule ids | Test ref (later) |
| --- | --- | --- | --- | --- |

## 16. Open items

| Id | Question | Owner | Due | Status / decision |
| --- | --- | --- | --- | --- |

## 17. Appendix

### 17.1 Future scope (not in this phase)

| Area | Requirement ref | Note |
| --- | --- | --- |
