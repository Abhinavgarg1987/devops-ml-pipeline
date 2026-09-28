from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_prediction():
    response = client.post("/predict", json={"years_experience": 4.0, "skill_score": 70.0})
    assert response.status_code == 200
    assert "prediction" in response.json()