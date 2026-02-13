# INTEGRATION TEST: prüft ContactRequest-Erstellung und Listing über die API
def test_contact_request_create_and_list(client):
    # Kategorie anlegen
    rc = client.post("/categories/", json={"name": "Sport"})
    assert rc.status_code == 200
    cat_id = rc.json()["id"]

    # Item anlegen
    ri = client.post(
        "/items/",
        json={
            "title": "Fussball",
            "description": "Kaum benutzt",
            "price": 5,
            "category_id": cat_id,
        },
    )
    assert ri.status_code == 200
    item_id = ri.json()["id"]

    # ContactRequest erstellen
    r = client.post(
        f"/items/{item_id}/contact",
        json={"sender_contact": "test@example.com", "message": "Noch da?"},
    )
    assert r.status_code == 200
    cr = r.json()
    assert cr["item_id"] == item_id

    # Kontakte für Item
    r = client.get(f"/items/{item_id}/contacts")
    assert r.status_code == 200
    assert len(r.json()) == 1

    # Inbox
    r = client.get("/contact-requests")
    assert r.status_code == 200
    assert len(r.json()) == 1
