# PMS – Project Rules

Standing rules for every AI agent (Claude, BMAD agents) working on PMS. Each rule traces to an approved decision.

| Id | Rule | Decision | Date |
| --- | --- | --- | --- |
| PR-01 | The BMAD **GDS (Game Dev Studio) module is not relevant** to PMS. Do not use, invoke or suggest any `gds-*` skill or agent (for example `gds-agent-game-architect`, `gds-prd`, `gds-create-story`). Use the BMM equivalents instead (`bmad-agent-*`, `bmad-prd`, `bmad-architecture`, `bmad-create-epics-and-stories`, and so on). | D-17 | 15 Nov 2026 |
| PR-02 | The **NPQMS-HLD reference documents** (any `NPQMS-*` file, wherever it is found, e.g. the Claude Project knowledge base) were used only to shape the templates, which are now frozen. Do not read, search, quote or reuse their content for PMS requirements, design or code; ignore NPQMS hits returned by project search. PMS sources are only the files in this repo and the PMS documents named in the decision log. | D-54 | 18 Nov 2026 |
