# PMS – Session prompts

Internal working prompts used to start each document-drafting session. Not part of the customer deliverable set (PR-03 applies to the documents these prompts produce, not to the prompts).

Each prompt is self-contained: paste it into a new session with the PMS folder (D:\POC\PMS) connected. Prompts for documents already written record how they were produced and can be reused to revise them.

| File | Document produced | Status | Decisions |
| --- | --- | --- | --- |
| brd-00-anchor-prompt.md | docs/02-brd/PMS-BRD.md | Used 18 Nov 2026 – anchor drafted, now rev 0.15 (business open items closed, D-104) | D-55 to D-69 |
| brd-m1-eims-prompt.md | docs/02-brd/PMS-BRD-M1-EIMS.md | Used 18 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-70 to D-76 |
| brd-m2-ams-prompt.md | docs/02-brd/PMS-BRD-M2-AMS.md | Used 19 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-77 to D-81 |
| brd-m3-lms-prompt.md | docs/02-brd/PMS-BRD-M3-LMS.md | Used 19 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-84 to D-88 |
| brd-m4-sms-prompt.md | docs/02-brd/PMS-BRD-M4-SMS.md | Used 19 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) | D-90 to D-94 |
| brd-m5-sup-prompt.md | docs/02-brd/PMS-BRD-M5-SUP.md | Used 20 Nov 2026 – drafted, now rev 0.3; business open items closed (D-104) (UM, AUTH, audit and activity log; ADM, NM, DM Phase 2) | D-97 to D-102 |
| brd-90-consistency-and-open-items-prompt.md | docs/02-brd/reviews/PMS-BRD-Consistency-Report.md, docs/02-brd/reviews/PMS-BRD-Open-Items-Note.md (fixes in the BRD set) | Used 20 Nov 2026 – consistency check CC-01 to CC-28 (26 editorial, 1 content fixed; OI-12 raised); open-items note; OI-02, OI-03, OI-04, OI-12, OI-EIMS-01, OI-EIMS-02 decided by the product owner on behalf of the HR Manager (option A) | D-103, D-104 |

New prompt and execute-prompt files start from the templates in `templates/00-prompt/` (D-95): one pair per document template, named after the prompt file they produce – for example `brd-mN-mod-prompt-template.md` and `execute-prompt-file-brd-mN-mod-prompt-template.md`.

**Execute prompts:** `execute-prompt-file-<prompt>.md` holds the short message to paste into a new session to run a prompt file – one per prompt file (anchor, M1-EIMS, M2-AMS, M3-LMS, M4-SMS, M5-SUP, BRD consistency and open items). The SDLC dashboard refresh has its own in `smd/prompt/execute-prompt-file-smd-update-prompt.md`.
