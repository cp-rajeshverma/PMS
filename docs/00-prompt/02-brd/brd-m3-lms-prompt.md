# Prompt – PMS-BRD-M3-LMS

| Field | Value |
| --- | --- |
| Document | docs/02-brd/PMS-BRD-M3-LMS.md |
| Template | templates/02-brd/brd-module-template.md |
| Used | 19 Nov 2026 |
| Outcome | All sections reviewed (D-84 to D-88); anchor rev 0.7 and 0.8 (OI-09); approval pending OI-02, OI-04 |
| Status | Done – reuse only to revise LMS |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 3: BRD. Today: the LMS module BRD, docs/02-brd/PMS-BRD-M3-LMS.md.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents; PR-02: never use NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/
   - docs/decisions/decision-log.md (newest first; use the next free D-id)
   - docs/02-brd/PMS-BRD.md (anchor, v1.0 rev 0.6) – glossary, roles (§4), FR-CMN (§5.3),
     BR-CMN-01..18 (§6), INT-01..10 and JOB-CMN-01 (§7), NFRs (§8), open items OI-01..08 (§12)
   - docs/02-brd/PMS-BRD-M1-EIMS.md and PMS-BRD-M2-AMS.md – drafted module BRDs;
     use them as the pattern for structure, depth, ids and wording

2. Inputs for the LMS BRD:
   - UX: docs/01-ux/ux-journey-index.md (UJ-LMS-01..04),
     docs/01-ux/ux-summary/scr-lms-01-my-leave.md, scr-lms-02-request.md, scr-lms-03-team-review.md,
     docs/01-ux/mockups/html/scr-lms-0*.html (paths per D-82)
   - Baseline BRD v1.0 in Claude Docs (artifact dc21fe25-f34d-426d-ade4-e9b5c2312ef1), §8 LMS:
     Leave entity, LMS-V1..V6, LMS-US1..US4 – input only, not the master
   - Decisions most relevant: D-04 (L1–L4), D-07 (O4 cancel while Submitted, O5 past dates),
     D-32 (calendar days incl. weekends, status Cancelled, no Reason field, no draft),
     D-05/S6 (no paid leave), D-58 and D-63 (Admin for top-level employee only),
     D-77 (BR-CMN-10 clarified: draft/rejected attendance does not block leave)
   - Anchor rules/integrations to reference, not repeat: BR-CMN-01..10, 12, 17, 18;
     INT-03, INT-04, INT-06, INT-07, INT-09; FR-CMN-004; open items OI-02, OI-04
   - Template: templates/02-brd/brd-module-template.md

3. Approach:
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - Before drafting, read the inputs and ask me the LMS BA gaps first.
   - Draft in this order, one review at a time: §1–§6, then §7, then §8–§9, then §10–§17.
   - Any change to the anchor (new rule, integration, open item, prefix) gets a new anchor
     revision row (next rev 0.7) and is mentioned in the decision.

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

5. At the end of the LMS document: update anchor §2.3 and §11 for LMS, add a session handoff
   note in memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md, and stop
   before SMS until I say go. Remind me to refresh the SDLC dashboard (smd/prompt/smd-update-prompt.md).

Start by loading the context, then show me the LMS gaps you found (first round of questions).
```
