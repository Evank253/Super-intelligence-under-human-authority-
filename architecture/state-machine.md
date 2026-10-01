# State Machine

## E0–E5

The E0–E5 ladder is retained as a prior human-ratified canonical model. Exact ratified definitions must be recovered from the authoritative source artifact before implementation code treats them as executable semantics.

**Recovery status: OPEN — source artifact required.**

The implementation must not invent definitions merely to make the state machine complete.

## Transition principle

`requested_state ≠ authorized_state`

The requested destination is untrusted input. Every upward transition requires explicit prerequisites.

## NOT_MEASURED

`NOT_MEASURED` means the required evidence or measurement has not been established. It is not equivalent to true, false, failed, or passed.
