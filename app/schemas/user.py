from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    role_id: int

class CustomerCreate(BaseModel):
    name: str
    dni: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    
class RoleResponse(BaseModel):
    name:str

class UserResponse(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    dni: Optional[str] = None
    phone: Optional[str] = None
    role: RoleResponse

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name:str
    phone:str
    