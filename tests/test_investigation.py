import pytest
from app.models.schemas import InvestigationRequest
from app.services.investigation import InvestigationService

def test_investigation_surfaces_evidence_and_missing_requirement():
    result = InvestigationService().investigate(InvestigationRequest(authorization_case_id="AUTH-1001"))
    statuses = {r.requirement_id: r.status for r in result.requirements}
    assert statuses["REQ-PT"] == "evidence_found"
    assert statuses["REQ-EXAM"] == "evidence_found"
    assert statuses["REQ-MED"] == "evidence_not_found"
    assert result.human_review_required is True
    assert all(e.provenance_valid and e.source_record_id for e in result.evidence)

def test_unknown_case_fails():
    with pytest.raises(KeyError):
        InvestigationService().investigate(InvestigationRequest(authorization_case_id="UNKNOWN"))
