# PMS – BRD Open Items: Decision Note

Document ID: PMS-BRD-OIN-v1.0
To: HR Manager (business owner, all modules)
From: Rajesh Verma (Enterprise Architect)
Date: 20 November 2026
Status: **Decided 20 November 2026** – option A for all six items (decision D-104); for the HR Manager's information and confirmation at the stakeholder review

## Purpose

The PMS BRD set (anchor and five module documents) is drafted and has passed its consistency check. Six business questions remained before the set could go to stakeholder review and sign-off. Each one below gives the question, why it matters, the options and their effect. To keep the review on schedule, option A was decided for every item on 20 November 2026 by the product owner on behalf of the HR Manager (D-104), and the BRD documents were updated accordingly (anchor rev 0.15, module documents rev 0.3). Please confirm these decisions at the stakeholder review; any change will be recorded as a new decision.

## Summary

| Id | Question | Decision (D-104) | Requirements updated |
| --- | --- | --- | --- |
| OI-02 | Pending items of a deactivated employee | A – decide what is waiting, keep the rest as it is | BR-CMN-06, FR-EIMS-018 |
| OI-03 | Does "missing attendance" include today? | A – only up to yesterday | FR-CMN-004, FR-AMS-003 |
| OI-04 | Who decides waiting items after a manager change? | A – the new manager | FR-EIMS-017, FR-UM-014 |
| OI-12 | More than one employee without a manager? | A – exactly one | BR-CMN-01, FR-EIMS-014, VR-EIMS-05 |
| OI-EIMS-01 | How the temporary password reaches the employee | A – company email from the Admin | NOT-EIMS-06, FR-AUTH-013 |
| OI-EIMS-02 | Onboarding at go-live: one by one or bulk import? | A – one by one; import in Phase 2 | PMS-BRD-M1-EIMS §3.2, §13 |

## OI-02 – Pending items when an employee is deactivated

**Question.** An employee leaves while some of their items are still open: attendance, leave or a profile change waiting for approval, a salary dispute, or salary records they have not yet accepted. What happens to them? (A manager who still has active team members cannot be deactivated – BR-CMN-14.)

**Why it matters.** It decides what approvers see after a leaver is deactivated and whether salary records stay open forever. Affects FR-EIMS-018, the approvals inbox (FR-CMN-010) and the salary records (PMS-BRD-M4-SMS).

| Option | Effect on users | Effect on the BRD |
| --- | --- | --- |
| **A (decided)** – The approver still decides submitted items and disputes; drafts, rejected items and salary records waiting for acceptance stay as they are and are kept for history | Approvers finish their work as normal; nothing is changed on the leaver's behalf | One rule added; no new screen |
| B – Deactivation is refused while the employee has submitted items or disputes, listing them | HR must chase approvers before a leaver can be deactivated | New check and message on the employee form |
| C – Deactivation closes everything automatically (leave cancelled, requests withdrawn, salary accepted) | Records change without the employee's action; disputes lost | Several new system rules across modules |

## OI-03 – Does the missing-attendance reminder include today?

**Question.** The dashboard reminds employees of weekdays with no attendance and no leave. Should today count, or only days up to yesterday?

**Why it matters.** It decides what employees see every morning. Affects FR-CMN-004 and FR-AMS-003.

| Option | Effect on users | Effect on the BRD |
| --- | --- | --- |
| **A (decided)** – Up to yesterday | No reminder for a day that is still in progress; fewer false alarms | Wording of FR-CMN-004 only |
| B – Include today | Today shows as missing until entered; reminder every morning | Wording of FR-CMN-004 only |

## OI-04 – Waiting items after a manager change

**Question.** When the Admin moves an employee to a new manager, who decides the items that were already waiting – the old or the new manager?

**Why it matters.** Without a rule, items could be left with a manager who can no longer see the employee. Affects FR-EIMS-017, FR-UM-014 and the approvals inbox.

| Option | Effect on users | Effect on the BRD |
| --- | --- | --- |
| **A (decided)** – Waiting items move to the new manager | Nothing is stranded; matches the rule that the old manager no longer sees the employee | Wording of FR-EIMS-017 and FR-UM-014 |
| B – The old manager decides items submitted before the change | Old manager keeps a partial view of a former team member | New exception to the data-scope rule |
| C – Manager change refused while items are waiting | HR must wait for approvals before reorganising | New check and message on the employee form |

## OI-12 – More than one employee without a manager?

**Question.** An employee with no manager ("None – top-level") has all records approved by the PMS Administrator. May more than one employee be top-level?

**Why it matters.** It decides how many people the Administrator approves for and how the onboarding form behaves. Affects BR-CMN-01, FR-EIMS-014, VR-EIMS-05 and "Also away" in leave review (BR-LMS-09).

| Option | Effect on users | Effect on the BRD |
| --- | --- | --- |
| **A (decided)** – Exactly one | Clear top of the organisation; Administrator approves for one person only | Validation added to FR-EIMS-014 / VR-EIMS-05 |
| B – Several allowed | Flexible for several heads; Administrator approves all their records; "Also away" stays empty for each | Wording of BR-CMN-01 and glossary |

## OI-EIMS-01 – Handing over the temporary password

**Question.** PMS shows a new employee's temporary password once, to the Administrator. How does it reach the employee?

**Why it matters.** It is the first step for every new user and a security point. Affects FR-EIMS-005, FR-EIMS-041 and FR-AUTH-013. In every option the employee must replace the temporary password at the first sign-in before any other screen opens (FR-AUTH-006, already in the BRD).

| Option | Effect on users | Effect on the BRD |
| --- | --- | --- |
| **A (decided)** – The Administrator sends it by company email, outside PMS | Works for remote joiners; the password is changed at first sign-in, so the email holds no lasting secret | Procedure note only; PMS sends no email in the POC |
| B – In person or by phone, never in writing | Most secure; needs the joiner to be reachable | Procedure note only |
| C – PMS sends the email automatically | No manual step | Needs the notification capability, planned for Phase 2; not possible in the POC without a scope change |

## OI-EIMS-02 – Onboarding at go-live

**Question.** At go-live, does the Administrator onboard every employee one by one, or is a bulk import needed?

**Why it matters.** It sets the go-live effort and whether a new function enters the POC. Affects PMS-BRD-M1-EIMS §3.2 and §13.

| Option | Effect on users | Effect on the BRD |
| --- | --- | --- |
| **A (decided)** – One by one with the approved screen; bulk import in Phase 2 | About 20 sample employees for the POC and about 100 in year 1 – manageable by hand | Bulk import added to future scope only |
| B – Bulk import in the POC | Faster go-live for large numbers | New requirements, file format, error handling and a screen change before design starts |

## Next steps

The six items are closed in the BRD set. The set now goes to stakeholder review (Business Analyst, HR Manager, Finance Manager, Security / IT owner) and sign-off, where these decisions are confirmed. The remaining open items (OI-01, OI-06 to OI-11) are UX document updates due before the functional design.
