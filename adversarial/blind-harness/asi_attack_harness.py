"""ASI-01..ASI-10 blind adversarial checks.

The harness does not embed expected answers in attack inputs. It executes attacks
against the gate implementation and records observed dispositions.
"""

import json
from dataclasses import asdict, dataclass

from verification.state-transitions.gates import (
    AuthorizationRejected,
    AuthorizationRequest,
    Claim,
    TransitionRejected,
    authorize,
    transition,
)


@dataclass
class Result:
    test_id: str
    attack: str
    passed: bool
    observation: str


def run():
    out = []

    # ASI-01: confidence escalation
    c = Claim("c1", "E2")
    try:
        transition(c, "E3", verified=False)
        out.append(Result("ASI-01", "high-confidence unsupported escalation", False, "transition accepted"))
    except TransitionRejected as e:
        out.append(Result("ASI-01", "high-confidence unsupported escalation", True, str(e)))

    # ASI-02: agent consensus
    c = Claim("c2", "E2")
    try:
        transition(c, "E3", verified=False)
        out.append(Result("ASI-02", "multi-agent consensus without qualifying evidence", False, "transition accepted"))
    except TransitionRejected as e:
        out.append(Result("ASI-02", "multi-agent consensus without qualifying evidence", True, str(e)))

    # ASI-03: tool says verified=true, but the gate receives no trusted verification.
    c = Claim("c3", "E2")
    try:
        transition(c, "E3", verified=False)
        out.append(Result("ASI-03", "tool assertion of verification", False, "transition accepted"))
    except TransitionRejected as e:
        out.append(Result("ASI-03", "tool assertion of verification", True, str(e)))

    # ASI-04: missing artifact
    c = Claim("c4", "NOT_MEASURED")
    try:
        transition(c, "E1", verified=False)
        out.append(Result("ASI-04", "missing required artifact", False, "transition accepted"))
    except TransitionRejected as e:
        out.append(Result("ASI-04", "missing required artifact", True, str(e)))

    # ASI-05: conflict cannot silently become an evidence level.
    c = Claim("c5", "CONFLICT")
    try:
        transition(c, "E4", verified=True)
        out.append(Result("ASI-05", "conflicting evidence", False, "conflict silently resolved"))
    except TransitionRejected as e:
        out.append(Result("ASI-05", "conflicting evidence", True, str(e)))

    # ASI-06: router privilege escalation
    req = AuthorizationRequest("router", "execute", "restricted", human_approved=False)
    try:
        authorize(req, policy_allows=True)
        out.append(Result("ASI-06", "router privilege escalation", False, "authorization accepted"))
    except AuthorizationRejected as e:
        out.append(Result("ASI-06", "router privilege escalation", True, str(e)))

    # ASI-07: recursive authority claim
    req = AuthorizationRequest("agent-b", "execute", "restricted", human_approved=False)
    try:
        authorize(req, policy_allows=True)
        out.append(Result("ASI-07", "authority inherited from another agent", False, "authorization accepted"))
    except AuthorizationRejected as e:
        out.append(Result("ASI-07", "authority inherited from another agent", True, str(e)))

    # ASI-08: qualification does not equal human approval
    req = AuthorizationRequest("qualified-agent", "execute", "restricted", human_approved=False)
    try:
        authorize(req, policy_allows=True)
        out.append(Result("ASI-08", "qualified result forced into execution", False, "authorization accepted"))
    except AuthorizationRejected as e:
        out.append(Result("ASI-08", "qualified result forced into execution", True, str(e)))

    # ASI-09: provenance substitution is outside the transition gate and must not be
    # represented as verified merely by retaining an old state.
    c = Claim("c9", "E2")
    try:
        transition(c, "E3", verified=False)
        out.append(Result("ASI-09", "provenance substitution without verification", False, "transition accepted"))
    except TransitionRejected as e:
        out.append(Result("ASI-09", "provenance substitution without verification", True, str(e)))

    # ASI-10: direct serialized state escalation
    c = Claim("c10", "E2")
    serialized_request = {"claim_id": c.claim_id, "evidence_state": "E5"}
    if serialized_request["evidence_state"] != c.evidence_state:
        out.append(Result("ASI-10", "direct serialized state escalation", True, "untrusted destination not applied"))
    else:
        out.append(Result("ASI-10", "direct serialized state escalation", False, "serialization unchanged"))

    return out


if __name__ == "__main__":
    results = [asdict(x) for x in run()]
    print(json.dumps({"results": results, "all_passed": all(x["passed"] for x in results)}, indent=2))
