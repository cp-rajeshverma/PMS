# Prompt – <PRJ>-HLD-Part03-MN-MOD-Datamodel

> Template guidance (delete this block in the prompt file)
> - Produces the session prompt `docs/00-prompt/hld-part03-mN-mod-datamodel-prompt.md` for HLD Part03 module document. Replace `mN` / `MOD` / `mod` with the module number and code (for example `m4`, `SMS`, `sms`) and fill every `<…>` placeholder; delete optional lines that do not apply.
> - Write the prompt before the session starts and index it in `docs/00-prompt/README.md`; after the session fill Used and Outcome and set Status to "Done – reuse only to revise <scope>".
> - Prompts are internal working files: the customer-facing rule applies to the document the prompt produces, not to the prompt (D-83).
> - Keep it self-contained: a new session must be able to run it with only the repository folder connected. Name decisions, rules and open items by id.
> - Pair it with `execute-prompt-file-hld-part03-mN-mod-datamodel-prompt-template.md`.

| Field | Value |
| --- | --- |
| Document | docs/03-hld/<PRJ>-HLD-Part03-MN-MOD-Datamodel.md |
| Template | templates/03-hld/hld-part03-module-datamodel-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: <project name> – repo folder <repository path> (git, <branch> branch).
We are continuing <Step n: HLD>. Today: the HLD Part03 Data Model for the <MOD> module, docs/03-hld/<PRJ>-HLD-Part03-MN-MOD-Datamodel.md.
<Optional: what is in scope and what gets a need-basis or placeholder entry only.>

1. Load context first (read, don't summarise back to me):
   - <agent instructions file> and <project rules file>
     (<rule id>: <one-line summary> – repeat for every standing project rule, including the
      customer-facing rule and the usage-logging rule)
   - <design-artifact conventions file>
   - the latest handoff notes in <session notes folder>
   - <decision log> (newest first; use the next free D-id after the newest entry)
   - <HLD Part03 anchor> (<version>) – conventions, index and roll-ups to follow
   - <module BRD> – §6 status lifecycle, §9 data requirements, §13 volumetrics
   - <HLD module documents already drafted> – the pattern for structure, depth, ids and wording

2. Inputs for the <MOD> Part03:
   - <HLD Part02 module functional design> (if drafted) – what each function reads and writes
   - Decisions most relevant: <D-id (one-line content)>, … ; ADRs <ADR ids>
   - Template: templates/03-hld/hld-part03-module-datamodel-template.md

3. Approach:
   - Output is markdown in docs/03-hld/ – the repo copy is the master.
   - Columns are defined only here; business statuses stay in the BRD (§6) and only their technical
     handling is designed; database per service, no cross-database foreign keys; sample data per
     scenario in the appendix.
   - Before drafting, read the inputs and ask me the <MOD> Part03 gaps first.
   - Draft in this order, one review at a time: §1–§2, then §3 one entity per review, then §4–§6.
   - Any change to the anchor (<PRJ>-HLD-Part03-Datamodel) – new rule, integration, open item, prefix or index entry –
     gets a new anchor revision row (next rev <x.y>) and is mentioned in the decision.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me design questions a few at a time (max 4 per round), each with your recommended
     answer first, using the question tool. If I ask what an option means, explain, then re-ask.
   - I review section by section; after each review propose one decision-log entry and write it
     only after my "yes". Do not move to the next section or document until I give the go-ahead.
   - Customer-facing documents follow <customer-facing rule id>: author "<author name and role>",
     no mention of <excluded names> anywhere in the document.
   - <Usage-logging rule id>: take a usage reading at session start and at every outcome commit;
     append one row per outcome with the difference to <usage log file>, quoting any text that
     contains commas; never invent figures.
   - Commit locally after each approved review with a clear message; I do the git push.
   - Work on my files on my computer (device shell), not by copying them to the cloud. Keep
     scratch files in $HOME (the device shell cannot write /tmp) and never read leftovers from /tmp.
   - Never delete any file without first listing exactly which files and asking my consent.
     If git leaves .lock or tmp_obj files it cannot remove, tell me and ask before touching them.
   - Keep messages concise: what was drafted, points to check, proposed decision.

5. At the end of the module document: update the Part03 anchor index and roll-ups for <MOD>, add a session handoff note in
   <session notes folder>/<date>.md, add the outcome to docs/00-prompt/README.md and to this
   prompt file's header, and stop before the next document until I say go. Remind me to refresh the SDLC
   dashboard (<dashboard execute prompt>).

Start by loading the context, then show me the <MOD> Part03 gaps you found (first round of questions).
```
