from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

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

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True
