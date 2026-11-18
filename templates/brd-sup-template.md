# <Project> – BRD-M<n>: Supporting Functions (SUP)

Document ID: <PRJ>-BRD-M<n>-SUP-v<x.y>
Module: Supporting functions (Admin & master data, User & access, Authentication, Notification, Audit, Document)
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

> Template guidance
> - Requirements are written on a need basis only. Where an existing platform or product already provides a capability, record it in §3 and keep the section heading with "Provided by <product / service> – no project requirements beyond §3".
> - Roles and the role catalogue are in the anchor <PRJ>-BRD §4; module-specific notifications are in each module BRD §10. This document covers the shared capability behind them.
> - Requirement prefixes: ADM, UM, AUTH, NM, DM (e.g. FR-UM-003).

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | First draft |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | | | |
| Business analyst | | | |
| Security / IT owner | | | |

## 2. Introduction

### 2.1 Purpose

<What supporting capabilities this document covers and why.>

### 2.2 Reference documents

| # | Document | Version | Use |
| --- | --- | --- | --- |
| 1 | <PRJ>-BRD (anchor) | v<x> | Roles, cross-module rules, system-wide NFRs |
| 2 | Module BRDs <PRJ>-BRD-M1..M<n>-<MOD> | v<x> | Consumers of these capabilities |
| 3 | UX Journey Index and UX Summaries (admin / shell screens) | v<x> | Screens |
| 4 | Decision log | D-01 to D-<nn> | Approved decisions |

## 3. Need-basis assessment

| Capability | Needed? (Yes / No / Partial) | Provided by (existing capability) | Project requirements in | Consumer modules |
| --- | --- | --- | --- | --- |
| Admin functions & master data | | | §4 | |
| User & access management | | | §5 | |
| Authentication & session | | | §6 | |
| Notification engine | | | §7 | |
| Audit & activity log | | | §8 | |
| Document management | | | §9 | |

## 4. Admin functions and master data

<Lookups / valid values, configuration parameters, business calendar, domain masters, bulk load.>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-ADM-001 | | | | | |

## 5. User and access management

<User lifecycle (create, activate, deactivate), role assignment, reporting hierarchy (manager – reportee), delegation, access review.>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-UM-001 | | | | | |

## 6. Authentication and session

<Business-level policy only: who signs in how, MFA for which users / actions, session timeout, lockout, first-login steps. Architecture is in HLD Part01 §9.>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-AUTH-001 | | | | | |

## 7. Notification engine

<Channels, in-app bell and history, templates, user preferences, delivery and retry expectations, reminders and escalation. Individual notifications (NOT ids) are listed in module BRDs §10.>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-NM-001 | | | | | |

## 8. Audit and activity log

<Which actions and fields are audited, who can view history, retention, export.>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-ADM-1xx | | | | | |

## 9. Document management

<Attachments: allowed types, size, who can upload / view / remove, retention.>

| Req id | Requirement | Priority | Phase | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- | --- |
| FR-DM-001 | | | | | |

## 10. Business and validation rules

| Rule id | Rule | Type (business / validation) | Applies to | Source |
| --- | --- | --- | --- | --- |

## 11. Data requirements

| Entity | Attribute | Description | Type / format | Mandatory | Sensitive (Y / N) |
| --- | --- | --- | --- | --- | --- |

## 12. Non-functional requirements (supporting-specific)

| NFR id | Category | Requirement | Measure / target |
| --- | --- | --- | --- |

## 13. Traceability matrix

| Capability | Screen id | Req id | Rule ids | Test ref (later) |
| --- | --- | --- | --- | --- |

## 14. Open items

| Id | Question | Owner | Due | Status / decision |
| --- | --- | --- | --- | --- |
