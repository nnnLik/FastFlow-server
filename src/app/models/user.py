from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable

from src.config.database import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean


# class User(Base):
#     __tablename__ = "user"

#     id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)

#     username = Column(String(50), unique=True, nullable=False)
#     email = Column(String(120), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)

#     about = Column(Text)

#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), server_default=func.now())

#     is_active = Column(Boolean, default=True)
#     is_staff = Column(Boolean, default=False)
#     is_superuser = Column(Boolean, default=False)

#     def __repr__(self):
#         return f'<User: {self.username}>'


class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
