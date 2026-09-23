from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Student Database Backend is running!"

def test_get_students():
    response = client.get("/students/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_chatbot():
    response = client.post(
        "/chat/",
        json={"message": "Rahul"}
    )

    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"]