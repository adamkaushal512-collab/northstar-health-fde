from __future__ import annotations
import re
from app.guardrails.content import safe_record
from app.models.schemas import EvidenceItem
_TOKEN_RE=re.compile(r"[a-z0-9]+")
def _tokens(text): return set(_TOKEN_RE.findall(text.lower()))
def _score(requirement,record):
    score=0.0; reasons=[]
    if record["evidence_type"]==requirement["evidence_type"]:
        score+=0.75; reasons.append("evidence_type_match")
    overlap=_tokens(requirement["description"])&_tokens(record["summary"])
    if overlap:
        score+=min(len(overlap)/max(len(_tokens(requirement["description"])),1),0.25); reasons.append("lexical_overlap")
    return round(min(score,1.0),3),reasons
def retrieve_evidence(requirements,records,minimum_score=0.70):
    out=[]
    for req in requirements:
        candidates=[]
        for rec in records:
            allowed,_=safe_record(rec)
            if not allowed: continue
            score,reasons=_score(req,rec)
            if score<minimum_score: continue
            candidates.append(EvidenceItem(evidence_id=f'{req["requirement_id"]}:{rec["record_id"]}',requirement_id=req["requirement_id"],evidence_type=rec["evidence_type"],finding=rec["summary"],source_system=rec["source_system"],source_record_id=rec["record_id"],service_date=rec["service_date"],provenance_valid=True,retrieval_score=score,retrieval_reasons=reasons))
        candidates.sort(key=lambda x:x.retrieval_score,reverse=True); out.extend(candidates)
    return out
