from app.guardrails.fallback import decide_fallback,Disposition
from app.guardrails.escalation import route_escalation
from app.runtime.safe_investigation import SafeInvestigationRuntime
def test_source_outage_fails_safe():
 d=decide_fallback(unavailable_sources=["clinical_records"]); assert d.disposition==Disposition.MANUAL_WORKFLOW and not d.automation_allowed
def test_missing_evidence_human_review():
 assert decide_fallback(missing_requirements=["REQ-MED"]).disposition==Disposition.HUMAN_REVIEW
def test_provenance_routes_safety():
 assert route_escalation(["provenance_failure"]).queue=="prior-auth-safety-review"
def test_partial_case_handoff():
 r=SafeInvestigationRuntime().investigate("AUTH-1001"); assert r.handoff and "insufficient_evidence" in r.handoff.reason_codes
def test_complete_case_keeps_human_boundary():
 r=SafeInvestigationRuntime().investigate("AUTH-1002"); assert r.fallback.disposition==Disposition.CONTINUE_REVIEW and r.investigation.human_review_required and not r.fallback.automation_allowed
