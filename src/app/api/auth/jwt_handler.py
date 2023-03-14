import time
from typing import Optional

from fastapi import HTTPException, Header, Depends
from sqlalchemy.orm import Session

import jwt

from src.config.security import JWT_ALGORITHM, JWT_SECRET
from src.app.api.user.service import user_by_email
from src.config.utils import get_db


async def token_response(token: str):
    return {"token": token}


async def signJWT(email: str):
    payload = {
        "userEmail": email,
        "expiry": time.time() + 600 * 60,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return await token_response(token)


def decodeJWT(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM], verify=True)
        if payload["expiry"] < time.time():
            return None
        return payload
    except jwt.InvalidTokenError:
        return {}


def get_current_user(
    token: Optional[str] = Header(None), db: Session = Depends(get_db)
):
    if not token:
        raise HTTPException(status_code=401, detail="Not authorized")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_email = payload.get("userEmail")
        user = user_by_email(db, user_email)
        user_id = user.id
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not authorized")
    except:
        raise HTTPException(status_code=401, detail="Not authorized")
    return user_id
