# Execute prompt – SMD update (refresh the SDLC dashboard)

Paste the block below into a new session to run `smd/prompt/smd-update-prompt.md`. Update the "Context for this refresh" lines to the latest milestone before pasting.

```text
Project: Payroll Management System (PMS) POC – repo folder D:\POC\PMS (git, main branch).
Task: refresh the SDLC Monitoring & Dashboard (SMD).

Please connect my folder D:\POC\PMS, read smd/prompt/smd-update-prompt.md and carry out
the prompt between "PROMPT START" and "PROMPT END" exactly as written. Options for this run: --commit.

Context for this refresh:
- Last milestone: PMS-BRD-M3-LMS drafted, all sections reviewed (D-84 to D-88), approval pending
  OI-02 and OI-04; anchor PMS-BRD.md now v1.0 rev 0.8 (new OI-09). Commits 1f767b2 to 7c44ca9.
- Session handoff: memory/sessions/2026-11-19.md (section "Evening 19 Nov – LMS BRD").

Working rules:
- Follow CLAUDE.md and memory/project/project-rules.md (PR-01, PR-02, PR-03). The dashboard is
  customer-facing: it must not mention AI tools, agents or assistants; author is
  Rajesh Verma (Enterprise Architect).
- Work on my files on my computer (device shell), not by copying them to the cloud.
- Write only inside smd/ (never smd/prompt/); do not edit project documents.
- Never delete any file without first listing exactly which files and asking my consent.
  If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
- Commit locally only (I do the git push).
- Keep the report under 15 lines, as the prompt asks.
```

Options: drop `--commit` to review the refreshed data before committing; add `--attach` to receive the regenerated dashboard HTML in the chat.
