from fastapi import APIRouter

from src.app.api.user.user_api import router as user_api


routes = APIRouter()

routes.include_router(
    user_api,
    prefix="/user",
    tags=[
        "user",
    ],
)
