from fastapi import HTTPException
from sqlalchemy.orm import Session


from src.app.models.user import User

from src.app.schemas.user_schema import UserCreate, UserUpdate

from src.config.security import Hash


def users(db: Session):
    return db.query(User).all()


def user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user


def user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user


def user_by_email(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user


def check_for_create_user(db: Session, user: User):
    try:
        user_by_username(db, username=user.username)
    except HTTPException:
        pass
    else:
        raise HTTPException(status_code=400, detail="Username already registered")
    try:
        user_by_email(db, email=user.email)
    except HTTPException:
        pass
    else:
        raise HTTPException(status_code=400, detail="Email already registered")


def create(db: Session, user: UserCreate):
    hashed_password = Hash.bcrypt(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        about=user.about,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_by_id(db: Session, user_update: dict, user_id: int):
    db_user = user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    updated_data = user_update.dict(exclude_unset=True)
    for field in updated_data:
        setattr(db_user, field, updated_data[field])
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user_by_id(db: Session, user_id: int):
    db_user = user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.is_active = False
    db.add(db_user)
    db.commit()
    return {"message": "User deactivated"}
