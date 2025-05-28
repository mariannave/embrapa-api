from pydantic import BaseModel

fake_users_db = {
    "user1": {
        "username": "user1",
        "hashed_password": "$2b$12$/TKy1L0/4hwjHsLTfF1tAOCFRlvmDaqRJihWDfq/Ps1nedrVAks2q",
        "disabled": False,
    }
}


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
