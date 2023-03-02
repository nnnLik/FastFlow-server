from sqlalchemy.orm import Session

from src.app.models.user import User


async def get_user_list(db: Session):
    return db.query(User).all()
