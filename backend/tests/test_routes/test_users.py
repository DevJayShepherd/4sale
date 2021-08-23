import json


def test_create_user(client):
    data = {
        "first_name": "string",
        "last_name": "string",
        "password": "string",
        "email": "user@example.com",
        "facebook": "string",
        "twitter": "string",
        "website": "string",
        "phone": "string",
        "public_email": "string",
        "picture": "string"
    }
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
