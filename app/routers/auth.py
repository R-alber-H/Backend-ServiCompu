from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.otp_repository import OtpRepository
from app.repositories.user_repositorry import UserRepository
from app.schemas.otp import OtpRequest, OtpVerify
from app.schemas.user import  UserResponse
from app.services.auth_service import AuthService
# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    repo_user = UserRepository(db)
    repo_otp = OtpRepository(db)
    return AuthService(repo_user, repo_otp)

# security = HTTPBearer()

# @router.post("/",response_model=UserResponse,status_code=201)
# def create_user(user_data:UserRegister,service: AuthService = Depends(get_auth_service)):
#     try:
#         return service.register(user_data)
#     except ValueError as e:
#         raise HTTPException(status_code=409, detail=str(e))

@router.post("/send-otp",status_code=200)
def send_otp(otp_request:OtpRequest, service:AuthService= Depends(get_auth_service)):
    try:
        return service.send_otp(otp_request.email)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.post("/verify-otp",status_code=200)
def verify_otp(otp_verify:OtpVerify, service:AuthService= Depends(get_auth_service)):
    try:
        return service.verify_otp(otp_verify.code,otp_verify.email)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))

@router.get("/me", response_model=UserResponse, status_code=200)
def get_me(payload = Depends(get_current_user), service: AuthService = Depends(get_auth_service)):
    try:
        return service.get_me(payload.get("email"))
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))