# ADR-004: API gateway holds the user tokens – the browser gets only a session cookie

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-11-22 |
| Deciders | Rajesh Verma (product owner, Enterprise Architect) |
| Decision log ref | D-110 (6), D-111, D-113 |
| Related principles / patterns | AP-MS-05, AP-MS-25, AP-CP-17, AP-CP-20, AP-XF-03 |

## Context

PMS is a single-page web application signing in at an OIDC identity provider (ADR-003). Tokens kept in the browser can be read by page scripts; logout, idle timeout (D-26) and session ending on reset, deactivation, role change and own password change (D-97, D-100, D-111) must be enforced reliably. No shared cache or session store is used in the POC (D-110 (8)).

## Decision

The API gateway is the confidential OIDC client (Authorization Code + PKCE). It keeps the access, refresh and ID tokens server side and gives the browser only an HttpOnly, Secure, SameSite=Lax session cookie; state-changing calls carry a CSRF token. The gateway relays the access token to the services. With two gateway instances and no shared store, the edge uses session affinity and the gateway relays identity-provider back-channel logouts to its peer instance.

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
| --- | --- | --- | --- |
| Tokens in browser memory (SPA with PKCE) | Simpler gateway; stateless | Tokens reachable by page scripts; refresh and logout logic in the frontend | Weaker security for personal and wage data |
| Gateway sessions in a shared store (Redis) | No affinity; clean failover | One more component to run | No cache server in the POC (D-110); planned for a future phase |

## Consequences

- **Positive:** No token in the browser; session rules enforced in one place; services see a standard bearer token.
- **Negative / trade-offs:** Session affinity at the edge; a gateway failover re-runs the sign-in silently and a request in flight can fail; a missed back-channel logout lasts at most the access-token lifetime (5 minutes) (AR-02).
- **Follow-ups:** Shared session store in a future phase; CSRF and cookie rules in the security standard.
