def test_create_mood(client):
    payload = {
        "mood_score": 7.5,
        "energy_level": 6.0,
        "anxiety_level": 3.0,
        "attachment_score": 5.0,
        "label": "content",
    }
    response = client.post("/api/v1/moods/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["mood_score"] == 7.5
    assert data["label"] == "content"
    assert "id" in data


def test_list_moods(client):
    client.post(
        "/api/v1/moods/",
        json={"mood_score": 5.0, "energy_level": 5.0, "anxiety_level": 5.0},
    )
    response = client.get("/api/v1/moods/")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_mood(client):
    create = client.post(
        "/api/v1/moods/",
        json={"mood_score": 8.0, "energy_level": 7.0, "anxiety_level": 2.0},
    )
    mood_id = create.json()["id"]
    response = client.get(f"/api/v1/moods/{mood_id}")
    assert response.status_code == 200
    assert response.json()["mood_score"] == 8.0
