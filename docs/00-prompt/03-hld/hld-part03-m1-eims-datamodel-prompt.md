# Prompt – PMS-HLD-Part03-M1-EIMS-Datamodel

| Field | Value |
| --- | --- |
| Document | docs/03-hld/PMS-HLD-Part03-M1-EIMS-Datamodel.md |
| Template | templates/03-hld/hld-part03-module-datamodel-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 4: HLD (SDLC Stage 3 Solution Design, plan D-108: 23 Nov – 11 Dec 2026,
target go-live 29 Jan 2027). Today: the HLD Part03 Data Model for the EIMS module,
docs/03-hld/PMS-HLD-Part03-M1-EIMS-Datamodel.md – the sixth of the 14 HLD documents and the first
module data-model document (order D-108: per module Part02 then Part03: EIMS, AMS, LMS, SMS, SUP).
Scope: the column-level definitions of the eims database – business entities EMPLOYEE and
PROFILE_CHANGE_REQUEST, system tables EMPLOYEE_ID_COUNTER and AUDIT_ENTRY (AUDIT_ENTRY is defined
once in the Part03 anchor §2.5: here only which EIMS records and fields are audited, no second
definition). The user account, role, password and sessions live in the identity provider and are
not PMS entities (Part03 anchor §2.2, ADR-003). This document sets the pattern for the AMS, LMS,
SMS and SUP data-model documents – keep it consistent and not heavier than needed.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents – use bmad-* equivalents;
      PR-02: never read, search, quote or reuse NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents or describe the delivery as
      AI-driven – author is "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, every reading in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md (entity status values Draft / In review /
     Approved / Deferred / Moved / Removed; columns defined only in module data-model documents;
     database per service, no cross-database FK; every diagram keeps a text-version table;
     technology-neutral wording apart from the conventions the Part03 anchor already fixes)
   - the latest handoff notes in memory/sessions/ (2026-11-23.md, last sections: HLD Part02-M1 EIMS
     handoff with "For Part03-M1-EIMS", the SMD refresh)
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry,
     D-140 at the time of writing) and docs/decisions/adr/ (ADR-001 to ADR-006)
   - docs/03-hld/PMS-HLD-Part03-Datamodel.md v1.0 rev 0.4 – conventions, index and roll-ups to
     follow: §2.2 eims ownership, §2.3 modelling conventions (uuid surrogate key plus business key,
     snake_case, constraint prefixes pk_ / uk_ / fk_ / ck_ / ix_, user references varchar(30),
     timestamptz UTC and IST business dates, numeric(12,2), status codes with check constraints and
     no lookup tables, is_active soft delete, Employee Id counter), §2.4 common columns, §2.5 common
     audit entry, §3.1 module documents, §3.2 entity index (EMPLOYEE, PROFILE_CHANGE_REQUEST,
     EMPLOYEE_ID_COUNTER Not started), §4.1 master ER, §5 cross-service rows for employee data,
     §6 classification (D-71 sensitive personal, hourly wage rate sensitive pay), §7 volumetrics,
     §8 schema management, §9.1 open items
   - the module BRD docs/02-brd/PMS-BRD-M1-EIMS.md v1.0 – §6 status lifecycles (profile, Active /
     Inactive, profile change request), §8 rules (VR-EIMS-01 to 10, BR-EIMS-01 to 10), §9.1 Employee
     and §9.2 Profile change request attributes, §13 volumetrics
   - docs/03-hld/PMS-HLD-Part02-M1-EIMS-Functional.md v1.0 rev 0.10 – what each function reads and
     writes: §3.1.3 ER, §3.1.4 status handling, the Database part (§3.2.n.5.6) and design notes of
     every function, §4.2 API inventory, §4.5 error catalogue, §5.2 open items
   - no module data-model document is drafted yet: this document sets the pattern

2. Inputs for the EIMS Part03:
   - Template: templates/03-hld/hld-part03-module-datamodel-template.md
   - Decisions most relevant: D-02 (system-generated Employee Id), D-70 and D-72 (profile change
     request), D-71 (EIMS rules, sensitive attributes, Ids never reused, email unique across active
     and inactive), D-104 (one top-level employee), D-126 (Employee Id counter row in the onboarding
     transaction; common audit entry; row_version on every business record; conventions), D-127,
     D-128 (classification, volumetrics, schema management), D-130 (EIMS keeps no copies, publishes
     no events), D-131 (copy of the role on EMPLOYEE, identity provider authoritative; search on
     name, Employee Id and email), D-132 (counter raised inside the onboarding transaction with the
     identity-provider call; email compared case-insensitively), D-133 (reporting-line locks;
     inactive employees read only), D-134, D-135 (country fields as ISO 3166-1 alpha-2 codes; submit
     clears the decision fields), D-136 (one open request per employee; full set of requested
     values; previous values copied at approval), D-137 (approver and decision time stored with the
     decision), D-138 (INT-03 fields), D-139; ADR-003 (identity provider holds passwords)
   - Design rules from the EIMS Part02 to turn into columns and constraints (ask me where they
     leave a choice):
     (a) role copy on EMPLOYEE (D-131) – values EMPLOYEE / MANAGER, written only by EIMS0020 and
         EIMS0040;
     (b) PROFILE_CHANGE_REQUEST holds the full set of employee-editable fields as requested and, on
         approval, the full set of previous values (D-136, D-137) – column layout (two column sets
         or another structure allowed by the anchor, which permits jsonb only for the outbox event);
     (c) database backstops: unique email ignoring case across all employees (D-132), at most one
         active top-level employee (VR-EIMS-05, D-104), at most one open request (Draft, Submitted,
         Rejected) per employee (BR-EIMS-03, D-136) – partial unique indexes or another rule;
     (d) submission time on EMPLOYEE and PROFILE_CHANGE_REQUEST (BRD §9.1, §9.2 "Submitted Date");
     (e) Manager Id as a self-reference within eims (FK allowed inside one database) and the index
         for direct reports;
     (f) indexes the functions need: directory search and sort (EIMS0010, D-131), approvees and
         approval items (EIMS0180, EIMS0200), open request per employee, recently created employees;
     (g) EMPLOYEE_ID_COUNTER layout and its start row (created at 0 by the migrations, Part03
         anchor §8);
     (h) which EIMS fields and record types (EMPLOYEE, PROFILE_CHANGE_REQUEST, USER_ACCOUNT) are
         audited, as a list against the anchor's AUDIT_ENTRY.
   - Open items brought forward (answer or re-route): OI-P02M1-01 (restore procedure for the
     employee database – data side only, the procedure stays with the database-and-data standard);
     OI-P03-03 (in-memory copies – not an EIMS item, stays with PMS-HLD-Part02-M2-AMS); OI-P02M1-02
     and 03 (BRD items – reference only).

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master. Document ID
     PMS-HLD-Part03-M1-EIMS-Datamodel-v1.0, revision 0.1 at first draft.
   - Columns are defined only here; business statuses stay in the BRD (§6) and only their technical
     handling is designed; database per service, no cross-database foreign keys; sample data per
     scenario in the appendix (synthetic only, no real personal data).
   - Before drafting, read the inputs and ask me the EIMS Part03 gaps first, starting with (b) and
     (c).
   - Draft in this order, one review at a time: §1–§2, then §3 one entity per review (EMPLOYEE,
     PROFILE_CHANGE_REQUEST, EMPLOYEE_ID_COUNTER with the audit list), then §4–§6.
   - Every approved review adds a revision row to §1.1. Open items of this document are
     OI-P03M1-nn in §6.2.
   - Any change to the anchor (PMS-HLD-Part03-Datamodel) – entity index status, a new rule or open
     item – gets a new anchor revision row (next rev 0.5) and is mentioned in the decision. The only
     other document this session may change is the Part02 EIMS document, and only for a correction
     found while modelling (with its own revision row and mention in the decision).

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
     to memory/usage/token-log.csv (stage 3, outcome PMS-HLD-Part03-M1-EIMS-Datamodel, module EIMS)
     and the reading itself, with its group split, to memory/usage/session-readings.csv; quote any
     text that contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
     A single device-shell command is limited in size: write long content in several parts.
     Mermaid: no semicolons in diagram labels; check that each diagram renders.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files: list them, ask once for delete permission on D:\POC\PMS,
     then remove only those files after each commit in this session.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the module document: update the Part03 anchor for EIMS (§3.1 module document
   status and version, §3.2 entity index status of EMPLOYEE, PROFILE_CHANGE_REQUEST and
   EMPLOYEE_ID_COUNTER, any roll-up the anchor keeps) with an anchor revision row, record how the
   items in 2 were settled or re-routed, add a session handoff note in memory/sessions/<date>.md,
   add the outcome to docs/00-prompt/README.md and to this prompt file's header, and stop before
   the next HLD document until I say go. Remind me to refresh the SDLC dashboard
   (smd/prompt/execute-prompt-file-smd-update-prompt.md) and that the next prompt is
   hld-part02-m2-ams-functional (from templates/00-prompt, prompt pair hld-part02-mN-mod-functional;
   OI-P02-02 and OI-P03-03 are due there).

Start by loading the context, then show me the EIMS Part03 gaps you found (first round of questions).
```
