from pydantic import BaseModel, field_validator


class AccountCreate(BaseModel):
    user_id: int
    role_id: int
    email: str
    username: str
    password: str

    @field_validator("email")
    def validate_email(cls, v):
        if "@" not in v:
            raise ValueError("Email tidak valid")
        return v


class AccountUpdate(BaseModel):
    user_id: int | None = None
    role_id: int | None = None
    email: str | None = None
    username: str | None = None
    password: str | None = None


class AccountResponse(BaseModel):
    id: int
    user_id: int
    role_id: int
    email: str
    username: str

    class Config:
        from_attributes = True