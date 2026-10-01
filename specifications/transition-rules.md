# Transition Rules

A requested destination state is untrusted input.

Every upward evidence transition must have explicit prerequisites. If E2 → E3 requires verification, an API request directly setting E3 without qualifying verification must be rejected.

Authorization is independently evaluated. A model field such as `authorize: true` is a request, not an authoritative decision.

Internal JSON, database rows, messages, or API payloads are untrusted with respect to security-critical state.

If an artifact changes while retaining a prior identity/hash, provenance integrity must fail.
