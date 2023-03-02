from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    username: str
    email: str
    about: str
    created_at: datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool


class UserList(UserBase):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
