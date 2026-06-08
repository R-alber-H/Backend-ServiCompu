from datetime import datetime, timedelta, timezone

from app.models.otp_code import OtpCode
from app.models.user import User
from app.repositories.otp_repository import OtpRepository
from app.repositories.user_repositorry import UserRepository
from app.schemas.user import UserRegister
from app.utils import email,jwt,otp

class AuthService():
    def __init__(self,repo_user: UserRepository,repo_otp: OtpRepository):
        self.repo_user = repo_user
        self.repo_otp = repo_otp
    
    def register(self, user: UserRegister):
        user_exists = self.repo_user.get_by_email(user.email)
        if user_exists:
            raise ValueError("El usuario ya esta registrado")
        new_user = User(
            name = user.name,
            email = user.email,
            address = user.address
        )
        return self.repo_user.create(new_user)
    
    def send_otp(self,user_email: str):
        user_exists = self.repo_user.get_by_email(user_email)
        if not user_exists:
            raise ValueError("El usuario no esta registrado")
        codigo = otp.generate_otp()
        new_otp_code = OtpCode(
            email = user_email,
            code = codigo,
            expires_at = datetime.now(timezone.utc)+ timedelta(minutes=10)
        )
        self.repo_otp.create(new_otp_code)
        email.send_otp_email(user_email,codigo)
        return {"message": "Código enviado a tu correo"}
        
    def verify_otp(self,codigo:str,user_email:str):
        code_exists = self.repo_otp.get_valid(user_email,codigo)
        if not code_exists:
            raise ValueError("Elcodigo no existe")
        self.repo_otp.mark_as_used(code_exists)
        user = self.repo_user.get_by_email(user_email)
        if not user:
            raise ValueError("El usuario no esta registrado")
        data = {"sub": str(user.id), "email": user.email}
        return jwt.create_access_token(data)
    
    def get_me(self,token:str):
        payload = jwt.verify_token(token)
        if not payload:
            raise ValueError("Token no valido")
        email = payload.get("email")
        user = self.repo_user.get_by_email(email)
        return user
        