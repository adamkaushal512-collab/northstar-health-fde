from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_investigation_api():
    response = client.post("/investigations", json={"authorization_case_id": "AUTH-1001"})
    assert response.status_code == 200
    body = response.json()
    assert body["authorization_case_id"] == "AUTH-1001"
    assert body["human_review_required"] is True
    assert body["audit_reference"].startswith("INV-")
