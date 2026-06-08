from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    rol: str
    address: Optional[str] = None

    class Config:
        from_attributes = True