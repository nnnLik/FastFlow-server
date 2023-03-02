from src.config.database import Base

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String


class Server(Base):
    __tablename__ = "server"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)

    server_name = Column(String(50), nullable=False)

    created_by = Column(Integer, ForeignKey("ff_user.id"))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    rel_created_by = relationship("User", foreign_keys=[created_by])

    def __repr__(self):
        return f"<Server name: {self.server_name}>"
