from app import create_app


def test_index_returns_lab_message():
    client = create_app().test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json() == {"message": "DevOps CI/CD lab is running"}


def test_health_returns_healthy_status():
    client = create_app().test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
