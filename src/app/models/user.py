from src.config.database import Base

from sqlalchemy.sql import func
from sqlalchemy import (
    Column, 
    String, 
    Integer, 
    Text, 
    DateTime,
    Boolean
    )


class FastFlowUser(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, nullable=False, index=True, unique=True)

    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    about_me = Column(Text)

    date_joined = Column(DateTime(timezone=True), server_default=func.now())
    
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'