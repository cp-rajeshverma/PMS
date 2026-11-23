# Prompt – PMS-HLD-Part03-Datamodel

| Field | Value |
| --- | --- |
| Document | docs/03-hld/PMS-HLD-Part03-Datamodel.md |
| Template | templates/03-hld/hld-part03-anchor-datamodel-template.md |
| Used | 23 Nov 2026 |
| Outcome | PMS-HLD-Part03-Datamodel v1.0 rev 0.4, all sections reviewed (D-126 to D-129): ownership per service, conventions, common columns and common audit entry, 5 business entities and 9 system tables, master ER, cross-service consistency of 12 data objects, classification, volumetrics, clean-up JOB-AMS-01 and the JOB-CMN-01 step (ADR-006 follow-up closed), schema management; Part01a rev 0.7, Part02 rev 0.5; open items OI-P03-01 to 03 |
| Status | Used – final approval at the Stage 3 gate |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 4: HLD (SDLC Stage 3 Solution Design, plan D-108: 23 Nov – 11 Dec 2026,
target go-live 29 Jan 2027). Today: the HLD Part03 Data Model anchor,
docs/03-hld/PMS-HLD-Part03-Datamodel.md – the fourth of the 14 HLD documents (order D-108: Part01 →
Part01a → Part02 anchor → Part03 anchor → per module Part02 then Part03: EIMS, AMS, LMS, SMS, SUP).
Scope: modelling conventions and common columns, data ownership per service, the entity index with
links, the entity-level master ER, cross-service data and consistency, and roll-ups of
classification, volumetrics and retention, and schema management (D-43). Columns are defined only in
the module data-model documents (PMS-HLD-Part03-M1-EIMS … M4-SMS, M5-SUP), which are not drafted
yet: roll-ups that depend on them get "Module document (planned)" and are completed as each module
document is written.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents – use bmad-* equivalents;
      PR-02: never read, search, quote or reuse NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents or describe the delivery as
      AI-driven – author is "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, every reading in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md (data model = anchor + one document per module +
     SUP, D-43; columns only in module documents; database per service, no cross-database foreign
     keys; supporting-module entities on a need basis only, skipped when an existing capability
     provides them, D-42; entity status values Draft, In review, Approved, Deferred, Moved, Removed;
     every diagram keeps a text-version table; designs stay technology-neutral)
   - the latest handoff note in memory/sessions/ (2026-11-23.md, last section: Part02 anchor outcome
     and the open items carried)
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry,
     D-126 at the time of writing) and docs/decisions/adr/ (ADR-001 to ADR-006)
   - the approved BRD set v1.0 (D-107) in docs/02-brd/: PMS-BRD.md §6 (BR-CMN-02, 06, 07, 18, 19),
     §7 (INT-01 to INT-10, JOB-CMN-01), §8 and §8.1 (NFRs, business volumetrics); the module BRDs
     M1-EIMS to M4-SMS §6 (status lifecycles), §9 (data requirements and sensitivity) and §13
     (module NFRs and volumetrics); PMS-BRD-M5-SUP §8 and §11 (audit and activity log, data) –
     read further sections only when a row needs them
   - docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md v1.0 rev 0.9 – §5.1, §8.2, §8.3 (outbox,
     topic, durable subscription, job lock), §8.5, §10.3 and §10.8 (log record, masking, retention),
     §11 (PostgreSQL 18, D-115), §12 data architecture summary, §13 seed data, §15 environments,
     §17 volumetrics
   - docs/03-hld/PMS-HLD-Part01a-Principles-Patterns-Decisions.md v1.0 rev 0.6 – group DATA
     (AP-DATA-07, 10, 11, 13 to 17), AP-XF-06, AP-SD-15, AP-CP-25, AP-EIP-61, AP-PERF-06, AP-DEV-10,
     all with Ref "Part03 (planned)"; §7 open items (OI-P01a-16 migration reversal plan)
   - docs/03-hld/PMS-HLD-Part02-Functional.md v1.0 rev 0.4 – §2.2 module documents, §3.2 dependency
     map, §4 function index (77 functions), §5 XF-01 to XF-09 (XF-02, 03, 04 in particular),
     §6.1 (Concurrency row, date / time / money / enum formats), §6.2 (ordering rule, idempotent
     consumers, competing consumers), §6.4 (audit log), §7.2 and §7.3 (events, jobs), §10.1 open
     items OI-P02-01 and 02

2. Inputs for the Part03 anchor:
   - Decisions most relevant: D-02 and D-71 (system-generated Employee Id, never reused), D-08
     (single company, IST, INR), D-10 (one service and entity per module), D-16 (outbox +
     reconciliation, contract-first), D-43 (Part03 split), D-70 (profile change request), D-75,
     D-80, D-87, D-93 (module data requirements and sensitivity; reconciliation run log is a job log,
     not a business entity), D-77 (discard is a soft delete that frees the date), D-90 (SMS rules,
     no rate history), D-101 (audit and activity log), D-104, D-110 (12) (audit in the owning
     database), D-112 (migrations, backups, seed data), D-113 (volumetrics), D-115 (PostgreSQL 18),
     D-117 (UTC storage), D-122 to D-125 (Part02 anchor; D-123 (5): a waiting item has no stored
     approver – the Approver Id is stored only with the decision)
   - ADRs: ADR-006 AMS → SMS outbox, idempotent consumer, nightly reconciliation (follow-up still
     open: the outbox clean-up rule, "in Part03"); ADR-003 (passwords only in the identity provider)
   - Items handed over by the Part02 anchor (must be answered or re-routed in this document):
     (a) SMS per-attendance version record and processed-event record (Part02 §6.2, XF-02, XF-03,
         XF-04): SMS stores, in the same local transaction as the salary change, the event id
         (duplicate check) and the last applied attendance version per attendance (ordering rule
         D-122); a reopened version is stored even when there is no record to void; the
         reconciliation stores the version it read in the same way; two SMS instances handling the
         same attendance are serialised on the per-attendance version record (one waits or fails and
         is redelivered). Decide: one record or two (version per attendance; processed event id),
         their keys and unique constraints, how the serialisation is achieved (row lock on the version
         record, or insert conflict), and how long processed-event ids are kept (they grow with every
         event – kept, or cleaned after a window longer than redelivery and dead-letter replay).
         Entity index and §5 here; columns in PMS-HLD-Part03-M4-SMS.
     (b) Audit table per module (Part02 §6.4, D-101, D-110 (12), FR-ADM-101 to 105, BR-CMN-07, 19):
         one append-only audit table in each service database (eims, ams, lms, sms), written in the
         same local transaction as the change; one entry per changed field with record type, record
         id, field, old value, new value, process (API id, job id or event type), user (Employee Id,
         Admin user name, System, or the event envelope actor), UTC time and flow reference; kept as
         long as the record; sensitive values kept in full and protected like the record; passwords
         never recorded. Decide: whether the anchor fixes one common audit structure for all four
         services (like the common columns in §2.4) with the module documents only listing what they
         audit, how append-only is enforced (no update / delete grant for the service user, or
         another way), classification and access of the old / new values (e.g. Day Wage Rate and
         Amount are sensitive, D-93), and the indexes needed for the history extract (ADM0020).
         Volume: about 490,000 entries a year, about 0.75 GB by year 5 (Part01 §17).
     (c) Outbox table and its clean-up rule – the ADR-006 follow-up (Part01 §8.3, §17: about 26,400
         rows a year plus reopens, about 65 MB by year 5; AP-EIP-61 message store, AP-DATA-11).
         Present the options with trade-offs (keep all sent rows; delete or move sent rows after a
         retention window; keep them as long as the attendance) and ask me. If a clean-up job is
         needed, it gets a job id, an owner (AMS) and a row in Part02 §7.3 (that anchor says the
         clean-up job is defined here). Record the rule in §7 and §8, and close the follow-up in the
         ADR-006 file and the Ref of AP-EIP-61 and AP-DATA-11 in Part01a.
     (d) Record version on every business record (Part02 §6.1 Concurrency, FR-CMN-014, NFR-06,
         Part01 §12): an integer, raised by 1 on each change, carried in every command and in events
         as subject.version. Fix in §2.3 / §2.4: column name (the template says row_version), start
         value, that it is on every business record (employee, profile change request, attendance,
         leave request, salary record) and not "where applicable", and which tables have none
         (audit, outbox, processed-event, run record – append-only or system tables).
     (e) Reconciliation run record (XF-04 step 5, FR-SMS-043 to 045, D-90, D-93, SMS0100, SMS0120):
         a job-log entity in sms – start, end, result, counts of records created and voided and of
         mismatches, flow reference – read by the Admin dashboard card for the last run. Decide where
         the individual mismatches (FR-SMS-044, logged, never changed) are kept (rows linked to the
         run, or the activity log only), its retention, and its type in the entity index (log). The
         job lock that keeps one run at a time (Part01 §8.3) is listed with it as a system table.
     (f) Employee Id sequence gaps (OI-P02-01; FR-EIMS-040, BR-EIMS-01: "EMP" + 4-digit sequence,
         unique, never reused, example "highest EMP0012 → next EMP0013"): the data side only – the
         generator (database sequence, or a counter row updated in the EIMS transaction) and whether a
         failed onboarding may leave a gap. Present the options with their effect on gaps and on
         concurrent onboarding, ask me, and record the convention in §2.3 (business identifiers).
         The order of the identity-provider call and the EIMS commit and the recovery stay with
         PMS-HLD-Part02-M5-SUP; update the OI-P02-01 status text in Part02 §10.1 only to say which part
         this document settled.
   - Other items to check while drafting: OI-P02-02 (check-then-act across databases) stays open
     for PMS-HLD-Part02-M2-AMS – note any data-side option in §9.1 only, do not decide it here;
     OI-P01a-16 (migration reversal plan) stays with docs/04-standards/database-and-data – §8 gives
     only the approach; identity-provider data (accounts, credentials, sessions, security events) is
     not modelled by PMS (ADR-003) and is listed in §2.2 as owned by the identity provider; cached
     copies of other services' data are short-lived in memory only (Part01 §12), no replicated
     tables, unless you find a function in Part02 §4 that needs one.
   - Common-column and format rules to apply from the approved inputs: timestamps in UTC, business
     dates as dates meaning the IST calendar date (BR-CMN-18, AP-DATA-13, D-117); amounts and rates
     with 2 decimals in INR, no currency column (D-08, Part02 §6.1); status values as upper-case
     codes from the module BRDs §6 (Part02 §6.1); records never physically deleted (BR-CMN-06);
     engine-specific types only for PostgreSQL 18 (D-115, Part01 §11).
   - No standards documents yet (D-108): rules that a standard will detail refer to
     "docs/04-standards/database-and-data (planned)" (area names of Part01a §2).
   - Template: templates/03-hld/hld-part03-anchor-datamodel-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master. Document ID
     PMS-HLD-Part03-Datamodel-v1.0, revision 0.1 at first draft.
   - The anchor holds conventions, ownership, the entity index with links, the entity-level master
     ER, cross-service consistency and roll-ups; columns are defined only in module documents
     (the common columns of §2.4, and the common audit structure if you decide so under (b), are the
     only column lists here); database per service (eims, ams, lms, sms), no cross-database foreign
     keys – a reference to another service's record is held as its business key (e.g. Employee Id)
     and checked through that service's API.
   - Entity index (§3.2): one row per entity and system table (business records, audit, outbox,
     processed-event and version records, run record, job lock), with its module document section
     as "Module document (planned)" and type master / transaction / history / config / log /
     reference; ask me in the first round whether system tables are listed with the business entities
     or in a separate group.
   - Master ER (§4.1): entity level only, grouped by owning service, cross-service references drawn
     as dashed lines, with its text-version table. Cross-service data (§5): one row per data object
     another service uses – at least INT-01 / INT-02 (attendance → salary record), INT-04 approver,
     INT-05 hourly wage rate, INT-06, INT-09, INT-10, the reconciliation query and the dashboard
     composition (INT-07) – with mechanism, consistency and reconciliation from Part02 §5.
   - Roll-ups §6 and §7 are filled from the BRD (§9 sensitivity, §13 volumetrics) and Part01 §17
     where they already give the figure; the rest is "Module document (planned)".
   - Before drafting, read the inputs and ask me the Part03 anchor gaps first, starting with (a) to
     (f) above.
   - Draft in this order, one review at a time: §1–§3, then §4–§5, then §6–§8, then §9.
   - Every approved review adds a revision row to §1.1. Open items of this document are
     OI-P03-nn in §9.1. Changes to other documents are allowed only for the items handed over above,
     each with its own revision row and after my "yes": the ADR-006 follow-up note, the Ref column
     of the Part01a items settled here (Part01a revision row), Part02 anchor §7.3 (a clean-up job, if
     any) and the OI-P02-01 status text in Part02 §10.1 (Part02 revision row).

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me design questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - New ADRs only for new significant decisions (e.g. an outbox clean-up rule that changes
     ADR-006), after my "yes"; register them in Part01a §5 and Part01 §18.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants (Claude, BMAD or any other) anywhere in the
     document, and no description of the delivery as AI-driven.
   - PR-04: take a usage reading at session start and at every outcome commit (in the Claude app:
     "show me where this session's tokens went"); append one row per outcome with the difference
     to memory/usage/token-log.csv (stage 3, outcome PMS-HLD-Part03-Datamodel, module ALL) and the
     reading itself, with its group split, to memory/usage/session-readings.csv; quote any text that
     contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
     A single device-shell command is limited in size: write long content in several parts.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, list them and ask once for delete
     permission on D:\POC\PMS, then remove only those files after each commit in this session.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the Part03 anchor: list every module data-model document (M1-EIMS, M2-AMS,
   M3-LMS, M4-SMS, M5-SUP) as "Not started" in §3.1, record how items (a) to (f) were settled or
   re-routed (a short "Items brought forward from Part02" table in §9, as Part02 §10.2 did), add a
   session handoff note in memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md
   and to this prompt file's header, and stop before the next HLD document until I say go. Remind me
   to refresh the SDLC dashboard (smd/prompt/execute-prompt-file-smd-update-prompt.md) and that the
   next prompt is hld-part02-m1-eims-functional (from templates/00-prompt, prompt pair
   hld-part02-mN-mod-functional), with OI-P01a-08 (threat-modelling method) still due before it.

Start by loading the context, then show me the Part03 anchor gaps you found (first round of questions).
```
