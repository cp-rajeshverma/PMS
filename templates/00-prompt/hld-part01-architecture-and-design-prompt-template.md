# Prompt – <PRJ>-HLD-Part01-Architecture-and-Design

> Template guidance (delete this block in the prompt file)
> - Produces the session prompt `docs/00-prompt/03-hld/hld-part01-architecture-and-design-prompt.md` for HLD Part01. Replace `mN` / `MOD` / `mod` with the module number and code (for example `m4`, `SMS`, `sms`) and fill every `<…>` placeholder; delete optional lines that do not apply.
> - Write the prompt before the session starts and index it in `docs/00-prompt/README.md`; after the session fill Used and Outcome and set Status to "Done – reuse only to revise <scope>".
> - Prompts are internal working files: the customer-facing rule applies to the document the prompt produces, not to the prompt (D-83).
> - Keep it self-contained: a new session must be able to run it with only the repository folder connected. Name decisions, rules and open items by id.
> - Pair it with `execute-prompt-file-hld-part01-architecture-and-design-prompt-template.md`.

| Field | Value |
| --- | --- |
| Document | docs/03-hld/<PRJ>-HLD-Part01-Architecture-and-Design.md |
| Template | templates/03-hld/hld-part01-architecture-and-design-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: <project name> – repo folder <repository path> (git, <branch> branch).
We are continuing <Step n: HLD>. Today: HLD Part01 Architecture and Design, docs/03-hld/<PRJ>-HLD-Part01-Architecture-and-Design.md.
<Optional: what is in scope and what gets a need-basis or placeholder entry only.>

1. Load context first (read, don't summarise back to me):
   - <agent instructions file> and <project rules file>
     (<rule id>: <one-line summary> – repeat for every standing project rule, including the
      customer-facing rule and the usage-logging rule)
   - <design-artifact conventions file>
   - the latest handoff notes in <session notes folder>
   - <decision log> (newest first; use the next free D-id after the newest entry)
   - <approved BRD set> – scope, roles and access, integrations and jobs, system-wide NFRs,
     volumetrics, constraints, dependencies, risks
   - <Part01a principles, patterns and decisions> (if drafted) and the ADR files

2. Inputs for the Part01:
   - Architecture and technology decisions: <D-id (one-line content)>, … ; ADRs <ADR ids>
   - <Standards or guardrail documents, if any>
   - Template: templates/03-hld/hld-part01-architecture-and-design-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master.
   - Every diagram keeps a text-version table; designs stay technology-neutral where the
     replatforming goal requires it; significant decisions get an ADR file and a register row in
     Part01a §5.
   - Before drafting, read the inputs and ask me the Part01 gaps first.
   - Draft in this order, one review at a time: §1–§4, then §5–§8, then §9–§10, then §11–§15, then §16–§20.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me architecture questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - Customer-facing documents follow <customer-facing rule id>: author "<author name and role>",
     no mention of <excluded names> anywhere in the document.
   - <Usage-logging rule id>: take a usage reading at session start and at every outcome commit;
     append one row per outcome with the difference to <usage log file> and the reading itself to
     <session readings file>, quoting any text that contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the Part01: record its status in the HLD anchors' reference lists, add a session handoff note in
   <session notes folder>/<date>.md, add the outcome to docs/00-prompt/README.md and to this
   prompt file's header, and stop before the next HLD document until I say go. Remind me to refresh the SDLC
   dashboard (<dashboard execute prompt>).

Start by loading the context, then show me the Part01 gaps you found (first round of questions).
```
