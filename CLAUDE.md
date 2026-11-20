# PMS – Payroll Management System (POC)

Project memory for AI agents. Read this first in every session.

## Mandatory rules

- **Never use the BMAD GDS (game development) module.** It is not relevant to PMS. Do not invoke or suggest any `gds-*` skill or agent; use the BMM (`bmad-*`) equivalents. (PR-01, decision D-17)
- **Do not use the NPQMS-HLD reference documents** (`NPQMS-*`) for PMS content. They only shaped the frozen templates; ignore any NPQMS result from project search. (PR-02, decision D-54)
- **Customer-facing documents never mention AI tools or agents** (Claude, BMAD, etc.) as authors, users or sources; author is Rajesh Verma (Enterprise Architect). (PR-03, decision D-60)
- **Log token consumption per stage + outcome/artifact** in `memory/usage/token-log.csv` at each outcome checkpoint (not only at session close); also keep each reading in `memory/usage/session-readings.csv`; internal only – shown in the "(internal view)" sections of the single SMD dashboard, removed manually before sharing with the customer. (PR-04, decisions D-89, D-96)
- Full rule list: `memory/project/project-rules.md`.

## Memory layout

| Layer | Location |
| --- | --- |
| Platform | `memory/platform/` – org-wide standards |
| Project | `CLAUDE.md`, `memory/project/`, `docs/` |
| User | Each user's own AI config (not committed) |
| Session | `memory/sessions/<yyyy-mm-dd>.md`, BMAD story files |

See `README.md` for the repository layout and lifecycle.
