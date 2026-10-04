import json,logging
from app.core.request_context import get_request_id
class JsonFormatter(logging.Formatter):
 def format(self,record):
  return json.dumps({"level":record.levelname,"logger":record.name,"message":record.getMessage(),"request_id":get_request_id()})
def configure_logging():
 h=logging.StreamHandler();h.setFormatter(JsonFormatter())
 root=logging.getLogger();root.handlers=[h];root.setLevel(logging.INFO)
