# ADR-003: Identity provider issues tokens and holds passwords

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-11-22 |
| Deciders | Rajesh Verma (product owner, Enterprise Architect) |
| Decision log ref | D-109 (reading of D-11 "JWT + bcrypt" with D-16, D-26, D-29) |
| Related principles / patterns | AP-CP-17, AP-MS-25, AP-XF-03 |

## Context

D-11 lists "JWT + bcrypt"; D-16 chose Keycloak as identity provider and D-26, D-29 and D-97 place lockout, session, role and security events there. The BRD set requires that passwords are never stored or shown in readable form (NFR-03, FR-AUTH-014) and stays technology-neutral ("identity provider").

## Decision

The identity provider signs the JWT access tokens (OpenID Connect, Authorization Code with PKCE for interactive sign-in) and stores and hashes passwords with its own built-in algorithm. PMS services hold no passwords and contain no password-hashing code; they validate the tokens only.

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
| --- | --- | --- | --- |
| Identity provider configured to hash with bcrypt through an add-on provider | Meets D-11 literally | Custom component to build, test and maintain | No business need for bcrypt specifically |
| PMS issues its own JWTs and hashes passwords with bcrypt | No identity provider to run | Conflicts with D-16, D-26, D-29; PMS must build lockout, sessions and security events | Rejected |

## Consequences

- **Positive:** One place for passwords, lockout, sessions and security events; services stay technology-neutral and replatformable.
- **Negative / trade-offs:** The password-hashing algorithm is the identity provider's choice; it is recorded in Part01 §9.2 and the security standard.
- **Follow-ups:** Token design, browser token handling and session design in Part01 §9.
