# PMS – Session prompts

Internal working prompts used to start each document-drafting session. Not part of the customer deliverable set (PR-03 applies to the documents these prompts produce, not to the prompts).

Prompts are grouped by SDLC document set in sub-folders that mirror `docs/`: `01-ux/`, `02-brd/`, `03-hld/` (later sets, e.g. `04-standards/`, are added with their first prompt); this README stays at the top and indexes all of them.

Each prompt is self-contained: paste it into a new session with the PMS folder (D:\POC\PMS) connected. Prompts for documents already written record how they were produced and can be reused to revise them.

| File | Document produced | Status | Decisions |
| --- | --- | --- | --- |
| 02-brd/brd-00-anchor-prompt.md | docs/02-brd/PMS-BRD.md | Used 18 Nov 2026 – anchor drafted, now rev 0.15 (business open items closed, D-104) | D-55 to D-69 |
| 02-brd/brd-m1-eims-prompt.md | docs/02-brd/PMS-BRD-M1-EIMS.md | Used 18 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-70 to D-76 |
| 02-brd/brd-m2-ams-prompt.md | docs/02-brd/PMS-BRD-M2-AMS.md | Used 19 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-77 to D-81 |
| 02-brd/brd-m3-lms-prompt.md | docs/02-brd/PMS-BRD-M3-LMS.md | Used 19 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-84 to D-88 |
| 02-brd/brd-m4-sms-prompt.md | docs/02-brd/PMS-BRD-M4-SMS.md | Used 19 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-90 to D-94 |
| 02-brd/brd-m5-sup-prompt.md | docs/02-brd/PMS-BRD-M5-SUP.md | Used 20 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) (UM, AUTH, audit and activity log; ADM, NM, DM Phase 2) | D-97 to D-102 |
| 02-brd/brd-90-consistency-and-open-items-prompt.md | docs/02-brd/reviews/PMS-BRD-Consistency-Report.md, docs/02-brd/reviews/PMS-BRD-Open-Items-Note.md (fixes in the BRD set) | Used 20 Nov 2026 – consistency check CC-01 to CC-28 (26 editorial, 1 content fixed; OI-12 raised); open-items note; OI-02, OI-03, OI-04, OI-12, OI-EIMS-01, OI-EIMS-02 decided by the product owner on behalf of the HR Manager (option A) | D-103, D-104 |
| 03-hld/hld-part01-architecture-and-design-prompt.md | docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md | Used 22 Nov 2026 – all sections reviewed, v1.0 rev 0.8 (on-premises Kubernetes POC with AWS target, identity provider tokens, gateway session, outbox and reconciliation, latest stack); final approval at the Stage 3 gate; ADR-002 to ADR-006 | D-108 to D-116 |
| 03-hld/hld-part01a-principles-patterns-decisions-prompt.md | docs/03-hld/PMS-HLD-Part01a-Principles-Patterns-Decisions.md | Used 23 Nov 2026 – all sections reviewed, v1.0 rev 0.5: 330 items assessed (230 Applied, 35 Partial, 3 Deferred, 62 N/A), ADR register ADR-001 to ADR-006, open items OI-P01a-01 to 17; Part01 rev 0.9 (§4.1 counts, OI-P01-01 closed); final approval at the Stage 3 gate | D-117 to D-121 |
| 03-hld/hld-part02-00-anchor-functional-prompt.md | docs/03-hld/PMS-HLD-Part02-Functional.md | Used 23 Nov 2026 – all sections reviewed, v1.0 rev 0.4: 77 functions (prefix SH added), flows XF-01 to XF-09, common API / event / error / audit / frontend conventions, event ordering by attendance version, shared design system, coverage of 175 FR ids; OI-P01a-03 and 06 closed (Part01a rev 0.6); open items OI-P02-01 and 02; final approval at the Stage 3 gate | D-122 to D-125 |
| 03-hld/hld-part03-00-anchor-datamodel-prompt.md | docs/03-hld/PMS-HLD-Part03-Datamodel.md | Ready for the next session – brings forward from the Part02 anchor: SMS per-attendance version and processed-event records, audit table per module, outbox clean-up rule (ADR-006 follow-up), record version on every business record, reconciliation run record, Employee Id sequence gaps (OI-P02-01) | – |

New prompt and execute-prompt files start from the templates in `templates/00-prompt/` (D-95): one pair per document template, named after the prompt file they produce – for example `brd-mN-mod-prompt-template.md` and `execute-prompt-file-brd-mN-mod-prompt-template.md`.

**Execute prompts:** `execute-prompt-file-<prompt>.md`, in the same sub-folder as its prompt, holds the short message to paste into a new session to run a prompt file – one per prompt file (anchor, M1-EIMS, M2-AMS, M3-LMS, M4-SMS, M5-SUP, BRD consistency and open items, HLD Part01, HLD Part01a, HLD Part02 anchor, HLD Part03 anchor). The SDLC dashboard refresh has its own in `smd/prompt/execute-prompt-file-smd-update-prompt.md`.
