# PMS – HLD Part01a: Architecture Principles, Patterns & Decisions

Document ID: PMS-HLD-Part01a-Principles-Patterns-Decisions-v1.0
Project: Payroll Management System (PMS) – proof of concept (POC), Stage 3 Solution Design
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 23-Nov-2026 | Rajesh Verma | First draft of §1–§3, based on PMS-HLD-Part01-Architecture-and-Design v1.0 rev 0.8 (D-109 to D-116), the approved BRD set v1.0 (D-107) and ADR-001 to ADR-006 |

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | Rajesh Verma (Enterprise Architect) | 23-Nov-2026 | §1–§3 approved (D-117) |
| Product owner | Rajesh Verma | 23-Nov-2026 | §1–§3 approved (D-117) |

## 2. How to use this document

This document holds (a) the catalogue of architecture principles and patterns the PMS design is assessed against (§3–§4, referenced from PMS-HLD-Part01-Architecture-and-Design §4) and (b) the register and record format of architecture decisions (ADRs, §5–§6, referenced from Part01 §18). It is the second of the 14 HLD documents of Stage 3 (D-108) and closes Part01 open item OI-P01-01. For each catalogue row it records:

| Column | Meaning |
| --- | --- |
| Id | Stable id, used in HLDs, ADRs and reviews (e.g. AP-RES-03) |
| Applicability | **Applied** · **Partial** · **Deferred** (later phase) · **N/A** (with reason) |
| Realization | How the design meets it (component, setting, pattern), one line |
| Ref | Where it is designed: Part01 / Part02 / Part03 section, ADR, decision, standard |

**Reading rules for PMS**

- **Applied** – the POC design meets the item in full; detail may still be designed in a later HLD document or standard.
- **Partial** – the POC meets part of the item; the realization states which part, and the remainder is Deferred (Part01 §20.3) or an open item (§7).
- **Deferred** – not in the POC; planned for a later phase (Part01 §20.3 or the decision named in Ref).
- **N/A** – does not fit PMS; the reason is stated (assumption, constraint or decision).
- A row Deferred or N/A because of a decision references the ADR or decision id in Ref.
- Rows are never deleted; project-specific rows are added at the end of a group.
- Where Part01 §4 already states an item, this document uses the same reading.
- Ref values for documents not yet written: "Part02 (planned)", "Part03 (planned)" and "docs/04-standards/<area> (planned)", where <area> is one of the 12 standards areas of OBJ-06 (D-61): architecture-and-design, frontend-and-ux, api-and-integration, coding-and-code-review, database-and-data, security, logging-and-observability, performance-and-scalability, resilience-and-availability, testing-and-quality, devops-and-cicd, documentation-and-governance.
- The catalogue stays technology-neutral; a product is named only where Part01 §6.2, §7, §9.2 or §11 already names it.
- Items the design does not settle yet are recorded as open items OI-P01a-nn (§7) for the HLD document or standard that settles them; they are not decided here.

**Sources:**

- Cloud design patterns – Azure Architecture Center (https://learn.microsoft.com/en-us/azure/architecture/patterns/)
- Enterprise Integration Patterns – Hohpe & Woolf (https://www.enterpriseintegrationpatterns.com/patterns/messaging/)
- Microservice patterns – microservices.io (C. Richardson)
- Twelve-Factor App (12factor.net)
- Well-Architected Framework
- OWASP Top 10

The catalogue sources describe patterns only; they do not set the PMS platform (ADR-002).

## 3. Group summary

330 items in 18 groups. Counts per applicability are filled when the §4 group reviews are complete and are copied to Part01 §4.1.

| Group | Code | Rows | Applied | Partial | Deferred | N/A |
| --- | --- | --- | --- | --- | --- | --- |
| A. Architecture approach & governance | GOV | 11 | | | | |
| B. X-First principles | XF | 13 | | | | |
| C. Well-architected qualities | WA | 15 | | | | |
| D. Software design principles | SD | 19 | | | | |
| E. Twelve-Factor App | TF | 12 | | | | |
| F. Frontend & experience architecture | FE | 10 | | | | |
| G. Microservice design patterns | MS | 34 | | | | |
| H. Cloud design patterns | CP | 44 | | | | |
| I. Enterprise integration patterns | EIP | 64 | | | | |
| J. Integration principles | INT | 13 | | | | |
| K. Data architecture | DATA | 17 | | | | |
| L. Security architecture | SEC | 20 | | | | |
| M. Logging & observability | OBS | 12 | | | | |
| N. Performance & scalability | PERF | 10 | | | | |
| O. Resilience & availability | RES | 10 | | | | |
| P. DevOps & continuous delivery | DEV | 11 | | | | |
| Q. Testing & quality | QA | 10 | | | | |
| R. Delivery governance & knowledge management | DG | 5 | | | | |
| **Total** | | **330** | | | | |

Group R follows D-116: tool-neutral wording, ids AP-DG-01 to AP-DG-05, linked to OBJ-05, KPI-05 and OBJ-06 area 12.

## 4. Catalogue

To be drafted: groups A–F, then G–L, then M–R.

## 5. Architecture decision register (ADRs)

To be drafted.

## 6. ADR record format

To be drafted.

## 7. Open items

| Id | Open item | Catalogue ids | Owner | Due |
| --- | --- | --- | --- | --- |
| – | Filled during the §4 group reviews | | | |
