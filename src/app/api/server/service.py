from src.app.models.server_members import ServerMembers
from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from src.app.schemas.server_schemas import ServerCreateSchemas

from src.app.models.server import Server


def get_user_servers(db: Session, user_id: int):
    return db.query(Server).join(ServerMembers).filter(ServerMembers.user == user_id).all()
    
def check_server_limit(db: Session, created_by: int):
    server_count = db.query(Server).filter(Server.created_by == created_by).count()
    if server_count >= 5:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have reached the limit of servers you can create."
        )

def check_server_name(db: Session, server_name: str, created_by: int):
    if db.query(Server).filter(Server.server_name == server_name, Server.created_by == created_by).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"You already have a server with name '{server_name}'"
        )

def add_user_to_server(db: Session, server_id: int, user_id: int):
    server_member = ServerMembers(server=server_id, user=user_id)
    db.add(server_member)
    db.commit()
    db.refresh(server_member)
    return {"message": "User added to server successfully"}

def create_server(db: Session, server: ServerCreateSchemas, created_by: int):
    check_server_name(db, server.server_name, created_by)
    check_server_limit(db, created_by)
    
    new_server = Server(**server.dict(), created_by=created_by)
    db.add(new_server)
    db.commit()
    db.refresh(new_server)

    add_user_to_server(db, new_server.id, created_by)

    return {"message": "Server created successfully"}

def delete_server(db: Session, server_id: int):
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Server not found")
    db.delete(server)
    db.commit()
    return {"message": "Server deleted successfully"}