from fastapi import  APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryResponse, CategoryCreate
from app.services.category_service import CategoryService
from app.utils.dependencies import require_admin, require_staff

router = APIRouter("/",prefix="categories",tags="category")

def get_category_service(db:Session = Depends(get_db)) -> CategoryService:
    repo_category = CategoryRepository(db) 
    return CategoryService(repo_category)

@router.post(path="/",response_model=CategoryResponse,status_code=201, dependencies=[Depends(require_admin)])
def create_category(data:CategoryCreate,service:CategoryService = Depends(get_category_service)):
    try:
        return service.create_category(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.get(path="/",response_model=list[CategoryResponse],status_code=200,dependencies=[Depends(require_staff)])
def get_all(service:CategoryService = Depends(get_category_service)):
    return service.get_all()
    