from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from src.app.api.auth.jwt_handler import signJWT
from src.app.api.user.service import (
    create,
    is_available_to_create,
    is_available_to_login,
)
from src.app.schemas.auth_schemas import LoginUserSchema, UserCreateSchema

from src.config.utils import get_db


router = APIRouter()


@router.post("/signup", tags=["user", "auth", "signup"], status_code=201)
async def signup(user: UserCreateSchema, db: Session = Depends(get_db)):
    if is_available_to_create(db, user):
        create(db=db, user=user)
    return await signJWT(user.email)


@router.post("/login", tags=["user", "auth", "login"], status_code=200)
async def login(user: LoginUserSchema, db: Session = Depends(get_db)):
    if is_available_to_login(db, user):
        return await signJWT(user.email)
    else:
        return {"error": "Invalid login details"}
