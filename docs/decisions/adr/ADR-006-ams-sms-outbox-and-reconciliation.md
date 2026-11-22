# ADR-006: AMS → SMS hand-over by transactional outbox, idempotent consumer and nightly reconciliation

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-11-22 |
| Deciders | Rajesh Verma (product owner, Enterprise Architect) |
| Decision log ref | D-16, D-21, D-24, D-90, D-110 (7), D-113 |
| Related principles / patterns | AP-MS-08, AP-MS-10, AP-MS-16, AP-INT-07, AP-INT-12, AP-EIP-10, AP-EIP-54, AP-CP-37 |

## Context

A salary record must be generated within 1 minute of attendance approval and voided when attendance is reopened (INT-01, INT-02, NFR-01), with exactly one non-voided salary record per approved attendance (NFR-06, KPI-04). AMS and SMS own separate databases (D-10); a lost or duplicated hand-over would create wrong wages (R-01, R-03).

## Decision

AMS writes each attendance-approved or attendance-reopened event to an outbox table in the same transaction as the status change; an outbox relay publishes it to a broker topic. SMS consumes it through a durable subscription and processes each event once (event id and attendance id); events that keep failing go to a dead-letter queue. Every night at 01:00 IST a reconciliation job in SMS, running in one instance under a database lock, reads approved attendance from AMS and creates missing records, voids stale ones and logs other mismatches (JOB-CMN-01).

## Alternatives considered

| Option | Pros | Cons | Why not chosen |
| --- | --- | --- | --- |
| Synchronous call AMS → SMS on approval | Simple | Approval fails when SMS is down; no failure isolation | Conflicts with NFR-02 and FR-CMN-008 isolation |
| Publish directly without an outbox | Less code | Event lost if the broker is down after the commit | R-01 |
| Reconciliation only (no events) | Simplest | Salary records up to a day late | NFR-01 (1 minute) |

## Consequences

- **Positive:** Hand-over survives broker or SMS outages; duplicates are harmless; any remaining gap is repaired nightly; one flow reference links AMS and SMS entries.
- **Negative / trade-offs:** Outbox relay, idempotency record and job lock to build and operate; eventual consistency of up to 1 minute (normal) or one night (failure).
- **Follow-ups:** Event envelope and schema in `contracts/events` (Part02 anchor); outbox clean-up rule in Part03.
