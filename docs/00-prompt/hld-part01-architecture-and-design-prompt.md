# Prompt – PMS-HLD-Part01-Architecture-and-Design

| Field | Value |
| --- | --- |
| Document | docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md |
| Template | templates/03-hld/hld-part01-architecture-and-design-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are starting Step 4: HLD (SDLC Stage 3 Solution Design, plan D-108: 23 Nov – 11 Dec 2026,
target go-live 29 Jan 2027). Today: HLD Part01 Architecture and Design,
docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md – the first of the 14 HLD documents
(order D-108: Part01 → Part01a → Part02 anchor → Part03 anchor → per module Part02 then Part03).
Part01a is not drafted yet: §4 (principles and patterns) and §18 (architecture decisions) carry
the PMS content known today and refer to PMS-HLD-Part01a-Principles-Patterns-Decisions for the
catalogue and the ADR register; §12 (data architecture) is a summary that Part03 details.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents – use bmad-* equivalents;
      PR-02: never read, search, quote or reuse NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, every reading in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/
   - docs/decisions/decision-log.md (newest first; use the next free D-id after the newest entry)
     and docs/decisions/adr/ (ADR-001)
   - the approved BRD set v1.0 (D-107) in docs/02-brd/: PMS-BRD.md (anchor) – objectives incl.
     OBJ-06 (§3.2), scope and out of scope (§3.3), role catalogue and role × module access (§4.2,
     §4.3), end-to-end process and journeys (§5), BR-CMN rules (§6), INT-01 to INT-10 and
     JOB-CMN-01 (§7), NFR-01 to NFR-09 and volumetrics (§8, §8.1), A-01 to A-05, C-01 to C-07,
     DEP-01 to DEP-06 (§9), R-01 to R-08 (§10), future scope (§13.1); module BRDs
     PMS-BRD-M1-EIMS, M2-AMS, M3-LMS, M4-SMS for integrations, jobs and NFRs only;
     PMS-BRD-M5-SUP for UM and AUTH, audit log and activity log (input to Part01 §9 and §10)
   - UX: docs/01-ux/ux-journey-index.md v1.1 (screens, navigation, shell) – reference only

2. Inputs for the Part01:
   - Architecture and technology decisions: D-10 (one microservice and one database per module,
     every standard applies in full), D-11 (React + TypeScript, PostgreSQL, JWT + bcrypt, GitHub +
     GitHub Actions, Docker, Azure App Service + Azure Database for PostgreSQL, Dev/QA/Prod,
     Playwright, k6), D-12 (Java Spring Boot first, later replatformed to Node.js and Python
     FastAPI – designs stay technology-neutral), D-16 (Spring Cloud Gateway, Keycloak, database per
     service, event-driven AMS → SMS with outbox and nightly reconciliation on ActiveMQ,
     contract-first OpenAPI 3, JUnit 5 + Mockito + Testcontainers), D-18 (single repository,
     independent services: separate builds, path-filtered pipelines, contracts-only sharing),
     D-21 (ActiveMQ Artemis), D-23 / ADR-001 (frontend as build-time packages in
     platform/shell-ui; runtime micro-frontends after the POC), D-24 (reconciliation 01:00 IST;
     1366 px light theme), D-26 (idle timeout 30 min; lock 15 min after 5 failed sign-ins via the
     identity provider), D-28 (password policy), D-29 (role held in the identity provider),
     D-57 (UM and AUTH in the POC; ADM, NM, DM Phase 2), D-58 / D-63 (Admin and manager data
     scope), D-59 (NFR targets and volumetrics), D-97 and D-100 (SUP session, account and
     security-event rules), D-101 (audit log and activity log, flow reference, masking,
     retention 90 days), D-61 (12 OBJ-06 standards areas), D-108 (Stage 3 plan; standards in
     docs/04-standards/ after the HLD documents)
   - Repository layout as built so far: services/{eims,ams,lms,sms}, platform/{gateway,keycloak,
     shell-ui}, contracts/{openapi,events}, infra/{activemq,azure,docker,postgres}
   - No standards documents yet (D-108): Part01 refers to docs/04-standards/ by area only
   - Template: templates/03-hld/hld-part01-architecture-and-design-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master. Document ID
     PMS-HLD-Part01-Architecture-and-Design-v1.0, revision 0.1 at first draft.
   - Every diagram keeps a text-version table; designs stay technology-neutral where the
     replatforming goal (D-12) requires it – product names appear in the technology-specific
     sections (§6.2, §7, §9.2, §11) only; significant decisions get an ADR file in
     docs/decisions/adr/ and are listed for the Part01a §5 register.
   - Reference BRD ids (INT, JOB, NFR, C, DEP, R) instead of repeating requirement text.
   - Before drafting, read the inputs and ask me the Part01 gaps first – for example the
     JWT + bcrypt (D-11) versus Keycloak (D-16, D-29) reading, cloud network topology, per-tier
     redundancy, environments, data migration (none expected for the POC), MFA (not in the POC
     unless decided).
   - Draft in this order, one review at a time: §1–§4, then §5–§8, then §9–§10, then §11–§15,
     then §16–§20.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me architecture questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - Customer-facing documents follow PR-03: author "Rajesh Verma (Enterprise Architect)",
     no mention of AI tools, agents or assistants (Claude, BMAD or any other) anywhere in the
     document.
   - PR-04: take a usage reading at session start and at every outcome commit (in the Claude app:
     "show me where this session's tokens went"); append one row per outcome with the difference
     to memory/usage/token-log.csv (stage 3, outcome PMS-HLD-Part01-Architecture-and-Design,
     module ALL) and the reading itself, with its group split, to
     memory/usage/session-readings.csv; quote any text that contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the Part01: record the Part01 status and the ADR list to carry into Part01a,
   add a session handoff note in memory/sessions/<date>.md, add the outcome to
   docs/00-prompt/README.md and to this prompt file's header, and stop before the next HLD
   document until I say go. Remind me to refresh the SDLC dashboard
   (smd/prompt/execute-prompt-file-smd-update-prompt.md) and that the next prompt is
   hld-part01a-principles-patterns-decisions (from templates/00-prompt).

Start by loading the context, then show me the Part01 gaps you found (first round of questions).
```
