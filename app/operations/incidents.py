from dataclasses import dataclass

@dataclass(frozen=True)
class Incident:
    severity: str
    reason: str
    action: str

def classify_incident(*, safety_regression=False, service_unavailable=False,
                      dependency_degraded=False) -> Incident | None:
    if safety_regression:
        return Incident("SEV-1","safety_regression","rollback_and_escalate")
    if service_unavailable:
        return Incident("SEV-2","service_unavailable","restore_service")
    if dependency_degraded:
        return Incident("SEV-3","dependency_degraded","use_fallback_and_investigate")
    return None
