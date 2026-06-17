from fastapi import  APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.brand_repository import BrandRepository
from app.services.brand_service import BrandService
from app.schemas.brand import BrandResponse, BrandCreate
from app.utils.dependencies import require_admin, require_staff

router = APIRouter(prefix="/brands", tags=["brand"])

def get_brand_service(db:Session = Depends(get_db)) -> BrandService:
    repo_brand = BrandRepository(db)
    return BrandService(repo_brand)

@router.post("/",response_model=BrandResponse,status_code=201,dependencies=[Depends(require_admin)])
def create_brand(data: BrandCreate,serivce:BrandService = Depends(get_brand_service)):
    try:
        return serivce.create_brand(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/",response_model=list[BrandResponse],status_code=200,dependencies=[Depends(require_staff)])
def get_all(service:BrandService = Depends(get_brand_service)):
    return service.get_all()