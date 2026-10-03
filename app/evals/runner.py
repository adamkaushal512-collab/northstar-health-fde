from __future__ import annotations
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from app.models.schemas import InvestigationRequest
from app.services.investigation import InvestigationService

EXPECTED_TOOLS = ["authorization.get_case", "payer.get_requirements", "clinical.get_records"]

@dataclass
class CaseEvaluation:
    case_id: str
    requirement_accuracy: float
    provenance_accuracy: float
    grounding_accuracy: float
    human_review_preserved: bool
    tool_sequence_valid: bool
    passed: bool

@dataclass
class EvaluationReport:
    cases: list[CaseEvaluation]
    requirement_accuracy: float
    provenance_accuracy: float
    grounding_accuracy: float
    human_review_rate: float
    tool_sequence_accuracy: float
    pass_rate: float

    def as_dict(self):
        return {
            "cases": [asdict(c) for c in self.cases],
            "metrics": {k: getattr(self, k) for k in (
                "requirement_accuracy", "provenance_accuracy", "grounding_accuracy",
                "human_review_rate", "tool_sequence_accuracy", "pass_rate"
            )}
        }

def load_eval_cases(path="data/evals/prior_auth_eval_cases.json"):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def ratio(value, total):
    return round(value / total, 4) if total else 1.0

def evaluate_case(service, case):
    result = service.investigate(InvestigationRequest(
        authorization_case_id=case["authorization_case_id"]
    ))
    expected = case["expected_requirement_statuses"]
    actual = {r.requirement_id: r.status for r in result.requirements}
    requirement_accuracy = ratio(sum(actual.get(k) == v for k, v in expected.items()), len(expected))
    provenance_accuracy = ratio(sum(bool(e.provenance_valid and e.source_system and e.source_record_id) for e in result.evidence), len(result.evidence))
    summaries = [r for r in result.requirements if r.grounded_summary is not None]
    grounding_accuracy = ratio(sum(bool(r.evidence_ids) for r in summaries), len(summaries))
    human = result.human_review_required is True
    tools = [t.tool for t in result.tool_trace] == EXPECTED_TOOLS
    passed = requirement_accuracy == provenance_accuracy == grounding_accuracy == 1.0 and human and tools
    return CaseEvaluation(case["authorization_case_id"], requirement_accuracy, provenance_accuracy, grounding_accuracy, human, tools, passed)

def run_evaluation(path="data/evals/prior_auth_eval_cases.json"):
    cases = [evaluate_case(InvestigationService(), c) for c in load_eval_cases(path)]
    n = len(cases)
    return EvaluationReport(
        cases,
        ratio(sum(c.requirement_accuracy for c in cases), n),
        ratio(sum(c.provenance_accuracy for c in cases), n),
        ratio(sum(c.grounding_accuracy for c in cases), n),
        ratio(sum(c.human_review_preserved for c in cases), n),
        ratio(sum(c.tool_sequence_valid for c in cases), n),
        ratio(sum(c.passed for c in cases), n),
    )

if __name__ == "__main__":
    print(json.dumps(run_evaluation().as_dict(), indent=2))
