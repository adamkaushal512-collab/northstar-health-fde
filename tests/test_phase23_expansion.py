from app.use_cases.registry import get_use_case
def test_initial_use_case_enabled():
 assert get_use_case("imaging_prior_auth").enabled
def test_new_use_case_requires_explicit_enablement():
 u=get_use_case("specialty_med_prior_auth")
 assert not u.enabled and u.decision_boundary=="human_only"
