from app.models.schemas import InvestigationRequest
from app.services.investigation import InvestigationService

def test_agent_trace_is_bounded_and_visible():
    result = InvestigationService().investigate(
        InvestigationRequest(authorization_case_id="AUTH-1001")
    )
    assert [item.tool for item in result.tool_trace] == [
        "authorization.get_case",
        "payer.get_requirements",
        "clinical.get_records",
    ]

def test_retrieval_is_grounded_and_ranked():
    result = InvestigationService().investigate(
        InvestigationRequest(authorization_case_id="AUTH-1001")
    )
    assert result.evidence
    assert all(item.retrieval_score >= 0.70 for item in result.evidence)
    assert all(item.source_system and item.source_record_id for item in result.evidence)

def test_summaries_only_exist_for_found_evidence():
    result = InvestigationService().investigate(
        InvestigationRequest(authorization_case_id="AUTH-1001")
    )
    by_id = {item.requirement_id: item for item in result.requirements}

    assert by_id["REQ-PT"].grounded_summary
    assert "source=synthetic-ehr:NOTE-101" in by_id["REQ-PT"].grounded_summary
    assert by_id["REQ-EXAM"].grounded_summary
    assert by_id["REQ-MED"].status == "evidence_not_found"
    assert by_id["REQ-MED"].grounded_summary is None

def test_human_review_remains_required():
    result = InvestigationService().investigate(
        InvestigationRequest(authorization_case_id="AUTH-1001")
    )
    assert result.human_review_required is True
