from app.models.schemas import EvidenceItem

def retrieve_evidence(requirements: list[dict], records: list[dict]) -> list[EvidenceItem]:
    evidence = []
    for requirement in requirements:
        for record in records:
            if record["evidence_type"] == requirement["evidence_type"]:
                evidence.append(EvidenceItem(
                    evidence_id=f'{requirement["requirement_id"]}:{record["record_id"]}',
                    requirement_id=requirement["requirement_id"],
                    evidence_type=record["evidence_type"],
                    finding=record["summary"],
                    source_system=record["source_system"],
                    source_record_id=record["record_id"],
                    service_date=record["service_date"],
                ))
    return evidence
