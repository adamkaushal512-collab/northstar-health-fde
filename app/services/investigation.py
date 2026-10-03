from uuid import uuid4

from app.agent.orchestrator import InvestigationAgent
from app.ai.grounding import GroundedEvidenceSynthesizer
from app.guardrails.validation import validate_grounding, validate_provenance
from app.models.schemas import InvestigationRequest, InvestigationResult, RequirementResult
from app.retrieval.evidence import retrieve_evidence

class InvestigationService:
    def __init__(self) -> None:
        self.agent = InvestigationAgent()
        self.synthesizer = GroundedEvidenceSynthesizer()

    def investigate(self, request: InvestigationRequest) -> InvestigationResult:
        context = self.agent.gather(request.authorization_case_id)
        case = context.case

        evidence = (
            retrieve_evidence(context.requirements, context.records)
            if context.clinical_status == "available"
            else []
        )
        warnings = validate_provenance(evidence)
        unavailable_sources: list[str] = []

        if context.clinical_status != "available":
            unavailable_sources.append("clinical_records")
            warnings.append(
                "Clinical source unavailable. Evidence absence cannot be determined."
            )

        requirement_results: list[RequirementResult] = []
        for requirement in context.requirements:
            matching = [
                item for item in evidence
                if item.requirement_id == requirement["requirement_id"]
                and item.provenance_valid
            ]

            if context.clinical_status != "available":
                status = "source_unavailable"
            elif matching:
                status = "evidence_found"
            else:
                status = "evidence_not_found"

            requirement_results.append(RequirementResult(
                requirement_id=requirement["requirement_id"],
                description=requirement["description"],
                status=status,
                evidence_ids=[item.evidence_id for item in matching],
                grounded_summary=self.synthesizer.summarize(requirement, matching),
            ))

        warnings.extend(validate_grounding(requirement_results, evidence))

        return InvestigationResult(
            authorization_case_id=case["authorization_case_id"],
            patient_reference=case["patient_reference"],
            procedure=case["procedure"],
            payer=case["payer"],
            requirements=requirement_results,
            evidence=evidence,
            unavailable_sources=unavailable_sources,
            warnings=warnings,
            tool_trace=context.tool_trace,
            human_review_required=True,
            audit_reference=f"INV-{uuid4().hex[:12]}",
        )
