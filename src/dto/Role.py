from pydantic import BaseModel, field_validator


class RoleCreate(BaseModel):
    name: str

    @field_validator("name")
    def validate_name(cls, v):
        if not v.strip():
            raise ValueError("Name tidak boleh kosong")
        return v
    
class RoleUpdate(BaseModel):
    name: str | None = None

    @field_validator("name")
    def validate_name(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Name tidak boleh kosong")
        return v
    
class RoleResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True