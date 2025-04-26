from src.infra.database_config import engine
from src.models import (ticket)

def create_tables():
    ticket.Base.metadata.create_all(bind=engine)