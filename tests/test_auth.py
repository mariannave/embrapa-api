import os
import pytest
from fastapi import HTTPException
from app import auth
from app.models import UserInDB


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    monkeypatch.setenv("SECRET_KEY", "testsecret")
    monkeypatch.setenv("ALGORITHM", "HS256")


@pytest.fixture
def fake_db():
    password = "testpass"
    hashed = auth.get_password_hash(password)
    return {
        "alice": {
            "username": "alice",
            "hashed_password": hashed,
            "disabled": False,
        },
        "bob": {
            "username": "bob",
            "hashed_password": auth.get_password_hash("bobpass"),
            "disabled": True,
        },
    }


def test_verify_password():
    password = "mypassword"
    hashed = auth.get_password_hash(password)
    assert auth.verify_password(password, hashed)
    assert not auth.verify_password("wrong", hashed)


def test_get_password_hash():
    password = "anotherpass"
    hashed = auth.get_password_hash(password)
    assert isinstance(hashed, str)
    assert auth.verify_password(password, hashed)


def test_get_user(fake_db):
    user = auth.get_user(fake_db, "alice")
    assert isinstance(user, UserInDB)
    assert user.username == "alice"
    assert auth.get_user(fake_db, "notfound") is None


def test_authenticate_user(fake_db):
    user = auth.authenticate_user(fake_db, "alice", "testpass")
    assert user is not False
    assert user.username == "alice"
    assert auth.authenticate_user(fake_db, "alice", "wrongpass") is False
    assert auth.authenticate_user(fake_db, "notfound", "testpass") is False


def test_create_access_token_and_decode(fake_db):
    data = {"sub": "alice"}
    token = auth.create_access_token(data)
    decoded = auth.jwt.decode(
        token, os.getenv("SECRET_KEY"), algorithms=os.getenv("ALGORITHM")
    )
    assert decoded["sub"] == "alice"
    assert "exp" in decoded


@pytest.mark.asyncio
async def test_get_current_user_valid_token(fake_db, monkeypatch):
    user = auth.get_user(fake_db, "alice")
    data = {"sub": user.username}
    token = auth.create_access_token(data)
    monkeypatch.setattr(auth, "fake_users_db", fake_db)
    result = await auth.get_current_user(token)
    assert result.username == "alice"


@pytest.mark.asyncio
async def test_get_current_user_invalid_token(monkeypatch):
    monkeypatch.setattr(auth, "fake_users_db", {})
    with pytest.raises(HTTPException):
        await auth.get_current_user("invalid.token.here")


@pytest.mark.asyncio
async def test_get_current_user_user_not_found(monkeypatch, fake_db):
    data = {"sub": "ghost"}
    token = auth.create_access_token(data)
    monkeypatch.setattr(auth, "fake_users_db", fake_db)
    with pytest.raises(HTTPException):
        await auth.get_current_user(token)


@pytest.mark.asyncio
async def test_get_current_active_user_active(fake_db):
    user = auth.get_user(fake_db, "alice")
    result = await auth.get_current_active_user(user)
    assert result.username == "alice"


@pytest.mark.asyncio
async def test_get_current_active_user_inactive(fake_db):
    user = auth.get_user(fake_db, "bob")
    with pytest.raises(HTTPException) as exc:
        await auth.get_current_active_user(user)
    assert exc.value.status_code == 400
