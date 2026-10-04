from dataclasses import dataclass
from app.core.errors import DependencyUnavailable
@dataclass(frozen=True)
class RetryPolicy:
 max_retries:int=2
def call_with_retry(fn,*args,policy=RetryPolicy(),**kwargs):
 last=None
 for _ in range(policy.max_retries+1):
  try:return fn(*args,**kwargs)
  except (TimeoutError,ConnectionError) as exc:last=exc
 raise DependencyUnavailable(str(last))
