from fastapi.testclient import TestClient
from app.main import app
c = TestClient(app)


def test_health():
    assert c.get("/health").status_code == 200


def test_memory_accumulates():
    c.post("/chat", json={"session_id": "s1", "message": "What is in the free plan?"})
    r = c.post("/chat", json={"session_id": "s1", "message": "and the pro one?"})
    assert r.json()["turns"] == 2
    assert len(r.json()["citations"]) >= 1
