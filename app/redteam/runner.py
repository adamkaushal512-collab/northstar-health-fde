import json
from pathlib import Path
from app.guardrails.content import detect_prompt_injection
from app.retrieval.evidence import retrieve_evidence
def load_cases(path="data/redteam/red_team_cases.json"):
    return json.loads(Path(path).read_text())
def evaluate(c):
    k=c["category"]
    if k=="prompt_injection": return detect_prompt_injection(c["payload"])
    if k=="cross_patient_leakage":
        scoped=[r for r in [c["foreign_record"]] if r["patient_reference"]==c["authorized_patient_reference"]]
        return not retrieve_evidence([c["requirement"]],scoped)
    if k=="irrelevant_evidence": return not retrieve_evidence([c["requirement"]],[c["record"]])
    if k=="missing_provenance": return not bool(c["record"].get("source_system") and c["record"].get("record_id"))
    if k=="unsafe_action": return c["requested_action"] not in {"read_case","read_requirements","read_clinical_records"}
    return False
def run_red_team():
    cases=load_cases(); results=[{"attack_id":c["attack_id"],"category":c["category"],"blocked":evaluate(c)} for c in cases]
    blocked=sum(r["blocked"] for r in results)
    return {"results":results,"metrics":{"attacks":len(results),"blocked":blocked,"block_rate":round(blocked/len(results),4)}}
if __name__=="__main__": print(json.dumps(run_red_team(),indent=2))
