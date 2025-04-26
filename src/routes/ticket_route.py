from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infra.database_config import get_db

from src.services.ticket_service import TicketService as service

router = APIRouter(prefix="/ticket", tags=["Ticket"])

def get_ticket_service(db: Session = Depends(get_db)):
    return service(db=db)

@router.get("/")

