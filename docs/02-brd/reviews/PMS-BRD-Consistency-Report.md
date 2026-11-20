# PMS – BRD Set Consistency Report

Document ID: PMS-BRD-CR-v1.0
Scope: consistency check of the PMS BRD set before stakeholder review (Stage 2 gate)
Project: Payroll Management System (PMS) – proof of concept (POC), Step 3 BRD
Author: Rajesh Verma (Enterprise Architect)
Date: November 2026

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | 20-Nov-2026 | Rajesh Verma | Consistency check of the BRD set; findings CC-01 to CC-28; editorial and content fixes applied; open item OI-12 raised (D-103) |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Product owner | Rajesh Verma | 20-Nov-2026 | Findings reviewed; fixes approved (D-103) |
| Business analyst | [BA] | | |

## 2. Scope and method

### 2.1 Documents checked

| Document | Version checked | Version after fixes |
| --- | --- | --- |
| PMS-BRD (anchor) | v1.0 rev 0.13 | v1.0 rev 0.14 |
| PMS-BRD-M1-EIMS | v1.0 rev 0.1 | v1.0 rev 0.2 |
| PMS-BRD-M2-AMS | v1.0 rev 0.1 | v1.0 rev 0.2 |
| PMS-BRD-M3-LMS | v1.0 rev 0.1 | v1.0 rev 0.2 |
| PMS-BRD-M4-SMS | v1.0 rev 0.1 | v1.0 rev 0.2 |
| PMS-BRD-M5-SUP | v1.0 rev 0.1 | v1.0 rev 0.2 |

Checked against: the UX Journey Index v1.0 (journeys, screens, navigation map, status lists), the decision log D-01 to D-102 and the BRD templates (anchor, module, supporting functions).

### 2.2 Checks performed

| # | Check | Result |
| --- | --- | --- |
| a | Ids: every FR, BR, VR, NFR, NOT, RPT, JOB, INT, US and OI id is unique and follows anchor §2.5; counts in anchor §2.3 and §11 match the module documents (FR numbering gaps are by design) | No duplicate ids; all counts match. Two prefixes in use were not defined in §2.5 and one example id did not exist (CC-02) |
| b | Cross-references: every cited id exists; no superseded reference | All cited ids exist; stale or incomplete references corrected (CC-06 to CC-10, CC-17, CC-21) |
| c | Coverage: each of the 30 journeys and 17 screens is assigned to exactly one BRD document and covered by at least one requirement | Complete: 30 journeys and 17 screens, each assigned once and covered |
| d | Decisions: every rule traces to an approved decision; later amendments reflected everywhere | Reconciliation voiding (D-90), Admin account and session rules (D-97), password rule (D-99) and D-70 wording now reflected in all documents (CC-04, CC-05, CC-07, CC-09, CC-10, CC-17, CC-26, CC-28) |
| e | Terms and status lists: glossary terms, role names, status codes and messages consistent and in line with the UX status lists | Consistent; differences in the UX documents are tracked as UX update open items (CC-12, CC-13) |
| f | Versions and references: revision rows, reference versions and open-item status current and the same wherever an item appears | Reference versions updated in all module documents; open-item due points and wording aligned (CC-01, CC-11, CC-15, CC-19, CC-22, CC-24, CC-27) |
| g | Customer-facing rules: author line; technology-neutral wording | Author line correct in all documents; no product names for the identity provider or other technology |

### 2.3 Classification

| Class | Meaning | Handling |
| --- | --- | --- |
| Editorial | Wording, stale reference, count | Fixed directly |
| Content | A requirement or rule changes | Proposed, fixed after product owner approval |
| Business question | Needs a business decision | Recorded as an open item in anchor §12 |

## 3. Summary

| Document | Editorial | Content | Business question | Total |
| --- | --- | --- | --- | --- |
| PMS-BRD (anchor) | 12 | 1 | 1 | 14 |
| PMS-BRD-M1-EIMS | 4 | – | – | 4 |
| PMS-BRD-M2-AMS | 3 | – | – | 3 |
| PMS-BRD-M3-LMS | 2 | – | – | 2 |
| PMS-BRD-M4-SMS | 3 | – | – | 3 |
| PMS-BRD-M5-SUP | 2 | – | – | 2 |
| **Total** | **26** | **1** | **1** | **28** |

All editorial and content findings are fixed. The business question is open item OI-12.

## 4. Findings

| Id | Document | Section | Item | Issue | Class | Fix / status |
| --- | --- | --- | --- | --- | --- | --- |
| CC-01 | PMS-BRD | §2.2 | Decision log reference | Range shown as D-01 to D-54 | Editorial | Now D-01 to D-103 – Fixed |
| CC-02 | PMS-BRD | §2.5 | Id conventions | US and OI prefixes used across the set but not defined; example NFR-SMS-01 does not exist | Editorial | US and OI rows added; example now NFR-EIMS-01; FR-ADM-1xx range noted – Fixed |
| CC-03 | PMS-BRD | §2.3 | SUP approval condition | SUP approval listed as pending OI-11, a UX update due before HLD Part02; no other module lists its UX update item | Content | SUP approval pending OI-02 and OI-04 only; OI-11 stays a pre-HLD item – Fixed (approved) |
| CC-04 | PMS-BRD | §2.4, §4.2, §7 | Voided, Reconciliation, SYS-REC, JOB-CMN-01 | Reconciliation described as only creating missed records and logging mismatches; it also voids records whose attendance is no longer Approved (D-90) | Editorial | Voiding added in all four places – Fixed |
| CC-05 | PMS-BRD | §2.4, §5.3 | Employee Id; FR-CMN-015 | Admin account exception (fixed user name, no Employee Id in the header, D-97) not stated | Editorial | Exception added with reference to FR-AUTH-024 and OI-11 – Fixed |
| CC-06 | PMS-BRD | §5.1 | Step 4 | Incomplete reference "BR-CMN" | Editorial | Now BR-CMN-09 – Fixed |
| CC-07 | PMS-BRD | §6 | BR-CMN-05 source | Cites D-02 (E2), replaced by D-70 | Editorial | Now "D-70 (replaces D-02 E2)" – Fixed |
| CC-08 | PMS-BRD | §5.3 | FR-CMN-004 | Missing-day rule does not cite open item OI-03 | Editorial | OI-03 added to the source – Fixed |
| CC-09 | PMS-BRD, PMS-BRD-M1-EIMS | §7, §11 | INT-08 | Outcome omits that deactivation and password reset end all sessions and a reset clears a lock (D-97) | Editorial | Effects added with FR-UM-006, FR-UM-007 – Fixed |
| CC-10 | PMS-BRD | §8 | NFR-03 | Password rule "not the Employee Id"; approved rule is "does not contain the Employee Id" and "differs from the current password" (D-97, D-99) | Editorial | Aligned with VR-AUTH-01 – Fixed |
| CC-11 | PMS-BRD | §12 | OI-02, OI-03, OI-04 | Due points refer to module BRDs already drafted; OI-02 wording omits the employee's own salary records awaiting acceptance or a dispute decision | Editorial | Due "Before BRD sign-off (Stage 2 gate)"; OI-02 wording widened – Fixed |
| CC-12 | PMS-BRD | §12 | OI-01 | UX Journey Index actor and screen-role columns also show "Manager" only for the reviews the Admin performs for the top-level employee | Editorial | Added to OI-01 – Fixed |
| CC-13 | PMS-BRD | §12 | OI-06 | The 17 UX summaries still show "0.1 / Draft – in review" although approved with the UX set (D-34) | Editorial | Added to OI-06 – Fixed |
| CC-14 | PMS-BRD | §2.4, §6 | Top-level employee (BR-CMN-01) | Text assumes one top-level employee; nothing limits "None – top-level" to one (FR-EIMS-014, VR-EIMS-05, BR-LMS-09) | Business question | Open item OI-12 raised (HR Manager); added to the EIMS and LMS approval conditions – Open |
| CC-15 | PMS-BRD-M1-EIMS | §1.1, §2.2 | References | Anchor rev 0.3 and D-01 to D-72 | Editorial | Anchor rev 0.14, D-01 to D-103, rev 0.2 row – Fixed |
| CC-16 | PMS-BRD-M1-EIMS | §8 | Cross-module rules | BR-CMN-19 (audit log) not listed | Editorial | Added – Fixed |
| CC-17 | PMS-BRD-M1-EIMS | §7.1, §7.2, §15 | FR-EIMS-005, FR-EIMS-018 | No link to FR-UM-006 / FR-UM-007 (D-97); acceptance said any sign-in attempt shows the inactive message, approved rule shows it only after the correct password | Editorial | Links added; acceptance corrected; traceability rows updated – Fixed |
| CC-18 | PMS-BRD-M1-EIMS | §16 | Open items | OI-11 (UX summaries SCR-EIMS-01, SCR-EIMS-02) not listed | Editorial | Added, with OI-12 – Fixed |
| CC-19 | PMS-BRD-M2-AMS | §1.1, §2.2 | References | Anchor rev 0.5 and D-01 to D-77 | Editorial | Anchor rev 0.14, D-01 to D-103, rev 0.2 row – Fixed |
| CC-20 | PMS-BRD-M2-AMS | §8 | Cross-module rules | BR-CMN-11, 14, 19 not listed although AMS is affected | Editorial | Added – Fixed |
| CC-21 | PMS-BRD-M2-AMS | §4.2, §16 | OI-01 | Admin access to SCR-AMS-03 for the top-level employee not noted (LMS and SMS note it) | Editorial | Note and open item added – Fixed |
| CC-22 | PMS-BRD-M3-LMS | §1.1, §2.2 | References | Anchor rev 0.7 and D-01 to D-84 | Editorial | Anchor rev 0.14, D-01 to D-103, rev 0.2 row – Fixed |
| CC-23 | PMS-BRD-M3-LMS | §8 | Cross-module rules | BR-CMN-11, 14, 19 not listed although LMS is affected | Editorial | Added – Fixed |
| CC-24 | PMS-BRD-M4-SMS | §1.1, §2.2 | References | Anchor rev 0.9 and D-01 to D-90 | Editorial | Anchor rev 0.14, AMS rev 0.2, D-01 to D-103, rev 0.2 row – Fixed |
| CC-25 | PMS-BRD-M4-SMS | §8 | Cross-module rules | BR-CMN-11, 14, 19 not listed although SMS is affected | Editorial | Added – Fixed |
| CC-26 | PMS-BRD-M4-SMS | §6.1 | Status VOIDED | Meaning names only the reopen; reconciliation also voids (D-90) | Editorial | Reconciliation added – Fixed |
| CC-27 | PMS-BRD-M5-SUP | §1.1, §2.2 | References | Anchor rev 0.12 and D-01 to D-101 | Editorial | Anchor rev 0.14, module BRDs rev 0.2, D-01 to D-103, rev 0.2 row – Fixed |
| CC-28 | PMS-BRD-M5-SUP | §6.2 | FR-AUTH-012 | "Not the Employee Id" while VR-AUTH-01 and the acceptance criterion say "does not contain" (D-99) | Editorial | Now "not containing the Employee Id (D-28, D-99)" – Fixed |

## 5. Open items raised

| Id | Question | Owner | Due | Status |
| --- | --- | --- | --- | --- |
| OI-12 | May more than one employee have no manager ("None – top-level")? If yes, the Admin approves all their records and "Also away" stays empty for each; if no, onboarding and manager changes must refuse a second top-level employee | HR Manager | Before BRD sign-off (Stage 2 gate) | Open – prepared for decision in PMS-BRD-Open-Items-Note |

Open items blocking BRD approval after this check: OI-02, OI-03, OI-04, OI-12 (anchor §12) and OI-EIMS-01, OI-EIMS-02 (PMS-BRD-M1-EIMS §16). UX update items OI-01 and OI-06 to OI-11 are due before HLD Part02.
