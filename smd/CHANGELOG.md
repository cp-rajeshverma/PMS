# SMD changelog

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
