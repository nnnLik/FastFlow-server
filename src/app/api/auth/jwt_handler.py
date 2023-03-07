import time
import jwt

from src.config.security import JWT_ALGORITHM, JWT_SECRET


async def token_response(token: str):
    return {"access token": token}


async def signJWT(username: str):
    payload = {
        "userID": username,
        "expiry": time.time() + 600,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return await token_response(token)


async def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token["expiry"] >= time.time() else None
    except Exception:
        return {}
