# INTEGRATION TEST: prüft Create- und List-Flow für Kategorien über die API
def test_create_and_list_categories(client):
    r = client.post("/categories/", json={"name": "Schulbedarf"})
    assert r.status_code == 200
    data = r.json()
    assert data["name"] == "Schulbedarf"
    assert "id" in data

    r = client.get("/categories/")
    assert r.status_code == 200
    items = r.json()
    assert len(items) == 1
    assert items[0]["name"] == "Schulbedarf"
