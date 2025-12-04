import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root_redirect():
    response = client.get("/")
    assert response.status_code in (200, 307)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    activities = client.get("/activities").json()
    activity_name = next(iter(activities.keys()))
    email = "testuser@mergington.edu"
    signup = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert signup.status_code in (200, 400)
    unregister = client.post(f"/activities/{activity_name}/unregister?email={email}")
    assert unregister.status_code in (200, 400)
