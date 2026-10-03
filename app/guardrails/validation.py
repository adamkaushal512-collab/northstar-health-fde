from app.models.schemas import EvidenceItem

def validate_provenance(evidence: list[EvidenceItem]) -> list[str]:
    warnings = []
    for item in evidence:
        if not item.source_system or not item.source_record_id:
            item.provenance_valid = False
            warnings.append(f"Evidence {item.evidence_id} is missing provenance.")
    return warnings
