from pydantic import BaseModel, field_validator

from src.enum.ticket_status_enum import ETicketStatus

class TicketBaseDTO(BaseModel):
    name_user: str
    title: str
    description: str
    status: int
    
   
class TicketCreateDTO(TicketBaseDTO):
    
    @field_validator("status")
    def validate_status(cls, value):
        if value not in ETicketStatus:
            raise ValueError("Status must be one of the following: 1(OPEN), 2(CLOSED), 3(PENDING)")

        return value
    
    @field_validator("name_user")
    def validate_name_use(cls, value):
        if len(value) < 3:
            raise ValueError("Name, Title and Description must be at least 3 characters")
        
        return value
    
    @field_validator("title")
    def validate_title(cls, value):
        if len(value) < 3:
            raise ValueError("Name, Title and Description must be at least 3 characters")
        
        return value
    
    @field_validator("description")
    def validate_description(cls, value):
        if len(value) < 3:
            raise ValueError("Name, Title and Description must be at least 3 characters")
        
        return value
    
    

class TicketUpdateDTO(TicketBaseDTO):
    id: int
    pass

class TicketGetDTO(TicketBaseDTO):
    id: int
    status_name: ETicketStatus(status).name # type: ignore
    pass