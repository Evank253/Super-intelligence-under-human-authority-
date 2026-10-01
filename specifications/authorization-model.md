# Authorization Model

Authorization has an owner distinct from intelligence and qualification.

Inputs include actor identity, requested action, scope, applicable policy, evidence state, human authorization where required, and safety constraints.

The model or router may request an authorization decision but cannot supply the authoritative decision as an untrusted field.

If required authorization evidence is missing, deny or hold for human review according to policy. Never infer authorization from confidence or capability.
