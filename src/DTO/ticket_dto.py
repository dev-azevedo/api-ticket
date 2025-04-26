from pydantic import BaseModel

from src.enum.ticket_status_enum import ETicketStatus

class TicketBaseDTO(BaseModel):
    name_user: str
    title: str
    description: str
    status: int
    
    
class TicketCreateDTO(TicketBaseDTO):
    pass

class TicketUpdateDTO(TicketBaseDTO):
    id: int
    pass

class TicketGetDTO(TicketBaseDTO):
    id: int
    status_name: ETicketStatus(status).name # type: ignore
    pass