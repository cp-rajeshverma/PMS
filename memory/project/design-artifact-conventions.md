# Design artifact set and template conventions

Status: templates frozen 17 Nov 2026 (D-35 to D-42); data model split 18 Nov 2026 (D-43, D-44); ADR template merged into Part01a 18 Nov 2026 (D-45); Part02 split into anchor + module + SUP (D-48); BRD split likewise (D-49). Templates live in `templates/`.

## Artifact set (per project)

| Artifact | Template | One per |
| --- | --- | --- |
| <PRJ>-BRD (anchor) | templates/02-brd/brd-anchor-template.md | project (context, roles, end-to-end process, cross-module rules, system-wide NFRs) |
| <PRJ>-BRD-M<n>-<MOD> | templates/02-brd/brd-module-template.md | functional module |
| <PRJ>-BRD-M<n>-SUP | templates/02-brd/brd-sup-template.md | project (supporting functions, need basis) |
| <PRJ>-HLD-Part01-Architecture-and-Design | templates/03-hld/hld-part01-architecture-and-design-template.md | project (includes A&A architecture in §9; no separate A&A document, D-40) |
| <PRJ>-HLD-Part01a-Principles-Patterns-Decisions | templates/03-hld/hld-part01a-principles-patterns-decisions-template.md | project (330-item catalogue in 18 groups; ADR register §5 and ADR format §6, D-45) |
| <PRJ>-HLD-Part02-Functional (anchor) | templates/03-hld/hld-part02-anchor-functional-template.md | project (module index, function index, cross-module flows, common API / event / error conventions, roll-up inventories, requirement coverage) |
| <PRJ>-HLD-Part02-M<n>-<MOD>-Functional | templates/03-hld/hld-part02-module-functional-template.md | functional module |
| <PRJ>-HLD-Part02-M<n>-SUP-Functional | templates/03-hld/hld-part02-sup-functional-template.md | project (supporting modules) |
| <PRJ>-HLD-Part03-Datamodel (anchor) | templates/03-hld/hld-part03-anchor-datamodel-template.md | project (conventions, ownership, entity index, master ER, cross-service, roll-ups) |
| <PRJ>-HLD-Part03-M<n>-<MOD>-Datamodel | templates/03-hld/hld-part03-module-datamodel-template.md | functional module (entity definitions) |
| <PRJ>-HLD-Part03-M<n>-SUP-Datamodel | templates/03-hld/hld-part03-sup-datamodel-template.md | project (supporting modules, need basis; entity structure per module template §3.1) |
| UX journey index / UX summaries | 01-ux/ux-*-template.md | project / screen |
| ADR file | format in Part01a §6 | significant architecture decision (`docs/decisions/adr/ADR-<NNN>-*.md`) |

## Conventions adopted

- Document ID pattern `<PRJ>-<DOC>-v<x.y>`; version / revision history and review-approval table in every document.
- Function ids `<MOD>0010`, step 10; supporting prefixes ADM, UM, AUTH, NM, DM.
- Per-function chapter (Part02 module template §3.2.1, D-38): purpose / trigger / conditions → actor & data scope → traceability (incl. related functions) → navigation & prototype → solution approach (design description, design notes, sequence & orchestration, frontend, backend, database, validation & errors, security & privacy, notifications & audit, scenarios) → notes.
- SUP functions reuse the Part02 §3.2.1 structure; no appendix copy.
- Design / entity status values: Draft, In review, Approved, Deferred, Moved, Removed (stub kept with reason or new location).
- API references `[API-<MOD>-nn : METHOD /ctx/resource (Purpose : ...)]`; API inventory is a roll-up keyed by API id.
- Every layer (BRD, Part02, Part03) = anchor + module documents + SUP document (D-43, D-48, D-49).
- Business statuses live in module BRD §6; HLD and data model hold only technical handling.
- Validation rules reference BRD VR / BR ids; frontend records only what the UX summary does not.
- Every diagram keeps a text-version table.
- Designs stay technology-neutral to support replatforming (Java → Node.js / Python FastAPI).
- Data model: anchor + one document per module + SUP (D-43); columns defined only in module documents; database per service, no cross-database FK; supporting-module entities modelled on a need basis only, skipped when an existing capability provides them (D-42).

## Reference material

NPQMS-HLD PDFs were used only as structural references in the Claude Project. They are never copied into the repo or `docs/`, and can be removed from the Project now that templates are frozen.
