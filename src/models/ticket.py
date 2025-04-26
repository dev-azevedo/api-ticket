from sqlalchemy import Column, Integer, String
from src.models.base_model import Base, BaseModel
from src.enum.ticket_status_enum import ETicketStatus


class Ticket(Base, BaseModel):
    __tablename__ = 'tickets'
    
    name_user = Column(String(255), nullable=False)
    title = Column(String(150), nullable=False)
    description = Column(String(255), nullable=False)
    status = Column(Integer, default=ETicketStatus.OPEN.value, nullable=False)
