from fastapi import FastAPI
from fastapi.testclient import TestClient
from education_management_system.main import app

client = TestClient(app)

def test_for_test():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {'status': 'I am Live.'}