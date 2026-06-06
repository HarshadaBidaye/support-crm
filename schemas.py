from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class NoteCreate(BaseModel):
    note_text: str

class NoteOut(BaseModel):
    id: int
    note_text: str
    created_at: datetime

    class Config:
        from_attributes = True

class TicketCreate(BaseModel):
    customer_name: str
    customer_email: str
    subject: str
    description: str

class TicketUpdate(BaseModel):
    status: Optional[str] = None
    note_text: Optional[str] = None

class TicketOut(BaseModel):
    id: int
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    created_at: datetime
    updated_at: datetime
    notes: List[NoteOut] = []

    class Config:
        from_attributes = True