# Prompt – PMS-HLD-Part02-M1-EIMS-Functional

| Field | Value |
| --- | --- |
| Document | docs/03-hld/PMS-HLD-Part02-M1-EIMS-Functional.md |
| Template | templates/03-hld/hld-part02-module-functional-template.md |
| Used | 23 Nov 2026 |
| Outcome | PMS-HLD-Part02-M1-EIMS-Functional v1.0 rev 0.10, all sections reviewed (D-130 to D-139): 20 functions with API-EIMS-01 to 28 and 28 error codes; threat-review method STRIDE at trust boundaries TB-1 to TB-5 (OI-P01a-08 closed, Part01a rev 0.8); OI-P02-01 settled for EIMS (identity-provider call inside the EIMS transaction, account take-over); role copy on EMPLOYEE; OI-P03-03 not affected; OI-P02-02 referenced; open items OI-P02M1-01 to 03; Part02 anchor rev 0.6 |
| Status | Used – final approval at the Stage 3 gate |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 4: HLD (SDLC Stage 3 Solution Design, plan D-108: 23 Nov – 11 Dec 2026,
target go-live 29 Jan 2027). Today: the HLD Part02 Functional Design for the EIMS module,
docs/03-hld/PMS-HLD-Part02-M1-EIMS-Functional.md – the fifth of the 14 HLD documents and the first
module document (order D-108: Part01 → Part01a → Part02 anchor → Part03 anchor → per module Part02
then Part03: EIMS, AMS, LMS, SMS, SUP).
Scope: the 20 EIMS system functions EIMS0010 to EIMS0200 of the Part02 anchor §4, each designed with
the template's per-function chapter; the EIMS steps of the cross-module flows XF-01, XF-07, XF-08 and
XF-09 (the flows themselves stay in the anchor); the EIMS API, error-code and NFR inventories. The
identity-provider side of account changes (UM0010 to UM0050) is designed in PMS-HLD-Part02-M5-SUP;
here it is a call to that function, not its design. Column definitions belong to
PMS-HLD-Part03-M1-EIMS-Datamodel (next document): the database parts of this document name the
entities and the rules from the Part03 anchor, not columns.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents – use bmad-* equivalents;
      PR-02: never read, search, quote or reuse NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents or describe the delivery as
      AI-driven – author is "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, every reading in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md (function ids <MOD>0010 in steps of 10; per-function
     chapter structure D-38; API reference format [API-<MOD>-nn : METHOD /ctx/resource (Purpose : ...)];
     API inventory as a roll-up keyed by API id; design status Draft / In review / Approved / Deferred,
     "Not started" in the anchor index until drafted (D-123); every diagram keeps a text-version table;
     designs stay technology-neutral to allow replatforming)
   - the latest handoff note in memory/sessions/ (2026-11-23.md, last sections: Part03 anchor outcome,
     SMD refresh, open items carried)
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry,
     D-130 at the time of writing) and docs/decisions/adr/ (ADR-001 to ADR-006)
   - docs/03-hld/PMS-HLD-Part02-Functional.md v1.0 rev 0.5 – conventions, index and roll-ups to
     follow: §2 reading rules, §3.2 dependency map, §4 (EIMS0010 to EIMS0200 and the UM / ADM functions
     they call), §5.1 XF-01, §5.7 XF-07, §5.8 XF-08, §5.9 XF-09 (and XF-02 to XF-06 for the EIMS APIs
     other modules call: INT-03, INT-04, INT-05, INT-07), §6.1 API, §6.3 error codes, §6.4 audit and
     activity log, §6.5 frontend, §7.1 API inventory, §10.1 OI-P02-01 and 02
   - docs/03-hld/PMS-HLD-Part03-Datamodel.md v1.0 rev 0.4 – §2.2 eims ownership, §2.3 conventions
     (Employee Id from EMPLOYEE_ID_COUNTER raised in the same local transaction, references, user
     references, formats, soft delete, row_version), §2.4 common columns, §2.5 common audit entry
     (insert-only), §3.2 entities EMPLOYEE, PROFILE_CHANGE_REQUEST, EMPLOYEE_ID_COUNTER, AUDIT_ENTRY,
     §5 cross-service rows, §6 classification (D-71 sensitive personal attributes, hourly wage rate
     sensitive pay), §9.1 open items
   - the module BRD docs/02-brd/PMS-BRD-M1-EIMS.md v1.0 – §4 access, §5 journeys, §6 status
     lifecycles (profile, account Active / Inactive, profile change request), §7 FR-EIMS-001 to 041
     by screen, §8 rules (BR-EIMS, VR-EIMS), §9 data, §10 notifications, §11 integrations, §12
     dashboard, §13 NFRs; the BRD anchor PMS-BRD.md §4.3 (role and data scope), §6 BR-CMN rules and
     §7 INT-03, INT-04, INT-05, INT-07, INT-08, INT-09; PMS-BRD-M5-SUP FR-UM-001 to 015 and
     FR-ADM-101 to 117 where EIMS functions call them
   - no HLD module document is drafted yet: this document sets the pattern (structure, depth, ids,
     wording) for AMS, LMS, SMS and SUP – keep it consistent and not heavier than needed

2. Inputs for the EIMS Part02:
   - UX v1.1 (D-105): docs/01-ux/ux-summary/scr-eims-01-directory.md, scr-eims-02-admin-form.md,
     scr-eims-03-my-profile.md, scr-eims-04-profile-review.md, plus scr-sh-03-dashboard.md and
     scr-sh-04-approvals.md for the EIMS card and inbox items; mockups
     docs/01-ux/mockups/html/scr-eims-0*.html (reference them, don't copy them)
   - HLD Part01 v1.0 rev 0.9: §8.2 rows 4, 5, 6, 8, 9, 10 (INT-03, 04, 05, 07, 08, 09), §8.5
     resilience defaults, §9.7 to §9.9 authorization, refused response and service-to-service
     identity, §10.3 log record, §10.5 flow reference, §10.8 masking, §14 load-test cases that touch
     EIMS, §16.3 NFR realization. Part01a v1.0 rev 0.7: AP-SEC-16 and OI-P01a-08
   - Decisions most relevant: D-02 (system-generated Employee Id), D-24, D-28 (password policy),
     D-29 (role held in the identity provider; deactivating a manager with reports blocked; during
     re-approval other modules use the last approved profile, which is stored), D-57 (UM and AUTH in
     the POC), D-58 and D-63 (Admin and manager data scope), D-70 and D-72 (profile change request),
     D-71 (EIMS rules: role change, joining-date change, manager rules, Ids never reused), D-73 to
     D-76 (EIMS BRD), D-97 (Admin account, deactivation and reset end sessions), D-99 (neutral
     refused page), D-100, D-101 (audit and activity log), D-104 (OI-02, OI-04, OI-12,
     OI-EIMS-01, OI-EIMS-02), D-105 (UX v1.1), D-111 (session ending, service-to-service tokens),
     D-122 to D-125 (Part02 anchor; D-123 (5): a waiting item has no stored approver), D-126 to D-129
     (Part03 anchor); ADRs ADR-001 (frontend composition), ADR-003 (identity provider holds
     passwords), ADR-004 (gateway holds user tokens)
   - Open items brought forward (must be answered or re-routed in this document):
     (a) OI-P01a-08 – threat-modelling method for the "Security & data privacy" part of every function
         design (§3.2.n.5.8), due before the first module Part02 document. Ask it in the first round:
         present the options with trade-offs (for example STRIDE per function at the trust
         boundaries the function crosses; a lighter checklist from the OWASP Top 10 mapping of
         Part01 §16.2 per function; STRIDE once per flow in the anchor plus a short per-function
         check here) and the depth per function (which rows the template's security table gets).
         Record the method in this document's §2 reading rules and the decision; close OI-P01a-08
         in Part01a §7 with a Part01a revision row, and leave the detailed method text to
         docs/04-standards/security (planned).
     (b) OI-P03-03 – lifetime of short-lived in-memory copies of other services' data. Check whether
         any EIMS function keeps such a copy (EIMS reads AMS and LMS only for the INT-09 checks,
         which must not be cached). If none does, say so in the database / backend parts and leave
         OI-P03-03 with PMS-HLD-Part02-M2-AMS; if one does, ask me.
     (c) OI-P02-01 – onboarding and account changes (EIMS0020, EIMS0040, EIMS0050, EIMS0060): the
         order of the identity-provider call and the EIMS commit, retry of a half-done onboarding and
         recovery belong to PMS-HLD-Part02-M5-SUP, which is drafted last. Ask me whether to settle
         the order here (EIMS owns the transaction and the Employee Id counter, Part03 anchor §2.3)
         and only reference it from M5-SUP, or to design the EIMS steps with a pointer to OI-P02-01.
     (d) OI-P02-02 – the joining-date check (EIMS0040, XF-07) is a check-then-act across databases;
         it is decided before PMS-HLD-Part02-M2-AMS. Reference it here; do not decide it unless I say.
   - Points to settle while drafting (ask me where the inputs leave a choice):
     the EIMS API list and ids API-EIMS-01 … (anchor §7.1 rows show "API-EIMS-nn (planned)"), user vs
     internal APIs (anchor §6.1); how the last approved profile is kept during re-approval (D-29)
     and the previous values of an approved change request (BRD §9.2) – as design rules, columns go
     to Part03-M1; the employee-directory query and its data-scope filter and paging (FR-EIMS-001 to
     006); the dashboard card and inbox items EIMS supplies (EIMS0200, INT-07, SH0020 to SH0040);
     the EIMS error codes EIMS-VAL / BUS / CON / ACC / SYS-nnn with the VR / BR id each enforces
     (anchor §6.3); the activity-log step names per function (anchor §6.4).
   - No notifications in the POC (C-05; NM Phase 2): §3.2.n.5.9 shows "None (C-05)" and the
     audit and activity entries; the temporary password is shown once to the Admin (D-104).
   - Template: templates/03-hld/hld-part02-module-functional-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master. Document ID
     PMS-HLD-Part02-M1-EIMS-Functional-v1.0, revision 0.1 at first draft.
   - Each function chapter follows the template's per-function structure (purpose, trigger and
     conditions; actor and data scope; traceability; navigation and prototype; solution approach;
     notes); reference BRD and UX ids instead of restating them; API references use
     [API-EIMS-nn : METHOD /api/eims/v1/... (Purpose : …)]; designs stay technology-neutral (no
     framework or product names; identity provider, broker, gateway named by role).
   - Small related functions may share a review (for example the three API-only functions EIMS0170
     to EIMS0190); propose the grouping of the 20 functions into reviews in the first round.
   - Every sequence diagram keeps its text-version table; check that each diagram renders.
   - Before drafting, read the inputs and ask me the EIMS Part02 gaps first, starting with (a), (c)
     and the review grouping.
   - Draft in this order, one review at a time: §1–§2 and §3.1, then §3.2 one system function (or a
     few small ones) per review, then §4–§5.
   - Every approved review adds a revision row to §1.1. Open items of this document are
     OI-P02M1-nn in §5.2.
   - Any change to the anchor (PMS-HLD-Part02-Functional) – API ids and endpoints in §7.1, error-code
     range, design status "Not started" → Draft / In review in §4 and §2.2, a new rule or open item –
     gets a new anchor revision row (next rev 0.6) and is mentioned in the decision. The only other
     documents this session may change: Part01a §7 (closing OI-P01a-08, with a revision row) and,
     if (c) is settled here, the OI-P02-01 status text in the anchor §10.1.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me design questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - New ADRs only for new significant decisions, after my "yes"; register them in Part01a §5 and
     Part01 §18.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants (Claude, BMAD or any other) anywhere in the
     document, and no description of the delivery as AI-driven.
   - PR-04: take a usage reading at session start and at every outcome commit (in the Claude app:
     "show me where this session's tokens went"); append one row per outcome with the difference
     to memory/usage/token-log.csv (stage 3, outcome PMS-HLD-Part02-M1-EIMS-Functional, module EIMS)
     and the reading itself, with its group split, to memory/usage/session-readings.csv; quote any
     text that contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
     A single device-shell command is limited in size: write long content in several parts.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, list them and ask once for delete
     permission on D:\POC\PMS, then remove only those files after each commit in this session.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the EIMS document: update the Part02 anchor for EIMS (§2.2 status and version, §4
   design status of EIMS0010 to EIMS0200, §7.1 API ids and endpoints, §6.3 error-code row) with an
   anchor revision row, record how (a) to (d) were settled or re-routed, add a session handoff note in
   memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md and to this prompt file's
   header, and stop before the next HLD document until I say go. Remind me to refresh the SDLC
   dashboard (smd/prompt/execute-prompt-file-smd-update-prompt.md) and that the next prompt is
   hld-part03-m1-eims-datamodel (from templates/00-prompt, prompt pair hld-part03-mN-mod-datamodel).

Start by loading the context, then show me the EIMS Part02 gaps you found (first round of questions).
```
