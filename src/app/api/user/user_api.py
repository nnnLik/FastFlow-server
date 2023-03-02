from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.utils import get_db

from .service import get_user_list


router = APIRouter()


@router.get("/")
async def get_list(db: Session = Depends(get_db)):
    users = await get_user_list(db)
    return users


@router.post("/")
async def get_list(db: Session = Depends(get_db)):
    users = await get_user_list(db)
    return users
