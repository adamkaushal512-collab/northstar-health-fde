from app.models.schemas import EvidenceItem, RequirementResult

def validate_provenance(evidence: list[EvidenceItem]) -> list[str]:
    warnings: list[str] = []
    for item in evidence:
        if not item.source_system or not item.source_record_id:
            item.provenance_valid = False
            warnings.append(f"Evidence {item.evidence_id} is missing provenance.")
    return warnings

def validate_grounding(
    requirements: list[RequirementResult],
    evidence: list[EvidenceItem],
) -> list[str]:
    warnings: list[str] = []
    valid_ids = {
        item.evidence_id for item in evidence
        if item.provenance_valid
    }

    for requirement in requirements:
        unknown = set(requirement.evidence_ids) - valid_ids
        if unknown:
            warnings.append(
                f"Requirement {requirement.requirement_id} references ungrounded evidence."
            )
            requirement.grounded_summary = None

        if requirement.grounded_summary and not requirement.evidence_ids:
            warnings.append(
                f"Requirement {requirement.requirement_id} has a summary without evidence."
            )
            requirement.grounded_summary = None

    return warnings
