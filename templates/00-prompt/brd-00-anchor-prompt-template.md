# Prompt – <PRJ>-BRD

> Template guidance (delete this block in the prompt file)
> - Produces the session prompt `docs/00-prompt/brd-00-anchor-prompt.md` for the BRD anchor. Replace `mN` / `MOD` / `mod` with the module number and code (for example `m4`, `SMS`, `sms`) and fill every `<…>` placeholder; delete optional lines that do not apply.
> - Write the prompt before the session starts and index it in `docs/00-prompt/README.md`; after the session fill Used and Outcome and set Status to "Done – reuse only to revise <scope>".
> - Prompts are internal working files: the customer-facing rule applies to the document the prompt produces, not to the prompt (D-83).
> - Keep it self-contained: a new session must be able to run it with only the repository folder connected. Name decisions, rules and open items by id.
> - Pair it with `execute-prompt-file-brd-00-anchor-prompt-template.md`.

| Field | Value |
| --- | --- |
| Document | docs/02-brd/<PRJ>-BRD.md |
| Template | templates/02-brd/brd-anchor-template.md |
| Used | – |
| Outcome | – |
| Status | Ready for the next session |

## Prompt

```text
Project: <project name> – repo folder <repository path> (git, <branch> branch).
We are continuing <Step n: BRD>. Today: the BRD anchor, docs/02-brd/<PRJ>-BRD.md.
<Optional: what is in scope and what gets a need-basis or placeholder entry only.>

1. Load context first (read, don't summarise back to me):
   - <agent instructions file> and <project rules file>
     (<rule id>: <one-line summary> – repeat for every standing project rule, including the
      customer-facing rule and the usage-logging rule)
   - <design-artifact conventions file>
   - the latest handoff notes in <session notes folder>
   - <decision log> (newest first; use the next free D-id after the newest entry)
   - <UX journey index and UX summaries> – approved journeys, screens, roles and status lists

2. Inputs for the BRD anchor:
   - <requirements baseline> (<location>) – input only, not the master; its ids are renumbered to
     the BRD convention with a mapping table (§2.5)
   - Decisions most relevant: <D-id (one-line content)>, …
   - Template: templates/02-brd/brd-anchor-template.md

3. Approach:
   - Output is markdown in docs/02-brd/ – the repo copy is the master.
   - The anchor holds only what spans modules: context, module BRD index, glossary, id conventions,
     roles and role × module access, end-to-end process and journey index, cross-module rules
     (BR-CMN), integrations and cross-module jobs, system-wide NFRs and volumetrics, risks,
     traceability roll-up, open items. Module requirements go to the module BRDs.
   - Before drafting, read the inputs and ask me the BRD anchor gaps first.
   - Draft in this order, one review at a time: §1–§3, then §4, then §5, then §6, then §7, then §8, then §9–§10, then §11–§13.
   - Every approved review adds a revision row to §1.1.

4. Working rules:
   - Fill sections only from the inputs and approved decisions; never invent requirements or
     design – record gaps as open items.
   - Ask me BA questions a few at a time (max 4 per round), each with your recommended
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

5. At the end of the anchor: set §2.3 module BRD index and §11 roll-up to "Not started" per module, add a session handoff note in
   <session notes folder>/<date>.md, add the outcome to docs/00-prompt/README.md and to this
   prompt file's header, and stop before the first module BRD until I say go. Remind me to refresh the SDLC
   dashboard (<dashboard execute prompt>).

Start by loading the context, then show me the BRD anchor gaps you found (first round of questions).
```
