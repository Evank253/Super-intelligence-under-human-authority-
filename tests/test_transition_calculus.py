from datetime import datetime, timedelta
from transition_calculus import *

NOW=datetime(2026,10,3,20)
A=frozenset({"A"}); AB=frozenset({"A","B"})

def t(**kw):
    d=dict(transition_id="t1",transition_class=TransitionClass.AUTHORITY,
    source_state="GOVERNED",destination_state="AUTHORIZED",subject="X",scope=A,
    timestamp=NOW,preconditions=frozenset({"QUALIFIED","GOVERNED"}),
    evidence_refs=("e1",),verification_refs=("v1",),qualification_refs=("q1",),
    governance_refs=("g1",),authority_ref=None,provenance=("g1",),
    decision_actor="system",decision_origin=DecisionOrigin.SYSTEM,
    temporal_validity=(NOW-timedelta(hours=1),NOW+timedelta(hours=1)),
    result=ValidationStatus.VALID)
    d.update(kw); return TransitionRecord(**d)

def ar(scope=A):
    return S4AuthorizationRecord("s4","AUTHORIZE","X",scope,NOW,NOW-timedelta(hours=1),NOW+timedelta(hours=1),"human")

def verify(r): return r.external_attestation=="human"

def test_self_authorization_rejected():
    x=t(); v=TransitionValidator().validate(x)
    assert v.status==ValidationStatus.AUTHORIZATION_REQUIRED
    assert effective_authority(x,v)=="NONE"

def test_authorized_label_is_not_authority():
    x=t(); v=TransitionValidator().validate(x)
    assert x.destination_state=="AUTHORIZED" and effective_authority(x,v)=="NONE"

def test_in_process_attestation_is_not_s4():
    x=t(authority_ref="s4",provenance=("g1","s4"),decision_actor="human",decision_origin=DecisionOrigin.S4)
    v=TransitionValidator({"s4":ar()},external_authority_verifier=verify).validate(x,now=NOW)
    assert v.status==ValidationStatus.NOT_MEASURED and effective_authority(x,v)=="NONE"

def test_scope_expansion_rejected():
    old=t(authority_ref="s4",provenance=("g1","s4"),decision_actor="human",decision_origin=DecisionOrigin.S4,scope=A)
    new=t(transition_id="t2",source_state="AUTHORIZED",scope=AB,authority_ref="s4",provenance=("t1","s4"),decision_origin=DecisionOrigin.S4)
    v=TransitionValidator({"s4":ar()},external_authority_verifier=verify).validate(new,now=NOW,prior_transition=old)
    assert v.status==ValidationStatus.INVALID and effective_authority(new,v)=="NONE"

def test_stale_authorization_rejected():
    old=NOW-timedelta(days=2)
    rec=S4AuthorizationRecord("old","AUTHORIZE","X",A,old,old,old+timedelta(hours=1),"human")
    x=t(authority_ref="old",provenance=("g1","old"),decision_actor="human",decision_origin=DecisionOrigin.S4,timestamp=old,temporal_validity=(old,old+timedelta(hours=1)))
    v=TransitionValidator({"old":rec},external_authority_verifier=verify).validate(x,now=NOW)
    assert v.status==ValidationStatus.INVALID

def test_not_measured_cannot_be_qualified():
    x=t(transition_class=TransitionClass.QUALIFICATION,source_state="NOT_MEASURED",destination_state="QUALIFIED",authority_ref=None,provenance=("e1",),decision_origin=DecisionOrigin.SYSTEM)
    assert TransitionValidator().validate(x).status==ValidationStatus.INVALID

def test_unresolved_and_evidence_cannot_become_authorized():
    for source in ("UNRESOLVED","EVIDENCE","QUALIFIED","NOT_MEASURED"):
        x=t(source_state=source,authority_ref="s4",provenance=("g1","s4"),decision_origin=DecisionOrigin.S4)
        v=TransitionValidator({"s4":ar()},external_authority_verifier=verify).validate(x,now=NOW)
        assert v.status==ValidationStatus.INVALID and effective_authority(x,v)=="NONE"

def test_caller_result_is_ignored():
    x=t(authority_ref="s4",provenance=("g1","s4"),decision_origin=DecisionOrigin.S4,result=ValidationStatus.VALID)
    v=TransitionValidator({"s4":ar()},external_authority_verifier=lambda r: True).validate(x,now=NOW)
    assert v.status==ValidationStatus.NOT_MEASURED and effective_authority(x,v)=="NONE"
