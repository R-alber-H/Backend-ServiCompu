from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class ProductCreate(BaseModel):
    brand_id :int
    supplier_id : Optional[int] = None
    name :str
    price :float
    img_url :str
    initial_stock:int
    description: Optional[str] = None
    category_ids:list[int]
    
class BrandResponse(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)
    
class SupplierResponse(BaseModel):
    id : int
    name:str
    phone :str
    model_config = ConfigDict(from_attributes=True)
    
class InventoryResponse(BaseModel):
    stock : int
    model_config = ConfigDict(from_attributes=True)

class CategoryResponse(BaseModel):
    id: int
    name: str
    model_config = ConfigDict(from_attributes=True)

class ProductCategoryResponse(BaseModel):
    category: CategoryResponse
    model_config = ConfigDict(from_attributes=True)
    
class ProductResponse(BaseModel):
    id:int
    name:str
    price:float
    img_url:str
    description:Optional[str] = None
    active:bool
    brand:BrandResponse
    supplier: Optional[SupplierResponse] = None
    inventory: InventoryResponse
    product_categories : list[ProductCategoryResponse]
    model_config = ConfigDict(from_attributes=True)
    
class ProductUpdate(BaseModel):
    name:str | None = None
    price:float | None = None