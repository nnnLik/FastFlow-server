from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    about: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class AllUsers(UserBase):
    pass

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    about: Optional[str] = None
