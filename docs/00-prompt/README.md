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
| 03-hld/hld-part01-architecture-and-design-prompt.md | docs/03-hld/PMS-HLD-Part01-Architecture-and-Design.md | Used 22 Nov 2026 – all sections reviewed, v1.0 rev 0.5 (on-premises Kubernetes POC with AWS target, identity provider tokens, gateway session, outbox and reconciliation, latest stack); final approval at the Stage 3 gate; ADR-002 to ADR-006 | D-108 to D-113 |

New prompt and execute-prompt files start from the templates in `templates/00-prompt/` (D-95): one pair per document template, named after the prompt file they produce – for example `brd-mN-mod-prompt-template.md` and `execute-prompt-file-brd-mN-mod-prompt-template.md`.

**Execute prompts:** `execute-prompt-file-<prompt>.md`, in the same sub-folder as its prompt, holds the short message to paste into a new session to run a prompt file – one per prompt file (anchor, M1-EIMS, M2-AMS, M3-LMS, M4-SMS, M5-SUP, BRD consistency and open items, HLD Part01). The SDLC dashboard refresh has its own in `smd/prompt/execute-prompt-file-smd-update-prompt.md`.
