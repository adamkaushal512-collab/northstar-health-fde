from app.operations.incidents import classify_incident
from app.operations.slo import availability_met

def test_safety_incident_is_sev1():
    i=classify_incident(safety_regression=True)
    assert i.severity=="SEV-1" and i.action=="rollback_and_escalate"

def test_dependency_degradation_uses_fallback():
    i=classify_incident(dependency_degraded=True)
    assert i.severity=="SEV-3" and i.action=="use_fallback_and_investigate"

def test_availability_slo():
    assert availability_met(995,1000,.99)
    assert not availability_met(980,1000,.99)
