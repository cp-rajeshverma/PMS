# SMD — SDLC Monitoring & Dashboard · UPDATE Prompt (recurring)

> **Location:** `D:\POC\PMS\smd\prompt\smd-update-prompt.md` · **Output:** `D:\POC\PMS\smd\web\PMS_SMD_Dashboard.html`
>
> **How to use:** Run this in an agent session with access to `D:\POC\PMS` whenever you want a fresh dashboard: end of day, after a stage gate, before a steering meeting, or after a BMAD agent session. It refreshes the **data only**. The renderer (`smd-template.html`) is not changed unless you explicitly ask.

---

**PROMPT START**

You are maintaining **SMD (SDLC Monitoring & Dashboard)** for the PMS project. SMD lives in `D:\POC\PMS\smd\` and is described in `smd/README.md`. Refresh the dashboard data from the current state of the repository.

## Inputs to read first
1. `smd/smd-config.yaml` (stages, path mapping, people)
2. `smd/CONVENTIONS.md` (front-matter, review, decision and CR file formats)
3. `smd/smd-data.json` (the previous data, i.e. the baseline for this refresh)
4. The latest file in `smd/snapshots/`

## Steps
1. **Detect changes.** If the repo is a git repo, list the commits since `meta.repo_commit` (author, date, files touched). Otherwise compare file modification times against `meta.generated_at`. Also look for new or changed files in the mapped artifact, review, decision, CR, story, agent-memory and session-log folders.
2. **Re-derive the data.**
   - Update artifacts, stages, steps, stories (coding steps), reviews, findings, coverage, decisions, CRs and risks, using the **source precedence** in the generate prompt (declared > config > git > inferred).
   - Refresh the `repo_files` index: add, rename or remove entries, update dates and authors, and relink to stories and artifacts. Keep `path` repo-relative so links from `smd/web/` (`../../<path>`) open the real file. Never index secrets files.
   - **Agent memory and session logs:** add one summarized `activity` entry per new session. Never copy raw log text, secrets, credentials, personal data or payroll figures.
   - Recompute stage `percent`, gate criteria `met`, pipeline `current_stage`, and app `health`. Health is **R** if any Critical finding is open or the current stage is more than 10 days past its planned end. It is **A** if any High finding is open or any item is overdue. Otherwise it is **G**. Always give a reason.
3. **Record the diff.** Fill `changes_since_last` with every status change, new artifact, version bump, new or closed finding, gate decision, and stage transition.
4. **Guardrails.**
   - Never move a stage backwards, or mark a gate Passed, **only on inference**. A change like that needs declared evidence (a review or decision file, or front-matter). If the evidence conflicts, keep the previous value and add a `data_quality.warnings` entry.
   - Never delete history. Removed artifacts become `status: "Superseded"` with a warning.
   - Do not edit project artifacts, code or logs. SMD only writes inside `smd/`, and never inside `smd/prompt/`. Ignore `smd/prompt/SDLC-Pipe_Master_Prompt.md`, which is for the phase-2 dynamic app.
   - If a new repo folder isn't covered by the mapping, don't guess silently. List it under warnings and propose a mapping line.
4a. **Token utilization (internal view, PR-04).**
   - Source: `memory/usage/token-log.csv` (format in `memory/usage/README.md`): one row per **stage + outcome/artifact** checkpoint, so a session with several outcomes has several rows. Read it; never write to it from SMD and never invent, estimate or back-fill figures (rows marked `not-recorded` stay "not recorded").
   - Check the log against the repo: every outcome completed since the last refresh (new or bumped artifact, approved section, stage transition, SMD refresh) should have at least one row. List missing ones under **Report back** as "token rows missing" (stage › outcome › closing commit) so they can be added; do not add them yourself.
   - Flag rows whose `stage` is not 0–8 or `X`, whose `outcome` matches no artifact code or known outcome name, or whose `total` differs from the sum of its columns.
   - `node smd/build.mjs` aggregates the log into the **internal** copy `smd/web/PMS_SMD_Dashboard_internal.html` (git-ignored): an Overview card under "Timeline (actual)" with Stage › outcome/artifact rows (module, tokens, effective tokens = input×1 + cache write×2 + cache read×0.1 + output×5, requests, source). The customer file `PMS_SMD_Dashboard.html` must contain **no** token data or code: the build strips everything between the `TK-START` / `TK-END` markers and fails if "token" remains.
   - Decisions, commits or activity whose text mentions tokens (e.g. D-89) are shown with `neutral_generic` from `smd-config.yaml` (`neutral_patterns`).
   - Never put token figures in `smd-data.json`, snapshots, `CHANGELOG.md` or any customer-facing text (PR-03).
5. **Write the outputs.**
   - `smd/smd-data.json` (update `meta.generated_at`, `meta.repo_commit`, `meta.previous_snapshot`, and the trend series)
   - `smd/snapshots/YYYY-MM-DD_HHmm.json`
   - Run `node smd/build.mjs` to regenerate `smd/web/PMS_SMD_Dashboard.html` (customer) and `smd/web/PMS_SMD_Dashboard_internal.html` (internal, with token utilization)
   - Prepend an entry to `smd/CHANGELOG.md`
6. **Verify.**
   - The build passes schema validation.
   - Every `path` exists. `build.mjs` reports 0 broken file links; list any that remain.
   - The HTML opens with no console errors (headless check, if available).
   - The file is under 2 MB.
   - The customer file contains no "token" text; the internal file shows the token card with the same totals as the log.
7. **Report back** in under 15 lines:
   - current stage and health (with reason),
   - the key changes since the last update,
   - newly opened or closed findings,
   - items due in the next 7 days,
   - data-quality warnings,
   - suggested mapping or convention fixes,
   - token utilization: total and effective tokens this refresh period per stage › outcome, plus any "token rows missing" (internal; never in the customer file).

Optional, only if I ask in this run: `--with-template` (also apply the UI changes I describe to `smd-template.html`), `--attach` (send me the generated HTML as an attachment), or `--commit` (create a git commit `chore(smd): refresh dashboard YYYY-MM-DD`).

**PROMPT END**
