import os
from dataclasses import dataclass
@dataclass(frozen=True)
class Settings:
 environment:str=os.getenv("NORTHSTAR_ENV","local")
 dependency_timeout_seconds:float=float(os.getenv("NORTHSTAR_DEPENDENCY_TIMEOUT_SECONDS","3"))
 dependency_max_retries:int=int(os.getenv("NORTHSTAR_DEPENDENCY_MAX_RETRIES","2"))
