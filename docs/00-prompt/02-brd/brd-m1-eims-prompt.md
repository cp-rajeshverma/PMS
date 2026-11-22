# Prompt – PMS-BRD-M1-EIMS

| Field | Value |
| --- | --- |
| Document | docs/02-brd/PMS-BRD-M1-EIMS.md |
| Template | templates/02-brd/brd-module-template.md |
| Used | 18 Nov 2026 |
| Outcome | All sections reviewed (D-70 to D-76); profile change request introduced (D-70, D-72); approval pending OI-02, OI-04, OI-EIMS-01, OI-EIMS-02 |
| Status | Done – reuse only to revise EIMS |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 3: BRD. Today: the EIMS module BRD, docs/02-brd/PMS-BRD-M1-EIMS.md.

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

2. Inputs for the EIMS BRD:
   - UX: docs/01-ux/ux-journey-index.md (UJ-EIMS-01..09, UJ-SYS-04),
     docs/01-ux/ux-summary/scr-eims-01-directory.md, scr-eims-02-admin-form.md,
     scr-eims-03-my-profile.md, scr-eims-04-profile-review.md, docs/01-ux/mockups/html/scr-eims-0*.html
   - Baseline BRD v1.0 in Claude Docs (artifact dc21fe25-f34d-426d-ade4-e9b5c2312ef1), §6 EIMS:
     Employee entity, EIMS-V1..V6, EIMS-US1..US6 – input only, not the master
   - Decisions most relevant: D-01, D-02 (E1–E3), D-07 (O3, O6), D-24 (Admin is system-only),
     D-28 (password policy), D-29 (role in identity provider, manager deactivation block),
     D-58 and D-63 (Admin data scope, top-level employee)
   - Anchor rules/integrations to reference, not repeat: BR-CMN-01..09, 11..14, 18;
     INT-03, INT-04, INT-05, INT-07, INT-08; FR-CMN-005
   - Template: templates/02-brd/brd-module-template.md

3. Approach:
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - Before drafting, read the inputs and ask me the EIMS BA gaps first.
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

5. At the end of the EIMS document: update anchor §2.3 and §11 for EIMS, add a session handoff
   note in memory/sessions/<date>.md, and stop before AMS until I say go.

Start by loading the context, then show me the EIMS gaps you found (first round of questions).
```

## Notes from the session

- Gaps decided: role change and deactivation blocked while a manager has reports; joining-date change checked against attendance and leave (INT-09); no reporting loops; no reactivation; Employee Id never reused; email unique incl. inactive; sensitive attributes listed (D-71).
- An approved profile changes only through a profile change request (D-70, D-72); EIMS holds two business entities.
- New prefix RPT-<MOD>-<NN> for dashboard / report items (D-76).
