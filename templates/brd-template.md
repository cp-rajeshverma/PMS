# <Project> – Business Requirements Document (BRD)

## 1. Document control

| Field | Value |
| --- | --- |
| Document | Business Requirements Document |
| Version | 0.1 |
| Status | Draft / In review / Approved |
| Product owner | <name> |
| Business analyst | <name> |
| Inputs | UX Journey Index v<x>, UX summaries v<x> |
| Last updated | <yyyy-mm-dd> |

| Version | Date | Author | Change |
| --- | --- | --- | --- |
| 0.1 | <date> | <name> | First draft |

## 2. Purpose and objectives

<Why the system is being built. Numbered business objectives, each measurable where possible.>

## 3. Scope

### 3.1 In scope

| Module | Capabilities |
| --- | --- |

### 3.2 Out of scope

- <item, with reason or target phase>

## 4. Stakeholders and roles

| Stakeholder / role | Responsibility | Interest |
| --- | --- | --- |

### 4.1 Permissions matrix

| Action | <Role 1> | <Role 2> | <Role 3> |
| --- | --- | --- | --- |

## 5. User journeys

| Journey Id | Journey | Actor | Screens | Requirement Ids |
| --- | --- | --- | --- | --- |

## 6. Functional requirements

Repeat 6.n for each module.

### 6.1 <Module name>

**Overview:** <one paragraph>

| Req Id | Requirement | Priority (MoSCoW) | UX ref | Acceptance criteria (Given / When / Then) |
| --- | --- | --- | --- | --- |
| FR-<MOD>-01 | | Must | SCR-<MOD>-01 | |

**User stories**

| Id | As a | I want to | So that |
| --- | --- | --- | --- |

## 7. Business rules

| Rule Id | Rule | Applies to | Source |
| --- | --- | --- | --- |
| BR-<AREA>-01 | | | |

## 8. Data requirements

Repeat 8.n per entity.

### 8.1 <Entity>

| Attribute | Description | Type | Required | Validation | Owner (who sets it) |
| --- | --- | --- | --- | --- | --- |

## 9. Non-functional requirements

| NFR Id | Category | Requirement | Measure / target |
| --- | --- | --- | --- |
| NFR-01 | Performance | | <e.g. p95 API < 500 ms> |
| NFR-02 | Security | | |
| NFR-03 | Availability | | |
| NFR-04 | Usability / accessibility | | |
| NFR-05 | Audit and compliance | | |
| NFR-06 | Scalability | | |

## 10. Integrations and scheduled jobs

| Id | Name | Type (event / API / scheduled) | Trigger | Producer → consumer | Business outcome |
| --- | --- | --- | --- | --- | --- |

## 11. Assumptions, constraints and dependencies

| Type | Id | Statement |
| --- | --- | --- |
| Assumption | A-01 | |
| Constraint | C-01 | |
| Dependency | DEP-01 | |

## 12. Risks

| Risk Id | Risk | Likelihood | Impact | Mitigation | Owner |
| --- | --- | --- | --- | --- | --- |

## 13. Traceability matrix

| Journey Id | Screen Id | Req Id | Business rule Ids | Test ref (later) |
| --- | --- | --- | --- | --- |

## 14. Glossary

| Term | Meaning |
| --- | --- |

## 15. Open items

| Id | Question | Owner | Due | Status / decision |
| --- | --- | --- | --- | --- |

Decisions are recorded in `docs/decisions/decision-log.md`.

## 16. Sign-off

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | | | |
| Business analyst | | | |
