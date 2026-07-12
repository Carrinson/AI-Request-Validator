from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_something():
    response = client.post("/validate", json={
    "messages": [{"role": "user", "content": "How do I do a bubble sort?"}],
    "model": "claude-opus-4-7",
    "max_tokens": 200,
    "system_prompt": ""
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_bad():
    response = client.post("/validate", json={
    "messages": [{"role": "user", "content": "How do I do a bubble sort?"}],
    "model": "claude-opus-4",
    "max_tokens": 200,
    "system_prompt": ""
    })
    assert response.status_code == 422