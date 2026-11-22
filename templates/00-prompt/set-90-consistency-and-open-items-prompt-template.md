# Prompt – <PRJ> <SET> set: consistency check and open-items note

> Template guidance (delete this block in the prompt file)
> - Produces a set-level gate prompt `docs/00-prompt/<nn-set>/set-90-consistency-and-open-items-prompt.md`, with `set` replaced by the document set it checks (for example `brd`, `hld-part02`, `hld-part03`), e.g. `brd-90-consistency-and-open-items-prompt.md`. Use it once all documents of a set are drafted and before the stage gate's stakeholder review. Replace `<SET>` and every `<…>` placeholder; delete lines that do not apply. Write it into the set's prompt sub-folder `<nn-set>` (`01-ux`, `02-brd`, `03-hld`).
> - Part A checks the set for consistency (ids and counts, cross-references, coverage, decisions, terms and status lists, versions, customer-facing rules) and writes a report; Part B prepares a decision note on the open business items for the business owner. The prompt never closes an open item – the business owner decides.
> - Review documents go to `docs/<stage folder>/reviews/` (customer-facing, PR-03). Name the set's anchor document, the next free decision id, open-item id and anchor revision.
> - Write the prompt before the session starts and index it in `docs/00-prompt/README.md`; after the session fill Used and Outcome and set Status to "Done – reuse only to re-check the <SET> set".
> - Prompts are internal working files: the customer-facing rule applies to the documents the prompt produces, not to the prompt (D-83).
> - Keep it self-contained: a new session must be able to run it with only the repository folder connected. Name decisions, rules and open items by id.
> - Pair it with `execute-prompt-file-set-90-consistency-and-open-items-prompt-template.md`. Example of a filled prompt: `docs/00-prompt/02-brd/brd-90-consistency-and-open-items-prompt.md`.

| Field | Value |
| --- | --- |
| Document | docs/<stage folder>/reviews/<PRJ>-<SET>-Consistency-Report.md (check result); docs/<stage folder>/reviews/<PRJ>-<SET>-Open-Items-Note.md (note for <business owner>); fixes in the <SET> documents |
| Template | templates/00-prompt/set-90-consistency-and-open-items-prompt-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are closing Step 3: BRD (SDLC Stage 2). All six BRD documents are drafted (anchor
PMS-BRD v1.0 rev 0.13; PMS-BRD-M1-EIMS, M2-AMS, M3-LMS, M4-SMS, M5-SUP at v1.0 rev 0.1).
Today, in this order: (A) a consistency check of the BRD set, then (B) a decision note on the
open business items for the HR Manager. Next free decision id: D-103 (check the log first).

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents; PR-02: never use NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only;
      PR-04: token usage per stage + outcome in memory/usage/token-log.csv, readings in
      memory/usage/session-readings.csv)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/ (2026-11-20.md)
   - docs/decisions/decision-log.md (newest first)
   - all six BRD documents in docs/02-brd/ in full
   - docs/01-ux/ux-journey-index.md (journeys, screens, navigation map, status lists)
   - the templates in templates/02-brd/ (section structure each document must follow)

2. Part A – consistency check. Check the BRD set against itself, the UX index and the
   decision log, and list every finding with document, section, id, issue and proposed fix:
   a. Ids: every FR / BR / VR / NFR / NOT / RPT / JOB / INT / US / OI id is unique, follows
      anchor §2.5, and the counts in anchor §11 and §2.3 match the module documents
      (FR numbering gaps are by design – D-74 to D-102).
   b. Cross-references: every id cited in one document exists where it is cited from
      (for example FR-EIMS-005 ↔ FR-UM-006, FR-EIMS-018 ↔ FR-UM-007, INT-01 to INT-10,
      BR-CMN-01 to 19, NFR-01 to 09, OI-01 to OI-11, OI-EIMS-01, 02); no dangling or
      superseded reference (e.g. baseline BR-C5 wording replaced by D-70).
   c. Coverage: each of the 30 journeys and 17 screens is assigned to exactly one BRD
      document (anchor §11) and is covered by at least one requirement there.
   d. Decisions: every rule traces to an approved decision; later decisions that amend
      earlier ones (e.g. D-70 → D-02, D-58 → baseline Admin access, D-100 → D-97) are
      reflected everywhere; no requirement contradicts a decision.
   e. Terms and status lists: glossary terms, role names, status codes and messages are
      used the same way in every document and match the UX status lists.
   f. Versions and references: §1.1 revision rows, §2.2 reference versions (anchor rev,
      decision range) are current; open-item status is the same wherever an item appears.
   g. Customer-facing rules: no AI tool, agent or assistant named anywhere (PR-03);
      no identity product named (technology-neutral, D-97); author line correct.
   Review documents live in docs/02-brd/reviews/ (create the folder if needed).
   Classify each finding: Editorial (wording, stale reference, count) – fix directly;
   Content (a requirement or rule changes) – propose the change, apply after my "yes";
   Business question – record as a new open item in the anchor §12 (next OI-12) for Part B.
   Write the result to docs/02-brd/reviews/PMS-BRD-Consistency-Report.md (customer-facing, PR-03):
   document control, scope and method, summary counts by class and document, findings
   table (id CC-01…, document, section, item, issue, class, fix / status), and open items
   raised. Present the findings to me in groups of at most 10 before fixing.
   Any change to a BRD gets a new revision row in that document (anchor next rev 0.14) and
   is named in the decision.

3. Part B – open-items note for the HR Manager. Cover the open business items that block
   BRD approval: OI-02, OI-03, OI-04 (anchor §12), OI-EIMS-01, OI-EIMS-02 (PMS-BRD-M1-EIMS
   §16) and any new business open item from Part A. For each: the question in plain
   business language, why it matters (which documents and requirements it blocks), 2–3
   options with their effect on users and on the BRD, my recommended option first, and the
   decision needed by when. Write it to docs/02-brd/reviews/PMS-BRD-Open-Items-Note.md
   (customer-facing, PR-03; addressed to the HR Manager, from Rajesh Verma (Enterprise
   Architect)); keep it to about two pages. Before writing, ask me for my recommendation on
   each item using the question tool (max 4 per round, your recommended answer first).
   Do not close any open item in this session – the HR Manager decides; the note only
   prepares the decision.

4. Working rules:
   - Never invent requirements; record gaps as open items.
   - Ask me questions a few at a time (max 4 per round), each with your recommended answer
     first, using the question tool. If I ask what an option means, explain, then re-ask.
   - After Part A and after Part B propose one decision-log entry each and write it only
     after my "yes". Do not move from Part A to Part B without my go-ahead.
   - PR-04: take a usage reading at session start and at every outcome commit (in the
     Claude app: "show me where this session's tokens went"); append one row per outcome
     (stage 2, outcomes "BRD consistency check" and "BRD open-items note") with the
     difference to memory/usage/token-log.csv and the reading itself, with its group split,
     to memory/usage/session-readings.csv; quote any text that contains commas; never
     invent figures. Also add the missing row for the SMD refresh of 20 Nov (stage X,
     commit 637739a) as not-recorded unless a reading exists.
   - Commit locally after each approved part with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. The
     device shell cannot write /tmp – keep scratch files in $HOME and never read leftovers
     from /tmp.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching
     them.
   - Keep messages concise: what was checked or drafted, points to check, proposed decision.

5. At the end: update anchor §12 if open items were added, add a session handoff note in
   memory/sessions/<date>.md, add the outcome to docs/00-prompt/README.md and to this
   prompt file's header, and stop until I say go. Remind me to refresh the SDLC dashboard
   (smd/prompt/execute-prompt-file-smd-update-prompt.md) and list what remains for the
   Stage 2 gate (HR Manager decisions, UX update OI-01 and OI-06 to OI-11, stakeholder
   review with named reviewers, sign-off).

Start by loading the context, then show me the Part A findings (first group).
```
