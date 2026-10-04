# Transition Validity Schema

**Status:** FORMALIZATION SCHEMA — IMPLEMENTATION REQUIRED

## Required TransitionRecord fields

| Field | Purpose |
|---|---|
| transition_id | Unique transition identity |
| transition_class | Typed transition family |
| source_state | State before transition |
| destination_state | State after transition |
| subject | Object/capability/authorization affected |
| scope | Authorized/evaluated scope |
| timestamp | Event time |
| preconditions | Required prerequisites |
| evidence_refs | Supporting evidence |
| verification_refs | Verification records |
| qualification_refs | Qualification records |
| governance_refs | Governance records |
| authority_ref | Authority source/record |
| provenance | Chain connecting source to transition |
| decision_actor | Actor producing the transition |
| decision_origin | Origin class, including S1/S2/S3/S4/external human |
| temporal_validity | Effective interval/status |
| result | ACCEPTED/REJECTED/etc. |
| failure_reason | Reason for rejection or invalidity |

## Validation requirements

A validator shall determine validity from the transition record and its referenced records rather than trusting destination_state.

At minimum it shall establish:

1. transition class is recognized;
2. source/destination pair is permitted for that class;
3. required prerequisites are present;
4. referenced evidence/verification/qualification records are valid for the transition;
5. provenance is intact;
6. scope is applicable;
7. temporal validity is satisfied;
8. required authority exists;
9. authority origin is appropriate;
10. anti-promotion constraints are satisfied.

## S4-specific validation

For destination AUTHORIZED, the validator must establish a valid S4 authorization record with external human origin, valid authority provenance, applicable subject, applicable scope, valid time, and unbroken transition provenance.

If these conditions are absent: NO_S4_AUTHORIZATION.

## Label/legitimacy rule

`destination_state = AUTHORIZED` MUST NOT by itself imply effective authority.

The effective state is derived from valid transition provenance.

## Fail-closed rule

If required transition evidence or authority cannot be established, the validator must not infer legitimacy from absence of an error, confidence, consensus, or destination label.

Use explicit states such as VALID, INVALID, NOT_MEASURED, UNRESOLVED, AUTHORIZATION_REQUIRED.

This schema is a formalization target and has not yet been runtime-verified.
