# Authority Boundaries

1. Models cannot authorize themselves.
2. Agents cannot inherit authority from another agent.
3. Routers can request actions but cannot grant authorization.
4. Qualification can establish an evidentiary condition but cannot substitute for human authorization.
5. Successful execution cannot retroactively create authority.
6. Confidence cannot create evidence.
7. Consensus cannot create qualifying evidence without the required evidence class.
8. Direct state mutation bypassing transition rules must be rejected.

Conceptual interfaces:

`authorize(action, actor, scope, evidence_state)`

`allowed_transition(claim, old_state, new_state, evidence)`
