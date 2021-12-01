

def test_create_profile_success(client_user, token):
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    profile = {
        "name": "Test User",
        "gender": "Male",
        "dob": "2020-03-10"
    }
    res = client_user.post("/profile", json=profile, headers=headers)
    assert res.status_code == 201
    assert res.json.get("name") == profile.get("name")


def test_update_profile_success(client_profile, token):
    headers = {
        "Authorization" : f"Bearer {token}"
    }
    profile = {
        "name": "Test Change",
        "gender": "Male",
        "dob": "2020-03-10"
    }
    res = client_profile.put("/profile", json=profile, headers=headers)
    assert res.status_code == 200
    assert res.json.get("name") == profile.get("name")
    assert res.json.get("gender") == profile.get("gender")
