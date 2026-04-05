from datetime import datetime

from pydantic import BaseModel, ValidationInfo, field_validator


class RegistrationCreate(BaseModel):
    user_id: int
    event_id: int

    @field_validator("user_id", "event_id")
    def validate_id(cls, v):
        if v <= 0:
            raise ValueError("ID tidak boleh 0 atau bernilai negatif")
        return v


class RegistrationResponse(BaseModel):
    id: int
    user_id: int
    event_id: int

    class Config:
        from_attributes = True