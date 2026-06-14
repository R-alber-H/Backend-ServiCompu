from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    address: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    dni: Optional[str] = None
    phone: Optional[str] = None
    role_id: int

    class Config:
        from_attributes = True