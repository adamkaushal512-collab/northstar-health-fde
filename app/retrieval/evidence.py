from __future__ import annotations
import re
from app.models.schemas import EvidenceItem

_TOKEN_RE = re.compile(r"[a-z0-9]+")

def _tokens(text: str) -> set[str]:
    return set(_TOKEN_RE.findall(text.lower()))

def _score(requirement: dict, record: dict) -> tuple[float, list[str]]:
    score = 0.0
    reasons: list[str] = []

    if record["evidence_type"] == requirement["evidence_type"]:
        score += 0.75
        reasons.append("evidence_type_match")

    requirement_terms = _tokens(requirement["description"])
    record_terms = _tokens(record["summary"])
    overlap = requirement_terms & record_terms
    if overlap:
        lexical = min(len(overlap) / max(len(requirement_terms), 1), 0.25)
        score += lexical
        reasons.append("lexical_overlap")

    return round(min(score, 1.0), 3), reasons

def retrieve_evidence(
    requirements: list[dict],
    records: list[dict],
    minimum_score: float = 0.70,
) -> list[EvidenceItem]:
    evidence: list[EvidenceItem] = []

    for requirement in requirements:
        candidates: list[EvidenceItem] = []
        for record in records:
            score, reasons = _score(requirement, record)
            if score < minimum_score:
                continue
            candidates.append(EvidenceItem(
                evidence_id=f'{requirement["requirement_id"]}:{record["record_id"]}',
                requirement_id=requirement["requirement_id"],
                evidence_type=record["evidence_type"],
                finding=record["summary"],
                source_system=record["source_system"],
                source_record_id=record["record_id"],
                service_date=record["service_date"],
                provenance_valid=True,
                retrieval_score=score,
                retrieval_reasons=reasons,
            ))

        candidates.sort(key=lambda item: item.retrieval_score, reverse=True)
        evidence.extend(candidates)

    return evidence
