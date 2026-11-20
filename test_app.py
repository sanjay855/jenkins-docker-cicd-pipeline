from app import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_status_endpoint():
    client = app.test_client()
    response = client.get("/api/status")
    assert response.status_code == 200
    data = response.get_json()
    assert data["service"] == "cloud-devops-status-api"
    assert "container_host" in data
