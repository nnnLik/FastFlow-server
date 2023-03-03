from typing import List

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from src.config.utils import get_db
from src.app.schemas.user_schema import User, AllUsers, UserCreate, UserUpdate

from src.app.api.user.service import (
    check_for_create_user,
    delete_user_by_id,
    update_user_by_id,
    user_by_email,
    users,
    user_by_username,
    user_by_id,
    create,
)


router = APIRouter()


@router.get("/", response_model=List[AllUsers])
async def all_users(db: Session = Depends(get_db)):
    return users(db)


@router.get("/{user_id}", response_model=User)
async def get_user_by_id(user_id: int, db=Depends(get_db)):
    return user_by_id(db, user_id=user_id)


@router.get("/name/{username}", response_model=User)
async def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return user_by_username(db, username=username)


@router.get("/email/{email}", response_model=User)
async def get_user_by_email(email: str, db: Session = Depends(get_db)):
    return user_by_email(db, email=email)


@router.post("/", response_model=User, status_code=201)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    check_for_create_user(db, user)
    return create(db=db, user=user)


@router.patch("/{user_id}", response_model=User)
async def update_user(
    user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)
):
    return update_user_by_id(db, user_update, user_id)


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user_by_id(db, user_id)
