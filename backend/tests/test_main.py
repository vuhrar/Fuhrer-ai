from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)


def test_root_returns_application_metadata():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "application": "Fuhrer",
        "version": "0.1.0",
        "status": "running",
    }


def test_health_returns_healthy_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
