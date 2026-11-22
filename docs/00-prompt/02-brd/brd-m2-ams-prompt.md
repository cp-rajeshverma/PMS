# Prompt – PMS-BRD-M2-AMS

| Field | Value |
| --- | --- |
| Document | docs/02-brd/PMS-BRD-M2-AMS.md |
| Template | templates/02-brd/brd-module-template.md |
| Used | 19 Nov 2026 |
| Outcome | All sections reviewed (D-77 to D-81); approval pending OI-02, OI-03, OI-04 |
| Status | Done – reuse only to revise AMS |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 3: BRD. Today: the AMS module BRD, docs/02-brd/PMS-BRD-M2-AMS.md.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents; PR-02: never use NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/
   - docs/decisions/decision-log.md (newest first; use the next free D-id)
   - docs/02-brd/PMS-BRD.md (anchor) – glossary, roles (§4), FR-CMN (§5.3), BR-CMN (§6),
     integrations (§7), NFRs (§8), open items (§12)
   - docs/02-brd/PMS-BRD-M1-EIMS.md – approved module BRD; use it as the pattern for structure,
     depth, ids and wording

2. Inputs for the AMS BRD:
   - UX: docs/01-ux/ux-journey-index.md (UJ-AMS-01..04, UJ-SYS-01..03 hand-overs),
     docs/01-ux/ux-summary/scr-ams-01-my-attendance.md, scr-ams-02-entry.md, scr-ams-03-team-review.md,
     docs/01-ux/mockups/html/scr-ams-0*.html
   - Baseline BRD v1.0 in Claude Docs (artifact dc21fe25-f34d-426d-ade4-e9b5c2312ef1), §7 AMS:
     Attendance entity, AMS-V1..V5, AMS-US1..US4 – input only, not the master
   - Decisions most relevant: D-03 (A1–A3), D-07 (O1, O2 reopen after dispute), D-08 (weekends),
     D-16 (events), D-24 (multi-select approve, calendar + list), D-25 (Voided), D-28 (missing-weekday
     reminder), D-31 (no withdrawal, 15-minute steps, 12-hour warning), D-58 and D-63 (Admin for
     top-level employee)
   - Anchor rules/integrations to reference, not repeat: BR-CMN-01..10, 12, 15, 17, 18;
     INT-01, INT-02, INT-06, INT-07, INT-09, JOB-CMN-01; FR-CMN-004; open items OI-02, OI-03, OI-04
   - Template: templates/02-brd/brd-module-template.md

3. Approach:
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - Before drafting, read the inputs and ask me the AMS BA gaps first.
   - Draft in this order, one review at a time: §1–§6, then §7, then §8–§9, then §10–§17.
   - Any change to the anchor gets a new anchor revision row and is named in the decision.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements –
     record gaps as open items.
   - Ask me BA questions a few at a time (max 4 per round), each with your recommended answer
     first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants anywhere in the document.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the AMS document: update anchor §2.3 and §11 for AMS, add a session handoff
   note in memory/sessions/<date>.md, and stop before LMS until I say go.

Start by loading the context, then show me the AMS gaps you found (first round of questions).
```

## Notes from the session

- Gaps decided (D-77): discard Draft / Rejected (soft delete); leave allowed over Draft / Rejected attendance, which then cannot be submitted; no backdating limit; 15-minute steps 00:00–23:45, minimum 0.25 h; "Over 12 h" flag for approvers; history defaults to the current month incl. inactive reports.
- Reopen reuses the Rejected status (D-78); anchor gained INT-10 (SMS → AMS salary status) and OI-08 (AMS UX updates).
