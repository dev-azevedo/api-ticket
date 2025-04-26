from sqlalchemy.orm import Session
from src.DTO.ticket_dto import TicketCreateDTO, TicketGetDTO
from src.models.ticket import Ticket

class TicketService:
    def __init__(self, db: Session):
        self.db = db
        self.query = self.db.query(Ticket)
        
    def get_all(self):
        return self.query.filter_by(active=True).all()
    
    def get_by_id(self, id): 
        ticket = self.query.filter_by(id=id, active=True).first()
        
        if not ticket:
            raise Exception(f"Ticket with id {id} not found")
        
        return ticket
    
    def create(self, ticket: TicketCreateDTO):
        ticket_format = Ticket(name_user=ticket.name_user, title=ticket.title, description=ticket.description)
        self.db.add(ticket_format)
        self.db.commit()
        self.db.refresh(ticket_format)  # Refresh to get the generated ID
    
        # Return as TicketGetDTO with the ID
        return TicketGetDTO(
            id=ticket_format.id,
            name_user=ticket_format.name_user,
            title=ticket_format.title,
            description=ticket_format.description
        )
    
    def update(self, ticket): 
        ticket_on_db = self.get_by_id(ticket.id)
        
        ticket_on_db.name_user = ticket.name_user
        ticket_on_db.title = ticket.title
        ticket_on_db.description = ticket.description
        ticket_on_db.status = ticket.status
        
        self.db.commit()
        self.db.refresh(ticket_on_db)  # Refresh to get the updated data
        
        return TicketGetDTO(
            id=ticket_on_db.id,
            name_user=ticket_on_db.name_user,
            title=ticket_on_db.title,
            description=ticket_on_db.description
        )
        
    def delete(self, id): 
        ticket_on_db = self.get_by_id(id)
        ticket_on_db.active = False
        
        self.db.commit()
        