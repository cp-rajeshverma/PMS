# <Project> – HLD Part01: Application Architecture & Design

Document ID: <PRJ>-HLD-Part01-Architecture-and-Design-v<x.y>
Project: <project name and phase>
Author: <name>
Date: <Month YYYY>

## 1. Document control

### 1.1 Version / revision history

| Version | Revision | Date | Author | Change remark |
| --- | --- | --- | --- | --- |
| 1.0 | 0.1 | <dd-Mon-yyyy> | <name> | Design based on BRD v<x> |

### 1.2 Review and approval

| Role | Name | Date | Decision |
| --- | --- | --- | --- |
| Architect | | | |
| Product owner | | | |

## 2. Introduction

This document describes the overall architecture and design of <application>. It is a Big Design Up Front (BDUF) artifact: it must be approved before implementation starts.

### 2.1 Reference documents

**Requirement documents**

| # | Document | Version |
| --- | --- | --- |
| 1 | <PRJ>-BRD (anchor), <PRJ>-BRD-M<n>-<MOD>, <PRJ>-BRD-M<n>-SUP | v<x> |
| 2 | UX Journey Index and UX Summaries | v<x> |
| 3 | Decision log / ADRs | D-01 to D-<nn> |

**Design documents**

| # | Document | Purpose |
| --- | --- | --- |
| 1 | <PRJ>-HLD-Part01-Architecture-and-Design | Overall architecture and design (this document) |
| 2 | <PRJ>-HLD-Part01a-Principles-Patterns-Decisions | Catalogue of principles and patterns with applicability and realization; ADR register and format |
| 3 | <PRJ>-HLD-Part02-M<n>-<MOD>-Functional | Solution approach for system functions of each functional module |
| 4 | <PRJ>-HLD-Part02-M<n>-SUP-Functional | Solution approach for supporting modules |
| 5 | <PRJ>-HLD-Part03-Datamodel | Data model |
| 6 | Standards and guardrails (`docs/04-standards/`) | Coding, API, database, security, testing rules |

### 2.2 Application overview

#### 2.2.1 Business background

<Business problem, users, main business flow, in 2–3 short paragraphs. Source: BRD anchor §3.>

#### 2.2.2 Application background

<Modules and their purpose; supporting capabilities; architecture in one paragraph (style, frontend, backend, data, identity, messaging, hosting); peripheral systems in one sentence each.>

## 3. Architecture approach & governance (BDUF)

### 3.1 Design-before-build artifact checklist

Implementation starts only when every mandatory artifact below is approved.

| # | Artifact | Document / section | Mandatory before build | Stakeholders to align | Status | Approved on |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Functional architecture | §5 | Yes | Product owner, BA | | |
| 2 | System architecture | §6 | Yes | Architect, infra, security | | |
| 3 | Deployment architecture | §7 | Yes | Architect, infra, DevOps | | |
| 4 | Integration architecture | §8 | Yes | Architect, integration owners | | |
| 5 | Authentication & authorization | §9 | Yes | Security, architect | | |
| 6 | Logging & observability | §10 | Yes | Operations, architect | | |
| 7 | Principles & patterns compliance | Part01a | Yes | Architect | | |
| 8 | Functional HLDs per module | Part02 | Yes | BA, dev leads | | |
| 9 | Data model | Part03 | Yes | Architect, DBA | | |
| 10 | API and event contracts | `contracts/` | Yes | Dev leads | | |
| 11 | Performance test strategy & plan | §14 | Before PT | QA, operations | | |
| 12 | Standards & guardrails | `docs/04-standards/` | Yes | Architect, dev leads | | |

### 3.2 Stakeholder alignment log

| Date | Topic / artifact | Stakeholders | Outcome | Decision ref |
| --- | --- | --- | --- | --- |

## 4. Architecture principles & patterns

The full catalogue (Part01a) assesses every principle and pattern. This chapter summarizes compliance.

### 4.1 Compliance summary by group

| Group (Part01a) | Applied | Partial | Deferred | N/A | Key items |
| --- | --- | --- | --- | --- | --- |

### 4.2 X-First principles

| Principle | How the design complies | Ref |
| --- | --- | --- |
| UX first | | |
| API first | | |
| Security first | | |
| Performance first | | |
| Cloud first | | |
| <others> | | |

### 4.3 Well-architected compliance

| Quality | Design response | Ref |
| --- | --- | --- |
| Resiliency | | |
| Availability | | |
| Decentralized | | |
| Independent & autonomous | | |
| Auto provisioning | | |
| Scalability | | |
| Security | | |
| Continuous delivery | | |
| Failure isolation | | |
| Observability | | |

### 4.4 Patterns applied

| Category | Patterns applied (Part01a ids) | Where |
| --- | --- | --- |
| Microservice design patterns | | |
| Cloud design patterns | | |
| Enterprise integration patterns | | |

## 5. Functional architecture

### 5.1 Functional building blocks

A representational block diagram of the application's functional architecture. It shows every functional component of the application (business modules and supporting modules) and the peripheral systems that integrate with it.

<Block diagram: application boundary containing business modules and supporting modules; peripheral systems outside the boundary, connected to the components they integrate with.>

**Text version of the diagram** (for readers and AI agents)

| Building block | Type (business module / supporting module / peripheral system) | Key capabilities | Integrates with |
| --- | --- | --- | --- |

### 5.2 End-to-end functional process

A high-level business process diagram showing how each functional component and peripheral system takes part in the process, from the first business event to the final outcome.

<Process diagram: swimlane per functional component / peripheral system; steps, decision points, handovers between components and backend jobs.>

**Text version of the diagram**

| Step | Functional component / peripheral system | Activity | Output / next step |
| --- | --- | --- | --- |

### 5.3 Domain / sub-domain based micro-application identification

A tower diagram. Each tower cuts across all three layers – Frontend, Backend API and Backend DB – and represents one micro-application, equivalent to one microservice. Towers are grouped under the domain / sub-domain they belong to.

<Tower diagram: columns = towers grouped by domain / sub-domain; rows = Frontend, Backend API, Backend DB; each cell names that tower's component in the layer.>

**List of microservices**

| Seq | Domain / sub-domain name | Domain context | Purpose |
| --- | --- | --- | --- |
| 1 | | /<context>/ | |

### 5.4 Stakeholder alignment

| Stakeholder | Date | Outcome |
| --- | --- | --- |

## 6. System architecture

### 6.1 Logical system architecture (technology-neutral)

<Layered diagram: channel, security/DMZ, load balancer, API gateway, identity provider, web/static hosting, application services, message broker, cache, database, observability, backup and recovery, CI/CD.>

| Seq | Component | Purpose | Technology | Instances / sizing |
| --- | --- | --- | --- | --- |
| 1 | Load balancer | | | |
| 2 | API gateway | | | |
| 3 | Identity provider | | | |
| 4 | Web server / static hosting | | | |
| 5 | Application services | | | |
| 6 | Message broker / queue | | | |
| 7 | Cache server | | | |
| 8 | Database server | | | |
| 9 | Scheduler / batch | | | |
| 10 | Log and monitoring stack | | | |
| 11 | Backup and recovery | | | |

### 6.2 Cloud system architecture (<cloud provider>)

<Diagram of the components mapped to cloud services.>

| Seq | Cloud service | Purpose | HA and scalability assurance |
| --- | --- | --- | --- |

### 6.3 Network topology (<cloud / on-premises>)

How the system's components are placed and connected on the network – cloud or on-premises, whichever applies. Shows network boundaries, zones / subnets, availability zones or data centres, entry points and the controls between them.

<Network topology diagram.
Cloud: virtual network (VNet / VPC), public, private and data subnets, availability zones, internet entry (DNS, WAF, load balancer / application gateway), NAT / egress, private endpoints for PaaS services, peering / VPN / ExpressRoute to other networks.
On-premises: internet edge, DMZ, firewalls, VLANs / segments, load balancers, server farms, database segment, management network, links to other sites.>

**Network zones / subnets**

| Zone / subnet | Address range (CIDR) | Purpose | Components placed | Exposure (public / private) |
| --- | --- | --- | --- | --- |

**Allowed traffic flows**

| Source zone | Destination zone | Protocol / port | Purpose | Control (NSG / firewall rule / private endpoint) |
| --- | --- | --- | --- | --- |

**External connectivity**

| Connection | Type (internet / VPN / private link / peering) | Purpose | Security |
| --- | --- | --- | --- |

### 6.4 Per-tier redundancy

| Tier | Zone count | Redundancy model | Failover behaviour |
| --- | --- | --- | --- |

### 6.5 Stakeholder alignment

| Stakeholder | Date | Outcome |
| --- | --- | --- |

## 7. Deployment architecture

Shows how and where the system runs: nodes (hardware or software execution environments), the artifacts deployed on them and the middleware connecting them.

### 7.1 Deployment diagram

<UML-style deployment diagram per environment: nodes, execution environments, deployed artifacts, communication paths.>

### 7.2 Nodes and execution environments

| Node | Type (VM / container / PaaS / SaaS) | Execution environment (runtime, version) | Deployed artifacts | Zone / subnet | Scaling |
| --- | --- | --- | --- | --- | --- |

### 7.3 Middleware and communication paths

| From node | To node | Middleware / protocol | Port | Security (TLS, auth) |
| --- | --- | --- | --- | --- |

### 7.4 Deployment per environment

| Environment | Nodes and sizing | Differences from production |
| --- | --- | --- |

### 7.5 Stakeholder alignment

| Stakeholder | Date | Outcome |
| --- | --- | --- |

## 8. Integration architecture

All integrations between components in the ecosystem: internal service-to-service, frontend-to-backend, and external systems.

### 8.1 Functional integration diagram

<Diagram: systems and data flowing between them.>

### 8.2 Integration catalogue

| Seq | Source | Target | Data object | Style (sync / async / batch) | Integration pattern (Part01a id) | Protocol | Message format | Authentication | Connection mechanism | Error handling |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### 8.3 Technical integration diagram

<Diagram: gateway, services, broker queues/topics, outbox relay, scheduled jobs, external endpoints.>

### 8.4 Protocol and pattern selection guide

| Need | Chosen protocol / pattern | Reason |
| --- | --- | --- |
| Query from UI | | |
| Command from UI | | |
| State change to other services | | |
| Bulk / periodic data | | |
| Long-running process | | |

### 8.5 Integration resilience defaults

| Integration type | Timeout | Retry policy | Circuit breaker | Idempotency | Dead-letter handling |
| --- | --- | --- | --- | --- | --- |
| Internal REST APIs | | | | | |
| Async events | | | | | |
| External APIs | | | | | |

### 8.6 Stakeholder alignment

| Stakeholder | Date | Outcome |
| --- | --- | --- |

## 9. Authentication & authorization

Architecture-level design of identity, access and API security. User-facing functions (sign-in, sign-out, onboarding, user / role administration) are designed in Part02-SUP §4.1–4.2.

### 9.1 Users, user categories and roles

| User category | Description | Authentication path | MFA |
| --- | --- | --- | --- |

| Role id | Role name | Role type (business / system / external) | Data scope |
| --- | --- | --- | --- |

### 9.2 Identity provider / authorization server

| Item | Decision |
| --- | --- |
| Product / service | |
| Realm / tenant design | |
| User store (IdP-managed / federated / application) | |
| Clients (per frontend, per service) | |
| Environments (one realm per environment / shared) | |

### 9.3 Authentication flows

| Flow | Used by | Protocol / grant (e.g. OIDC Authorization Code + PKCE, Client Credentials) | Notes |
| --- | --- | --- | --- |
| Interactive user sign-in | | | |
| Token refresh | | | |
| Sign-out / single logout | | | |
| Service-to-service | | | |

<Sequence diagram of the interactive sign-in flow: Browser, Frontend, Gateway, IdP, Service.>

### 9.4 MFA approach

<Which users / roles / actions require MFA, factors allowed, enrolment and recovery, step-up for sensitive actions.>

### 9.5 Token design

| Item | Decision |
| --- | --- |
| Token type and format (JWT) | |
| Signing algorithm and key rotation | |
| Access token lifetime | |
| Refresh token lifetime and rotation | |
| Claims (sub, roles, scopes, data-scope attributes, tenant) | |
| Audience per service | |
| Revocation / forced logout | |
| Token storage in the browser | |

### 9.6 Session management

| Item | Decision |
| --- | --- |
| Session idle timeout | |
| Absolute session timeout | |
| Concurrent sessions | |
| Account lockout policy | |

### 9.7 Authorization model

| Layer | Mechanism | Enforced at |
| --- | --- | --- |
| Coarse-grained (role → API / route) | RBAC | Gateway |
| Fine-grained (role → feature / action) | Permission | Service |
| Data scope (own / reportees / all) | Row-level rule | Service / query |
| UI (menu, button visibility) | Claims-driven | Frontend (never the only check) |

### 9.8 API-level security

| Control | Decision |
| --- | --- |
| Token validation (signature, issuer, audience, expiry) | |
| Scopes per API | |
| Rate limiting / throttling | |
| CORS policy | |
| Input validation and payload limits | |
| Security headers | |
| Public (unauthenticated) endpoints | |

### 9.9 Service-to-service authentication

<Client credentials / mTLS / token exchange; how the user identity propagates in calls and events (correlation id, on-behalf-of).>

### 9.10 Secrets and key management

<Secret store, rotation, who can read; no secrets in code, images or logs.>

### 9.11 Stakeholder alignment

| Item | Stakeholder | Date | Outcome |
| --- | --- | --- | --- |

## 10. Unified & centralized logging and observability

### 10.1 Logging architecture

<Diagram: each node → log shipper/agent → central log platform → dashboards and alerts.>

### 10.2 Log types

| Log type | Purpose | Produced by | Store | Retention |
| --- | --- | --- | --- | --- |
| Application log | | | | |
| Access log (gateway, web) | | | | |
| Business event log | | | | |
| Security log | | | | |
| Audit trail (business) | | | | |
| Infrastructure / platform log | | | | |

### 10.3 Standard log record

| Field | Description | Mandatory |
| --- | --- | --- |
| timestamp (UTC, ISO-8601) | | Y |
| level | | Y |
| service / node | | Y |
| environment | | Y |
| correlation_id | | Y |
| trace_id / span_id | | Y |
| user_id (no personal data) | | N |
| event_type | | Y |
| message | | Y |
| business keys (e.g. entity id) | | N |
| error code / stack (errors only) | | N |

### 10.4 Logging per node

| Node / component | Events logged | Level policy | Shipping method |
| --- | --- | --- | --- |

### 10.5 Correlation and tracing

<How the correlation id is created at the edge and propagated through HTTP headers, message headers and jobs; tracing standard.>

### 10.6 KPIs derived from logs

| KPI | Type (business / system) | Source events | Dashboard |
| --- | --- | --- | --- |

### 10.7 Metrics, dashboards and alerts

| Signal | Threshold / SLO | Alert channel | Owner |
| --- | --- | --- | --- |

### 10.8 Privacy and retention

<Personal data masking rules; retention per log type; access to logs.>

## 11. Technology stack

### 11.1 Development

| Layer | Component | Technology | Version | Remark |
| --- | --- | --- | --- | --- |

### 11.2 Deployment and operations

| Layer | Technology | Remark |
| --- | --- | --- |

### 11.3 AI / ML (if applicable)

| Component | Technology | Remark |
| --- | --- | --- |

## 12. Data architecture (summary)

Full design in <PRJ>-HLD-Part03-Datamodel. Summary: database per service, data ownership, caching, retention, backup (RPO/RTO).

| Service | Database / schema | Main entities | Cached data | RPO / RTO |
| --- | --- | --- | --- | --- |

## 13. Data migration strategy

<Master vs transaction data; what is migrated; approach; cutover; open questions. Or "Not applicable – greenfield" with seed-data approach.>

## 14. Performance test strategy and plan

### 14.1 Performance targets (SLAs)

| Tier / transaction type | p95 response | Throughput | Error rate |
| --- | --- | --- | --- |

### 14.2 Use cases for load testing

| Use case id | Business use case | Journey / API | Why included (volume / criticality) |
| --- | --- | --- | --- |

### 14.3 Load distribution (business mix)

| Use case id | Share of load % | Peak concurrent users | Transactions per hour | Think time |
| --- | --- | --- | --- | --- |

### 14.4 Test types and scenarios

| Test type | Objective | Load profile | Duration |
| --- | --- | --- | --- |
| Load | | | |
| Stress | | | |
| Soak / endurance | | | |
| Spike | | | |

### 14.5 Test data strategy

<Volume, generation approach, owner, reset between runs.>

### 14.6 Environment and tools

<PT environment sizing vs production; tools; monitoring during tests.>

### 14.7 Entry and exit criteria

| Criteria | Entry | Exit |
| --- | --- | --- |

### 14.8 Schedule and responsibilities

| Activity | Owner | Planned date |
| --- | --- | --- |

### 14.9 Analysis and tuning

<How results are analysed, bottlenecks fixed and tests re-run; reporting format.>

## 15. Environment strategy

<Diagram: non-prod environments, CI/CD, production.>

| Environment | Purpose | Owner | Availability | Hosting |
| --- | --- | --- | --- | --- |

**Security posture per environment:** <production vs non-production controls; no unmasked personal data outside production.>

**CI/CD:** <tooling, pipeline stages, quality gates.>

**Testing and deployment flow:** <environment → test phase → owning team.>

## 16. Security & NFR

### 16.1 Security guidelines

| Seq | Security type | Description | Realization |
| --- | --- | --- | --- |
| 1 | Infrastructure-level security | | |
| 2 | Application-level security | | |
| 3 | Data at rest | | |
| 4 | Data in transit | | |
| 5 | Secure environment access | | |
| 6 | Safe coding and deployment | | |
| 7 | Secrets and key management | | |

### 16.2 OWASP Top 10 control mapping

| OWASP category | Control |
| --- | --- |
| A01 Broken Access Control | |
| A02 Cryptographic Failures | |
| A03 Injection | |
| A04 Insecure Design | |
| A05 Security Misconfiguration | |
| A06 Vulnerable and Outdated Components | |
| A07 Identification and Authentication Failures | |
| A08 Software and Data Integrity Failures | |
| A09 Security Logging and Monitoring Failures | |
| A10 Server-Side Request Forgery | |

### 16.3 Non-functional requirements realization

| Seq | NFR id (BRD) | NFR | Realization | Verification |
| --- | --- | --- | --- | --- |

## 17. Volumetrics

**Current volume:** <users, transactions per year, by entity>

| Volume type | YoY % | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Users | | | | | | |
| Transactions | | | | | | |

| Entity | Rows per year | Avg row size | Year-5 size |
| --- | --- | --- | --- |

## 18. Architecture decisions

Architecture decisions are registered in <PRJ>-HLD-Part01a-Principles-Patterns-Decisions §5 (ADR register); each ADR is a separate file in `docs/decisions/adr/` using the format in Part01a §6. List here only the ADRs that shape this document's chapters:

| ADR | Title | Affects Part01 chapter(s) |
| --- | --- | --- |

## 19. Risks and technical debt

| Id | Item | Impact | Mitigation / plan |
| --- | --- | --- | --- |

## 20. Appendix

<Open items, glossary, future scope.>
