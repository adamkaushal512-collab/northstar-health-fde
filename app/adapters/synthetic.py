import json
from pathlib import Path
DATA_DIR = Path(__file__).resolve().parents[2] / "data" / "synthetic"

def _load(name: str):
    return json.loads((DATA_DIR / name).read_text(encoding="utf-8"))

class SyntheticAuthorizationAdapter:
    def get_case(self, case_id: str) -> dict:
        for case in _load("authorization_cases.json"):
            if case["authorization_case_id"] == case_id:
                return case
        raise KeyError(f"authorization case not found: {case_id}")

class SyntheticPayerAdapter:
    def get_requirements(self, payer: str, procedure: str) -> list[dict]:
        return [r for r in _load("payer_requirements.json")
                if r["payer"] == payer and r["procedure"] == procedure]

class SyntheticClinicalAdapter:
    def get_records(self, patient_reference: str) -> tuple[list[dict], str]:
        status = _load("source_status.json").get("clinical_records", "available")
        if status != "available":
            return [], "unavailable"
        return [r for r in _load("clinical_records.json")
                if r["patient_reference"] == patient_reference], "available"
