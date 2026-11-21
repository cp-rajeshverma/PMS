# SMD – SDLC Monitoring & Dashboard (PMS)

A read-only, static, single-file HTML dashboard of the PMS delivery lifecycle, generated from this repository.

## View it

- **Inside a checkout:** open `smd/web/PMS_SMD_Dashboard.html` (double-click). Every artifact, decision and code-file link opens the real file from the repository; ↗ opens it on GitHub; ⧉ copies the path.
- **As an attachment:** send `smd/web/PMS_SMD_Dashboard.html` on its own. All screens work offline; a banner explains that file links need a checkout (GitHub links still work).
- Print / Save as PDF from the Overview gives a one-page status report.

## Screens

Overview (pipeline strip, KPIs, Done / Doing / Next, changes, timeline) · Stage 0–8 detail (gate, steps, milestones, artifacts, decisions) · Build matrix · Artifacts · Repository browser · Reviews & gaps (coverage, open items, reviews) · Decisions · Risks · Activity · Change requests · Trend · Data & quality.

## Files

| File | Purpose |
| --- | --- |
| `prompt/` | Generate, update and conventions prompts; `SDLC-Pipe_Master_Prompt.md` is the phase-2 dynamic app (not used by SMD) |
| `smd-config.yaml` | Stages, repo-path mapping, exclusions, ID patterns, audience (customer-facing) |
| `CONVENTIONS.md` | Front-matter, review, decision, story and CR file conventions |
| `smd-data.json` | Current dashboard data (source copy of the embedded block) |
| `smd-template.html` | Renderer (HTML + CSS + vanilla JS, empty data placeholder) |
| `build.mjs` | Injects the data into the template, checks every linked path, writes `web/` |
| `web/` | Generated output: `PMS_SMD_Dashboard.html` (one dashboard, D-96) and `.smd-anchor.png` (checkout detection). Its Overview ends with two internal sections – token utilization per stage › outcome (`memory/usage/token-log.csv`) and whole-session token readings (`memory/usage/session-readings.csv`), rule PR-04 |
| `snapshots/` | Data snapshot per refresh (history and trend) |
| `CHANGELOG.md` | One entry per refresh |

## How the dashboard is built

`PMS_SMD_Dashboard.html` = `smd-template.html` (layout, styles and the code for every screen, with empty data placeholders) + `smd-data.json` (all content) + the internal token logs, combined by `node smd/build.mjs`. Change the look in the template, the content in the data; never edit the generated file. Opened on its own, the template shows no data – that is expected.

## Refresh

Run `smd/prompt/smd-update-prompt.md` with an agent that has access to the repository. To rebuild from existing data only: `node smd/build.mjs` (Node 18+, no dependencies).

## Audience rule

The dashboard is customer-facing (project rule PR-03 / D-60): it never names AI tools or agents. Agent tooling folders, agent instructions and memory are excluded; working sessions are summarised only. **Before sharing the dashboard with the customer, remove the two "(internal view)" token sections** (everything between the `TK-START` / `TK-END` markers in the generated file) (D-96).
