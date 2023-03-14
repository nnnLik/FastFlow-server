from src.app.api.server.service import get_user_servers
from src.app.api.server.service import delete_server
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.schemas.server_schemas import ServerCreateSchemas

from src.config.utils import get_db

from src.app.api.auth.jwt_bearer import JWTBearer
from src.app.api.auth.jwt_handler import get_current_user

from src.app.api.server.service import create_server
from src.app.models.user import User


router = APIRouter()


@router.get("/user/{user_id}", dependencies=[Depends(JWTBearer)])
async def user_servers(
    user_id: int,
    db: Session = Depends(get_db)
):
    servers = get_user_servers(db, user_id)
    return {"servers": servers}

@router.post(
    "/", dependencies=[Depends(JWTBearer())]
)
async def post_server(
    server: ServerCreateSchemas,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_server(db=db, server=server, created_by=current_user)

@router.delete("/servers/{server_id}")
def delete_server_handler(server_id: int, db: Session = Depends(get_db)):
    return delete_server(db, server_id)