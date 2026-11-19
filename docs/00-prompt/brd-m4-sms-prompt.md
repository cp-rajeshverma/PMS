# Prompt – PMS-BRD-M4-SMS

| Field | Value |
| --- | --- |
| Document | docs/02-brd/PMS-BRD-M4-SMS.md |
| Template | templates/02-brd/brd-module-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 3: BRD. Today: the SMS module BRD, docs/02-brd/PMS-BRD-M4-SMS.md.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents; PR-02: never use NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/
   - docs/decisions/decision-log.md (newest first; use the next free D-id – D-89 if nothing newer)
   - docs/02-brd/PMS-BRD.md (anchor, v1.0 rev 0.8) – glossary (salary terms), roles (§4, SYS-SMS,
     SYS-REC), end-to-end steps 9–13 (§5.1), FR-CMN (§5.3), BR-CMN-01..18 (§6),
     INT-01..10 and JOB-CMN-01 (§7), NFRs and volumetrics (§8), KPI-02 / KPI-04 (§3.2),
     risks R-01 / R-03 (§10), open items OI-01..09 (§12)
   - docs/02-brd/PMS-BRD-M1-EIMS.md, PMS-BRD-M2-AMS.md and PMS-BRD-M3-LMS.md – drafted module BRDs;
     use them as the pattern for structure, depth, ids and wording (AMS §3.3, §7.4, §11 already
     describe the AMS side of the salary hand-overs – stay consistent with them)

2. Inputs for the SMS BRD:
   - UX: docs/01-ux/ux-journey-index.md (UJ-SMS-01..04, UJ-SYS-01..03),
     docs/01-ux/ux-summary/scr-sms-01-my-salary.md, scr-sms-02-team-review.md,
     docs/01-ux/mockups/html/scr-sms-0*.html (paths per D-82); salary items on
     scr-sh-03-dashboard.md and scr-sh-04-approvals.md
   - Baseline BRD v1.0 in Claude Docs (artifact dc21fe25-f34d-426d-ade4-e9b5c2312ef1), §9 SMS:
     Salary entity, wage formula, SMS-R1..R4 (→ BR-SMS-01..04), SMS-US1..US4 – input only,
     not the master
   - Decisions most relevant: D-05 (S1–S6: rate on Employee, hours × rate, generated on attendance
     approval, manager approves then employee accepts or disputes, no paid leave), D-07 (O1 dispute
     reopens attendance, O2 manager cannot reject salary), D-25 (Voided status, "Show voided",
     excluded from totals, void reason in Remarks, one non-voided record per attendance),
     D-33 (accept several at once, no auto-accept, Keep as is with explanation),
     D-16 / D-24 (event hand-over, nightly reconciliation 01:00 IST, multi-select approve),
     D-58 and D-63 (Admin for top-level employee only), D-59 (salary record within 1 minute,
     reconciliation < 5 minutes), D-77 (INT-10 "Salary disputed" for AMS)
   - Anchor rules/integrations to reference, not repeat: BR-CMN-01..08, 12, 13, 15, 16, 17, 18;
     INT-01, INT-02, INT-03, INT-04, INT-05, INT-07, INT-10, JOB-CMN-01; FR-CMN-002, 011, 012;
     NFR-01, NFR-06; open items OI-01, OI-02, OI-04, OI-06 (reconciliation time still "TBD" in UX)
   - Template: templates/02-brd/brd-module-template.md

3. Approach:
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - Before drafting, read the inputs and ask me the SMS BA gaps first.
   - Draft in this order, one review at a time: §1–§6, then §7, then §8–§9, then §10–§17.
   - Any change to the anchor (new rule, integration, open item, prefix) gets a new anchor
     revision row (next rev 0.9) and is mentioned in the decision.

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
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the SMS document: update anchor §2.3 and §11 for SMS, add a session handoff
   note in memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md and to this
   prompt file's header, and stop before SUP until I say go. Remind me to refresh the SDLC
   dashboard (smd/prompt/execute-prompt-file-smd-update-prompt.md).

Start by loading the context, then show me the SMS gaps you found (first round of questions).
```
