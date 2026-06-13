from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    name = Column(String, nullable=False)
    dni = Column(String, nullable=True, unique=True)
    email = Column(String, nullable=True, unique=True)
    phone = Column(String, nullable=True)
    password = Column(String, nullable=True)  
    create_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    orders = relationship("Order", back_populates="user")
    role = relationship("Role", back_populates="users")