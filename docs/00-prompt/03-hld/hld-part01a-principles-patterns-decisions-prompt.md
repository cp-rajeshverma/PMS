# Prompt – PMS-HLD-Part01a-Principles-Patterns-Decisions

| Field | Value |
| --- | --- |
| Document | docs/03-hld/PMS-HLD-Part01a-Principles-Patterns-Decisions.md |
| Template | templates/03-hld/hld-part01a-principles-patterns-decisions-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are continuing Step 4: HLD (SDLC Stage 3 Solution Design, plan D-108: 23 Nov – 11 Dec 2026,
target go-live 29 Jan 2027). Today: HLD Part01a Principles, Patterns and Decisions,
docs/03-hld/PMS-HLD-Part01a-Principles-Patterns-Decisions.md – the second of the 14 HLD documents
(order D-108: Part01 → Part01a → Part02 anchor → Part03 anchor → per module Part02 then Part03).
Scope: the full catalogue of 330 items in 18 groups (A GOV 11, B XF 13, C WA 15, D SD 19, E TF 12,
F FE 10, G MS 34, H CP 44, I EIP 64, J INT 13, K DATA 17, L SEC 20, M OBS 12, N PERF 10, O RES 10,
P DEV 11, Q QA 10, R DG 5), the group summary (§3), the ADR register (§5) and the ADR format (§6).
Part02 and Part03 are not drafted yet: rows realised there get "Part02 / Part03 (planned)" as Ref.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents – use bmad-* equivalents;
      PR-02: never read, search, quote or reuse NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents or describe the delivery as
      AI-driven – author is "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, every reading in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/ (2026-11-22.md: Part01 status and the ADR list
     to carry into Part01a)
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry)
     and docs/decisions/adr/ (ADR-001 to ADR-006)
   - docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md v1.0 rev 0.8 (all sections approved,
     D-109 to D-116) – the main source: §4 already cites catalogue ids (XF, WA, MS, CP, EIP, INT),
     §5–§17 hold the design each row's Realization and Ref point to, §18 lists ADR-001 to ADR-006,
     §19 risks AR-01 to AR-09, §20 open items (OI-P01-01 closes with this document)
   - the approved BRD set v1.0 (D-107) in docs/02-brd/: PMS-BRD.md §8 (NFR-01 to NFR-09), §9
     (C-01 to C-07, DEP-01 to DEP-06) and PMS-BRD-M5-SUP §12 (NFR-SUP-01 to 05) – the qualities
     the principles serve; read other BRD sections only when a row needs them

2. Inputs for the Part01a:
   - Architecture decisions: D-10, D-11, D-12, D-16, D-18, D-21, D-23, D-26, D-28, D-29, D-57,
     D-58, D-59, D-60, D-61, D-97, D-100, D-101, D-108 to D-116
   - ADR files: ADR-001 frontend composition (D-23); ADR-002 hosting and runtime platform (D-109,
     D-110); ADR-003 identity provider issues tokens and holds passwords (D-109); ADR-004 API
     gateway holds the user tokens (D-110, D-111); ADR-005 edge on the Kubernetes Gateway API with
     WAF (D-112); ADR-006 AMS → SMS outbox, idempotent consumer and nightly reconciliation (D-16,
     D-113)
   - No standards documents yet (D-108): rows that standards will detail get
     "docs/04-standards/<area> (planned)" as Ref, by OBJ-06 area (D-61)
   - Template: templates/03-hld/hld-part01a-principles-patterns-decisions-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master. Document ID
     PMS-HLD-Part01a-Principles-Patterns-Decisions-v1.0, revision 0.1 at first draft.
   - For each catalogue row record Applicability (Applied / Partial / Deferred / N/A) with the
     reason, a one-line Realization and the Ref (Part01 section, ADR, Part02 / Part03 planned,
     standard planned). Rows are never deleted; project-specific rows go at the end of a group.
   - Keep Part01 consistent: where Part01 §4 already states an item, use the same reading; after
     the group counts are final, update Part01 §4.1 (counts) and close OI-P01-01 – that is the
     only Part01 change in this session, with a Part01 revision row.
   - Every ADR keeps its own file in docs/decisions/adr/; §5 lists ADR-001 to ADR-006 with their
     related catalogue ids; a catalogue row Deferred or N/A because of a decision references the
     ADR or D-id. New ADRs only for new significant decisions, after my "yes".
   - Product names appear only where Part01 allows them (realization text may name a product only
     when Part01 §6.2, §7, §9.2 or §11 already names it; otherwise use neutral terms).
   - Before drafting, read the inputs and ask me the Part01a gaps first. Group R is already decided
     (D-116): title "R. Delivery governance & knowledge management (DG)", ids AP-DG-01 to
     AP-DG-05, tool-neutral wording as in D-116 – the template's group R title and row texts are
     not used in the document. Known gaps to include:
     (a) the reading of "Cloud first" (AP-XF-05) as "cloud-ready" for the on-premises POC;
     (b) items Part01 leaves open (for example caching, service mesh, multi-AZ, MFA) –
     Deferred with the Future reference in Part01 §20.3.
   - Draft in this order, one review at a time: §1–§3, then §4 groups A–F, then groups G–L,
     then groups M–R, then §5–§6 (and the Part01 §4.1 counts).

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items (OI-P01a-nn).
   - Ask me architecture questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants (Claude, BMAD or any other) anywhere in the
     document, and no description of the delivery as AI-driven.
   - PR-04: take a usage reading at session start and at every outcome commit (in the Claude app:
     "show me where this session's tokens went"); append one row per outcome with the difference
     to memory/usage/token-log.csv (stage 3, outcome PMS-HLD-Part01a-Principles-Patterns-Decisions,
     module ALL) and the reading itself, with its group split, to
     memory/usage/session-readings.csv; quote any text that contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
     A single device-shell command is limited in size: write long content in several parts.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the Part01a: link the ADR register from Part01 §18 (Part01a §5), record the
   Part01 §4.1 counts and the closure of OI-P01-01, add a session handoff note in
   memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md and to this prompt
   file's header, and stop before the next HLD document until I say go. Remind me to refresh the
   SDLC dashboard (smd/prompt/execute-prompt-file-smd-update-prompt.md) and that the next prompt is
   hld-part02-00-anchor-functional (from templates/00-prompt).

Start by loading the context, then show me the Part01a gaps you found (first round of questions).
```
