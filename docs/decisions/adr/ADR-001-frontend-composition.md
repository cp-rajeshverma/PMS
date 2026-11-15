# ADR-001: Frontend composition – build-time packages for the POC

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-11-15 |
| Deciders | Rajesh Verma (product owner) |
| Decision log ref | D-23 |

## Context

PMS has four modules, each owning its frontend (`services/<module>/frontend`). Users must see one application with one login, menu and look. The frontends must be combined somehow.

## Decision

For the POC, each module frontend is built as a library package and imported into the shell app (`platform/shell-ui`), which is built and deployed as one application. After the POC, PMS moves to runtime micro-frontends (Module Federation).

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
| --- | --- | --- | --- |
| Runtime micro-frontends (Module Federation) | Each module deploys its UI alone; full vertical slice | Shared-dependency, auth and routing complexity; five frontend deployments | Deferred until after the POC for simplicity |
| One shared frontend app | Simplest | Drops per-module frontend ownership; conflicts with D-10 | Does not fit the module-per-service design |

## Consequences

- **Positive:** One frontend build and deployment; simpler auth and routing; module code stays separated.
- **Negative / trade-offs:** A change to any module's UI needs the shell rebuilt and redeployed.
- **Follow-ups:** Keep module frontends free of shell internals (export a defined module contract: routes, menu entries, components) so the move to Module Federation is contained.
