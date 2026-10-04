from dataclasses import dataclass
from app.models.schemas import InvestigationRequest
from app.services.investigation import InvestigationService
from app.guardrails.fallback import decide_fallback
from app.guardrails.escalation import route_escalation
from app.guardrails.handoff import build_handoff
@dataclass
class SafeInvestigationResult:
 investigation:object; fallback:object; escalation:object; handoff:object|None
class SafeInvestigationRuntime:
 def __init__(self):self.service=InvestigationService()
 def investigate(self,case_id):
  result=self.service.investigate(InvestigationRequest(authorization_case_id=case_id))
  missing=[r.requirement_id for r in result.requirements if r.status!="evidence_found"]
  fallback=decide_fallback(unavailable_sources=result.unavailable_sources,missing_requirements=missing,provenance_failure=any(not e.provenance_valid for e in result.evidence))
  escalation=route_escalation(fallback.reasons)
  handoff=build_handoff(result,escalation.queue,fallback.reasons) if escalation.required else None
  return SafeInvestigationResult(result,fallback,escalation,handoff)
