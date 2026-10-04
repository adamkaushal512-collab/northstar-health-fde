from dataclasses import dataclass
@dataclass(frozen=True)
class HumanHandoff:
 case_id:str; queue:str; reason_codes:list[str]; evidence_ids:list[str]; unavailable_sources:list[str]; audit_reference:str
def build_handoff(result,queue,reason_codes):
 return HumanHandoff(result.authorization_case_id,queue,reason_codes,[e.evidence_id for e in result.evidence if e.provenance_valid],list(result.unavailable_sources),result.audit_reference)
