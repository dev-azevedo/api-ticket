from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from src.infra.database_config import get_db
from src.DTO.ticket_dto import TicketGetDTO, TicketCreateDTO, TicketUpdateDTO

from src.services.ticket_service import TicketService as service

router = APIRouter(prefix="/ticket", tags=["Ticket"])

def get_ticket_service(db: Session = Depends(get_db)):
    return service(db=db)

@router.get("/", response_model=list[TicketGetDTO], summary="Get all")
def get( 
    service: service = Depends(get_ticket_service)):
    try:
        return service.get_all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/{id}", response_model=TicketGetDTO, summary="Get by id")
def get(
    id: int, 
    service: service = Depends(get_ticket_service)):
    try:
        return service.get_by_id(id=id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
@router.post("/", response_model=TicketGetDTO, summary="Create")
def create(
    ticket: TicketCreateDTO, 
    service: service = Depends(get_ticket_service)):
    try:
        service.create(ticket=ticket)
        return Response(status_code=status.HTTP_201_CREATED)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.put("/", response_model=TicketGetDTO, summary="Update")
def update(
    ticket: TicketUpdateDTO, 
    service: service = Depends(get_ticket_service)):
    try:
        return service.update(ticket=ticket)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.delete("/{id}", summary="Delete")
def delete(
    id: int, 
    service: service = Depends(get_ticket_service)):
    try:
        service.delete(id=id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:    
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))