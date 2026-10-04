from dataclasses import dataclass
@dataclass(frozen=True)
class Escalation:
 required:bool; queue:str|None; reason_codes:list[str]
def route_escalation(reasons):
 if not reasons:return Escalation(False,None,[])
 if "system_error" in reasons or "source_unavailable" in reasons:return Escalation(True,"prior-auth-manual-operations",reasons)
 if "provenance_failure" in reasons:return Escalation(True,"prior-auth-safety-review",reasons)
 return Escalation(True,"prior-auth-specialist-review",reasons)
