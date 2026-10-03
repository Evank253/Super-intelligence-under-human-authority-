#!/usr/bin/env python3
import json, sys, tempfile, time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"runtime"))
from sos_runtime.runtime import SoSRuntime

def case(name,fn):
    t=time.perf_counter()
    try:
        value=fn()
        return {"name":name,"passed":bool(value),"elapsed_ms":round((time.perf_counter()-t)*1000,3)}
    except Exception as e:
        return {"name":name,"passed":False,"error":f"{type(e).__name__}: {e}",
                "elapsed_ms":round((time.perf_counter()-t)*1000,3)}

def expect_denied(fn):
    try: fn()
    except PermissionError: return True
    return False

def main():
    rt=SoSRuntime(tempfile.mkdtemp(prefix="sos-bench-"))
    rows=[case("health",lambda:rt.health()["runtime"]=="ONLINE")]
    a=rt.index.register("capability","benchmark-capability","KCN",
        "Evank253/KCN-SUPER-COGNITIVE-HUMAN-GOVERNED-INTELLIGENCE-ECOSYSTEM-",
        "BENCHMARK_FIXTURE",None,"fixture",capabilities=["reasoning","routing"])
    rows.append(case("index-provenance",lambda:bool(a.source_repository and a.source_commit)))
    e=rt.evidence.observe(a.artifact_id,"runtime-observation","SoS-BENCHMARK-001")
    rows.append(case("evidence-witness",lambda:e.subject_id==a.artifact_id))
    rows.append(case("unauthorized-fails-closed",lambda:expect_denied(lambda:rt.execute("run","subject-1"))))
    auth=rt.authorization.issue("run","subject-1","EXTERNAL_HUMAN_AUTHORITY",
        "CONSTITUTIONAL_PROCESS",["subject-1"],human_ratification="BENCHMARK_FIXTURE")
    rows.append(case("authorized-execution",lambda:rt.execute("run","subject-1",auth.authorization_id)["outcome"]=="EXECUTED"))
    rt.authorization.revoke(auth.authorization_id,"benchmark revocation")
    rows.append(case("revocation-fails-closed",lambda:expect_denied(lambda:rt.execute("run","subject-1",auth.authorization_id))))
    child=rt.index.reindex(a.artifact_id,{"name":"benchmark-capability-v2","capabilities":["reasoning","routing","reconstruction"]})
    rows.append(case("reindex-preserves-lineage",lambda:child.parent_artifact_id==a.artifact_id and len(rt.index.lineage(child.artifact_id))==2))
    summary={"suite":"SoS-BENCHMARK-001","cases":len(rows),
             "passed":sum(r["passed"] for r in rows),"failed":sum(not r["passed"] for r in rows),
             "results":rows}
    print(json.dumps(summary,indent=2))
    raise SystemExit(0 if summary["failed"]==0 else 1)

if __name__=="__main__": main()
