from dataclasses import dataclass
@dataclass(frozen=True)
class UseCase:
 key:str; name:str; decision_boundary:str; enabled:bool=False
USE_CASES={
 "imaging_prior_auth":UseCase("imaging_prior_auth","MRI/CT prior authorization evidence investigation","human_only",True),
 "specialty_med_prior_auth":UseCase("specialty_med_prior_auth","Specialty medication prior authorization evidence investigation","human_only",False),
}
def get_use_case(key:str)->UseCase:return USE_CASES[key]
