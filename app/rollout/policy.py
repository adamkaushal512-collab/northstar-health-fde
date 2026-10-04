from dataclasses import dataclass

@dataclass(frozen=True)
class RolloutSignals:
    error_rate: float
    safety_regressions: int
    dependency_failure_rate: float

def rollout_decision(signals: RolloutSignals) -> str:
    if signals.safety_regressions > 0:
        return "rollback"
    if signals.error_rate > 0.05 or signals.dependency_failure_rate > 0.10:
        return "pause"
    return "continue"
