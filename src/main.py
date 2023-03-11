from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from src.config.database import SessionLocal

from src.app.routers import routes


app = FastAPI(title="FastFlow")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router=routes)
