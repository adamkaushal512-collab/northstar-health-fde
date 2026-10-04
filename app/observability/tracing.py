from contextlib import contextmanager
import time
@contextmanager
def span(name):
 start=time.perf_counter()
 data={"name":name,"status":"ok","duration_ms":0.0}
 try:yield data
 except Exception:
  data["status"]="error";raise
 finally:data["duration_ms"]=round((time.perf_counter()-start)*1000,3)
