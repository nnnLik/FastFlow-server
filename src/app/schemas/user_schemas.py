from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr
    about: Optional[str] = None


class UserSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    is_active: bool
    is_staff: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class AllUsersSchema(UserBaseSchema):
    pass

    class Config:
        orm_mode = True


class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    about: Optional[str] = None
