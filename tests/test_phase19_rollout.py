from app.rollout.policy import RolloutSignals,rollout_decision

def test_safety_regression_rolls_back():
    assert rollout_decision(RolloutSignals(.01,1,.01))=="rollback"

def test_operational_regression_pauses():
    assert rollout_decision(RolloutSignals(.08,0,.01))=="pause"

def test_healthy_rollout_continues():
    assert rollout_decision(RolloutSignals(.01,0,.02))=="continue"
