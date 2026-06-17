from typing import Optional
from pydantic import BaseModel

class SupplierCreate(BaseModel):
    name: str
    phone: str | None = None

class SupplierResponse(BaseModel):
    id:int
    name:str
    phone: str | None
    class Config:
        from_attributes = True
        