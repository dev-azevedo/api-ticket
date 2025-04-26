from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    __abastract__ = True
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(Integer, default=func.now(),  onupdate=func.now(), nullable=False)    
    active = Column(Boolean, default=True, nullable=False)
    