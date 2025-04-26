from sqlalchemy.orm import Session
from models.ticket import Ticket

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
    
    def create(self, ticket):
        self.db.add(ticket)
        self.db.commit()
        return ticket
    
    def update(self, ticket): 
        ticket_on_db = self.get_by_id(ticket.id)
        
        ticket_on_db.name_user = ticket.name_user
        ticket_on_db.title = ticket.title
        ticket_on_db.description = ticket.description
        ticket_on_db.status = ticket.status
        
        self.db.commit()
        return ticket_on_db
        
        
    def delete(self, id): 
        ticket_on_db = self.get_by_id(id)
        ticket_on_db.active = False
        
        self.db.commit()
        