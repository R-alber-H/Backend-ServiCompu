from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    delivery_type = Column(String, nullable=False)
    address = Column(String, nullable=True)
    state = Column(String, nullable=False, default="pendiente")
    total = Column(Float, nullable=False)
    create_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="orders")
    details = relationship("OrderDetail", back_populates="order")