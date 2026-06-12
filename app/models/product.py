from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    brand_id =Column(Integer,ForeignKey("brands.id"),nullable=False)
    supplier_id = Column(Integer,ForeignKey("suppliers.id"))
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    img_url = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)
    create_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    order_details = relationship("OrderDetail", back_populates="product")
    attributes = relationship("ProductAttribute", back_populates="product")
    brand = relationship("Brand", back_populates="products")
    supplier = relationship("Supplier", back_populates="products")