from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    img_url = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    create_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    order_details = relationship("OrderDetail", back_populates="product")
    attributes = relationship("ProductAttribute", back_populates="product")