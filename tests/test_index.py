def test_index_call(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json.get("message") == "Home"

def test_index_failure(client):
    res = client.post("/")
    assert res.status_code == 405
    assert "Method Not Allowed" in res.data.decode()
