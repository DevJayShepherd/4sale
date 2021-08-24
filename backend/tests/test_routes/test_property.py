import json


def test_add_property(client):
    data = {
        "property_title": "string",
        "property_price": "string",
        "property_status": "string",
        "property_area_size": "string",
        "property_bedrooms": 0,
        "property_garages": 0,
        "property_bathrooms": 0,
        "property_description": "string"
    }
    response = client.post("/property/create-property", json.dumps(data))
    assert response.status_code == 200
