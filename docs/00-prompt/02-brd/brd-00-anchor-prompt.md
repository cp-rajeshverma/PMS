# Prompt – PMS-BRD (anchor)

| Field | Value |
| --- | --- |
| Document | docs/02-brd/PMS-BRD.md |
| Template | templates/02-brd/brd-anchor-template.md |
| Used | 18 Nov 2026 (first draft); later revisions 0.3–0.6 came from module work |
| Outcome | Anchor v1.0 rev 0.2 approved section by section (D-55 to D-69); now rev 0.6 |
| Status | Done – reuse only to revise the anchor |

## Prompt

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
We are starting Step 3: BRD. Today: the BRD anchor, docs/02-brd/PMS-BRD.md.

1. Load context first (read, don't summarise back to me):
   - CLAUDE.md and memory/project/project-rules.md
     (PR-01: never use BMAD gds-* agents; PR-02: never use NPQMS reference content;
      PR-03: customer-facing documents never mention AI tools/agents – author is
      "Rajesh Verma (Enterprise Architect)", human-accountable wording only)
   - memory/project/design-artifact-conventions.md
   - the latest handoff notes in memory/sessions/
   - docs/decisions/decision-log.md (newest first; use the next free D-id)

2. Inputs for the BRD:
   - Approved UX (Step 2): docs/01-ux/ux-journey-index.md, docs/01-ux/ux-summary/*.md,
     docs/01-ux/mockups/html/*.html
   - Baseline BRD v1.0 in Claude Docs (artifact dc21fe25-f34d-426d-ade4-e9b5c2312ef1) –
     input only, not the master; cite it as "PMS – Business Requirements Document (baseline) v1.0"
   - Templates: templates/02-brd/brd-anchor-template.md, brd-module-template.md, brd-sup-template.md

3. Approach (D-53):
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - Order: PMS-BRD.md (anchor) → M1-EIMS → M2-AMS → M3-LMS → M4-SMS → M5-SUP
     (SUP need-basis assessment after the module BRDs).
   - Today: draft only the anchor. Show me the outline first (section → input → what needs my
     input), then draft in reviews: §1–§3, §4, §5, §6, §7, §8, §9–§10, §11–§13.
   - The anchor holds only what spans modules: glossary, ID conventions and baseline id mapping,
     roles and role × module access, end-to-end process and journey index, shared dashboard and
     approvals inbox (FR-CMN), cross-module rules (BR-CMN), integrations (INT, JOB-CMN),
     system-wide NFRs and volumetrics, assumptions, risks, traceability roll-up, open items (OI).

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

Start by loading the context, then show me the outline of the anchor with what you will fill
from each input and what needs my input.
```

## Notes from the session

- Review roles use placeholders [BA], [HR Manager], [Finance Manager] until names are shared (D-55).
- Baseline ids were renumbered (BR-C → BR-CMN, EIMS-V → VR-EIMS, …); mapping in anchor §2.5.
- Shell requirements: login / password in SUP (AUTH), dashboard and approvals inbox in the anchor as FR-CMN (D-64).
