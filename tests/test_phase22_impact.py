from app.impact.metrics import ImpactSnapshot,compare
def test_impact_comparison():
 b=ImpactSnapshot(1000,42,4.8,.31,.22);a=ImpactSnapshot(1000,24,2.1,.20,.14)
 r=compare(b,a)
 assert r["resolution_time_change_pct"]<0
 assert r["systems_searched_change_pct"]<0
 assert r["escalation_rate_change_pct"]<0
