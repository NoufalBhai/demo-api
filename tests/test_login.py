import pytest
from app.utlis import verify_token

def test_login(client_user):
    user = {
        "email": "test@email.com",
        "password": "123456" 
    }
    res = client_user.post("/auth/login", json=user)
    assert res.status_code == 200
    assert res.json.get("token_type") == "baerer"
    data, err = verify_token(res.json.get("access_token"))
    assert not err
    assert data.get("id") == 1


@pytest.mark.parametrize(
    "email, password, status_code, message",
    [
        (None, None, 400, "Please Provide Required Fields"),
        ("test@email.com", None, 400, "Password is mandatory field"),
        (None, "123456", 400, "Email is mandatory field"),
    ]
)
def test_login_400_errors(client, email, password, status_code, message):
    user = {}
    if email:
        user["email"] = email
    if password:
        user.update({"password": password})

    res = client.post("/auth/login", json=user)
    assert res.status_code == status_code
    assert res.json.get("message") == message

def test_login_user_not_exists(client):
    user = {"email":"test1@gmail.com", "password": "12345"}
    res = client.post("/auth/login", json=user)
    assert res.status_code == 404
    assert res.json.get("message") == f"User with email {user.get('email')} is Not Found"

def test_login_password_missmatch(client_user):
    user = {"email":"test@email.com", "password": "12345"}
    res = client_user.post("/auth/login", json=user)
    assert res.status_code == 403
    assert res.json.get("message") == "Password or email Missmatch"