from __future__ import annotations
from dataclasses import dataclass, field

from app.adapters.synthetic import (
    SyntheticAuthorizationAdapter,
    SyntheticClinicalAdapter,
    SyntheticPayerAdapter,
)
from app.models.schemas import ToolTrace

@dataclass
class AgentContext:
    case: dict
    requirements: list[dict]
    records: list[dict]
    clinical_status: str
    tool_trace: list[ToolTrace] = field(default_factory=list)

class InvestigationAgent:
    """Bounded workflow agent with an explicit, allow-listed tool sequence."""

    def __init__(self) -> None:
        self.authorization = SyntheticAuthorizationAdapter()
        self.payer = SyntheticPayerAdapter()
        self.clinical = SyntheticClinicalAdapter()

    def gather(self, case_id: str) -> AgentContext:
        trace: list[ToolTrace] = []

        case = self.authorization.get_case(case_id)
        trace.append(ToolTrace(
            tool="authorization.get_case",
            status="success",
            detail="Authorization case loaded.",
        ))

        requirements = self.payer.get_requirements(case["payer"], case["procedure"])
        trace.append(ToolTrace(
            tool="payer.get_requirements",
            status="success",
            detail=f"{len(requirements)} payer requirements loaded.",
        ))

        records, clinical_status = self.clinical.get_records(case["patient_reference"])
        trace.append(ToolTrace(
            tool="clinical.get_records",
            status="success" if clinical_status == "available" else "unavailable",
            detail=(
                f"{len(records)} clinical records loaded."
                if clinical_status == "available"
                else "Clinical source unavailable."
            ),
        ))

        return AgentContext(
            case=case,
            requirements=requirements,
            records=records,
            clinical_status=clinical_status,
            tool_trace=trace,
        )
