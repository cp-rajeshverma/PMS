# <Project> – HLD Part01a: Architecture Principles & Patterns Catalogue

Document ID: <PRJ>-HLD-Part01a-Principles-Patterns-v<x.y>
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

## 1. Document control

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | First draft |

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Product owner | | | |

## 2. How to use this catalogue

This catalogue lists the architecture principles and patterns the design is assessed against. It is referenced from <PRJ>-HLD-Part01-AnD §4. For each row, record:

| Column | Meaning |
| --- | --- |
| Id | Stable id, used in HLDs, ADRs and reviews (e.g. AP-RES-03) |
| Applicability | **Applied** · **Partial** · **Deferred** (later phase) · **N/A** (with reason) |
| Realization | How the design meets it (component, setting, pattern), one line |
| Ref | Where it is designed: AnD / Part02 / Part03 section, ADR, standard |

Rows are never deleted; mark them N/A with a reason. Add project-specific rows at the end of a group.

**Sources:** 

- Cloud design patterns – Azure Architecture Center (https://learn.microsoft.com/en-us/azure/architecture/patterns/); 
- Enterprise Integration Patterns – Hohpe & Woolf (https://www.enterpriseintegrationpatterns.com/patterns/messaging/); 
- Microservice patterns – microservices.io (C. Richardson); 
- Twelve-Factor App (12factor.net); 
- Well-Architected Framework; 
- OWASP Top 10.

## 3. Group summary

| Group | Code | Rows | Applied | Partial | Deferred | N/A |
| --- | --- | --- | --- | --- | --- | --- |
| A. Architecture approach & governance | GOV | | | | | |
| B. X-First principles | XF | | | | | |
| C. Well-architected qualities | WA | | | | | |
| D. Software design principles | SD | | | | | |
| E. Twelve-Factor App | TF | | | | | |
| F. Frontend & experience architecture | FE | | | | | |
| G. Microservice design patterns | MS | | | | | |
| H. Cloud design patterns | CP | | | | | |
| I. Enterprise integration patterns | EIP | | | | | |
| J. Integration principles | INT | | | | | |
| K. Data architecture | DATA | | | | | |
| L. Security architecture | SEC | | | | | |
| M. Logging & observability | OBS | | | | | |
| N. Performance & scalability | PERF | | | | | |
| O. Resilience & availability | RES | | | | | |
| P. DevOps & continuous delivery | DEV | | | | | |
| Q. Testing & quality | QA | | | | | |
| R. AI-assisted delivery | AI | | | | | |

## 4. Catalogue

### A. Architecture approach & governance (GOV)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-GOV-01 | Big Design Up Front (BDUF) | Enterprise architecture artifacts (AnD, A&A, HLDs, data model, contracts) are approved before implementation starts | | | |
| AP-GOV-02 | Stakeholder alignment | Functional, system, deployment and integration architectures are reviewed and signed off with the stakeholders concerned | | | |
| AP-GOV-03 | Architecture decision records | Every significant decision is recorded with context, options and consequences | | | |
| AP-GOV-04 | End-to-end traceability | Requirement → design → code → test are linked by ids | | | |
| AP-GOV-05 | Standards & guardrails compliance | Design and code follow published standards; deviations need an ADR | | | |
| AP-GOV-06 | Architecture review gates | Formal review at end of design, before build, before go-live | | | |
| AP-GOV-07 | Approved technology stack | Only technologies on the approved stack are used; additions via ADR | | | |
| AP-GOV-08 | Documentation as code | Architecture and design docs are versioned with the code | | | |
| AP-GOV-09 | Reuse → buy → build | Prefer reuse of platform capabilities, then proven products, then custom build | | | |
| AP-GOV-10 | Evolutionary architecture | Architecture can change incrementally; fitness functions verify key qualities | | | |
| AP-GOV-11 | Replatforming readiness | Contracts, events and data are language-neutral so services can move runtime | | | |

### B. X-First principles (XF)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-XF-01 | UX first | User journeys and mockups are designed and approved before functional and technical design | | | |
| AP-XF-02 | API first / contract first | Every capability is a versioned API contract (OpenAPI / event schema) defined before implementation | | | |
| AP-XF-03 | Security first | Security controls designed in at every layer from the start | | | |
| AP-XF-04 | Performance first | Performance budgets and load profile defined at design time | | | |
| AP-XF-05 | Cloud first | Managed cloud services preferred over self-managed infrastructure | | | |
| AP-XF-06 | Data first | Data ownership, model and quality defined before services | | | |
| AP-XF-07 | Observability first | Logs, metrics, traces and health checks designed in, not added later | | | |
| AP-XF-08 | Automation first | Build, test, deploy, provisioning and checks are automated | | | |
| AP-XF-09 | Test first | Tests and acceptance criteria written before or with code | | | |
| AP-XF-10 | Accessibility first | Accessibility standard (e.g. WCAG 2.1 AA) applied from mockups onward | | | |
| AP-XF-11 | Privacy by design | Personal data minimized, classified and protected by default | | | |
| AP-XF-12 | Mobile / responsive first | Layouts designed for the smallest supported screen first | | | |
| AP-XF-13 | Cost aware (FinOps) | Cost is a design input; resources sized and switched off when idle | | | |

### C. Well-architected qualities (WA)

| Id | Quality | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-WA-01 | Resiliency | System recovers from failures and continues to function | | | |
| AP-WA-02 | Availability | System meets its availability target with no single point of failure | | | |
| AP-WA-03 | Decentralized | No central component that every request or team depends on | | | |
| AP-WA-04 | Independent & autonomous | Each service is built, deployed, scaled and failed independently | | | |
| AP-WA-05 | Auto provisioning | Infrastructure and environments are created from code (IaC) | | | |
| AP-WA-06 | Scalability | Capacity grows horizontally without redesign | | | |
| AP-WA-07 | Security | Confidentiality, integrity and availability protected end to end | | | |
| AP-WA-08 | Continuous delivery | Every change can be released safely at any time through a pipeline | | | |
| AP-WA-09 | Failure isolation | A failing component does not cascade to others | | | |
| AP-WA-10 | Observability | Internal state is understandable from logs, metrics and traces | | | |
| AP-WA-11 | Reliability (WAF pillar) | Workload performs its intended function correctly and consistently | | | |
| AP-WA-12 | Cost optimization (WAF pillar) | Delivers business value at the lowest reasonable cost | | | |
| AP-WA-13 | Operational excellence (WAF pillar) | Operations are automated, monitored and continuously improved | | | |
| AP-WA-14 | Performance efficiency (WAF pillar) | Resources match demand efficiently | | | |
| AP-WA-15 | Sustainability | Resource usage and energy footprint minimized | | | |

### D. Software design principles (SD)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-SD-01 | Single responsibility | A class / module has one reason to change | | | |
| AP-SD-02 | Open–closed | Open for extension, closed for modification | | | |
| AP-SD-03 | Liskov substitution | Subtypes are usable wherever their base type is expected | | | |
| AP-SD-04 | Interface segregation | Clients depend only on the interfaces they use | | | |
| AP-SD-05 | Dependency inversion | Depend on abstractions, not concrete implementations | | | |
| AP-SD-06 | Separation of concerns | Presentation, business logic and data access kept apart | | | |
| AP-SD-07 | High cohesion, loose coupling | Related logic together; minimal dependencies between modules | | | |
| AP-SD-08 | DRY | Each piece of knowledge has one authoritative representation | | | |
| AP-SD-09 | KISS | Prefer the simplest design that works | | | |
| AP-SD-10 | YAGNI | Build only what current requirements need | | | |
| AP-SD-11 | Law of Demeter | Objects talk only to their immediate collaborators | | | |
| AP-SD-12 | Composition over inheritance | Build behaviour by composing objects | | | |
| AP-SD-13 | Fail fast | Detect and report invalid state at the earliest point | | | |
| AP-SD-14 | Convention over configuration | Sensible defaults; configure only exceptions | | | |
| AP-SD-15 | Immutability by default | Prefer immutable objects and append-only records | | | |
| AP-SD-16 | Hexagonal / clean architecture | Domain core isolated from frameworks via ports and adapters | | | |
| AP-SD-17 | Domain-driven design | Bounded contexts, ubiquitous language, aggregates | | | |
| AP-SD-18 | Stateless services | No session state held in service instances | | | |
| AP-SD-19 | Defensive validation | Validate at every trust boundary; server-side validation is authoritative | | | |

### E. Twelve-Factor App (TF)

| Id | Factor | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-TF-01 | Codebase | One codebase tracked in version control, many deploys | | | |
| AP-TF-02 | Dependencies | Explicitly declared and isolated | | | |
| AP-TF-03 | Config | Configuration stored in the environment, not code | | | |
| AP-TF-04 | Backing services | Treated as attached resources | | | |
| AP-TF-05 | Build, release, run | Strictly separated stages | | | |
| AP-TF-06 | Processes | Stateless, share-nothing processes | | | |
| AP-TF-07 | Port binding | Services export themselves via a port | | | |
| AP-TF-08 | Concurrency | Scale out via the process model | | | |
| AP-TF-09 | Disposability | Fast start-up and graceful shutdown | | | |
| AP-TF-10 | Dev/prod parity | Environments kept as similar as possible | | | |
| AP-TF-11 | Logs | Logs treated as event streams | | | |
| AP-TF-12 | Admin processes | One-off admin tasks run as one-off processes | | | |

### F. Frontend & experience architecture (FE)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-FE-01 | Headless frontend | UI consumes the backend only through APIs | | | |
| AP-FE-02 | Single-page application | One entry point; client-side routing and rendering | | | |
| AP-FE-03 | Micro-frontends | Each module owns its UI; composed in a shell (build-time or runtime) | | | |
| AP-FE-04 | Shared design system | One component library and style tokens for all modules | | | |
| AP-FE-05 | Backend for frontend | Aggregation API tailored to a UI where needed | | | |
| AP-FE-06 | Responsive layout | Works across supported screen sizes | | | |
| AP-FE-07 | Accessibility | Keyboard, screen reader, contrast per standard | | | |
| AP-FE-08 | Internationalization readiness | Text externalized; locale-aware formats | | | |
| AP-FE-09 | Client-side security | Tokens handled securely; no secrets in the browser | | | |
| AP-FE-10 | Consistent feedback | Standard loading, empty, error and success states | | | |

### G. Microservice design patterns (MS)

| Id | Pattern | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-MS-01 | Decompose by business capability | Services aligned to business capabilities | | | |
| AP-MS-02 | Decompose by subdomain | Services aligned to DDD subdomains / bounded contexts | | | |
| AP-MS-03 | Database per service | Each service owns its data; no direct access by others | | | |
| AP-MS-04 | Shared database (anti-pattern check) | Confirm services do not share tables | | | |
| AP-MS-05 | API gateway | Single entry point for clients; routing, auth, rate limits | | | |
| AP-MS-06 | Backends for frontends | Separate gateway / API per client type | | | |
| AP-MS-07 | Service discovery / registry | Services locate each other dynamically | | | |
| AP-MS-08 | Saga – choreography | Distributed transaction via events between services | | | |
| AP-MS-09 | Saga – orchestration | Distributed transaction via a central orchestrator | | | |
| AP-MS-10 | Transactional outbox | Events written in the same DB transaction as state, then published | | | |
| AP-MS-11 | Polling publisher / transaction log tailing | How outbox events are relayed to the broker | | | |
| AP-MS-12 | Domain events | Services publish events when domain state changes | | | |
| AP-MS-13 | Event sourcing | State stored as a sequence of events | | | |
| AP-MS-14 | CQRS | Separate read and write models | | | |
| AP-MS-15 | API composition | Query that joins data from several services in a composer | | | |
| AP-MS-16 | Idempotent consumer | Duplicate messages processed safely | | | |
| AP-MS-17 | Circuit breaker | Stop calling a failing service for a period | | | |
| AP-MS-18 | Externalized configuration | Configuration outside the deployable artifact | | | |
| AP-MS-19 | Health check API | Endpoint reporting liveness and readiness | | | |
| AP-MS-20 | Log aggregation | Logs from all services collected centrally | | | |
| AP-MS-21 | Distributed tracing | Requests traced across services with trace ids | | | |
| AP-MS-22 | Application metrics | Services expose metrics for monitoring | | | |
| AP-MS-23 | Audit logging | User actions recorded per business entity | | | |
| AP-MS-24 | Exception tracking | Exceptions reported centrally with context | | | |
| AP-MS-25 | Access token | Identity propagated to services via a token (e.g. JWT) | | | |
| AP-MS-26 | Consumer-driven contract test | Consumers define contract tests the provider must pass | | | |
| AP-MS-27 | Service component test | Service tested in isolation with test doubles | | | |
| AP-MS-28 | Service instance per container | Each service instance in its own container | | | |
| AP-MS-29 | Sidecar | Cross-cutting concerns in a co-deployed process | | | |
| AP-MS-30 | Microservice chassis / service template | Common framework and starter for all services | | | |
| AP-MS-31 | Strangler application | Incremental replacement of a legacy system | | | |
| AP-MS-32 | Anti-corruption layer | Translation layer between different domain models | | | |
| AP-MS-33 | API versioning | Backward-compatible evolution of service contracts | | | |
| AP-MS-34 | Self-contained service | A service can answer synchronous requests without waiting on others | | | |

### H. Cloud design patterns (CP)

Source: Azure Architecture Center cloud design patterns catalogue.

| Id | Pattern | Summary | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-CP-01 | Ambassador | Helper service sends network requests on behalf of a consumer | | | |
| AP-CP-02 | Anti-Corruption Layer | Façade / adapter between a modern application and a legacy system | | | |
| AP-CP-03 | Asynchronous Request-Reply | Decouple backend processing from the frontend while giving a timely response | | | |
| AP-CP-04 | Backends for Frontends | Separate backend services per frontend | | | |
| AP-CP-05 | Bulkhead | Isolate elements into pools so one failure does not take down others | | | |
| AP-CP-06 | Cache-Aside | Load data into a cache on demand | | | |
| AP-CP-07 | Choreography | Services decide how to process a business operation without a central orchestrator | | | |
| AP-CP-08 | Circuit Breaker | Handle faults of variable duration when calling remote services | | | |
| AP-CP-09 | Claim Check | Split large messages into a claim check and a payload | | | |
| AP-CP-10 | Compensating Transaction | Undo steps of an eventually consistent operation | | | |
| AP-CP-11 | Competing Consumers | Several consumers process messages from one channel | | | |
| AP-CP-12 | Compute Resource Consolidation | Consolidate tasks into one computational unit | | | |
| AP-CP-13 | CQRS | Separate read and update interfaces | | | |
| AP-CP-14 | Deployment Stamps | Independent copies of components including data stores | | | |
| AP-CP-15 | Event Sourcing | Append-only store of events describing changes | | | |
| AP-CP-16 | External Configuration Store | Configuration in a central location outside the package | | | |
| AP-CP-17 | Federated Identity | Delegate authentication to an external identity provider | | | |
| AP-CP-18 | Gatekeeper | Dedicated host validates and sanitizes requests before back ends | | | |
| AP-CP-19 | Gateway Aggregation | Gateway aggregates several requests into one | | | |
| AP-CP-20 | Gateway Offloading | Offload shared functionality to a gateway | | | |
| AP-CP-21 | Gateway Routing | Route requests to several services through one endpoint | | | |
| AP-CP-22 | Geode | Back ends deployed across geographically distributed nodes | | | |
| AP-CP-23 | Health Endpoint Monitoring | Functional checks exposed through endpoints | | | |
| AP-CP-24 | Idempotent Consumer | Duplicate delivery has the same effect as single delivery | | | |
| AP-CP-25 | Index Table | Indexes over frequently queried fields | | | |
| AP-CP-26 | Leader Election | One instance coordinates collaborating instances | | | |
| AP-CP-27 | Materialized View | Prepopulated views for query needs | | | |
| AP-CP-28 | Messaging Bridge | Intermediary between incompatible messaging systems | | | |
| AP-CP-29 | Pipes and Filters | Complex processing broken into reusable steps | | | |
| AP-CP-30 | Priority Queue | Higher-priority requests processed first | | | |
| AP-CP-31 | Publisher-Subscriber | Announce events to many consumers asynchronously | | | |
| AP-CP-32 | Quarantine | External assets checked against agreed quality before use | | | |
| AP-CP-33 | Queue-Based Load Leveling | Queue buffers load between a task and a service | | | |
| AP-CP-34 | Rate Limiting | Control resource consumption to avoid throttling | | | |
| AP-CP-35 | Retry | Retry anticipated transient failures | | | |
| AP-CP-36 | Saga | Data consistency across microservices | | | |
| AP-CP-37 | Scheduler Agent Supervisor | Coordinate actions across distributed services | | | |
| AP-CP-38 | Sequential Convoy | Ordered processing of related messages without blocking others | | | |
| AP-CP-39 | Sharding | Horizontal partitions of a data store | | | |
| AP-CP-40 | Sidecar | Components in a separate process or container | | | |
| AP-CP-41 | Static Content Hosting | Static content served from storage / CDN | | | |
| AP-CP-42 | Strangler Fig | Incremental migration of a legacy system | | | |
| AP-CP-43 | Throttling | Control consumption by applications, tenants or services | | | |
| AP-CP-44 | Valet Key | Token giving restricted direct access to a resource | | | |

### I. Enterprise integration patterns (EIP)

Source: Enterprise Integration Patterns (Hohpe & Woolf), messaging patterns catalogue.

| Id | Category | Pattern | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-EIP-01 | Integration style | File Transfer | | | |
| AP-EIP-02 | Integration style | Shared Database | | | |
| AP-EIP-03 | Integration style | Remote Procedure Invocation | | | |
| AP-EIP-04 | Integration style | Messaging | | | |
| AP-EIP-05 | Channels | Message Channel | | | |
| AP-EIP-06 | Channels | Point-to-Point Channel | | | |
| AP-EIP-07 | Channels | Publish-Subscribe Channel | | | |
| AP-EIP-08 | Channels | Datatype Channel | | | |
| AP-EIP-09 | Channels | Invalid Message Channel | | | |
| AP-EIP-10 | Channels | Dead Letter Channel | | | |
| AP-EIP-11 | Channels | Guaranteed Delivery | | | |
| AP-EIP-12 | Channels | Channel Adapter | | | |
| AP-EIP-13 | Channels | Messaging Bridge | | | |
| AP-EIP-14 | Channels | Message Bus | | | |
| AP-EIP-15 | Message construction | Command Message | | | |
| AP-EIP-16 | Message construction | Document Message | | | |
| AP-EIP-17 | Message construction | Event Message | | | |
| AP-EIP-18 | Message construction | Request-Reply | | | |
| AP-EIP-19 | Message construction | Return Address | | | |
| AP-EIP-20 | Message construction | Correlation Identifier | | | |
| AP-EIP-21 | Message construction | Message Sequence | | | |
| AP-EIP-22 | Message construction | Message Expiration | | | |
| AP-EIP-23 | Message construction | Format Indicator | | | |
| AP-EIP-24 | Routing | Pipes and Filters | | | |
| AP-EIP-25 | Routing | Message Router | | | |
| AP-EIP-26 | Routing | Content-Based Router | | | |
| AP-EIP-27 | Routing | Message Filter | | | |
| AP-EIP-28 | Routing | Dynamic Router | | | |
| AP-EIP-29 | Routing | Recipient List | | | |
| AP-EIP-30 | Routing | Splitter | | | |
| AP-EIP-31 | Routing | Aggregator | | | |
| AP-EIP-32 | Routing | Resequencer | | | |
| AP-EIP-33 | Routing | Composed Message Processor | | | |
| AP-EIP-34 | Routing | Scatter-Gather | | | |
| AP-EIP-35 | Routing | Routing Slip | | | |
| AP-EIP-36 | Routing | Process Manager | | | |
| AP-EIP-37 | Routing | Message Broker | | | |
| AP-EIP-38 | Transformation | Message Translator | | | |
| AP-EIP-39 | Transformation | Envelope Wrapper | | | |
| AP-EIP-40 | Transformation | Content Enricher | | | |
| AP-EIP-41 | Transformation | Content Filter | | | |
| AP-EIP-42 | Transformation | Claim Check | | | |
| AP-EIP-43 | Transformation | Normalizer | | | |
| AP-EIP-44 | Transformation | Canonical Data Model | | | |
| AP-EIP-45 | Endpoints | Message Endpoint | | | |
| AP-EIP-46 | Endpoints | Messaging Gateway | | | |
| AP-EIP-47 | Endpoints | Messaging Mapper | | | |
| AP-EIP-48 | Endpoints | Transactional Client | | | |
| AP-EIP-49 | Endpoints | Polling Consumer | | | |
| AP-EIP-50 | Endpoints | Event-Driven Consumer | | | |
| AP-EIP-51 | Endpoints | Competing Consumers | | | |
| AP-EIP-52 | Endpoints | Message Dispatcher | | | |
| AP-EIP-53 | Endpoints | Selective Consumer | | | |
| AP-EIP-54 | Endpoints | Durable Subscriber | | | |
| AP-EIP-55 | Endpoints | Idempotent Receiver | | | |
| AP-EIP-56 | Endpoints | Service Activator | | | |
| AP-EIP-57 | System management | Control Bus | | | |
| AP-EIP-58 | System management | Detour | | | |
| AP-EIP-59 | System management | Wire Tap | | | |
| AP-EIP-60 | System management | Message History | | | |
| AP-EIP-61 | System management | Message Store | | | |
| AP-EIP-62 | System management | Smart Proxy | | | |
| AP-EIP-63 | System management | Test Message | | | |
| AP-EIP-64 | System management | Channel Purger | | | |

### J. Integration principles (INT)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-INT-01 | Async by default between services | Events for state propagation; synchronous calls only when an immediate answer is needed | | | |
| AP-INT-02 | Contract-first interfaces | OpenAPI for REST, schema for events, versioned | | | |
| AP-INT-03 | Protocol selection guide | REST/HTTPS for queries and commands, broker (AMQP/JMS) for events, batch files for bulk | | | |
| AP-INT-04 | Authenticated integrations | Every call carries a user or service token; no anonymous endpoints | | | |
| AP-INT-05 | Transport security | TLS on every connection | | | |
| AP-INT-06 | Correlation id propagation | One id carried across HTTP headers and message headers | | | |
| AP-INT-07 | At-least-once delivery with idempotency | Consumers deduplicate by message id | | | |
| AP-INT-08 | Timeouts, retries and backoff | Bounded timeouts; retry only transient errors | | | |
| AP-INT-09 | Dead-letter handling | Poison messages parked, alerted and replayable | | | |
| AP-INT-10 | Event schema evolution | Backward-compatible changes; version in the envelope | | | |
| AP-INT-11 | Canonical event envelope | Standard header fields (id, type, version, time, source, correlation id) | | | |
| AP-INT-12 | Reconciliation for eventual consistency | Scheduled check repairs missed events | | | |
| AP-INT-13 | Connection management | Pooled connections, keep-alive, limits per client | | | |

### K. Data architecture (DATA)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-DATA-01 | Single source of truth | Each data item owned by exactly one service | | | |
| AP-DATA-02 | No cross-service joins | Data from other services obtained via API or events | | | |
| AP-DATA-03 | Schema migration as code | Versioned migrations (e.g. Flyway) run by the pipeline | | | |
| AP-DATA-04 | Soft delete | Records flagged inactive, never physically deleted | | | |
| AP-DATA-05 | Standard audit columns | created/updated by and at on every table | | | |
| AP-DATA-06 | Optimistic locking | Version column prevents lost updates | | | |
| AP-DATA-07 | Referential integrity policy | Within a service: DB foreign keys; across services: application checks | | | |
| AP-DATA-08 | Read / write separation | Reporting reads separated from transactional writes where needed | | | |
| AP-DATA-09 | Caching strategy | What is cached, TTL, invalidation | | | |
| AP-DATA-10 | Data classification | Personal and sensitive data identified and tagged | | | |
| AP-DATA-11 | Retention & archival | Retention period and archival per entity | | | |
| AP-DATA-12 | Backup & restore | RPO / RTO defined and tested | | | |
| AP-DATA-13 | UTC storage of timestamps | Stored in UTC, displayed in user time zone | | | |
| AP-DATA-14 | Naming conventions | Consistent table, column and key naming | | | |
| AP-DATA-15 | Business keys vs surrogate keys | Immutable business id alongside technical primary key | | | |
| AP-DATA-16 | Immutable approved records | Approved / financial records changed only by new versions | | | |
| AP-DATA-17 | Pagination for lists | All list queries paginated server-side | | | |

### L. Security architecture (SEC)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-SEC-01 | Zero trust | Every request authenticated and authorized, inside or outside the network | | | |
| AP-SEC-02 | Least privilege | Users, services and pipelines get only the access they need | | | |
| AP-SEC-03 | Defense in depth | Layered controls: network, gateway, service, data | | | |
| AP-SEC-04 | Secure by default | Deny by default; features opened explicitly | | | |
| AP-SEC-05 | Centralized identity (OAuth2 / OIDC) | One identity provider issues tokens | | | |
| AP-SEC-06 | Token validation at gateway and service | JWT signature, expiry, audience checked at both layers | | | |
| AP-SEC-07 | Role-based access control | Permissions by role, enforced on API and UI | | | |
| AP-SEC-08 | Multi-factor authentication | MFA policy per user type | | | |
| AP-SEC-09 | Password & session policy | Complexity, lockout, idle timeout, session expiry | | | |
| AP-SEC-10 | Secrets management | Secrets in a vault, rotated, never in code | | | |
| AP-SEC-11 | Encryption in transit | TLS 1.2+ everywhere | | | |
| AP-SEC-12 | Encryption at rest | Databases, storage and backups encrypted | | | |
| AP-SEC-13 | Input validation & output encoding | Prevent injection and XSS | | | |
| AP-SEC-14 | API protection | Rate limiting, CORS, security headers, size limits | | | |
| AP-SEC-15 | OWASP Top 10 coverage | Each category mapped to a control | | | |
| AP-SEC-16 | Threat modelling | STRIDE (or similar) per component at design time | | | |
| AP-SEC-17 | Dependency scanning & SBOM | Vulnerable libraries blocked in the pipeline | | | |
| AP-SEC-18 | SAST / DAST | Static and dynamic security testing in the pipeline | | | |
| AP-SEC-19 | Audit trail | Security-relevant actions logged, tamper-evident | | | |
| AP-SEC-20 | Personal data masking | No personal data in logs or non-production data | | | |

### M. Logging & observability (OBS)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-OBS-01 | Unified & centralized logging | All nodes ship logs to one platform | | | |
| AP-OBS-02 | Structured logs | JSON with a standard field set | | | |
| AP-OBS-03 | Correlation & trace ids | Every log line carries correlation and trace ids | | | |
| AP-OBS-04 | Standard log levels | Agreed meaning of ERROR / WARN / INFO / DEBUG | | | |
| AP-OBS-05 | Business event logging | Business events logged for business KPIs | | | |
| AP-OBS-06 | System metrics (RED / USE) | Rate, errors, duration; utilization, saturation, errors | | | |
| AP-OBS-07 | Distributed tracing | OpenTelemetry traces across gateway, services and broker | | | |
| AP-OBS-08 | Health & readiness probes | Liveness and readiness endpoints per service | | | |
| AP-OBS-09 | Dashboards | Business and system dashboards | | | |
| AP-OBS-10 | SLO-based alerting | Alerts on SLO breaches, not raw noise | | | |
| AP-OBS-11 | Log retention | Retention per log type | | | |
| AP-OBS-12 | Audit log separate from technical log | Business audit in the database; technical logs in the log platform | | | |

### N. Performance & scalability (PERF)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-PERF-01 | Performance budgets | Response-time targets per screen / API | | | |
| AP-PERF-02 | Horizontal scaling | Stateless instances added under load | | | |
| AP-PERF-03 | Caching | Reference data and expensive reads cached | | | |
| AP-PERF-04 | Async processing for heavy work | Long tasks moved off the request path | | | |
| AP-PERF-05 | Connection pooling | DB and HTTP connections pooled | | | |
| AP-PERF-06 | Efficient queries | Indexes, no N+1, projections | | | |
| AP-PERF-07 | Payload efficiency | Pagination, compression, minimal payloads | | | |
| AP-PERF-08 | Static content via CDN | Frontend assets served from edge | | | |
| AP-PERF-09 | Capacity planning | Sizing from volumetrics, reviewed yearly | | | |
| AP-PERF-10 | Performance testing | Load, stress, soak, spike before go-live | | | |

### O. Resilience & availability (RES)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-RES-01 | Timeouts everywhere | Every remote call bounded | | | |
| AP-RES-02 | Retry with backoff and jitter | Transient errors retried safely | | | |
| AP-RES-03 | Circuit breaking | Failing dependencies isolated | | | |
| AP-RES-04 | Bulkheads | Resource pools per dependency | | | |
| AP-RES-05 | Graceful degradation | Partial functionality when a dependency is down | | | |
| AP-RES-06 | Redundancy across zones | No single point of failure | | | |
| AP-RES-07 | RTO / RPO targets | Recovery objectives defined and tested | | | |
| AP-RES-08 | Idempotent operations | Safe to retry writes | | | |
| AP-RES-09 | Self-healing | Failed instances replaced automatically | | | |
| AP-RES-10 | Failure injection | Planned tests of failure scenarios | | | |

### P. DevOps & continuous delivery (DEV)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-DEV-01 | CI/CD pipeline per service | Build, test, scan, deploy automated | | | |
| AP-DEV-02 | Branching strategy | Agreed model (e.g. trunk-based) with protected main | | | |
| AP-DEV-03 | Infrastructure as code | All environments from code | | | |
| AP-DEV-04 | Build once, deploy many | Same immutable artifact promoted across environments | | | |
| AP-DEV-05 | Containerization | Services packaged as container images | | | |
| AP-DEV-06 | Automated quality gates | Coverage, static analysis, security scan block merges | | | |
| AP-DEV-07 | Deployment strategy | Rolling / blue-green with rollback | | | |
| AP-DEV-08 | Feature toggles | Incomplete features hidden in production | | | |
| AP-DEV-09 | Semantic versioning | Versions for services, APIs and events | | | |
| AP-DEV-10 | Automated database migrations | Migrations run in the pipeline, reversible plan | | | |
| AP-DEV-11 | No secrets in repository | Secret scanning in pipeline | | | |

### Q. Testing & quality (QA)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-QA-01 | Test pyramid | Many unit, fewer integration, few end-to-end tests | | | |
| AP-QA-02 | Coverage targets | Unit test and code-quality thresholds enforced | | | |
| AP-QA-03 | Contract testing | API and event contracts verified on both sides | | | |
| AP-QA-04 | Integration tests with real dependencies | Containers for DB and broker in tests | | | |
| AP-QA-05 | End-to-end tests | Critical journeys automated | | | |
| AP-QA-06 | Performance tests | Per PT strategy | | | |
| AP-QA-07 | Security tests | Per security testing plan | | | |
| AP-QA-08 | Test data management | Synthetic data; no production personal data | | | |
| AP-QA-09 | Shift-left quality | Reviews, static checks and tests early | | | |
| AP-QA-10 | Definition of done | Agreed checklist per story | | | |

### R. AI-assisted delivery (AI)

| Id | Principle | Description | Applicability | Realization | Ref |
| --- | --- | --- | --- | --- | --- |
| AP-AI-01 | Human in the loop | Every AI-produced artifact is reviewed and approved by a person | | | |
| AP-AI-02 | Traceable AI output | Artifacts state their inputs and the decisions they implement | | | |
| AP-AI-03 | Layered AI memory | Platform, project, user and session memory kept separate | | | |
| AP-AI-04 | Guardrail rules for agents | Project rules restrict which agents and tools may be used | | | |
| AP-AI-05 | Curated knowledge base | Only approved project documents are fed to agents | | | |
