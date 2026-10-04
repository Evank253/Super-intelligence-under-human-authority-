"""ASI qualification harness — evidence-bounded core."""
from __future__ import annotations
from dataclasses import dataclass, asdict
from enum import Enum
import hashlib, json, time
from typing import Any, Callable, Iterable, Protocol

class EvidenceState(str, Enum):
    NOT_MEASURED="NOT_MEASURED"; OBSERVED="OBSERVED"; VERIFIED="VERIFIED"; QUALIFIED="QUALIFIED"

class AuthorityDecision(str, Enum):
    HUMAN_REVIEW_REQUIRED="HUMAN_REVIEW_REQUIRED"; AUTHORIZED="AUTHORIZED"; DENIED="DENIED"

@dataclass(frozen=True)
class Task:
    task_id:str; domain:str; prompt:str; expected:Any|None=None; hidden:bool=True; difficulty:str="unknown"

@dataclass(frozen=True)
class Submission:
    system_id:str; task_id:str; answer:Any; latency_ms:float; evidence_refs:tuple[str,...]=()

@dataclass(frozen=True)
class Score:
    task_id:str; system_id:str; correct:bool; score:float; evidence_state:EvidenceState; reason:str

@dataclass(frozen=True)
class AuthorityRequest:
    actor:str; action:str; evidence_state:EvidenceState; human_ratified:bool=False

class SystemAdapter(Protocol):
    system_id:str
    def solve(self, task:Task)->Submission: ...

def canonical_json(value:Any)->str:
    return json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False)

def sha256_record(value:Any)->str:
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()

def score_exact(task:Task, submission:Submission)->Score:
    if task.expected is None:
        return Score(task.task_id,submission.system_id,False,0.0,EvidenceState.NOT_MEASURED,"No expected answer; external adjudication required.")
    correct=submission.answer==task.expected
    return Score(task.task_id,submission.system_id,correct,1.0 if correct else 0.0,EvidenceState.OBSERVED,"Exact-match adjudication.")

def run_tasks(adapter:SystemAdapter,tasks:Iterable[Task],scorer:Callable[[Task,Submission],Score]=score_exact)->list[Score]:
    results=[]
    for task in tasks:
        started=time.perf_counter()
        submission=adapter.solve(task)
        elapsed=(time.perf_counter()-started)*1000
        submission=Submission(submission.system_id,submission.task_id,submission.answer,elapsed,submission.evidence_refs)
        if submission.system_id!=adapter.system_id: raise ValueError("adapter system_id mismatch")
        if submission.task_id!=task.task_id: raise ValueError("submission task_id mismatch")
        results.append(scorer(task,submission))
    return results

def aggregate(scores:Iterable[Score])->dict[str,Any]:
    rows=list(scores)
    if not rows:return {"n":0,"mean_score":None,"correct":0}
    return {"n":len(rows),"mean_score":sum(r.score for r in rows)/len(rows),"correct":sum(r.correct for r in rows),"evidence_states":{s.value:sum(r.evidence_state==s for r in rows) for s in EvidenceState}}

def request_authority(req:AuthorityRequest)->AuthorityDecision:
    if req.human_ratified and req.evidence_state==EvidenceState.QUALIFIED:return AuthorityDecision.AUTHORIZED
    if req.evidence_state in {EvidenceState.NOT_MEASURED,EvidenceState.OBSERVED,EvidenceState.VERIFIED}:return AuthorityDecision.HUMAN_REVIEW_REQUIRED
    return AuthorityDecision.DENIED

def evidence_record(task:Task,submission:Submission,score:Score)->dict[str,Any]:
    record={"task":asdict(task),"submission":asdict(submission),"score":asdict(score)}
    record["record_sha256"]=sha256_record(record)
    return record
