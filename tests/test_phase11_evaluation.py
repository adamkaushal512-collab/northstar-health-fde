from app.evals.runner import load_eval_cases, run_evaluation

def test_eval_dataset_has_multiple_scenarios():
    cases = load_eval_cases()
    assert len(cases) == 3
    assert {c["scenario"] for c in cases} == {"partial evidence", "complete evidence", "no matching evidence"}

def test_phase11_baseline_metrics():
    report = run_evaluation()
    assert report.requirement_accuracy == 1.0
    assert report.provenance_accuracy == 1.0
    assert report.grounding_accuracy == 1.0
    assert report.human_review_rate == 1.0
    assert report.tool_sequence_accuracy == 1.0
    assert report.pass_rate == 1.0
