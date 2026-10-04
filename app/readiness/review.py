from dataclasses import dataclass

@dataclass(frozen=True)
class ReadinessCheck:
    name: str
    passed: bool
    blocking: bool = True

def assess_readiness(checks: list[ReadinessCheck]) -> dict:
    blockers=[c.name for c in checks if c.blocking and not c.passed]
    return {
        "decision":"go" if not blockers else "no_go",
        "blocking_failures":blockers,
        "checks":{c.name:c.passed for c in checks},
    }
