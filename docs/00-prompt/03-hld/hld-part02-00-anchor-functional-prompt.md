# Prompt – PMS-HLD-Part02-Functional

| Field | Value |
| --- | --- |
| Document | docs/03-hld/PMS-HLD-Part02-Functional.md |
| Template | templates/03-hld/hld-part02-anchor-functional-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 4: HLD (SDLC Stage 3 Solution Design, plan D-108: 23 Nov – 11 Dec 2026,
target go-live 29 Jan 2027). Today: the HLD Part02 Functional Design anchor,
docs/03-hld/PMS-HLD-Part02-Functional.md – the third of the 14 HLD documents (order D-108: Part01 →
Part01a → Part02 anchor → Part03 anchor → per module Part02 then Part03: EIMS, AMS, LMS, SMS, SUP).
Scope: module and function index, cross-module flows (XF-nn), common API / event / error / audit /
frontend conventions, roll-up inventories, cross-module NFR summary and requirement coverage.
Per-function designs belong only in the module documents (PMS-HLD-Part02-M1-EIMS … M4-SMS,
M5-SUP), which are not drafted yet: roll-ups that depend on them get "Module document (planned)"
and are completed as each module document is written (D-48).

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents – use bmad-* equivalents;
      PR-02: never read, search, quote or reuse NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents or describe the delivery as
      AI-driven – author is "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, every reading in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md (function ids <MOD>0010 in steps of 10;
     supporting prefixes ADM, UM, AUTH, NM, DM; API reference format
     [API-<MOD>-nn : METHOD /ctx/resource (Purpose : ...)]; API inventory as a roll-up keyed by API id;
     every diagram keeps a text-version table; designs stay technology-neutral)
   - the latest handoff note in memory/sessions/ (2026-11-23.md: Part01a outcome and the open items
     carried to the Part02 anchor)
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry,
     D-122 at the time of writing) and docs/decisions/adr/ (ADR-001 to ADR-006)
   - the approved BRD set v1.0 (D-107) in docs/02-brd/: PMS-BRD.md §3 (modules and scope),
     §4 (roles and data scope), §5 (end-to-end process, 30 journeys, shared dashboard and approvals
     inbox), §6 (cross-module rules BR-CMN), §7 (INT-01 to INT-10, JOB-CMN-01), §8 (NFR-01 to
     NFR-09), FR-CMN-001 to 016; the module BRDs M1-EIMS to M4-SMS and M5-SUP for their function
     lists (FR, US), statuses and NFRs – read further sections only when a row needs them
   - the UX set v1.1 (D-105): docs/01-ux/ux-journey-index.md, docs/01-ux/ux-summary/*.md
     (SCR-SH-00 layout and SCR-SH-03/04 dashboard and approvals inbox in particular) and the shared
     mockup assets in docs/01-ux/mockups/html/assets/
   - docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md v1.0 rev 0.9 – §5 functional
     architecture, §8 integration architecture (§8.2 catalogue, §8.3 outbox / topic / durable
     subscription / dead-letter, §8.4 protocol guide, §8.5 resilience defaults), §9.7–§9.9
     authorization, refused response and service-to-service identity, §10.3 standard log record,
     §10.5 flow reference, §14 load-test use cases, §16.3 NFR realization
   - docs/03-hld/PMS-HLD-Part01a-Principles-Patterns-Decisions.md v1.0 rev 0.5 – the catalogue
     readings to apply (groups G, I, J, F in particular) and §7 open items OI-P01a-01 to 17

2. Inputs for the Part02 anchor:
   - Decisions most relevant: D-10 (one service and entity per module), D-16 (gateway, identity
     provider, outbox + reconciliation, contract-first OpenAPI), D-18 (single repo, contracts-only
     sharing), D-23 / ADR-001 (build-time frontend packages in the shell), D-38 (per-function
     chapter structure), D-43, D-48 (Part02 split: anchor + module + SUP), D-57 (UM and AUTH in the
     POC; ADM, NM, DM Phase 2), D-58 and D-63 (Admin and manager data scope), D-70 (profile change
     request), D-77, D-84, D-90 (AMS, LMS, SMS rules), D-97, D-99, D-100, D-101 (SUP rules; audit and
     activity log with flow reference), D-104 (OI-02 to OI-04, OI-12 decided), D-105 (UX v1.1),
     D-109 to D-115 (Part01), D-116 to D-121 (Part01a)
   - ADRs: ADR-001 frontend composition; ADR-004 gateway holds the user tokens (session cookie,
     CSRF token); ADR-006 AMS → SMS outbox, idempotent consumer, nightly reconciliation (follow-up:
     event envelope and schema in contracts/events, set in the Part02 anchor)
   - Open items brought forward (must be answered or re-routed in this document):
     (a) OI-P01a-06 – ordering rule when an attendance-approved (INT-01) and an attendance-reopened
         (INT-02) event for the same attendance arrive late or out of order; the one real design gap
         from Part01a. Part01 gives: one topic, durable subscription, SMS replicas sharing the
         subscription queue, redelivery with backoff, dead-letter after 5 attempts, idempotency by
         event id and attendance id, one non-voided salary record per approved attendance (NFR-06),
         nightly reconciliation. Present the options with trade-offs (for example a per-attendance
         sequence or version number in the event that the consumer compares; the consumer re-reading
         the current attendance status from AMS before acting; broker message grouping per
         attendance id) and ask me; record the rule in §6.2 and the affected flow in §5.
     (b) OI-P01a-03 – shared design system (component library, style tokens) for the shell and the
         module packages: ask whether §6.5 defines it from the shared mockup assets and SCR-SH-00,
         or leaves it to docs/04-standards/frontend-and-ux (planned) – and close or re-route the
         open item accordingly.
     (c) Common conventions Part01 hands to this anchor: §6.1 API conventions (base path per module
         context /eims, /ams, /lms, /sms through the gateway; resource naming; methods and status
         codes; pagination; version check on commands – FR-CMN-014, Part01 §8.4; correlation and
         trace headers X-Flow-Ref and traceparent – Part01 §10.5); §6.2 event envelope (event id,
         type, version, time, source, flow reference, trace context, acting user – Part01 §8.2,
         §9.9, §10.5) and delivery, ordering, idempotency and dead-letter rules; §6.3 error body and
         error code scheme with the flow reference shown as "Reference: <flow reference>"
         (FR-ADM-114; Part01 §8.2 row 12 and §10.3 name the common error catalogue here), including
         the neutral refused response that never reveals whether a record exists (FR-UM-015).
   - Other items handed over by Part01 / Part01a to check while drafting: the INT-10 caller
     (Part01 §8.2 row 11 "fixed in Part02"); competing consumers on the SMS subscription
     (Part01a AP-CP-11, Part02 planned); the version form in the API base path (relates to
     OI-P01a-11, whose scheme stays with the API standard); the dead-letter replay procedure stays
     with OI-P01a-07 unless you decide otherwise.
   - No notifications in the POC (C-05; NM Phase 2): §7.4 states this; reminders are dashboard
     to-dos and approvals-inbox items (BRD §5.3).
   - No standards documents yet (D-108): conventions that standards will detail get
     "docs/04-standards/<area> (planned)" as reference, using the area names in Part01a §2.
   - Template: templates/03-hld/hld-part02-anchor-functional-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master. Document ID
     PMS-HLD-Part02-Functional-v1.0, revision 0.1 at first draft.
   - The anchor holds the module and function index, cross-module flows, common API, event,
     error, audit and frontend conventions, roll-up inventories and requirement coverage; function
     designs are only in the module documents. Business statuses stay in the module BRDs §6; the
     HLD holds only their technical handling.
   - Function index (§4): one row per function, ids <MOD>0010, <MOD>0020 … per module and UM / AUTH
     for SUP (ADM only for the POC part FR-ADM-101 to 117); derived from the BRD functional
     requirements and journeys; ask me the grouping rule (one function per journey / screen action /
     FR group) in the first round.
   - Cross-module flows (§5): candidates from BRD §5 and §7 – for example onboarding and account
     creation (INT-08), attendance approval → salary generation (INT-01), dispute → reopen → void
     (INT-02), nightly reconciliation (JOB-CMN-01), dashboard and approvals inbox composition
     (INT-07), attendance / leave date check (INT-06), joining-date change check (INT-09), manager
     change moving waiting items (D-104, OI-04), deactivation and session ending (D-97, D-111);
     confirm the list with me before drafting. Each flow gets a diagram plus its text-version table.
   - Product names never appear (technology-neutral, as Part01 §2); use the neutral terms of
     Part01 (identity provider, broker, gateway, edge).
   - Before drafting, read the inputs and ask me the Part02 anchor gaps first, starting with (a),
     (b) and (c) above.
   - Draft in this order, one review at a time: §1–§3, then §4–§5, then §6, then §7–§10.
   - Every approved review adds a revision row to §1.1. Open items of this document are
     OI-P02-nn in §10.1; an OI-P01a item settled here is marked closed in Part01a §7 with a Part01a
     revision row (the only Part01a change allowed in this session).

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me design questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - New ADRs only for new significant decisions (e.g. the event-ordering rule if it departs from
     ADR-006), after my "yes"; register them in Part01a §5 and Part01 §18.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants (Claude, BMAD or any other) anywhere in the
     document, and no description of the delivery as AI-driven.
   - PR-04: take a usage reading at session start and at every outcome commit (in the Claude app:
     "show me where this session's tokens went"); append one row per outcome with the difference
     to memory/usage/token-log.csv (stage 3, outcome PMS-HLD-Part02-Functional, module ALL) and the
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

5. At the end of the Part02 anchor: list every module document (M1-EIMS, M2-AMS, M3-LMS, M4-SMS,
   M5-SUP) as "Not started" in §2.2, record which OI-P01a items were closed or re-routed, add a
   session handoff note in memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md
   and to this prompt file's header, and stop before the next HLD document until I say go. Remind me
   to refresh the SDLC dashboard (smd/prompt/execute-prompt-file-smd-update-prompt.md) and that the
   next prompt is hld-part03-00-anchor-datamodel (from templates/00-prompt).

Start by loading the context, then show me the Part02 anchor gaps you found (first round of questions).
```
