from pydantic import BaseModel, Field, validator
import re

class UserCreate(BaseModel):
    username: str
    password: str = Field(..., min_length=8)

    @validator("password")
    def validate_password(cls, v):
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[0-9]", v):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[\W_]", v):
            raise ValueError("Password must contain at least one symbol")
        return v

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        from_attributes = True