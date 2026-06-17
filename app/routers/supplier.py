from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.repositories.supplier_repository import SupplierRepository
from app.schemas.supplier import SupplierResponse, SupplierCreate
from app.services.supplier_service import SupplierService
from app.utils.dependencies import require_admin,require_staff

router = APIRouter(prefix="/suppliers",tags=["supplier"])

def get_supplier_service(db:Session = Depends(get_db)) -> SupplierService:
    repo_supplier = SupplierRepository(db)
    return SupplierService(repo_supplier)

@router.post(path="/",response_model=SupplierResponse,status_code=201,dependencies=[Depends(require_admin)])
def create_supplier(data:SupplierCreate,service:SupplierService = Depends(get_supplier_service)):
    try:
        return service.create_supplier(data)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get(path="/",response_model=list[SupplierResponse],status_code=200,dependencies=[Depends(require_staff)])
def get_all(service:SupplierService = Depends(get_supplier_service)):
    return service.get_all()