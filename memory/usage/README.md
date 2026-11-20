# Token usage log (internal – PR-04)

`token-log.csv` records token consumption at **stage + outcome/artifact** level. `session-readings.csv` keeps every cumulative session reading as taken, with its group split (instructions, files and commands, documents, conversation, other). Both are internal: they feed the two "(internal view)" sections of the single SMD dashboard `smd/web/PMS_SMD_Dashboard.html`, which are removed manually before the dashboard is shared with the customer (D-96, PR-03).

## When to log – per outcome, not per session

A session can produce several outcomes, so log at **outcome checkpoints**:

1. At session start (or right after the previous outcome is logged) take a **cumulative usage reading** for the session.
2. When an outcome/artifact is completed (typically at its commit), take a new cumulative reading and append **one row with the difference** since the previous reading. Also append the reading itself to `session-readings.csv` (columns: `date, session, checkpoint, requests, input, cache_write, cache_read, output, total, instructions_pct, files_pct, documents_pct, conversation_pct, other_pct, source, ref, note`; the group percentages come from the usage explanation).
3. Work that is not an artifact (reviews, refactors, dashboards, housekeeping) is logged against the closest outcome or as stage `X`.
4. If a session ends mid-outcome, log the partial delta with the same `outcome` value; the dashboard sums rows.

How to read the cumulative usage:
- Cowork / Claude app: ask "show me where this session's tokens went" (usage explanation); use the `tokens` totals and `requests`.
- Claude Code: `/cost` (or the telemetry export, if configured).
- API: Admin usage report for the workspace / key.
If no reading is possible, log the row with empty token columns and `source=estimated` plus a note, or `not-recorded`. Never invent figures.

## Columns

| Column | Meaning |
| --- | --- |
| date | yyyy-mm-dd (IST) when the outcome checkpoint is logged |
| stage | 0–8 from `smd/smd-config.yaml`, or `X` = cross-stage governance and tooling (SMD, prompts, repo housekeeping) |
| outcome | Artifact code (e.g. `PMS-BRD-M4-SMS`) or a short outcome name (e.g. `UX mockups – LMS`). Use module-wise names so the dashboard can group per module |
| module | ALL, EIMS, AMS, LMS, SMS, SUP |
| activity | Short description (draft, section review, rework, refresh…) |
| requests | Number of model requests in the delta, if known |
| input, cache_write, cache_read, output | Token counts of the delta |
| total | input + cache_write + cache_read + output |
| source | `measured`, `estimated` or `not-recorded` |
| ref | Commit hash or decision id that closed the outcome |
| note | Free text; no secrets, personal data or payroll figures |

Effective (cost-weighted) tokens used by the dashboard: input × 1 + cache_write × 2 + cache_read × 0.1 + output × 5.
