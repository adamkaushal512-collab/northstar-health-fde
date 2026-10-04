from dataclasses import dataclass

@dataclass(frozen=True)
class UATResult:
    scenario_id: str
    accepted: bool
    notes: str

def evaluate_uat(scenario: dict, actual: dict) -> UATResult:
    checks = [
        actual.get("human_review_required") is scenario["expected_human_review_required"],
        actual.get("disposition") == scenario["expected_disposition"],
        set(scenario.get("required_reason_codes", []))
            .issubset(set(actual.get("reason_codes", []))),
    ]
    return UATResult(
        scenario["scenario_id"],
        all(checks),
        "Acceptance criteria satisfied." if all(checks) else "Acceptance criteria failed.",
    )
