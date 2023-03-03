from src.config.database import Base

from sqlalchemy.sql import func
from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean


class User(Base):
    __tablename__ = "ff_user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)

    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    about = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User: {self.username}>"
