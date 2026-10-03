from __future__ import annotations
from app.models.schemas import EvidenceItem

class GroundedEvidenceSynthesizer:
    """Deterministic stand-in for the future LLM boundary.

    It deliberately produces text only from retrieved evidence and exposes the
    same contract a model-backed implementation can satisfy later.
    """

    def summarize(self, requirement: dict, evidence: list[EvidenceItem]) -> str | None:
        if not evidence:
            return None

        source_lines = [
            f'{item.finding} [source={item.source_system}:{item.source_record_id}]'
            for item in evidence
            if item.provenance_valid
        ]
        if not source_lines:
            return None

        return " ".join(source_lines)
