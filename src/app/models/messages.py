from src.config.database import Base

from src.app.models.user import User

from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text


class Message(Base):
    __tablename__ = "message"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)

    user = Column(Integer, ForeignKey("ff_user.id"))
    server_room = Column(Integer, ForeignKey("server_message_room.id"))

    content = Column(Text)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    rel_user = relationship("User", foreign_keys=[user])
    rel_server_room = relationship("ServerMessageRoom", foreign_keys=[server_room])

    def __repr__(self):
        return f"<Message name: {self.content}>"
