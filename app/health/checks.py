from dataclasses import dataclass
@dataclass
class DependencyHealth:
 name:str; available:bool=True
def readiness(dependencies=None):
 deps=dependencies or [DependencyHealth("authorization"),DependencyHealth("payer"),DependencyHealth("clinical_records")]
 ok=all(d.available for d in deps)
 return {"status":"ready" if ok else "degraded","dependencies":{d.name:"available" if d.available else "unavailable" for d in deps}}
