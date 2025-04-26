from sqlalchemy import Column, Integer, String
from src.models.base_model import BaseModel
from src.enum.status_enum import EStutus


class Ticket(BaseModel):
    __tablename__ = 'tickets'
    
    title = Column(String(150), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(Integer, default=EStutus.OPEN.value, nullable=False)
