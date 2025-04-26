from fastapi import FastAPI
from src.infra.create_tables import create_tables
from src.routes.ticket_route import router


create_tables()

app = FastAPI(
    title="API Tickets",
    description="API para gerenciamento de tickets",
    varsion="0.1.0",
    contact={
        "name": "Jhonatan Azevedo",
        "email": "dev.azevedo@outlook.com",
    },
)

app.include_router(router)