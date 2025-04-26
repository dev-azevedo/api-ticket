from models.ticket import Ticket
from infra.database_config import engine

def create_tables():
    Ticket.Base.metadata.create_all(engine)