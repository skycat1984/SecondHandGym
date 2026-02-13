# INTEGRATION TEST: kompletter Item-Flow (create, get, filter, patch, delete)
def test_items_flow_create_get_list_filter_patch_delete(client):
    # Kategorie anlegen
    rc = client.post("/categories/", json={"name": "Buecher"})
    assert rc.status_code == 200
    cat_id = rc.json()["id"]

    # Item anlegen
    r = client.post(
        "/items/",
        json={
            "title": "Mathebuch",
            "description": "Guter Zustand",
            "price": 10,
            "category_id": cat_id,
        },
    )
    assert r.status_code == 200
    item = r.json()
    item_id = item["id"]
    assert item["status"] == "verfuegbar"

    # GET /items/{id}
    r = client.get(f"/items/{item_id}")
    assert r.status_code == 200

    # Filter status
    r = client.get("/items/", params={"status": "verfuegbar"})
    assert r.status_code == 200
    assert len(r.json()) == 1

    # Filter category_id
    r = client.get("/items/", params={"category_id": cat_id})
    assert r.status_code == 200
    assert len(r.json()) == 1

    # PATCH status
    r = client.patch(f"/items/{item_id}/status", json={"status": "reserviert"})
    assert r.status_code == 200
    patched = r.json()
    assert patched["status"] == "reserviert"
    assert patched["updated_at"] is not None

    # DELETE
    r = client.delete(f"/items/{item_id}")
    assert r.status_code == 204

    # danach 404
    r = client.get(f"/items/{item_id}")
    assert r.status_code == 404

# INTEGRATION TEST: prüft, dass negative Preise über die API 422 zurückgeben
def test_item_price_validation(client):
    rc = client.post("/categories/", json={"name": "Test"})
    cat_id = rc.json()["id"]

    r = client.post(
        "/items/",
        json={
            "title": "X",
            "description": "Y",
            "price": -1,
            "category_id": cat_id,
        },
    )
    assert r.status_code == 422
