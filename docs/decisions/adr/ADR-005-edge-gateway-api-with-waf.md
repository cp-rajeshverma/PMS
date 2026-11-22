# ADR-005: Edge on the Kubernetes Gateway API with a WAF rule set

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-11-22 |
| Deciders | Rajesh Verma (product owner, Enterprise Architect) |
| Decision log ref | D-112 (2) (amends D-110 (3)), D-113 |
| Related principles / patterns | AP-CP-20, AP-CP-21, AP-CP-18, AP-WA-07 |

## Context

D-110 placed ingress-nginx with ModSecurity at the edge of the local cluster. The Kubernetes project retired ingress-nginx in March 2026: no further releases or security fixes. The edge is the only entry point and must apply TLS, routing and a WAF rule set, and must work the same on-premises and on AWS (ADR-002).

## Decision

The edge uses the Kubernetes Gateway API, implemented by Envoy Gateway, with the Coraza WAF and the OWASP Core Rule Set. On AWS the same edge runs on EKS behind the Application Load Balancer and AWS WAF.

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
| --- | --- | --- | --- |
| Keep ingress-nginx | Already known | Retired, no security fixes | Unacceptable security risk |
| Traefik Proxy | Simple; Ingress and Gateway API | WAF needs a plugin or external component | Weaker WAF story |
| NGINX Gateway Fabric | NGINX-based Gateway API | WAF (App Protect) is commercial | Licence cost for the POC |

## Consequences

- **Positive:** Supported, standard routing API; the same Gateway and route definitions on every platform; open-source WAF with the OWASP rule set.
- **Negative / trade-offs:** The WAF runs as a dynamic module; loading by image volume needs Kubernetes 1.35 or later (AR-06, OI-P01-05).
- **Follow-ups:** WAF rule tuning and exclusions in the security standard.
