from __future__ import annotations
import sys
from pathlib import Path

# Allow `python scripts/demo.py` from a fresh clone without requiring an editable install.
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime.safe_investigation import SafeInvestigationRuntime

def line(char="=", n=72):
    print(char * n)

def main() -> None:
    case_id = sys.argv[1] if len(sys.argv) > 1 else "AUTH-1001"
    result = SafeInvestigationRuntime().investigate(case_id)
    inv = result.investigation

    line()
    print("NORTHSTAR HEALTH — PRIOR AUTHORIZATION INVESTIGATION DEMO")
    line()
    print(f"Case: {inv.authorization_case_id}")
    print(f"Procedure: {inv.procedure}")
    print(f"Payer: {inv.payer}")
    print(f"Human review required: {inv.human_review_required}")
    print(f"Audit reference: {inv.audit_reference}")

    print("\nPAYER REQUIREMENTS")
    line("-")
    for req in inv.requirements:
        print(f"[{req.status}] {req.requirement_id}: {req.description}")
        if req.grounded_summary:
            print(f"  Summary: {req.grounded_summary}")
        if req.evidence_ids:
            print(f"  Evidence: {', '.join(req.evidence_ids)}")

    print("\nEVIDENCE + PROVENANCE")
    line("-")
    if not inv.evidence:
        print("No evidence returned.")
    for e in inv.evidence:
        print(f"{e.evidence_id} -> {e.requirement_id}")
        print(f"  Finding: {e.finding}")
        print(f"  Source: {e.source_system}/{e.source_record_id} ({e.service_date})")
        print(f"  Provenance valid: {e.provenance_valid}; retrieval score: {e.retrieval_score}")

    print("\nBOUNDED TOOL TRACE")
    line("-")
    for t in inv.tool_trace:
        print(f"{t.tool}: {t.status} — {t.detail}")

    print("\nSAFETY / FALLBACK")
    line("-")
    print(f"Unavailable sources: {inv.unavailable_sources or 'none'}")
    print(f"Warnings: {inv.warnings or 'none'}")
    print(f"Disposition: {result.fallback.disposition.value}")
    print(f"Reason codes: {result.fallback.reasons or 'none'}")
    print(f"Automation allowed: {result.fallback.automation_allowed}")
    print(f"Escalation required: {result.escalation.required}")
    if result.escalation.queue:
        print(f"Escalation queue: {result.escalation.queue}")

    line()
    print("AI assists evidence investigation; the human specialist retains the decision.")
    line()

if __name__ == "__main__":
    main()
