from dataclasses import dataclass
from enum import Enum
class Disposition(str,Enum):
 CONTINUE_REVIEW="continue_review"; HUMAN_REVIEW="human_review"; MANUAL_WORKFLOW="manual_workflow"
@dataclass(frozen=True)
class FallbackDecision:
 disposition:Disposition; reasons:list[str]; message:str; automation_allowed:bool=False
def decide_fallback(unavailable_sources=None,missing_requirements=None,provenance_failure=False,system_error=False):
 reasons=[]
 if unavailable_sources: reasons.append("source_unavailable")
 if missing_requirements: reasons.append("insufficient_evidence")
 if provenance_failure: reasons.append("provenance_failure")
 if system_error: reasons.append("system_error")
 if system_error or unavailable_sources: return FallbackDecision(Disposition.MANUAL_WORKFLOW,reasons,"Use established manual workflow.")
 if reasons: return FallbackDecision(Disposition.HUMAN_REVIEW,reasons,"Specialist review required.")
 return FallbackDecision(Disposition.CONTINUE_REVIEW,[],"Evidence assembly complete; human decision remains required.")
