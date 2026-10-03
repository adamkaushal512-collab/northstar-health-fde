from uuid import uuid4
from app.adapters.synthetic import SyntheticAuthorizationAdapter, SyntheticClinicalAdapter, SyntheticPayerAdapter
from app.guardrails.validation import validate_provenance
from app.models.schemas import InvestigationRequest, InvestigationResult, RequirementResult
from app.retrieval.evidence import retrieve_evidence

class InvestigationService:
    def __init__(self):
        self.authorization = SyntheticAuthorizationAdapter()
        self.payer = SyntheticPayerAdapter()
        self.clinical = SyntheticClinicalAdapter()

    def investigate(self, request: InvestigationRequest) -> InvestigationResult:
        case = self.authorization.get_case(request.authorization_case_id)
        requirements = self.payer.get_requirements(case["payer"], case["procedure"])
        records, clinical_status = self.clinical.get_records(case["patient_reference"])
        evidence = retrieve_evidence(requirements, records) if clinical_status == "available" else []
        warnings = validate_provenance(evidence)
        unavailable_sources = []
        if clinical_status != "available":
            unavailable_sources.append("clinical_records")
            warnings.append("Clinical source unavailable. Evidence absence cannot be determined.")

        results = []
        for requirement in requirements:
            matching = [e for e in evidence if e.requirement_id == requirement["requirement_id"]]
            status = ("source_unavailable" if clinical_status != "available"
                      else "evidence_found" if matching else "evidence_not_found")
            results.append(RequirementResult(
                requirement_id=requirement["requirement_id"],
                description=requirement["description"],
                status=status,
                evidence_ids=[e.evidence_id for e in matching],
            ))

        return InvestigationResult(
            authorization_case_id=case["authorization_case_id"],
            patient_reference=case["patient_reference"],
            procedure=case["procedure"],
            payer=case["payer"],
            requirements=results,
            evidence=evidence,
            unavailable_sources=unavailable_sources,
            warnings=warnings,
            human_review_required=True,
            audit_reference=f"INV-{uuid4().hex[:12]}",
        )
