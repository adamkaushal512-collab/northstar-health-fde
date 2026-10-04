from dataclasses import dataclass
@dataclass(frozen=True)
class ImpactSnapshot:
 cases:int; avg_minutes:float; avg_systems_searched:float; escalation_rate:float; repeat_contact_rate:float
def percent_change(before:float,after:float)->float:
 return round((after-before)/before*100,2) if before else 0.0
def compare(before:ImpactSnapshot,after:ImpactSnapshot)->dict:
 return {
  "resolution_time_change_pct":percent_change(before.avg_minutes,after.avg_minutes),
  "systems_searched_change_pct":percent_change(before.avg_systems_searched,after.avg_systems_searched),
  "escalation_rate_change_pct":percent_change(before.escalation_rate,after.escalation_rate),
  "repeat_contact_rate_change_pct":percent_change(before.repeat_contact_rate,after.repeat_contact_rate),
  "cases_observed":after.cases,
 }
