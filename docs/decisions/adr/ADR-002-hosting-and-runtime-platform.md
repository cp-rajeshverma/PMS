# ADR-002: Hosting and runtime platform – on-premises Kubernetes for the POC, AWS as the cloud target

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-11-22 |
| Deciders | Rajesh Verma (product owner, Enterprise Architect) |
| Decision log ref | D-109 (amends D-11 for hosting) |
| Related principles / patterns | AP-XF-05, AP-WA-02, AP-WA-05, AP-WA-06, AP-MS-28, AP-TF (Twelve-Factor) |

## Context

D-11 named Azure App Service and Azure Database for PostgreSQL as hosting. The POC must first be deployed on-premises, and the same design must be deployable to AWS later without redesign. Services must scale out per module (NFR-07), run two instances per stateless tier in Production (D-109) and stay technology-neutral for replatforming (D-12, NFR-08). Containers (Docker) are already decided (D-11).

## Decision

PMS runs as containers on a Kubernetes platform on-premises for Dev, QA and Prod in the POC. AWS is the documented cloud target: Amazon EKS for the containers and Amazon RDS for PostgreSQL in ap-south-1 (Mumbai). ActiveMQ Artemis stays self-hosted on both platforms. Azure is no longer a target.

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
| --- | --- | --- | --- |
| Azure App Service + Azure Database for PostgreSQL (D-11) | Managed PaaS, little operations work | Not deployable on-premises; ties the POC to one cloud | Hosting requirement changed to on-premises first, AWS later |
| Docker Compose on Linux VMs | Simplest to run | Manual scaling and failover; new deployment files for AWS | Does not meet per-service scale-out and portability as well |
| Plain VMs without containers | Familiar to operations | Conflicts with D-11 (Docker); poor portability | Rejected |
| Mapping to both AWS and Azure | Keeps both clouds open | Double documentation, no single target | Not needed for the POC |

## Consequences

- **Positive:** The same container images and deployment definitions run on-premises and on Amazon EKS; per-service scale-out and two-instance redundancy come from the platform.
- **Negative / trade-offs:** The on-premises platform (Kubernetes, PostgreSQL, broker, backups) is self-managed; Kubernetes adds operations skill needs for a small POC.
- **Follow-ups:** Provisioning approach (infrastructure as code) and on-premises infrastructure details in Part01 §6.3, §7 and §15 (OI-P01-02); AWS mapping in Part01 §6.2.
