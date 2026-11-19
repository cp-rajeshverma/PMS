# SMD Conventions — cheat-sheet for the team and BMAD agents

These conventions are what make SMD accurate. Anything that doesn't follow them is still picked up, but it shows as **inferred** in the dashboard. The source copy lives in `D:\POC\PMS\smd\prompt\`. The generate prompt copies it to `D:\POC\PMS\smd\CONVENTIONS.md`.

## 1. Artifact front-matter (Markdown artifacts)

Add this at the top of every key artifact (BRD, HLD, Brief, PRD, UX Spec, Architecture, test strategy, release notes…):

```yaml
---
smd:
  code: PMS-BRD-001            # <APP>-<TYPE>-<NNN>; delta artifacts in CRs: PMS-CR-2027-03-BRD
  type: BRD                    # Template|Mockup|BRD|HLD|Brief|PRD|UXSpec|Architecture|Epic|Story|TestPlan|TestReport|ReleaseNote|Runbook|Other
  stage: 2                     # stage number from smd-config.yaml
  step: null                   # e.g. PRD, Architecture (BMAD steps)
  module: ALL                  # ALL|EIMS|AMS|LMS|SMS
  author: Rajesh Verma
  reviewers: [ ]
  version: 0.6
  status: Draft                # Planned|Draft|In Review|Rework|Approved|Superseded
  planned: 2026-12-05
  completed: null              # set when Approved
  depends_on: [PMS-MOCKUP-001, PMS-TEMPLATE-BRD]
---
```

For non-Markdown files (Word, PDF, Figma exports, images), add a **sidecar file** with the same name plus `.smd.yaml` next to it, e.g. `PMS_Mockups_v1.pdf.smd.yaml`, containing the same keys.

## 2. Requirement IDs (for coverage and gap analysis)

Use stable IDs in headings or tables so coverage can be computed:

| Artifact | ID pattern | Example |
|---|---|---|
| Mockup screen | `UI-<MOD>-NNN` | UI-LMS-004 |
| BRD requirement | `BR-<MOD>-NNN` | BR-AMS-012 |
| HLD component / NFR | `HLD-<AREA>-NN`, `NFR-NN` | HLD-API-03, NFR-07 |
| PRD functional req. | `FR-<MOD>-NNN` | FR-LMS-004 |
| Story | `STORY-<MOD>-NN` (or BMAD `epic.story`, e.g. 2.3) | STORY-SMS-21 |
| Test case | `TC-<MOD>-NNN` | TC-EIMS-033 |

Reference an upstream ID where it is implemented, e.g. "FR-LMS-004 (← BR-LMS-002, UI-LMS-004)". Use the same pattern in story files.

## 3. Review and gap files — `reviews/`

One file per review: `reviews/RV-NNN_<short-name>.md`

```yaml
---
smd-review:
  id: RV-003
  type: gap                     # peer|stage-exit|gap
  artifacts: [PMS-MOCKUP-001, PMS-BRD-001]
  reviewers: [<name>, <agent: QA>]
  date: 2026-11-20
  verdict: Rework               # Approved|Approved-with-comments|Rework
  findings:
    - id: F-011
      source: PMS-MOCKUP-001
      target: PMS-BRD-001
      category: Missing         # Missing|Inconsistent|Ambiguous|Out-of-scope|NFR-gap
      severity: High            # Critical|High|Medium|Low
      summary: Leave cancellation screen (UI-LMS-007) has no BRD requirement
      owner: <BA name>
      due: 2026-11-27
      status: Open              # Open|In-progress|Resolved|Accepted-risk|Deferred-to-CR
---
Free-text review notes below…
```

## 4. Decision log — `decisions/`

`decisions/ADR-NNN_<short-name>.md` with:

```yaml
---
smd-decision: { id: ADR-004, title: SQLite for POC persistence, date: 2026-11-18, author: <name>, stage: 3, status: Accepted }
---
```

## 5. Gate sign-off

When a stage gate is passed, record it as a `stage-exit` review with `verdict: Approved`, and add `gate: <stage number>` under `smd-review`. SMD marks a gate Passed **only** when it finds this evidence.

## 6. Stories and coding steps (Build)

In each BMAD story file, keep a status block that SMD can read:

```yaml
smd-story: { id: STORY-LMS-03, epic: EPIC-LMS-1, module: LMS,
  steps: { drafted: 2027-01-05, approved: 2027-01-06, branch: feature/lms-03, implemented: null,
           unit_tests: null, dod: null, code_review: null, qa_review: null, merged_ci: null, done: null } }
```

Also reference the story ID in branch names and commit messages, e.g. `feat(LMS-03): apply leave API`.

## 7. Change Requests (after go-live) — `crs/`

- `crs/CR-YYYY-NNN_<short-name>.md`, containing an `smd-cr:` block with `id, title, requester, modules, type, priority, status, pipeline`.
- A CR bundle is a pipeline file, `crs/pipelines/PMS-CR-YYYY-NN.yaml`, which lists its CRs and the date of each stage.

## 8. Agent memory and session logs

No format is required. SMD summarizes them into the activity feed and never embeds them. Agents writing session logs should start each one with a line in this form:

`Session: <date> · Agent: <BMAD role> · Stage: <n> · Story/Artifact: <id> · Outcome: <one line>`

That line becomes the activity entry as-is.
