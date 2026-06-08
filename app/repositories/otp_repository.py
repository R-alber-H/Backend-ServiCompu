from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models.otp_code import OtpCode

class OtpRepository:
    def __init__(self,db: Session):
        self.db = db
        
    def create(self,otp: OtpCode) -> OtpCode:
        self.db.add(otp)
        self.db.commit()
        self.db.refresh(otp)
        return otp

    def get_valid(self, email: str, code: str) -> OtpCode | None:
        return self.db.query(OtpCode).filter(
            OtpCode.email == email,
            OtpCode.code == code, 
            OtpCode.used == False,
            OtpCode.expires_at > datetime.now(timezone.utc)
            ).first()
    
    def mark_as_used(self,otp: OtpCode):
        otp.used = True
        self.db.commit()