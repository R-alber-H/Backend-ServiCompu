from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.jwt import verify_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Token no válido")
    return payload

def require_admin(payload: dict = Depends(get_current_user)):
    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Acceso solo para administradores")
    return payload

def require_staff(payload: dict = Depends(get_current_user)):
    if payload.get("role") not in ["admin", "ventas"]:
        raise HTTPException(status_code=403, detail="Acceso no autorizado")
    return payload