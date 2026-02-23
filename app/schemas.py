from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    details: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int
    createdAt: datetime
    updatedAt: Optional[datetime] = None
    completed: bool

    class Config:
        from_attributes = True
