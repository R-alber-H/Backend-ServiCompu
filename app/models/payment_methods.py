from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class PaymentMethod(Base):
    __tablename__ = "payment_methods"
    
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False,unique=True)
    
    orders = relationship("Order", back_populates="payment_method")