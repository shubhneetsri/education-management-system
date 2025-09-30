import uuid
from fastapi.testclient import TestClient
from education_management_system.main import app

client = TestClient(app)

def test_create_user():
    username = f"user_{uuid.uuid4()}"
    email = f"{username}@example.com"
    payload = {"username": username, "email": email, "password": "simplepass"}

    response = client.post("/block_users/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == username
    assert data["email"] == email

def test_get_users():
    response = client.get("/block_users/users")
    assert response.status_code == 200
    users = response.json()
    assert isinstance(users, list)
    assert len(users) >= 1
