from pydantic import BaseModel, field_validator

from src.enum.ticket_status_enum import ETicketStatus

class TicketBaseDTO(BaseModel):
    name_user: str
    title: str
    description: str
   
class TicketCreateDTO(TicketBaseDTO):
    pass

class TicketUpdateDTO(TicketBaseDTO):
    id: int
    status: int
    pass

class TicketGetDTO(TicketBaseDTO):
    id: int
    pass