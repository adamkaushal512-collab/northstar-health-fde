from contextvars import ContextVar
import uuid
_request_id=ContextVar("request_id",default=None)
def new_request_id(value=None):
 rid=value or str(uuid.uuid4());_request_id.set(rid);return rid
def get_request_id():return _request_id.get()
