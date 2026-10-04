"""Harness-only smoke test. Passing this is not evidence of AGI/ASI."""
from evaluation.asi_qualification import *
def main():
    task=Task("SMOKE-001","logic","What is 2 + 2?",4,False)
    submission=Submission("smoke-adapter",task.task_id,4,1.0)
    score=score_exact(task,submission)
    assert score.correct and score.evidence_state==EvidenceState.OBSERVED
    assert aggregate([score])["mean_score"]==1.0
    assert request_authority(AuthorityRequest("smoke","deploy",EvidenceState.OBSERVED,False))==AuthorityDecision.HUMAN_REVIEW_REQUIRED
    assert request_authority(AuthorityRequest("human","deploy",EvidenceState.QUALIFIED,True))==AuthorityDecision.AUTHORIZED
    assert len(evidence_record(task,submission,score)["record_sha256"])==64
    print("EA-G2 harness smoke: PASS")
    print("Harness validation only; intelligence status remains NOT ESTABLISHED.")
if __name__=="__main__": main()
