import pytest

@pytest.mark.parametrize("email, password, status_code, message",[
    ("test@email.com", "123456", 201, None),
    (None, "123456", 400, "Email is mandatory field"),
    ("test@email.com", None, 400, "Password is mandatory field"),
    (None, None, 400, "Please Provide Required Fields"),
])
def test_register_success(client, email, password, status_code, message):
    user = {}
    if email:
        user["email"] = email
    if password:
        user["password"] = password
    res = client.post("/auth/register", json=user)
    assert res.status_code == status_code
    if status_code == 201:
        assert res.json.get("email") == email
    assert res.json.get("message") == message
