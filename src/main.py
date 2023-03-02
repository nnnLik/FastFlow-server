from fastapi import FastAPI, Request, Response

from src.app.routers import routes
from src.config.database import SessionLocal

app = FastAPI(title="FastFlow")


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal Server Error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(router=routes)
