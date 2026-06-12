from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Attribute(Base):
    __tablename__ = "attributes"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,unique=True,nullable=False)