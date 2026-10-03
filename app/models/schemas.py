from typing import Literal
from pydantic import BaseModel, Field

class InvestigationRequest(BaseModel):
    authorization_case_id: str = Field(min_length=1)

class EvidenceItem(BaseModel):
    evidence_id: str
    requirement_id: str
    evidence_type: str
    finding: str
    source_system: str
    source_record_id: str
    service_date: str
    provenance_valid: bool = True
    retrieval_score: float = 0.0
    retrieval_reasons: list[str] = []

class RequirementResult(BaseModel):
    requirement_id: str
    description: str
    status: Literal["evidence_found", "evidence_not_found", "source_unavailable"]
    evidence_ids: list[str] = []
    grounded_summary: str | None = None

class ToolTrace(BaseModel):
    tool: str
    status: Literal["success", "unavailable", "error"]
    detail: str

class InvestigationResult(BaseModel):
    authorization_case_id: str
    patient_reference: str
    procedure: str
    payer: str
    requirements: list[RequirementResult]
    evidence: list[EvidenceItem]
    unavailable_sources: list[str]
    warnings: list[str]
    tool_trace: list[ToolTrace] = []
    human_review_required: bool = True
    audit_reference: str
