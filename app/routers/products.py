from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductResponse,ProductCreate
from app.services.product_service import ProductService
from app.utils.dependencies import require_admin,require_staff

router = APIRouter(prefix="/products", tags=["product"])

def get_product_service(db:Session = Depends(get_db)) -> ProductService:
    repo_product = ProductRepository(db)
    return ProductService(repo_product)

@router.post("/",response_model=ProductResponse,status_code=201,dependencies=[Depends(require_admin)])
def create_product(data:ProductCreate, service :ProductService = Depends(get_product_service)):
    try:
        return service.create_product(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/",response_model= list[ProductResponse],status_code=200,dependencies=[Depends(require_staff)])
def get_all(sservice :ProductService = Depends(get_product_service)):
    return sservice.get_all()

@router.get("/{id}", response_model=ProductResponse, status_code=200,dependencies=[Depends(require_staff)])
def get_by_id(id: int, service: ProductService = Depends(get_product_service)):
    try:
        return service.get_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))