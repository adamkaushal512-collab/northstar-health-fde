from app.config.settings import Settings
from app.core.resilience import call_with_retry
from app.core.errors import DependencyUnavailable
from app.health.checks import readiness,DependencyHealth
def test_settings_defaults():
 s=Settings();assert s.dependency_timeout_seconds>0 and s.dependency_max_retries>=0
def test_retry_recovers():
 state={"n":0}
 def flaky():
  state["n"]+=1
  if state["n"]<2:raise ConnectionError("temporary")
  return "ok"
 assert call_with_retry(flaky)=="ok"
def test_retry_exhaustion():
 def bad():raise TimeoutError("down")
 try:call_with_retry(bad)
 except DependencyUnavailable:pass
 else:assert False
def test_readiness_degraded():
 r=readiness([DependencyHealth("ehr",False)])
 assert r["status"]=="degraded"
