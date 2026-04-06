from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, field_validator, model_validator


class UserCreate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    whatsapp: str
    created_at: datetime
    updated_at: datetime

    @field_validator("whatsapp")
    def validate_whatsapp(cls, v):
        if not v.isdigit():
            raise ValueError("Nomor whatsapp harus angka")
        if len(v) < 10:
            raise ValueError("Nomor whatsapp tidak valid")
        return v


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: Optional[str] = None
    whatsapp: Optional[str] = None
    created_at: datetime
    updated_at: datetime
