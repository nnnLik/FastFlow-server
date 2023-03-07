from pydantic import BaseModel, EmailStr

from src.app.schemas.user_schemas import UserBaseSchema


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: str


class UserCreateSchema(UserBaseSchema):
    password: str
