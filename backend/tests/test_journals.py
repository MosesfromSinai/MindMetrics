def test_create_journal(client):
    payload = {
        "title": "Morning Reflection",
        "content": "Feeling calm and grounded today.",
        "mood_tag": "calm",
    }
    response = client.post("/api/v1/journals/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Morning Reflection"
    assert data["mood_tag"] == "calm"


def test_list_journals(client):
    client.post(
        "/api/v1/journals/",
        json={"title": "Entry 1", "content": "Test content"},
    )
    response = client.get("/api/v1/journals/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_journal(client):
    create = client.post(
        "/api/v1/journals/",
        json={"title": "Test", "content": "Body text"},
    )
    journal_id = create.json()["id"]
    response = client.get(f"/api/v1/journals/{journal_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test"
