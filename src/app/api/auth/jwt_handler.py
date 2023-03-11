import time
import jwt

from src.config.security import JWT_ALGORITHM, JWT_SECRET


async def token_response(token: str):
    return {"access token": token}


async def signJWT(email: str):
    payload = {
        "userEmail": email,
        "expiry": time.time() + 600,
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