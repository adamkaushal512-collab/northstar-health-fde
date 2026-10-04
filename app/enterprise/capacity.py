def required_workers(peak_cases_per_minute:float,worker_cases_per_minute:float,headroom:float=0.30)->int:
 import math
 if worker_cases_per_minute<=0: raise ValueError("worker capacity must be positive")
 return max(1,math.ceil((peak_cases_per_minute*(1+headroom))/worker_cases_per_minute))
