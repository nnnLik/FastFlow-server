from fastapi import HTTPException
from sqlalchemy.orm import Session


from src.app.models.user import User

from src.app.schemas.auth_schemas import LoginUserSchema, UserCreateSchema

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


def is_available_to_create(db: Session, user: User):
    is_exist_by_username = db.query(User).filter(User.username == user.username).first()
    is_exist_by_email = db.query(User).filter(User.email == user.email).first()

    if is_exist_by_username is not None:
        raise HTTPException(status_code=400, detail="Username already registered")
    elif is_exist_by_email is not None:
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        return True


def is_available_to_login(db: Session, user: LoginUserSchema):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not Hash.verify(db_user.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return True


def create(db: Session, user: UserCreateSchema):
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
