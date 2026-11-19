# PMS – Session prompts

Internal working prompts used to start each document-drafting session. Not part of the customer deliverable set (PR-03 applies to the documents these prompts produce, not to the prompts).

Each prompt is self-contained: paste it into a new session with the PMS folder (D:\POC\PMS) connected. Prompts for documents already written record how they were produced and can be reused to revise them.

| File | Document produced | Status | Decisions |
| --- | --- | --- | --- |
| brd-00-anchor-prompt.md | docs/02-brd/PMS-BRD.md | Used 18 Nov 2026 – anchor drafted, now rev 0.8 | D-55 to D-69 |
| brd-m1-eims-prompt.md | docs/02-brd/PMS-BRD-M1-EIMS.md | Used 18 Nov 2026 – drafted, approval pending open items | D-70 to D-76 |
| brd-m2-ams-prompt.md | docs/02-brd/PMS-BRD-M2-AMS.md | Used 19 Nov 2026 – drafted, approval pending open items | D-77 to D-81 |
| brd-m3-lms-prompt.md | docs/02-brd/PMS-BRD-M3-LMS.md | Used 19 Nov 2026 – drafted, approval pending open items | D-84 to D-88 |
| brd-m4-sms-prompt.md | docs/02-brd/PMS-BRD-M4-SMS.md | Ready – next session | from D-89 |

The prompt for PMS-BRD-M5-SUP is added after SMS.

**Execute prompts:** `execute-prompt-file-<prompt>.md` holds the short message to paste into a new session to run a prompt file – one per prompt file (anchor, M1-EIMS, M2-AMS, M3-LMS, M4-SMS). The SDLC dashboard refresh has its own in `smd/prompt/execute-prompt-file-smd-update-prompt.md`.
