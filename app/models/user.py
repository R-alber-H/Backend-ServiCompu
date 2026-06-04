from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    rol = Column(String, nullable=False, default="cliente")
    address = Column(String, nullable=True)
    create_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship("Order", back_populates="user")