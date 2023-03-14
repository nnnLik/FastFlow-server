from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.config.utils import get_db
from src.app.schemas.user_schemas import (
    UserSchema,
    AllUsersSchema,
    UserUpdateSchema,
)

from src.app.api.user.service import (
    delete_user_by_id,
    update_user_by_id,
    user_by_email,
    users,
    user_by_username,
    user_by_id,
)

from src.app.api.auth.jwt_bearer import JWTBearer

router = APIRouter()


@router.get(
    "/", dependencies=[Depends(JWTBearer())], response_model=List[AllUsersSchema]
)
async def all_users(db: Session = Depends(get_db)):
    return users(db)


@router.get(
    "/{user_id}", dependencies=[Depends(JWTBearer())], response_model=UserSchema
)
async def get_user_by_id(user_id: int, db=Depends(get_db)):
    return user_by_id(db, user_id=user_id)


@router.get(
    "/name/{username}", dependencies=[Depends(JWTBearer())], response_model=UserSchema
)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return user_by_username(db, username=username)


@router.get(
    "/email/{email}", dependencies=[Depends(JWTBearer())], response_model=UserSchema
)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_by_email(db, email=email)


@router.patch(
    "/{user_id}", dependencies=[Depends(JWTBearer())], response_model=UserSchema
)
async def update_user(
    user_id: int, user_update: UserUpdateSchema, db: Session = Depends(get_db)
):
    return update_user_by_id(db, user_update, user_id)


@router.delete(
    "/{user_id}",
    dependencies=[Depends(JWTBearer())],
)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_by_id(db, user_id)
