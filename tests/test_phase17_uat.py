from app.pilot.uat import evaluate_uat

def test_uat_accepts_matching_workflow():
    scenario={"scenario_id":"UAT-X","expected_human_review_required":True,
              "expected_disposition":"human_review",
              "required_reason_codes":["insufficient_evidence"]}
    actual={"human_review_required":True,"disposition":"human_review",
            "reason_codes":["insufficient_evidence"]}
    assert evaluate_uat(scenario,actual).accepted

def test_uat_rejects_unsafe_automation():
    scenario={"scenario_id":"UAT-Y","expected_human_review_required":True,
              "expected_disposition":"continue_review","required_reason_codes":[]}
    actual={"human_review_required":False,"disposition":"continue_review","reason_codes":[]}
    assert not evaluate_uat(scenario,actual).accepted
