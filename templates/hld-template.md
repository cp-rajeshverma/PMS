# <Project> – High-Level Design (HLD)

## 1. Document control

| Field | Value |
| --- | --- |
| Document | High-Level Design |
| Version | 0.1 |
| Status | Draft / In review / Approved |
| Architect | <name> |
| Approver | <name> |
| Inputs | BRD v<x>, UX Journey Index v<x>, Standards v<x> |
| Last updated | <yyyy-mm-dd> |

| Version | Date | Author | Change |
| --- | --- | --- | --- |

## 2. Context and goals

<Business context in brief, with BRD references. Architecture goals and quality attributes, ranked.>

## 3. Architecture principles

| Id | Principle | Rationale | Implication |
| --- | --- | --- | --- |
| AP-01 | | | |

## 4. System context (C4 level 1)

<Diagram: users, the system, external systems. Short description of each actor.>

## 5. Container view (C4 level 2)

<Diagram: shell UI, micro-frontends, API gateway, identity provider, services, message broker, databases.>

| Container | Technology | Responsibility | Talks to |
| --- | --- | --- | --- |

## 6. Service catalogue

Repeat 6.n per service.

### 6.1 <Service name>

| Item | Detail |
| --- | --- |
| Responsibility | |
| Owned data | |
| APIs exposed | <link to contracts/openapi/...> |
| Events published | |
| Events consumed | |
| Scheduled jobs | |
| Dependencies | |
| BRD requirements covered | FR-… |

## 7. Data architecture

<Entity per service, ownership, keys, retention, audit fields, soft delete, migration approach (e.g. Flyway).>

| Entity | Owning service | Database | Key attributes | Retention |
| --- | --- | --- | --- | --- |

## 8. Integration architecture

| Id | Flow | Style (sync REST / async event / scheduled) | Producer → consumer | Contract | Reliability (outbox, retry, idempotency, DLQ) |
| --- | --- | --- | --- | --- | --- |

<Sequence diagram for each key cross-service flow.>

## 9. API contract summary

| Service | Resource | Methods | Roles | Contract file |
| --- | --- | --- | --- | --- |

## 10. Frontend architecture

<Shell app, micro-frontend composition, routing, shared design system, state management, auth handling.>

## 11. Security architecture

<Identity provider, token flow, role-based access, service-to-service auth, secrets management, data protection, OWASP controls, audit.>

## 12. Non-functional design

| NFR Id (BRD) | Design approach | Verification |
| --- | --- | --- |

Covers performance, scalability, resilience (timeouts, retries, circuit breakers), observability (logs, metrics, traces, health checks) and availability.

## 13. Deployment architecture

<Environments, hosting, containers, networking, CI/CD pipelines, configuration, rollback.>

| Environment | Purpose | Hosting | Deployed by |
| --- | --- | --- | --- |

## 14. Technology stack

| Layer | Technology | Version | Notes |
| --- | --- | --- | --- |

## 15. Replatforming considerations

<What must stay language-neutral (contracts, events, DB schema, identity) so services can move to other runtimes.>

## 16. Architecture decisions

| ADR | Title | Status |
| --- | --- | --- |

## 17. Risks and technical debt

| Id | Item | Impact | Mitigation / plan |
| --- | --- | --- | --- |

## 18. Traceability

| Req Id (BRD) | Service / component | API / event | ADR |
| --- | --- | --- | --- |

## 19. Sign-off

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Product owner | | | |
