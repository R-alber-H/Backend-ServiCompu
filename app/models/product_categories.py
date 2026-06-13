from sqlalchemy import Column, Integer,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class ProductCategory(Base):
    __tablename__ = "product_categories"
    
    id = Column(Integer, primary_key=True,index=True)
    product_id = Column(Integer,ForeignKey("products.id"),nullable=False)
    category_id = Column(Integer,ForeignKey("categories.id"),nullable=False)
    
    category = relationship("Category", back_populates="product_categories")
    product = relationship("Product",back_populates="product_categories")