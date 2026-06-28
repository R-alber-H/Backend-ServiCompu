from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.role_repository import RoleRepository
from app.repositories.user_repositorry import UserRepository
from app.schemas.user import CustomerCreate, UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService
from app.utils.dependencies import require_admin, require_staff

router = APIRouter(prefix="/users", tags=["user"])

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo_user = UserRepository(db)
    repo_role = RoleRepository(db)
    return UserService(repo_user, repo_role)

@router.post("/customer",response_model=UserResponse,status_code=201, dependencies=[Depends(require_staff)])
def create_customer(user_data:CustomerCreate,service :UserService = Depends(get_user_service)):
    try:
        return service.create_customer(user_data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.post("/staff", response_model=UserResponse, status_code=201, dependencies=[Depends(require_admin)])
def create_staff(user_data: UserCreate, service: UserService = Depends(get_user_service)):
    try:
        return service.create_staff(user_data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.get("/",response_model=list[UserResponse],status_code=200, dependencies=[Depends(require_admin)])
def get_all(service :UserService = Depends(get_user_service)):
    return service.get_all()

@router.put("/{id}", response_model=UserResponse,status_code=200,dependencies=[Depends(require_admin)])
def update_user(id:int ,user_data : UserUpdate, service : UserService = Depends(get_user_service)):
    try:
        return service.update_user(id,user_data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
