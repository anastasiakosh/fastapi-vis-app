from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_data_endpoint():
    response = client.get("/api/data")
    assert response.status_code == 200
    assert "x" in response.json()
    assert "y" in response.json()
