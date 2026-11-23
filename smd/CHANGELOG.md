# SMD changelog

## 2026-11-23 19:03 IST – refresh (HLD Part02 Functional anchor all sections approved)

- Refreshed from commit `7aff5c1` (8 commits since `9b0ead9`: `a208701` to `7aff5c1`); clean working tree.
- **Stage 3 Solution Design In Progress, 15% → 20%**: PMS-HLD-Part02-Functional (anchor) drafted and reviewed section by section (D-122 to D-125), v1.0 rev 0.4 – 77 system functions, cross-module flows XF-01 to XF-09, common API, event, error, audit and frontend conventions, coverage of all 175 functional requirements; HLD Part01a rev 0.6; ADR-006 follow-up on event ordering. Step S3.2 In Progress (module documents not started); final approval at the Stage 3 gate.
- Health **Green** (unchanged): no Critical or High findings open; Stage 3 on plan.
- Findings: OI-P01a-03 and OI-P01a-06 closed; OI-P02-01 and OI-P02-02 added (Low, for the module documents). New review RV-14; milestone M3.0d completed. BRD → HLD Part02 coverage 175 / 175 requirements assigned.
- Data: 55 artifacts (46 approved, 3 in review), 131 decisions / ADRs (+4), 41 open items / findings (17 open), 14 reviews (+RV-14), 8 risks, 89 linked repository files (+1).
- Warnings: HLD Part01 §8.2 row 11 to be aligned with the Part02 anchor at the set consistency check; Stage 7 step S7.2 still names the former cloud target. Customer-facing filtering: 40 texts neutralised (+3).

## 2026-11-23 13:20 IST – refresh (HLD Part01a all sections approved)

- Refreshed from commit `9b0ead9` (9 commits since `3efd265`: `09f23ac` to `9b0ead9`); clean working tree.
- **Stage 3 Solution Design In Progress, 10% → 15%**: PMS-HLD-Part01a-Principles-Patterns-Decisions drafted and reviewed section by section (D-117 to D-121), v1.0 rev 0.5 – 330 catalogue items assessed (230 Applied, 35 Partial, 3 Deferred, 62 N/A), ADR register ADR-001 to ADR-006; HLD Part01 rev 0.7 → 0.9 (group R renamed, D-116; §4.1 counts, D-121). Step S3.1 completed; final approval of both at the Stage 3 gate.
- Health **Green** (unchanged): no Critical or High findings open; Stage 3 on plan.
- Findings: OI-P01-01 closed; OI-P01a-01 to 17 added (Low, for the standards and the HLD Part02 anchor). New review RV-13; milestone M3.0c completed.
- Data: 54 artifacts (46 approved, 2 in review), 127 decisions / ADRs (+6), 39 open items / findings (17 open), 13 reviews (+RV-13), 8 risks, 88 linked repository files (+1), 0 broken links.
- Warnings: Stage 7 step S7.2 still names the former cloud target (renaming proposed). Customer-facing filtering: 37 texts neutralised (+2).

## 2026-11-22 23:30 IST – correction (configuration fixes; D-115)

- Configuration: HLD open items now feed the findings list (`docs/03-hld/*.md#Open items`); the neutral pattern is limited to usage-logging wording, so security terms in the HLD and ADR titles are shown as written; internal prompt and screenshot folders excluded.
- Findings: OI-P01-01 to OI-P01-06 added (1 open, Low; 5 closed). ADR-003 and ADR-004 titles shown as written.
- D-115: PostgreSQL 18 in every environment, matching Amazon RDS; HLD Part01 rev 0.7. Health Green (unchanged).
- Data: 121 decisions / ADRs, 22 open items / findings (1 open), 0 broken links.

## 2026-11-22 22:46 IST – refresh (Stage 3 started; HLD Part01 all sections approved)

- Refreshed from commit `f45c9d4` (15 commits since `fd2e5eb`: `10e70d5` to `f45c9d4`); working tree holds staged, uncommitted renames of internal working files outside this view.
- **Stage 3 Solution Design Not Started → In Progress, 0% → 10%**: stage plan (D-108) – planned 23 Nov – 11 Dec 2026, target go-live 29 Jan 2027; PMS-HLD-Part01-Architecture-and-Design drafted, all 20 sections approved section by section (D-109 to D-113), open items updated (D-114), v1.0 rev 0.6, final approval at the Stage 3 gate.
- Health **Green** (unchanged): no Critical or High findings open; Stage 3 on plan.
- New: ADR-002 to ADR-006; review RV-12 (HLD Part01 section reviews); milestones M3.0 and M3.0b completed.
- Data: 54 artifacts (46 approved), 120 decisions / ADRs (+12), 12 reviews (+RV-12), 16 BRD findings (0 open), 8 risks, 87 linked repository files (+6), 0 broken links.
- Warnings: HLD open items not yet in the findings feed (mapping line proposed); neutral pattern too broad for security wording (narrowing proposed); internal prompt folders still to be excluded. Customer-facing filtering: 35 texts neutralised (+3).

## 2026-11-21 – correction (no new refresh)

- Stage 2 milestones completed: consistency check and business open items (D-103, D-104), UX set v1.1 (D-105), BRD set signed off (D-107); the Overview "Done" list now shows them.
- Template fix: the internal-section marker no longer shows as text above the token card; removing everything between the TK-START and TK-END markers still leaves a working page.

## 2026-11-21 14:52 IST – refresh (Stage 2 BRD completed; gate passed)

- Refreshed from commit `fd2e5eb` (4 commits since `21aa65f`: `d42c33f` to `fd2e5eb`); clean working tree.
- **Stage 2 BRD Completed, 85% → 100%; gate Passed (D-107)**: UX set v1.1 (D-105), stakeholder review approved (D-106, sample reviewer names for the POC), BRD set signed off as approved baseline v1.0. Current stage moves to 3 (Solution Design).
- Health **Green** (unchanged): no open findings or open items.
- Findings: OI-01, OI-06 to OI-11 and F-SMD-01 closed (D-105). Risk R-07 mitigated (Low).
- Data: 49 artifacts (41 approved), 108 decisions / ADRs (+3), 16 open items / findings (0 open), 11 reviews (+RV-10, RV-11), 8 risks, 81 linked repository files (65 refreshed), 0 broken links.
- Warnings: folder docs/02-brd/reviews/ still not mapped (mapping line proposed); sample reviewer names noted. Customer-facing filtering: 32 texts neutralised (+3).

## 2026-11-20 23:19 IST – refresh (BRD consistency check; business open items decided)

- Refreshed from commit `21aa65f` (5 commits since `b4e141a`: `637739a` to `21aa65f`); clean working tree.
- **Stage 2 BRD In Progress, 80% → 85%**: BRD set consistency check (D-103, 28 findings, 27 fixed, OI-12 raised) and six business open items decided (D-104); anchor PMS-BRD rev 0.13 → 0.15, module BRDs rev 0.1 → 0.3; gate criteria now 3 of 6 met.
- Health **Amber → Green**: no Critical or High finding open; remaining open items are UX updates due before HLD Part02; reviewers not named (R-07).
- Findings: OI-02, OI-03, OI-04, OI-EIMS-01, OI-EIMS-02 closed; OI-12 raised and closed (D-104). Coverage Mockups → BRD 17/17, Journeys → BRD 30/30.
- Data: 49 artifacts, 105 decisions / ADRs (+2), 16 open items / findings (8 open), 9 reviews (+RV-09), 8 risks (R-02 updated), 81 linked repository files, 0 broken links.
- Warnings: new folder docs/02-brd/reviews/ not mapped (mapping line proposed). Customer-facing filtering: 29 texts neutralised (+2).

## 2026-11-20 19:48 IST – refresh (SUP BRD drafted; all six BRD documents drafted)

- Refreshed from commit `b4e141a` (7 commits since `00e9b24`: `8e4ecb0` to `b4e141a`); clean working tree.
- **Stage 2 BRD In Progress, 65% → 80%**: PMS-BRD-M5-SUP drafted (v1.0 rev 0.1, all sections reviewed D-97 to D-102, approval pending OI-02, OI-04, OI-11); anchor PMS-BRD rev 0.10 → 0.13; gate criterion "BRD documents drafted" now met (6 of 6).
- Health **Amber** (unchanged): High open items OI-02, OI-03, OI-04 overdue and blocking approval of all five module BRDs; reviewers not named (R-07).
- Findings: OI-05 closed (D-97); new OI-11 (shell UX updates, Medium). Coverage Mockups → BRD 17/17, Journeys → BRD 30/30.
- Data: 49 artifacts, 103 decisions / ADRs (+8), 15 open items / findings (13 open), 8 reviews (+RV-08), 8 risks, 81 linked repository files, 0 broken links.
- Warnings: new internal prompt-templates folder not indexed (exclusion proposed, with the two folders already listed). Customer-facing filtering: 27 texts neutralised (+5).

## 2026-11-19 22:49 IST – refresh (SMS BRD drafted)

- Refreshed from commit `00e9b24` (9 commits since `7c44ca9`: `dbbc014` to `00e9b24`); clean working tree.
- **Stage 2 BRD In Progress, 50% → 65%**: PMS-BRD-M4-SMS drafted (v1.0 rev 0.1, all sections reviewed D-90 to D-94, approval pending OI-02, OI-04); anchor PMS-BRD rev 0.8 → 0.10; gate criterion "BRD documents drafted" now 5 of 6.
- Health **Amber** (unchanged): High open items OI-02, OI-03, OI-04 overdue and now blocking EIMS, AMS, LMS and SMS approval; reviewers not named (R-07).
- Findings: new OI-10 (SMS UX updates, Medium). Coverage Mockups → BRD 17/17, Journeys → BRD 30/30.
- Data: 49 artifacts, 95 decisions / ADRs (+6), 14 open items / findings (13 open), 7 reviews (+RV-07), 8 risks, 80 linked repository files.
- Warnings: two unmapped folders unchanged (exclusion proposed). Customer-facing filtering: 22 texts neutralised (+3).

## 2026-11-19 20:33 IST – refresh (LMS BRD drafted)

- Refreshed from commit `7c44ca9` (11 commits since `32b2031`: `acf55e7` to `7c44ca9`); clean working tree.
- **Stage 2 BRD In Progress, 35% → 50%**: PMS-BRD-M3-LMS drafted (v1.0 rev 0.1, all sections reviewed D-84 to D-88, approval pending OI-02, OI-04); anchor PMS-BRD rev 0.6 → 0.8; gate criterion "BRD documents drafted" now 4 of 6.
- Health **Amber** (unchanged): High open items OI-02, OI-03, OI-04 overdue and blocking EIMS, AMS and LMS approval; reviewers not named (R-07).
- Findings: new OI-09 (LMS UX updates, Medium); F-SMD-02 resolved (SCR-LMS-02 now covered). Coverage Mockups → BRD 17/17, Journeys → BRD 30/30.
- Data: 49 artifacts, 89 decisions / ADRs (+6), 13 open items / findings (12 open), 6 reviews (+RV-06), 8 risks (R-02 owner corrected to HR Manager per PMS-BRD §10), 79 linked repository files, 0 broken links.
- Warnings: two new unmapped folders (internal working files, internal screenshots) – exclusion proposed. Customer-facing filtering: 19 texts neutralised (+5).

## 2026-11-19 18:48 IST – initial baseline (SMD 1.0)

- First build from commit `32b2031` plus working-tree change D-82 (mockups moved to `docs/01-ux/mockups/html/` and `png/`).
- Lifecycle: Stage 0 Completed (18 Nov, D-52), Stage 1 Completed (15 Nov, D-34), **Stage 2 BRD In Progress (35%)** – anchor rev 0.6 in review, EIMS and AMS drafted, LMS / SMS / SUP not started. Stages 3–8 Not Started.
- Health **Amber**: OI-02, OI-03, OI-04 past due point; BRD reviewers not named (R-07).
- Data: 49 artifacts, 83 decisions / ADRs, 12 open items / findings, 5 reviews, 8 risks, 78 linked repository files, 0 broken links.
- Coverage: Mockups → BRD 16/17 (SCR-LMS-02 pending LMS BRD); Journeys → BRD 30/30.
- Customer-facing filtering: 14 texts neutralised.
