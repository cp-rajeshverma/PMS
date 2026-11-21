# Execute prompt – SMD update (refresh the SDLC dashboard)

Paste the block below into a new session to run `smd/prompt/smd-update-prompt.md`. No editing is needed: the run derives the context from the repository. Add optional notes only for things the repository does not show.

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
Task: refresh the SDLC Monitoring & Dashboard (SMD).

Please connect my folder D:\POC\PMS, read smd/prompt/smd-update-prompt.md and carry out
the prompt between "PROMPT START" and "PROMPT END" exactly as written. Options for this run: --commit.

Context for this refresh: derive it yourself – commits since meta.repo_commit in
smd/smd-data.json, the newest file in memory/sessions/ and the newest decisions in
docs/decisions/decision-log.md. Mention in the report if my notes below disagree with the repo.
Notes (optional): <leave empty or add anything the repo does not show>

Working rules:
- Follow CLAUDE.md and memory/project/project-rules.md (PR-01, PR-02, PR-03). The dashboard is
  customer-facing: it must not mention AI tools, agents or assistants; author is
  Rajesh Verma (Enterprise Architect).
- Work on my files on my computer (device shell), not by copying them to the cloud.
- Write only inside smd/ (never smd/prompt/); do not edit project documents.
- Exception to "write only inside smd/": after the commit, take a usage reading and append the
  refresh row (stage X, outcome "SMD refresh") to memory/usage/token-log.csv and the reading to
  memory/usage/session-readings.csv (PR-04), in a second commit.
- Never delete any file without first listing exactly which files and asking my consent.
- If git leaves .lock or tmp_obj files: list them, ask once for delete permission on D:\POC\PMS,
  then remove only those files after each commit in this session.
- Commit locally only (I do the git push).
- Keep the report under 15 lines, as the prompt asks.
```

Run after each approved outcome or gate.

Options: drop `--commit` to review the refreshed data before committing; add `--attach` to receive the regenerated dashboard HTML in the chat – use it when you want the dashboard to send to the customer, and remove the two internal token sections (between the `TK-START` and `TK-END` markers) before sharing.
