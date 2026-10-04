from app.readiness.review import ReadinessCheck,assess_readiness

def test_readiness_go_when_blockers_pass():
    r=assess_readiness([ReadinessCheck("tests",True),ReadinessCheck("security",True)])
    assert r["decision"]=="go"

def test_readiness_no_go_on_blocker():
    r=assess_readiness([ReadinessCheck("tests",True),ReadinessCheck("security",False)])
    assert r["decision"]=="no_go" and "security" in r["blocking_failures"]
