from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    payment_method_id = Column(Integer, ForeignKey("payment_methods.id"),nullable=False)
    is_delivery = Column(Boolean, nullable=False)
    delivery_address = Column(String, nullable=True)
    total = Column(Float, nullable=False)
    create_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    user = relationship("User", back_populates="orders")
    details = relationship("OrderDetail", back_populates="order")
    payment_method = relationship("PaymentMethod", back_populates="orders")
    status_history = relationship("OrderStatusHistory", back_populates="order")