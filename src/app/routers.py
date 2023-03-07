from fastapi import APIRouter

from src.app.api.user.user_api import router as user_api
from src.app.api.auth.auth_api import router as auth_api

routes = APIRouter()

routes.include_router(
    user_api,
    prefix="/user",
    tags=[
        "user",
    ],
)
routes.include_router(
    auth_api,
    prefix="/auth",
    tags=[
        "auth",
    ],
)
