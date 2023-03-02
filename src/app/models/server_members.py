from src.config.database import Base

from src.app.models.user import User
from src.app.models.server import Server

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
)


class ServerMembers(Base):
    __tablename__ = "server_members"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)

    server = Column(Integer, ForeignKey("server.id"))
    user = Column(Integer, ForeignKey("ff_user.id"))

    joined_at = Column(DateTime(timezone=True), server_default=func.now())
    left_at = Column(DateTime(timezone=True), nullable=True, default=None)

    rel_user = relationship("User", foreign_keys=[user])
    rel_server = relationship("Server", foreign_keys=[server])

    def __repr__(self):
        return f"<ServerMembers user: {self.user} ServerMember: {self.user}>"
