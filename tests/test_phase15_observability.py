import json,logging
from app.core.request_context import new_request_id
from app.observability.logging import JsonFormatter
from app.observability.metrics import increment,snapshot,reset
from app.observability.tracing import span
def test_request_id_json_log():
 new_request_id("req-123")
 rec=logging.LogRecord("northstar",logging.INFO,"",0,"hello",(),None)
 data=json.loads(JsonFormatter().format(rec))
 assert data["request_id"]=="req-123"
def test_metrics_counter():
 reset();increment("investigations");increment("investigations")
 assert snapshot()["investigations"]==2
def test_trace_span():
 with span("investigation") as s:pass
 assert s["status"]=="ok" and s["duration_ms"]>=0
