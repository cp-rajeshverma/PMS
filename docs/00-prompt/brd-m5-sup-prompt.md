# Prompt – PMS-BRD-M5-SUP

| Field | Value |
| --- | --- |
| Document | docs/02-brd/PMS-BRD-M5-SUP.md |
| Template | templates/02-brd/brd-sup-template.md |
| Used | 20 Nov 2026 |
| Outcome | All sections reviewed (D-97 to D-102): SUP rules incl. OI-05 closed (D-97); §1–§3 with the activity-log addition (D-98); §5–§6 (D-99); own password change ends other sessions (D-100); audit and activity log, §4, §7–§11 (D-101); §12–§14 (D-102); anchor rev 0.11 to 0.13 (OI-11, BR-CMN-19, NFR-09, SUP status); approval pending OI-02, OI-04, OI-11 |
| Status | Done – reuse only to revise SUP |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 3: BRD. Today: the supporting functions BRD, docs/02-brd/PMS-BRD-M5-SUP.md,
covering user management (UM) and authentication and authorization (AUTH); ADM, NM and DM get a
need-basis entry only (Phase 2, D-57).

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents; PR-02: never use NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry)
   - docs/02-brd/PMS-BRD.md (anchor, v1.0 rev 0.10) – glossary (Employee Id, Admin, temporary
     password, soft delete), §3.3 scope (SUP row) and out of scope, roles and role catalogue (§4.2),
     role × module access incl. the SUP row (§4.3), end-to-end step 2 (§5.1), journeys UJ-SH-01,
     02, 05 (§5.2), FR-CMN-015 and 016 (§5.3), BR-CMN-01, 06, 08 (§6), INT-08 (§7), NFR-03, NFR-04,
     NFR-05 (§8), C-05, C-06, DEP-01 (§9), R-04 (§10), §11 SUP row, open item OI-05 (§12),
     future scope (§13.1: self-service password reset, single sign-on)
   - docs/02-brd/PMS-BRD-M1-EIMS.md – the Admin screens that drive UM (onboarding and user account,
     role, deactivation, password reset: §3.3, FR-EIMS-005, 010, 012, 016, 018, 040, 041, INT-08).
     EIMS owns those screens; SUP owns the capability behind them – reference, don't repeat, and
     stay consistent. PMS-BRD-M2-AMS, M3-LMS and M4-SMS are the pattern for structure, depth, ids
     and wording.

2. Inputs for the SUP BRD:
   - UX: docs/01-ux/ux-journey-index.md (UJ-SH-01, UJ-SH-02, UJ-SH-05; navigation map and user menu),
     docs/01-ux/ux-summary/scr-sh-01-login.md, scr-sh-02-set-password.md, scr-sh-00-layout.md
     (user menu, session expiry), scr-eims-01-directory.md (reset password),
     scr-eims-02-admin-form.md (role, deactivate); docs/01-ux/mockups/html/scr-sh-0[0-2]*.html
   - Baseline BRD v1.0 in Claude Docs (artifact dc21fe25-f34d-426d-ade4-e9b5c2312ef1), §4 roles,
     permissions matrix and login (Employee Id + password, no SSO, no self-registration) –
     input only, not the master
   - Decisions most relevant: D-01 (C3 simple login, three roles), D-07 (O6 Admin resets passwords),
     D-24 (Admin is a system role only), D-26 (idle timeout 30 min; lock 15 min after 5 failed
     sign-ins), D-28 (password policy), D-29 (role chosen by Admin at onboarding, held in the
     identity provider; deactivating a manager with reports blocked), D-53 (SUP need-basis after
     M1–M4), D-57 (UM and AUTH in the POC; ADM, NM, DM Phase 2), D-58 and D-63 (Admin data scope;
     manager scope direct reports only), D-59 (NFR targets), D-71 (Employee Id never reused;
     no reactivation in the POC)
   - Anchor items to reference, not repeat: BR-CMN-01, 06, 08; INT-08; FR-CMN-015, 016;
     NFR-03, 04, 05; C-05, C-06; DEP-01; R-04; OI-05
   - Template: templates/02-brd/brd-sup-template.md (prefixes ADM, UM, AUTH, NM, DM)

3. Approach:
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - Authorization (who may do what on which data) is written in §5 from the anchor role catalogue
     and role × module access; the BRD stays technology-neutral ("identity provider") – product
     names belong in the HLD (Part01 §9).
   - §4 (ADM), §7 (NM), §8 (audit) and §9 (DM) keep their headings with the need-basis result
     (Phase 2 per D-57, or "Provided by … – no project requirements beyond §3"); do not invent
     requirements for them. OI-05 (values the Admin can change without a release) is decided in
     this session, because it is due before PMS-BRD-M5-SUP.
   - Before drafting, read the inputs and ask me the SUP BA gaps first.
   - Draft in this order, one review at a time: §1–§3, then §5–§6, then §4 and §7–§11,
     then §12–§14.
   - Any change to the anchor (new rule, integration, open item, prefix) gets a new anchor
     revision row (next rev 0.11) and is mentioned in the decision.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements –
     record gaps as open items.
   - Ask me BA questions a few at a time (max 4 per round), each with your recommended answer
     first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants anywhere in the document.
   - PR-04: take a usage reading at session start and at every outcome commit (in the Claude app:
     "show me where this session's tokens went"); append one row per outcome with the difference to
     memory/usage/token-log.csv and the reading itself, with its group split, to
     memory/usage/session-readings.csv; quote any text that contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. The device
     shell cannot write /tmp – keep scratch files in $HOME and never read leftovers from /tmp.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the SUP document: update anchor §2.3 and §11 for SUP, add a session handoff
   note in memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md and to this
   prompt file's header, and stop until I say go. Remind me to refresh the SDLC dashboard
   (smd/prompt/execute-prompt-file-smd-update-prompt.md) and list what remains for the Stage 2
   gate (business open items, UX update, consistency check, stakeholder review, sign-off).

Start by loading the context, then show me the SUP gaps you found (first round of questions).
```
