from datetime import datetime, timezone
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base

class OrderStatusHistory(Base):
    __tablename__ = "order_status_history"
    
    id = Column(Integer,primary_key=True,index=True)
    order_id = Column(Integer,ForeignKey("orders.id"),nullable=False)
    state = Column(String, nullable=False)
    create_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    
    order = relationship("Order", back_populates="status_history")